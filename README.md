# BG3 Party Guide

A local, single-user web guide for a Baldur's Gate 3 party plan. Content lives in
per-character / per-section Markdown files; a small Rust server assembles them and
serves an interactive page where you can **check off levels and items** as you play.

## Run it

```sh
cargo run            # serves http://127.0.0.1:8787
```

Then open <http://127.0.0.1:8787> in a browser. `Ctrl-C` to stop.
Set a different port with `BG3_PORT`, e.g. `BG3_PORT=9000 cargo run`.

For a faster binary: `cargo run --release` (or `cargo build --release` then run
`target/release/bg3`).

## How it fits together

```
Browser (index.html — vanilla JS, accessible tabs and item tooltips)
   │  GET  /api/plan      → merged guide JSON
   │  GET  /api/progress  → checkoff state
   │  POST /api/progress  → toggle one checkoff → written to disk
   ▼
Rust server (axum, 127.0.0.1 only — no auth, no TLS, nothing off-box)
   ├─ assembles /api/plan from content/*.md  (YAML frontmatter → JSON)
   └─ reads/writes progress.json
```

Because it binds to loopback and is single-user, there is no security or scaling
surface to worry about.

## Files

| Path | What it is |
|---|---|
| `content/meta.md` | Title, mode, patch, assumptions. |
| `content/party.md` | Roster, synergies, combat gameplan, item allocation, progression, watch-outs, skills. |
| `content/proficiencies.md` | Skill/save coverage matrix. |
| `content/loot.md` | The act-by-act loot guide (`loot_guide`). |
| `content/tadpole.md` | Illithid-powers plan. |
| `content/characters/*.md` | One file per character (`charles`, `asterion`, `gale`, `bonbon`). Each holds `nickname` + a `builds` array. |
| `progress.json` | Your checkoffs (`{ "checked": { key: true } }`). **Git-tracked** — your playthrough progress shows up as a clean diff. |
| `index.html` | The UI. Served as a static file by the server. |
| `src/` | The Rust server (`main.rs`, `content.rs`, `progress.rs`). |
| `ITEMIZATION-CHANGELOG.md` | Why each gear decision was made, and the defence for every departure from the ranked video guides. Not loaded by the app. |
| `tools/check_itemization.py` | Slot-coverage check for `content/characters/*.md`. |

## Editing the guide

Edit the `content/*.md` files directly — they open cleanly in Obsidian (the
frontmatter shows as Properties). Each `GET /api/plan` re-reads from disk, so just
**refresh the browser** to see changes; no rebuild, no server restart.

Character files look like:

```markdown
---
nickname: Charles
builds:
  - name: The Three Booms
    role: Melee crit-smite nova frontline
    class: Oathbreaker Paladin 7 / Hexblade Warlock 5
    leveling:
      - { char_level: 2, class: Paladin 1, gains: Lay on Hands }
      # ...
    itemization:
      act1:
        - id: early-pact-weapon
          item: Early pact-bound weapon
          slot: weapons
          note: "Bind the best available weapon so it attacks with Charisma."
---
```

Each itemization entry has a stable `id`, display `item`, equipment `slot`, and
`note`. The UI groups entries by act and slot, showing the note in the item's
hover/focus tooltip. Keep IDs stable when renaming an item so existing checkoffs
survive content edits.

Alongside `act1`/`act2`/`act3`, each character carries a `progression` key that lists
every equipment slot once with its Act 1 → 2 → 3 chain. The UI renders it as a fourth
tab. After editing itemization, run:

```sh
python3 tools/check_itemization.py
```

It mirrors the slot vocabulary in `index.html` and reports any character-act missing a
slot, plus any `slot:` value the UI would silently bucket under "Other".

## Checkoffs

Checkboxes appear on:

- **Leveling** tables (per character level).
- **Itemization** lists (per character build, per act).
- **Loot guide** tables (per act / area / item).

Keys are stable composite strings so `progress.json` diffs cleanly and survives
edits, e.g.

```
lvl:charles/the-three-booms/main/7
item:charles/the-three-booms/act1/early-pact-weapon
loot:1/emerald-grove/idol-of-silvanus
```

To reset progress, empty the file: `{ "version": 1, "checked": {} }`.

## Dev note

The Rust toolchain here is 1.82, so `Cargo.lock` pins `indexmap`/`hashbrown` to
versions that predate the edition-2024 requirement. If you upgrade Rust past ~1.85
you can unpin them (`cargo update`).
