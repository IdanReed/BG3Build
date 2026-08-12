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
    INT: 8
    WIS: 10
    CHA: 17
  stats_note: 'Point-buy base 8/15/14/8/10/15 = all 27 (DEX 15 + CHA 15 cost 9 each). +2 → CHA 17, +1 → DEX 16 → Gloves of Dexterity then set it to 18 (Crèche, Act 1). No INT (Wizard dip dropped).'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss). Birthright raises him to CHA 22 in Act 3 if Gale is not using it.'
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
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Paralyse — attacks within 3m auto-crit, the party's melee auto-crit engine for Charles's smites. Upcast adds +1 target per slot above 5th. Concentration.
    - spell: Command
      level: '1'
      guide_level: 11
      school: Enchantment
      save: WIS save
      when: Bard 10 (Magical Secrets)
      why: The bonus-action loop via the Band of the Mystic Scoundrel; +1 target per slot above 1st, so the Bard-11 L6 slot (caster level 11) hits up to 6. DC uses CHA + Arcane Acuity.
    - spell: Glyph of Warding
      level: '3'
      guide_level: 6
      school: Abjuration
      save: DEX save
      when: Bard 5
      why: Pre-placed AoE burst (5d8, choose element) set before a fight as a ground trap.
    recommended:
    - spell: Fear
      level: '3'
      guide_level: 9
      school: Illusion
      save: WIS save
      when: Bard 5
      why: 9m cone — frightened enemies drop weapons and can't act/approach; scales with CHA + Arcane Acuity. Concentration.
    - spell: Confusion
      level: '4'
      guide_level: 8
      school: Enchantment
      save: WIS save
      when: Bard 7
      why: 6m scramble — enemies attack randomly / skip turns. Concentration.
    - spell: Hypnotic Pattern
      level: '3'
      guide_level: 6
      school: Illusion
      save: WIS save
      when: Bard 5
      why: Best-in-class AoE lockdown (9m incapacitate); superb acuity payoff. Concentration; breaks on damage.
    - spell: Counterspell
      level: '3'
      guide_level: 11
      school: Abjuration
      save: Reaction (contested by slot level)
      when: Bard 10 (Magical Secrets)
      why: Shuts off enemy casters as a Reaction.
    - spell: Hold Person
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Bard 3
      why: Cheaper single-target paralyse (auto-crit within 3m), available far earlier than Hold Monster — the early-game stand-in. Concentration.
    - spell: Dominate Person
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Turn a humanoid against its allies; a flex 5th-level pick alongside Hold Monster. Concentration.
    - spell: Vicious Mockery
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Psychic damage + disadvantage on the target's next attack; free ranged control that plays into acuity.
    - spell: Friends
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: None (Concentration)
      when: Bard 1
      why: Advantage on Charisma checks vs a non-hostile creature — the face enabler. Never cast on companions (approval loss when it ends).
    - spell: Slow
      level: '3'
      guide_level: 7
      school: Transmutation
      save: WIS save
      when: Bard 5
      why: UNDEAD-PROOF control (unlike Hold Monster/Command) — halves speed, −2 AC/DEX-saves, one action only, ~50% chance to fizzle a cast. Bank it as a known spell for the Act-2/undead/construct fights where paralyze doesn't work. Concentration.
    - spell: Healing Word
      level: '1'
      guide_level: 2
      school: Evocation
      save: None
      when: Bard 1
      why: 'The no-healer party''s emergency pickup: bonus-action ranged revive/heal so a downed ally doesn''t cost a full turn. Cheap insurance to keep known — pairs with stocked Revivify scrolls.'
    - spell: Longstrider
      level: '1'
      guide_level: 2
      school: Transmutation
      save: None (ritual)
      when: Bard 1
      why: Free out-of-combat party movement buff that lasts until long rest and does not require Concentration.
    - spell: Enhance Ability
      level: '2'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Bard 4
      why: 'Advantage on checks using one chosen ability. At char 5, replace the now-redundant Faerie Fire with this and use it for consequential dialogue, theft, and exploration checks; it is an out-of-combat mode, not something to maintain alongside Hold Person.'
    - spell: Dissonant Whispers
      level: '1'
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Early psychic damage plus Frightened; a useful single-target control spell before the Acuity engine.
    - spell: Faerie Fire
      level: '1'
      guide_level: 2
      school: Evocation
      save: DEX save
      when: Bard 1
      why: Early area advantage and anti-invisibility tool. Concentration, so replace it once stronger control spells dominate.
    - spell: Tasha's Hideous Laughter
      level: '1'
      guide_level: 3
      school: Enchantment
      save: WIS save
      when: Bard 2
      why: Cheap early single-target incapacitation; a bridge to Hold Person that can later be replaced.
    - spell: Invisibility
      level: '2'
      guide_level: 5
      wiki: Invisibility (spell)
      school: Illusion
      save: None
      when: Bard 4
      why: Scouting, theft setup, and an emergency escape tool with strong out-of-combat utility.
    - spell: Otto's Irresistible Dance
      level: '6'
      guide_level: 12
      school: Enchantment
      save: WIS save after the effect begins
      when: Bard 11
      why: Immediate single-target shutdown for encounters where the level 6 slot is not reserved for an upcast Command.
    - spell: Mage Hand
      level: Cantrip
      guide_level: 5
      school: Conjuration
      save: None
      when: Bard 4
      why: 'Exploration and object-manipulation utility with no attack roll, save, or Concentration. For a no-slot Wet setup, drop a water bottle where the Hand can reach it and use the Hand''s Throw for a 2m splash.'
    - spell: Light
      level: Cantrip
      guide_level: 11
      school: Evocation
      save: None
      when: Bard 10
      why: Long-lasting illumination for dark areas without consuming a spell slot or Concentration.
  leveling:
  - char_level: 1
    class: Fighter 1
    gains:
    - Second Wind
    - STR + CON saving-throw proficiency
    - All armour, shields, and martial-weapon proficiency
    recommendations:
    - category: Fighting style
      recommendation: Archery
      note: +2 to ranged attack rolls offsets Sharpshooter and remains essential after the hand-crossbow pivot.
  - char_level: 2
    class: Bard 1
    gains:
    - Bardic Inspiration
    - Bard Spellcasting (2 cantrips and 4 spells known)
    - Bard skill selection
    recommendations:
    - category: Cantrips
      recommendation:
      - Vicious Mockery
      - Friends
      note: Mockery is the ranged fallback; Friends supports Bonbon's face role but should not be cast on companions.
    - category: Spells
      recommendation:
      - Healing Word
      - Longstrider
      - Dissonant Whispers
      - Faerie Fire
      note: Emergency pickup, ritual party movement, early single-target control, and an early advantage tool.
  - char_level: 3
    class: Bard 2
    gains:
    - Jack of All Trades
    - Song of Rest
    - One additional spell known
    recommendations:
    - category: Spell
      recommendation: Tasha's Hideous Laughter
      note: Cheap early control until Hold Person and the Acuity package arrive.
  - char_level: 4
    class: Swords Bard 3
    gains:
    - Blade Flourish and Slashing Flourish
    - Medium-armour and Scimitar proficiency
    - Expertise selections ×2
    - Level 2 Bard spells
    recommendations:
    - category: Subclass
      recommendation: College of Swords
      note: Ranged Slashing Flourish supplies the multi-hit engine.
    - category: Fighting style
      recommendation: Dueling
      note: Archery already handles the ranged plan; Dueling is the useful melee fallback.
    - category: Expertise
      recommendation:
      - Persuasion
      - Deception
      note: Establishes Bonbon as the party face.
    - category: Spell
      recommendation: Hold Person
      note: The early paralyse option before Hold Monster.
  - char_level: 5
    class: Swords Bard 4
    gains:
    - Third Bard cantrip
    - One additional spell known
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Sharpshooter
      note: The +10 damage mode is the Act 1 ranged spike; Archery and advantage offset its attack penalty.
    - category: Cantrip
      recommendation: Mage Hand
      note: 'General exploration utility without competing for concentration. For a no-slot Wet setup, drop a water bottle for the Hand and use its Throw on the Hand''s turn.'
    - category: Spells
      recommendation:
      - Invisibility
      - Enhance Ability
      note: Learn Invisibility as the new spell and use the level-up replacement to trade the early Faerie Fire bridge for Enhance Ability. Both are Concentration and are normally exploration tools once Hold Person is online.
  - char_level: 6
    class: Swords Bard 5
    gains:
    - Font of Inspiration (Bardic Inspiration refreshes on short rest)
    - Improved Bardic Inspiration d8
    - Level 3 Bard spells
    recommendations:
    - category: Spells
      recommendation:
      - Glyph of Warding
      - Hypnotic Pattern
      note: Learn one and replace an early flex spell with the other; these are the priority burst and control picks.
  - char_level: 7
    class: Swords Bard 6
    gains:
    - Extra Attack
    - Countercharm
    - One additional spell known
    recommendations:
    - category: Spell
      recommendation: Slow
      note: The undead- and construct-safe control choice when paralysis is invalid.
  - char_level: 8
    class: Swords Bard 7
    gains:
    - Level 4 Bard spells
    - One additional spell known
    recommendations:
    - category: Spell
      recommendation: Confusion
      note: Wide-area control that scales extremely well with Arcane Acuity.
  - char_level: 9
    class: Swords Bard 8
    gains:
    - One additional spell known
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: War Caster
      note: Advantage on concentration saves protects the later Hold Monster engine.
    - category: Spell
      recommendation: Fear
      note: Add it now as the flexible cone-control option without delaying the earlier core picks.
  - char_level: 10
    class: Swords Bard 9
    gains:
    - Level 5 Bard spells
    - One additional spell known
    recommendations:
    - category: Spells
      recommendation:
      - Hold Monster
      - Dominate Person
      note: Learn Hold Monster first and replace a lower-level flex spell for Dominate Person if both are wanted immediately.
  - char_level: 11
    class: Swords Bard 10
    gains:
    - Magical Secrets selections ×2
    - Expertise selections ×2
    - Improved Bardic Inspiration d10
    - Fourth Bard cantrip
    recommendations:
    - category: Magical Secrets
      recommendation:
      - Command
      - Counterspell
      note: Command is the Band-enabled bonus-action control engine; Counterspell supplies the missing reaction defence.
    - category: Expertise
      recommendation:
      - Insight
      - Intimidation
      note: Completes the face and dialogue coverage; swap one for a campaign-specific skill if preferred.
    - category: Cantrip
      recommendation: Light
      note: Reliable illumination without concentration.
  - char_level: 12
    class: Swords Bard 11
    gains:
    - Level 6 Bard spells
    - One additional spell known
    - A level 6 spell slot (also upcasts Command to six targets)
    recommendations:
    - category: Spell
      recommendation: Otto's Irresistible Dance
      note: Best-in-class single-target shutdown when the level 6 slot is not reserved for mass Command.
  itemization:
    act1:
    - id: titanstring-bow
      item: Titanstring Bow
      slot: weapons
      note: 'SELECTED ranged weapon. Buy Titanstring from Brem after Find the Missing Shipment. Archery + Sharpshooter + ranged Slashing Flourish apply its STR rider to large, accurate nova shots. Default to the STR 19 Club + Knife + Bloodlust package below; use a Hill Giant elixir for a single-target boss where Bloodlust cannot trigger.'
    - id: club-of-hill-giant-strength
      item: Club of Hill Giant Strength (melee main hand)
      slot: weapons
      note: 'SELECTED Titanstring stat stick from the Arcane Tower. Equip this Light club in the melee main hand with Knife of the Undermountain King off-hand while firing Titanstring from the ranged slot; STR 19 adds +4 damage to every projectile and preserves the elixir slot for Bloodlust.'
    - id: knife-of-the-undermountain-king-offhand
      item: Knife of the Undermountain King (melee off-hand)
      slot: weapons
      note: 'SELECTED Crèche stat stick beside the Light Hill Giant club; no feat is required. Organ Rearranger lowers Bonbon''s critical threshold on Titanstring and spell attack rolls. Its low-die damage reroll applies only to melee weapon attacks, not ranged shots; the global critical-range bonus is the reason Bonbon carries it.'
    - id: elixir-of-bloodlust
      item: Elixir of Bloodlust (default)
      slot: consumables
      note: 'DEFAULT for encounters with adds. A kill grants 5 temporary HP and another Action once per turn; in this non-Honour run the extra Action benefits from Extra Attack. The Club costs only 1 Titanstring damage per projectile versus STR 21, which the extra Action easily repays after a kill.'
    - id: elixir-of-hill-giant-strength
      item: Elixir of Hill Giant Strength (boss alternative)
      slot: consumables
      note: 'ALTERNATIVE for a single boss or any fight without a dependable Bloodlust kill. STR 21 raises Titanstring from the Club''s +4 rider to +5. Farming is allowed, so keep a large stock for both this swap and Asterion''s daily Tavern-Brawler requirement.'
    - id: gloves-of-archery
      item: Gloves of Archery (early default)
      slot: hands
      note: 'Buy from Grat at the Goblin Camp. Longbow proficiency is redundant, but +2 damage applies to every ranged weapon hit and is the clean early Titanstring glove.'
    - id: wondrous-gloves
      item: Wondrous Gloves (Flourish alternative)
      slot: hands
      note: 'Grymforge Mimic loot. +1 AC and one extra Bardic Inspiration supply another Slashing Flourish; use them for a nova-focused rest cycle when accuracy is already comfortable.'
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      slot: hands
      note: 'SELECTED late-Act-1 gloves from the Crèche. DEX 18 plus +1 Attack Rolls is a net +2 ranged accuracy over Bonbon''s natural DEX 16, while also improving initiative, AC, DEX saves, and skills. Swap to Wondrous Gloves only when the extra Flourish is worth the accuracy loss.'
    - id: the-protecty-sparkswall
      item: The Protecty Sparkswall
      slot: armour
      note: 'SELECTED late-Act-1 chest from Grymforge. +1 Spell Save DC directly improves Hold Person, Hypnotic Pattern, Fear, Slow, and Glyph of Warding; while Bonbon has Lightning Charges it also grants +1 AC and saving throws. The low clothing AC is the deliberate price of prioritising control DC while staying at range.'
    - id: adamantine-scale-mail
      item: Adamantine Splint Armour (defensive alternative)
      slot: armour
      note: 'DEFENSIVE ALTERNATIVE. Fighter-first grants proficiency; the Splint provides AC 18, crit immunity, 2 damage reduction, and Reeling. Equip it when survival or concentration protection matters more than Protecty Sparkswall''s +1 spell DC. The compatibility ID retains its old “scale-mail” name so existing checklist keys are not orphaned.'
    - id: caustic-band
      item: Caustic Band
      slot: rings
      note: 'SELECTED damage ring from Derryth in the Underdark. +2 Acid applies to every weapon hit, so Bonbon''s multiple Slashing-Flourish projectiles exploit it better than Charles''s smaller Act 1 attack count.'
    - id: diadem-of-arcane-synergy
      item: Diadem of Arcane Synergy
      slot: head
      note: 'SELECTED late-Act-1 head from Ardent Jhe''rezath in the Crèche. After Bonbon inflicts a condition with Hold Person, Fear, Dissonant Whispers, or another spell, Arcane Synergy adds CHA to each subsequent ranged weapon attack for 2 turns. Multiple Titanstring and Slashing-Flourish hits exploit the flat rider better than the rest of the party. Replace it with the Helmet of Arcane Acuity in Act 2.'
    - id: broodmother-s-revenge
      item: Broodmother's Revenge
      slot: amulets
      note: 'SELECTED damage neck after saving the Grove: non-lethally knock out the isolated friendly Kagha and loot it. Any healing, including a potion at full HP, coats Titanstring for +1d6 Poison on every projectile for 2 turns. Skip it against poison-resistant or immune enemies.'
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      slot: head
      note: 'Helmet of Arcane Acuity (Mason''s Guild — +2 acuity/hit → +spell save DC). THE pivot: switch to dual hand crossbows now — more hits per turn stack Acuity far faster than Titanstring''s single big shots.'
    - id: dual-hand-crossbows
      item: Ne'er Misser + Hellfire Hand Crossbow
      wiki:
      - Ne'er Misser
      - Hellfire Hand Crossbow
      slot: weapons
      note: 'Ne''er Misser (Roah at Moonrise) and Hellfire Hand Crossbow (Yurgir) are Light, so no Dual Wielder feat is needed. Main-hand, off-hand, and Slashing Flourish hits rapidly stack Arcane Acuity; Asterion is now an unarmed Monk and no longer needs either crossbow.'
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      slot: rings
      note: 'Band of the Mystic Scoundrel (Akabi''s Circus wheel → Chult jungle) makes Enchantment and Illusion spells bonus actions after a weapon hit. Bonbon can build Arcane Acuity and cast Hold Monster or Command in the same turn.'
    - id: bow-alternative
      item: Hellrider's Longbow (initiative alternative)
      wiki: Hellrider Longbow
      slot: weapons
      note: 'If you ever want a bow again: Hellrider''s Longbow (Rivington) grants +initiative — handy for the controller who wants to act first; Gontr Mael is the top bow but grants NO initiative.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      slot: amulets
      note: 'Amulet of Greater Health sets CON to 23 and grants advantage on CON saves. It stacks with War Caster to protect Bonbon''s Hold Monster concentration, which enables Charles''s automatic melee crits.'
  playstyle: |-
    - **Act 1 default:** equip Titanstring plus the Hill Giant club main hand and Knife of the Undermountain King off-hand, drink Bloodlust, and use Protecty Sparkswall to raise Hold Person/control DC. Use ranged Slashing Flourish for nova damage and trigger Broodmother's Revenge with healing before a multi-projectile turn.
    - **Act 1 alternatives:** use a Hill Giant elixir for a boss with no Bloodlust target; use Adamantine Splint for defence.
    - **Act 2+:** switch to dual hand crossbows and Flourish to stack Arcane Acuity. In Act 3, spend it on a same-turn bonus-action Hold Monster or Command.
    - **Protect concentration:** stay at range. Against undead, use Hypnotic Pattern or Slow instead of Hold Monster/Command.
---
