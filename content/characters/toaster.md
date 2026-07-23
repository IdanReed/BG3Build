---
nickname: Toaster
builds:
- name: The Shock Bottle
  is_primary: true
  role: Wet + Lightning AoE nuke + party Haste engine
  class: Sorcerer 10 (Draconic Bloodline — Blue) / Tempest Cleric 2
  race: Gale (Human)
  race_notes: 'Human (BG3): a freely-assigned +2/+1 ability bonus like every race (the CHA 17 in starting_stats is 15 point-buy + the +2 racial), ''Civil Militia'' proficiency with Shields + Light armour + spear/pike/halberd/glaive (no trident), one extra skill, and +25% carry weight — stat-neutral vs any other race, so it costs nothing. NETHERESE ORB: only an EARLY-Act-1 issue — the 3-item ''The Wizard of Waterdeep'' quest; feed Gale 3 magic items and the hunger resolves (Elminster later quells it entirely). Ignoring it stacks escalating Arcane Hunger debuffs (disadvantage on saves → attacks → half move) and only the final ignored stage is fatal — it is NOT an Act 1–2 resource drain. Recruited as a Wizard; respec via Withers into this Draconic-Blue Sorcerer / Tempest Cleric build.'
  background: Sage (Arcana, History) — Gale's default
  starting_stats:
    STR: 8
    DEX: 14
    CON: 14
    INT: 8
    WIS: 12
    CHA: 17
  ability_targets: CHA 17 → 20 (Hag's Hair + Mirror).
  metamagic:
  - Twinned + Extended (L2)
  - Quickened (L3)
  feats:
  - at: Sorc 4
    feat: War Caster
  - at: Sorc 8
    feat: Alert
    note: 'Swapped from Elemental Adept (redundant — Wet already negates lightning/cold resistance). Alert (+5 initiative, immune to Surprise) fixes the party''s biggest R1 problem: low-DEX Toaster must Twinned-Haste the melee BEFORE they act. Haste concentration is already covered by War Caster (Sorc 4).'
  key_spells:
  - Create Water (via Tempest dip)
  - Witch Bolt / Lightning Bolt
  - Haste (Twinned)
  - Counterspell
  - Glyph of Warding (scroll only — not a Sorcerer spell)
  creation:
    level1_class: Sorcerer 1 (Draconic Bloodline — Blue)
    level1_gains: Draconic Bloodline (Blue / lightning) subclass; Draconic Resilience (unarmoured AC = 13 + DEX, +1 HP per Sorcerer level); free Witch Bolt. Metamagic starts at Sorcerer 2.
    subclass_choice: Draconic Bloodline (Blue) is chosen at Sorcerer 1 (character creation).
    proficiencies:
      armor_weapons: 'Sorcerer: no armour; Daggers, Quarterstaves, Light Crossbows. The Tempest Cleric 2 dip (char 11–12) later adds Heavy armour, Shields, and Martial weapons.'
      saving_throws: Constitution + Charisma (Sorcerer, the creation class). The late Cleric dip grants no additional save proficiency.
      skills: Sorcerer chooses 2 from Arcana, Deception, Insight, Intimidation, Persuasion, Religion. Gale's Sage background adds Arcana + History; Human grants one extra skill proficiency.
    starting_cantrips: 4 known at level 1 — recommend Shocking Grasp (best lightning cantrip) + utility.
    starting_spells: 2 known at level 1, plus Witch Bolt granted free by Blue Draconic Ancestry.
    notes: 'Gale (Human) — recruited on the Ravaged Beach as a Wizard, then respec''d via Withers into the Sorcerer build (assign the starting stats above during respec; the CHA 17 uses Human''s +2 racial). 2 feats total (Sorc 4 + Sorc 8). Create Water and Destructive Wrath come from the Tempest Cleric 2 dip at char 11–12 — the Sorcerer cannot apply Wet on its own. Netherese orb: just feed him 3 magic items in early Act 1 (The Wizard of Waterdeep) and it''s done.'
  spells:
    note: Sorcerer is a KNOWN caster (learn on level-up, replace 1 per level); the Tempest Cleric 2 dip is a prepared caster re-picked freely. Mandatory = the wet-lightning engine + Haste; Recommended = flex nukes and utility.
    mandatory:
    - spell: Witch Bolt
      level: '1'
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1 (free, Blue ancestry)
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
      why: 8d6 Lightning line — the main AoE nuke; doubled vs Wet, maximized by Destructive Wrath, boosted by Elemental Affinity + Elemental Adept.
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
      when: char 11 (Tempest Cleric 1)
      why: NOT a Sorcerer spell — obtained via the Tempest dip (prepared). Applies Wet (double Lightning/Cold), which doubles the whole lightning package. No save, so low WIS is irrelevant.
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
      why: 'Best lightning cantrip: 1d8→3d8 by char 10, strips Reactions, advantage vs metal armour; scales with Potent Robe, Elemental Affinity, Spellmight Gloves, Markoheshkir; the War Caster opportunity-spell payload.'
    - spell: Cone of Cold
      level: '5'
      school: Evocation
      save: DEX save
      when: Sorc 9–10
      why: '5d8 Cold AoE; off-element for Elemental Adept: Lightning, but Wet gives Cold vulnerability too so it still doubles.'
    - spell: Fireball
      level: '3'
      school: Evocation
      save: DEX save
      when: Sorc 5+
      why: 8d6 Fire AoE flex for fire-vulnerable or non-Wet packs; off-type (no Elemental Affinity/Adept synergy), situational.
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
    - label: Level 1
      note: Gale is recruited on the Ravaged Beach as a level-1 Evocation Wizard. Do NOT level him as a Wizard — respec him into the Sorcerer build at Withers as soon as you can afford it (~100g). See the Respec tab for the actual leveling.
      rows:
      - char_level: 1
        class: Wizard 1 (as recruited)
        gains: Recruited state only — Evocation Wizard. A placeholder until the Withers respec into Sorcerer.
    - label: Respec → Sorcerer
      note: 'Respec at Withers (~100g) and rebuild from level 1 as a Draconic (Blue) Sorcerer. Assign the starting stats during the respec (the CHA 17 uses Human''s +2 racial) and re-pick Metamagic/spells to match this plan. Final: Sorcerer 10 → Tempest Cleric 2.'
      rows:
      - char_level: 1
        class: Sorcerer 1
        gains: Draconic Bloodline (Blue → Lightning); Witch Bolt free from Blue ancestry; 4 cantrips (Shocking Grasp) + 2 spells; +1 HP/level (Draconic Resilience)
      - char_level: 2
        class: Sorcerer 2
        gains: 'Font of Magic (sorcery points); Metamagic: Twinned + Quickened Spell (Extended later)'
      - char_level: 3
        class: Sorcerer 3
        gains: L2 spells (Misty Step); more sorcery points
      - char_level: 4
        class: Sorcerer 4
        gains: 'Feat: War Caster'
      - char_level: 5
        class: Sorcerer 5
        gains: 3rd-level slots → Haste (Twinned Haste on the Paladin), Counterspell, Lightning Bolt, Fireball
      - char_level: 6
        class: Sorcerer 6
        gains: 'Draconic 6: Elemental Affinity — add CHA to Lightning damage'
      - char_level: 7
        class: Sorcerer 7
        gains: 4th-level slots
      - char_level: 8
        class: Sorcerer 8
        gains: 'Feat: Elemental Adept (Lightning — ignore Lightning resistance; treat 1s on damage dice as 2s)'
      - char_level: 9
        class: Sorcerer 9
        gains: 5th-level slots (Cone of Cold)
      - char_level: 10
        class: Sorcerer 10
        gains: Sorcerer capstone for this build; 6 cantrips; final Metamagic pick
      - char_level: 11
        class: Tempest Cleric 1
        gains: Create/Destroy Water (the Wet engine → doubles Lightning/Cold); heavy armour + shields; Thunderwave domain spell
      - char_level: 12
        class: Tempest Cleric 2
        gains: 'Channel Divinity: Destructive Wrath — maximise any Lightning/Thunder roll'
  itemization:
    act1:
    - id: the-spellsparkler
      item: The Spellsparkler
      note: The Spellsparkler
    - id: head-slot-open
      item: Head slot open
      note: Head slot open (the Diadem of Arcane Synergy went to Durc — its weapon-damage buff is dead on a pure caster); save it for a spell-DC hat (Hood of the Weave / Birthright later)
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
      note: Amulet of the Devout (extra Destructive Wrath) — Toaster keeps the neck; the Amulet of Greater Health went to the Bard
  playstyle: Soak enemies with Create Water (Wet = lightning/cold vulnerability), then maximize with Destructive Wrath. Doubles as the party's Haste engine via Twinned Haste on the Paladin.
  traps:
  - 'Friendly fire: electrified water damages anyone standing in it (incl. your melee), and Wet makes your own frontliner take double enemy lightning/cold — soak clusters that don''t overlap the Paladin.'
  - 'Gale''s Netherese orb: a one-off early-Act-1 chore — feed him 3 magic items (The Wizard of Waterdeep) and it resolves; ignoring it stacks Arcane Hunger debuffs and only the final stage is fatal. Not an ongoing tax.'
  - 'Respec cost: Gale joins as a Wizard — bank ~100g for the Withers respec into Sorcerer, and re-pick metamagic/spells to match this plan.'
---

