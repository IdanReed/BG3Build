---
nickname: Bonbon
builds:
- name: The Commander
  is_primary: true
  role: Ranged acuity control + damage + party face
  class: Swords Bard 11 / Fighter 1
  build_order: Fighter 1 at character creation → Swords Bard 1–11. No respec at any point.
  race: Half-Elf or Human (early shield)
  background: Guild Artisan (Insight, Persuasion) — proficiencies.md assumes this one
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
  stats_note: 'Point-buy 8/15/14/8/10/15 = all 27 (DEX 15 + CHA 15 cost 9 each). +2 → CHA 17, +1 → DEX 16; Gloves of Dexterity then set DEX to 18 (Crèche, Act 1). INT stays at 8 — nothing in the build uses it.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss). Birthright reaches CHA 22 in Act 3 if Gale is not using it.'
  feats:
  - at: Bard 4 (char 5)
    feat: Sharpshooter
  - at: Bard 8 (char 9)
    feat: War Caster
    note: Advantage on CON saves to hold Hold Monster — the party's melee auto-crit engine — plus opportunity-spell casting. Taken over Dual Wielder because hand crossbows are Light and dual-wield without it.
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
    starting_spells: '4 known at Bard 1 → ~14 by Bard 11, plus 2 Magical Secrets at Bard 10. She has no Shield reaction — lean on range, positioning and the Fighter dip''s armour proficiency instead.'
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
      why: 'Strong 9m AoE incapacitate and a superb Acuity payoff. ⚠ The tier lists rate it only A, not S — the duration is short and ANY damage wakes the targets, so it does not survive a party that is already firing into the pack. Treat it as a way to buy one clean turn, not as a lockdown. Concentration.'
    - spell: Globe of Invulnerability
      level: '6'
      guide_level: 11
      school: Abjuration
      save: None (Concentration)
      when: Bard 10 (Magical Secrets)
      why: 'The second Magical Secret. Rated the #9 spell in the game and unreachable by any other party member, so taking it here is the only way to have it repeatably rather than off scrolls. A dome that blocks incoming spells outright, which is the answer to the Act 3 caster gauntlets and to the Netherbrain''s area attacks. ⚠ Concentration, so it competes with Hold Monster: use it on the turns where survival beats control. Counterspell stays off her list because Gale and Charles already cover that lane, and three carriers is one more than the guides advise.'
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
      why: 'Advantage on checks with one chosen ability. At char 5, replace the redundant Faerie Fire with it for dialogue, theft and exploration — an out-of-combat mode, never held alongside Hold Person. ⚠ Rated only B: "significant checks are less frequent than players expect," and Bonbon already has Expertise ×4 plus Jack of All Trades. Low stakes either way.'
    - spell: Greater Invisibility
      level: '4'
      guide_level: 8
      school: Illusion
      save: None (Concentration)
      when: Bard 7+ — optional pick
      why: 'A-tier, and the tier lists note it "anchors an entire party strategy" — the target stays invisible while attacking, giving permanent advantage and imposing disadvantage on attacks against it. Concentration, so it directly competes with Hold Monster: take it as the survivability alternative for fights where nothing worth Holding exists, or on a run where you want the stealth loop.'
    - spell: Silence
      level: '2'
      guide_level: 5
      school: Illusion
      save: None (Concentration)
      when: Bard 3+ — optional pick
      why: 'A-tier. A zone that hard-disables enemy spellcasting with no save at all — the answer to the Act 3 caster packs that Counterspell can only handle one at a time, and the reason leaving Counterspell off her list costs less than it looks. Concentration.'
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
      note: 'Command is hers and genuinely unique, because the Band of the Mystic Scoundrel makes it a BONUS ACTION at the party''s highest Acuity DC, and her level 6 slot upcasts it to six targets, neither of which Gale can replicate. Counterspell stays off her list: Gale learns it at Sorc 6 and Charles gets it post-respec, so taking it here would give the party THREE carriers where the guides recommend two. Globe of Invulnerability is rated the #9 spell in the game and is otherwise unreachable by any of the four, and a Magical Secret is what makes it repeatable instead of a scroll purchase. Heroes'' Feast is the alternative pick if you would rather have a permanent party-wide buff than an emergency dome.'
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
      note: 'Crèche stat stick beside the Light club, no feat needed. Organ Rearranger lowers the crit threshold globally, which is the reason to carry it — it improves Titanstring and her spell attacks, not just melee. The low-die reroll is melee-only. She keeps it for the whole run; the Adamantine ore goes into armour instead of the shield, so nothing displaces it.'
    - id: elixir-of-bloodlust
      item: Elixir of Bloodlust (default)
      slot: consumables
      note: DEFAULT with adds. A kill grants 5 temp HP and another Action once per turn, and outside Honour that Action benefits from Extra Attack. The Club costs only 1 Titanstring damage per projectile versus STR 21 — repaid by one extra Action.
    - id: elixir-of-hill-giant-strength
      item: Elixir of Hill Giant Strength (boss alternative)
      slot: consumables
      note: For a lone boss or any fight with no dependable Bloodlust kill. STR 21 raises the Titanstring rider from +4 to +5. Keep a big stock — Asterion needs one daily too.
    - id: gloves-of-archery
      item: Gloves of Archery (early default)
      slot: hands
      note: Grat at the Goblin Camp. Longbow proficiency is redundant, but +2 damage applies to every ranged weapon hit — the clean early Titanstring glove, worn until the Crèche.
    - id: gloves-of-dexterity
      item: Gloves of Dexterity
      slot: hands
      note: 'LATE-ACT-1 DEFAULT, from the Crèche, and rated the #1 item of the 20 best in Act 1 — "the most impactful equipable item in Act 1, and in the narrator''s view the entire game." DEX 18 plus +1 Attack Rolls is a net +2 ranged accuracy over natural DEX 16, plus initiative, AC, DEX saves and skills. ⚠ The video pitches these at a Sorcerer who respecs DEX to 8 and reclaims the points; that does not work here, because the gloves are a Crèche pickup and the character would spend all of early Act 1 at DEX 8. On Bonbon the +1 Attack Rolls also applies to every projectile of a Slashing Flourish and every hand-crossbow bolt — four or more attack rolls a turn.'
    - id: wondrous-gloves
      item: Wondrous Gloves (Flourish alternative)
      slot: hands
      note: Grymforge Mimic loot. +1 AC and one extra Bardic Inspiration supply another Slashing Flourish — take them for a nova-focused rest cycle when accuracy is already comfortable.
    - id: the-protecty-sparkswall
      item: The Protecty Sparkswall
      slot: armour
      note: 'ACT 1 CHEST, from the gilded chest at the end of the trapped Grymforge bridge, and rated #8 of 20 as "the caster default through much of Act 2." +1 Spell Save DC improves Hold Person, Hypnotic Pattern, Fear, Slow and Glyph. ⚠ Its second effect, +1 AC and saves while carrying Lightning Charges, is dead here — she has no charge generator, since The Spellsparkler is Gale''s. Take it purely for the flat +1 DC, and understand the low clothing AC is the price of control DC at range until the Adamantine Forge.'
    - id: adamantine-scale-mail
      item: Adamantine Splint Armour (late-Act-1 upgrade)
      slot: armour
      note: 'THE FIRST MITHRAL ORE, and the chest she finishes Act 1 in. Fighter-first grants Heavy proficiency and she is the party''s ONLY legal wearer. AC 18 flat, ATTACKERS CANNOT LAND CRITICAL HITS, all incoming damage reduced by 2, and melee attackers sent Reeling. Crit immunity is what protects Hold Monster: a concentration save is DC = half the damage taken or 10, whichever is higher, so a critical hit roughly doubles that DC. Swap off Protecty once she has it and accept losing +1 spell DC for 6 AC and crit immunity. (The ID keeps an older name so existing checkoffs survive.)'
    - id: the-whispering-promise
      item: The Whispering Promise
      slot: rings
      note: 'THE CHAR 1–3 BLESS FIX, rated #10 of 20. Volo, or Grat at the Goblin Camp, for about 40g — available before the Grove is resolved. Healing a creature gives it +1d4 to attacks and saves for 2 turns with NO Concentration. Bonbon is the carrier because her Healing Word is a BONUS ACTION and she already runs Broodmother''s Revenge, so one bonus action fires both riders. Best trigger for the whole party is a THROWN Potion of Healing, which blesses every creature it splashes; it works on targets already at full HP, and drinking a potion self-triggers it. ⚠ It applies the SAME condition as the Bless spell, so it does NOT stack with Charles''s Bless and is NOT boosted by his Staff of Arcane Blessing — its value is levels 1–3 before Charles has Bless, and later any fight where he concentrates on Hex or Darkness instead.'
    - id: caustic-band
      item: Caustic Band
      slot: rings
      note: 'Derryth, Underdark, rated #12 of 20 and explicitly for characters making several attacks per turn. +2 Acid per weapon hit, applied to every Slashing-Flourish projectile. ⚠ Per the wiki it covers melee, ranged and Thrown attacks but NOT Unarmed Strike, which is why it can never move to Asterion despite his higher hit count. She wears it alongside the Whispering Promise — she has two ring slots and the two do not conflict.'
    - id: diadem-of-arcane-synergy
      item: Diadem of Arcane Synergy
      slot: head
      note: Ardent Jhe'rezath, Crèche. Once a spell condition lands (Hold Person, Fear, Dissonant Whispers), Arcane Synergy adds CHA to each subsequent ranged weapon attack for 2 turns — the many Titanstring and Flourish hits exploit the flat rider best. It gives way to the Helmet of Arcane Acuity in Act 2.
    - id: grymskull-helm
      item: Grymskull Helm (free early head)
      slot: head
      note: Free from Grymforge, and worth wearing on the way to the Crèche — crit immunity costs nothing and covers the stretch before either the Diadem or the Adamantine Splint exists. Retire it as soon as the Diadem lands.
    - id: broodmother-s-revenge
      item: Broodmother's Revenge
      slot: amulets
      note: 'After saving the Grove — talk Kagha down, then knock the isolated friendly Kagha out non-lethally and loot it. Rated #17 of 20. Any healing, even a potion at full HP, coats Titanstring for +1d6 Poison per projectile for 2 turns, and her bonus-action Healing Word fires it alongside the Whispering Promise. Skip against poison-resistant or immune enemies.'
    - id: boots-of-speed
      item: Boots of Speed
      slot: feet
      note: 'HERS, and rated #14 of 20. Bonus-action Dash for a character with no innate mobility, which is exactly what the video means by giving it to "the character most likely to waste a turn out of position." ⚠ It is NOT Asterion''s: Step of the Wind already gives him bonus-action Dash and Disengage from Monk 2, so the boots would buy him nothing while displacing the Night Walkers. ⚠ The video flags the opportunity-attack rider as bugged — take these for the Dash, not the defensive text.'
    - id: act1-cloak-bonbon
      item: No cloak exists yet
      slot: cloaks
      note: Deliberately empty. The Deathstalker Mantle is the only magical cloak obtainable in Act 1 and it is a Dark Urge reward that goes to Asterion; every other cloak in the game first appears in Act 2 or later. Her slot opens at Last Light.
    act2:
    - id: helmet-of-arcane-acuity
      item: Helmet of Arcane Acuity
      slot: head
      note: 'Mason''s Guild in Reithwin Town — an Act 2 pickup, not an Act 3 one. +2 Arcane Acuity per weapon hit, each remaining turn giving +1 spell attack AND +1 spell save DC, capped at 10. THE PIVOT: switch to dual hand crossbows now, because more hits per turn stack Acuity far faster than Titanstring''s single big shots. Extra Attack plus off-hand plus Slashing Flourish is 3–4 hits a turn at 2 turns each, so she reaches the +10 cap inside one round. ⚠ Damage taken strips 2 turns of Acuity, which is why her defensive gear matters more than it looks.'
    - id: dual-hand-crossbows
      item: Ne'er Misser + Hellfire Hand Crossbow
      wiki:
      - Ne'er Misser
      - Hellfire Hand Crossbow
      slot: ranged weapons
      note: 'Roah at Moonrise plus Yurgir''s corpse in the Gauntlet of Shar. Both Light, so no Dual Wielder feat. Main-hand, off-hand and Flourish hits stack Acuity fast. ⚠ Both are contested on paper and both stay with her: Charles would like Ne''er Misser''s Magic Missile for shooting out of his own Darkness, and Asterion could use the Hellfire, but neither converts hand-crossbow hits into spell save DC. ⚠ Breaking Yurgir''s contract via Raphael forfeits the Hellfire Hand Crossbow.'
    - id: act2-melee-bonbon
      item: Club of Hill Giant Strength + Knife of the Undermountain King (held over)
      slot: weapons
      note: 'The melee set stays equipped even though she fights from the ranged set, because the Knife''s crit-threshold reduction is global and applies to her bolts and spell attacks. ⚠ THE ADAMANTINE SHIELD IS NOT PART OF THIS PLAN. It was previously slotted here on the theory that an inactive melee-set shield still grants crit immunity, which the wiki confirms only for the AC bonus. That gamble is unnecessary: both Mithral ores now go to Adamantine Splint Armour for her and Adamantine Scale Mail for Charles, and the Splint gives her the same crit immunity outright while she keeps the Knife.'
    - id: act2-chest-bonbon
      item: Adamantine Splint Armour (held over)
      slot: armour
      note: AC 18, crit immunity and −2 to every incoming damage instance carry her through Act 2 unchanged. Crit immunity does double duty here — it protects Hold Monster concentration and it stops Arcane Acuity being stripped two turns at a time by big hits.
    - id: act2-hands-bonbon
      item: Gloves of Dexterity (held over)
      slot: hands
      note: DEX 18 and +1 Attack Rolls remain the best glove effect available to her, and every hit is now an Acuity stack rather than just damage. Nothing in Act 2 beats it.
    - id: spellcrux-amulet
      item: Spellcrux Amulet
      slot: amulets
      note: 'ACT 2 NECK, worn by the Warden in the Moonrise Towers Prison. Replenish an expended spell slot of ANY level as a BONUS ACTION, once per long rest. On a Bard 11 with a single level-6 slot that is literally a second six-target Command or a second Hold Monster, recovered mid-fight without spending her action. It replaces Broodmother''s Revenge, whose poison coating needs a per-turn heal she no longer has time for once the Acuity loop starts.'
    - id: act2-rings-bonbon
      item: Caustic Band + The Whispering Promise (held over)
      slot: rings
      note: 'Both keep working into Act 2 — Caustic Band adds +2 Acid to every bolt, and the Whispering Promise still covers any fight where Charles concentrates on Hex or Darkness instead of Bless. ⚠ The Risky Ring is NOT hers: advantage on attacks would stack Acuity faster, but disadvantage on saving throws lands directly on the Constitution saves protecting Hold Monster, and Charles needs the ring more. The Band of the Mystic Scoundrel takes a slot in Act 3.'
    - id: cloak-of-cunning-brume
      item: Cloak of Cunning Brume
      slot: cloaks
      note: 'Sold by Mattis at Last Light Inn for about 70g. Disengaging also creates a 2m fog cloud for a turn, which obscures and blinds everything inside it — a genuine backline escape button for the moment something closes on her. ⚠ An honest cheap fill: the Act 2 cloak pool is built for melee characters (Fleshmelter and Thunderskin both trigger on being hit), and the one unconditional cloak, Cloak of Protection, goes to Charles, who has permanent disadvantage on saves. She upgrades properly in Act 3.'
    - id: act2-feet-bonbon
      item: Boots of Brilliance
      slot: feet
      note: Heavy chest in the room just north of Yurgir, Gauntlet of Shar. Restores one Bardic Inspiration charge per long rest. Slashing Flourish consumes an Inspiration on every multi-target turn and she is Inspiration-starved rather than AC-starved, so this beats keeping Boots of Speed once the Acuity loop replaces raw repositioning.
    act3:
    - id: band-of-the-mystic-scoundrel
      item: Band of the Mystic Scoundrel
      slot: rings
      note: 'THE ACT 3 ENGINE, in a backpack in the Chult jungle reached through Akabi''s wheel at the Circus — one party member only, so send her. After a weapon hit, Enchantment and Illusion spells become BONUS ACTIONS, so she builds Arcane Acuity with her action and fires Hold Monster or a six-target Command in the same turn. ⚠ Read the wiki caveat before playing it: once Quickening Incantation is active she can no longer cast those spells as an ACTION that turn — only as the bonus action. ⚠ Useful trick: any weapon attack triggers it, even against a world object, so she can prime the loop off a barrel before combat starts.'
    - id: act3-ring2-bonbon
      item: Caustic Band (second slot, held over)
      slot: rings
      note: +2 Acid on every bolt and every Flourish projectile is still the cleanest flat rider available to her, and it needs no setup. Swap it for the Ring of Free Action in any fight with webs, paralysis or Black Tentacles, since being Paralysed both ends Hold Monster and hands out automatic critical hits.
    - id: bow-alternative
      item: Gontr Mael (opening-round alternative)
      wiki: Gontr Mael
      slot: ranged weapons
      note: 'Carried by the Steel Watcher Titan in the Steel Watch Foundry. A legendary +3 longbow with Celestial Haste once per long rest. ⚠ NOT the default, and the reason is structural: it is Two-Handed, so equipping it cancels the dual-hand-crossbow set that is the entire Arcane Acuity engine — she would trade three or four Acuity-stacking hits a turn for two. Carry it purely for an opening-round Celestial Haste, then swap back. ⚠ It does not drop if the Titan is killed by the Atrophied condition.'
    - id: act3-ranged-bonbon
      item: Ne'er Misser + Hellfire Hand Crossbow (held over)
      slot: ranged weapons
      note: 'The standing Act 3 ranged set, unchanged. ⚠ Hellrider''s Longbow is NOT hers — it is Two-Handed, so it cannot coexist with the hand crossbows at all, which settles the initiative contest with Gale in his favour permanently. He has the idle ranged slot; she does not.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health (goes to Charles)
      slot: amulets
      note: 'NOT HERS, on reflection. Setting Constitution to 23 and granting advantage on CON saves is superb, but she already has War Caster''s advantage on those saves, AC 21 in Armour of Agility, and a cloak that gives attackers disadvantage — so the amulet''s advantage half is redundant on her. Charles has a permanent DISADVANTAGE from the Risky Ring for it to cancel, which nothing else in the game does as cleanly. She keeps the Spellcrux Amulet instead, and a free level-6 slot per long rest is worth more to a controller than +6 to saves she is already winning.'
    - id: act3-amulet-bonbon
      item: Spellcrux Amulet (held over)
      slot: amulets
      note: A bonus-action level-6 spell slot once per long rest is a second six-target Command or a second Hold Monster in the fight that needs it. On a Bard 11 with exactly one slot at that level, this is the highest-leverage neck she can wear.
    - id: armour-of-agility
      item: Armour of Agility
      slot: armour
      note: 'ACT 3 CHEST, sold by Gloomy Fentonson at the Stormshore Armoury. Medium armour that adds her FULL Dexterity modifier — AC 17 + 4 = 21 at DEX 18 — plus +2 to ALL saving throws and no Stealth penalty. It beats the Adamantine Splint by 3 AC and 2 saves; the trade is losing crit immunity, so keep the Splint bagged for any fight where she is being focused and Arcane Acuity keeps getting stripped. ⚠ Do not take Medium Armour Master or Magic Initiate: Cleric on her — the wiki notes either feat breaks the full-Dexterity passive.'
    - id: wavemother-s-cloak
      item: Wavemother's Cloak
      slot: cloaks
      note: 'ACT 3 CLOAK, in an opulent chest behind Allandra Grey''s desk on the upper floor of the Water Queen''s House. Once per turn in combat it grants Water Layer Protection until she takes damage: +2 AC, +2 to saving throws, Fire resistance and immunity to Burning. On a backline controller who is rarely hit, that refreshes every turn and effectively never falls off — strictly better than the flat +1/+1 of a Cloak of Protection for her, and it leaves Cloak of Displacement free for Asterion, who has no armour at all.'
    - id: act3-hands-bonbon
      item: Gloves of Dexterity (held over)
      slot: hands
      note: 'Nothing in Act 3 beats DEX 18 plus +1 to every attack roll for her. ⚠ Bracers of Defence are dead once she wears Armour of Agility, and Craterflesh Gloves want a crit-focused build she is not — she is a controller whose damage comes from volume, not critical hits.'
    - id: act3-head-bonbon
      item: Helmet of Arcane Acuity (held over)
      slot: head
      note: 'It stays, and it is not close. Three or four weapon hits a turn take her to the +10 Arcane Acuity cap inside one round, which is +10 to spell save DC. ⚠ BIRTHRIGHT IS REJECTED FOR EXACTLY THIS REASON: +2 Charisma is +1 spell save DC. Ten against one. Keep Birthright bagged as an out-of-combat swap for Persuasion, Deception and Intimidation, where the wiki notes it stacks with the Mirror of Loss for Charisma 24.'
    - id: act3-feet-bonbon
      item: Boots of Persistence
      slot: feet
      note: 'Sold by Dammon at the Forge of the Nine in the Lower City. Permanent Freedom of Movement and Longstrider — Freedom of Movement makes a Ring of Free Action unnecessary and frees her second ring slot for Caustic Band. Medium armour proficiency is required and Fighter 1 supplies it. ⚠ Helldusk Boots are the better item in the abstract but go to Charles, who has save disadvantage to undo; Gale cannot wear Persistence at all, so this is the allocation that leaves nobody stranded.'
    progression:
    - id: prog-head
      item: 'Head: Grymskull Helm → Diadem of Arcane Synergy → Helmet of Arcane Acuity'
      slot: head
      note: Free Grymskull crit immunity as a stopgap → Diadem (Crèche) for CHA on ranged hits → Helmet of Arcane Acuity (Mason's Guild, Act 2) for the rest of the run. The Helmet never comes off again — Birthright's +2 Charisma is +1 spell DC against Acuity's +10.
    - id: prog-armour
      item: 'Chest: The Protecty Sparkswall → Adamantine Splint Armour → Armour of Agility'
      slot: armour
      note: Act 1 early Protecty (Grymforge) for +1 spell DC → Act 1 late and Act 2 Adamantine Splint (first Mithral ore) for AC 18 and crit immunity → Act 3 Armour of Agility (Stormshore Armoury) for AC 21 and +2 saves. Keep the Splint bagged for fights where crit immunity beats raw AC.
    - id: prog-hands
      item: 'Hands: Gloves of Archery → Gloves of Dexterity'
      slot: hands
      note: Act 1 early Archery gloves (Grat) → Gloves of Dexterity from the Crèche for the rest of the run. Nothing later beats DEX 18 plus +1 to every attack roll on a character making four attack rolls a turn.
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
    - id: prog-rings
      item: 'Rings: Whispering Promise + Caustic Band → Band of the Mystic Scoundrel + Caustic Band'
      slot: rings
      note: Whispering Promise covers levels 1–3 before Charles has Bless and stays useful in any fight he concentrates elsewhere; Caustic Band runs all game. The Band of the Mystic Scoundrel (Chult jungle, via Akabi's wheel) takes the first slot in Act 3 and turns her control spells into bonus actions.
    - id: prog-weapons
      item: 'Melee: Club of Hill Giant Strength + Knife of the Undermountain King, all game'
      slot: weapons
      note: A stat-stick set she never actually swings. The Club supplies STR 19 for the Titanstring rider in Act 1, and the Knife's crit-threshold reduction is global — it improves her bolts and spell attacks, which is why it keeps the slot after Titanstring is retired.
    - id: prog-ranged
      item: 'Ranged: Titanstring Bow → Ne''er Misser + Hellfire Hand Crossbow'
      slot: ranged weapons
      note: THE BUILD'S PIVOT. Titanstring's single big STR-scaled shots carry Act 1; from the Helmet of Arcane Acuity in Act 2 she switches to dual hand crossbows permanently, because three or four smaller hits stack Acuity to its cap far faster than one large one. Gontr Mael is an opening-round swap only, never the default.
    - id: prog-consumables
      item: 'Elixir: Bloodlust (default) / Hill Giant Strength (boss fights)'
      slot: consumables
      note: Bloodlust whenever the fight has adds she can kill for the extra Action; Hill Giant Strength for a lone boss where no kill is coming. Stock both heavily — Asterion drinks a Giant Strength every single day.
  playstyle: |-
    - **Act 1 default:** equip Titanstring plus the Hill Giant club main hand and Knife of the Undermountain King off-hand, drink Bloodlust, and use Protecty Sparkswall to raise Hold Person/control DC. Use ranged Slashing Flourish for nova damage and trigger Broodmother's Revenge with healing before a multi-projectile turn.
    - **Act 1 alternatives:** use a Hill Giant elixir for a boss with no Bloodlust target; use Adamantine Splint for defence.
    - **Act 2+:** switch to dual hand crossbows and Flourish to stack Arcane Acuity. In Act 3, spend it on a same-turn bonus-action Hold Monster or Command.
    - **Protect concentration:** stay at range. Against undead, use Hypnotic Pattern or Slow instead of Hold Monster/Command.
    - **Carry the party's Daylight:** Gale casts Daylight (Enchant Item) on Bonbon's main-hand weapon once per long rest — it is bugged to last until the next rest and travels with her, keeping Gale lit for his Coruscation → Callous Glow chain. She is the carrier because the spell requires a main-hand weapon, which rules out Asterion's empty Tavern Brawler hands, and because her mid-range position keeps the 15m radius over the fight. ⚠ Do not swap her main-hand weapon afterwards, and let Gale cast it *before* any Darkness Arrow goes out.
    - **Division of control with Gale:** Bonbon owns the *Concentration* lane (Hold Person/Hold Monster — the auto-crit setup for Charles); Gale owns the *non-concentration* lane (Extended Command). They stack rather than compete, so do not both spend a turn on the same target. Bonbon also keeps Hellrider's Longbow by default, since she needs to land the first weapon hit to open the Band loop.
---
