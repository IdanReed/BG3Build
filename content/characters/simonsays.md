---
nickname: SimonSays
builds:
- name: The Commander
  is_primary: true
  role: Ranged acuity control + damage + party face
  class: Swords Bard 10 / Fighter 1 / Wizard 1
  build_order: Pure Swords Bard to 7 → respec at 8 → Fighter 1 → Wizard 1 → Swords Bard 1–10.
  race: Half-Elf or Human (early shield)
  background: Entertainer or Guild Artisan (face)
  starting_stats:
    STR: 8
    DEX: 16
    CON: 14
    INT: 10
    WIS: 10
    CHA: 17
  stats_note: Adopt Gloves of Dexterity (DEX 18) then respec DEX points into INT 16.
  ability_targets: CHA 17 → 18 (Hag's Hair) → 20 (Mirror of Loss); 22 via a later ASI if using a shield.
  feats:
  - at: Bard 4 (retaken post-respec)
    feat: Sharpshooter
  - at: Bard 8
    feat: War Caster
    note: Swapped from Dual Wielder (useless on a two-handed longbow). Advantage on CON saves to hold Hold Monster — the party's melee auto-crit engine — plus opportunity-spell casting. (Triggers at Bard class level 8.)
  fighting_styles:
  - Archery (Fighter)
  - Dueling (Bard)
  key_spells:
  - Glyph of Warding
  - Hold Monster
  - Confusion
  - Fear
  - Magical Secrets → Command + Counterspell
  - Wizard → Shield
  creation:
    level1_class: Fighter 1 (first class in the final post-respec build)
    level1_gains: Archery fighting style (+2 ranged), Second Wind, and — because Fighter is taken FIRST — STR + CON save proficiency, all armour (incl. Heavy) + Shields + Martial weapons, and 2 Fighter skills.
    subclass_choice: College of Swords is chosen at Bard 3 (Blade Flourish, a fighting style, Medium armour + Scimitars); Extra Attack at Bard 6. The Fighter/Wizard dips have no subclass at these levels.
    proficiencies:
      armor_weapons: 'From Fighter 1 (first class): Light/Medium/Heavy armour, Shields, Simple + Martial weapons + the Archery fighting style. College of Swords also adds Medium armour + Scimitars.'
      saving_throws: Strength + Constitution — from Fighter as the FIRST class (CON = concentration insurance for Hold Monster / Fear / Confusion). Multiclassing into Bard/Wizard grants no additional save proficiency.
      skills: Fighter picks 2 (Perception + Athletics, or Insight for the face). Bard adds 3 skills + Expertise on 2 (Bard 3) and 2 more (Bard 10) + Jack of All Trades (Bard 2) — the face/skill engine. Background Entertainer/Guild Artisan adds 2.
    starting_cantrips: 'Bard: 2 at Bard 1 (Vicious Mockery, Friends) → 4 by Bard 10. The Wizard dip adds 3 INT cantrips (filler).'
    starting_spells: 'Bard: 4 known at Bard 1 → 13 by Bard 10 + 2 Magical Secrets. Wizard 1: 6 spellbook picks — MUST include Shield (there is no Shield scroll to transcribe).'
    notes: 'Half-Elf/Human. Final order (after the level-8 respec): Fighter 1 → Wizard 1 → Swords Bard ×10 = caster level 11 → a single L6 slot (the Wizard dip''s whole point: Command up to 6 targets). Pre-respec you play pure Swords Bard 1–7. Feats/ASIs at Bard class levels 4 and 8.'
  spells:
    note: Bard is a known caster (Always Prepared, replace 1 per level-up); Wizard-dip spells key off INT and re-prepare freely. Mandatory = the acuity-control engine; Recommended = the wider control/utility toolbox.
    mandatory:
    - spell: 'Fighting Style: Archery'
      level: Feature (Fighter 1)
      school: N/A (passive)
      save: None
      when: char 8 (Fighter 1, post-respec)
      why: +2 ranged attack for the Slashing-Flourish → Arcane-Acuity engine (Hellrider's Longbow → Gontr Mael).
    - spell: Hold Monster
      level: '5'
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Paralyse — attacks within 3m auto-crit, the party's melee auto-crit engine for Durc's smites. Upcast adds +1 target per slot above 5th. Concentration.
    - spell: Command
      level: '1'
      school: Enchantment
      save: WIS save
      when: Bard 10 (Magical Secrets)
      why: The bonus-action loop via the Band of the Mystic Scoundrel; +1 target per slot above 1st, so the Wizard-dip L6 slot hits up to 6. DC uses CHA + Arcane Acuity.
    - spell: Glyph of Warding
      level: '3'
      school: Abjuration
      save: DEX save
      when: Bard 5
      why: Pre-placed AoE burst (5d8, choose element) set before a fight as a ground trap.
    - spell: Shield
      level: '1'
      school: Abjuration
      save: None (reaction, INT via Wizard)
      when: char 9 (Wizard 1)
      why: +5 AC reaction and negates Magic Missile — the survivability payoff of the Wizard dip. Must be one of the 6 Wizard-1 picks (no Shield scroll exists).
    recommended:
    - spell: Fear
      level: '3'
      school: Illusion
      save: WIS save
      when: Bard 5
      why: 9m cone — frightened enemies drop weapons and can't act/approach; scales with CHA + Arcane Acuity. Concentration.
    - spell: Confusion
      level: '4'
      school: Enchantment
      save: WIS save
      when: Bard 7
      why: 6m scramble — enemies attack randomly / skip turns. Concentration.
    - spell: Hypnotic Pattern
      level: '3'
      school: Illusion
      save: WIS save
      when: Bard 5
      why: Best-in-class AoE lockdown (9m incapacitate); superb acuity payoff. Concentration; breaks on damage.
    - spell: Counterspell
      level: '3'
      school: Abjuration
      save: Reaction (contested by slot level)
      when: Bard 10 (Magical Secrets)
      why: Shuts off enemy casters as a Reaction.
    - spell: Hold Person
      level: '2'
      school: Enchantment
      save: WIS save
      when: Bard 3
      why: Cheaper single-target paralyse (auto-crit within 3m), available far earlier than Hold Monster — the early-game stand-in. Concentration.
    - spell: Dominate Person
      level: '5'
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Turn a humanoid against its allies; a flex 5th-level pick alongside Hold Monster. Concentration.
    - spell: Magic Missile
      level: '1'
      school: Evocation
      save: None (auto-hit force)
      when: char 9 (Wizard 1)
      why: Reliable chip damage and a dependable concentration-breaker; force is INT-independent so it stays useful at INT 16.
    - spell: Vicious Mockery
      level: Cantrip
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Psychic damage + disadvantage on the target's next attack; free ranged control that plays into acuity.
    - spell: Friends
      level: Cantrip
      school: Enchantment
      save: None (Concentration)
      when: Bard 1
      why: Advantage on Charisma checks vs a non-hostile creature — the face enabler. Never cast on companions (approval loss when it ends).
    - spell: Slow
      level: '3'
      school: Transmutation
      save: WIS save
      when: Bard 5
      why: UNDEAD-PROOF control (unlike Hold Monster/Command) — halves speed, −2 AC/DEX-saves, one action only, ~50% chance to fizzle a cast. Bank it as a known spell for the Act-2/undead/construct fights where paralyze doesn't work. Concentration.
    - spell: Healing Word
      level: '1'
      school: Evocation
      save: None
      when: Bard 1
      why: 'The no-healer party''s emergency pickup: bonus-action ranged revive/heal so a downed ally doesn''t cost a full turn. Cheap insurance to keep known — pairs with stocked Revivify scrolls.'
  leveling:
    respecs:
    - label: Level 1
      note: How you build from character creation and play until the level-8 respec — pure Swords Bard, no multiclassing yet.
      rows:
      - char_level: 1
        class: Swords Bard 1
        gains: Bardic Inspiration; 2 cantrips + 4 spells known (Vicious Mockery, Friends, Healing Word); Bard skills + Expertise setup
      - char_level: 2
        class: Swords Bard 2
        gains: Jack of All Trades (½ prof to non-proficient checks); Song of Rest
      - char_level: 3
        class: Swords Bard 3
        gains: 'College of Swords: Blade Flourish + Dueling fighting style, Medium armour + Scimitars; Expertise ×2; L2 spells (Hold Person)'
      - char_level: 4
        class: Swords Bard 4
        gains: 'Feat: Sharpshooter'
      - char_level: 5
        class: Swords Bard 5
        gains: L3 spells (Glyph of Warding, Fear, Hypnotic Pattern, Slow); Font of Inspiration (Bardic Inspiration on short rest)
      - char_level: 6
        class: Swords Bard 6
        gains: Extra Attack → two ranged Slashing Flourishes in one action (+8 Arcane Acuity on turn 1)
      - char_level: 7
        class: Swords Bard 7
        gains: L4 spells (Confusion); last level before the respec
    - label: Level 8 respec
      note: 'At char level 8, respec at Withers and rebuild from level 1 in this exact order. You''re char level 8 the moment the rebuild reaches Bard 6 (Extra Attack); levels 9–12 then continue as Bard 7–10. Final: Fighter 1 → Wizard 1 → Swords Bard ×10.'
      rows:
      - char_level: 1
        class: Fighter 1
        gains: 'Taken FIRST: Archery fighting style (+2 ranged), Second Wind; STR + CON save proficiency; all armour (incl. Heavy) + Shields + Martial weapons; 2 Fighter skills'
      - char_level: 2
        class: Wizard 1
        gains: Spellbook (6 picks — MUST include Shield; add Magic Missile); Arcane Recovery; scribe scrolls; 3 INT cantrips
      - char_level: 3
        class: Swords Bard 1
        gains: Bardic Inspiration; Bard cantrips + spells (Vicious Mockery, Friends, Healing Word)
      - char_level: 4
        class: Swords Bard 2
        gains: Jack of All Trades; Song of Rest
      - char_level: 5
        class: Swords Bard 3
        gains: 'College of Swords: Blade Flourish + Dueling style, Medium armour + Scimitars; Expertise ×2; L2 spells (Hold Person)'
      - char_level: 6
        class: Swords Bard 4
        gains: 'Feat: Sharpshooter (retaken)'
      - char_level: 7
        class: Swords Bard 5
        gains: L3 spells (Glyph of Warding, Fear, Hypnotic Pattern, Slow); Font of Inspiration
      - char_level: 8
        class: Swords Bard 6
        gains: Extra Attack — the rebuild catches up to your char level here; two ranged Slashing Flourishes/turn
      - char_level: 9
        class: Swords Bard 7
        gains: L4 spells (Confusion)
      - char_level: 10
        class: Swords Bard 8
        gains: 'Feat: War Caster (advantage on CON saves to hold Hold Monster; opportunity-spell casting)'
      - char_level: 11
        class: Swords Bard 9
        gains: L5 spells (Hold Monster — the melee auto-crit engine; Dominate Person)
      - char_level: 12
        class: Swords Bard 10
        gains: Magical Secrets (Command + Counterspell); 2 more Expertise; caster level 11 → the single L6 slot (Command up to 6 targets)
  itemization:
    act1:
    - id: hellrider-s-longbow
      item: Hellrider's Longbow
      note: Hellrider's Longbow (Rivington — initiative)
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      note: Gloves of Dexterity (DEX 18)
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      note: Helmet of Arcane Acuity (Mason's Guild — +2 acuity/hit → +spell save DC)
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      note: Band of the Mystic Scoundrel (Akabi's Circus wheel → Chult jungle — cast Enchantment/Illusion as a bonus action after a weapon hit)
    - id: gontr-mael
      item: Gontr Mael
      note: Gontr Mael (top bow — but it grants NO initiative; keep Hellrider's Longbow if you need to act first)
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      note: Amulet of Greater Health (CON 23) — reallocated here to armour Hold Monster concentration; stacks with War Caster
  playstyle: 'OPENING: with Extra Attack (Bard 6), Blade Flourish is NOT once-per-turn — fire TWO ranged Slashing Flourishes in one Attack action = 4 hits = +8 Arcane Acuity on turn 1 (not +4), then convert via the Band of the Mystic Scoundrel into a bonus-action Hold Monster at the boosted DC. Sustain: land a flourish EVERY turn (Acuity also decays −1/turn on top of −2 per hit taken) to hold the DC; cap 10 = +10 spell save DC. The Wizard-dip 6th-level slot lets Command hit up to 6. ⚠ Hold Monster & Command have NO effect on undead — see the party undead-fallback plan; carry Hypnotic Pattern/Slow for those fights.'
---

