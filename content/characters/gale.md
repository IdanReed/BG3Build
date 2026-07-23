---
nickname: Gale
builds:
- name: The Shock Bottle
  is_primary: true
  role: Wet + Lightning AoE nuke + party Haste engine
  class: Sorcerer 10 (Storm Sorcery) / Tempest Cleric 2
  race: Gale (Human)
  race_notes: 'Human (BG3): a freely-assigned +2/+1 ability bonus like every race (the CHA 17 in starting_stats is 15 point-buy + the +2 racial), ''Civil Militia'' proficiency with Shields + Light armour + spear/pike/halberd/glaive (no trident), one extra skill, and +25% carry weight — stat-neutral vs any other race, so it costs nothing. NETHERESE ORB: only an EARLY-Act-1 issue — the 3-item ''The Wizard of Waterdeep'' quest; feed Gale 3 magic items and the hunger resolves (Elminster later quells it entirely). Ignoring it stacks escalating Arcane Hunger debuffs (disadvantage on saves → attacks → half move) and only the final ignored stage is fatal — it is NOT an Act 1–2 resource drain. Recruited as a Wizard; respec via Withers into this Storm Sorcery / Tempest Cleric build.'
  background: Sage (Arcana, History) — Gale's default
  starting_stats:
    STR: 8
    DEX: 14
    CON: 14
    INT: 8
    WIS: 12
    CHA: 17
  stats_note: 'Point-buy base 8/14/14/8/12/15 = all 27 points (14s cost 2 each — set BOTH DEX and CON to 14 in point-buy). Then Human +2 → CHA 17; the +1 racial is a free spare (CON/DEX/WIS — no modifier change, so just bank it on CON). If you see 2 points left, you set a physical to 13 — bump it to 14.'
  ability_targets: CHA 17 → 20 (Hag's Hair + Mirror).
  metamagic:
  - Twinned + Extended (L2)
  - Quickened (L3)
  feats:
  - at: Sorc 4
    feat: War Caster
  - at: Sorc 8
    feat: Alert
    note: 'Swapped from Elemental Adept (redundant — Wet already negates lightning/cold resistance). Alert (+5 initiative, immune to Surprise) fixes the party''s biggest R1 problem: low-DEX Gale must Twinned-Haste the melee BEFORE they act. Haste concentration is already covered by War Caster (Sorc 4).'
  key_spells:
  - Create Water (Storm Spells at Sorc 6; also Tempest dip)
  - Witch Bolt / Lightning Bolt
  - Haste (Twinned)
  - Counterspell
  - Glyph of Warding (scroll only — not a Sorcerer spell)
  creation:
    level1_class: Sorcerer 1 (Storm Sorcery)
    level1_gains: Storm Sorcery subclass; Tempestuous Magic (after casting any levelled spell, Fly 9m as a bonus action with no opportunity attacks) from level 1. Metamagic starts at Sorcerer 2. (No Draconic Resilience AC/HP and no free Witch Bolt — Storm trades durability for mobility + AoE.)
    subclass_choice: Storm Sorcery (Sorcerer 1)
    proficiencies:
      armor_weapons: No armour early — heavy armour + shields arrive with the Tempest dip (11–12).
      saving_throws: CON + CHA (Sorcerer-first).
      skills: Sage (Arcana, History) + 2 Sorcerer picks + Human extra.
    starting_cantrips: 4 at level 1 — Shocking Grasp + utility.
    starting_spells: 'Chromatic Orb: Lightning + Shield; add Witch Bolt at level 2.'
    notes: '2 feats (Sorc 4 + Sorc 8). Create Water comes free at Sorc 6 (Storm Spells); Destructive Wrath from the Tempest 2 dip (11–12). Netherese orb: feed him 3 magic items in early Act 1 — done.'
  spells:
    note: Sorcerer is a KNOWN caster (learn on level-up, replace 1 per level); the Tempest Cleric 2 dip is a prepared caster re-picked freely. Mandatory = the wet-lightning engine + Haste; Recommended = flex nukes and utility.
    mandatory:
    - spell: Witch Bolt
      level: '1'
      school: Evocation
      save: Ranged spell attack
      when: Sorc 2 (learned — Storm grants no free spell)
      why: 1d12 Lightning, Concentration; re-activate each turn with no roll, builds Lightning Charges on The Spellsparkler, and works with Destructive Wrath.
    - spell: 'Chromatic Orb: Lightning'
      level: '1'
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1–3
      why: 2d8 Lightning that creates an Electrified Water surface; upcasts +1d8/level; triggers Destructive Wrath — cheap single-target lightning that sets up the electrify combo.
    - spell: Lightning Bolt
      level: '3'
      school: Evocation
      save: DEX save
      when: Sorc 5
      why: 8d6 Lightning line — the main AoE nuke; doubled vs Wet, maximized by Destructive Wrath, and each cast also fires Heart of the Storm (free Lightning splash to all enemies in 6m, itself doubled by Wet).
    - spell: Haste
      level: '3'
      school: Transmutation
      save: None (Concentration)
      when: Sorc 5
      why: Single-target so Twinnable; Twinned Haste (3 sorcery points) on the Paladin is the party Haste engine. Never cast another Concentration spell after it.
    - spell: Counterspell
      level: '3'
      school: Abjuration
      save: Reaction (no save at equal/higher slot)
      when: Sorc 5
      why: Shuts down enemy casters; upcast to beat higher-level spells without a check.
    - spell: Create or Destroy Water
      level: '1'
      school: Transmutation
      save: None
      when: char 6 (Storm Spells) / char 11 (Tempest dip)
      why: Storm grants this at Sorc 6 (Storm Spells) — self-apply Wet (double Lightning/Cold) without the dip; also available from the Tempest Cleric dip. Applying Wet doubles the whole lightning/cold package. No save, so low WIS is irrelevant.
    - spell: Call Lightning
      level: '3'
      school: Conjuration
      save: DEX save
      when: char 6 (Storm Spells)
      why: 'Storm Spell at Sorc 6: summon a storm cloud (Concentration), then re-fire a bolt as an ACTION each turn with NO further slot — sustained AoE Lightning, doubled by Wet, that triggers Heart of the Storm every turn. Competes with Haste for Concentration, so use it on fights where you aren''t the one Twinned-Hasting.'
    - spell: Destructive Wrath
      level: Channel Divinity (not a spell)
      school: Tempest Domain feature
      save: N/A
      when: char 12 (Tempest Cleric 2)
      why: 'The payoff: spend a Channel Divinity charge to MAXIMISE any Thunder/Lightning roll (Lightning Bolt / Chain Lightning / Markoheshkir bolts / Thunderwave). 1/rest (2 with Amulet of the Devout).'
    recommended:
    - spell: Shocking Grasp
      level: Cantrip
      school: Evocation
      save: Melee spell attack
      when: Sorc 1
      why: 'Best lightning cantrip: 1d8→3d8 by char 10, strips Reactions, advantage vs metal armour; scales with Potent Robe, Spellmight Gloves, Markoheshkir; the War Caster opportunity-spell payload.'
    - spell: Cone of Cold
      level: '5'
      school: Evocation
      save: DEX save
      when: Sorc 9–10
      why: '5d8 Cold AoE; off-element, but Wet gives Cold vulnerability too, so it still doubles.'
    - spell: Fireball
      level: '3'
      school: Evocation
      save: DEX save
      when: Sorc 5+
      why: 8d6 Fire AoE flex for fire-vulnerable or non-Wet packs; off-type (no Heart of the Storm — that only fires on Lightning/Thunder), situational.
    - spell: Misty Step
      level: '2'
      school: Conjuration
      save: None (bonus action)
      when: Sorc 3+
      why: Reposition out of your own electrified water.
    - spell: Thunderwave
      level: '1'
      school: Evocation
      save: CON save
      when: char 11 (Tempest domain, always-prepared)
      why: 'Free domain spell: 2d8 Thunder + knockback; a Thunder roll, so Destructive Wrath maximises it (16 guaranteed) and it triggers Reverberation gear.'
    - spell: Aid
      level: '2'
      school: Abjuration
      save: None
      when: char 12 (Tempest Cleric 2)
      why: Party max-HP buff, no concentration, no save — a strong prepared pick that ignores the low WIS DC.
    - spell: Sleet Storm
      level: '3'
      school: Conjuration
      save: DEX save
      when: char 6 (Storm Spells)
      why: 'Storm Spell at Sorc 6: ice-surface control — enemies inside are blinded and knocked Prone (breaks Concentration), and the ground turns to slippery ice. Off-element for damage, but premier lockdown/utility for a mobile storm caster.'
    - spell: Heart of the Storm
      level: Feature (Storm Sorcery, Sorc 6)
      school: Storm Sorcery feature — Lightning/Thunder
      save: None (automatic)
      when: char 6
      why: 'Passive: whenever you cast a Lightning/Thunder spell of level 1+, all enemies within 6m take (Sorcerer level ÷ 2) Lightning/Thunder — a free AoE splash on every Chromatic Orb: Lightning / Lightning Bolt / Call Lightning, and it is ALSO doubled by Wet. Enemies-only, so no friendly fire from this part.'
    - spell: Chain Lightning
      level: '6'
      school: Evocation
      save: DEX save
      when: Markoheshkir / scroll only (Sorc learns it at class 11, unreached)
      why: 10d8 Lightning — accessed via Markoheshkir (Kereska's Favour / Bolts of Doom, 1/short rest) or scrolls, not learned at Sorc 10.
    - spell: Glyph of Warding
      level: '3'
      school: Abjuration
      save: DEX save
      when: scroll only for this build
      why: 'CORRECTION: listed in the party plan but NOT a Sorcerer spell (Bard/Cleric/Wizard, class level 5); the Cleric dip only reaches level 2, so this build can only cast it from scrolls.'
  leveling:
    respecs:
    - label: Lv 1–5 · Cleric-start
      note: 'Early game: Tempest Cleric 1 FIRST for on-demand Wet (Create Water) + heavy armour in Act 1, then Sorcerer. Tradeoff — Cleric-first means WIS+CHA saves (no CON) until the char-6 respec.'
      rows:
      - char_level: 1
        class: Tempest Cleric 1
        gains: Create Water (Wet); heavy armour + shields
      - char_level: 2
        class: Sorcerer 1
        gains: Storm Sorcery; Tempestuous Magic (fly)
      - char_level: 3
        class: Sorcerer 2
        gains: Metamagic (Twinned + Quickened)
      - char_level: 4
        class: Sorcerer 3
        gains: L2 slots (Misty Step)
      - char_level: 5
        class: Sorcerer 4
        gains: 'Feat: War Caster'
    - label: Lv 6 · respec to all-Sorcerer
      note: 'At char 6, respec to PURE Sorcerer (drop the early Cleric). Regains CON+CHA saves (Twinned-Haste concentration), on-time Lightning Bolt, and the Storm-6 spike — and Create Water now comes free from Storm Spells at Sorc 6.'
      rows:
      - char_level: 1
        class: Sorcerer 1
        gains: Storm Sorcery; Tempestuous Magic (fly)
      - char_level: 2
        class: Sorcerer 2
        gains: Metamagic (Twinned + Quickened)
      - char_level: 3
        class: Sorcerer 3
        gains: L2 slots (Misty Step)
      - char_level: 4
        class: Sorcerer 4
        gains: 'Feat: War Caster'
      - char_level: 5
        class: Sorcerer 5
        gains: L3 slots → Twinned Haste; Lightning Bolt; Counterspell
      - char_level: 6
        class: Sorcerer 6
        gains: Storm Spells (Create Water, Call Lightning, Sleet Storm); Heart of the Storm; resistance
      - char_level: 7
        class: Sorcerer 7
        gains: L4 slots
      - char_level: 8
        class: Sorcerer 8
        gains: 'Feat: Alert'
    - label: Endgame · Sorc 10 / Tempest 2
      note: 'Final build: pure Sorcerer to 10, then the 2 Tempest levels at 11–12 for Destructive Wrath. Cleric LAST keeps CON saves (no reorder respec needed). Cleric-first also works if you want Wrath the moment you dip, but loses the CON save.'
      rows:
      - char_level: 1
        class: Sorcerer 1
        gains: Storm Sorcery; Tempestuous Magic (fly)
      - char_level: 2
        class: Sorcerer 2
        gains: Metamagic (Twinned + Quickened)
      - char_level: 3
        class: Sorcerer 3
        gains: L2 slots (Misty Step)
      - char_level: 4
        class: Sorcerer 4
        gains: 'Feat: War Caster'
      - char_level: 5
        class: Sorcerer 5
        gains: L3 slots → Twinned Haste; Lightning Bolt
      - char_level: 6
        class: Sorcerer 6
        gains: Storm Spells; Heart of the Storm; resistance
      - char_level: 7
        class: Sorcerer 7
        gains: L4 slots
      - char_level: 8
        class: Sorcerer 8
        gains: 'Feat: Alert'
      - char_level: 9
        class: Sorcerer 9
        gains: L5 slots (Cone of Cold)
      - char_level: 10
        class: Sorcerer 10
        gains: capstone; 6 cantrips
      - char_level: 11
        class: Tempest Cleric 1
        gains: Create/Destroy Water; heavy armour + shields
      - char_level: 12
        class: Tempest Cleric 2
        gains: Destructive Wrath (maximise Lightning/Thunder)
  itemization:
    act1:
    - id: the-spellsparkler
      item: The Spellsparkler
      note: 'The Spellsparkler (Waukeen''s Rest — Counsellor Florrick reward). Spells build Lightning Charges (+1 attack, +1 Lightning; 5 charges → 1d8 burst). ⚠ It''s "Consumable by Gale" — WIELD it, do NOT feed it to the Netherese orb.'
    - id: head-slot-open
      item: Head slot open
      note: Head slot open (the Diadem of Arcane Synergy went to Charles — its weapon-damage buff is dead on a pure caster); save it for a spell-DC hat (Hood of the Weave / Birthright later)
    act2:
    - id: callous-glow-ring
      item: Callous Glow Ring
      note: Callous Glow Ring
    - id: boots-of-stormy-clamour
      item: Boots of Stormy Clamour
      note: Boots of Stormy Clamour
    - id: coruscation-ring
      item: Coruscation Ring
      note: Coruscation Ring
    - id: potent-robe
      item: Potent Robe
      note: Potent Robe (Alfira at Last Light — only if she survived Act 1)
    act3:
    - id: markoheshkir
      item: Markoheshkir
      note: Markoheshkir (Kereska's Favour → Lightning)
    - id: gloves-of-belligerent-skies
      item: Gloves of Belligerent Skies
      note: Gloves of Belligerent Skies (Crèche, Act 1) — every Lightning/Thunder hit stacks Reverberation → 5 stacks = CON save or Prone; turns each AoE into soft-CC. (Spellmight Gloves do NOTHING for this kit — they need spell ATTACK rolls, and everything here is save-based.)
    - id: birthright
      item: Birthright
      note: Birthright (+2 CHA)
    - id: amulet-of-the-devout
      item: Amulet of the Devout
      note: Amulet of the Devout (extra Destructive Wrath) — Gale keeps the neck; the Amulet of Greater Health went to the Bard
  playstyle: 'Self-apply Wet (Create Water from Sorc 6, thrown water bottles, or the Tempest dip), then blast doubled Lightning/Cold — Chromatic Orb: Lightning / Lightning Bolt / Call Lightning, each also splashing Heart of the Storm (doubled by Wet); maximise the big one with Destructive Wrath. Party Haste engine via Twinned Haste on the Paladin. Kite with Tempestuous Magic flight every turn — reposition, take AoE angles, and escape melee, since Storm trades Draconic durability for that mobility. Keep the wet/electrified cluster OFF the melee (a Wet ally takes double lightning/cold).'
  traps:
  - 'Friendly fire: electrified water damages anyone standing in it (incl. your melee), and Wet makes your own frontliner take double enemy lightning/cold — soak clusters that don''t overlap the Paladin.'
  - 'Gale''s Netherese orb: a one-off early-Act-1 chore — feed him 3 magic items (The Wizard of Waterdeep) and it resolves; ignoring it stacks Arcane Hunger debuffs and only the final stage is fatal. Not an ongoing tax.'
  - 'Respec cost: Gale joins as a Wizard — bank ~100g for the Withers respec into Sorcerer, and re-pick metamagic/spells to match this plan.'
  - 'Class order: currently Cleric-first (Cleric 2 / Sorc 1) → WIS + CHA saves, NO CON save. Respec at char 6 to Sorcerer-first (→ Sorcerer 6, the Storm spike) to regain CON saves for Haste concentration, and take the Tempest 2 dip LAST (char 11–12) for Destructive Wrath. Char 6–10 you have no armour — lean on Tempestuous flight + Storm''s lightning/thunder resistance until heavy armour lands at char 11.'
---

