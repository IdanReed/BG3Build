---
title: BG3 Party Plan — Booms, Loot, Shock & Command
mode: non-Honour
mode_note: Everything (builds, item interactions, damage numbers) assumes non-Honour. Several novas depend on non-Honour rules (Deepened Pact Extra-Attack stacking; Savage Attacker rerolling smite/rider dice); in Honour mode they shrink substantially.
stat_assumption: Every party member is assumed to get a Hag's Hair (+1) and a Mirror of Loss (+2) on their primary ability, reaching the 20 cap (17 → 18 → 20) without a feat. Hag's Hair is normally one per playthrough; this assumes a per-character source.
patch: 'Patch 8 (2025-04-15) + hotfixes #30–#36; Patch 8 was the final major patch.'
data_model: 'The content/ directory is the SINGLE SOURCE OF TRUTH: one Markdown-with-YAML-frontmatter file per section (meta, party, proficiencies, loot, tadpole) plus one per character under content/characters/. The Rust server (cargo run, binary `bg3`) assembles these into /api/plan and serves index.html at http://127.0.0.1:8787. Checkoff state (levels/items) persists to progress.json, which is git-tracked, via /api/progress. party_plan.json + build.mjs + the embedded <script id=party-data> block are the frozen pre-migration backup and file:// fallback; they are no longer authoritative. Re-run `bg3 migrate` only to regenerate content/ from party_plan.json.'
companion_docs:
- party-review.md
- research/research.md
---

