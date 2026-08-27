---
nickname: Asterion
builds:
- name: The Fist in the Dark
  is_primary: true
  role: Mobile Open-Hand monk — stun-lock striker, psychic flurry, party thief
  class: Open Hand Monk 9 / Thief Rogue 3
  build_order: Rogue 1 (creation, Expertise) → Monk 1–9 → Rogue 2 → Thief 3. No respec after the initial rebuild.
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: 'Fey Ancestry (advantage vs Charm, no magical Sleep), Darkvision, one High Elf wizard cantrip, bonus-action Vampire Bite. ⚠ Must stay unarmoured and shieldless; after Tavern Brawler both melee hands stay empty so Attack/Extra Attack are unarmed. Graceful Cloth is Clothing, not armour, and Bracers of Defence work unarmoured and shieldless.'
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background, unchangeable even by respec.
  starting_stats:
    STR: 8
    DEX: 17
    CON: 15
    INT: 8
    WIS: 16
    CHA: 8
  stats_note: 'Point-buy 8/15/15/8/15/8 = all 27 (DEX, CON and WIS all at 15 cost 9 each). EVERY +1 THIS BUILD RECEIVES LANDS ON AN ODD SCORE, which is the whole reason the array looks like this: 14 and 15 are both +2, so a +1 spent onto an even score buys nothing at all. INT is dumped to 8 because nothing in the build touches it, and the 2 points that frees are exactly the cost of CON 14 → 15 — which is what turns Tavern Brawler''s +1 into CON 16 and a real +3 instead of a wasted point. Racial +2 → DEX 17 and +1 → WIS 16, Hag''s Hair → DEX 18, Tavern Brawler → CON 16.'
  ability_targets: 'MODDED Hair: DEX 17 → 18 → 20 via Graceful Cloth (its +2 caps at 20). Mirror of Loss goes to WIS 16 → 18. Tavern Brawler''s +1 goes to CON 15 → 16 for +3, never to STR. STR stays 8 because the elixir overrides it.'
  ability_scores:
  - ability: STR
    steps:
    - score: 8
      source: 'point-buy'
    - score: 21
      source: 'Elixir'
  - ability: DEX
    steps:
    - score: 15
      source: 'point-buy'
    - score: 17
      source: '+2 Racial'
    - score: 18
      source: '+1 Hag''s Hair'
    - score: 20
      source: '+2 The Graceful Cloth'
  - ability: CON
    steps:
    - score: 15
      source: 'point-buy'
    - score: 16
      source: '+1 Tavern Brawler, Monk 4'
  - ability: INT
    steps:
    - score: 8
      source: 'point-buy'
  - ability: WIS
    steps:
    - score: 15
      source: 'point-buy'
    - score: 16
      source: '+1 Racial'
    - score: 18
      source: '+2 Mirror of Loss, Act 3'
  - ability: CHA
    steps:
    - score: 8
      source: 'point-buy'
  feats:
  - at: Monk 4 (char 5)
    feat: Tavern Brawler
    note: 'The engine, and one of only TWO S+ feats in the tier list (Alert is the other — Asterion takes both, and nobody else in the party takes either). TWO separate effects, and the second one is easy to miss: it adds your STR modifier to unarmed attack rolls AND damage a second time, AND it raises Strength or Constitution by 1 (base cap 20). Take the CON option — STR is overridden by the Giant Strength elixir anyway — and note this is why CON is bought at an ODD 15, so the +1 reaches 16 and a full +3 instead of being swallowed by the 14/15 tier. Drink Giant Strength each long rest and UNEQUIP Corellon''s Grace so main-action attacks are empty-hand punches. Once STR > DEX it also drives attack rolls and the Stun DC (BG3 monk DCs use the higher of DEX/STR). Cloud Giant (STR 27, +8) is the ceiling. ⚠ SCOPE: the feat also covers Throw and Improvised Melee Weapon attacks, neither of which requires empty hands — only the base Unarmed Strike action needs "no melee weapons equipped." Asterion punches, so the hands-empty rule binds him exactly as written, but it never blocks a thrown consumable.'
  - at: Monk 8 (char 9)
    feat: Alert
    note: '+5 Initiative and immunity to Surprise — with DEX 20 that is a near-guaranteed first turn to open-strike and Stun the priority target before it acts. (Alternative: +2 WIS for more AC and rider damage.)'
  key_abilities:
  - Flurry of Blows — Open Hand variants Topple (Prone) / Stagger (no Reactions) / Push
  - Stunning Strike — the party's on-demand hard control
  - Manifestation of Mind — +psychic per unarmed hit, DOUBLED by the Resonance Stone
  - Ki Resonation (Punch → Blast) — AoE finisher
  - Step of the Wind / Patient Defense / Deflect Missiles — mobility + defense
  - Fast Hands (Thief) → two Flurries of Blows per turn
  combat_style: 'Char 2–4 — Corellon''s Grace improves Flurry punches and saves and gives a stronger pre-feat main attack. Char 5 — Tavern Brawler takes over: unequip every melee weapon, stay unarmoured and shieldless, drink a daily Giant Strength elixir, punch.'
  creation:
    level1_class: Rogue 1 (taken at character creation / first class in the respec)
    level1_gains: '4 Rogue skill proficiencies (Stealth, Investigation, Acrobatics, Insight) + Expertise in 2 of them (Sleight of Hand + Stealth) + Sneak Attack 1d6 (vestigial once he punches — it needs a finesse weapon, not fists). MUST be the creation class so Expertise lands on the thief skills.'
    subclass_choice: Open Hand (Monk 3) · Thief (Rogue 3)
    proficiencies:
      armor_weapons: Unarmed and unarmoured — required for Martial Arts / Flurry / Unarmoured Defence.
      saving_throws: DEX + INT (Rogue).
      skills: 'Charlatan (Deception, Sleight of Hand) + Elf Keen Senses (Perception) + 4 Rogue picks (Stealth, Investigation, Acrobatics, Insight). Expertise: Sleight of Hand + Stealth (Rogue 1). Only Rogue 3, so no second Expertise pair and no Reliable Talent.'
    starting_cantrips: 'One High Elf racial cantrip, but it is NOT selectable on a recruited companion — race-related choices are fixed and the respec does not re-present them. Read it off the save; nothing in the build depends on it.'
    starting_spells: None — Ki/martial build.
    notes: '2 feats (Monk 4 + Monk 8). Rogue 1 FIRST for Expertise, then Monk 1–9, then Thief. Daily Giant Strength elixir; DEX stays for pickpocketing.'
  spells:
    note: Not a caster. His build-defining Ki abilities and martial features appear at their unlock levels in the Leveling guide; this panel tracks the one High Elf racial cantrip.
    mandatory:
    - spell: Flurry of Blows (+ Open Hand variants)
      level: Feature (Monk 1; Open Hand variants Monk 3)
      school: Ki — Bludgeoning + rider
      save: 'Topple: DEX · Push: STR · Stagger: none (weapon-action DC)'
      when: char 2 (Monk 1) / char 4 (Monk 3)
      why: 'Bonus action + 1 Ki → two unarmed strikes. Open Hand adds Topple (Prone → allies attack at advantage), Stagger (no Reactions) and Push (5m + fall damage). With Fast Hands or Wholeness of Body, Flurry TWICE per turn.'
    - spell: Stunning Strike
      level: Feature (Monk 5)
      school: Ki — control
      save: CON save (DC 8 + prof + higher of DEX/STR)
      when: char 6 (Monk 5)
      why: 'The party contribution — 1 Ki on a hit, CON save or Stunned (auto-fails STR/DEX saves, attacked at advantage, loses its turn). Locks bosses and hands Charles free crits. The DC rides the elixir''s STR, up to +8.'
    - spell: Manifestation of Mind
      level: Feature (Open Hand, Monk 6)
      school: Toggle — Psychic
      save: None
      when: char 7 (Monk 6)
      why: Every unarmed strike deals +1d4 + WIS PSYCHIC. At 4–6 hits a turn, ALL of it doubles under the Resonance Stone — how the Monk joins the psychic engine without a Shadow Blade. Toggle to Soul/Body for radiant/necrotic vs psychic-resistant foes.
    - spell: Extra Attack
      level: Feature (Monk 5)
      school: N/A
      save: None
      when: char 6 (Monk 5)
      why: With both melee hands empty, the Action supplies two unarmed strikes; the Martial-Arts bonus strike and Flurry stack on top.
    - spell: 'Tavern Brawler + Giant Strength elixir'
      level: Feat (Monk 4) + consumable
      school: N/A
      save: None
      when: char 5
      why: Daily Elixir of Giant Strength. TB adds that STR mod to every unarmed attack AND damage a second time, and once STR > DEX it drives attack rolls and the Stun DC. The accuracy and damage backbone.
    recommended:
    - spell: Minor Illusion
      source: granted
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (35:56) — moves NPCs with no save or roll; clusters enemies for AoE, sets ambushes, pulls enemies one at a time'
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: char 1 (High Elf racial cantrip — fixed, not selectable)
      why: 'Would be the ideal pick — S tier for pulling creatures toward a distraction with no save, redirecting sightlines for stealth and theft without touching his low INT — but a recruited companion''s racial cantrip is locked at creation and the respec does not re-present it. Listed here as the thing to hope for, not a pick to make; check the save for what he actually has.'
    - spell: Ki Resonation (Punch → Blast)
      level: Feature (Open Hand, Monk 9)
      school: Ki — detonate
      save: CON save
      when: char 10 (Monk 9)
      why: Punch to mark a target Resonating, then Blast to detonate an AoE around it (party and summons excluded) — a nova finisher on clustered packs.
    - spell: Step of the Wind
      level: Feature (Monk 2)
      school: Ki — mobility
      save: None
      when: char 3 (Monk 2)
      why: Bonus-action Dash/Disengage (jumping is free) — dive the backline, reposition, leave melee without opportunity attacks.
    - spell: Patient Defense
      level: Feature (Monk 2)
      school: Ki — defense
      save: None
      when: char 3 (Monk 2)
      why: Bonus action + Ki → attackers have Disadvantage and he has advantage on DEX saves. The survival button for a no-armour body.
    - spell: Deflect Missiles
      level: Feature (Monk 3)
      school: Reaction
      save: None
      when: char 4 (Monk 3)
      why: Reduce a ranged attack by 1d10 + DEX + monk level (often to 0) and optionally hurl it back — a hard counter to archers.
    - spell: Wholeness of Body
      level: Feature (Open Hand, Monk 6)
      school: Ki — heal + economy
      save: None
      when: char 7 (Monk 6)
      why: 'Action: heal 3× monk level, refund half his Ki, and gain an EXTRA bonus action for 3 turns — two Flurries per turn even before the Thief dip. Once per long rest.'
    - spell: Fast Hands (Thief)
      level: Feature (Thief, Rogue 3)
      school: N/A
      save: None
      when: char 12 (Thief 3)
      why: A permanent second bonus action → Flurry of Blows TWICE per turn (2 Ki, 4 extra strikes) on top of the Attack action; also fuels Cunning Action utility.
    - spell: Vampire Bite
      level: Racial (Vampire Spawn)
      school: Bonus action — Necrotic + heal
      save: None
      when: char 1
      why: A free bonus-action heal/buff on a grappled or downed foe, mostly out of combat — minor in the flurry economy, but it costs nothing.
  leveling:
  - char_level: 1
    class: Rogue 1
    gains:
    - Sneak Attack 1d6
    - Four Rogue skill proficiencies
    - Expertise selections ×2
    - DEX + INT saving-throw proficiency
    - Vampire Bite (Astarion origin action)
    recommendations:
    - category: Skills
      picks: 4
      recommendation:
      - Stealth
      - Investigation
      - Acrobatics
      - Insight
      note: 'SIX picks land on this level, not two — Rogue grants 4 skill proficiencies BEFORE the 2 Expertise picks, and it is easy to click past them. Stealth is mandatory rather than optional: Charlatan supplies Sleight of Hand and Elf Keen Senses supplies Perception, but nothing grants Stealth, so without picking it here the Expertise: Stealth choice below has no valid target. Investigation is the party''s only coverage — Charles, Gale and Bonbon all lack it. Acrobatics rides DEX 17→20 and Insight rides WIS 16→18. ALTERNATIVE worth considering: swap Insight (already covered by Gale and Bonbon) for Athletics — on the daily Giant Strength elixir Asterion hits STR 27, making him the party''s only viable shove/grapple carrier; update proficiencies.md to match if you take it.'
    - category: Expertise
      picks: 2
      recommendation:
      - Sleight of Hand
      - Stealth
      note: The reason Rogue must be the first class; these power stealing and scouting for the whole run.
    - category: Racial cantrip
      wiki: false
      granted: true
      fixed: true
      recommendation: Whatever Larian assigned him (one High Elf wizard cantrip)
      note: '⚠ NOT a selection, and not a grant you get to steer. Astarion is a recruited companion, and the wiki is explicit that race-related choices carry over unchanged: "the selectable aspects of any given race, such as a high elf''s choice of cantrip, also remain fixed" (Withers, Services). The Withers respec will not re-present it, so he keeps whatever Larian assigned. Check the cantrip on the save rather than planning around it. If it turns out to be Bone Chill that is a fine outcome — A tier, "targets AC at range, prevents healing, and gives undead disadvantage on attacks" — and nothing in this build depends on the cantrip either way.'
  - char_level: 2
    class: Monk 1
    gains:
    - Unarmoured Defence
    - Martial Arts (DEX-based unarmed attacks and a bonus unarmed strike)
    - Flurry of Blows
    - Martial Arts die 1d4
  - char_level: 3
    class: Monk 2
    gains:
    - Unarmoured Movement
    - Patient Defence
    - Step of the Wind (Dash and Disengage)
  - char_level: 4
    class: Monk 3
    gains:
    - Deflect Missiles
    - Martial Arts die 1d6
    recommendations:
    - category: Subclass
      picks: 1
      recommendation: Way of the Open Hand
      note: Adds Topple, Stagger and Push variants to Flurry of Blows.
  - char_level: 5
    class: Monk 4
    gains:
    - Slow Fall
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Tavern Brawler
      note: Adds the Giant-Strength modifier to unarmed attack and damage rolls a second time — the build's accuracy and damage engine.
  - char_level: 6
    class: Monk 5
    gains:
    - Extra Attack
    - Stunning Strike (Melee and Unarmed)
  - char_level: 7
    class: Monk 6
    gains:
    - Manifestation of Body, Mind, and Soul
    - Wholeness of Body
    - Ki-Empowered Strikes
  - char_level: 8
    class: Monk 7
    gains:
    - Evasion
    - Stillness of Mind
  - char_level: 9
    class: Monk 8
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Alert
      note: +5 Initiative and immunity to Surprise let him disable a priority target before it acts. A +2 WIS ASI is the defensive alternative.
  - char_level: 10
    class: Monk 9
    gains:
    - Advanced Unarmoured Movement
    - Ki Resonation attacks and Blast
    - Martial Arts die 1d8
  - char_level: 11
    class: Rogue 2
    gains:
    - Cunning Action (Dash, Disengage, and Hide)
  - char_level: 12
    class: Rogue 3 (Thief)
    gains:
    - Fast Hands (permanent second bonus action)
    - Second-Story Work
    recommendations:
    - category: Subclass
      picks: 1
      recommendation: Thief
      note: Fast Hands enables two Flurries per turn — the whole reason for the three-level Rogue tail.
  itemization:
    act1:
    - id: staff-of-arcane-blessing
      item: Staff of Arcane Blessing
      tier: A
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (24:19) — incredible for a party making frequent spell attack rolls, and does less than the tooltip implies'
      slot: weapons
      note: 'HIS JOB, NOT A WEAPON — and the party''s entire Bless supply. Arcane Tower BASEMENT in the Underdark; the elevator buttons only appear if someone carries Bernard''s Guiding Light ring. The staff GRANTS Bless as a level 1 spell, once per long rest, so Asterion needs no Paladin dip and no class access to cast it — this is why he stays a clean Open Hand Monk 9 / Thief Rogue 3. Every Bless its wielder casts also applies MYSTRA''S BLESSING, a second +1d4 that lands only on SPELL attack rolls, which is worth +1d4 accuracy on each of Gale''s 3–7 Scorching Ray rays. THE ROUTINE: equip the staff out of combat → cast Bless → unequip and fight with empty hands. Concentration then sits on Asterion, who is the only party member with nothing else to concentrate on. ⚠ LIMITS TO PLAN AROUND: the staff''s free cast is ONCE PER LONG REST, and Bless at level 1 hits only THREE creatures — pick Charles, Gale and Bonbon and leave Asterion out, since he benefits least from +1d4 and the other three all key off attack rolls. ⚠ Do NOT let Gale consume it; the wiki flags it as Consumable by Gale. ⚠ Losing concentration drops the regular Bless but the wiki notes Mystra''s Blessing persists on its own, so Gale keeps his spell-attack bonus even if Asterion is hit.'
    - id: corellon-s-grace
      item: Corellon's Grace
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (10:19) — great for a Tavern Brawler Monk defensively and offensively, but early-game only'
      slot: weapons
      note: 'EARLY ONLY, from Auntie Ethel. Before Tavern Brawler the staff attack is a solid main Action, Natural Pugilist improves bonus-action and Flurry punches, and unarmoured gives +2 saves. ⚠ UNEQUIP at char 5 — Attack/Extra Attack otherwise swing the staff and lose Tavern Brawler, even though Flurry still works. The staves tier list rates it S and says in the same breath that Tavern Brawler monks replace it, so retiring it is the intended arc, not a downgrade.'
    - id: dual-hand-crossbows-plus-one
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      slot: ranged weapons
      note: A PAIR, one in each hand, from Act-1 weapon traders. Rogue proficiency gives a main-hand shot plus a bonus-action off-hand shot when melee is out of reach. The ranged set does not touch the melee hands, so Tavern Brawler stays live.
    - id: graceful-cloth
      item: Graceful Cloth
      tier: S
      tier_note: 'TwFGCc8OOfw (10:24) — +2 Dexterity is the strongest effect on the list; initiative, AC and damage in one'
      rank: '#3'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #3 of 20 — +2 Dexterity and advantage on Dexterity checks; acts like a free feat'
      wiki: The Graceful Cloth
      slot: armour
      bis: true
      note: 'Lady Esther, Rosymorn trail. Clothing, not armour, so Unarmoured Defence still works — worn all game. Cat''s Grace carries DEX to 20 early; once DEX is capped the reason to keep it is ADVANTAGE ON DEXTERITY CHECKS, which is advantage on every Sleight of Hand roll he makes as party thief.'
    - id: circlet-of-psionic-revenge
      item: Circlet of Psionic Revenge
      tier: B
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (13:02) — a small amount of damage that is not always triggered, but it will see play in some compositions'
      slot: head
      note: 'THE ONLY LEGAL HEAD HE HAS IN ACT 1. Carried by Githyanki Inquisitor Ch''r''ai W''wargaz in the Crèche Inquisitor''s Chamber. Succeed a saving throw and the foe that forced it takes 1d4 Psychic. ⚠ THE CONSTRAINT THAT PICKS THIS: per the wiki, "Helmets and Gloves marked as Light, Medium or Heavy Armour count as armour, and prevent Unarmoured Defence from working" — which permanently rules out Covert Cowl (Light) and the Dark Justiciar Helmet (Medium). This circlet carries no proficiency requirement, so it is legal. The +1 mental saves printed on it are Githyanki-only and he does not get them; take it for the retaliation, which the Resonance Stone doubles from Act 2.'
    - id: act1-hands-asterion
      item: Glove slot
      slot: hands
      wiki: false
      note: 'GENUINELY OPEN ALL OF ACT 1 — there is no best-in-slot here until the Gloves of Soul Catching in Act 3, so pick per fight. Bracers are the default; swap to an offensive pair when a fight is short enough that AC matters less than damage.'
      options:
      - id: bracers-of-defence
        item: Bracers of Defence
        tier: S
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (10:30) — for a wide array of characters, though often discarded for a later upgrade'
        note: 'DEFAULT. Blighted Village cellar. +2 AC while unarmoured and shieldless, which with DEX 20 and WIS 18 is AC 21 — the highest no-armour AC in the party.'
      - id: the-sparkle-hands
        item: The Sparkle Hands
        tier: A
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (43:19) — a solid alternative to an S-tier item, with real usage of its own'
        note: 'Decrepit Sanctuary, Sunlit Wetlands. 2 Lightning Charges per unarmed hit; charges add attack and damage, burst for 1d8 Lightning, and grant advantage against metal-armoured enemies. Best when he is landing 4-6 hits a turn.'
      - id: gloves-of-cinder-and-sizzle
        item: Gloves of Cinder and Sizzle
        tier: S
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (21:57) — an S-tier pick for just about every monk, because damage is the class''s job'
        note: 'Lady Esther, late Act 1. +1d4 Fire per unarmed hit, so a Flurry turn applies it repeatedly, plus a level-3 Scorching Ray once per long rest. Prefer Sparkle Hands against metal or fire resistance.'
      - id: gloves-of-thievery
        item: Gloves of Thievery
        tier: B
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (33:57) — functionally equivalent to the Gloves of Power for the same job'
        note: 'Brem, Zhentarim. Advantage on Sleight of Hand — and unlike Guidance this actually shows up in the pickpocket window. Keep them bagged and swap in only to steal, since the slot is worth more as AC or damage in a fight.'
    - id: elixir-of-giant-strength
      item: Elixir of Hill Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (30:26) — sets Strength to 21; S used normally, and S+ ABOVE THE SCALE if drunk daily to skip strength investment'
      slot: consumables
      note: Hill Giant (STR 21) early → Cloud Giant (STR 27) later. Powers Tavern Brawler damage and, since STR > DEX, his attack rolls and Stunning-Strike DC. Occupies the one-elixir-per-rest slot.
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (6:44) — DARK URGE ORIGIN ONLY; free invisibility on a kill, broken, and the only act one magic cloak'
      rank: '#4'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #4 of 20 — invisibility after a kill, in a slot with no early competition'
      wiki: The Deathstalker Mantle
      slot: cloaks
      bis: true
      note: 'Dark Urge reward, handed over by Charles. Invisible for 2 turns on a kill — reposition and re-engage, perfect for a diving monk. ⚠ It is the ONLY magical cloak obtainable in Act 1 by anyone; every other cloak in the game is Act 2 or later, which is why three of the four cloak slots below stay empty until Act 2.'
    - id: disintegrating-night-walkers
      item: Disintegrating Night Walkers
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (19:19) — probably the best boots in the game'
      rank: '#11'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #11 of 20 — short-rest Misty Step plus immunity to most movement-restricting surfaces'
      slot: feet
      bis: true
      note: Nere, Grymforge. Free Misty Step once per short rest plus immunity to difficult terrain from surfaces, Enwebbed and Entangled — the permanent combat boots. ⚠ They do NOT cover Paralysed or Restrained; the Ring of Free Action closes that in Act 3.
    - id: bracing-band
      item: Bracing Band
      tier: A
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (6:13) — good for a lot of characters, though there are often better options'
      slot: ring 1
      note: 'FREE PERMANENT +1 AC, and almost nobody takes it. Sergeant Thrinn''s reward for Find the Missing Boots at Grymforge. "After shoving an enemy, the wearer gains a +1 to their Armour Class until their next turn" — and per the wiki the trigger "is not just Shove", with FLURRY OF BLOWS: PUSH named explicitly on the list. Asterion already throws Push as one of his three Open Hand Flurry variants, so on any turn he pushes something the bonus is simply always up, on the character with no armour to fall back on. ⚠ Thrinn gives ONE of two rewards — take this over Armour of Uninhibited Kushigo, since Graceful Cloth is the standing chest anyway. ⚠ The Ring of Protection goes to Gale, who is the party''s lowest-AC body; Asterion is already at AC 21.'
    - id: act1-ring2-asterion
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'OPEN. He wants movement above all else in Act 1 — he has the longest distance to cover and the most attacks to land once he arrives.'
      options:
      - id: crusher-s-ring
        item: Crusher's Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (9:50) — movement speed is universally applicable; an extremely rare party leaves it on the table'
        note: 'DEFAULT. Take it from Crusher at the Goblin Camp for +3m movement; it stacks with Longstrider and reaches the priority target without spending a bonus action.'
      - id: opt-ring-of-protection-ast
        item: Ring of Protection
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (34:55) — raises the party''s average AC; give it to the easiest-to-hit member'
        rank: '#20'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #20 of 20 — +1 AC and all saves fits almost anyone, for the whole game'
        note: "+1 AC and +1 to all saving throws. Currently Gale's, but it is the generically strongest defensive ring in Act 1 if Gale can spare it."
      - id: opt-smugglers-ring
        item: Smuggler's Ring
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (40:05) — +2 Sleight of Hand is great, but it is a fully out-of-combat item'
        note: '+2 Sleight of Hand. He is the party thief, and unlike Guidance this is a FLAT bonus, so it actually shows up in the pickpocket window\u2019s roll-needed number.'
    - id: sentient-amulet
      item: Sentient Amulet
      tier: A
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (43:06) — mainly for its use on a monk, but worth having in the arsenal'
      slot: amulets
      note: Grymforge, Adamantine chest. Ki Restoration (2 Ki, 1/long rest) plus Shatter — a cheap early neck that refuels Flurries. Mind the WIS-save Hysterical side effect on the rare version.
    - id: armour-of-uninhibited-kushigo
      item: Armour of Uninhibited Kushigo
      tier: C
      tier_note: 'TwFGCc8OOfw (5:09) — monk-only; Kushigo Counter needs Patient Defense, the weakest monk bonus action'
      slot: armour
      note: Grymforge, for returning Sergeant Thrinn's boots. During Patient Defence, Kushigo Counter gives a reaction unarmed strike when an attacker misses. Graceful Cloth stays default — use this only for a counter fight.
    act2:
    - id: resonance-stone
      item: Resonance Stone
      slot: other
      note: 'Mind Flayer Colony, late Act 2. He places and carries it: Manifestation of Mind psychic, Psionic Overload and his Circlet''s retaliation are all doubled across 4–6 hits a turn. It also gives enemies disadvantage on mental saving throws, and Command and both Hold spells are WIS saves — so anything standing near Asterion is close to unable to resist Gale''s control. ⚠ IT DOES NOT HELP STUNNING STRIKE: per the wiki the aura''s penalty covers Intelligence, Wisdom and Charisma saves, and Stunning Strike is a CONSTITUTION save. ⚠ The aura also makes the party — and him — psychic-vulnerable and disadvantaged on mental saves; the Amulet of the Harpers below is the counter. Holster it against psychic or mind-affecting enemies, and expect it to stop working once Act 2 ends.'
    - id: amulet-of-the-harpers
      item: Amulet of the Harpers
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (25:47) — such a powerful effect for such a relatively small cost'
      slot: amulets
      note: 'Quartermaster Talli, Last Light Inn. ADVANTAGE ON WISDOM SAVING THROWS, plus Shield 1/long rest. It replaces the Sentient Amulet because it is the direct answer to the Stone he is carrying: the aura hands the whole party disadvantage on mental saves, and advantage cancels that back to a straight roll for the member standing closest to it. It is also the Act 2 answer to Hold Person, Fear and Dominate.'
    - id: flawed-helldusk-gloves
      item: Flawed Helldusk Gloves
      tier: S
      tier_note: 'The BEST GLOVES In Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (11:57) — increasing weapon damage is simply that powerful'
      slot: hands
      note: 'Crafted by Dammon at Last Light Inn once he has been given the THIRD piece of Infernal Iron. Unarmed attacks deal an extra 1d4 Necrotic and can inflict Bleeding, plus +1 STR saves. No armour tag, so Unarmoured Defence survives. Across five strikes a turn that is roughly +12 damage against the +2 AC the Bracers were giving — take the damage while Act 2 enemies are still soft. ⚠ Budget the Infernal Iron deliberately; the same pieces upgrade Karlach''s engine.'
    - id: shadow-cloaked-ring
      item: Shadow-Cloaked Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (38:32) — bonus damage is always among the best things an item can give, and this is no exception'
      slot: ring 1
      note: 'THE ACT 2 DAMAGE RING. Carried by the Shadow Mastiff Alpha at the Ruined Battlefield — destroy the everburning torches nearby to make it appear. +1d4 against Lightly or Heavily Obscured creatures and creatures made of shadow, and the wiki names weapon AND UNARMED attacks explicitly, which most riders do not. Nearly everything in the Shadow-Cursed Lands qualifies, so it is roughly +12 across a full Flurry turn.'
    - id: eversight-ring
      item: Eversight Ring
      tier: A
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (9:55) — mandatory with a Warlock or a Darkness plan; depends heavily on party composition'
      wiki: Eversight Ring
      slot: ring 2
      note: 'House of Healing morgue. The wearer cannot be Blinded — and per the wiki that blind immunity "also allows the wearer to see through magical darkness." This is what lets Asterion fight beside Charles inside a Darkness cloud at all; without it he is simply blind in there. It takes the second ring slot from Act 2, displacing Crusher''s Ring.'
    - id: act2-armour-asterion
      item: Graceful Cloth
      tier: S
      tier_note: 'TwFGCc8OOfw (10:24) — +2 Dexterity is the strongest effect on the list; initiative, AC and damage in one'
      rank: '#3'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #3 of 20 — +2 Dexterity and advantage on Dexterity checks; acts like a free feat'
      held: 1
      wiki: The Graceful Cloth
      slot: armour
      bis: true
      note: 'CARRIED OVER, and worn all game. Clothing rather than armour, so Unarmoured Defence still applies, and it gives +2 Dexterity plus advantage on all Dexterity ability checks — which doubles as his pickpocket bonus.'
    - id: act2-head-asterion
      item: Circlet of Psionic Revenge
      tier: B
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (13:02) — a small amount of damage that is not always triggered, but it will see play in some compositions'
      held: 1
      slot: head
      note: 'CARRIED OVER. No armour tag, so Unarmoured Defence survives it.'
    - id: act2-feet-asterion
      item: Disintegrating Night Walkers
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (19:19) — probably the best boots in the game'
      rank: '#11'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #11 of 20 — short-rest Misty Step plus immunity to most movement-restricting surfaces'
      held: 1
      slot: feet
      bis: true
      note: 'CARRIED OVER. Misty Step once per short rest plus immunity to being knocked Prone and to Web, Entangle and Grease — mobility and safety in one slot.'
    - id: act2-cloak-asterion
      item: Deathstalker Mantle
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (6:44) — DARK URGE ORIGIN ONLY; free invisibility on a kill, broken, and the only act one magic cloak'
      rank: '#4'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #4 of 20 — invisibility after a kill, in a slot with no early competition'
      held: 1
      wiki: The Deathstalker Mantle
      slot: cloaks
      bis: true
      note: 'CARRIED OVER. The Dark Urge cloak: a kill grants Greater Invisibility, which on the party thief is both an escape and a repositioning tool.'
    - id: act2-ranged-asterion
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      held: 1
      slot: ranged weapons
      note: 'CARRIED OVER, still a pair. Rogue proficiency gives a main-hand shot plus a bonus-action off-hand shot for turns melee cannot reach.'
    - id: act2-weapons-asterion
      item: Empty hands
      held: 1
      slot: weapons
      wiki: false
      note: 'CARRIED OVER, and deliberately empty: after Tavern Brawler both melee hands stay free so Attack and Extra Attack resolve as unarmed strikes. The Staff of Arcane Blessing is still carried purely as a pre-combat Bless swap.'
    act3:
    - id: gloves-of-soul-catching
      item: Gloves of Soul Catching
      tier: S
      tier_note: 'The BEST GLOVES In BG3 COMPLETE - Honor Mode Tier List and Guide - Act 3 (22:25) — the numbers on this item are ridiculously high'
      slot: hands
      bis: true
      note: House of Hope, Hope's reward. +1d10 Force per unarmed hit, +2 CON, and once per turn either heal 10 HP or take +5 to an attack or save. Best-in-slot monk gloves and a clear upgrade on the Flawed Helldusk Gloves.
    - id: mask-of-soul-perception
      item: Mask of Soul Perception
      tier: S
      tier_note: 'Is EVERY Act 3 Helmet Awesome? - BG3 Helmets Tier List and Guide - Act 3 (26:03) — a great item that pretty much every party will want to use on someone'
      slot: head
      bis: true
      note: Devil's Fee — locked chest in Helsik's room, DC 20. +2 to Attack rolls, Initiative and Perception, plus Detect Thoughts. The first real head upgrade he gets, and it finally retires the Circlet.
    - id: boots-of-uninhibited-kushigo
      item: Boots of Uninhibited Kushigo
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (55:34) — best in slot for pretty much every monk; a damage item for a damage class'
      slot: feet
      note: Astral Plane — Prelate Lir'i'c, at the start of Act 3. Adds his WIS modifier to every unarmed strike, so flat damage on every one of 5–6 hits. Boots are not on the Monk armour-exclusion list, so an armour tag on late boots is never a problem for him.
    - id: vest-of-soul-rejuvenation
      item: Vest of Soul Rejuvenation
      tier: S
      tier_note: 'TwFGCc8OOfw (54:13) — +2 AC best in slot for monks, but S BY DEFAULT with no real competition'
      slot: armour
      note: 'ACT 3 CHEST, and the piece that finally beats Graceful Cloth. Sold by Rolan at Sorcerous Sundries, or Lorroakan''s Projection if Rolan is dead. +2 Armour Class on an unarmoured build, 1d4 healing on a successful save against a spell, and Greater Kushigo Counter — a REACTION unarmed strike against any attacker that misses, carrying every one of his riders. It also completes the Soul set beside Gloves of Soul Catching and the Mask of Soul Perception. ⚠ Losing the Cloth costs advantage on Sleight of Hand; keep it bagged and swap back for theft.'
    - id: cloak-of-displacement
      item: Cloak of Displacement
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (27:27) — absolutely excellent'
      slot: cloaks
      bis: true
      note: 'Sold by Entharl Danthelon at Danthelon''s Dancing Axe, Wyrm''s Crossing. At the start of his turn, enemies take DISADVANTAGE on attack rolls against him until he takes damage. He is the only party member with neither armour nor damage reduction, so it is worth more here than on Charles in Helldusk plate. Useful wiki quirk: Displaced is not stripped by anything the game does not count as a hit, including a successful save against a damage-dealing spell.'
    - id: ring-of-free-action
      item: Ring of Free Action
      tier: C
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (21:55) — some minor uses; a swap-in against enemies that paralyse or Hold Person'
      slot: ring 1
      note: 'Araj Oblodra, Crimson Draughts in the Lower City, or from her at Moonrise in Act 2. Ignore difficult terrain and CANNOT BE PARALYSED OR RESTRAINED. His Night Walkers already cover Web, Entangle and Grease but not those two, and Paralysed is what turns a dived monk into a pile of free critical hits.'
    - id: act3-rings-asterion
      item: Shadow-Cloaked Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (38:32) — bonus damage is always among the best things an item can give, and this is no exception'
      held: true
      slot: ring 2
      note: 'Act 3 still has plenty of obscured interiors and Charles generates his own Darkness, so the +1d4 stays live on most turns. Swap it for the Eversight Ring whenever the plan is to fight inside Charles''s cloud. ⚠ The Callous Glow Ring is NOT his: it needs illuminated targets, which fights both the Shadow-Cursed Lands and Charles''s Darkness, and Gale''s Coruscation chain already lights targets for his own copy.'
    - id: act3-ranged-asterion
      item: Hand Crossbow +2
      tier: A
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (43:35) — the pick over Ne''er Misser only when Ballistic Armour doubles your piercing damage'
      slot: ranged weapons
      note: 'Any +2 pair from an Act 3 vendor. Monk 9 Deft Strikes upgrades hand crossbows he is proficient with to 1d8, so the slot is not wasted, but it stays a fallback for targets he cannot reach. ⚠ The Hellfire Hand Crossbow and Ne''er Misser both go to Bonbon, whose entire engine is hand-crossbow hits.'
    progression:
    - id: prog-head
      item: 'Head: Circlet of Psionic Revenge → Mask of Soul Perception'
      slot: head
      note: 'Act 1–2 Circlet (Crèche) → Act 3 Mask (Devil''s Fee). Only two entries because almost every good helmet in the game is tagged Light or Medium armour, and per the wiki those "prevent Unarmoured Defence from working" — that single rule disqualifies Covert Cowl, the Dark Justiciar Helmet and Shadow of Menzoberranzan for him permanently.'
    - id: prog-armour
      item: 'Chest: Graceful Cloth → Vest of Soul Rejuvenation'
      slot: armour
      note: Act 1–2 Graceful Cloth (Lady Esther) → Act 3 Vest (Sorcerous Sundries). The Cloth is Clothing so Unarmoured Defence survives; keep it bagged after the swap because its advantage on Dexterity checks is his pickpocketing.
    - id: prog-hands
      item: 'Hands: Bracers of Defence → Flawed Helldusk Gloves → Gloves of Soul Catching'
      slot: hands
      note: Act 1 Bracers (Blighted Village) → Act 2 Flawed Helldusk (Dammon, 3rd Infernal Iron) → Act 3 Soul Catching (House of Hope). Defence first while he is fragile, then damage once five strikes a turn make riders worth more than 2 AC.
    - id: prog-feet
      item: 'Boots: Disintegrating Night Walkers → Boots of Uninhibited Kushigo'
      slot: feet
      note: Act 1–2 Night Walkers (Nere, Grymforge) → Act 3 Kushigo boots (Astral Plane). Boots are not on the Monk armour-exclusion list, so an armour tag never matters here.
    - id: prog-cloaks
      item: 'Cloak: Deathstalker Mantle → Cloak of Displacement'
      slot: cloaks
      note: Act 1–2 Deathstalker (Dark Urge reward via Charles) → Act 3 Displacement (Danthelon). Nothing in the Act 2 pool beats invisibility-on-kill for a diver who reliably lands a kill each turn.
    - id: prog-amulets
      item: 'Amulet: Sentient Amulet → Amulet of the Harpers'
      slot: amulets
      note: Act 1 Sentient (Grymforge) → Act 2–3 Harpers (Talli). The Harpers swap is timed to the Resonance Stone — advantage on Wisdom saves cancels the disadvantage the Stone inflicts on its own carrier.
    - id: prog-ring1
      item: 'Ring 1: Bracing Band → Shadow-Cloaked Ring → Ring of Free Action'
      slot: ring 1
      note: 'Bracing Band from Sergeant Thrinn at Grymforge, and its +1 AC is live on any turn he throws Flurry of Blows: Push → Shadow-Cloaked Ring from the Shadow Mastiff Alpha → Ring of Free Action from Araj, which closes the Paralysed and Restrained gap the Night Walkers leave open.'
    - id: prog-ring2
      item: 'Ring 2: Crusher''s Ring → Eversight Ring → Shadow-Cloaked Ring'
      slot: ring 2
      note: Crusher's Ring for +3m movement in Act 1, when he has the most ground to cover → Eversight Ring from the House of Healing → Shadow-Cloaked moves across to this hand in Act 3. Eversight stays in the bag for any fight inside Charles's Darkness.
    - id: prog-weapons
      item: 'Melee: Corellon''s Grace (levels 2–4) → both hands EMPTY for the rest of the run'
      slot: weapons
      note: The only slot that ends the game deliberately empty. From character level 5 a held weapon makes Attack and Extra Attack swing it instead of punching, which loses Tavern Brawler and every unarmed rider.
    - id: prog-ranged
      item: 'Ranged: Hand Crossbows +1 → Hand Crossbows +2'
      slot: ranged weapons
      note: A fallback slot only, for targets he cannot reach. Monk 9 Deft Strikes upgrades hand crossbows he is proficient with to 1d8, so it is not wasted, but Ne'er Misser and the Hellfire Hand Crossbow both go to Bonbon.
    - id: prog-elixirs
      item: 'Elixir: Hill Giant Strength → Cloud Giant Strength'
      slot: consumables
      note: One every long rest, all game. It drives attack rolls, damage and the Stunning-Strike DC, and it occupies the one-elixir-per-rest slot so no Bloodlust alongside it.
  playstyle: |-
    - **Prep:** drink Giant Strength, enable Manifestation of Mind, and carry the Resonance Stone from Act 2 onward.
    - **Turn:** Stunning Strike the priority target, then Flurry: Topple (or Stagger against casters). Thief 3 adds a second Flurry.
    - **If Stun fails:** raw Flurries + Topple; switch Manifestation to Soul against psychic resistance.
  pickpocket:
    note: |-
      The party thief. Only Rogue 3, so there is no Reliable Talent floor and a steal CAN fail on a low roll. Expertise plus Graceful Cloth advantage still clears nearly every Act 1–2 lift; save-scum the rare high-DC item.

      Must-have high-DC item: quicksave-scum, Enthrall the vendor (ally-cast), or hand the lift to someone else. Escape is standard — turn-based mode to freeze timers, break line of sight, pass loot to a clean member, wait out the investigation.
    success_math: 'At char 12: DEX 20 (+5) + prof 4 doubled by Expertise (+8) = +13 flat, with Graceful Cloth advantage. No Reliable-Talent floor, so a low roll CAN fail — rare, and most targets sit well under. ⚠ Guidance and Bardic Inspiration do NOT apply to the background pickpocket roll; only flat Sleight-of-Hand gear does.'
    gear:
    - item: The Graceful Cloth
      effect: 'Cat''s Grace — advantage on DEX checks (stealing) plus DEX toward 20. Clothing, so Unarmoured Defence still works. Worn all game.'
      where: Lady Esther, Rosymorn Monastery Trail (Act 1)
    - item: Gloves of Thievery
      effect: Advantage on Sleight of Hand — the backup once the Cloth takes the glove slot.
      where: Brem, Zhentarim Basement (Act 1)
    - item: Smuggler's Ring (+2) / Gloves of Power (+1)
      wiki:
      - Smuggler's Ring
      - Gloves of Power
      effect: Flat +Sleight of Hand — the only lever that beats an over-floor target; swap in for that one lift.
      where: Various vendors / loot
  traps:
  - 'From char 5 onward, stay UNARMOURED, SHIELDLESS and EMPTY-HANDED. A monk weapon does not disable Martial Arts, Flurry or special unarmed commands, but ordinary main-action attacks swing it and lose Tavern Brawler and the unarmed riders.'
  - 'The Giant Strength elixir is load-bearing (attack, damage, Stun DC) and takes the one-elixir-per-long-rest slot — no Bloodlust or Battlemage alongside it. Bank a stack.'
  - 'Stunning Strike is a CON save — high-CON bosses, legendary resistance and undead may shrug it. Do not build the whole turn around it landing.'
  - 'No Reliable Talent (only Rogue 3) — high-DC pickpocketing can fail; save-scum or use flat +SoH gear.'
  - 'The Resonance Stone debuffs the party''s mental saves and makes HIM psychic-vulnerable (no Gnome Cunning) — cluster it in Charles''s Aura of Protection or leave it holstered against psychic enemies.'
  - 'Only 2 feats (Monk 4 + Monk 8), both spent on Tavern Brawler and Alert. A Monk 8 / Thief 4 split buys a third feat at the cost of Ki Resonation — a real option, but not this plan.'
  illithid:
    note: 'Ability Drain — A-tier, free passive, and his alone in this party. Once per turn when he makes an attack roll, the target''s matching ability drops by 1 (Strength or Dexterity for unarmed strikes), degrading the enemy''s own offence, and it counts as inflicting a condition. ⚠ Once per TURN, not per hit, so it does not scale with his 4–6 strikes. Also worth buying Luck of the Far Realms for him: Charles''s stacked crit-threshold gear makes the reaction fire early on hits that were already crits, whereas Asterion stacks none and gets a reliable trigger. ⚠ Cull the Weak is mutually exclusive with Non-Lethal Attacks — toggle it off before any knockout you need to leave alive. Alert makes him the first-turn Black Hole carrier — the pull has no save, and targets inside the Stone aura roll its secondary Slow save at disadvantage vs his DC 17. He still has two Flurries afterward; when grouping is unnecessary, pre-cast Psionic Overload and keep the Action for two attacks. Cull the Weak handles mob cleanup — off when a kill must trigger Deathstalker. Bonbon keeps Mind Blast. NOT Awakened — his bonus actions are Flurries/Step.'
---
