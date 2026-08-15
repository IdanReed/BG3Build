---
nickname: Bonbon
builds:
- name: The Commander
  is_primary: true
  role: Ranged acuity control + damage + party face
  class: Swords Bard 11 / Fighter 1
  build_order: Fighter 1 at character creation → Swords Bard 1–11. No respec, no Wizard dip.
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
  stats_note: 'Point-buy 8/15/14/8/10/15 = all 27 (DEX 15 + CHA 15 cost 9 each). +2 → CHA 17, +1 → DEX 16; Gloves of Dexterity then set DEX to 18 (Crèche, Act 1). No INT — the Wizard dip is dropped.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss). Birthright reaches CHA 22 in Act 3 if Gale is not using it.'
  feats:
  - at: Bard 4 (char 5)
    feat: Sharpshooter
  - at: Bard 8 (char 9)
    feat: War Caster
    note: Advantage on CON saves to hold Hold Monster — the party's melee auto-crit engine — plus opportunity-spell casting. Chosen over Dual Wielder because hand crossbows are Light and dual-wield without it.
  fighting_styles:
  - Archery (Fighter)
  - Dueling (Bard)
  key_spells:
  - Glyph of Warding
  - Hold Monster
  - Confusion
  - Fear
  - Magical Secrets → Command + Globe of Invulnerability
  creation:
    level1_class: Fighter 1 (taken at character creation)
    level1_gains: 'Archery fighting style (+2 ranged), Second Wind, and — because Fighter is taken FIRST — STR + CON saves, all armour (incl. Heavy) + shields + martial weapons, and 2 Fighter skills.'
    subclass_choice: College of Swords (Bard 3)
    proficiencies:
      armor_weapons: All armour, shields, martial weapons and Archery (Fighter 1); Medium + Scimitars (College of Swords).
      saving_throws: STR + CON (Fighter-first) — CON guards Hold Monster concentration.
      skills: Fighter 2 + Bard skills; Expertise ×4 (Bard 3 + 10) + Jack of All Trades — the party face.
    starting_cantrips: '2 at Bard 1 (Vicious Mockery, Friends) → 4 by Bard 10.'
    starting_spells: '4 known at Bard 1 → ~14 by Bard 11, plus 2 Magical Secrets at Bard 10. No Wizard dip means no Shield reaction — lean on range, positioning and the Fighter dip''s heavy armour instead.'
    notes: 'Half-Elf/Human. Fighter 1 at creation → Swords Bard ×11, no respec. Bard 11 = caster level 11 → one L6 slot, so Command still hits up to 6 targets WITHOUT a Wizard dip. Dropping Wizard costs only the Shield reaction and scroll scribing. Feats/ASIs at Bard 4 (char 5) and Bard 8 (char 9).'
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
      why: Paralyse — attacks within 3m auto-crit, the melee auto-crit engine for Charles's smites. Upcast adds +1 target per slot above 5th. Concentration.
    - spell: Command
      level: '1'
      guide_level: 11
      school: Enchantment
      save: WIS save
      when: Bard 10 (Magical Secrets)
      why: The bonus-action loop via the Band of the Mystic Scoundrel. +1 target per slot above 1st, so the Bard-11 L6 slot hits up to 6. DC uses CHA + Arcane Acuity.
    - spell: Glyph of Warding
      level: '3'
      guide_level: 6
      school: Abjuration
      save: DEX save
      when: Bard 5
      why: Pre-placed AoE burst (5d8, choose element) set as a ground trap before a fight.
    recommended:
    - spell: Fear
      level: '3'
      guide_level: 9
      school: Illusion
      save: WIS save
      when: Bard 5
      why: 9m cone — frightened enemies drop weapons and cannot act or approach; scales with CHA + Arcane Acuity. Concentration.
    - spell: Confusion
      level: '4'
      guide_level: 8
      school: Enchantment
      save: WIS save
      when: Bard 7
      why: 6m scramble — enemies attack randomly or skip turns. Concentration.
    - spell: Hypnotic Pattern
      level: '3'
      guide_level: 6
      school: Illusion
      save: WIS save
      when: Bard 5
      why: Best-in-class AoE lockdown (9m incapacitate) and a superb acuity payoff. Concentration; breaks on damage.
    - spell: Globe of Invulnerability
      level: '6'
      guide_level: 11
      school: Abjuration
      save: None (Concentration)
      when: Bard 10 (Magical Secrets)
      why: 'REPLACES Counterspell as the second Magical Secret. Rated the #9 spell in the game and unreachable by any other party member — the plan previously budgeted for scrolls, and this makes it repeatable. A dome that blocks incoming spells outright, which is the answer to the Act 3 caster gauntlets and to the Netherbrain''s area attacks. ⚠ Concentration, so it competes with Hold Monster: use it on the turns where survival beats control. Counterspell is dropped because Gale and Charles already cover that lane and three carriers is one more than the guides advise.'
    - spell: Hold Person
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Bard 3
      why: Cheaper single-target paralyse (auto-crit within 3m), far earlier than Hold Monster — the early-game stand-in. Concentration.
    - spell: Dominate Person
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Bard 9
      why: Turn a humanoid against its allies — a flex 5th-level pick alongside Hold Monster. Concentration.
    - spell: Vicious Mockery
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Psychic damage plus disadvantage on the target's next attack — free ranged control that feeds acuity.
    - spell: Friends
      level: Cantrip
      guide_level: 2
      school: Enchantment
      save: None (Concentration)
      when: Bard 1
      why: Advantage on Charisma checks against a non-hostile creature — the face enabler. Never cast it on companions (approval loss when it ends).
    - spell: Slow
      level: '3'
      guide_level: 7
      school: Transmutation
      save: WIS save
      when: Bard 5
      why: UNDEAD-PROOF control, unlike Hold Monster/Command — half speed, −2 AC and DEX saves, one action only, ~50% chance to fizzle a cast. Bank it for the Act-2 undead and construct fights where paralysis fails. Concentration.
    - spell: Healing Word
      level: '1'
      guide_level: 2
      school: Evocation
      save: None
      when: Bard 1
      why: The no-healer party's emergency pickup — a bonus-action ranged revive so a downed ally does not cost a full turn. Cheap to keep known; pairs with stocked Revivify scrolls.
    - spell: Longstrider
      level: '1'
      guide_level: 2
      school: Transmutation
      save: None (ritual)
      when: Bard 1
      why: Free out-of-combat party movement buff lasting until long rest, with no Concentration.
    - spell: Enhance Ability
      level: '2'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Bard 4
      why: Advantage on checks with one chosen ability. At char 5, replace the redundant Faerie Fire with it for dialogue, theft and exploration — an out-of-combat mode, never held alongside Hold Person.
    - spell: Dissonant Whispers
      level: '1'
      guide_level: 2
      school: Enchantment
      save: WIS save
      when: Bard 1
      why: Early psychic damage plus Frightened — useful single-target control before the Acuity engine.
    - spell: Faerie Fire
      level: '1'
      guide_level: 2
      school: Evocation
      save: DEX save
      when: Bard 1
      why: Early area advantage and anti-invisibility. Concentration, so replace it once stronger control arrives.
    - spell: Tasha's Hideous Laughter
      level: '1'
      guide_level: 3
      school: Enchantment
      save: WIS save
      when: Bard 2
      why: Cheap early single-target incapacitation — a bridge to Hold Person that can be replaced later.
    - spell: Invisibility
      level: '2'
      guide_level: 5
      wiki: Invisibility (spell)
      school: Illusion
      save: None
      when: Bard 4
      why: Scouting, theft setup and an emergency escape — strong out-of-combat utility.
    - spell: Otto's Irresistible Dance
      level: '6'
      guide_level: 12
      school: Enchantment
      save: WIS save after the effect begins
      when: Bard 11
      why: Immediate single-target shutdown when the level 6 slot is not reserved for an upcast Command.
    - spell: Mage Hand
      level: Cantrip
      guide_level: 5
      school: Conjuration
      save: None
      when: Bard 4
      why: 'Exploration and object manipulation with no attack roll, save or Concentration. For a no-slot Wet setup, drop a water bottle in reach and use the Hand''s Throw for a 2m splash.'
    - spell: Light
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
    recommendations:
    - category: Fighting style
      recommendation: Archery
      note: +2 to ranged attack rolls offsets Sharpshooter and stays essential after the hand-crossbow pivot.
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
      note: Mockery is the ranged fallback; Friends supports the face role but must never be cast on companions.
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
      note: Archery already covers the ranged plan; Dueling is the melee fallback.
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
      note: The +10 damage mode is the Act 1 ranged spike; Archery and advantage offset the attack penalty.
    - category: Cantrip
      recommendation: Mage Hand
      note: 'Exploration utility with no concentration cost. For a no-slot Wet setup, drop a water bottle for the Hand and use its Throw on the Hand''s turn.'
    - category: Spells
      recommendation:
      - Invisibility
      - Enhance Ability
      note: Learn Invisibility; use the level-up replacement to trade Faerie Fire for Enhance Ability. Both concentrate — exploration tools once Hold Person is online.
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
      note: The flexible cone-control option, added without delaying the earlier core picks.
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
      note: Learn Hold Monster first; replace a lower-level flex spell for Dominate Person if both are wanted immediately.
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
      - Globe of Invulnerability
      note: 'CHANGED. Command stays — hers is genuinely unique because the Band of the Mystic Scoundrel makes it a BONUS ACTION at the party''s highest Acuity DC, and her level 6 slot upcasts it to six targets, neither of which Gale can replicate. Counterspell is dropped: Gale learns it at Sorc 6 and Charles gets it post-respec, so taking it here would give the party THREE carriers where the guides recommend two. Globe of Invulnerability is rated the #9 spell in the game and is otherwise unreachable by any of the four — the plan previously covered it by buying scrolls, and a Magical Secret makes it repeatable. Heroes'' Feast is the alternative pick if you would rather have a permanent party-wide buff than an emergency dome.'
    - category: Expertise
      recommendation:
      - Insight
      - Intimidation
      note: Completes face and dialogue coverage; swap one for a campaign-specific skill if preferred.
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
      note: Brem, after Find the Missing Shipment. Archery + Sharpshooter + ranged Slashing Flourish apply its STR rider to large, accurate nova shots. Default to the STR 19 Club + Knife + Bloodlust package; Hill Giant elixir for a boss where Bloodlust cannot trigger.
    - id: club-of-hill-giant-strength
      item: Club of Hill Giant Strength (melee main hand)
      slot: weapons
      note: Titanstring stat stick, from the Arcane Tower. Light club main hand, Knife off-hand, Titanstring in the ranged slot — STR 19 adds +4 damage per projectile and keeps the elixir slot free for Bloodlust.
    - id: knife-of-the-undermountain-king-offhand
      item: Knife of the Undermountain King (melee off-hand)
      slot: weapons
      note: Crèche stat stick beside the Light club, no feat needed. Organ Rearranger lowers the crit threshold on Titanstring and spell attacks — that global crit-range bonus is the reason to carry it. The low-die reroll is melee-only, not ranged.
    - id: elixir-of-bloodlust
      item: Elixir of Bloodlust (default)
      slot: consumables
      note: DEFAULT with adds. A kill grants 5 temp HP and another Action once per turn, and non-Honour that Action benefits from Extra Attack. The Club costs only 1 Titanstring damage per projectile versus STR 21 — repaid by one extra Action.
    - id: elixir-of-hill-giant-strength
      item: Elixir of Hill Giant Strength (boss alternative)
      slot: consumables
      note: For a lone boss or any fight with no dependable Bloodlust kill. STR 21 raises the Titanstring rider from +4 to +5. Keep a big stock — Asterion needs one daily too.
    - id: gloves-of-archery
      item: Gloves of Archery (early default)
      slot: hands
      note: Grat at the Goblin Camp. Longbow proficiency is redundant, but +2 damage applies to every ranged weapon hit — the clean early Titanstring glove.
    - id: wondrous-gloves
      item: Wondrous Gloves (Flourish alternative)
      slot: hands
      note: Grymforge Mimic loot. +1 AC and one extra Bardic Inspiration supply another Slashing Flourish — take them for a nova-focused rest cycle when accuracy is already comfortable.
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      slot: hands
      note: Crèche. DEX 18 + 1 Attack Rolls = net +2 ranged accuracy over natural DEX 16, plus better initiative, AC, DEX saves and skills. Swap to Wondrous Gloves only when the extra Flourish beats the accuracy.
    - id: the-protecty-sparkswall
      item: The Protecty Sparkswall
      slot: armour
      note: Grymforge. +1 Spell Save DC improves Hold Person, Hypnotic Pattern, Fear, Slow and Glyph; with Lightning Charges it adds +1 AC and saves. The low clothing AC is the deliberate price of control DC at range.
    - id: adamantine-scale-mail
      item: Adamantine Splint Armour (defensive alternative)
      slot: armour
      note: DEFENSIVE ALTERNATIVE — Fighter-first grants proficiency. AC 18 flat, crit immunity, all incoming damage reduced by 2, Reeling. Take it when survival beats Protecty's +1 spell DC. (The ID keeps its old scale-mail name so checklist keys survive.)
    - id: adamantine-shield
      item: Adamantine Shield (melee off-hand stat stick)
      slot: off-hand
      note: 'THE SECOND ORE — replanned. Bonbon is the party''s only legal Adamantine wearer, and this is the piece the old plan wrote off as having "no legal wielder." Per the wiki, "a character need not to be actively holding the equipped shield to get the AC bonus… a character with a sword and shield in its melee weapon slots and a longbow in its ranged weapon slots benefits from the shield''s AC bonus even while using the bow." So it sits in her MELEE off-hand, replacing the Knife of the Undermountain King, while she fights from the ranged set as normal: +2 AC and crit immunity for free. Crit immunity matters most on HER because she holds Hold Monster — a concentration save is DC = half the damage taken or 10, whichever is higher, so a crit roughly doubles that DC — and because it stops Hold Person or Sleeping from handing attackers automatic crits. ⚠ COSTS the Knife''s global crit-threshold reduction, and ⚠ VERIFY IN PLAY that crit immunity (not just AC) carries over from the inactive melee set; the wiki only confirms the AC bonus. If it does not carry, wear the free Grymskull Helm through Act 1 instead and sell the ore.'
    - id: the-whispering-promise
      item: The Whispering Promise
      slot: rings
      note: 'THE CHAR 1–3 BLESS FIX. Volo, or Grat at the Goblin Camp, for about 40g — so it is available before the Grove is resolved. Healing a creature gives it +1d4 to attacks and saves for 2 turns with NO Concentration. Bonbon is the carrier because her Healing Word is a BONUS ACTION and because she already runs Broodmother''s Revenge, so a single bonus action fires both riders at once. Best trigger for the whole party is a THROWN Potion of Healing, which blesses every creature it splashes; it also works on targets already at full HP, and drinking a potion self-triggers it. ⚠ It applies the SAME condition as the Bless spell, so it does NOT stack with Charles''s Bless and is NOT boosted by his Staff of Arcane Blessing — its value is levels 1–3 before Charles has Bless, and later any fight where he concentrates on Hex or Darkness instead. Displaces Caustic Band; swap back once Charles''s Bless is reliable.'
    - id: caustic-band
      item: Caustic Band
      slot: rings
      note: Derryth, Underdark. +2 Acid per weapon hit — the multiple Slashing-Flourish projectiles exploit it better than Charles's smaller Act 1 attack count. Returns to the ring slot once The Whispering Promise has done its job in the early levels.
    - id: diadem-of-arcane-synergy
      item: Diadem of Arcane Synergy
      slot: head
      note: Ardent Jhe'rezath, Crèche. Once a spell condition lands (Hold Person, Fear, Dissonant Whispers), Arcane Synergy adds CHA to each subsequent ranged weapon attack for 2 turns — the many Titanstring and Flourish hits exploit the flat rider best. Replaced by the Helmet of Arcane Acuity in Act 2.
    - id: broodmother-s-revenge
      item: Broodmother's Revenge
      slot: amulets
      note: After saving the Grove — knock the isolated friendly Kagha out non-lethally and loot it. Any healing, even a potion at full HP, coats Titanstring for +1d6 Poison per projectile for 2 turns. Skip vs poison-resistant or immune enemies.
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      slot: head
      note: 'Mason''s Guild — +2 Acuity per hit → higher spell save DC. THE pivot: switch to dual hand crossbows now, since more hits per turn stack Acuity far faster than Titanstring''s single big shots.'
    - id: dual-hand-crossbows
      item: Ne'er Misser + Hellfire Hand Crossbow
      wiki:
      - Ne'er Misser
      - Hellfire Hand Crossbow
      slot: weapons
      note: Roah at Moonrise + Yurgir. Both Light, so no Dual Wielder feat. Main-hand, off-hand and Flourish hits stack Acuity fast; Asterion is unarmed now and needs neither.
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      slot: rings
      note: Akabi's Circus wheel → Chult jungle. Enchantment and Illusion spells become bonus actions after a weapon hit, so Bonbon can build Arcane Acuity and cast Hold Monster or Command in the same turn.
    - id: bow-alternative
      item: Hellrider's Longbow (initiative alternative)
      wiki: Hellrider Longbow
      slot: weapons
      note: Rivington. +initiative, handy for a controller who wants to act first. Gontr Mael is the stronger bow but grants NO initiative.
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      slot: amulets
      note: Sets CON to 23 and grants advantage on CON saves. Stacks with War Caster to protect Hold Monster concentration, which enables Charles's automatic melee crits.
  playstyle: |-
    - **Act 1 default:** equip Titanstring plus the Hill Giant club main hand and Knife of the Undermountain King off-hand, drink Bloodlust, and use Protecty Sparkswall to raise Hold Person/control DC. Use ranged Slashing Flourish for nova damage and trigger Broodmother's Revenge with healing before a multi-projectile turn.
    - **Act 1 alternatives:** use a Hill Giant elixir for a boss with no Bloodlust target; use Adamantine Splint for defence.
    - **Act 2+:** switch to dual hand crossbows and Flourish to stack Arcane Acuity. In Act 3, spend it on a same-turn bonus-action Hold Monster or Command.
    - **Protect concentration:** stay at range. Against undead, use Hypnotic Pattern or Slow instead of Hold Monster/Command.
    - **Carry the party's Daylight:** Gale casts Daylight (Enchant Item) on Bonbon's main-hand weapon once per long rest — it is bugged to last until the next rest and travels with her, keeping Gale lit for his Coruscation → Callous Glow chain. She is the carrier because the spell requires a main-hand weapon, which rules out Asterion's empty Tavern Brawler hands, and because her mid-range position keeps the 15m radius over the fight. ⚠ Do not swap her main-hand weapon afterwards, and let Gale cast it *before* any Darkness Arrow goes out.
    - **Division of control with Gale:** Bonbon owns the *Concentration* lane (Hold Person/Hold Monster — the auto-crit setup for Charles); Gale owns the *non-concentration* lane (Extended Command). They stack rather than compete, so do not both spend a turn on the same target. Bonbon also keeps Hellrider's Longbow by default, since she needs to land the first weapon hit to open the Band loop.
---
