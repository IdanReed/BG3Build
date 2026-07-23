//! One-shot migration: `party_plan.json` -> split `content/*.md` files.
//!
//! Run with `bg3 migrate`. It is safe to re-run; it overwrites the generated
//! files. After writing, it re-assembles the plan from the new files and
//! verifies the result is content-identical to the original JSON (modulo the
//! deliberate itemization promotion), so you know nothing was lost.

use std::collections::BTreeSet;
use std::path::Path;

use anyhow::{anyhow, Context, Result};
use serde_json::{json, Map, Value};

use crate::content;

/// kebab-case slug for filenames and stable checkoff ids.
pub fn slug(s: &str) -> String {
    let mut out = String::new();
    let mut prev_dash = false;
    for ch in s.chars() {
        if ch.is_ascii_alphanumeric() {
            out.push(ch.to_ascii_lowercase());
            prev_dash = false;
        } else if !prev_dash && !out.is_empty() {
            out.push('-');
            prev_dash = true;
        }
    }
    out.trim_matches('-').to_string()
}

/// The item name is the text before the first `(` or `:` — whichever comes
/// first. Used only to derive a stable id/label; the full original text is
/// preserved verbatim in `note`, so the promotion is lossless.
fn extract_item_name(s: &str) -> String {
    let paren = s.find('(');
    let colon = s.find(':');
    let cut = match (paren, colon) {
        (Some(p), Some(c)) => p.min(c),
        (Some(p), None) => p,
        (None, Some(c)) => c,
        (None, None) => s.len(),
    };
    let name = s[..cut].trim();
    if name.is_empty() {
        s.trim().to_string()
    } else {
        name.to_string()
    }
}

/// Promote an itemization list from `["str", ...]` to
/// `[{id, item, note}, ...]`. `note` keeps the original string verbatim so the
/// display is unchanged and the migration round-trips exactly.
fn promote_item_list(list: &[Value]) -> Value {
    let mut used: BTreeSet<String> = BTreeSet::new();
    let promoted: Vec<Value> = list
        .iter()
        .enumerate()
        .map(|(i, v)| {
            let s = v.as_str().unwrap_or_default();
            let item = extract_item_name(s);
            let mut id = slug(&item);
            if id.is_empty() {
                id = format!("item-{}", i + 1);
            }
            // De-collide ids within a single act.
            let mut candidate = id.clone();
            let mut n = 2;
            while used.contains(&candidate) {
                candidate = format!("{id}-{n}");
                n += 1;
            }
            used.insert(candidate.clone());
            json!({ "id": candidate, "item": item, "note": s })
        })
        .collect();
    Value::Array(promoted)
}

/// Walk every character build and promote its `itemization.actN` string lists.
fn promote_itemization(characters: &mut Value) {
    let Some(map) = characters.as_object_mut() else { return };
    for (_nick, builds) in map.iter_mut() {
        let Some(arr) = builds.as_array_mut() else { continue };
        for build in arr.iter_mut() {
            let Some(it) = build.get_mut("itemization").and_then(|v| v.as_object_mut()) else {
                continue;
            };
            for (_act, list) in it.iter_mut() {
                if let Some(strings) = list.as_array() {
                    // Only promote if the entries are strings (idempotent: skip
                    // already-promoted object lists).
                    if strings.iter().all(|e| e.is_string()) && !strings.is_empty() {
                        *list = promote_item_list(strings);
                    }
                }
            }
        }
    }
}

/// Reverse of `promote_itemization`: replace `{id,item,note}` with `note` so an
/// assembled plan can be compared to the original string-based JSON.
fn normalize_itemization(value: &mut Value) {
    let Some(chars) = value.get_mut("characters").and_then(|v| v.as_object_mut()) else {
        return;
    };
    for (_nick, builds) in chars.iter_mut() {
        let Some(arr) = builds.as_array_mut() else { continue };
        for build in arr.iter_mut() {
            let Some(it) = build.get_mut("itemization").and_then(|v| v.as_object_mut()) else {
                continue;
            };
            for (_act, list) in it.iter_mut() {
                if let Some(entries) = list.as_array() {
                    if entries.iter().any(|e| e.is_object()) {
                        let strings: Vec<Value> = entries
                            .iter()
                            .map(|e| {
                                e.get("note")
                                    .cloned()
                                    .unwrap_or_else(|| e.clone())
                            })
                            .collect();
                        *list = Value::Array(strings);
                    }
                }
            }
        }
    }
}

fn md_document(front: &Value, body: &str) -> Result<String> {
    let yaml = serde_yaml::to_string(front).context("serializing front matter to YAML")?;
    // serde_yaml already ends with a newline.
    Ok(format!("---\n{yaml}---\n\n{body}"))
}

