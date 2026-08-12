//! Checkoff state persisted to `progress.json` (git-trackable).
//!
//! The file is a flat `key -> true` map so a playthrough shows up as a clean
//! `git diff`. Keys are stable composite strings minted by the frontend, e.g.
//! `lvl:Durc/The Three Booms/main/7` or `loot:1/emerald-grove/everburn-blade`.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};
use std::sync::Mutex;

use anyhow::{Context, Result};
use serde::{Deserialize, Serialize};

/// On-disk shape of `progress.json`.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Progress {
    pub version: u32,
    /// Only checked keys are stored (unchecked = absent), so the file stays small.
    pub checked: BTreeMap<String, bool>,
}

impl Default for Progress {
    fn default() -> Self {
        Progress {
            version: 1,
            checked: BTreeMap::new(),
        }
    }
}

/// Thread-safe handle around the progress file. Cloneable via `Arc` in state.
pub struct ProgressStore {
    path: PathBuf,
    inner: Mutex<Progress>,
}

impl ProgressStore {
    /// Load `progress.json` from `root`, or start empty if it doesn't exist yet.
    pub fn load(root: &Path) -> Result<Self> {
        let path = root.join("progress.json");
        let inner = if path.exists() {
            let raw = std::fs::read_to_string(&path)
                .with_context(|| format!("reading {}", path.display()))?;
            serde_json::from_str(&raw)
                .with_context(|| format!("parsing {} as progress JSON", path.display()))?
        } else {
            Progress::default()
        };
        Ok(ProgressStore {
            path,
            inner: Mutex::new(inner),
        })
    }

    /// Snapshot the current state (for `GET /api/progress`).
    pub fn snapshot(&self) -> Progress {
        self.inner.lock().unwrap().clone()
    }

    /// Toggle one key and persist. `checked == false` removes the key.
    /// Returns the JSON that was written so callers can log/verify.
    pub fn set(&self, key: &str, checked: bool) -> Result<()> {
        // Keep mutation, serialization, and the atomic replace in one critical
        // section. Otherwise two quick POSTs can both use progress.json.tmp and
        // an older snapshot can overwrite a newer one.
        let mut guard = self.inner.lock().unwrap();
        let previous = guard.checked.get(key).copied();
        if checked {
            guard.checked.insert(key.to_string(), true);
        } else {
            guard.checked.remove(key);
        }
        let serialized = serde_json::to_string_pretty(&*guard)?;
        if let Err(error) = self.write_atomic(&serialized) {
            // Keep GET /api/progress consistent with the last durable snapshot.
            match previous {
                Some(value) => {
                    guard.checked.insert(key.to_string(), value);
                }
                None => {
                    guard.checked.remove(key);
                }
            }
            return Err(error);
        }
        Ok(())
    }

    /// Write via temp-file + rename so a crash mid-write can't corrupt the file.
    fn write_atomic(&self, contents: &str) -> Result<()> {
        let tmp = self.path.with_extension("json.tmp");
        std::fs::write(&tmp, contents).with_context(|| format!("writing {}", tmp.display()))?;
        std::fs::rename(&tmp, &self.path)
            .with_context(|| format!("renaming {} -> {}", tmp.display(), self.path.display()))?;
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::ProgressStore;
    use std::sync::Arc;
    use std::time::{SystemTime, UNIX_EPOCH};

    #[test]
    fn concurrent_updates_are_all_persisted() {
        let unique = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_nanos();
        let root =
            std::env::temp_dir().join(format!("bg3-progress-test-{}-{unique}", std::process::id()));
        std::fs::create_dir_all(&root).unwrap();

        let store = Arc::new(ProgressStore::load(&root).unwrap());
        let handles: Vec<_> = (0..16)
            .map(|index| {
                let store = Arc::clone(&store);
                std::thread::spawn(move || {
                    store.set(&format!("item:test/{index}"), true).unwrap();
                })
            })
            .collect();
        for handle in handles {
            handle.join().unwrap();
        }

        let on_disk = ProgressStore::load(&root).unwrap().snapshot();
        assert_eq!(on_disk.checked.len(), 16);
        assert!(on_disk.checked.values().all(|checked| *checked));

        drop(store);
        std::fs::remove_dir_all(root).unwrap();
    }
}
