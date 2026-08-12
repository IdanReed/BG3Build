---
title: BG3 Party Plan — Booms, Loot, Shock & Command
mode: non-Honour
mode_note: Everything (builds, item interactions, damage numbers) assumes non-Honour. Several novas depend on non-Honour rules (Deepened Pact Extra-Attack stacking; Savage Attacker rerolling smite/rider dice); in Honour mode they shrink substantially.
stat_assumption: 'MODDED RUN: the Hag''s Hair mod provides one permanent +1 Hair for every party member. Each character uses it on the build''s stated primary ability (normally 17→18), then uses the Mirror of Loss in Act 3 to reach 20 without an ASI. The vanilla game provides only one Hair.'
patch: 'Patch 8 (2025-04-15) + hotfixes #30–#36; Patch 8 was the final major patch.'
data_model: 'The content/ directory is the SINGLE SOURCE OF TRUTH: one Markdown-with-YAML-frontmatter file per section (meta, party, proficiencies, loot, tadpole) plus one per character under content/characters/. The Rust server (cargo run, binary bg3) assembles these into /api/plan and serves index.html at http://127.0.0.1:8787. Checkoff state (levels/items) persists to progress.json, which is git-tracked, via /api/progress. Edit the content files directly and refresh the browser - there is no build step.'
companion_docs:
- party-review.md
- research/research.md
---
