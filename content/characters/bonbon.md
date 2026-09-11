---
nickname: Bonbon
builds:
- name: The Commander
  is_primary: true
  role: Ranged acuity control + damage + party face
  class: Swords Bard 11 / Fighter 1
  at_a_glance:
    armour: All armour + shields (Fighter first); the party's only Heavy wearer
    elixir: Hill Giant Strength every long rest in Acts 1–2 (Titanstring rider); Elixir of Vigilance every long rest in Act 3 (The Dead Shot needs no Strength)
    concentration: Hold Monster, or Hold Person on humanoids Charles is not holding; Hypnotic Pattern or Slow when paralysis is invalid; Silence over Charles's Hunger of Hadar on non-Holdable fights
  build_order: Fighter 1 at character creation → Swords Bard. One respec, at the Crèche once the Gloves of Dexterity are on (Fighter 1 re-taken first, then Bard 1–11).
  race: Wood Half-Elf
  background: Guild Artisan (Insight, Persuasion); proficiencies.md assumes this one
  starting_stats:
    STR: 10
    DEX:
      base: 8
      final: 18
      via: Gloves of Dexterity set DEX to 18 (Crèche, Act 1) and stay on all game
    CON: 16
    INT: 8
    WIS: 14
    CHA: 17
  stats_note: 'Creation: 8/15/14/8/10/15, +2 CHA, +1 DEX. Respec at the Crèche with the Gloves of Dexterity on: STR 10, DEX 8, CON 15 + 1 = 16, INT 8, WIS 14, CHA 15 + 2 = 17; Fighter 1 first, then Bard. The Gloves hold DEX at 18 all game.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss: DC 25 Religion check + 60% roll; Enhance Ability, Guidance, quicksave first). Birthright reaches CHA 22 in Act 3 if Gale is not using it.'
  ability_scores:
  - ability: STR
    steps:
    - score: 8
      source: 'point-buy at creation'
    - score: 10
      source: 'Crèche respec'
    - score: 21
      source: 'Elixir of Hill Giant Strength every long rest through Act 2; Act 3 drinks Vigilance instead, so STR sits at 10'
  - ability: DEX
    steps:
    - score: 15
      source: 'point-buy at creation'
    - score: 16
      source: '+1 Racial'
    - score: 18
      source: 'SET by Gloves of Dexterity (Crèche, Act 1), worn all game; the respec puts base DEX at 8 under them'
  - ability: CON
    steps:
    - score: 14
      source: 'point-buy at creation'
    - score: 16
      source: 'Crèche respec (15 + 1 Racial)'
  - ability: INT
    steps:
    - score: 8
      source: 'point-buy'
  - ability: WIS
    steps:
    - score: 10
      source: 'point-buy at creation'
    - score: 14
      source: 'Crèche respec'
  - ability: CHA
    steps:
    - score: 15
      source: 'point-buy'
    - score: 17
      source: '+2 Racial'
    - score: 18
      source: '+1 Hag''s Hair'
    - score: 20
      source: '+2 Mirror of Loss, Act 3 (DC 25 Religion check + 60% roll: Enhance Ability, Guidance, quicksave first)'
  feats:
  - at: Bard 4 (char 5)
    feat: Sharpshooter
  - at: Bard 8 (char 9)
    feat: Alert
    note: +5 initiative and Surprise immunity, so Hold Monster lands before the enemy's first turn. Taken over War Caster; Splint crit immunity, Helldusk damage reduction, the shield and Charles's aura carry the concentration save.
  fighting_styles:
  - Archery (Fighter)
  - Dueling (Bard)
  key_spells:
  - Glyph of Warding
  - Hold Monster
  - Confusion
  - Plant Growth
  - Magical Secrets → Command + Conjure Elemental
  creation:
    level1_class: Fighter 1 (taken at character creation, and re-taken first at the Crèche respec)
    level1_gains: 'Archery (+2 ranged), Second Wind, STR + CON saves, all armour incl. Heavy, shields, martial weapons, and 2 Fighter skills (Fighter first).'
    subclass_choice: College of Swords (Bard 3)
    proficiencies:
      armor_weapons: All armour, shields, martial weapons and Archery (Fighter 1); Medium armour + Scimitars (College of Swords).
      saving_throws: STR + CON (Fighter first); CON guards Hold Monster concentration.
      skills: Fighter 2 + Bard 1; Expertise ×4 (Bard 3 + Bard 10) + Jack of All Trades. The party face.
    starting_cantrips: '2 at Bard 1 (Minor Illusion, Friends), a 3rd at Bard 4 (Vicious Mockery), a 4th at Bard 10 (Mage Hand).'
    starting_spells: '4 known at Bard 1, +1 per Bard level (14 at Bard 11), plus the 2 Magical Secrets at Bard 10 on top: 16 known. One optional swap per level from Bard 2. No Shield reaction: stay at range.'
    notes: 'Wood Half-Elf. Fighter 1 at creation → Swords Bard 11, one respec at the Crèche (Fighter 1 first again). Bard 11 gives the L6 slot for a six-target Command. Feats at Bard 4 (char 5) and Bard 8 (char 9).'
  spells:
    note: Known caster, one optional swap per level from Bard 2. Mandatory = the Acuity-control engine; Recommended = the rest of the final list. 16 known at Bard 11 (14 Bard + 2 Magical Secrets).
    mandatory:
    - spell: 'Fighting Style: Archery'
      level: Feature (Fighter 1)
      school: N/A (passive)
      save: None
      when: char 1 (Fighter 1)
      why: +2 ranged attack; offsets Sharpshooter's −5 on every shot.
    - spell: Hold Monster
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (30:07) — paralysis is devastating but costs a level 5 slot and caps at two targets'
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Bard 9 (char 10)
      why: Paralyse; attacks within 3 m auto-crit, the set-up for Charles's smite nova. Upcast adds a target per slot above 5th. Concentration.
    - spell: Command
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (28:37) — concentration-free turn denial that upcasts to multiple enemies; every higher-level slot competes with it'
      level: '1'
      guide_level: 11
      school: Enchantment
      save: WIS save
      when: Bard 10 (Magical Secrets, char 11)
      why: Bonus action through the Band of the Mystic Scoundrel. +1 target per slot above 1st; the L6 slot hits six. DC uses CHA + Arcane Acuity.
    - spell: Glyph of Warding
      tier: S
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (45:04) — cast it directly on an enemy like a Fireball; non-concentration, six damage types, plus an AoE Dex-save sleep'
      level: '3'
      guide_level: 6
      school: Abjuration
      save: DEX save
      when: Bard 5 (char 6)
      why: 5d8 burst, element of choice; set as a ground trap before a fight or cast straight onto an enemy. No concentration.
    recommended:
    - spell: Plant Growth
      tier: B
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (20:19) — quarter movement, non-concentration, same footprint as Hunger of Hadar; but FLAMMABLE and useless versus ranged enemies'
      level: '3'
      school: Transmutation
      save: None
      when: Bard 8 (char 9)
      why: No concentration, no save; quarter movement in a 6 m circle. Cast between the pack and the back line, never on the melee cluster; layer it under Charles's Hunger of Hadar. ⚠ Fire burns it away.
    - spell: Confusion
      tier: B
      tier_note: 'Spells tier list, level 4, part 1 (Banishment through Fire Shield) (13:24) — hits enemies only, not allies; unreliable, but shut a door and the encounter kills itself'
      level: '4'
      guide_level: 8
      school: Enchantment
      save: WIS save
      when: Bard 7 (char 8)
      why: 6 m scramble; enemies attack at random or skip turns. Enemies only. Concentration.
    - spell: Hypnotic Pattern
      tier: A
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (10:24) — best when it catches the whole encounter; A only because it shares a role with Fear and Sleet Storm, and he would accept S'
      level: '3'
      guide_level: 6
      school: Illusion
      save: WIS save
      when: Bard 5 (char 6, swap for Dissonant Whispers)
      why: 9 m AoE incapacitate at her Acuity DC. Any damage wakes a target, so it buys one clean turn, not a lockdown. Concentration.
    - spell: Conjure Elemental
      tier: S
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (15:03) — an all-day summon as strong as an extra party member; all eight modes viable'
      level: '5'
      guide_level: 11
      school: Conjuration
      save: None
      when: Bard 10 (Magical Secrets, char 11)
      why: 'Second Secret. No concentration, lasts until long rest: cast the L6 version before the first fight and refund the slot with Spellcrux. Air Myrmidon (default): its flail Stuns on a failed DC 13 CON save, Raging Vortex is a no-save Silence. Earth Myrmidon tanks. Never Water or Fire.'
    - spell: Globe of Invulnerability
      tier: S
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (26:18) — total damage immunity wins most boss fights outright; get one cast into every Honour party'
      level: '6'
      guide_level: 11
      school: Abjuration
      save: None (Concentration)
      when: Scroll only — NOT selectable as a Magical Secret
      why: 'Not learnable (Magical Secrets stop at level 5; no Wizard dip to scribe). Buy scrolls for the Act 3 caster gauntlets and the Netherbrain. ⚠ Concentration: a scroll cast drops Hold Monster. Counterspell stays off her list; Gale and Charles carry it.'
    - spell: Hold Person
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (55:42) — paralysis costs turns and gives automatic crits within 10 ft; humanoids only, best with high save DC'
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Bard 3 (char 4)
      why: Single-humanoid paralyse from char 4 (auto-crit within 3 m); upcast adds targets. Concentration.
    - spell: Vicious Mockery
      tier: C
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (1:04:16) — too little damage to beat firing a bow; a late-game bard filler action only'
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 4 (char 5)
      why: Ranged fallback when the bow cannot fire; disadvantage on the target's next attack.
    - spell: Friends
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (26:48) — advantage on Charisma checks; COUNTS AS A CRIME ON TACTICIAN AND HONOUR MODE, so hide or fast-travel afterwards'
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: None (Concentration)
      when: Bard 1 (char 2)
      why: Advantage on Charisma checks against a non-hostile. Never on companions (approval loss when it ends); leave the area afterwards.
    - spell: Minor Illusion
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (35:56) — moves NPCs with no save or roll; clusters enemies for AoE, sets ambushes, pulls enemies one at a time'
      level: Cantrip
      school: Illusion
      save: None
      when: Bard 1 (char 2)
      why: Moves creatures toward a point with no save; groups enemies for Gale's Fireball and relocates NPCs for Asterion's theft routes.
    - spell: Slow
      tier: B
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (33:15) — targets six creatures so it spares allies, and bypasses incapacitation immunity; the reliable second-choice control spell'
      level: '3'
      guide_level: 7
      school: Transmutation
      save: WIS save
      when: Bard 6 (char 7)
      why: Undead- and construct-proof control; half speed, −2 AC and DEX saves, one action, casts can fail. For the fights where paralysis is invalid. Concentration.
    - spell: Healing Word
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (10:48) — ranged bonus-action revive, and the delivery system for Whispering Promise and Hellrider''s Pride buffs'
      level: '1'
      guide_level: 2
      school: Evocation
      save: None
      when: Bard 1 (char 2)
      why: Bonus-action ranged revive for the no-healer party. Triggers the Whispering Promise and Broodmother's Revenge in Act 1.
    - spell: Longstrider
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (27:03) — free all-day +10 movement on everyone including summons; he would put it in S+ if that existed'
      level: '1'
      guide_level: 2
      school: Transmutation
      save: None (ritual)
      when: Bard 1 (char 2)
      why: Ritual +3 m movement on the whole party until long rest, no concentration. She is the party's only copy; never swap it out.
    - spell: Heroism
      tier: C
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (16:32) — 5 temp HP per turn plus fear immunity, but needs long fights and no other temp HP source; he admits it is a pet spell'
      level: '1'
      school: Enchantment
      save: None (Concentration)
      when: Bard 1 (char 2) → swapped for Enhance Ability at Bard 4
      why: The concentration spell until Hold Person; one ally is immune to Frightened and gains 5 temporary HP each turn.
    - spell: Enhance Ability
      tier: B
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (36:31) — cast a couple of times a run; worth preparing for the few unavoidable skill checks'
      level: '2'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Bard 4 (char 5, swap for Heroism)
      why: Advantage on checks with one ability. Dialogue, theft, and the Mirror of Loss Religion check in Act 3. Out of combat only.
    - spell: Silence
      tier: A
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (43:29) — free as a ritual, shuts down enemy casters and noisy legendary actions; needs something holding them inside'
      level: '2'
      guide_level: 5
      school: Illusion
      save: None (Concentration)
      when: Bard 10 (char 11, the regular pick beside the Secrets)
      why: No-save zone; no spellcasting and no verbal escapes (Misty Step, Dimension Door) inside it. Cast over Charles's Hunger of Hadar on fights with nothing to Hold. Concentration.
    - spell: Dissonant Whispers
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (42:35) — concentration-free damage plus two turns of Frightened on a WIS save; effectively stuns melee enemies'
      level: '1'
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1 (char 2) → swapped for Hypnotic Pattern at Bard 5
      why: Early psychic damage plus Frightened on a WIS save, no concentration. Gone at char 6.
    - spell: Tasha's Hideous Laughter
      tier: A
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (52:09) — weak early because damage grants extra saves; late, a 10-turn disable that bypasses boss incapacitation immunities'
      level: '1'
      guide_level: 3
      school: Enchantment
      save: WIS save
      when: Bard 2 (char 3)
      why: Single-target incapacitate on a WIS save. Kept all game; through the Band it is a bonus action at her Acuity DC, and it bypasses boss incapacitation immunities.
    - spell: Invisibility
      tier: A
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (58:48) — wins no fights alone but invaluable for scouting and as a panic button; potions compete'
      level: '2'
      guide_level: 5
      wiki: Invisibility (spell)
      school: Illusion
      save: None
      when: Bard 4 (char 5)
      why: Scouting, theft setup and an escape. Kept all game; potions are the backup.
    - spell: Otto's Irresistible Dance
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (41:05) — no-save lockdown that bypasses legendary resistance; only for fights with one main enemy'
      level: '6'
      guide_level: 12
      school: Enchantment
      save: WIS save after the effect begins
      when: Bard 11 (char 12)
      why: Single-target shutdown when the L6 slot is not reserved for a six-target Command.
    - spell: Mage Hand
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (33:23) — costs a short-rest charge, but scouts, triggers traps, throws potions and soaks one enemy attack'
      level: Cantrip
      guide_level: 5
      school: Conjuration
      save: None
      when: Bard 10 (char 11), or drop
      why: Exploration and object use with no roll or concentration. Its Throw splashes a water bottle (2 m) to Wet a target for Gale's Cone of Cold or Chain Lightning.
  leveling:
  - char_level: 1
    class: Fighter 1
    gains:
    - Second Wind
    - STR + CON saving-throw proficiency
    - All armour, shields, and martial-weapon proficiency
    - Two Fighter skill proficiencies
    recommendations:
    - category: Fighting style
      picks: 1
      recommendation: Archery
      note: +2 to ranged attack rolls; offsets Sharpshooter on every projectile.
    - category: Skills
      picks: 2
      recommendation:
      - Intimidation
      - Perception
      note: 'Two picks, Fighter-first only. Intimidation must come from here (char 11 spends Expertise on it; no other list offers it). Perception is the most-rolled skill. Not Athletics.'
  - char_level: 2
    class: Bard 1
    gains:
    - Bardic Inspiration
    - Bard Spellcasting (2 cantrips and 4 spells known)
    - Bard skill selection
    recommendations:
    - category: Cantrips
      picks: 2
      recommendation:
      - Minor Illusion
      - Friends
      note: Minor Illusion groups enemies and moves NPCs with no save; Friends for dialogue, never on companions.
    - category: Spells
      picks: 4
      recommendation:
      - Healing Word
      - Longstrider
      - Dissonant Whispers
      - Heroism
      note: Bonus-action revive, ritual party movement, early Frightened control, and Heroism as the concentration spell until Hold Person.
    - category: Skill
      picks: 1
      recommendation: Deception
      note: 'One pick (multiclass Bard). It must be Deception: char 4 spends Expertise on it and no other list offers it. Wood Half-Elf grants no free skill.'
  - char_level: 3
    class: Bard 2
    gains:
    - Jack of All Trades
    - Song of Rest
    - One additional spell known
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Tasha's Hideous Laughter
      note: Cheap single-target incapacitate now; a bonus action at her Acuity DC through the Band in Act 3. Kept all game.
  - char_level: 4
    class: Swords Bard 3
    gains:
    - Blade Flourish and Slashing Flourish
    - Medium-armour and Scimitar proficiency
    - Expertise selections ×2
    - Level 2 Bard spells
    recommendations:
    - category: Subclass
      picks: 1
      recommendation: College of Swords
      note: Ranged Slashing Flourish is the multi-hit engine.
    - category: Fighting style
      picks: 1
      recommendation: Dueling
      note: A formality; neither Swords style touches a bow.
    - category: Expertise
      picks: 2
      recommendation:
      - Persuasion
      - Deception
      note: The party face.
    - category: Spell
      picks: 1
      recommendation: Hold Person
      note: The paralyse before Hold Monster; Charles's melee auto-crits within 3 m.
  - char_level: 5
    class: Swords Bard 4
    gains:
    - Third Bard cantrip
    - One additional spell known
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Sharpshooter
      note: +10 damage mode for the Act 1 spike. Toggle off below ~40% displayed hit chance.
    - category: Cantrip
      picks: 1
      recommendation: Vicious Mockery
      note: Ranged fallback when the bow cannot fire.
    - category: Spell
      picks: 1
      recommendation: Invisibility
      note: 'One new spell (7 known). Scouting, theft setup and an escape; kept all game.'
    - category: Replacement
      picks: 1
      optional: true
      recommendation: Heroism → Enhance Ability
      note: 'Hold Person now owns the concentration lane. Enhance Ability covers dialogue, theft and the Act 3 Mirror of Loss check.'
  - char_level: 6
    class: Swords Bard 5
    gains:
    - Font of Inspiration (Bardic Inspiration refreshes on short rest)
    - Improved Bardic Inspiration d8
    - Level 3 Bard spells
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Glyph of Warding
      note: 'One new spell (8 known). The pre-placed 5d8 burst.'
    - category: Replacement
      picks: 1
      optional: true
      recommendation: Dissonant Whispers → Hypnotic Pattern
      note: 'Keep Longstrider (the party''s only copy). Hypnotic Pattern buys one clean turn; any damage wakes the targets.'
  - char_level: 7
    class: Swords Bard 6
    gains:
    - Extra Attack
    - Countercharm
    - One additional spell known
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Slow
      note: Undead- and construct-proof control when paralysis is invalid.
  - char_level: 8
    class: Swords Bard 7
    gains:
    - Level 4 Bard spells
    - One additional spell known
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Confusion
      note: Wide-area control that scales with Arcane Acuity.
    - category: Replacement
      picks: 1
      optional: true
      recommendation: No swap
      note: 'Every known spell still earns its place. Greater Invisibility was weighed and dropped (Concentration; competes with Hold Monster).'
  - char_level: 9
    class: Swords Bard 8
    gains:
    - One additional spell known
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Alert
      note: +5 initiative and Surprise immunity so Hold Monster lands before enemies act. Splint crit immunity, Helldusk damage reduction and the shield cover the concentration save War Caster would have.
    - category: Spell
      picks: 1
      recommendation: Plant Growth
      note: 'No concentration, no save; quarter movement in 6 m. Cast between the pack and the back line, never on the melee cluster; layer it under Charles''s Hunger of Hadar.'
  - char_level: 10
    class: Swords Bard 9
    gains:
    - Level 5 Bard spells
    - One additional spell known
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Hold Monster
      note: 'One new spell (12 known); the level-5 list opens. Paralyse anything Hold Person cannot touch.'
    - category: Replacement
      picks: 1
      optional: true
      recommendation: No swap
      note: 'Every known spell still earns its place; Invisibility stays. Dominate Person (D tier) is not taken; Silence arrives as the regular Bard 10 pick next level.'
  - char_level: 11
    class: Swords Bard 10
    gains:
    - Magical Secrets selections ×2
    - Expertise selections ×2
    - Improved Bardic Inspiration d10
    - Fourth Bard cantrip
    - Spells known 12 → 13 (a regular Bard pick), plus the two Magical Secrets on top
    recommendations:
    - category: Magical Secrets
      picks: 2
      recommendation:
      - Command
      - Conjure Elemental
      note: 'Secrets stop at level 5 (no Globe of Invulnerability). Command: a bonus action through the Band, six targets from the L6 slot. Conjure Elemental: Air Myrmidon (Stun flail, no-save Silence vortex) or Earth Myrmidon (tank); never Water or Fire. Counterspell is the runner-up.'
    - category: Expertise
      picks: 2
      recommendation:
      - Insight
      - Intimidation
      note: Completes face and dialogue coverage; swap one for a campaign-specific skill if preferred.
    - category: Spell
      picks: 1
      recommendation: Silence
      note: 'The regular Bard 10 pick, a separate level-up step from the Secrets. Silence over Charles''s Hunger of Hadar on non-Holdable fights: no save, no casting, no Misty Step or Dimension Door out.'
    - category: Cantrip
      picks: 1
      recommendation: Mage Hand
      note: 'Fourth cantrip. Exploration and object use; its Throw can Wet a target with a water bottle for Gale''s Cone of Cold or Chain Lightning. Drop it if unused.'
  - char_level: 12
    class: Swords Bard 11
    gains:
    - Level 6 Bard spells
    - One additional spell known
    - A level 6 spell slot (also upcasts Command to six targets)
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Otto's Irresistible Dance
      note: Single-target shutdown when the L6 slot is not reserved for a six-target Command.
  itemization:
    act1:
    - id: titanstring-bow
      item: Titanstring Bow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (32:39) — adds your strength modifier; best in slot Act 1 damage with a giant strength elixir'
      slot: weapons
      bis: true
      note: 'Brem, Zhentarim hideout, after Find the Missing Shipment. Her bow for Acts 1–2. Drink an Elixir of Hill Giant Strength every long rest for the +5 rider on every projectile; skip the Club of Hill Giant Strength.'
    - id: act1-offhand-bonbon
      item: Safeguard Shield
      tier: A
      tier_note: '5wATdII3wmI (13:55) — +1 saving throws with no story requirement; usually the earliest upgrade over a plain shield'
      slot: weapons
      note: 'Dammon, the Grove. Sits in the inactive melee set: +2 AC and +1 to all saves while she shoots. Fighter 1 gives shield proficiency. Replaced by the Sentinel Shield at Moonrise.'
    - id: knife-of-the-undermountain-king-offhand
      item: Knife of the Undermountain King
      tier: S
      tier_note: 'jeSeVkmqmuc (21:07) — +2 shortsword; wider crit range, damage-dice rerolls, advantage in darkness; stat stick for anyone'
      slot: weapons
      note: 'Crèche stat stick; main hand until the Resonance Stone, shield in the off hand. Organ Rearranger lowers the crit threshold on ranged and spell attacks too. ⚠ Whether it fires from the inactive set is unverified. Goes to Charles at the Stone.'
    - id: elixir-of-hill-giant-strength
      item: Elixir of Hill Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (30:26) — sets Strength to 21; S used normally, and S+ ABOVE THE SCALE if drunk daily to skip strength investment'
      slot: consumables
      note: 'One every long rest through Act 2; STR 21 puts +5 on every Titanstring projectile. Skip the Club. Stock heavily; Asterion drinks one daily too.'
    - id: arrows-of-many-targets-bonbon-a1
      item: Arrow of Many Targets
      tier: S
      tier_note: 'ZMCimWeIxCk (42:03) — PLACED IN S+ TIER: near quadruple damage, four attack rolls, fastest Arcane Acuity stacking, plus a crit bug'
      slot: consumables
      note: 'Buy from every arrow vendor (Roah Moonglow, Dammon). One attack roll hits up to four targets and riders apply in full. The Act 1 opener for a spread pack.'
    - id: gloves-of-archery
      item: Gloves of Archery
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (15:11) — best in slot for any ranged attacker; flat +2 damage plus bow proficiency'
      slot: hands
      note: Grat, Goblin Camp. +2 damage on every ranged hit; worn until the Crèche.
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (25:38) — called the best item in the game for what it enables'
      rank: '#1'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #1 of 20 — sets Dexterity to 18 and adds +1 attacks, freeing ability points and feats'
      slot: hands
      bis: true
      note: 'A''jak''nir Jeera, Crèche Y''llek. DEX set to 18 and +1 to attack rolls, on every Flourish projectile. Worn all game: respec to DEX 8 (STR 10, CON 16, WIS 14) as soon as they are on.'
    - id: wondrous-gloves
      item: Wondrous Gloves
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (49:02) — best in slot for many bards and good enough on other characters too'
      slot: hands
      note: Grymforge Mimic loot. +1 AC and one extra Bardic Inspiration; a swap for a nova rest cycle when accuracy is already comfortable.
    - id: the-protecty-sparkswall
      item: The Protecty Sparkswall
      tier: S
      tier_note: 'TwFGCc8OOfw (16:41) — earliest chest slot +1 spell save DC; best in slot for casters through acts 1-2'
      rank: '#8'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #8 of 20 — +1 spell save DC on clothing makes it the caster default well into Act 2'
      slot: armour
      note: 'Gilded chest at the end of the trapped Grymforge bridge. +1 spell save DC for Hold Person and Hypnotic Pattern until the Adamantine Splint is poured. The Lightning Charge rider is dead on her.'
    - id: adamantine-scale-mail
      item: Adamantine Splint Armour
      tier: S
      tier_note: 'VjmWkRCoDWE (19:03) — 18 AC, crit immunity, 2 damage reduction and 3 turns of reeling; STORY EVENT LATE IN ACT 1'
      rank: '#15'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #15 of 20 — stronger damage reduction than the scale mail, and fewer serious alternatives'
      slot: armour
      bis: true
      note: 'First Mithral ore at the Adamantine Forge; she is the only Heavy wearer. AC 18, no critical hits against her, −2 to all incoming damage. Wear it over Protecty once poured; crit immunity protects concentration. (The id keeps an older name so checkoffs survive.)'
    - id: act1-ring2-bonbon
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'Open slot. The Whispering Promise until Asterion has the Staff of Arcane Blessing (its Bless is the same non-stacking condition), then pick per stretch.'
      options:
      - id: opt-whispering-promise
        item: The Whispering Promise
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (49:20) — a mainstay through Acts 1 and 2; very few parties would not benefit strongly'
        rank: '#10'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #10 of 20 — healing grants two turns of Bless, with no concentration or dedicated action'
        note: 'Volo, or Grat at the Goblin Camp, ~40 gp. Healing gives the target Bless for 2 turns with no concentration; her bonus-action Healing Word triggers it. Off once Asterion casts Bless.'
      - id: opt-crushers-ring
        item: Crusher's Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (9:50) — movement speed is universally applicable; an extremely rare party leaves it on the table'
        note: 'Crusher, Goblin Camp. +3 m movement; stacks with Longstrider.'
      - id: opt-ring-of-protection
        item: Ring of Protection
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (34:55) — raises the party''s average AC; give it to the easiest-to-hit member'
        rank: '#20'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #20 of 20 — +1 AC and all saves fits almost anyone, for the whole game'
        note: "Mol's reward for Steal the Sacred Idol. +1 AC and +1 to all saving throws."
      - id: opt-bracing-band
        item: Bracing Band
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (6:13) — good for a lot of characters, though there are often better options'
        note: "Sergeant Thrinn, Grymforge, for Find the Missing Boots. +1 AC after a Shove."
    - id: caustic-band
      item: Caustic Band
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (7:16) — for almost every party; goes on whoever makes the most attacks in a round'
      rank: '#12'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #12 of 20 — a passive 2 acid on every weapon attack, which adds up on multiattackers'
      slot: ring 1
      note: 'Derryth, Myconid Colony (Underdark). +2 Acid on every weapon hit, Flourish projectiles included. Weapon attacks only, not Unarmed, so never Asterion''s.'
    - id: act1-head-bonbon
      item: Head slot
      slot: head
      wiki: false
      note: 'Pick one: Diadem for damage, Grymskull for crit immunity. Both leave for the Helmet of Arcane Acuity in Act 2. The Warped Headband is a dialogue swap only.'
      options:
      - id: diadem-of-arcane-synergy
        item: Diadem of Arcane Synergy
        tier: S
        tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (21:57) — a huge damage boost even for characters outside the builds designed around it'
        note: 'Ardent Jhe''rezath, Crèche. After she lands a condition, every ranged hit adds her CHA modifier. The damage pick.'
      - id: grymskull-helm
        item: Grymskull Helm
        tier: S
        tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (25:05) — features in most parties and makes a playthrough much safer'
        note: 'Grym, Adamantine Forge. No critical hits against her and Fire resistance; Heavy, so only she can wear it. The safety pick.'
      - id: opt-warped-headband-of-intellect-bonbon
        item: Warped Headband of Intellect
        tier: A
        tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (47:26) — sets Intelligence to 17 for wizard dips, Eldritch Knights and dialogue checks'
        note: 'Lump the Enlightened, Blighted Village barn (loot him). Dialogue swap: INT set to 17 for Arcana, History, Investigation and Religion checks, including the Mirror of Loss Religion check. Never in combat.'
    - id: broodmother-s-revenge
      item: Broodmother's Revenge
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (21:11) — free to trigger, which is what pushes it to the top'
      rank: '#17'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #17 of 20 — the largest early per-hit damage die, but it needs a healing trigger'
      slot: amulets
      note: 'Kagha, after the Grove is saved (knock her out non-lethally, loot it). Any heal, even a potion at full HP, adds +1d6 Poison to every projectile for 2 turns; Healing Word triggers it. Skip against poison-immune enemies.'
    - id: boots-of-speed
      item: Boots of Speed
      tier: A
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (11:29) — bonus-action double move; some party member almost always wants it (captions garble the letter)'
      rank: '#14'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #14 of 20 — bonus-action Dash gives anyone Rogue-grade mobility'
      slot: feet
      note: 'Thulla, Ebonlake Grotto (Underdark). Bonus-action Dash for a character with no innate mobility. Not Asterion''s: Step of the Wind covers him. ⚠ The opportunity-attack rider is bugged; take them for the Dash.'
    - id: act1-cloak-bonbon
      item: No cloak exists yet
      slot: cloaks
      note: Empty by design. The only Act 1 magical cloak (Deathstalker Mantle) is Asterion's; her first cloak is at Last Light Inn.
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (35:18) — broken like all the Arcane Acuity items, and one of the easiest to use'
      slot: head
      bis: true
      note: 'Mason''s Guild, Reithwin Town. Every weapon hit gives 2 turns of Arcane Acuity (+1 spell attack and +1 spell save DC per turn, cap 10). Two Flourishes are four hits, +8; a Hasted turn caps it. ⚠ Damage taken strips 2 turns.'
    - id: act2-ranged-bonbon
      item: Titanstring Bow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (32:39) — adds your strength modifier; best in slot Act 1 damage with a giant strength elixir'
      held: 1
      slot: ranged weapons
      bis: true
      note: 'Carried over. STR rider on every projectile with the daily Hill Giant elixir; Gale''s Drakethroat Glaive enchants it Cold each long rest, which feeds the Snowburst Ring. Replaced by The Dead Shot in Act 3.'
    - id: act2-melee-bonbon
      item: Knife of the Undermountain King
      tier: S
      tier_note: 'jeSeVkmqmuc (21:07) — +2 shortsword; wider crit range, damage-dice rerolls, advantage in darkness; stat stick for anyone'
      held: 1
      slot: weapons
      note: 'Main hand until the Stone. The melee set is never swung; it is a rack of holder passives. At the Resonance Stone Phalar Aluve takes the hand and the Knife goes to Charles.'
    - id: act2-safeguard-bonbon
      item: Safeguard Shield
      tier: A
      tier_note: '5wATdII3wmI (13:55) — +1 saving throws with no story requirement; usually the earliest upgrade over a plain shield'
      held: 1
      slot: weapons
      note: 'Off hand until Moonrise. +2 AC and +1 to all saves from the inactive set, until the Sentinel Shield.'
    - id: phalar-aluve-bonbon
      item: Phalar Aluve
      tier: S
      tier_note: 'The BEST WEAPON TYPE in BG3 - Versatile Weapons Honor Mode Tier List and Guide - Act 1 (30:10) — one of the best weapons in the game even ignoring the strongest thing it does'
      slot: weapons
      bis: true
      note: 'From Charles at the Stone respec; main hand for the rest of the run, shield beside it. Shriek is an action (Haste action on turn 1, or pre-cast from stealth): 6 m aura on her, ends if unequipped. Always Shriek, never Sing. Stand 3–6 m from the targets.'
    - id: act2-offhand-bonbon
      item: Sentinel Shield
      tier: S
      tier_note: '5wATdII3wmI (31:06) — +3 initiative replaces Alert entirely; only downside is that ONLY ONE EXISTS'
      slot: weapons
      note: 'Lann Tarv, Moonrise main floor, ~580 gp. Default off hand from Act 2 to the end: +2 AC and +3 initiative from the inactive melee set. ⚠ Only the AC carry is wiki-confirmed; check initiative on the sheet with the bow drawn.'
      options:
      - id: opt-sentinel-shield-bonbon
        item: Ketheric's Shield
        tier: S
        tier_note: '5wATdII3wmI (30:04) — +1 spell save DC and spell attack in a slot that never gets it; also boosts Shield Bash'
        note: 'Ketheric Thorm, Mind Flayer Colony (his second fight), or pickpocketed after disarming him. +2 AC, advantage on DEX saves, +1 spell save DC and spell attack. Swap in for fights where +1 DC matters more than +3 initiative.'
    - id: act2-chest-bonbon
      item: Adamantine Splint Armour
      tier: S
      tier_note: 'VjmWkRCoDWE (19:03) — 18 AC, crit immunity, 2 damage reduction and 3 turns of reeling; STORY EVENT LATE IN ACT 1'
      rank: '#15'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #15 of 20 — stronger damage reduction than the scale mail, and fewer serious alternatives'
      held: true
      slot: armour
      bis: true
      note: Carried over. AC 18, crit immunity and −2 on every hit; the shield adds 2 more. Crit immunity protects Hold concentration and stops Acuity being stripped by big hits.
    - id: act2-hands-bonbon
      item: Gloves of Dexterity
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (25:38) — called the best item in the game for what it enables'
      rank: '#1'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #1 of 20 — sets Dexterity to 18 and adds +1 attacks, freeing ability points and feats'
      held: true
      slot: hands
      bis: true
      note: Carried over. DEX 18 and +1 attack rolls; every hit is an Acuity stack. Nothing in Act 2 beats it.
    - id: act2-elixir-bonbon
      item: Elixir of Hill Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (30:26) — sets Strength to 21; S used normally, and S+ ABOVE THE SCALE if drunk daily to skip strength investment'
      held: 1
      slot: consumables
      note: 'Carried over: one every long rest for the Titanstring rider (+5 per projectile). The last act she drinks it.'
    - id: arrows-of-many-targets-bonbon-a2
      item: Arrow of Many Targets
      tier: S
      tier_note: 'ZMCimWeIxCk (42:03) — PLACED IN S+ TIER: near quadruple damage, four attack rolls, fastest Arcane Acuity stacking, plus a crit bug'
      slot: consumables
      note: 'Restock at Roah Moonglow (Moonrise) and Dammon (Last Light). One roll, up to four targets, riders in full: two arrows cap Arcane Acuity on turn 1 without Haste, and with Cold each target gets Snowburst ice.'
    - id: spellcrux-amulet
      item: Spellcrux Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (33:07) — plainly incredible'
      slot: amulets
      note: 'The Warden, Moonrise Towers prison. Bonus action: restore one expended slot of any level, once per long rest. In Act 3, cast the L6 Myrmidon before the first fight, then refund the L6 slot. Replaces Broodmother''s.'
    - id: act2-rings-bonbon
      item: Caustic Band
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (7:16) — for almost every party; goes on whoever makes the most attacks in a round'
      rank: '#12'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #12 of 20 — a passive 2 acid on every weapon attack, which adds up on multiattackers'
      slot: ring 1
      bis: true
      note: 'Carried over. +2 Acid on every arrow and Flourish projectile. Ring 1 until the Band of the Mystic Scoundrel in Act 3.'
    - id: act2-ring2-bonbon
      item: Snowburst Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (42:08) — free ice surfaces on any cold damage; best in slot for a cold dealer'
      slot: ring 2
      wiki: Snowburst Ring
      note: 'Last Light Inn, loose plank in the bedroom north of the bar (DC 10 Perception). Every Cold hit drops a 4.5 m ice circle for 2 turns (DEX save or Prone); needs Gale''s Drakethroat set to Cold. ⚠ Shoot the back line first; ice under Charles can end his Hold.'
      options:
      - id: opt-whispering-promise-hold
        item: The Whispering Promise
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (49:20) — a mainstay through Acts 1 and 2; very few parties would not benefit strongly'
        rank: '#10'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #10 of 20 — healing grants two turns of Bless, with no concentration or dedicated action'
        note: 'Only until Asterion has the Staff of Arcane Blessing; after that its Bless is the same non-stacking condition and it does nothing.'
      - id: opt-ring-of-mental-inhibition
        item: Ring of Mental Inhibition
        tier: B
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (24:59) — powerful if the party is carefully built around it, but it needs very specific builds'
        note: 'House in Deep Shadows. Mental Fatigue on any enemy that fails a save against her; the next control lands more easily.'
      - id: opt-callous-glow-ring
        item: Callous Glow Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
        note: '+2 Radiant per projectile against illuminated targets. Gale''s, and it fights Charles''s Darkness.'
    - id: cloak-of-cunning-brume
      item: Cloak of Cunning Brume
      tier: A
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (9:53) — best for certain strategies rather than universally good'
      slot: cloaks
      note: 'Mattis, Last Light Inn, ~70 gp. Disengaging leaves a 2 m fog cloud for a turn; the backline escape button. Upgraded in Act 3.'
    - id: act2-feet-bonbon
      item: Boots of Brilliance
      tier: B
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (42:08) — regains one Bardic Inspiration but needs fiddly swapping (captions garble the letter)'
      slot: feet
      note: 'Heavy chest in the room north of Yurgir, Gauntlet of Shar. Restores one Bardic Inspiration per long rest. Flourish spends Inspiration only on a hit, so this is a small edge; Boots of Speed stay bagged.'
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      tier: S
      tier_note: 'ULTIMATE Guide to Rings - BG3 Honor Mode Tier List and Guide - Act 3 (8:21) — tons of builds are built around maximising it; locks enemies down'
      slot: ring 1
      bis: true
      note: 'Backpack in the Chult jungle through Akabi''s wheel at the Circus (one party member goes; send her). After a weapon hit, Enchantment and Illusion spells become bonus actions: Flourish, then Hold Monster or six-target Command the same turn. ⚠ Those spells cannot be cast as an action that turn.'
    - id: act3-ring2-bonbon
      item: Ring of Feywild Sparks
      tier: S
      tier_note: 'ULTIMATE Guide to Rings - BG3 Honor Mode Tier List and Guide - Act 3 (23:24) — an UNLISTED plus one spell save DC on any caster, the only ring that grants it'
      held: false
      slot: ring 2
      note: 'Auntie Ethel, Blushing Mermaid. Hidden +1 spell save DC (not on the tooltip) on every Hold Monster, Command and Confusion. Ring 2 for Act 3.'
      options:
      - id: opt-caustic-band-bonbon-a3
        item: Caustic Band
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (7:16) — for almost every party; goes on whoever makes the most attacks in a round'
        rank: '#12'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #12 of 20 — a passive 2 acid on every weapon attack, which adds up on multiattackers'
        note: 'Carried over from Acts 1–2. Swap in when +2 Acid on 4–8 projectiles beats +1 DC: trash packs with nothing worth Holding.'
    - id: act3-ranged-bonbon
      item: The Dead Shot
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (55:41) — improved crit and double proficiency to hit; his pick for endgame two-handed bow'
      held: false
      slot: ranged weapons
      bis: true
      note: 'Fytz the Firecracker, Stormshore Armoury. +2 longbow; Keen Attack doubles proficiency on its ranged attacks (+5 to hit over Titanstring at char 9+) and it crits on 19. ⚠ Keen Attack switches off under disadvantage: never shoot into Charles''s Darkness.'
      options:
      - id: opt-titanstring-bow-bonbon-a3
        item: Titanstring Bow
        tier: S
        tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (32:39) — adds your strength modifier; best in slot Act 1 damage with a giant strength elixir'
        note: 'Bagged. Swap in when hit chance is already ≥ 75% (Bless, a Held target); its STR rider needs a Giant Strength elixir that day instead of Vigilance.'
    - id: act3-melee-bonbon
      item: Phalar Aluve
      tier: S
      tier_note: 'The BEST WEAPON TYPE in BG3 - Versatile Weapons Honor Mode Tier List and Guide - Act 1 (30:10) — one of the best weapons in the game even ignoring the strongest thing it does'
      held: 2
      slot: weapons
      bis: true
      note: 'Carried over; main hand for the run. Shriek every fight from 3–6 m of the cluster; the set is still never swung. Viconia''s Walking Fortress is Charles''s.'
    - id: act3-offhand-bonbon
      item: Sentinel Shield
      tier: S
      tier_note: '5wATdII3wmI (31:06) — +3 initiative replaces Alert entirely; only downside is that ONLY ONE EXISTS'
      held: 2
      slot: weapons
      note: 'Carried over from Moonrise. +2 AC and +3 initiative from the inactive melee set. ⚠ Only the AC carry is wiki-confirmed; check initiative on the sheet with the bow drawn.'
      options:
      - id: opt-ketherics-shield-bonbon-a3
        item: Ketheric's Shield
        tier: S
        tier_note: '5wATdII3wmI (30:04) — +1 spell save DC and spell attack in a slot that never gets it; also boosts Shield Bash'
        note: 'Bagged. Swap in for the fight where +1 spell save DC matters more than +3 initiative: a single-boss Hold Monster.'
    - id: act3-elixir-bonbon
      item: Elixir of Vigilance
      tier: S
      tier_note: '9BcQXb37Bik (57:59) — rated S+ ABOVE THE SCALE: a free Alert feat, and +5 on a d4 initiative roll means going first'
      slot: consumables
      note: 'One every long rest in Act 3: +5 initiative and Surprise immunity, ~25 gp (Danthelon, Popper). The Dead Shot needs no Strength, so Giant Strength stops; Asterion keeps drinking it.'
    - id: arrows-of-many-targets-bonbon-a3
      item: Arrow of Many Targets
      tier: S
      tier_note: 'ZMCimWeIxCk (42:03) — PLACED IN S+ TIER: near quadruple damage, four attack rolls, fastest Arcane Acuity stacking, plus a crit bug'
      slot: consumables
      note: 'Restock at Dammon (Forge of the Nine) and the Lower City arrow vendors. One roll, up to four targets: the turn-1 Acuity filler before the bonus-action Hold Monster or Command. ⚠ Whether the Cold or Titan rider reaches the secondary targets is unverified.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 3 (13:32) — the only real decision left is who to put it on'
      slot: amulets
      note: 'Not hers. CON 23 and advantage on CON saves; Charles has the Risky Ring disadvantage it cancels. She keeps the Spellcrux Amulet.'
    - id: act3-amulet-bonbon
      item: Spellcrux Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (33:07) — plainly incredible'
      held: true
      slot: amulets
      note: Carried over. Bonus-action refund of one slot per long rest; cast the L6 Myrmidon before the first fight, refund the slot, and the six-target Command is still there.
    - id: helldusk-armour-bonbon
      item: Helldusk Armour
      tier: S
      tier_note: 'VjmWkRCoDWE (57:31) — 21 AC, 3 damage reduction, anyone can wear it; ALSO S IF GRABBED IN ACT 1 BY EXPLOIT'
      slot: armour
      bis: true
      note: 'Raphael, House of Hope. AC 21, −3 on every hit, Fire resistance, Burning immunity, Fly once per long rest; no proficiency needed. Chip damage becomes zero: no concentration save, no Acuity lost. ⚠ Heavy, so Stealth at disadvantage.'
      options:
      - id: opt-armour-of-agility
        item: Armour of Agility
        tier: S
        tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (1:00:01) — 17 AC uncapped by Dex and +2 saves; the highest AC setup in the game'
        note: 'Gloomy Fentonson, Stormshore Armoury. Medium: AC 17 + full DEX (21 at DEX 18), +2 to all saves, no Stealth penalty. Take it when +2 saves beat −3 damage reduction. ⚠ No Medium Armour Master or Magic Initiate: Cleric; either breaks the passive.'
      - id: opt-bhaalist-armour-bonbon
        item: Bhaalist Armour
        tier: S
        tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (42:20) — piercing vulnerability aura breaks the game; LOCKED BEHIND A STORY EVENT, SOME RUNS ONLY'
        note: 'Bhaal path only (Echo of Abazigal, after the Murder Tribunal). Nova swap for a single-boss Hold fight: stand within 3 m of the Held target, every projectile crits and Piercing is doubled. AC 17; the aura helps nobody else.'
    - id: wavemother-s-cloak
      item: Wavemother's Cloak
      tier: D
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (38:55) — a worse duplicate of another cloak''s effect, and combat-only'
      slot: cloaks
      note: 'Opulent chest behind Allandra Grey''s desk, Water Queen''s House upper floor. Once per turn in combat: +2 AC, +2 saves, Fire resistance until she takes damage. On a backline shooter it rarely falls off.'
    - id: act3-hands-bonbon
      item: Gloves of Dexterity
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (25:38) — called the best item in the game for what it enables'
      rank: '#1'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #1 of 20 — sets Dexterity to 18 and adds +1 attacks, freeing ability points and feats'
      held: 1
      slot: hands
      bis: true
      note: 'Worn all game. DEX 18 and +1 to attack rolls over a base DEX of 8; nothing in Act 3 replaces them.'
    - id: act3-head-bonbon
      item: Helmet of Arcane Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (35:18) — broken like all the Arcane Acuity items, and one of the easiest to use'
      held: true
      slot: head
      bis: true
      note: 'Carried over. Three or four hits a turn reach the +10 Acuity cap. Birthright stays bagged as the dialogue swap (+2 CHA; stacks with the Mirror for 24).'
    - id: act3-feet-bonbon
      item: Boots of Persistence
      tier: B
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (51:25) — reasonable, though Freedom of Movement on one character is not a tremendous effect'
      slot: feet
      note: 'Dammon, Forge of the Nine (Lower City). Permanent Freedom of Movement and Longstrider; Fighter 1 supplies the Medium proficiency. Helldusk Boots are Charles''s.'
      options:
      - id: opt-boots-of-striding-bonbon
        item: Boots of Striding
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (16:09) — always worth looking at for the characters they suit'
        note: 'Per-fight swap once Charles wears Helldusk Boots. Focused Stride on casting a concentration spell blocks Prone and forced movement; Persistence covers Paralysed and Restrained. Wear Striding against Shove and knockdown fights.'
    progression:
    - id: prog-head
      item: 'Head: Grymskull Helm → Diadem of Arcane Synergy → Helmet of Arcane Acuity'
      slot: head
      note: Grymskull (free, Adamantine Forge) → Diadem (Crèche) → Helmet of Arcane Acuity (Mason's Guild, Act 2) for the rest of the run. Warped Headband of Intellect and Birthright are dialogue swaps only.
    - id: prog-armour
      item: 'Chest: The Protecty Sparkswall → Adamantine Splint Armour → Helldusk Armour'
      slot: armour
      note: Protecty (Grymforge) → Splint (first Mithral ore) → Helldusk (Raphael, House of Hope). Armour of Agility is the +2-saves option; Bhaalist Armour the Bhaal-path nova swap.
    - id: prog-hands
      item: 'Hands: Gloves of Archery → Gloves of Dexterity (all game)'
      slot: hands
      note: Gloves of Archery (Grat) until the Crèche → Gloves of Dexterity (A'jak'nir Jeera) from the Crèche to the end; respec to DEX 8 once they are on.
    - id: prog-feet
      item: 'Boots: Boots of Speed → Boots of Brilliance → Boots of Persistence'
      slot: feet
      note: Boots of Speed (Thulla) → Boots of Brilliance (Gauntlet of Shar) → Boots of Persistence (Dammon, Lower City); Boots of Striding per fight once Charles is in Helldusk Boots.
    - id: prog-cloaks
      item: 'Cloak: none available → Cloak of Cunning Brume → Wavemother''s Cloak'
      slot: cloaks
      note: Empty in Act 1 → Cloak of Cunning Brume (Mattis, Last Light) as the backline escape → Wavemother's Cloak (Water Queen's House) in Act 3, +2 AC and +2 saves every turn she is not hit.
    - id: prog-amulets
      item: 'Amulet: Broodmother''s Revenge → Spellcrux Amulet'
      slot: amulets
      note: Broodmother's Revenge (Kagha) in Act 1 → Spellcrux Amulet (Moonrise prison Warden) from Act 2 on; in Act 3 it refunds the morning Myrmidon's L6 slot.
    - id: prog-ring1
      item: 'Ring 1: Caustic Band → Band of the Mystic Scoundrel'
      slot: ring 1
      note: Caustic Band (Derryth) through Acts 1–2 → Band of the Mystic Scoundrel (Chult backpack, Circus) in Act 3.
    - id: prog-ring2
      item: 'Ring 2: The Whispering Promise → Snowburst Ring → Ring of Feywild Sparks'
      slot: ring 2
      note: The Whispering Promise until Asterion casts Bless → Snowburst Ring (Last Light Inn) in Act 2 with Drakethroat set to Cold → Ring of Feywild Sparks (Blushing Mermaid) in Act 3; Caustic Band is the Act 3 option.
    - id: prog-weapons
      item: 'Melee: Knife + Safeguard Shield → Phalar Aluve + Sentinel Shield (Moonrise / the Stone)'
      slot: weapons
      note: 'A rack she never swings. Knife of the Undermountain King (Crèche) + Safeguard Shield (Dammon) → Sentinel Shield (Lann Tarv, Moonrise) → Phalar Aluve (from Charles at the Stone). Ketheric''s Shield is the +1 DC option. Shield AC carries from the inactive set; verify the rest in game.'
    - id: prog-ranged
      item: 'Ranged: Titanstring Bow → The Dead Shot (Act 3)'
      slot: ranged weapons
      note: Titanstring (Brem) with a daily Hill Giant elixir through Act 2 → The Dead Shot (Fytz, Stormshore Armoury) in Act 3; Titanstring stays bagged for fights already at ≥ 75% hit chance.
    - id: prog-consumables
      item: 'Elixir: Hill Giant Strength (Acts 1–2) → Vigilance (Act 3); Arrows of Many Targets every act'
      slot: consumables
      note: 'Elixir of Hill Giant Strength every long rest for Titanstring → Elixir of Vigilance every long rest once The Dead Shot is in hand. Keep Arrows of Many Targets stocked in every act.'
  playstyle: |-
    - **Act 1 default:** Titanstring in the ranged set, Knife + Safeguard Shield in the melee set, an Elixir of Hill Giant Strength every long rest, Protecty for DC until the Splint is poured. Healing Word before a Flourish turn coats the arrows with Broodmother's poison.
    - **Sharpshooter toggle (Acts 1–2):** off below ~40% displayed hit chance (about 30% with advantage). Moot in Act 3 with The Dead Shot.
    - **Flourish every attack:** the Inspiration is spent only on a hit; a miss refunds it.
    - **Arrows of Many Targets:** open with one or two. One roll, up to four targets, riders in full; two arrows cap Arcane Acuity on turn 1 without Haste.
    - **Act 2 on:** two Flourishes are four Acuity triggers (+8); a Hasted turn caps at +10. Shoot the back line first so Snowburst ice lands away from Charles and Asterion; Gale's fire melts it.
    - **Act 3 turn:** Flourish (Acuity and the Band trigger), then bonus-action Hold Monster or six-target Command. Keen Attack switches off under disadvantage: never shoot into Charles's Darkness.
    - **Act 3 morning:** Elixir of Vigilance; cast Conjure Elemental (Air Myrmidon) from the L6 slot before the first fight; Spellcrux refunds the slot as a bonus action.
    - **Shriek, always:** from the Stone, activate Shriek off Phalar Aluve (action; the Haste action on turn 1, or pre-cast from stealth) and stand 3–6 m from the targets. Never Sing.
    - **Plant Growth:** between the pack and the back line, never on the melee cluster; layer it under Charles's Hunger of Hadar. No fire into the zone.
    - **Nothing to Hold:** Silence over Charles's Hunger of Hadar (no casting, no Misty Step out). Hypnotic Pattern or Slow against undead and constructs instead of Hold or Command.
    - **Arrow of Darkness:** the last attack of her turn, aimed at the ground so the cloud edge sits between Charles and the target. Nothing under the cloud is targetable afterwards.
    - **Drakethroat (Act 2 on):** at each long rest drop her bow beside Charles; Gale Twins Draconic Elemental Weapon (Cold) onto both (+1 attack, +1d4 Cold per projectile, until the next long rest). Pick it back up.
    - **Daylight carrier:** Gale casts Daylight on her main-hand melee weapon (Knife, then Phalar Aluve) once per long rest; it travels with her. Do not swap the main hand afterwards, and cast it before any Darkness Arrow.
    - **The melee set is a rack:** she never swings it. Shield AC pays out from the inactive set (wiki-confirmed); check the Knife crit, Sentinel initiative and Ketheric's DC on the sheet with the bow drawn.
    - **Lanes with Gale:** Bonbon holds the Concentration lane (Hold Person, Hold Monster); Gale runs non-concentration control (Extended Command). Never both on one target.
---
