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
Browser (src/ui/index.html — vanilla JS, accessible tabs and item tooltips)
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
| `content/locations/*.md` | One file per place the party visits: items with where/how, quests, lockouts, people. Behind the Locations tab. |
| `content/route.md` | The order the party visits those places, with cutoffs and a gold table. The Route page at the top of the Locations tab; each location page lists its own stops. |
| `content/ratings.md` | **Generated.** Every item rating read out of the guide corpus, behind the Ratings tab. Rebuilt by `tools/build_ratings_page.py`; delete it and the tab disappears. |
| `content/characters/*.md` | One file per character (`charles`, `asterion`, `gale`, `bonbon`). Each holds `nickname` + a `builds` array. |
| `progress.json` | Your checkoffs (`{ "checked": { key: true } }`). **Git-tracked** — your playthrough progress shows up as a clean diff. |
| `src/` | All application source: the Rust server (`main.rs`, `content.rs`, `progress.rs`) and the UI at `src/ui/index.html`. |
| `resources/` | Raw source material — `videos/{transcripts,summaries}/`, `reddit/`, `wiki/`, and the extracted `tiers/` datasets the tools read. |
| `docs/` | Reasoning and decisions. Never displayed by the app. `itemization-changelog.md` defends every gear choice and every departure from the ranked video guides; `goals.md` holds the party goals; `extraction-brief.md` explains how a transcript becomes a tier table; `act2-route.md` is the Act 2 quest order, linked from the header chip. |
| `tools/check_itemization.py` | Slot-coverage check for `content/characters/*.md`. |
| `tools/build_ratings_page.py` | Rebuilds `content/ratings.md` from `resources/tiers/item_tiers.json`. |
| `tools/apply_spell_tiers.py` | Writes `resources/tiers/spell_tiers.json` into the `spells` blocks of `content/characters/*.md`. |

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

Each leveling row separates what the level hands over from what you choose:
`gains` is automatic, and a `recommendations` entry can carry `picks: N` (how
many selections that level opens — the UI renders an "open pick" placeholder for
any the guide has not assigned yet), `granted: true` (supplied free by the class,
subclass or race, spending no pick and no prepared slot), and `optional: true`
(the level-up replacement swap). A spell in the `spells` panel can carry
`source: granted` to earn the same "Free" badge there.

Each itemization entry has a stable `id`, display `item`, equipment `slot`, and
`note`. The UI groups entries by act and slot, showing the note in the item's
hover/focus tooltip. Keep IDs stable when renaming an item so existing checkoffs
survive content edits.

An entry may also carry ratings from the guide corpus, which render as coloured
badges next to the item name: `tier`/`tier_note` for its letter tier within its
own slot, and `rank`/`rank_note` for its placing in that act's top-20 countdown.
An item often has both. These are generated from `resources/tiers/item_tiers.json`:

```sh
python tools/fetch_transcripts.py PLgTVc5Jd2rrLPuc3vE6XqK65QQboFfolP  # get transcripts
python tools/dump_tier_verdicts.py --slot Rings                       # read the verdicts
python tools/apply_item_tiers.py                                      # write to content
```

Edit the dataset and re-run the applier rather than hand-editing a badge — it
strips and rewrites every field it manages. See `AGENTS.md` for the rules on what
may be recorded.

Spells and cantrips carry the same `tier`/`tier_note` pair, read from the spell
tier lists instead of the gear ones, and every card in the Spells panel badges its
entries the same way. There is no `rank` on a spell: that series runs no top-20
countdown. They are generated from `resources/tiers/spell_tiers.json`:

```sh
python tools/merge_spell_tiers.py   # resources/tiers/spells/*.json → resources/tiers/spell_tiers.json
python tools/apply_spell_tiers.py   # write to content
```

The two appliers own different regions of the same files — `apply_spell_tiers.py`
only touches lines inside a build's `spells:` block and `apply_item_tiers.py` only
touches lines outside it — so either can be re-run alone without dropping the
other's ratings.

## The Locations tab

`content/locations/*.md` is one page per place (the Crèche and every Act 2
location so far), and `content/route.md` is the order the party visits them. The
Route page lists every stop with its cutoffs; a location page shows its own stops
with the place before and after each, so a place the route leaves and comes back
to reads as two visits. Item ticks on a location page use `place:<slug>/<id>` keys
and are linked to the Loot tab and the character pages by item name. Delete the
directory and the tab disappears. Schema: the "Location guides" section of
`AGENTS.md`.

## The Ratings tab

The character pages badge only the party's own gear. The **Ratings** tab is the
whole corpus: every item any tier list rated, by item type, then by the act whose
list rated it, sorted best-first inside each letter. Each row carries the verdict
in one clause and a timestamp link into the video it came from, and gear that is
already in the party's plan gets a chip naming who wears it. The Overview page
tracks what has and has not been read yet.

It is generated, so rebuild it whenever the dataset grows:

```sh
python tools/merge_slot_tiers.py        # resources/tiers/slots/*.json → resources/tiers/item_tiers.json
python tools/build_ratings_page.py      # resources/tiers/item_tiers.json → content/ratings.md
```

Without `content/ratings.md` the server serves no `ratings` and the tab is simply
not shown, which keeps the rest of the guide usable mid-extraction.

Alongside `act1`/`act2`/`act3`, each character carries a `progression` key that lists
every equipment slot once with its Act 1 → 2 → 3 chain. The UI renders it as a fourth
tab. After editing itemization, run:

```sh
python3 tools/check_itemization.py
```

It mirrors the slot vocabulary in `src/ui/index.html` and reports any character-act missing a
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
