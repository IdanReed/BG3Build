---
nickname: Bonbon
builds:
- name: The Commander
  is_primary: true
  role: Ranged acuity control + damage + party face
  class: Swords Bard 11 / Fighter 1
  at_a_glance:
    armour: All armour + shields (Fighter first) — the party's only heavy wearer
    elixir: Bloodlust in Act 1 while the Club supplies Strength → Giant Strength (Hill 21, then Cloud 27) from the Stone, for Titanstring
    concentration: Hold Monster, or Hold Person on humanoids Charles is not holding — Fear or Slow only when paralysis is invalid
  build_order: Fighter 1 at character creation → Swords Bard 1–11. No respec at any point.
  race: Half-Elf or Human (early shield)
  background: Guild Artisan (Insight, Persuasion) — proficiencies.md assumes this one
  starting_stats:
    STR: 8
    DEX:
      base: 16
      final: 18
      via: Gloves of Dexterity — sets DEX to 18 (Crèche, Act 1) until Helldusk Gloves replace them in Act 3 and it returns to 16
    CON: 14
    INT: 8
    WIS: 10
    CHA: 17
  stats_note: 'Point-buy 8/15/14/8/10/15 = all 27 (DEX 15 + CHA 15 cost 9 each). +2 → CHA 17, +1 → DEX 16; Gloves of Dexterity then set DEX to 18 (Crèche, Act 1). INT stays at 8 — nothing in the build uses it.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss). Birthright reaches CHA 22 in Act 3 if Gale is not using it.'
  ability_scores:
  - ability: STR
    steps:
    - score: 8
      source: 'point-buy'
    - score: 19
      source: 'SET by Club of Hill Giant Strength (Act 1 until the Stone)'
    - score: 21
      source: 'Elixir of Hill Giant Strength every long rest from the Stone, once Phalar Aluve displaces the Club'
    - score: 27
      source: 'Elixir of Cloud Giant Strength, from level-9 vendors'
  - ability: DEX
    steps:
    - score: 15
      source: 'point-buy'
    - score: 16
      source: '+1 Racial'
    - score: 18
      source: 'SET by Gloves of Dexterity, Act 1'
    - score: 16
      source: 'Act 3: Helldusk Gloves replace the Gloves of Dexterity, so DEX drops back to its natural 16'
  - ability: CON
    steps:
    - score: 14
      source: 'point-buy'
  - ability: INT
    steps:
    - score: 8
      source: 'point-buy'
  - ability: WIS
    steps:
    - score: 10
      source: 'point-buy'
  - ability: CHA
    steps:
    - score: 15
      source: 'point-buy'
    - score: 17
      source: '+2 Racial'
    - score: 18
      source: '+1 Hag''s Hair'
    - score: 20
      source: '+2 Mirror of Loss, Act 3'
  feats:
  - at: Bard 4 (char 5)
    feat: Sharpshooter
  - at: Bard 8 (char 9)
    feat: War Caster
    note: Advantage on CON saves to hold Hold Monster — the party's melee auto-crit engine — plus opportunity-spell casting. Taken over Dual Wielder, which would only matter for pairing Phalar Aluve with a second weapon; a shield does that job with no feat.
  fighting_styles:
  - Archery (Fighter)
  - Dueling (Bard)
  key_spells:
  - Glyph of Warding
  - Hold Monster
  - Confusion
  - Fear
  - Magical Secrets → Command + Conjure Elemental
  creation:
    level1_class: Fighter 1 (taken at character creation)
    level1_gains: 'Archery fighting style (+2 ranged), Second Wind, and — because Fighter is taken FIRST — STR + CON saves, all armour (incl. Heavy) + shields + martial weapons, and 2 Fighter skills.'
    subclass_choice: College of Swords (Bard 3)
    proficiencies:
      armor_weapons: All armour, shields, martial weapons and Archery (Fighter 1); Medium + Scimitars (College of Swords).
      saving_throws: STR + CON (Fighter-first) — CON guards Hold Monster concentration.
      skills: Fighter 2 + Bard skills; Expertise ×4 (Bard 3 + 10) + Jack of All Trades — the party face.
    starting_cantrips: '2 at Bard 1 (Vicious Mockery, Friends) → 4 by Bard 10.'
    starting_spells: '4 known at Bard 1, +1 every Bard level → 14 by Bard 11, plus the 2 Magical Secrets at Bard 10 that sit on top of the class table (16 in all). She has no Shield reaction — lean on range, positioning and the Fighter dip''s armour proficiency instead.'
    notes: 'Half-Elf/Human. Fighter 1 at creation → Swords Bard ×11, no respec. Bard 11 = caster level 11 → one L6 slot, so Command hits up to 6 targets on Bard levels alone; the only things a Wizard dip would have added are the Shield reaction and scroll scribing. Feats/ASIs at Bard 4 (char 5) and Bard 8 (char 9). ⚠ WHY NOT FIGHTER 2 (Action Surge)? The multiclass guides list Fighter 2 as a near-universal package and their own party build runs a Swords Bard 6 / Fighter 2 core. Action Surge would give a second Attack action to saturate Arcane Acuity and fire control a full turn earlier — but it costs Bard 11, and with it the LEVEL 6 SLOT that upcasts Command to six targets and unlocks Otto''s Irresistible Dance. Since the six-target Command is this build''s stated payoff and the Acuity engine is gear-gated to Act 2–3 anyway, Fighter 1 wins here. Revisit only if the control loop feels a turn too slow in play.'
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
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (30:07) — paralysis is devastating but costs a level 5 slot and caps at two targets'
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Paralyse — attacks within 3m auto-crit, the melee auto-crit engine for Charles's smites. Upcast adds +1 target per slot above 5th. Concentration.
    - spell: Command
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (28:37) — concentration-free turn denial that upcasts to multiple enemies; every higher-level slot competes with it'
      level: '1'
      guide_level: 11
      school: Enchantment
      save: WIS save
      when: Bard 10 (Magical Secrets)
      why: The bonus-action loop via the Band of the Mystic Scoundrel. +1 target per slot above 1st, so the Bard-11 L6 slot hits up to 6. DC uses CHA + Arcane Acuity.
    - spell: Glyph of Warding
      tier: S
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (45:04) — cast it directly on an enemy like a Fireball; non-concentration, six damage types, plus an AoE Dex-save sleep'
      level: '3'
      guide_level: 6
      school: Abjuration
      save: DEX save
      when: Bard 5
      why: Pre-placed AoE burst (5d8, choose element) set as a ground trap before a fight.
    recommended:
    - spell: Fear
      tier: A
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (35:36) — strongest of the three encounter-ending control spells, but a 30ft cone, so hardest to land'
      level: '3'
      guide_level: 9
      school: Illusion
      save: WIS save
      when: Bard 5
      why: 9m cone — frightened enemies drop weapons and cannot act or approach; scales with CHA + Arcane Acuity. Concentration.
    - spell: Confusion
      tier: B
      tier_note: 'Spells tier list, level 4, part 1 (Banishment through Fire Shield) (13:24) — hits enemies only, not allies; unreliable, but shut a door and the encounter kills itself'
      level: '4'
      guide_level: 8
      school: Enchantment
      save: WIS save
      when: Bard 7
      why: 6m scramble — enemies attack randomly or skip turns. Concentration.
    - spell: Hypnotic Pattern
      tier: A
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (10:24) — best when it catches the whole encounter; A only because it shares a role with Fear and Sleet Storm, and he would accept S'
      level: '3'
      guide_level: 6
      school: Illusion
      save: WIS save
      when: Bard 5
      why: 'Strong 9m AoE incapacitate and a superb Acuity payoff. ⚠ The tier lists rate it only A, not S — the duration is short and ANY damage wakes the targets, so it does not survive a party that is already firing into the pack. Treat it as a way to buy one clean turn, not as a lockdown. Concentration.'
    - spell: Conjure Elemental
      tier: S
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (15:03) — an all-day summon as strong as an extra party member; all eight modes viable'
      level: '5'
      guide_level: 11
      school: Conjuration
      save: None
      when: Bard 10 (Magical Secrets)
      why: 'The second Magical Secret. S tier — "a day-long, concentration-free elemental or myrmidon is comparable to adding another character to the party." The concentration-free part is what makes it fit HER specifically: she can field it and still hold Hold Monster, which no other summon of this weight allows. The Water Myrmidon also mass-applies Wet, the party''s only reliable way to strip fire resistance ahead of Gale.'
    - spell: Globe of Invulnerability
      tier: S
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (26:18) — total damage immunity wins most boss fights outright; get one cast into every Honour party'
      level: '6'
      guide_level: 11
      school: Abjuration
      save: None (Concentration)
      when: Scroll only — NOT selectable as a Magical Secret
      why: 'Rated the #9 spell in the game and worth carrying, but she cannot learn it: Magical Secrets at Bard 10 selects from spells up to LEVEL 5 only, and Globe is 6th-level. With no Wizard dip there is no scribing route either, so buy scrolls and cast them for the Act 3 caster gauntlets and the Netherbrain''s area attacks. ⚠ Concentration, so a scroll cast still costs her Hold Monster that turn. Counterspell stays off her list because Gale and Charles already cover that lane, and three carriers is one more than the guides advise.'
    - spell: Hold Person
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (55:42) — paralysis costs turns and gives automatic crits within 10 ft; humanoids only, best with high save DC'
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Bard 3
      why: Cheaper single-target paralyse (auto-crit within 3m), far earlier than Hold Monster — the early-game stand-in. Concentration.
    - spell: Dominate Person
      tier: D
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (25:19) — one unreliable temporary ally for a level 5 slot; AoE control is better'
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Turn a humanoid against its allies — a flex 5th-level pick alongside Hold Monster. Concentration.
    - spell: Vicious Mockery
      tier: C
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (1:04:16) — too little damage to beat firing a bow; a late-game bard filler action only'
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Psychic damage plus disadvantage on the target's next attack — free ranged control that feeds acuity.
    - spell: Friends
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (26:48) — advantage on Charisma checks; COUNTS AS A CRIME ON TACTICIAN AND HONOUR MODE, so hide or fast-travel afterwards'
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: None (Concentration)
      when: Bard 1
      why: Advantage on Charisma checks against a non-hostile creature — the face enabler. Never cast it on companions (approval loss when it ends).
    - spell: Slow
      tier: B
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (33:15) — targets six creatures so it spares allies, and bypasses incapacitation immunity; the reliable second-choice control spell'
      level: '3'
      guide_level: 7
      school: Transmutation
      save: WIS save
      when: Bard 5
      why: UNDEAD-PROOF control, unlike Hold Monster/Command — half speed, −2 AC and DEX saves, one action only, ~50% chance to fizzle a cast. Bank it for the Act-2 undead and construct fights where paralysis fails. Concentration.
    - spell: Healing Word
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (10:48) — ranged bonus-action revive, and the delivery system for Whispering Promise and Hellrider''s Pride buffs'
      level: '1'
      guide_level: 2
      school: Evocation
      save: None
      when: Bard 1
      why: The no-healer party's emergency pickup — a bonus-action ranged revive so a downed ally does not cost a full turn. Cheap to keep known; pairs with stocked Revivify scrolls.
    - spell: Longstrider
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (27:03) — free all-day +10 movement on everyone including summons; he would put it in S+ if that existed'
      level: '1'
      guide_level: 2
      school: Transmutation
      save: None (ritual)
      when: Bard 1
      why: Free out-of-combat party movement buff lasting until long rest, with no Concentration.
    - spell: Enhance Ability
      tier: B
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (36:31) — cast a couple of times a run; worth preparing for the few unavoidable skill checks'
      level: '2'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Bard 4
      why: 'Advantage on checks with one chosen ability. At char 5, replace the redundant Faerie Fire with it for dialogue, theft and exploration — an out-of-combat mode, never held alongside Hold Person. ⚠ Rated only B: "significant checks are less frequent than players expect," and Bonbon already has Expertise ×4 plus Jack of All Trades. Low stakes either way.'
    - spell: Greater Invisibility
      tier: A
      tier_note: 'Spells tier list, level 4, part 2 (Freedom of Movement through Wall of Fire) (13:18) — A for ordinary parties: free attacks then a surprise round; broken if built around stealth checks'
      level: '4'
      guide_level: 8
      school: Illusion
      save: None (Concentration)
      when: Bard 7+ — optional pick
      why: 'A-tier, and the tier lists note it "anchors an entire party strategy" — the target stays invisible while attacking, giving permanent advantage and imposing disadvantage on attacks against it. Concentration, so it directly competes with Hold Monster: take it as the survivability alternative for fights where nothing worth Holding exists, or on a run where you want the stealth loop.'
    - spell: Silence
      tier: A
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (43:29) — free as a ritual, shuts down enemy casters and noisy legendary actions; needs something holding them inside'
      level: '2'
      guide_level: 5
      school: Illusion
      save: None (Concentration)
      when: Bard 3+ — optional pick
      why: 'A-tier. A zone that hard-disables enemy spellcasting with no save at all — the answer to the Act 3 caster packs that Counterspell can only handle one at a time, and the reason leaving Counterspell off her list costs less than it looks. Concentration.'
    - spell: Dissonant Whispers
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (42:35) — concentration-free damage plus two turns of Frightened on a WIS save; effectively stuns melee enemies'
      level: '1'
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Early psychic damage plus Frightened — useful single-target control before the Acuity engine.
    - spell: Faerie Fire
      tier: C
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (57:53) — huge radius, but other spells grant advantage and do more; outclassed at its own job'
      level: '1'
      guide_level: 2
      school: Evocation
      save: DEX save
      when: Bard 1
      why: Early area advantage and anti-invisibility. Concentration, so replace it once stronger control arrives.
    - spell: Tasha's Hideous Laughter
      tier: A
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (52:09) — weak early because damage grants extra saves; late, a 10-turn disable that bypasses boss incapacitation immunities'
      level: '1'
      guide_level: 3
      school: Enchantment
      save: WIS save
      when: Bard 2
      why: Cheap early single-target incapacitation — a bridge to Hold Person that can be replaced later.
    - spell: Invisibility
      tier: A
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (58:48) — wins no fights alone but invaluable for scouting and as a panic button; potions compete'
      level: '2'
      guide_level: 5
      wiki: Invisibility (spell)
      school: Illusion
      save: None
      when: Bard 4
      why: Scouting, theft setup and an emergency escape — strong out-of-combat utility.
    - spell: Otto's Irresistible Dance
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (41:05) — no-save lockdown that bypasses legendary resistance; only for fights with one main enemy'
      level: '6'
      guide_level: 12
      school: Enchantment
      save: WIS save after the effect begins
      when: Bard 11
      why: Immediate single-target shutdown when the level 6 slot is not reserved for an upcast Command.
    - spell: Mage Hand
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (33:23) — costs a short-rest charge, but scouts, triggers traps, throws potions and soaks one enemy attack'
      level: Cantrip
      guide_level: 5
      school: Conjuration
      save: None
      when: Bard 4
      why: 'Exploration and object manipulation with no attack roll, save or Concentration. For a no-slot Wet setup, drop a water bottle in reach and use the Hand''s Throw for a 2m splash.'
    - spell: Light
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (30:38) — hands-free, concentration-free light lasting all day; most parties need some light source'
      level: Cantrip
      guide_level: 11
      school: Evocation
      save: None
      when: Bard 10
      why: Long-lasting illumination for dark areas, with no slot or Concentration.
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
      note: +2 to ranged attack rolls offsets Sharpshooter and stays essential after the hand-crossbow pivot.
    - category: Skills
      picks: 2
      recommendation:
      - Intimidation
      - Perception
      note: 'TWO picks, easy to miss behind the Fighting Style — and only because Fighter is the FIRST class here; a Fighter dip taken later grants no skills at all. Intimidation is load-bearing, not flavour: char 11 spends Expertise on it, Expertise requires existing proficiency, and Intimidation appears on neither the Guild Artisan background nor the Swords package — the Fighter list is its only source. Perception is the most-rolled skill in the game. Do NOT take Athletics on a STR 8 character; Jack of All Trades already covers it at half proficiency.'
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
      - Vicious Mockery
      - Friends
      note: Mockery is the ranged fallback; Friends supports the face role but must never be cast on companions.
    - category: Spells
      picks: 4
      recommendation:
      - Healing Word
      - Longstrider
      - Dissonant Whispers
      - Faerie Fire
      note: Emergency pickup, ritual party movement, early single-target control, and an early advantage tool.
    - category: Skill
      picks: 1
      recommendation: Deception
      note: 'ONE pick, not three — multiclassing into Bard grants a single skill, where a first-class Bard would grant three. It must be Deception: char 4 spends Expertise on it, and Deception appears on neither the Guild Artisan background nor the Fighter list, so this is its only source. Taking it here also makes the build legal on the Half-Elf option, which grants no free skill in BG3 — on Human you could instead put Deception on the racial free skill and spend this pick on Performance.'
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
      picks: 1
      recommendation: College of Swords
      note: Ranged Slashing Flourish supplies the multi-hit engine.
    - category: Fighting style
      picks: 1
      recommendation: Dueling
      note: A formality — neither Swords style touches a bow. Duelling wants a lone melee weapon and Two-Weapon Fighting an off-hand attack, and she makes neither. Pick Duelling and move on.
    - category: Expertise
      picks: 2
      recommendation:
      - Persuasion
      - Deception
      note: Establishes Bonbon as the party face.
    - category: Spell
      picks: 1
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
      picks: 1
      recommendation: Sharpshooter
      note: The +10 damage mode is the Act 1 ranged spike; Archery and advantage offset the attack penalty.
    - category: Cantrip
      picks: 1
      recommendation: Mage Hand
      note: 'Exploration utility with no concentration cost. For a no-slot Wet setup, drop a water bottle for the Hand and use its Throw on the Hand''s turn.'
    - category: Spell
      picks: 1
      recommendation: Invisibility
      note: 'ONE new spell known at Bard 4 (7 total), not two — the second name below comes out of the free replacement, not a second pick. Both spells concentrate, so they are exploration tools once Hold Person is online.'
    - category: Replacement
      picks: 1
      optional: true
      recommendation: Faerie Fire → Enhance Ability
      note: 'The optional swap every Bard level from 2 onward offers. Faerie Fire has done its job by now, and Enhance Ability is the better out-of-combat concentration spell.'
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
      note: 'ONE new spell known at Bard 5 (8 total). Glyph of Warding is the priority burst pick; take it with the pick and bring Hypnotic Pattern in on the swap below.'
    - category: Replacement
      picks: 1
      optional: true
      recommendation: An early flex spell → Hypnotic Pattern
      note: 'Hypnotic Pattern is the level-3 control card and it does not need a second pick — trade one of the char-2 level-1 spells for it. Longstrider is the safest to drop; it is a ritual you can re-cast off a scroll.'
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
      note: The undead- and construct-safe control choice when paralysis is invalid.
  - char_level: 8
    class: Swords Bard 7
    gains:
    - Level 4 Bard spells
    - One additional spell known
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Confusion
      note: Wide-area control that scales extremely well with Arcane Acuity.
    - category: Replacement
      picks: 1
      optional: true
      recommendation: Healing Word or Dissonant Whispers → Greater Invisibility
      note: 'The free replacement slot every Bard level from 2 onward offers, unused until now. Greater Invisibility is endorsed elsewhere in this build but never actually learned in any row — A tier, "enables repeated attacks or casts while hidden" and "can anchor an entire party strategy." By char 8 the level-1 picks from char 2 are dead weight, so this costs nothing.'
  - char_level: 9
    class: Swords Bard 8
    gains:
    - One additional spell known
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: War Caster
      note: Advantage on concentration saves protects the later Hold Monster engine.
    - category: Spell
      picks: 1
      recommendation: Hold Person
      note: 'MORE HOLD, NOT MORE FEAR. A held humanoid takes automatic critical hits from melee within 3m, which is exactly what Charles converts into a doubled-smite nova, so a second Hold is worth more to this party than a cone of Frightened. Upcast Hold Person hits an extra target per slot level, and her Arcane Acuity DC makes it stick. Keep Fear only as a scroll or a swap for a crowd of non-humanoids that Hold Person cannot touch.'
  - char_level: 10
    class: Swords Bard 9
    gains:
    - Level 5 Bard spells
    - One additional spell known
    recommendations:
    - category: Spell
      picks: 1
      recommendation: Hold Monster
      note: 'ONE new spell known at Bard 9 (12 total) and the level-5 list opens. Hold Monster is the pick — it extends the auto-crit setup to everything Hold Person cannot touch.'
    - category: Replacement
      picks: 1
      optional: true
      recommendation: A lower-level flex spell → Dominate Person
      note: 'Only if both are wanted immediately. Dominate Person costs no extra pick if it replaces a dead level-1 or level-2 spell; otherwise leave it and take it with the char-12 pick instead.'
  - char_level: 11
    class: Swords Bard 10
    gains:
    - Magical Secrets selections ×2
    - Expertise selections ×2
    - Improved Bardic Inspiration d10
    - Fourth Bard cantrip
    - One additional Bard spell known (13th)
    recommendations:
    - category: Magical Secrets
      picks: 2
      recommendation:
      - Command
      - Conjure Elemental
      note: '⚠ MAGICAL SECRETS STOP AT LEVEL 5, so Globe of Invulnerability is NOT selectable here. bg3.wiki: "At level 10, all Bards can learn two spells up to level 5," and the list is Banishing Smite, Cone of Cold, Conjure Elemental, Contagion, Wall of Stone. Globe and Heroes'' Feast are both 6th-level and neither is on it, and with no Wizard dip there is no scroll-scribing route either — buy Globe scrolls and cast them, that is all. Command takes the first pick: the Band of the Mystic Scoundrel makes hers a BONUS ACTION at the party''s highest Acuity DC and the level 6 slot upcasts it to six targets, neither of which Gale can replicate. Conjure Elemental takes the second — S tier, "a day-long, concentration-free elemental or myrmidon is comparable to adding another character to the party," and because it needs no Concentration she stays free to hold Hold Monster. The Water Myrmidon also mass-applies Wet, which is the party''s only reliable way to strip enemy fire resistance for Gale. Counterspell is the runner-up if you would rather have the interrupt.'
    - category: Expertise
      picks: 2
      recommendation:
      - Insight
      - Intimidation
      note: Completes face and dialogue coverage; swap one for a campaign-specific skill if preferred.
    - category: Spell
      picks: 1
      recommendation: Silence
      note: 'The FOURTH pick on this level and the easiest of all to miss: Bard 10 grants a normal 13th Bard spell known ON TOP of the two Magical Secrets, which the level-up UI presents as a separate step. Silence is A tier for "caster lockdown" and "since dangerous casters appear throughout the game, Silence has frequent opportunities." It is also load-bearing here — the Magical Secrets note above justifies dropping Counterspell partly by pointing at Silence, yet no row ever learned it.'
    - category: Cantrip
      picks: 1
      recommendation: Minor Illusion
      note: 'S tier — "moves creatures toward a point without a saving throw," which groups enemies for Gale''s Fireball and relocates NPCs for Asterion''s theft routes. Both published Swords Bard guides name it for the face specifically: "Minor Illusion can distract/relocate entire rooms of NPCs to open up some unique thievery options." Light is the A-tier alternative if the party needs another illumination carrier, but Gale already learns Light at char 4 and Daylight at char 8.'
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
      note: Best-in-class single-target shutdown when the level 6 slot is not reserved for mass Command.
  itemization:
    act1:
    - id: titanstring-bow
      item: Titanstring Bow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (32:39) — adds your strength modifier; best in slot Act 1 damage with a giant strength elixir'
      slot: weapons
      bis: true
      note: Brem, after Find the Missing Shipment. Archery + Sharpshooter + ranged Slashing Flourish apply its STR rider to large, accurate nova shots, and it is HER BOW FOR THE WHOLE RUN. Act 1 default is the STR 19 Club + Knife + Bloodlust package; Hill Giant elixir for a boss where Bloodlust cannot trigger. From the Stone the Club leaves her hands and the elixir supplies the Strength every day.
    - id: club-of-hill-giant-strength
      item: Club of Hill Giant Strength
      tier: A
      tier_note: 'nmFK4uJQfC8 (17:42) — sets strength to 19, freeing the elixir slot for monks and Titanstring archers'
      slot: weapons
      note: Titanstring stat stick, from the Arcane Tower. Light club main hand, Knife off-hand, Titanstring in the ranged slot — STR 19 adds +4 damage per projectile and keeps the elixir slot free for Bloodlust.
    - id: knife-of-the-undermountain-king-offhand
      item: Knife of the Undermountain King
      tier: S
      tier_note: 'jeSeVkmqmuc (21:07) — +2 shortsword; wider crit range, damage-dice rerolls, advantage in darkness; stat stick for anyone'
      slot: weapons
      note: 'ACT 1 ONLY. Crèche stat stick beside the Light club, no feat needed. Organ Rearranger lowers the crit threshold globally, but this party''s crits come from Hold, not from threshold, so on a volume-and-control build it is a harmless filler rather than a reason. The Sentinel Shield replaces it at Moonrise, and from the Stone it becomes CHARLES''S bagged Psychic-immune fallback blade.'
    - id: elixir-of-bloodlust
      item: Elixir of Bloodlust
      tier: S
      tier_note: '9BcQXb37Bik (22:44) — extra action per kill; on Honour that action gets no Extra Attack, on Tactician or below it does'
      slot: consumables
      note: ACT 1 DEFAULT with adds, until the Stone. A kill grants 5 temp HP and another Action once per turn, and outside Honour that Action benefits from Extra Attack. The Club costs only 1 Titanstring damage per projectile versus STR 21 — repaid by one extra Action. Once Phalar Aluve displaces the Club, a daily Giant Strength elixir takes this slot for good.
    - id: elixir-of-hill-giant-strength
      item: Elixir of Hill Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (30:26) — sets Strength to 21; S used normally, and S+ ABOVE THE SCALE if drunk daily to skip strength investment'
      slot: consumables
      note: Act 1 — for a lone boss or any fight with no dependable Bloodlust kill; STR 21 raises the Titanstring rider from +4 to +5. FROM THE STONE it is her STANDING elixir, because the Club leaves her melee set and Titanstring's rider needs a Strength score. Keep a big stock — Asterion drinks one daily too.
    - id: gloves-of-archery
      item: Gloves of Archery
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (15:11) — best in slot for any ranged attacker; flat +2 damage plus bow proficiency'
      slot: hands
      note: Grat at the Goblin Camp. Longbow proficiency is redundant, but +2 damage applies to every ranged weapon hit — the clean early Titanstring glove, worn until the Crèche.
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (25:38) — called the best item in the game for what it enables'
      rank: '#1'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #1 of 20 — sets Dexterity to 18 and adds +1 attacks, freeing ability points and feats'
      slot: hands
      bis: true
      note: 'LATE-ACT-1 DEFAULT, from the Crèche, and rated the #1 item of the 20 best in Act 1 — "the most impactful equipable item in Act 1, and in the narrator''s view the entire game." DEX 18 plus +1 Attack Rolls is a net +2 ranged accuracy over natural DEX 16, plus initiative, AC, DEX saves and skills. ⚠ The video pitches these at a Sorcerer who respecs DEX to 8 and reclaims the points; that does not work here, because the gloves are a Crèche pickup and the character would spend all of early Act 1 at DEX 8. On Bonbon the +1 Attack Rolls also applies to every projectile of a Slashing Flourish and every hand-crossbow bolt — four or more attack rolls a turn.'
    - id: wondrous-gloves
      item: Wondrous Gloves
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (49:02) — best in slot for many bards and good enough on other characters too'
      slot: hands
      note: Grymforge Mimic loot. +1 AC and one extra Bardic Inspiration supply another Slashing Flourish — take them for a nova-focused rest cycle when accuracy is already comfortable.
    - id: the-protecty-sparkswall
      item: The Protecty Sparkswall
      tier: S
      tier_note: 'TwFGCc8OOfw (16:41) — earliest chest slot +1 spell save DC; best in slot for casters through acts 1-2'
      rank: '#8'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #8 of 20 — +1 spell save DC on clothing makes it the caster default well into Act 2'
      slot: armour
      note: 'ACT 1 CHEST, from the gilded chest at the end of the trapped Grymforge bridge, and rated #8 of 20 as "the caster default through much of Act 2." +1 Spell Save DC improves Hold Person, Hypnotic Pattern, Fear, Slow and Glyph. ⚠ Its second effect, +1 AC and saves while carrying Lightning Charges, is dead here — she has no charge generator, since The Spellsparkler is Gale''s. Take it purely for the flat +1 DC, and understand the low clothing AC is the price of control DC at range until the Adamantine Forge.'
    - id: adamantine-scale-mail
      item: Adamantine Splint Armour
      tier: S
      tier_note: 'VjmWkRCoDWE (19:03) — 18 AC, crit immunity, 2 damage reduction and 3 turns of reeling; STORY EVENT LATE IN ACT 1'
      rank: '#15'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #15 of 20 — stronger damage reduction than the scale mail, and fewer serious alternatives'
      slot: armour
      bis: true
      note: 'THE FIRST MITHRAL ORE, and the chest she finishes Act 1 in. Fighter-first grants Heavy proficiency and she is the party''s ONLY legal wearer. AC 18 flat, ATTACKERS CANNOT LAND CRITICAL HITS, all incoming damage reduced by 2, and melee attackers sent Reeling. Crit immunity is what protects Hold Monster: a concentration save is DC = half the damage taken or 10, whichever is higher, so a critical hit roughly doubles that DC. Swap off Protecty once she has it and accept losing +1 spell DC for 6 AC and crit immunity. (The ID keeps an older name so existing checkoffs survive.)'
    - id: act1-ring2-bonbon
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'OPEN, and it changes hands mid-act. The Whispering Promise is the only Bless the party can get before the Underdark, so it starts here and comes off the moment Asterion picks up the Staff of Arcane Blessing — after that its Bless is the same non-stacking condition and it is pure waste.'
      options:
      - id: opt-whispering-promise
        item: The Whispering Promise
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (49:20) — a mainstay through Acts 1 and 2; very few parties would not benefit strongly'
        rank: '#10'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #10 of 20 — healing grants two turns of Bless, with no concentration or dedicated action'
        note: 'Volo, or Grat at the Goblin Camp, ~40g. Healing a creature gives it +1d4 to attacks and saves for 2 turns with NO Concentration, and her Healing Word is a bonus action so it costs her nothing. Take it off once Asterion is casting real Bless.'
      - id: opt-crushers-ring
        item: Crusher's Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (9:50) — movement speed is universally applicable; an extremely rare party leaves it on the table'
        note: 'Crusher at the Goblin Camp. +3m movement, stacks with Longstrider. Not build-defining for anyone, but good on ANY character who needs to close distance without spending a bonus action.'
      - id: opt-ring-of-protection
        item: Ring of Protection
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (34:55) — raises the party''s average AC; give it to the easiest-to-hit member'
        rank: '#20'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #20 of 20 — +1 AC and all saves fits almost anyone, for the whole game'
        note: "Mol's reward for Steal the Sacred Idol. +1 AC and +1 to ALL saving throws — the generically best defensive ring in Act 1, and the item guides say to put it on the lowest-AC body."
      - id: opt-bracing-band
        item: Bracing Band
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (6:13) — good for a lot of characters, though there are often better options'
        note: "Sergeant Thrinn at Grymforge, for Find the Missing Boots. A free permanent +1 AC after shoving — almost nobody takes it, and it is fine on anyone."
    - id: caustic-band
      item: Caustic Band
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (7:16) — for almost every party; goes on whoever makes the most attacks in a round'
      rank: '#12'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #12 of 20 — a passive 2 acid on every weapon attack, which adds up on multiattackers'
      slot: ring 1
      note: 'Derryth, Underdark, rated #12 of 20 and explicitly for characters making several attacks per turn. +2 Acid per weapon hit, applied to every Slashing-Flourish projectile. ⚠ Per the wiki it covers melee, ranged and Thrown attacks but NOT Unarmed Strike, which is why it can never move to Asterion despite his higher hit count. She wears it alongside the Whispering Promise — she has two ring slots and the two do not conflict.'
    - id: act1-head-bonbon
      item: Head slot
      slot: head
      wiki: false
      note: 'A REAL COIN-FLIP FOR ACT 1, which is why it is not a single pick: one of these is damage and the other is what keeps Hold Monster from breaking. Both get replaced by the Helmet of Arcane Acuity in Act 2 regardless.'
      options:
      - id: diadem-of-arcane-synergy
        item: Diadem of Arcane Synergy
        tier: S
        tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (21:57) — a huge damage boost even for characters outside the builds designed around it'
        note: 'Ardent Jhe''rezath, Crèche. Once she lands a condition — Hold Person, Fear, Dissonant Whispers — Arcane Synergy adds her Charisma to every subsequent ranged weapon hit. The damage pick.'
      - id: grymskull-helm
        item: Grymskull Helm
        tier: S
        tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (25:05) — features in most parties and makes a playthrough much safer'
        note: 'Free from Grym at the Adamantine Forge. Attackers cannot land critical hits, plus Fire resistance. She is the party''s ONLY character with Heavy Armour proficiency, so she is the only one who can legally wear it — and crit immunity blunts the worst concentration-save spikes on her Hold Monster. The safety pick.'
    - id: broodmother-s-revenge
      item: Broodmother's Revenge
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (21:11) — free to trigger, which is what pushes it to the top'
      rank: '#17'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #17 of 20 — the largest early per-hit damage die, but it needs a healing trigger'
      slot: amulets
      note: 'After saving the Grove — talk Kagha down, then knock the isolated friendly Kagha out non-lethally and loot it. Rated #17 of 20. Any healing, even a potion at full HP, coats Titanstring for +1d6 Poison per projectile for 2 turns, and her bonus-action Healing Word is what triggers it. Skip against poison-resistant or immune enemies.'
    - id: boots-of-speed
      item: Boots of Speed
      tier: A
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (11:29) — bonus-action double move; some party member almost always wants it (captions garble the letter)'
      rank: '#14'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #14 of 20 — bonus-action Dash gives anyone Rogue-grade mobility'
      slot: feet
      note: 'HERS, and rated #14 of 20. Bonus-action Dash for a character with no innate mobility, which is exactly what the video means by giving it to "the character most likely to waste a turn out of position." ⚠ It is NOT Asterion''s: Step of the Wind already gives him bonus-action Dash and Disengage from Monk 2, so the boots would buy him nothing while displacing the Night Walkers. ⚠ The video flags the opportunity-attack rider as bugged — take these for the Dash, not the defensive text.'
    - id: act1-cloak-bonbon
      item: No cloak exists yet
      slot: cloaks
      note: Deliberately empty. The Deathstalker Mantle is the only magical cloak obtainable in Act 1 and it is a Dark Urge reward that goes to Asterion; every other cloak in the game first appears in Act 2 or later. Her slot opens at Last Light.
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (35:18) — broken like all the Arcane Acuity items, and one of the easiest to use'
      slot: head
      bis: true
      note: 'Mason''s Guild in Reithwin Town — an Act 2 pickup, not an Act 3 one. Every weapon hit grants 2 turns of Arcane Acuity; each remaining turn is +1 spell attack AND +1 spell save DC, capped at 10 turns. TITANSTRING STAYS: a ranged Slashing Flourish fires two projectiles and each one that damages is a separate trigger, so Extra Attack''s two Flourishes are four hits and +8 in one Action, and any Hasted turn caps her at +10. ⚠ Dual hand crossbows were the old plan; their only edge is a fifth hit from the bonus-action off-hand shot, and her bonus action belongs to Healing Word now and the Band of the Mystic Scoundrel later. ⚠ Damage taken strips 2 turns of Acuity, which is why her defensive gear matters more than it looks.'
    - id: act2-ranged-bonbon
      item: Titanstring Bow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (32:39) — adds your strength modifier; best in slot Act 1 damage with a giant strength elixir'
      held: 1
      slot: ranged weapons
      bis: true
      note: 'CARRIED OVER for the whole run. Its Strength rider lands on every projectile, Flourish projectiles and special-arrow riders included, and with Sharpshooter that is 23–28 a hit against 18.5 from a hand crossbow. Until the Stone the Club supplies STR 19; from the Stone a daily Elixir of Hill Giant Strength (21), then Cloud Giant (27) once level-9 vendors stock it. ⚠ Ne''er Misser and the Hellfire Hand Crossbow are no longer part of the plan: they only pulled ahead through the bonus-action off-hand shot, and her bonus action is spoken for.'
    - id: act2-melee-bonbon
      item: Club of Hill Giant Strength + Sentinel Shield
      wiki:
      - Club of Hill Giant Strength
      - Sentinel Shield
      slot: weapons
      note: 'UNTIL THE STONE. The melee set is never swung, so it is two stat sticks — every "holder gains" passive on an equipped weapon applies while she shoots, and so does a shield''s AC. The Club keeps STR 19 on Titanstring; the SENTINEL SHIELD from Lann Tarv on the main floor of Moonrise adds +2 AC and +3 Initiative. The Knife retires here: crit threshold is not what this party is built on.'
    - id: phalar-aluve-bonbon
      item: Phalar Aluve + Ketheric's Shield
      wiki:
      - Phalar Aluve
      - Ketheric's Shield
      slot: weapons
      bis: true
      note: 'FROM THE STONE, and for the rest of the run. Charles hands over PHALAR ALUVE at his respec, and KETHERIC''S SHIELD drops from Ketheric''s second fight in the Colony: +2 AC, +1 SPELL SAVE DC on top of the Acuity cap, and advantage on DEX saves, all live from her inactive melee set. Phalar is Versatile, not Light, so without Dual Wielder no weapon can share her hands with it — a shield is the only legal partner, which is exactly why the Club and Knife leave. SHE IS THE SHRIEK CARRIER NOW. Shriek is a 6 m aura on the WIELDER that ends if the sword is unequipped and costs an ACTION: spend her Haste action on it on turn 1 (or pre-cast from stealth), then play 3–6 m from the enemies she wants debuffed — outside the 3 m ranged-disadvantage band, inside the aura. −1d4 to their saves and attack rolls, and +1d4 Thunder every time anyone damages them.'
    - id: act2-chest-bonbon
      item: Adamantine Splint Armour
      tier: S
      tier_note: 'VjmWkRCoDWE (19:03) — 18 AC, crit immunity, 2 damage reduction and 3 turns of reeling; STORY EVENT LATE IN ACT 1'
      rank: '#15'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #15 of 20 — stronger damage reduction than the scale mail, and fewer serious alternatives'
      held: true
      slot: armour
      bis: true
      note: AC 18, crit immunity and −2 to every incoming damage instance carry her through Act 2 unchanged, and a shield in the melee set adds 2 more from Moonrise. Crit immunity does double duty here — it protects Hold Monster concentration and it stops Arcane Acuity being stripped two turns at a time by big hits.
    - id: act2-hands-bonbon
      item: Gloves of Dexterity
      tier: S
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (25:38) — called the best item in the game for what it enables'
      rank: '#1'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #1 of 20 — sets Dexterity to 18 and adds +1 attacks, freeing ability points and feats'
      held: true
      slot: hands
      bis: true
      note: DEX 18 and +1 Attack Rolls remain the best glove effect available to her, and every hit is now an Acuity stack rather than just damage. Nothing in Act 2 beats it.
    - id: act2-elixir-bonbon
      item: Elixir of Hill Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (30:26) — sets Strength to 21; S used normally, and S+ ABOVE THE SCALE if drunk daily to skip strength investment'
      slot: consumables
      note: 'STANDING ELIXIR FROM THE STONE — one every long rest, like Asterion. STR 21 puts +5 on every Titanstring projectile unconditionally, where Bloodlust needed her to land the kill. Bloodlust stays the pick only while the Club is still in her hands. Cloud Giant (STR 27, +8) replaces it as soon as a level-9 vendor stocks one — Araj, Talli, Mattis and Roah all can.'
    - id: spellcrux-amulet
      item: Spellcrux Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (33:07) — plainly incredible'
      slot: amulets
      note: 'ACT 2 NECK, worn by the Warden in the Moonrise Towers Prison. Replenish an expended spell slot of ANY level as a BONUS ACTION, once per long rest. On a Bard 11 with a single level-6 slot that is literally a second six-target Command or a second Hold Monster, recovered mid-fight without spending her action. It replaces Broodmother''s Revenge, whose poison coating needs a per-turn heal she no longer has time for once the Acuity loop starts.'
    - id: act2-rings-bonbon
      item: Caustic Band
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (7:16) — for almost every party; goes on whoever makes the most attacks in a round'
      rank: '#12'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #12 of 20 — a passive 2 acid on every weapon attack, which adds up on multiattackers'
      slot: ring 1
      bis: true
      note: 'Caustic Band keeps adding +2 Acid to every bolt and never comes off. Per the wiki it covers melee, ranged and Thrown attacks but NOT Unarmed Strike, which is why it can never move to Asterion despite his higher hit count.'
    - id: act2-ring2-bonbon
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'GENUINELY OPEN until Act 3. The Whispering Promise came off the moment Asterion started casting real Bless off the Staff of Arcane Blessing, because both apply the same condition and do not stack. Nothing in the Act 2 pool is clearly best-in-slot for her, so pick per stretch. WARNING the Risky Ring is NOT a candidate: disadvantage on saving throws lands directly on the Constitution saves protecting Hold Monster.'
      options:
      - id: opt-whispering-promise-hold
        item: The Whispering Promise
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (49:20) — a mainstay through Acts 1 and 2; very few parties would not benefit strongly'
        rank: '#10'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #10 of 20 — healing grants two turns of Bless, with no concentration or dedicated action'
        note: 'Keep it on ONLY until Asterion reaches the Arcane Tower basement. After that it is pure waste, because its Bless is the same non-stacking condition and it never gets Mystra''s Blessing.'
      - id: opt-ring-of-mental-inhibition
        item: Ring of Mental Inhibition
        tier: B
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (24:59) — powerful if the party is carefully built around it, but it needs very specific builds'
        note: 'House in Deep Shadows. Applies Mental Fatigue when an enemy fails a save against her — it compounds with her Acuity-inflated DC, so the next control lands more easily.'
      - id: opt-callous-glow-ring
        item: Callous Glow Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
        note: '+2 Radiant against ILLUMINATED targets on every projectile. Strong on a multi-hit ranged build, but it is currently Gale''s and it fights Charles''s darkness.'
    - id: cloak-of-cunning-brume
      item: Cloak of Cunning Brume
      tier: A
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (9:53) — best for certain strategies rather than universally good'
      slot: cloaks
      note: 'Sold by Mattis at Last Light Inn for about 70g. Disengaging also creates a 2m fog cloud for a turn, which obscures and blinds everything inside it — a genuine backline escape button for the moment something closes on her. ⚠ An honest cheap fill: the Act 2 cloak pool is built for melee characters (Fleshmelter and Thunderskin both trigger on being hit), and the one unconditional cloak, Cloak of Protection, goes to Charles, who has permanent disadvantage on saves. She upgrades properly in Act 3.'
    - id: act2-feet-bonbon
      item: Boots of Brilliance
      tier: B
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (42:08) — regains one Bardic Inspiration but needs fiddly swapping (captions garble the letter)'
      slot: feet
      note: Heavy chest in the room just north of Yurgir, Gauntlet of Shar. Restores one Bardic Inspiration charge per long rest. Slashing Flourish consumes an Inspiration on every multi-target turn and she is Inspiration-starved rather than AC-starved, so this beats keeping Boots of Speed once the Acuity loop replaces raw repositioning.
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      tier: S
      tier_note: 'ULTIMATE Guide to Rings - BG3 Honor Mode Tier List and Guide - Act 3 (8:21) — tons of builds are built around maximising it; locks enemies down'
      slot: ring 1
      bis: true
      note: 'THE ACT 3 ENGINE, in a backpack in the Chult jungle reached through Akabi''s wheel at the Circus — one party member only, so send her. After a weapon hit, Enchantment and Illusion spells become BONUS ACTIONS, so she builds Arcane Acuity with her action and fires Hold Monster or a six-target Command in the same turn. ⚠ Read the wiki caveat before playing it: once Quickening Incantation is active she can no longer cast those spells as an ACTION that turn — only as the bonus action. ⚠ Useful trick: any weapon attack triggers it, even against a world object, so she can prime the loop off a barrel before combat starts.'
    - id: act3-ring2-bonbon
      item: Caustic Band
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (7:16) — for almost every party; goes on whoever makes the most attacks in a round'
      rank: '#12'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #12 of 20 — a passive 2 acid on every weapon attack, which adds up on multiattackers'
      held: true
      slot: ring 2
      note: +2 Acid on every bolt and every Flourish projectile is still the cleanest flat rider available to her, and it needs no setup. Swap it for the Ring of Free Action in any fight with webs, paralysis or Black Tentacles, since being Paralysed both ends Hold Monster and hands out automatic critical hits.
    - id: act3-ranged-bonbon
      item: Titanstring Bow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (32:39) — adds your strength modifier; best in slot Act 1 damage with a giant strength elixir'
      held: true
      slot: ranged weapons
      bis: true
      note: 'The standing set, unchanged: Titanstring with a daily Elixir of Cloud Giant Strength for +8 on every projectile. ⚠ Gontr Mael is ASTERION''S: its Celestial Haste is a self-only Concentration spell, and she is already Hasted by Gale and concentrating on Hold Monster, so on her it did nothing. ⚠ Hellrider''s Longbow is Gale''s; he has the idle ranged slot.'
    - id: act3-melee-bonbon
      item: Phalar Aluve + Ketheric's Shield
      held: 2
      wiki:
      - Phalar Aluve
      - Ketheric's Shield
      slot: weapons
      bis: true
      note: 'CARRIED OVER. She still carries Shriek for the party from 3–6 m of the cluster, and Ketheric''s +1 spell save DC sits on top of the Acuity cap. Viconia''s Walking Fortress goes to Charles.'
    - id: act3-elixir-bonbon
      item: Elixir of Cloud Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (32:28) — sets Strength to 27; S used normally, S+ ABOVE THE SCALE if drunk daily; also enormous jump distance'
      slot: consumables
      note: 'STR 27 — +8 on every projectile, so a four-hit Action carries +32 from the elixir alone. Sold by level-9 vendors across Acts 2 and 3 with semi-random stock (Araj, Talli, Roah, Mattis, Danthelon, Helsik, Popper and more); Asterion drinks the same, so buy every one you see and fall back on Hill Giant on a short day.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 3 (13:32) — the only real decision left is who to put it on'
      slot: amulets
      note: 'NOT HERS, on reflection. Setting Constitution to 23 and granting advantage on CON saves is superb, but she already has War Caster''s advantage on those saves, AC 21 in Helldusk Armour, and a cloak that refreshes +2 AC every turn — so the amulet''s advantage half is redundant on her. Charles has a permanent DISADVANTAGE from the Risky Ring for it to cancel, which nothing else in the game does as cleanly. She keeps the Spellcrux Amulet instead, and a free level-6 slot per long rest is worth more to a controller than +6 to saves she is already winning.'
    - id: act3-amulet-bonbon
      item: Spellcrux Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (33:07) — plainly incredible'
      held: true
      slot: amulets
      note: A bonus-action level-6 spell slot once per long rest is a second six-target Command or a second Hold Monster in the fight that needs it. On a Bard 11 with exactly one slot at that level, this is the highest-leverage neck she can wear.
    - id: helldusk-armour-bonbon
      item: Helldusk Armour
      tier: S
      tier_note: 'VjmWkRCoDWE (57:31) — 21 AC, 3 damage reduction, anyone can wear it; ALSO S IF GRABBED IN ACT 1 BY EXPLOIT'
      slot: armour
      bis: true
      note: 'ACT 3 CHEST, carried by Raphael in the House of Hope. AC 21 flat, ALL INCOMING DAMAGE REDUCED BY 3, Fire resistance and immunity to Burning, Infernal Retribution (a caster whose spell she saves against starts Burning) and a non-concentration Fly once per long rest. It grants its own proficiency, so anyone can wear it — it went to nobody while Charles was locked to Luminous Armour. The damage reduction is the point for a concentrator: chip damage becomes zero, which means no concentration save and no Arcane Acuity stripped. ⚠ Heavy, so Stealth at disadvantage; Asterion sneaks, she does not.'
      options:
      - id: opt-armour-of-agility
        item: Armour of Agility
        tier: S
        tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (1:00:01) — 17 AC uncapped by Dex and +2 saves; the highest AC setup in the game'
        note: 'THE SAVE-FOCUSED ALTERNATIVE, sold by Gloomy Fentonson at the Stormshore Armoury: medium armour with her FULL Dexterity modifier and +2 to ALL saving throws, no Stealth penalty. At DEX 16 under Helldusk Gloves that is AC 20, one behind Helldusk''s flat 21; take it if +2 saves matter more than 3 damage reduction. ⚠ Do not take Medium Armour Master or Magic Initiate: Cleric on her — the wiki notes either feat breaks the full-Dexterity passive.'
    - id: wavemother-s-cloak
      item: Wavemother's Cloak
      tier: D
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (38:55) — a worse duplicate of another cloak''s effect, and combat-only'
      slot: cloaks
      note: 'ACT 3 CLOAK, in an opulent chest behind Allandra Grey''s desk on the upper floor of the Water Queen''s House. Once per turn in combat it grants Water Layer Protection until she takes damage: +2 AC, +2 to saving throws, Fire resistance and immunity to Burning. On a backline controller who is rarely hit, that refreshes every turn and effectively never falls off — strictly better than the flat +1/+1 of a Cloak of Protection for her, and it leaves Cloak of Displacement free for Asterion, who has no armour at all.'
    - id: act3-hands-bonbon
      item: Helldusk Gloves
      tier: S
      tier_note: 'The BEST GLOVES In BG3 COMPLETE - Honor Mode Tier List and Guide - Act 3 (24:29) — best in slot for almost anyone; +1d6 damage, +1 attack rolls and +1 spell save DC'
      slot: hands
      bis: true
      note: 'ACT 3 HANDS, worn by Haarlep in the House of Hope boudoir; no armour tag. Infernal Acuity is +1 spell save DC and, per the wiki, +1 to ALL attack rolls; Infernal Touch adds 1d6 Fire to every weapon hit — every Titanstring projectile. Against the Gloves of Dexterity that trades DEX 18 for her natural 16 (−1 attack, −1 damage, −1 AC, −1 initiative) for +1 Hold Monster DC and about +10 damage a turn. Keep the Gloves of Dexterity bagged; they are not wrong, just second. ⚠ Craterflesh Gloves want a crit-focused build she is not.'
    - id: act3-head-bonbon
      item: Helmet of Arcane Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (35:18) — broken like all the Arcane Acuity items, and one of the easiest to use'
      held: true
      slot: head
      bis: true
      note: 'It stays, and it is not close. Three or four weapon hits a turn take her to the +10 Arcane Acuity cap inside one round, which is +10 to spell save DC. ⚠ BIRTHRIGHT IS REJECTED FOR EXACTLY THIS REASON: +2 Charisma is +1 spell save DC. Ten against one. Keep Birthright bagged as an out-of-combat swap for Persuasion, Deception and Intimidation, where the wiki notes it stacks with the Mirror of Loss for Charisma 24.'
    - id: act3-feet-bonbon
      item: Boots of Persistence
      tier: B
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (51:25) — reasonable, though Freedom of Movement on one character is not a tremendous effect'
      slot: feet
      note: 'Sold by Dammon at the Forge of the Nine in the Lower City. Permanent Freedom of Movement and Longstrider — Freedom of Movement makes a Ring of Free Action unnecessary and frees her second ring slot for Caustic Band. Medium armour proficiency is required and Fighter 1 supplies it. ⚠ Helldusk Boots are the better item in the abstract but go to Charles, who has save disadvantage to undo; Gale cannot wear Persistence at all, so this is the allocation that leaves nobody stranded.'
    progression:
    - id: prog-head
      item: 'Head: Grymskull Helm → Diadem of Arcane Synergy → Helmet of Arcane Acuity'
      slot: head
      note: Free Grymskull crit immunity as a stopgap → Diadem (Crèche) for CHA on ranged hits → Helmet of Arcane Acuity (Mason's Guild, Act 2) for the rest of the run. The Helmet never comes off again — Birthright's +2 Charisma is +1 spell DC against Acuity's +10.
    - id: prog-armour
      item: 'Chest: The Protecty Sparkswall → Adamantine Splint Armour → Helldusk Armour'
      slot: armour
      note: Act 1 early Protecty (Grymforge) for +1 spell DC → Act 1 late and Act 2 Adamantine Splint (first Mithral ore) for AC 18 and crit immunity → Act 3 Helldusk Armour (Raphael) for AC 21 and 3 damage reduction on every hit. Armour of Agility is the +2-saves alternative; keep the Splint bagged for fights where crit immunity beats everything.
    - id: prog-hands
      item: 'Hands: Gloves of Archery → Gloves of Dexterity → Helldusk Gloves'
      slot: hands
      note: Act 1 early Archery gloves (Grat) → Gloves of Dexterity from the Crèche through Act 2 → Helldusk Gloves (Haarlep, House of Hope) in Act 3 for +1 spell save DC, +1 to all attack rolls and 1d6 Fire on every projectile.
    - id: prog-feet
      item: 'Boots: Boots of Speed → Boots of Brilliance → Boots of Persistence'
      slot: feet
      note: Act 1 Boots of Speed for a character with no innate mobility → Act 2 Boots of Brilliance (Gauntlet of Shar) once Bardic Inspiration becomes the bottleneck → Act 3 Boots of Persistence (Dammon) for permanent Freedom of Movement, which frees a ring slot.
    - id: prog-cloaks
      item: 'Cloak: none available → Cloak of Cunning Brume → Wavemother''s Cloak'
      slot: cloaks
      note: Empty in Act 1 because no magical cloak exists then → cheap Cunning Brume (Mattis) as a backline escape → Wavemother's Cloak (Water Queen's House) in Act 3, whose +2 AC and +2 saves refresh every turn she is not hit, which for her is most of them.
    - id: prog-amulets
      item: 'Amulet: Broodmother''s Revenge → Spellcrux Amulet'
      slot: amulets
      note: Act 1 Broodmother's (Kagha) while her bonus action is free for Healing Word → Act 2–3 Spellcrux (Moonrise Prison Warden), which returns a level-6 slot as a bonus action once per long rest — a second six-target Command.
    - id: prog-ring1
      item: 'Ring 1: Caustic Band → Band of the Mystic Scoundrel'
      slot: ring 1
      note: Caustic Band holds this hand through Acts 1 and 2 — a flat 2 acid on every attack, which is worth most on the character making the most attacks → Band of the Mystic Scoundrel in Act 3, which turns her Command into a bonus action at the party's highest Arcane Acuity DC.
    - id: prog-ring2
      item: 'Ring 2: The Whispering Promise → flex → Caustic Band'
      slot: ring 2
      note: The Whispering Promise until Asterion's Staff of Arcane Blessing takes over Bless duty, then a flex slot per fight, then Caustic Band moves across to this hand once the Band of the Mystic Scoundrel claims ring 1.
    - id: prog-weapons
      item: 'Melee: Club + Knife → Club + Sentinel Shield → Phalar Aluve + Ketheric''s Shield'
      slot: weapons
      note: A stat-stick set she never swings, and every holder passive on it applies while she shoots. Act 1 Club (STR 19 for Titanstring) + Knife → Club + Sentinel Shield (Moonrise) for +2 AC and +3 Initiative → from the Stone, Phalar Aluve (from Charles) + Ketheric's Shield (Colony) for +2 AC and +1 spell save DC, and she carries Shriek for the party from 3–6 m.
    - id: prog-ranged
      item: 'Ranged: Titanstring Bow, all game'
      slot: ranged weapons
      note: Two Flourishes an Action are four Acuity triggers, and any Hasted turn caps Acuity on its own, so the hand-crossbow pivot was never needed. Titanstring's Strength rider stays on every projectile through a daily Giant Strength elixir once the Club is gone. Gontr Mael goes to Asterion.
    - id: prog-consumables
      item: 'Elixir: Bloodlust (Act 1) → Giant Strength (Hill, then Cloud) from the Stone'
      slot: consumables
      note: Bloodlust while the Club supplies Strength — an extra Action on any kill; Hill Giant for a lone boss. From the Stone the Club is gone, so Giant Strength is the standing elixir every long rest, Cloud Giant (STR 27) once level-9 vendors carry it. Stock heavily — Asterion drinks the same.
  playstyle: |-
    - **Act 1 default:** equip Titanstring plus the Hill Giant club main hand and Knife of the Undermountain King off-hand, drink Bloodlust, and use Protecty Sparkswall to raise Hold Person/control DC. Use ranged Slashing Flourish for nova damage and trigger Broodmother's Revenge with healing before a multi-projectile turn.
    - **Act 1 alternatives:** use a Hill Giant elixir for a boss with no Bloodlust target; use Adamantine Splint for defence.
    - **Act 2+:** keep Titanstring; two ranged Flourishes a turn are four Acuity triggers and a Hasted turn caps it. From the Stone she carries Phalar Aluve: Shriek with the Haste action on turn 1, standing 3–6 m from the melee cluster, then Flourish. In Act 3, spend Acuity on a same-turn bonus-action Hold Monster or Command.
    - **Protect concentration:** stay at range. Against undead, use Hypnotic Pattern or Slow instead of Hold Monster/Command.
    - **Carry the party's Daylight:** Gale casts Daylight (Enchant Item) on Bonbon's main-hand weapon once per long rest — it is bugged to last until the next rest and travels with her, keeping Gale lit for his Coruscation → Callous Glow chain. She is the carrier because the spell requires a main-hand weapon, which rules out Asterion's empty Tavern Brawler hands, and because her mid-range position keeps the 15m radius over the fight. ⚠ Do not swap her main-hand weapon afterwards, and let Gale cast it *before* any Darkness Arrow goes out.
    - **Division of control with Gale:** Bonbon owns the *Concentration* lane (Hold Person/Hold Monster — the auto-crit setup for Charles); Gale owns the *non-concentration* lane (Extended Command). They stack rather than compete, so do not both spend a turn on the same target.
---
