---
nickname: Bonbon
builds:
- name: The Commander
  is_primary: true
  role: Ranged acuity control + damage + party face
  class: Swords Bard 11 / Fighter 1
  build_order: Fighter 1 at character creation → Swords Bard 1–11 (no respec, no Wizard dip).
  race: Half-Elf or Human (early shield)
  background: Entertainer or Guild Artisan (face)
  starting_stats:
    STR: 8
    DEX:
      base: 16
      final: 18
      via: Gloves of Dexterity — sets DEX to 18 (Crèche, Act 1)
    CON: 14
    INT: 10
    WIS: 10
    CHA: 17
  stats_note: Adopt Gloves of Dexterity (DEX 18) so spare DEX can go to CON/CHA; no INT needed now the Wizard dip is dropped.
  ability_targets: CHA 17 → 18 (Hag's Hair) → 20 (Mirror of Loss); 22 via a later ASI if using a shield.
  feats:
  - at: Bard 4 (char 5)
    feat: Sharpshooter
  - at: Bard 8 (char 9)
    feat: War Caster
    note: 'Advantage on CON saves to hold Hold Monster — the party''s melee auto-crit engine — plus opportunity-spell casting. (Chosen over Dual Wielder — hand crossbows are Light and dual-wield without it.)'
  fighting_styles:
  - Archery (Fighter)
  - Dueling (Bard)
  key_spells:
  - Glyph of Warding
  - Hold Monster
  - Confusion
  - Fear
  - Magical Secrets → Command + Counterspell
  creation:
    level1_class: Fighter 1 (taken at character creation)
    level1_gains: Archery fighting style (+2 ranged), Second Wind, and — because Fighter is taken FIRST — STR + CON save proficiency, all armour (incl. Heavy) + Shields + Martial weapons, and 2 Fighter skills.
    subclass_choice: College of Swords (Bard 3)
    proficiencies:
      armor_weapons: All armour + shields + martial + Archery (Fighter 1); Medium + Scimitars (College of Swords).
      saving_throws: STR + CON (Fighter-first) — CON guards Hold Monster concentration.
      skills: Fighter 2 + Bard skills; Expertise ×4 (Bard 3 + 10) + Jack of All Trades — the party face.
    starting_cantrips: 'Bard: 2 at Bard 1 (Vicious Mockery, Friends) → 4 by Bard 10.'
    starting_spells: 'Bard: 4 known at Bard 1 → ~14 by Bard 11, plus 2 Magical Secrets at Bard 10. No Wizard dip, so no Shield reaction — lean on range, positioning, and the Fighter dip''s heavy armour instead.'
    notes: 'Half-Elf/Human. Order: Fighter 1 at character creation → Swords Bard ×11 (no respec). Bard 11 = caster level 11 → a single L6 slot, so Command still hits up to 6 targets WITHOUT a Wizard dip. Dropping Wizard costs only the Shield reaction + scroll scribing; the mass-Command ceiling is unchanged. Feats/ASIs at Bard class levels 4 (char 5) and 8 (char 9).'
  spells:
    note: Bard is a known caster (Always Prepared, replace 1 per level-up). Mandatory = the acuity-control engine; Recommended = the wider control/utility toolbox.
    mandatory:
    - spell: 'Fighting Style: Archery'
      level: Feature (Fighter 1)
      school: N/A (passive)
      save: None
      when: char 1 (Fighter 1)
      why: +2 ranged attack — offsets Sharpshooter's −5 and lands the big Titanstring shots in Act 1; later carries the dual hand-crossbow Arcane-Acuity engine.
    - spell: Hold Monster
      level: '5'
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Paralyse — attacks within 3m auto-crit, the party's melee auto-crit engine for Charles's smites. Upcast adds +1 target per slot above 5th. Concentration.
    - spell: Command
      level: '1'
      school: Enchantment
      save: WIS save
      when: Bard 10 (Magical Secrets)
      why: The bonus-action loop via the Band of the Mystic Scoundrel; +1 target per slot above 1st, so the Bard-11 L6 slot (caster level 11) hits up to 6. DC uses CHA + Arcane Acuity.
    - spell: Glyph of Warding
      level: '3'
      school: Abjuration
      save: DEX save
      when: Bard 5
      why: Pre-placed AoE burst (5d8, choose element) set before a fight as a ground trap.
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
  - char_level: 2
    class: Swords Bard 1
    gains: Bardic Inspiration; 2 cantrips + 4 spells known (Vicious Mockery, Friends, Healing Word); Bard skills + Expertise setup
  - char_level: 3
    class: Swords Bard 2
    gains: Jack of All Trades (½ prof to non-proficient checks); Song of Rest
  - char_level: 4
    class: Swords Bard 3
    gains: 'College of Swords: Blade Flourish + Dueling fighting style, Medium armour + Scimitars; Expertise ×2; L2 spells (Hold Person)'
  - char_level: 5
    class: Swords Bard 4
    gains: 'Feat: Sharpshooter'
  - char_level: 6
    class: Swords Bard 5
    gains: L3 spells (Glyph of Warding, Fear, Hypnotic Pattern, Slow); Font of Inspiration (Bardic Inspiration on short rest)
  - char_level: 7
    class: Swords Bard 6
    gains: Extra Attack → two ranged Slashing Flourishes in one action (+8 Arcane Acuity/turn once the Helmet is online)
  - char_level: 8
    class: Swords Bard 7
    gains: L4 spells (Confusion)
  - char_level: 9
    class: Swords Bard 8
    gains: 'Feat: War Caster (advantage on CON saves to hold Hold Monster; opportunity-spell casting)'
  - char_level: 10
    class: Swords Bard 9
    gains: L5 spells (Hold Monster — the melee auto-crit engine; Dominate Person)
  - char_level: 11
    class: Swords Bard 10
    gains: Magical Secrets (Command + Counterspell); 2 more Expertise
  - char_level: 12
    class: Swords Bard 11
    gains: caster level 11 → the single L6 slot (Command up to 6 targets); +1 spell known
  itemization:
    act1:
    - id: titanstring-bow
      item: Titanstring Bow
      note: 'Titanstring Bow (Zhentarim Basement — Brem, after Find the Missing Shipment). Adds your STR modifier to damage — pair with an Elixir of Giant Strength (Hill 21 → Cloud 27) for +5 to +8 per hit. Two-handed longbow + Archery + Sharpshooter = big single / flourish shots; stronger in Act 1 than dual crossbows, which only pay off once the Acuity helmet is online.'
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      note: Gloves of Dexterity (DEX 18)
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      note: 'Helmet of Arcane Acuity (Mason''s Guild — +2 acuity/hit → +spell save DC). THE pivot: switch to dual hand crossbows now — more hits per turn stack Acuity far faster than Titanstring''s single big shots.'
    - id: dual-hand-crossbows
      item: Dual hand crossbows
      note: 'Two hand crossbows (Light — no Dual Wielder needed): main + off-hand + two Slashing-Flourish projectiles = 4+ Acuity stacks per turn to saturate the Helmet fast. (Ne''er Misser + Hellfire are earmarked for Asterion — pick a different pair.)'
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      note: Band of the Mystic Scoundrel (Akabi's Circus wheel → Chult jungle — cast Enchantment/Illusion as a bonus action after a weapon hit)
    - id: bow-alternative
      item: Bow alternative (initiative)
      note: 'If you ever want a bow again: Hellrider''s Longbow (Rivington) grants +initiative — handy for the controller who wants to act first; Gontr Mael is the top bow but grants NO initiative.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      note: Amulet of Greater Health (CON 23) — reallocated here to armour Hold Monster concentration; stacks with War Caster
  playstyle: |-
    - **Act 1 (Titanstring):** Archery + Titanstring Bow + an Elixir of Giant Strength; open with a big single shot or, from Bard 6, two ranged Slashing Flourishes (each projectile carries +STR and Sharpshooter's +10). No Acuity helmet yet, so a few big hits beat many small ones — dual crossbows come later.
    - **Act 2+ (pivot to dual hand crossbows):** with the Helmet of Arcane Acuity online, switch to two hand crossbows — main + off-hand + two Flourish projectiles = 4+ hits/turn to stack Arcane Acuity fast (cap 10 = +10 spell save DC).
    - **Control loop:** convert the stacked DC via the Band of the Mystic Scoundrel (Act 3) into a bonus-action Hold Monster / Command the same turn. Land a flourish EVERY turn (Acuity decays −1/turn, −2 per hit taken) to hold the DC.
    - The Bard-11 6th-level slot lets Command hit up to 6.
    - No Wizard dip = no Shield reaction; stay at range and use the Fighter dip's heavy armour + distance to protect concentration.
    - ⚠ **Hold Monster & Command have NO effect on undead** — carry Hypnotic Pattern / Slow for those fights (see the party undead-fallback plan).
---
