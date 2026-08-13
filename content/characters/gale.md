---
nickname: Gale
builds:
- name: The Shock Bottle
  is_primary: true
  role: Wet + Lightning AoE nuke + party Haste engine
  class: Sorcerer 10 (Storm Sorcery) / Tempest Cleric 2
  race: Gale (Human)
  race_notes: 'Human (BG3) — a free +2/+1 like every race (the CHA 17 is 15 point-buy + racial +2), Civil Militia proficiency with shields, light armour and spear/pike/halberd/glaive (no trident), one extra skill, +25% carry weight. Stat-neutral, so it costs nothing. NETHERESE ORB: an early-Act-1 chore only — feed Gale 3 magic items (The Wizard of Waterdeep) and the hunger resolves; Elminster later quells it entirely. Ignoring it stacks Arcane Hunger debuffs (disadvantage on saves → attacks → half move) and only the final ignored stage is fatal. NOT an ongoing Act 1–2 drain. Recruited as a Wizard; respec via Withers into this build.'
  background: Sage (Arcana, History) — Gale's default
  starting_stats:
    STR: 8
    DEX: 14
    CON: 14
    INT: 8
    WIS: 12
    CHA: 17
  stats_note: 'Point-buy 8/14/14/8/12/15 = all 27 (14s cost 2 each — set BOTH DEX and CON to 14). Human +2 → CHA 17; the +1 is a spare, so bank it on CON. ⚠ 2 points left over means you set a physical to 13 — bump it to 14.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss). Birthright brings Gale to CHA 22 in Act 3 when he wears it.'
  metamagic:
  - Twinned + Extended (L2)
  - Quickened (L3)
  feats:
  - at: Sorc 4
    feat: War Caster
  - at: Sorc 8
    feat: Alert
    note: 'Swapped from Elemental Adept (redundant — Wet already negates lightning/cold resistance). Alert (+5 initiative, immune to Surprise) fixes the party''s biggest round-1 problem: low-DEX Gale must Twinned-Haste the melee BEFORE they act. War Caster (Sorc 4) already covers Haste concentration.'
  key_spells:
  - Create Water (Storm Spells at Sorc 6; also Tempest dip)
  - Witch Bolt / Lightning Bolt
  - Haste (Twinned)
  - Counterspell
  - Glyph of Warding (scroll only — not a Sorcerer spell)
  creation:
    level1_class: Tempest Cleric 1 for the character-level-1–5 bridge; respec to Sorcerer-first at character level 6.
    level1_gains: Prepared Cleric spells, Guidance, Create Water, Wrath of the Storm, heavy armour, shields, martial weapons, and WIS + CHA saves. The level-6 respec trades the Cleric level for pure Storm Sorcerer 6 and CON + CHA saves.
    subclass_choice: Tempest Domain for the early bridge; Storm Sorcery after the level-6 respec.
    proficiencies:
      armor_weapons: 'Heavy armour, shields and martial weapons at char 1–5. Pure Sorcerer at 6 loses the Cleric package, but Human Civil Militia keeps light armour and shield proficiency; the Tempest dip restores heavy armour at 11–12.'
      saving_throws: WIS + CHA through character level 5; CON + CHA after the Sorcerer-first level-6 respec.
      skills: Sage (Arcana, History) + 2 Sorcerer picks + Human extra.
    starting_cantrips: Guidance, Resistance and Thaumaturgy from Cleric 1; Sorcerer cantrips arrive at character level 2.
    starting_spells: 'WIS 12 + Cleric 1 = 2 prepared Cleric spells — Create or Destroy Water + Healing Word, Sanctuary as flex. At char 4 swap Healing Word to Bane for Bonbon''s Hold Person setup. At char 2 take Chromatic Orb: Lightning + Shield.'
    notes: The bridge gives Act 1 immediate Wet and armour. At char 6, respec to pure Storm Sorcerer 6 for on-time Haste, Lightning Bolt, Storm Spells and CON saves. Retake the Tempest 2 dip only at char 11–12.
  spells:
    note: Sorcerer is a KNOWN caster (learn on level-up, replace 1 per level); the Tempest Cleric 2 dip is a prepared caster re-picked freely. Mandatory = the wet-lightning engine + Haste; Recommended = flex nukes and utility.
    mandatory:
    - spell: Witch Bolt
      level: '1'
      guide_level: 3
      school: Evocation
      save: Ranged spell attack
      when: Sorc 2 (learned — Storm grants no free spell)
      why: 1d12 Lightning, Concentration. Re-activate each turn with no roll, builds Lightning Charges on The Spellsparkler, and works with Destructive Wrath.
    - spell: 'Chromatic Orb: Lightning'
      level: '1'
      guide_level: 2
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1–3
      why: 2d8 Lightning that creates an Electrified Water surface, +1d8 per upcast level, and triggers Destructive Wrath — cheap single-target lightning that sets up the electrify combo.
    - spell: Lightning Bolt
      level: '3'
      guide_level: 6
      school: Evocation
      save: DEX save
      when: char 6 (learned at Sorc 5 during the pure-Sorcerer respec)
      why: 8d6 Lightning line — the main AoE nuke. Doubled vs Wet, maximised by Destructive Wrath, and every cast fires Heart of the Storm (free Lightning splash within 6m, also doubled by Wet). Arrives at char 6 in this bridge, not level 5.
    - spell: Haste
      level: '3'
      guide_level: 6
      school: Transmutation
      save: None (Concentration)
      when: char 6 (learned at Sorc 5 during the pure-Sorcerer respec)
      why: 'Single-target, so Twinnable — 3 Sorcery Points Hastes Charles + Asterion. Arrives at char 6 in this bridge. Never cast another Concentration spell while it runs: ending Haste makes both targets Lethargic.'
    - spell: Counterspell
      level: '3'
      guide_level: 6
      school: Abjuration
      save: Reaction (no save at equal/higher slot)
      when: Sorc 6
      why: Shuts down enemy casters; upcast to beat higher-level spells without a check.
    - spell: Create or Destroy Water
      level: '1'
      guide_level: 1
      school: Transmutation
      save: None
      when: 'char 1–5 (prepared Tempest Cleric spell); char 6 (Storm Spell); char 11+ (prepared again)'
      why: Gale owns Wet for the whole run — the early Tempest level prepares it, then Storm Sorcery grants it free after the char-6 respec. Wet doubles Lightning/Cold. No save and no Concentration, so it is safe while holding Haste.
    - spell: Call Lightning
      level: '3'
      guide_level: 6
      school: Conjuration
      save: DEX save
      when: char 6 (Storm Spells)
      why: Storm Spell at Sorc 6 — summon a cloud (Concentration), then re-fire a bolt as an ACTION each turn with no further slot. Sustained AoE Lightning, doubled by Wet, triggering Heart of the Storm every turn. Competes with Haste, so use it in fights where Gale is not Hasting.
    - spell: Destructive Wrath
      level: Channel Divinity (not a spell)
      school: Tempest Domain feature
      save: N/A
      when: char 12 (Tempest Cleric 2)
      why: The payoff — spend a Channel Divinity charge to MAXIMISE any Thunder/Lightning roll (Lightning Bolt, Chain Lightning, Markoheshkir bolts, Thunderwave). 1/rest, 2 with the Amulet of the Devout.
    recommended:
    - spell: Shocking Grasp
      level: Cantrip
      guide_level: 2
      school: Evocation
      save: Melee spell attack
      when: Sorc 1
      why: 'Best lightning cantrip — 1d8 → 3d8 by char 10, strips Reactions, advantage vs metal armour. Scales with Potent Robe, Spellmight Gloves and Markoheshkir, and is the War Caster opportunity-spell payload.'
    - spell: Ray of Frost
      level: Cantrip
      guide_level: 2
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1
      why: Wet-compatible Cold fallback with a movement penalty — for when Gale needs range instead of Shocking Grasp.
    - spell: Mage Hand
      level: Cantrip
      guide_level: 2
      school: Conjuration
      save: None
      when: char 2 (Sorc 1)
      why: 'Exploration and object manipulation — no attack roll, save or Concentration. For a no-slot single-target Wet, drop a bottle in reach and use the Hand''s Throw for a 2m splash. Lasts 10 turns, recharges on a short rest.'
    - spell: Minor Illusion
      level: Cantrip
      guide_level: 2
      school: Illusion
      save: None
      when: Sorc 1
      why: Groups enemies before combat so the lightning area spells hit more targets.
    - spell: Bone Chill
      level: Cantrip
      guide_level: 5
      school: Necromancy
      save: Ranged spell attack
      when: Sorc 4
      why: Ranged anti-healing utility and advantage against Undead.
    - spell: Cone of Cold
      level: '5'
      guide_level: 9
      school: Evocation
      save: DEX save
      when: Sorc 9–10
      why: 5d8 Cold AoE — off-element, but Wet gives Cold vulnerability too, so it still doubles.
    - spell: Telekinesis
      level: '5'
      guide_level: 10
      school: Transmutation
      save: STR save
      when: Sorc 10
      why: Concentration control that can repeatedly reposition a dangerous target or throw it from high ground.
    - spell: Fireball
      level: '3'
      guide_level: 8
      school: Evocation
      save: DEX save
      when: Sorc 5+
      why: 8d6 Fire AoE flex for fire-vulnerable or non-Wet packs. Off-type, so no Heart of the Storm — situational.
    - spell: Misty Step
      level: '2'
      guide_level: 4
      school: Conjuration
      save: None (bonus action)
      when: Sorc 3+
      why: Reposition out of your own electrified water.
    - spell: Mirror Image
      level: '2'
      guide_level: 5
      school: Illusion
      save: None
      when: Sorc 4
      why: Non-concentration defence that can be prepared before a dangerous engagement.
    - spell: Thunderwave
      level: '1'
      guide_level: 1
      school: Evocation
      save: CON save
      when: char 11 (Tempest domain, always-prepared)
      why: Free domain spell — 2d8 Thunder + knockback. A Thunder roll, so Destructive Wrath maximises it (16 guaranteed) and it triggers Reverberation gear.
    - spell: Sleet Storm
      level: '3'
      guide_level: 6
      school: Conjuration
      save: DEX save
      when: char 6 (Storm Spells)
      why: Storm Spell at Sorc 6 — ice-surface control that blinds and knocks Prone (breaking Concentration) and turns the ground slippery. Off-element for damage, but premier lockdown for a mobile storm caster.
    - spell: Ice Storm
      level: '4'
      guide_level: 7
      school: Evocation
      save: DEX save
      when: Sorc 7
      why: Large Cold burst plus an ice surface — Wet doubles the Cold and the surface controls survivors.
    - spell: Heart of the Storm
      level: Feature (Storm Sorcery, Sorc 6)
      school: Storm Sorcery feature — Lightning/Thunder
      save: None (automatic)
      when: char 6
      why: 'Passive — any Lightning/Thunder spell of level 1+ deals (Sorcerer level ÷ 2) to all enemies within 6m. A free splash on every Chromatic Orb: Lightning, Lightning Bolt and Call Lightning, also doubled by Wet. Enemies only — no friendly fire from this part.'
    - spell: Chain Lightning
      level: '6'
      school: Evocation
      save: DEX save
      when: Markoheshkir / scroll only (Sorc learns it at class 11, unreached)
      why: 10d8 Lightning — reached via Markoheshkir (Kereska's Favour / Bolts of Doom, 1/short rest) or scrolls, not learned at Sorc 10.
    - spell: Fire Bolt
      level: Cantrip
      guide_level: 10
      school: Evocation
      save: Ranged spell attack
      when: Sorc 10
      why: Long-range cleanup and a damage type outside the lightning/cold package.
    - spell: Glyph of Warding
      level: '3'
      school: Abjuration
      save: DEX save
      when: scroll only for this build
      why: 'CORRECTION: listed in the party plan but NOT a Sorcerer spell (Bard/Cleric/Wizard, class level 5). The Cleric dip only reaches level 2, so this build casts it from scrolls only.'
    - spell: Guidance
      level: Cantrip
      guide_level: 1
      school: Divination
      save: None
      when: char 1–5 (Tempest Cleric bridge)
      why: Adds 1d4 to an ally's ability checks. Gale loses it at the char-6 respec, so keep the Silver Pendant from the Harper outpost as the permanent replacement. Guidance concentrates — treat it as an exploration buff.
    - spell: Bane
      wiki: Bane (spell)
      level: '1'
      guide_level: 4
      school: Enchantment
      save: CHA save
      when: char 4–5 (prepared Tempest Cleric bridge spell)
      why: 'SHORT BRIDGE ONLY — Bane first (up to 3 enemies, −1d4 saves), then Bonbon holds Hold Person on a separate Concentration slot. Gale''s WIS 12 is a weak DC 11–12, so target low CHA. Retire it at the char-6 respec: Gale must hold Twinned Haste, and Phalar Shriek + Gloves of Baneful Striking give free save penalties.'
    - spell: Resistance
      level: Cantrip
      guide_level: 1
      wiki: Resistance (Cantrip)
      school: Abjuration
      save: None
      when: char 1 (Tempest Cleric)
      why: Adds 1d4 to an ally's saving throws while Concentrating — situational preparation before a known hazard.
    - spell: Thaumaturgy
      level: Cantrip
      guide_level: 1
      school: Transmutation
      save: None
      when: char 1 (Tempest Cleric)
      why: Advantage on Intimidation and Performance checks for dialogue utility.
    - spell: Healing Word
      level: '1'
      guide_level: 1
      school: Evocation
      save: None
      when: char 1–5 (Tempest Cleric bridge)
      why: Bonus-action ranged recovery for a downed ally; its value does not depend on a high Wisdom score. Bonbon has the permanent copy from char 2 onward.
    - spell: Sanctuary
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None
      when: char 1 (Tempest Cleric)
      why: Protects an ally who must survive or disengage; attacking or harming another creature ends it.
    - spell: Shield
      level: '1'
      guide_level: 2
      school: Abjuration
      save: None (reaction, +5 AC)
      when: char 2 (Sorcerer 1)
      why: Reaction defence that sharply improves Gale's survival without using Concentration.
  leveling:
    respecs:
    - label: Lv 1–5 · Cleric-start
      note: 'Early game — Tempest Cleric 1 FIRST for on-demand Wet (Create Water) and heavy armour in Act 1, then Sorcerer. Tradeoff: Cleric-first means WIS+CHA saves, no CON, until the char-6 respec.'
      rows:
      - char_level: 1
        class: Tempest Cleric 1
        gains:
        - Cleric Spellcasting
        - Heavy armour, shields, and martial weapons
        - Wrath of the Storm
        - Tempest domain spells Fog Cloud and Thunderwave
        - WIS + CHA saving-throw proficiency
        recommendations:
        - category: Subclass
          recommendation: Tempest Domain
          note: Early Create Water access, armour, and the later Destructive Wrath package.
        - category: Cantrips
          recommendation:
          - Guidance
          - Resistance
          - Thaumaturgy
          note: Utility choices that do not depend on Gale's low WIS attack roll.
        - category: Prepared spells
          recommendation:
          - Create or Destroy Water
          - Healing Word (char 1–3) → Bane (char 4–5)
          note: Only 2 prepared Cleric spells at WIS 12. Keep Create Water throughout; start with Healing Word, swap to Bane when Bonbon gains Hold Person. Sanctuary is the flex. Bane's low DC makes it a bridge, not a level-6+ plan.
      - char_level: 2
        class: Sorcerer 1
        gains:
        - Sorcerer Spellcasting
        - Tempestuous Magic (bonus-action Fly after a levelled spell)
        recommendations:
        - category: Subclass
          recommendation: Storm Sorcery
          note: The build's mobility and level-6 lightning/thunder package.
        - category: Cantrips
          recommendation:
          - Shocking Grasp
          - Ray of Frost
          - Mage Hand
          - Minor Illusion
          note: One lightning attack, one Wet-compatible cold attack, and two utility picks.
        - category: Spells
          recommendation:
          - 'Chromatic Orb: Lightning'
          - Shield
          note: Early lightning burst and the essential defensive reaction.
      - char_level: 3
        class: Sorcerer 2
        gains:
        - Font of Magic
        - Two Sorcery Points
        - Two Metamagic selections
        recommendations:
        - category: Metamagic
          recommendation:
          - Twinned Spell
          - Extended Spell
          note: Quickened is not selectable until Sorcerer 3; Twinned is mandatory for the later Haste engine.
        - category: Spell
          recommendation: Witch Bolt
          note: Sustained lightning that scales with Wet and Destructive Wrath.
      - char_level: 4
        class: Sorcerer 3
        gains:
        - Level 2 Sorcerer spells
        - Third Metamagic selection
        - Three Sorcery Points
        recommendations:
        - category: Metamagic
          recommendation: Quickened Spell
          note: Available at Sorcerer 3; converts key spells into bonus actions.
        - category: Spell
          recommendation: Misty Step
          note: Escapes electrified surfaces and fixes casting angles.
      - char_level: 5
        class: Sorcerer 4
        gains:
        - Fifth Sorcerer cantrip
        - Four Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: War Caster
          note: Advantage on concentration saves protects the upcoming Twinned Haste engine.
        - category: Cantrip
          recommendation: Bone Chill
          note: Adds ranged anti-healing utility.
        - category: Spell
          recommendation: Mirror Image
          note: Non-concentration defence for fights where Shield alone is not enough.
    - label: Lv 6 · respec to all-Sorcerer
      note: At char 6, respec to PURE Sorcerer and drop the early Cleric level. Regains CON+CHA saves (Twinned-Haste concentration), on-time Lightning Bolt and the Storm-6 spike — and Create Water now comes free from Storm Spells at Sorc 6.
      rows:
      - char_level: 1
        class: Sorcerer 1
        gains:
        - Sorcerer Spellcasting
        - Tempestuous Magic
        - CON + CHA saving-throw proficiency
        recommendations:
        - category: Subclass
          recommendation: Storm Sorcery
        - category: Cantrips
          recommendation:
          - Shocking Grasp
          - Ray of Frost
          - Mage Hand
          - Minor Illusion
        - category: Spells
          recommendation:
          - 'Chromatic Orb: Lightning'
          - Shield
      - char_level: 2
        class: Sorcerer 2
        gains:
        - Font of Magic
        - Two Sorcery Points
        - Two Metamagic selections
        recommendations:
        - category: Metamagic
          recommendation:
          - Twinned Spell
          - Extended Spell
          note: Take Quickened at the next Sorcerer level.
        - category: Spell
          recommendation: Witch Bolt
      - char_level: 3
        class: Sorcerer 3
        gains:
        - Level 2 Sorcerer spells
        - Third Metamagic selection
        - Three Sorcery Points
        recommendations:
        - category: Metamagic
          recommendation: Quickened Spell
        - category: Spell
          recommendation: Misty Step
      - char_level: 4
        class: Sorcerer 4
        gains:
        - Fifth Sorcerer cantrip
        - Four Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: War Caster
        - category: Cantrip
          recommendation: Bone Chill
        - category: Spell
          recommendation: Mirror Image
      - char_level: 5
        class: Sorcerer 5
        gains:
        - Level 3 Sorcerer spells
        - Five Sorcery Points
        recommendations:
        - category: Spells
          recommendation:
          - Haste
          - Lightning Bolt
          note: Learn one and replace an early flex spell with the other — these are the priority level-3 picks.
      - char_level: 6
        class: Sorcerer 6
        gains:
        - Heart of the Storm
        - Heart of the Storm resistances
        - Storm Spells (Call Lightning, Create or Destroy Water, Gust of Wind, Sleet Storm, and Thunderwave)
        - Six Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Counterspell
          note: Add the reaction defence now that Haste and Lightning Bolt are secured.
      - char_level: 7
        class: Sorcerer 7
        gains:
        - Level 4 Sorcerer spells
        - Seven Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Ice Storm
          note: Cold also doubles against Wet targets, and it supplies a large control surface.
      - char_level: 8
        class: Sorcerer 8
        gains:
        - Eight Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: Alert
          note: Lets low-DEX Gale cast Twinned Haste before the party's martial turns.
        - category: Spell
          recommendation: Fireball
          note: Flexible non-Lightning area damage where applying Wet is inefficient.
    - label: Endgame · Sorc 10 / Tempest 2
      note: Pure Sorcerer to 10, then the 2 Tempest levels at 11–12 for Destructive Wrath. Cleric LAST keeps CON saves with no reorder respec. Cleric-first also works if you want Wrath the moment you dip, but loses the CON save.
      rows:
      - char_level: 1
        class: Sorcerer 1
        gains:
        - Sorcerer Spellcasting
        - Tempestuous Magic
        - CON + CHA saving-throw proficiency
        recommendations:
        - category: Subclass
          recommendation: Storm Sorcery
        - category: Cantrips
          recommendation:
          - Shocking Grasp
          - Ray of Frost
          - Mage Hand
          - Minor Illusion
        - category: Spells
          recommendation:
          - 'Chromatic Orb: Lightning'
          - Shield
      - char_level: 2
        class: Sorcerer 2
        gains:
        - Font of Magic
        - Two Sorcery Points
        - Two Metamagic selections
        recommendations:
        - category: Metamagic
          recommendation:
          - Twinned Spell
          - Extended Spell
        - category: Spell
          recommendation: Witch Bolt
      - char_level: 3
        class: Sorcerer 3
        gains:
        - Level 2 Sorcerer spells
        - Third Metamagic selection
        - Three Sorcery Points
        recommendations:
        - category: Metamagic
          recommendation: Quickened Spell
        - category: Spell
          recommendation: Misty Step
      - char_level: 4
        class: Sorcerer 4
        gains:
        - Fifth Sorcerer cantrip
        - Four Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: War Caster
        - category: Cantrip
          recommendation: Bone Chill
        - category: Spell
          recommendation: Mirror Image
      - char_level: 5
        class: Sorcerer 5
        gains:
        - Level 3 Sorcerer spells
        - Five Sorcery Points
        recommendations:
        - category: Spells
          recommendation:
          - Haste
          - Lightning Bolt
          note: Learn one and replace an early flex spell with the other.
      - char_level: 6
        class: Sorcerer 6
        gains:
        - Heart of the Storm
        - Heart of the Storm resistances
        - Storm Spells (Call Lightning, Create or Destroy Water, Gust of Wind, Sleet Storm, and Thunderwave)
        - Six Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Counterspell
      - char_level: 7
        class: Sorcerer 7
        gains:
        - Level 4 Sorcerer spells
        - Seven Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Ice Storm
      - char_level: 8
        class: Sorcerer 8
        gains:
        - Eight Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: Alert
          note: Guarantees the setup caster acts early enough to Haste the martial characters.
        - category: Spell
          recommendation: Fireball
          note: Flexible non-Lightning area damage where Wet setup is inefficient.
      - char_level: 9
        class: Sorcerer 9
        gains:
        - Level 5 Sorcerer spells
        - Nine Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Cone of Cold
          note: Wet doubles Cold too, so this stays inside the party's vulnerability engine.
      - char_level: 10
        class: Sorcerer 10
        gains:
        - Fourth Metamagic selection
        - Sixth Sorcerer cantrip
        - One additional spell known
        - Ten Sorcery Points
        recommendations:
        - category: Metamagic
          recommendation: Heightened Spell
          note: Forces disadvantage on a key saving throw when raw damage is not the answer.
        - category: Cantrip
          recommendation: Fire Bolt
          note: A long-range, non-Lightning damage type for cleanup turns.
        - category: Spell
          recommendation: Telekinesis
          note: Concentration control that repositions dangerous enemies or throws them from high ground.
      - char_level: 11
        class: Tempest Cleric 1
        gains:
        - Cleric Spellcasting
        - Heavy armour, shields, and martial weapons
        - Wrath of the Storm
        - Tempest domain spells Fog Cloud and Thunderwave
        recommendations:
        - category: Cantrips
          recommendation:
          - Guidance
          - Resistance
          - Thaumaturgy
        - category: Prepared spells
          recommendation:
          - Healing Word
          - Sanctuary
          note: 'WIS 12 allows 2 prepared Cleric spells. Do not prepare Create Water here: Storm Sorcery already grants it and a character can only have one version. Healing Word and Sanctuary stay useful despite the low WIS.'
      - char_level: 12
        class: Tempest Cleric 2
        gains:
        - Channel Divinity
        - Destructive Wrath (maximise Lightning or Thunder damage)
        - Turn Undead
  itemization:
    act1:
    - id: bow-of-awareness
      item: Bow of Awareness
      slot: ranged weapons
      note: Roah Moonglow, Shattered Sanctum. Carried purely for +1 Initiative so Gale lands Twinned Haste or Wet before the melee turns — no shortbow proficiency needed for the passive, and he should cast rather than fire it.
    - id: the-spellsparkler
      item: The Spellsparkler
      slot: weapons
      note: 'Counsellor Florrick. Damaging spells build Lightning Charges (+1 attack, +1 Lightning; 5 charges → a 1d8 burst), best with multi-hit spells. ⚠ Marked “Consumable by Gale” — wield it, never feed it to the orb.'
    - id: melf-s-first-staff
      item: Melf's First Staff (save-DC alternative)
      slot: weapons
      note: Blurg, late Act 1. +1 Spell Save DC and spell attacks beats charge generation when the key cast is a save-based Lightning Bolt, Sleet Storm or control spell. Keep Spellsparkler for multi-hit turns.
    - id: shadespell-circlet
      item: The Shadespell Circlet
      slot: head
      note: Omeluum, after his quest. +1 Spell Save DC while obscured in shadow. The Haste Helm goes to Charles — Tempestuous Magic already repositions Gale after levelled spells.
    - id: the-lifebringer
      item: The Lifebringer (defensive head alternative)
      slot: head
      note: Blurg. Lightning Charges grant 3 temp HP until they expire — for when Shadespell cannot stay active.
    - id: boots-of-stormy-clamour
      item: Boots of Stormy Clamour
      slot: feet
      note: Omeluum. Inflicting a condition → 2 turns of Reverberation. ⚠ A multi-target action triggers them once, on one target — control support, not AoE-wide.
    - id: gloves-of-belligerent-skies
      item: Gloves of Belligerent Skies
      slot: hands
      note: Crèche Inquisitor's Chamber. Lightning/Thunder/Radiant → 2 turns of Reverberation, save-based Lightning Bolt included. ⚠ Triggers once per attack, so an AoE applies it only to the first logged target.
    - id: pearl-of-power-amulet
      item: Pearl of Power Amulet
      slot: amulets
      note: Omeluum. One L3-or-lower slot back per long rest — another Haste, Lightning Bolt or Counterspell. Swap to the Elemental Augmentation neck once spent.
    - id: necklace-of-elemental-augmentation
      item: Necklace of Elemental Augmentation (cantrip alternative)
      slot: amulets
      note: Crèche display case. +CHA to Shocking Grasp, Ray of Frost or another native elemental cantrip — for after Pearl of Power is spent.
    - id: safeguard-shield
      item: Safeguard Shield
      slot: shields
      note: Dammon, the Grove. +2 AC, +1 all saves — protects Haste concentration. Civil Militia keeps shield proficiency after the char-6 respec.
    - id: spidersilk-armour
      item: Spidersilk Armour (early concentration alternative)
      slot: armour
      note: Minthara. Light armour, advantage on CON saves, +1 Stealth — a bridge until War Caster, after which the advantage is redundant.
    act2:
    - id: callous-glow-ring
      item: Callous Glow Ring
      slot: rings
      note: +2 radiant whenever Gale damages an illuminated target. His area and multi-hit spells trigger the rider repeatedly, and the radiant damage can also activate Belligerent Skies.
    - id: coruscation-ring
      item: Coruscation Ring
      slot: rings
      note: Applies Radiating Orb when Gale deals spell damage while illuminated. The attack penalties protect the party and count as conditions for his Reverberation package.
    - id: potent-robe
      item: Potent Robe
      slot: armour
      note: Alfira at Last Light, if she survived Act 1. +CHA to cantrip damage and temp HP each turn — improves slot-free Shocking Grasp turns.
    act3:
    - id: markoheshkir
      item: Markoheshkir
      slot: weapons
      note: +1 spell attack/DC plus Kereska's Favour. Choose Bolts of Doom for Lightning Charges, lightning resistance and free lightning spells that feed the Wet-lightning engine.
    - id: birthright
      item: Birthright
      slot: head
      note: +2 CHA (up to 22 here), raising spell attack rolls and save DC. His straightforward damage/control headpiece when Bonbon is not using it.
    - id: amulet-of-the-devout
      item: Amulet of the Devout
      slot: amulets
      note: +2 spell save DC and an extra Channel Divinity charge, which Gale converts into another Destructive Wrath. Bonbon takes the Amulet of Greater Health.
  playstyle: |-
    - **Choose a job:** Twinned Haste Charles + Asterion, or make a separate enemy cluster Wet and blast it with Lightning.
    - **Burst:** Destructive Wrath on the biggest Lightning hit.
    - **Stay safe:** reposition with Tempestuous Magic and never Wet or electrify the melee lane.
  traps:
  - 'Friendly fire: electrified water damages anyone standing in it, including your melee, and Wet makes your own frontliner take double enemy lightning/cold. Soak clusters that do not overlap the Paladin.'
  - 'Netherese orb: a one-off early-Act-1 chore — feed Gale 3 magic items (The Wizard of Waterdeep) and it resolves. Ignoring it stacks Arcane Hunger debuffs and only the final stage is fatal. Not an ongoing tax.'
  - 'Respec cost: Gale joins as a Wizard — bank ~100g for the Withers respec into Sorcerer and re-pick metamagic and spells to match this plan.'
  - 'Class order: char 1–5 is Cleric-first, so WIS + CHA saves and no CON proficiency during the bridge. Respec at char 6 to pure Sorcerer 6 for CON + CHA saves and the Storm spike, then Tempest 2 last at char 11–12. Char 6–10 loses heavy armour, but Civil Militia still permits light armour + a shield.'
---
