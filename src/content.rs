//! Assembles the merged plan JSON the frontend consumes at `GET /api/plan`.
//!
//! Two sources, picked automatically:
//!   * If `content/meta.md` exists -> assemble from the split Markdown files.
//!   * Otherwise -> read the legacy monolithic `party_plan.json` verbatim.
//!
//! This lets the same binary serve Phase 1 (before migration) and Phase 2
//! (after `bg3 migrate` has written the `content/` tree).

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
    let data: Value =
        serde_yaml::from_str(yaml).context("parsing YAML front matter into JSON")?;
    Ok(Doc { data, body })
}

fn read_doc(path: &Path) -> Result<Doc> {
    let raw = std::fs::read_to_string(path)
        .with_context(|| format!("reading {}", path.display()))?;
    parse_frontmatter(&raw).with_context(|| format!("in {}", path.display()))
}

/// Load the plan by assembling it from the split `content/*.md` files.
pub fn load_plan(root: &Path) -> Result<Value> {
    let content_dir = root.join("content");
    assemble_from_content(&content_dir)
        .with_context(|| format!("assembling plan from {}", content_dir.display()))
}

/// Assemble the top-level `{meta, party, proficiencies, characters, loot_guide,
/// tadpole}` object from the split Markdown files.
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

    // Characters: one file each under content/characters/, keyed by `nickname`.
    let mut chars: Vec<(String, Value)> = Vec::new();
    let cdir = dir.join("characters");
    for entry in std::fs::read_dir(&cdir)
        .with_context(|| format!("reading {}", cdir.display()))?
    {
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
    chars.sort_by_key(|(nick, _)| {
        roster_order
            .iter()
            .position(|r| r == nick)
            .unwrap_or(usize::MAX)
    });

    let mut characters = Map::new();
    for (nick, builds) in chars {
        characters.insert(nick, builds);
    }

    let mut root = Map::new();
    root.insert("meta".into(), meta);
    root.insert("party".into(), party);
    root.insert("proficiencies".into(), proficiencies);
    root.insert("characters".into(), Value::Object(characters));
    root.insert("loot_guide".into(), loot_guide);
    root.insert("tadpole".into(), tadpole);
    Ok(Value::Object(root))
}
