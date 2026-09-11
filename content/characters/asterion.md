---
nickname: Asterion
builds:
- name: The Fist in the Dark
  is_primary: true
  role: Mobile Open-Hand monk — stun-lock striker, psychic flurry, party thief
  class: Open Hand Monk 9 / Thief Rogue 3
  at_a_glance:
    armour: None — unarmoured, shieldless and empty-handed; any armour-tagged helmet or glove breaks Unarmoured Defence
    elixir: Giant Strength every long rest (Hill 21 → Cloud 27) — Tavern Brawler runs on it
    concentration: Bless from the Staff of Arcane Blessing, or Celestial Haste from Gontr Mael in Act 3 — each once per long rest, never both at once
  build_order: Rogue 1 (creation, Expertise) → Monk 1–6 (char 2–7) → Rogue 2–3 Thief (char 8–9) → Monk 7–9 (char 10–12). No respec after the initial rebuild.
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: 'Fey Ancestry, Darkvision, one fixed High Elf cantrip, bonus-action Vampire Bite. ASCEND at Cazador for +1d10 Necrotic on every unarmed hit, Ascendant Bite and Misty Escape. ⚠ Stay unarmoured, shieldless and empty-handed.'
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background, unchangeable even by respec.
  starting_stats:
    STR: 8
    DEX: 16
    CON: 15
    INT: 8
    WIS: 17
    CHA: 8
  stats_note: 'Point-buy 8/15/15/8/15/8, all 27 points. Every +1 this build receives has to land on an odd score, which is why DEX, CON and WIS all start at 15 and INT is dumped.'
  ability_targets: 'MODDED Hair: racial +2 and Hag''s Hair both go to WIS, 15 → 17 → 18; Mirror of Loss takes it to 20 (DC 25 Religion check + 60% roll: Enhance Ability, Guidance, quicksave first). Racial +1 to DEX 16, Graceful Cloth to 18. Tavern Brawler''s +1 to CON, never STR.'
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
    - score: 16
      source: '+1 Racial'
    - score: 18
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
    - score: 17
      source: '+2 Racial'
    - score: 18
      source: '+1 Hag''s Hair'
    - score: 20
      source: '+2 Mirror of Loss, Act 3 (DC 25 Religion check + 60% roll: Enhance Ability, Guidance, quicksave first)'
  - ability: CHA
    steps:
    - score: 8
      source: 'point-buy'
  feats:
  - at: Monk 4 (char 5)
    feat: Tavern Brawler
    note: 'Adds the Giant Strength modifier to unarmed attack rolls AND damage a second time, and raises CON 15 → 16. Take the CON option, drink the elixir every long rest, unequip Corellon''s Grace. ⚠ Once STR beats DEX it also sets the Stun DC.'
  - at: Monk 8 (char 11)
    feat: Alert
    note: '+5 Initiative and immunity to Surprise — the first turn, to open-strike and Stun the priority target before it acts. Arrives at char 11 under the Rogue-tail order.'
  key_abilities:
  - Flurry of Blows — Open Hand variants Topple (Prone) / Stagger (no Reactions) / Push
  - Stunning Strike — the party's on-demand hard control
  - Manifestation of Mind — +psychic per unarmed hit, DOUBLED by the Resonance Stone
  - Ki Resonation (Punch → Blast) — AoE finisher
  - Step of the Wind / Patient Defense / Deflect Missiles — mobility + defense
  - Fast Hands (Thief) → two Flurries of Blows per turn
  combat_style: 'Char 2–4 — Corellon''s Grace improves Flurry punches and saves. Char 5 — Tavern Brawler takes over: unequip every melee weapon, stay unarmoured and shieldless, drink Giant Strength daily, punch.'
  creation:
    level1_class: Rogue 1 (taken at character creation / first class in the respec)
    level1_gains: '4 Rogue skills (Stealth, Investigation, Acrobatics, Athletics) + Expertise in Sleight of Hand and Stealth + Sneak Attack 1d6, which needs a finesse OR ranged weapon, so it rides the hand crossbows. MUST be the creation class.'
    subclass_choice: Open Hand (Monk 3) · Thief (Rogue 3)
    proficiencies:
      armor_weapons: Unarmed and unarmoured — required for Martial Arts / Flurry / Unarmoured Defence.
      saving_throws: DEX + INT (Rogue).
      skills: 'Charlatan (Deception, Sleight of Hand) + Elf Keen Senses (Perception) + 4 Rogue picks (Stealth, Investigation, Acrobatics, Athletics). Expertise: Sleight of Hand + Stealth. Only Rogue 3, so no second pair and no Reliable Talent.'
    starting_cantrips: 'One High Elf cantrip, fixed at creation on a recruited companion and never re-presented by the respec. Read it off the save; nothing in the build depends on it.'
    starting_spells: None — Ki/martial build.
    notes: '2 feats (Monk 4 + Monk 8 = char 5 and char 11). Rogue 1 FIRST for Expertise, then Monk 1–6, Rogue 2–3, Monk 7–9. Giant Strength elixir every long rest.'
  spells:
    note: Not a caster. His build-defining Ki abilities and martial features appear at their unlock levels in the Leveling guide; this panel tracks the one High Elf racial cantrip.
    mandatory:
    - spell: Flurry of Blows (+ Open Hand variants)
      level: Feature (Monk 1; Open Hand variants Monk 3)
      school: Ki — Bludgeoning + rider
      save: 'Topple: DEX · Push: STR · Stagger: none (weapon-action DC)'
      when: char 2 (Monk 1) / char 4 (Monk 3)
      why: 'Bonus action + 1 Ki → two unarmed strikes. Open Hand adds Topple (Prone), Stagger (no Reactions) and Push (5 m + fall damage). Fast Hands from char 9 gives a second Flurry every turn.'
    - spell: Stunning Strike
      level: Feature (Monk 5)
      school: Ki — control
      save: CON save (DC 8 + prof + higher of DEX/STR)
      when: char 6 (Monk 5)
      why: '1 Ki on a hit: CON save or Stunned — auto-fails STR and DEX saves, attacked at advantage, loses its turn. The DC rides the elixir''s STR. ⚠ The Resonance Stone does not help; Stunning Strike is a CON save.'
    - spell: Manifestation of Mind
      level: Feature (Open Hand, Monk 6)
      school: Toggle — Psychic
      save: None
      when: char 7 (Monk 6)
      why: 'Toggle it on before every fight: +1d4 + WIS Psychic per unarmed strike, doubled by the Resonance Stone across 4–6 hits. Switch to Soul or Body against psychic-resistant enemies.'
    - spell: Extra Attack
      level: Feature (Monk 5)
      school: N/A
      save: None
      when: char 6 (Monk 5)
      why: With both melee hands empty the Action supplies two unarmed strikes; the Martial-Arts bonus strike and Flurry stack on top.
    - spell: 'Tavern Brawler + Giant Strength elixir'
      level: Feat (Monk 4) + consumable
      school: N/A
      save: None
      when: char 5
      why: Drink an Elixir of Giant Strength every long rest. Tavern Brawler adds that STR modifier to unarmed attack rolls and damage again, and once STR beats DEX it also sets the Stun DC.
    recommended:
    - spell: Minor Illusion
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (35:56) — moves NPCs with no save or roll; clusters enemies for AoE, sets ambushes, pulls enemies one at a time'
      source: granted
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: char 1 (High Elf racial cantrip — fixed, not selectable)
      why: 'Not a pick to make — a recruited companion''s racial cantrip is locked at creation and the respec never re-presents it. Check the save for what he actually has; nothing depends on it.'
    - spell: Celestial Haste
      level: Item action (Gontr Mael)
      school: Transmutation — self only
      save: None (Concentration)
      when: Act 3, once per long rest
      why: 'Gontr Mael''s once-per-long-rest self-Haste: an extra Action for 5 turns, +2 AC, no Lethargic. Gale never Hastes him. ⚠ Concentration, so a day gets Haste or the staff''s Bless, never both.'
    - spell: Ki Resonation (Punch → Blast)
      level: Feature (Open Hand, Monk 9)
      school: Ki — detonate
      save: CON save
      when: char 12 (Monk 9)
      why: Punch to mark a target Resonating, then Blast to detonate an AoE around it — party and summons excluded. The nova finisher on a clustered pack.
    - spell: Step of the Wind
      level: Feature (Monk 2)
      school: Ki — mobility
      save: None
      when: char 3 (Monk 2)
      why: Bonus-action Dash or Disengage, jumping free — dive the back line and leave melee without opportunity attacks.
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
      why: 'Reaction: reduce a ranged attack by 1d10 + DEX + monk level, often to 0, and optionally hurl it back at the archer.'
    - spell: Wholeness of Body
      level: Feature (Open Hand, Monk 6)
      school: Ki — heal + economy
      save: None
      when: char 7 (Monk 6)
      why: 'Action, once per long rest: heal 3× monk level, refund half his Ki, and gain an extra bonus action for 3 turns.'
    - spell: Fast Hands (Thief)
      level: Feature (Thief, Rogue 3)
      school: N/A
      save: None
      when: char 9 (Thief 3)
      why: A permanent second bonus action → Flurry of Blows TWICE per turn (2 Ki, 4 extra strikes) on top of the Attack action.
    - spell: Vampire Bite
      level: Racial (Vampire Spawn)
      school: Bonus action — Necrotic + heal
      save: None
      when: char 1
      why: 'Bite a living creature before a fight for Happy: +1 to attack rolls, saves and most checks. ⚠ Not Gale, not corpses, not pre-upgrade Karlach.'
    - spell: Ascendant Bite
      level: Racial (Vampire Ascendant)
      school: Bonus action — Necrotic + heal
      save: None
      when: Act 3, after Cazador
      why: 'Replaces Vampire Bite once he Ascends: 6d6 healing, 6d6 Necrotic, and it grants Happy too. Ascension also adds +1d10 Necrotic to every unarmed hit.'
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
      - Athletics
      note: 'SIX picks land here, not two — 4 Rogue skills come BEFORE the 2 Expertise picks. Stealth is mandatory: nothing else grants it, so Expertise: Stealth has no target without it. Athletics rides the Giant Strength elixir for Shove.'
    - category: Expertise
      picks: 2
      recommendation:
      - Sleight of Hand
      - Stealth
      note: Why Rogue must be the first class — these two power stealing and scouting for the whole run.
    - category: Racial cantrip
      wiki: false
      granted: true
      fixed: true
      recommendation: Whatever Larian assigned him (one High Elf wizard cantrip)
      note: '⚠ NOT a selection. A recruited companion''s racial cantrip is fixed at creation and the Withers respec never re-presents it — read it off the save and plan nothing around it.'
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
      note: Adds the Giant Strength modifier to unarmed attack and damage rolls a second time, and raises CON to 16. The accuracy and damage engine.
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
    class: Rogue 2
    gains:
    - Cunning Action (Dash, Disengage, and Hide)
  - char_level: 9
    class: Rogue 3 (Thief)
    gains:
    - Fast Hands (permanent second bonus action)
    - Second-Story Work
    recommendations:
    - category: Subclass
      picks: 1
      recommendation: Thief
      note: Fast Hands gives two Flurries of Blows per turn — the reason for the Rogue tail, and taking it here lands it three levels earlier.
  - char_level: 10
    class: Monk 7
    gains:
    - Evasion
    - Stillness of Mind
  - char_level: 11
    class: Monk 8
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Alert
      note: +5 Initiative and immunity to Surprise let him Stun the priority target before it acts. A +2 WIS ASI is the defensive alternative.
  - char_level: 12
    class: Monk 9
    gains:
    - Advanced Unarmoured Movement
    - Ki Resonation attacks and Blast
    - Martial Arts die 1d8
  itemization:
    act1:
    - id: staff-of-arcane-blessing
      item: Staff of Arcane Blessing
      tier: A
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (24:19) — incredible for a party making frequent spell attack rolls, and does less than the tooltip implies'
      slot: weapons
      note: 'HIS JOB, NOT A WEAPON. Arcane Tower BASEMENT, Underdark — someone must carry Bernard''s Guiding Light ring for the elevator. Out of combat: equip, cast Bless on Charles, Gale and Bonbon, unequip. ⚠ Once per long rest, three targets only, and never let Gale consume it.'
    - id: corellon-s-grace
      item: Corellon's Grace
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (10:19) — great for a Tavern Brawler Monk defensively and offensively, but early-game only'
      slot: weapons
      note: 'EARLY ONLY, from Auntie Ethel. Natural Pugilist improves bonus-action and Flurry punches and unarmoured gives +2 saves. ⚠ UNEQUIP at char 5 or Attack and Extra Attack swing the staff and lose Tavern Brawler.'
    - id: dual-hand-crossbows-plus-one
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      slot: ranged weapons
      note: 'A PAIR, one per hand, from Act 1 weapon traders. Rogue proficiency gives a main-hand shot plus a bonus-action off-hand shot when melee is out of reach. ⚠ Keep the dual-wield toggle OFF so a shot cannot spend a Flurry.'
    - id: graceful-cloth
      item: Graceful Cloth
      tier: S
      tier_note: 'TwFGCc8OOfw (10:24) — +2 Dexterity is the strongest effect on the list; initiative, AC and damage in one'
      rank: '#3'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #3 of 20 — +2 Dexterity and advantage on Dexterity checks; acts like a free feat'
      wiki: The Graceful Cloth
      slot: armour
      bis: true
      note: 'Lady Esther, Rosymorn trail. Clothing, not armour, so Unarmoured Defence still works. DEX 16 → 18, and its advantage on Dexterity checks is his pickpocket bonus. Worn through Acts 1–2.'
    - id: circlet-of-psionic-revenge
      item: Circlet of Psionic Revenge
      tier: B
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (13:02) — a small amount of damage that is not always triggered, but it will see play in some compositions'
      slot: head
      note: 'THE ONLY LEGAL HEAD IN ACT 1. Githyanki Inquisitor Ch''r''ai W''wargaz, Crèche Inquisitor''s Chamber. Succeed a save and the foe that forced it takes 1d4 Psychic, doubled by the Resonance Stone from Act 2. ⚠ Light, Medium and Heavy-tagged helmets break Unarmoured Defence.'
    - id: act1-hands-asterion
      item: Glove slot
      slot: hands
      wiki: false
      note: 'OPEN ALL OF ACT 1 — no best-in-slot until the Gloves of Soul Catching in Act 3, so pick per fight. Bracers are the default; swap to an offensive pair for short fights.'
      options:
      - id: bracers-of-defence
        item: Bracers of Defence
        tier: S
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (10:30) — for a wide array of characters, though often discarded for a later upgrade'
        note: 'DEFAULT. Blighted Village cellar. +2 AC while unarmoured and shieldless — AC 21 at DEX 18 / WIS 20, the highest no-armour AC in the party.'
      - id: the-sparkle-hands
        item: The Sparkle Hands
        tier: A
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (43:19) — a solid alternative to an S-tier item, with real usage of its own'
        note: 'Decrepit Sanctuary, Sunlit Wetlands. 2 Lightning Charges per unarmed hit: extra attack and damage, a 1d8 Lightning burst, and advantage against metal-armoured enemies. Best on 4–6-hit turns.'
      - id: gloves-of-cinder-and-sizzle
        item: Gloves of Cinder and Sizzle
        tier: S
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (21:57) — an S-tier pick for just about every monk, because damage is the class''s job'
        note: 'Lady Esther, late Act 1. +1d4 Fire per unarmed hit plus one level-3 Scorching Ray a long rest. ⚠ Prefer Sparkle Hands against metal armour or fire resistance.'
      - id: gloves-of-thievery
        item: Gloves of Thievery
        tier: B
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (33:57) — functionally equivalent to the Gloves of Power for the same job'
        note: 'Brem, Zhentarim. Advantage on Sleight of Hand, and unlike Guidance it shows up in the pickpocket window. Keep them bagged and swap in only to steal.'
    - id: elixir-of-giant-strength
      item: Elixir of Hill Giant Strength
      tier: S
      tier_note: '9BcQXb37Bik (30:26) — sets Strength to 21; S used normally, and S+ ABOVE THE SCALE if drunk daily to skip strength investment'
      slot: consumables
      note: 'Hill Giant (STR 21) early → Cloud Giant (STR 27) later. Drink one every long rest; it drives attack rolls, damage and the Stunning-Strike DC. ⚠ It takes the one-elixir-per-rest slot.'
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (6:44) — DARK URGE ORIGIN ONLY; free invisibility on a kill, broken, and the only act one magic cloak'
      rank: '#4'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #4 of 20 — invisibility after a kill, in a slot with no early competition'
      wiki: The Deathstalker Mantle
      slot: cloaks
      bis: true
      note: 'Dark Urge reward, handed over by Charles. Invisible for 2 turns on a kill — reposition and re-engage. ⚠ The only magical cloak obtainable in Act 1 by anyone.'
    - id: disintegrating-night-walkers
      item: Disintegrating Night Walkers
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (19:19) — probably the best boots in the game'
      rank: '#11'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #11 of 20 — short-rest Misty Step plus immunity to most movement-restricting surfaces'
      slot: feet
      bis: true
      note: 'Nere, Grymforge. Misty Step once per short rest; cannot be Enwebbed, Entangled or Ensnared and cannot slip on grease or ice — the permanent combat boots. ⚠ No cover for Paralysed or Restrained; the Ring of Free Action closes that in Act 3.'
    - id: bracing-band
      item: Bracing Band
      tier: A
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (6:13) — good for a lot of characters, though there are often better options'
      slot: ring 1
      note: 'Sergeant Thrinn''s reward for Find the Missing Boots, Grymforge. +1 AC until his next turn after a Shove, and Flurry of Blows: Push counts, so it is up on any turn he pushes. ⚠ Thrinn gives one of two rewards — take this over Armour of Uninhibited Kushigo.'
    - id: act1-ring2-asterion
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'OPEN. Movement comes first in Act 1 — he has the longest distance to cover and the most attacks to land once he arrives.'
      options:
      - id: crusher-s-ring
        item: Crusher's Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (9:50) — movement speed is universally applicable; an extremely rare party leaves it on the table'
        note: 'DEFAULT. Take it from Crusher at the Goblin Camp: +3 m movement, stacks with Longstrider, reaches the priority target without spending a bonus action.'
      - id: opt-ring-of-protection-ast
        item: Ring of Protection
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (34:55) — raises the party''s average AC; give it to the easiest-to-hit member'
        rank: '#20'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #20 of 20 — +1 AC and all saves fits almost anyone, for the whole game'
        note: '+1 AC and +1 to all saving throws. Gale''s by default — take it only if he can spare it.'
      - id: opt-smugglers-ring
        item: Smuggler's Ring
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (40:05) — +2 Sleight of Hand is great, but it is a fully out-of-combat item'
        note: '+2 Sleight of Hand, and being flat it moves the pickpocket window''s roll-needed number. Swap it in for one high-DC lift.'
    - id: sentient-amulet
      item: Sentient Amulet
      tier: A
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (43:06) — mainly for its use on a monk, but worth having in the arsenal'
      slot: amulets
      note: 'Grymforge, Adamantine chest. Ki Restoration (2 Ki, once per long rest) plus Shatter — a cheap early neck that refuels Flurries. ⚠ Mind the rare version''s WIS-save Hysterical effect.'
    - id: armour-of-uninhibited-kushigo
      item: Armour of Uninhibited Kushigo
      tier: C
      tier_note: 'TwFGCc8OOfw (5:09) — monk-only; Kushigo Counter needs Patient Defense, the weakest monk bonus action'
      slot: armour
      note: 'Grymforge, for returning Sergeant Thrinn''s boots. Kushigo Counter gives a reaction unarmed strike when an attacker misses during Patient Defence. Graceful Cloth stays default; wear this only for a counter fight.'
    act2:
    - id: resonance-stone
      item: Resonance Stone
      slot: other
      note: 'Mind Flayer Colony, late Act 2. He carries it: Manifestation of Mind, Psionic Overload and the Circlet''s retaliation all double, and enemies near him fail the WIS saves for Command and both Holds. ⚠ Not Stunning Strike (CON save), and it makes the party psychic-vulnerable — holster it against psychic enemies.'
    - id: amulet-of-the-harpers
      item: Amulet of the Harpers
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (25:47) — such a powerful effect for such a relatively small cost'
      slot: amulets
      note: 'Quartermaster Talli, Last Light Inn. Advantage on WISDOM saving throws plus Shield once per long rest — it cancels the disadvantage the Stone he carries inflicts, and answers Hold Person, Fear and Dominate.'
    - id: flawed-helldusk-gloves
      item: Flawed Helldusk Gloves
      tier: S
      tier_note: 'The BEST GLOVES In Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (11:57) — increasing weapon damage is simply that powerful'
      slot: hands
      note: 'Dammon at Last Light Inn, after the THIRD piece of Infernal Iron. +1d4 Necrotic per unarmed hit, can inflict Bleeding, +1 STR saves, and no armour tag. ⚠ The same iron upgrades Karlach''s engine — budget it.'
    - id: shadow-cloaked-ring
      item: Shadow-Cloaked Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (38:32) — bonus damage is always among the best things an item can give, and this is no exception'
      slot: ring 1
      note: 'THE ACT 2 DAMAGE RING. Shadow Mastiff Alpha at the Ruined Battlefield — destroy the everburning torches nearby to make it appear. +1d4 against Lightly or Heavily Obscured creatures, unarmed hits included, so it is live almost everywhere in the Shadow-Cursed Lands.'
    - id: eversight-ring
      item: Eversight Ring
      tier: A
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (9:55) — mandatory with a Warlock or a Darkness plan; depends heavily on party composition'
      wiki: Eversight Ring
      slot: ring 2
      note: 'House of Healing morgue. Cannot be Blinded, so he FIGHTS UNBLINDED inside Charles''s Darkness cloud. It displaces Crusher''s Ring from Act 2. ⚠ Nobody shoots into or out of the cloud, sight or not.'
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
      note: 'CARRIED OVER. Clothing rather than armour, so Unarmoured Defence still applies; +2 Dexterity and advantage on all Dexterity checks, which doubles as his pickpocket bonus.'
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
      note: 'CARRIED OVER. Misty Step once per short rest; no Web, Entangle, Ensnare, or slipping on grease and ice — mobility and safety in one slot.'
      options:
      - id: opt-boots-of-stormy-clamour-asterion-a2
        item: Boots of Stormy Clamour
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (12:32) — the best way to apply Reverberation, and many builds are based on it'
        rank: '#7'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #7 of 20 — any condition also applies Reverberation; build-defining later'
        note: 'PER FIGHT, borrowed from Charles whenever he wears Striding. Every condition Asterion inflicts adds 2 turns of Reverberation, so the next Stunning Strike CON save is at −2 to −4. Costs the Night Walkers'' Misty Step that fight.'
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
      note: 'CARRIED OVER. A kill grants Greater Invisibility — on the party thief that is both an escape and a repositioning tool.'
    - id: act2-ranged-asterion
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      held: 1
      slot: ranged weapons
      note: 'CARRIED OVER, still a pair, for turns melee cannot reach. ⚠ Dual-wield toggle stays OFF.'
    - id: act2-weapons-asterion
      item: Empty hands
      held: 1
      slot: weapons
      wiki: false
      note: 'CARRIED OVER and deliberately empty, so Attack and Extra Attack resolve as unarmed strikes. The Staff of Arcane Blessing is carried only as a pre-combat Bless swap.'
    act3:
    - id: gloves-of-soul-catching
      item: Gloves of Soul Catching
      tier: S
      tier_note: 'The BEST GLOVES In BG3 COMPLETE - Honor Mode Tier List and Guide - Act 3 (22:25) — the numbers on this item are ridiculously high'
      slot: hands
      bis: true
      note: House of Hope, Hope's reward. +1d10 Force per unarmed hit, +2 CON, and once a turn either heal 10 HP or take +5 to an attack or save.
    - id: mask-of-soul-perception
      item: Mask of Soul Perception
      tier: S
      tier_note: 'Is EVERY Act 3 Helmet Awesome? - BG3 Helmets Tier List and Guide - Act 3 (26:03) — a great item that pretty much every party will want to use on someone'
      slot: head
      bis: true
      note: Devil's Fee — locked chest in Helsik's room, DC 20. +2 to attack rolls, Initiative and Perception, plus Detect Thoughts. It retires the Circlet.
    - id: boots-of-uninhibited-kushigo
      item: Boots of Uninhibited Kushigo
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (55:34) — best in slot for pretty much every monk; a damage item for a damage class'
      slot: feet
      note: Prelate Lir'i'c, Astral Plane, at the start of Act 3. Adds his WIS modifier to every unarmed strike, so flat damage on all 5–6 hits. Boots carry no armour-tag problem for a monk.
      options:
      - id: opt-boots-of-stormy-clamour-asterion-a3
        item: Boots of Stormy Clamour
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (12:32) — the best way to apply Reverberation, and many builds are based on it'
        rank: '#7'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #7 of 20 — any condition also applies Reverberation; build-defining later'
        note: 'PER FIGHT, borrowed from Charles whenever he wears Helldusk Boots. Wear them when Asterion is the condition-inflicter and the next Stunning Strike matters more than the Kushigo WIS damage.'
    - id: vest-of-soul-rejuvenation
      item: Vest of Soul Rejuvenation
      tier: S
      tier_note: 'TwFGCc8OOfw (54:13) — +2 AC best in slot for monks, but S BY DEFAULT with no real competition'
      slot: armour
      note: 'ACT 3 CHEST. Rolan at Sorcerous Sundries, or Lorroakan''s Projection if Rolan is dead. +2 AC unarmoured, 1d4 healing on a save against a spell, and a reaction unarmed strike carrying every rider when an attacker misses. ⚠ Keep the Graceful Cloth bagged for theft.'
    - id: cloak-of-displacement
      item: Cloak of Displacement
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (27:27) — absolutely excellent'
      slot: cloaks
      bis: true
      note: 'Entharl Danthelon, Danthelon''s Dancing Axe, Wyrm''s Crossing. From the start of his turn enemies attack him at DISADVANTAGE until he takes damage — worth most on the one body with neither armour nor damage reduction.'
    - id: ring-of-free-action
      item: Ring of Free Action
      tier: C
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (21:55) — some minor uses; a swap-in against enemies that paralyse or Hold Person'
      slot: ring 1
      note: 'Araj Oblodra — Moonrise in Act 2, or Crimson Draughts in the Lower City. Ignores difficult terrain and CANNOT BE PARALYSED OR RESTRAINED, the one gap the Night Walkers leave open.'
    - id: act3-rings-asterion
      item: Shadow-Cloaked Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (38:32) — bonus damage is always among the best things an item can give, and this is no exception'
      held: true
      slot: ring 2
      note: 'Act 3 keeps plenty of obscured interiors and Charles makes his own Darkness, so the +1d4 stays live most turns. Swap to the Eversight Ring for any fight inside the cloud. ⚠ The Callous Glow Ring is Gale''s, not his.'
    - id: act3-ranged-asterion
      item: Gontr Mael
      tier: A
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (50:53) — at-will Celestial Haste is nice, but only the third best two-handed bow for damage'
      slot: ranged weapons
      bis: true
      note: 'Steel Watcher Titan, Steel Watch Foundry — it does not drop if the Titan dies to Atrophied. Never fired; held for CELESTIAL HASTE, a holder action needing no proficiency: self-Haste, 5 turns, no Lethargic. ⚠ Concentration, so not on a Bless day.'
    - id: ascension-asterion
      item: Vampire Ascendant
      slot: other
      note: 'ASCEND at Cazador''s palace, Act 3. +1d10 Necrotic on every unarmed hit across 5–6 hits a turn, plus Ascendant Bite (6d6 heal, 6d6 Necrotic, grants Happy) and Misty Escape. ⚠ Not doubled by the Resonance Stone.'
    progression:
    - id: prog-head
      item: 'Head: Circlet of Psionic Revenge → Mask of Soul Perception'
      slot: head
      note: 'Acts 1–2 Circlet (Crèche) → Act 3 Mask (Devil''s Fee). Only two entries: helmets tagged Light, Medium or Heavy armour break Unarmoured Defence, which rules out most of the slot for him.'
    - id: prog-armour
      item: 'Chest: Graceful Cloth → Vest of Soul Rejuvenation'
      slot: armour
      note: Acts 1–2 Graceful Cloth (Lady Esther) → Act 3 Vest (Sorcerous Sundries). Keep the Cloth bagged after the swap — its advantage on Dexterity checks is his pickpocketing.
    - id: prog-hands
      item: 'Hands: Bracers of Defence → Flawed Helldusk Gloves → Gloves of Soul Catching'
      slot: hands
      note: Act 1 Bracers (Blighted Village) → Act 2 Flawed Helldusk (Dammon, 3rd Infernal Iron) → Act 3 Soul Catching (House of Hope). Defence first, damage once five strikes a turn beat 2 AC.
    - id: prog-feet
      item: 'Boots: Disintegrating Night Walkers → Boots of Uninhibited Kushigo'
      slot: feet
      note: Acts 1–2 Night Walkers (Nere, Grymforge) → Act 3 Kushigo boots (Astral Plane). Borrow Charles's Boots of Stormy Clamour for fights where Asterion is the condition-inflicter.
    - id: prog-cloaks
      item: 'Cloak: Deathstalker Mantle → Cloak of Displacement'
      slot: cloaks
      note: Acts 1–2 Deathstalker (Dark Urge reward via Charles) → Act 3 Displacement (Danthelon). Nothing in the Act 2 pool beats invisibility-on-kill for a diver.
    - id: prog-amulets
      item: 'Amulet: Sentient Amulet → Amulet of the Harpers'
      slot: amulets
      note: Act 1 Sentient (Grymforge) → Acts 2–3 Harpers (Talli). Time the Harpers swap to the Resonance Stone — advantage on Wisdom saves cancels the disadvantage the Stone inflicts on its carrier.
    - id: prog-ring1
      item: 'Ring 1: Bracing Band → Shadow-Cloaked Ring → Ring of Free Action'
      slot: ring 1
      note: 'Bracing Band (Thrinn, Grymforge), live on any turn he throws Flurry of Blows: Push → Shadow-Cloaked Ring (Shadow Mastiff Alpha) → Ring of Free Action (Araj), which closes the Paralysed and Restrained gap.'
    - id: prog-ring2
      item: 'Ring 2: Crusher''s Ring → Eversight Ring → Shadow-Cloaked Ring'
      slot: ring 2
      note: Crusher's Ring for +3 m in Act 1 → Eversight Ring (House of Healing) → Shadow-Cloaked moves to this hand in Act 3. Keep Eversight bagged for fights inside Charles's Darkness.
    - id: prog-weapons
      item: 'Melee: Corellon''s Grace (levels 2–4) → both hands EMPTY for the rest of the run'
      slot: weapons
      note: The one slot that ends the game deliberately empty. From char 5 a held weapon makes Attack and Extra Attack swing it, losing Tavern Brawler and every unarmed rider.
    - id: prog-ranged
      item: 'Ranged: Hand Crossbows +1 → Gontr Mael'
      slot: ranged weapons
      note: Hand crossbows through Acts 1–2 for targets he cannot reach → Gontr Mael (Steel Watch Foundry) in Act 3, held for its once-per-long-rest Celestial Haste rather than fired.
    - id: prog-elixirs
      item: 'Elixir: Hill Giant Strength → Cloud Giant Strength'
      slot: consumables
      note: One every long rest, all game — it drives attack rolls, damage and the Stunning-Strike DC. No Bloodlust alongside it, but Potion of Speed is a potion and does stack.
  playstyle: |-
    - **Prep:** drink Giant Strength, toggle Manifestation of Mind on, bite a living creature for Happy (+1 attack rolls, saves and checks; Ascendant Bite after Cazador), and carry the Resonance Stone from Act 2. Pick the day's concentration: staff Bless or Gontr Mael's Celestial Haste.
    - **Opener:** Hide outside enemy vision cones — no roll needed. Release Shift first, or the whole party tries to hide and Charles rolls Stealth.
    - **Turn:** Stunning Strike the priority target, then Flurry: Topple on a concentrating caster, because Prone ends concentration with no save. Stagger only against a caster with a dangerous reaction. Fast Hands adds a second Flurry from char 9.
    - **Nova:** drink a Potion of Speed — a potion, so it stacks with the Giant Strength elixir — then Ki Resonation Punch and Blast from char 12.
    - **If Stun fails:** raw Flurries plus Topple, then leave. End the turn 50 ft from melee enemies and Dash out rather than stand there.
    - **Inside Charles's Darkness:** wear the Eversight Ring and fight unblinded. Nobody, him included, shoots into or out of the cloud.
  pickpocket:
    note: |-
      The party thief. Only Rogue 3, so no Reliable Talent floor and a low roll CAN fail. Expertise plus Graceful Cloth advantage clears nearly every Act 1–2 lift; quicksave before a high-DC item.

      For a must-have over the floor: Enthrall the vendor (ally-cast) or hand the lift to someone else. To escape, enter turn-based mode, break line of sight, pass the loot to a clean member and wait the investigation out.
    success_math: 'At char 12: DEX 18 (+4) + proficiency 4 doubled by Expertise (+8) = +12 flat, with advantage from the Graceful Cloth. ⚠ Guidance and Bardic Inspiration do NOT apply to the pickpocket roll; only flat Sleight-of-Hand gear does.'
    gear:
    - item: The Graceful Cloth
      effect: 'Cat''s Grace — advantage on Dexterity checks, so on every Sleight of Hand roll, plus DEX 16 → 18. Clothing, so Unarmoured Defence still works.'
      where: Lady Esther, Rosymorn Monastery Trail (Act 1)
    - item: Gloves of Thievery
      effect: Advantage on Sleight of Hand — the Act 3 backup, once the Vest of Soul Rejuvenation replaces the Cloth.
      where: Brem, Zhentarim Basement (Act 1)
    - item: Smuggler's Ring (+2) / Gloves of Power (+1)
      wiki:
      - Smuggler's Ring
      - Gloves of Power
      effect: Flat +Sleight of Hand — the only lever that beats an over-floor target. Swap in for that one lift.
      where: Various vendors / loot
  traps:
  - 'From char 5 stay UNARMOURED, SHIELDLESS and EMPTY-HANDED. Flurry and the special unarmed commands still work with a weapon held, but ordinary attacks swing it and lose Tavern Brawler and every rider.'
  - 'The Giant Strength elixir is load-bearing and takes the one-elixir-per-long-rest slot — no Bloodlust. Bank a stack. With no elixir, punch on DEX (+4/+4) and still keep both hands empty.'
  - 'Stunning Strike is a CON save — high-CON bosses, legendary resistance and undead shrug it. Do not build the whole turn around it landing.'
  - 'No Reliable Talent at Rogue 3 — a high-DC pickpocket can fail. Quicksave, or swap in flat +Sleight of Hand gear.'
  - 'The Resonance Stone debuffs the party''s mental saves and makes HIM psychic-vulnerable — keep him inside Charles''s Aura of Protection, or holster the Stone against psychic enemies.'
  - 'Stillness of Mind auto-casts from char 10 and spends his ACTION — no toggle, no prompt. Stand inside Charles''s aura when fear is expected; nothing in the party grants immunity.'
  - 'Keep the DUAL-WIELD toggle OFF. With it on, a hand-crossbow shot spends a Flurry on an off-hand shot.'
  - 'Only 2 feats (char 5 and char 11), both spent. Monk 8 / Thief 4 buys a third at the cost of Ki Resonation and the d8 Martial Arts die — not this plan.'
  illithid:
    note: 'Ability Drain — his alone: once per turn an attack drops the target''s matching ability by 1, and it counts as inflicting a condition. Add Luck of the Far Realms. Alert at char 11 makes him the first-turn Black Hole carrier. ⚠ Cull the Weak off before a non-lethal knockout.'
---