fn write_md(path: &Path, front: &Value, body: &str) -> Result<()> {
    let doc = md_document(front, body)?;
    std::fs::write(path, doc).with_context(|| format!("writing {}", path.display()))?;
    println!("  wrote {}", path.display());
    Ok(())
}

pub fn run(root: &Path) -> Result<()> {
    let src = root.join("party_plan.json");
    let raw = std::fs::read_to_string(&src)
        .with_context(|| format!("reading {}", src.display()))?;
    let mut plan: Value =
        serde_json::from_str(&raw).with_context(|| format!("parsing {}", src.display()))?;
    let obj = plan
        .as_object_mut()
        .ok_or_else(|| anyhow!("party_plan.json root is not an object"))?;

    let content_dir = root.join("content");
    let chars_dir = content_dir.join("characters");
    std::fs::create_dir_all(&chars_dir)
        .with_context(|| format!("creating {}", chars_dir.display()))?;

    println!("Migrating party_plan.json -> content/ ...");

    // Simple single-object sections.
    write_md(&content_dir.join("meta.md"), obj.get("meta").unwrap_or(&Value::Null), "")?;
    write_md(&content_dir.join("party.md"), obj.get("party").unwrap_or(&Value::Null), "")?;
    write_md(
        &content_dir.join("proficiencies.md"),
        obj.get("proficiencies").unwrap_or(&Value::Null),
        "",
    )?;
    write_md(&content_dir.join("tadpole.md"), obj.get("tadpole").unwrap_or(&Value::Null), "")?;

    // loot_guide -> wrapped so the file is self-describing.
    let loot_front = json!({ "loot_guide": obj.get("loot_guide").cloned().unwrap_or(Value::Null) });
    write_md(&content_dir.join("loot.md"), &loot_front, "")?;

    // Characters: promote itemization, then one file per nickname.
    let mut characters = obj
        .get("characters")
        .cloned()
        .ok_or_else(|| anyhow!("party_plan.json has no `characters`"))?;
    promote_itemization(&mut characters);
    let cmap = characters
        .as_object()
        .ok_or_else(|| anyhow!("`characters` is not an object"))?;
    for (nick, builds) in cmap {
        let mut front = Map::new();
        front.insert("nickname".into(), Value::String(nick.clone()));
        front.insert("builds".into(), builds.clone());
        let path = chars_dir.join(format!("{}.md", slug(nick)));
        write_md(&path, &Value::Object(front), "")?;
    }

    // Verify round-trip.
    println!("Verifying round-trip ...");
    let mut assembled = content::assemble_from_content(&content_dir)
        .context("re-assembling from freshly written content/")?;
    normalize_itemization(&mut assembled);

    let original: Value = serde_json::from_str(&raw)?;
    if assembled == original {
        println!("OK: assembled plan is content-identical to party_plan.json (itemization promoted, everything else preserved).");
    } else {
        report_diff(&original, &assembled);
        return Err(anyhow!(
            "round-trip mismatch — content/ does NOT reproduce party_plan.json; see diff above"
        ));
    }

    println!("\nDone. The server now serves /api/plan from content/. \
        party_plan.json is left in place as a backup.");
    Ok(())
}

/// Best-effort structural diff to point at the first divergence.
fn report_diff(a: &Value, b: &Value) {
    fn walk(path: &str, a: &Value, b: &Value, hits: &mut Vec<String>) {
        if hits.len() >= 20 {
            return;
        }
        match (a, b) {
            (Value::Object(oa), Value::Object(ob)) => {
                let mut keys: BTreeSet<&String> = oa.keys().collect();
                keys.extend(ob.keys());
                for k in keys {
                    match (oa.get(k), ob.get(k)) {
                        (Some(va), Some(vb)) => walk(&format!("{path}/{k}"), va, vb, hits),
                        (Some(_), None) => hits.push(format!("{path}/{k}: only in original")),
                        (None, Some(_)) => hits.push(format!("{path}/{k}: only in assembled")),
                        (None, None) => {}
                    }
                }
            }
            (Value::Array(aa), Value::Array(ab)) => {
                if aa.len() != ab.len() {
                    hits.push(format!(
                        "{path}: array length {} (original) vs {} (assembled)",
                        aa.len(),
                        ab.len()
                    ));
                }
                for (i, (va, vb)) in aa.iter().zip(ab.iter()).enumerate() {
                    walk(&format!("{path}[{i}]"), va, vb, hits);
                }
            }
            _ => {
                if a != b {
                    hits.push(format!("{path}: value differs"));
                }
            }
        }
    }
    let mut hits = Vec::new();
    walk("", a, b, &mut hits);
    eprintln!("Round-trip differences (first {}):", hits.len());
    for h in hits {
        eprintln!("  {h}");
    }
}
