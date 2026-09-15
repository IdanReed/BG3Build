//! Assembles the merged plan JSON the frontend consumes at `GET /api/plan`.
//!
//! Two sources, picked automatically:
//!   * If `content/meta.md` exists -> assemble from the split Markdown files.
//!   * Otherwise -> read the legacy monolithic `party_plan.json` verbatim.
//!
//! This lets the same binary serve Phase 1 (before migration) and Phase 2
//! (after `bg3 migrate` has written the `content/` tree).

use std::collections::HashSet;
use std::path::Path;

use anyhow::{anyhow, Context, Result};
use serde_json::{Map, Value};

/// Front-matter + body split out of a `.md` source file.
pub struct Doc {
    pub data: Value,
    /// Markdown body after the front matter. Reserved for Phase 3 (freeform
    /// per-character notes rendering); parsed now so the format is stable.
    #[allow(dead_code)]
    pub body: String,
}

/// Split a Markdown file into its YAML front matter (parsed to JSON) and body.
/// Accepts an optional leading BOM and either `\n` or `\r\n` line endings.
pub fn parse_frontmatter(text: &str) -> Result<Doc> {
    let text = text.strip_prefix('\u{feff}').unwrap_or(text);
    let normalized = text.replace("\r\n", "\n");
    let rest = normalized
        .strip_prefix("---\n")
        .ok_or_else(|| anyhow!("file does not start with a `---` front-matter fence"))?;
    let end = rest
        .find("\n---")
        .ok_or_else(|| anyhow!("front matter is not closed by a `---` fence"))?;
    let yaml = &rest[..end];
    // Body starts after the closing fence's line.
    let after = &rest[end + 1..]; // at the closing "---"
    let body = after
        .strip_prefix("---")
        .map(|b| b.trim_start_matches('\n').to_string())
        .unwrap_or_default();
    let data: Value = serde_yaml::from_str(yaml).context("parsing YAML front matter into JSON")?;
    Ok(Doc { data, body })
}

fn read_doc(path: &Path) -> Result<Doc> {
    let raw =
        std::fs::read_to_string(path).with_context(|| format!("reading {}", path.display()))?;
    parse_frontmatter(&raw).with_context(|| format!("in {}", path.display()))
}

/// Load the plan by assembling it from the split `content/*.md` files.
pub fn load_plan(root: &Path) -> Result<Value> {
    let content_dir = root.join("content");
    assemble_from_content(&content_dir)
        .with_context(|| format!("assembling plan from {}", content_dir.display()))
}

/// Assemble the top-level `{meta, party, proficiencies, characters, loot_guide,
/// tadpole}` object from the split Markdown files, plus the optional `ratings`,
/// `locations` and `route` fields when their content exists.
pub fn assemble_from_content(dir: &Path) -> Result<Value> {
    let meta = read_doc(&dir.join("meta.md"))?.data;
    let party = read_doc(&dir.join("party.md"))?.data;
    let proficiencies = read_doc(&dir.join("proficiencies.md"))?.data;
    let tadpole = read_doc(&dir.join("tadpole.md"))?.data;

    // loot.md holds `{ loot_guide: [...] }` so the file is self-describing.
    let loot_doc = read_doc(&dir.join("loot.md"))?.data;
    let loot_guide = loot_doc
        .get("loot_guide")
        .cloned()
        .ok_or_else(|| anyhow!("loot.md front matter is missing `loot_guide`"))?;

    // ratings.md is generated from the guide corpus by
    // `tools/build_ratings_page.py`, so it is optional: a checkout that has not run
    // the generator simply gets no Ratings tab. A file that exists must still be
    // well formed, which catches a half-written generator run.
    let ratings_path = dir.join("ratings.md");
    let ratings = if ratings_path.exists() {
        Some(
            read_doc(&ratings_path)?
                .data
                .get("ratings")
                .cloned()
                .ok_or_else(|| anyhow!("ratings.md front matter is missing `ratings`"))?,
        )
    } else {
        None
    };

    // Characters: one file each under content/characters/, keyed by `nickname`.
    let mut chars: Vec<(String, Value)> = Vec::new();
    let mut nicknames = HashSet::new();
    let cdir = dir.join("characters");
    for entry in std::fs::read_dir(&cdir).with_context(|| format!("reading {}", cdir.display()))? {
        let path = entry?.path();
        if path.extension().and_then(|e| e.to_str()) != Some("md") {
            continue;
        }
        let doc = read_doc(&path)?;
        let nickname = doc
            .data
            .get("nickname")
            .and_then(|v| v.as_str())
            .ok_or_else(|| anyhow!("{}: missing `nickname`", path.display()))?
            .to_string();
        if !nicknames.insert(nickname.clone()) {
            return Err(anyhow!(
                "{}: duplicate character nickname `{nickname}`",
                path.display()
            ));
        }
        let builds = doc
            .data
            .get("builds")
            .cloned()
            .ok_or_else(|| anyhow!("{}: missing `builds`", path.display()))?;
        chars.push((nickname, builds));
    }

    // Order characters by the party roster so the nav matches the intended order;
    // any not listed in the roster fall to the end, alphabetically.
    let roster_order: Vec<String> = party
        .get("roster")
        .and_then(|r| r.as_array())
        .map(|rows| {
            rows.iter()
                .filter_map(|row| row.get("nickname").and_then(|n| n.as_str()))
                .map(String::from)
                .collect()
        })
        .unwrap_or_default();
    chars.sort_by(|(left, _), (right, _)| {
        let left_position = roster_order
            .iter()
            .position(|roster_nick| roster_nick == left)
            .unwrap_or(usize::MAX);
        let right_position = roster_order
            .iter()
            .position(|roster_nick| roster_nick == right)
            .unwrap_or(usize::MAX);
        left_position
            .cmp(&right_position)
            .then_with(|| left.to_lowercase().cmp(&right.to_lowercase()))
    });

    let mut characters = Map::new();
    for (nick, builds) in chars {
        characters.insert(nick, builds);
    }

    // Location guides are optional: no content/locations/ directory means no
    // `locations` field and no Locations tab. A file that exists must parse and
    // carry a unique `slug` and a `name`, because the frontend keys the nav and the
    // checkoffs on the slug. Sorted by act, then `order`, then name.
    let locations = load_locations(&dir.join("locations"))?;

    // route.md orders the locations; it is optional in the same way.
    let route_path = dir.join("route.md");
    let route = if route_path.exists() {
        Some(
            read_doc(&route_path)?
                .data
                .get("route")
                .cloned()
                .ok_or_else(|| anyhow!("route.md front matter is missing `route`"))?,
        )
    } else {
        None
    };

    let mut root = Map::new();
    root.insert("meta".into(), meta);
    root.insert("party".into(), party);
    root.insert("proficiencies".into(), proficiencies);
    root.insert("characters".into(), Value::Object(characters));
    root.insert("loot_guide".into(), loot_guide);
    root.insert("tadpole".into(), tadpole);
    if let Some(ratings) = ratings {
        root.insert("ratings".into(), ratings);
    }
    if !locations.is_empty() {
        root.insert("locations".into(), Value::Array(locations));
    }
    if let Some(route) = route {
        root.insert("route".into(), route);
    }
    Ok(Value::Object(root))
}

/// Read every `content/locations/*.md`, returning an empty list when the
/// directory is absent.
fn load_locations(ldir: &Path) -> Result<Vec<Value>> {
    let mut locations: Vec<Value> = Vec::new();
    if !ldir.is_dir() {
        return Ok(locations);
    }
    let mut slugs = HashSet::new();
    for entry in std::fs::read_dir(ldir).with_context(|| format!("reading {}", ldir.display()))? {
        let path = entry?.path();
        if path.extension().and_then(|e| e.to_str()) != Some("md") {
            continue;
        }
        let doc = read_doc(&path)?;
        let slug = doc
            .data
            .get("slug")
            .and_then(|v| v.as_str())
            .ok_or_else(|| anyhow!("{}: missing `slug`", path.display()))?
            .to_string();
        if !slugs.insert(slug.clone()) {
            return Err(anyhow!(
                "{}: duplicate location slug `{slug}`",
                path.display()
            ));
        }
        if doc.data.get("name").and_then(|v| v.as_str()).is_none() {
            return Err(anyhow!("{}: missing `name`", path.display()));
        }
        locations.push(doc.data);
    }
    let sort_key = |v: &Value| {
        (
            v.get("act").and_then(|x| x.as_i64()).unwrap_or(i64::MAX),
            v.get("order").and_then(|x| x.as_i64()).unwrap_or(i64::MAX),
            v.get("name")
                .and_then(|x| x.as_str())
                .unwrap_or("")
                .to_lowercase(),
        )
    };
    locations.sort_by(|a, b| sort_key(a).cmp(&sort_key(b)));
    Ok(locations)
}

#[cfg(test)]
mod tests {
    use super::{assemble_from_content, parse_frontmatter};
    use std::path::{Path, PathBuf};

    /// A throwaway content tree with the required files, so the optional ones can
    /// be exercised on their own.
    fn scratch_content(tag: &str) -> PathBuf {
        let dir = std::env::temp_dir().join(format!("bg3-content-{tag}-{}", std::process::id()));
        let _ = std::fs::remove_dir_all(&dir);
        std::fs::create_dir_all(dir.join("characters")).unwrap();
        for (name, body) in [
            ("meta.md", "version: 0.0.0"),
            (
                "party.md",
                "roster:
- nickname: Charles",
            ),
            ("proficiencies.md", "skills: []"),
            ("tadpole.md", "characters: []"),
            ("loot.md", "loot_guide: []"),
        ] {
            write_md(&dir.join(name), body);
        }
        write_md(
            &dir.join("characters/charles.md"),
            "nickname: Charles
builds: []",
        );
        dir
    }

    fn write_md(path: &Path, frontmatter: &str) {
        std::fs::write(
            path,
            format!(
                "---
{frontmatter}
---
"
            ),
        )
        .unwrap();
    }

    #[test]
    fn locations_and_route_are_optional() {
        let dir = scratch_content("none");
        let plan = assemble_from_content(&dir).unwrap();
        assert!(plan.get("locations").is_none());
        assert!(plan.get("route").is_none());
        let _ = std::fs::remove_dir_all(&dir);
    }

    #[test]
    fn locations_sort_by_act_then_order_and_route_passes_through() {
        let dir = scratch_content("sorted");
        std::fs::create_dir_all(dir.join("locations")).unwrap();
        write_md(
            &dir.join("locations/b.md"),
            "slug: moonrise-towers
name: Moonrise Towers
act: 2
order: 20",
        );
        write_md(
            &dir.join("locations/a.md"),
            "slug: last-light-inn
name: Last Light Inn
act: 2
order: 10",
        );
        write_md(
            &dir.join("locations/c.md"),
            "slug: creche-yllek
name: Creche
act: 1
order: 99",
        );
        write_md(
            &dir.join("route.md"),
            "route:
- act: 2
  steps: []",
        );

        let plan = assemble_from_content(&dir).unwrap();
        let slugs: Vec<&str> = plan["locations"]
            .as_array()
            .unwrap()
            .iter()
            .map(|l| l["slug"].as_str().unwrap())
            .collect();
        assert_eq!(slugs, ["creche-yllek", "last-light-inn", "moonrise-towers"]);
        assert_eq!(plan["route"][0]["act"], 2);
        let _ = std::fs::remove_dir_all(&dir);
    }

    #[test]
    fn duplicate_location_slugs_are_rejected() {
        let dir = scratch_content("dupe");
        std::fs::create_dir_all(dir.join("locations")).unwrap();
        write_md(
            &dir.join("locations/a.md"),
            "slug: same
name: A
act: 2
order: 1",
        );
        write_md(
            &dir.join("locations/b.md"),
            "slug: same
name: B
act: 2
order: 2",
        );
        let err = assemble_from_content(&dir).err().unwrap();
        assert!(err.to_string().contains("duplicate location slug"));
        let _ = std::fs::remove_dir_all(&dir);
    }

    #[test]
    fn frontmatter_accepts_bom_and_windows_line_endings() {
        let doc = parse_frontmatter(
            "\u{feff}---\r\nnickname: Charles\r\nbuilds: []\r\n---\r\nBody text\r\n",
        )
        .unwrap();

        assert_eq!(doc.data["nickname"], "Charles");
        assert_eq!(doc.body, "Body text\n");
    }

    #[test]
    fn frontmatter_requires_a_closing_fence() {
        let result = parse_frontmatter("---\nnickname: Charles\n");
        assert!(result.is_err());
        let error = result.err().unwrap();
        assert!(error.to_string().contains("not closed"));
    }
}
