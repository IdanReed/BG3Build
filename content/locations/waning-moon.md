---
slug: waning-moon
name: The Waning Moon
act: 2
order: 100
region: Shadow-Cursed Lands
wiki: The Waning Moon
summary: 'Thisobald Thorm''s distillery. Optional on the party''s route: no plan gear here. Worth the stop for Madeline''s Ledger (Punish the Wicked), Thisobald''s hint about Ketheric''s relic, and his poison lab.'
arrive: 'Deep curse: Pixie Blessing or a lit Moonlantern in hand, or the party cannot be here. West of the central square. Several doors from the street and the river shore: the upper ones open onto the gallery, the lower ones onto the brewery floor. A stone stair from the square comes down past the outhouse at X -210, Y -49. Locked attic door at X -187, Y -53. Nearest waypoint: Reithwin Town (X -78, Y -46). The Road to Baldur''s Gate waypoint (X -263, Y -37) lies past the footbridge north-west of the building.'
curse: deep
items:
- id: madelines-ledger
  name: 'Madeline''s Ledger'
  for: any
  core: false
  where: 'Behind the bar, under loose floorboards (X -224, Y -77).'
  how: 'Perception 10 reveals the planks.'
  note: 'Quest item for Punish the Wicked: Madeline''s reports to Dark Justiciar Netasha. Take it to He Who Was on the Ruined Battlefield (X 126, Y 105).'
- id: worn-key
  name: Worn Key
  for: any
  core: false
  where: 'On Thisobald''s remains.'
  how: 'Loot the gore after he bursts or dies.'
  note: 'Opens the metal door at the end of the bar into the backroom laboratory.'
- id: research-notes
  name: Research Notes
  wiki: 'Research Notes (Waning Moon)'
  for: any
  core: false
  where: 'Workbench in the middle of the backroom lab (X -257, Y -83).'
  how: 'Through the Worn Key door. Interacting starts a voiceover. Pass the Intelligence 14 at the end (the location page calls it Investigation) to mark the stash on the map.'
  note: 'Thisobald''s purple worm poison, one ingredient short: corpse rose petals, hidden by a courier at a covert spot. Passing the check marks the Brewer''s Alchemist stash. Failing it means Survival 21 to find the dirt mound instead.'
- id: thisobalds-brewed-up-bellyglummer
  name: 'Thisobald''s Brewed-Up Bellyglummer'
  for: any
  core: false
  where: 'Crafted. Corpse Rose x4 in the Brewer''s Alchemist stash: a dirt mound in the small barn at X -248, Y -4, under the house behind three stacked barrels. Another Corpse Rose grows by a grave at X -142, Y 57 in the graveyard.'
  how: 'Dig the mound (marked by the Research Notes check, else Survival 21). Grind three Corpse Roses into Salts of Corpse Rose and combine with any Suspension.'
  note: 'Very rare weapon coating, bonus action, 10 turns: each hit forces CON 17 or Poisoned (disadvantage on attack rolls and ability checks, 1d6 Poison at the end of its next turn). Damage once per turn. No Inoculated on a save, so it can be reapplied. Bonbon''s bow before a boss that must miss. First craft: Criminal and Guild Artisan inspirations.'
- id: purple-worm-gullet
  name: Purple Worm Gullet
  for: any
  core: false
  where: 'Three pieces around the backroom lab.'
  how: 'Loot the lab.'
  note: 'Combine three into a Suspension of Purple Worm Slime. That unlocks the Purple Worm Toxin recipe and serves as the Suspension for the Bellyglummer.'
- id: punch-drunk-bastard
  name: Punch-Drunk Bastard
  for: any
  core: false
  where: 'Backroom lab, locked chest at X -259, Y -92 next to the trapped cage door. The treatise On Serpent Venom Toxin is in the same chest.'
  how: 'Sleight of Hand 10.'
  note: 'Rare +1 greatclub. While Drunk: advantage on all attack rolls and a 1d4 Thunder blast (3 m) on each melee hit. Nobody in the party uses two-handers; sell (190 gp).'
- id: rat-bat
  name: Rat Bat
  for: any
  core: false
  where: 'Leaning against the bar near Thisobald (X -224, Y -78).'
  how: 'Pick it up.'
  note: 'Rare +1 greatclub, hidden +1d6 Piercing, advantage against beasts. Sell (190 gp).'
- id: ichorous-gloves
  name: Ichorous Gloves
  for: any
  core: false
  where: 'Locked chest in the storeroom behind the bar (X -253, Y -67), with alchemy ingredients.'
  how: 'Sleight of Hand 10.'
  note: 'Uncommon gloves: Acid damage also inflicts Noxious Fumes, once per turn. No acid in this party; sell.'
- id: potion-of-angelic-slumber
  name: Potion of Angelic Slumber
  for: any
  core: false
  where: 'Rustic chest downstairs at X -208, Y -90.'
  how: 'Open the chest.'
  note: 'Consumable. Keep it for a long fight day.'
- id: key-the-waning-moon
  name: Key
  wiki: 'Key (The Waning Moon)'
  for: any
  core: false
  where: 'On a towel by the outhouse at X -210, Y -49 (the skeleton inside has an Antidote). A second copy lies on a broken cupboard inside the attic (X -190, Y -87).'
  how: 'Pick it up.'
  note: 'Opens the attic door at X -187, Y -53 from either side.'
- id: the-waning-moon-consignments
  name: 'The Waning Moon: Consignments'
  for: any
  core: false
  where: 'Table in the backroom lab (X -261, Y -91), with several potions.'
  how: 'Through the Worn Key door.'
  note: 'Thisobald''s diary. He got the Mason drunk on truth serum and reported his Selûnite heresy to Ketheric, put a blackmailer who dosed him with his own serum into a barrel, and guessed at Ketheric''s immortality. Read it before the storage cage: the barrels there hold a woman''s bones and the party comments change.'
quests:
- name: Punish the Wicked
  steps: |-
    - He Who Was (Ruined Battlefield, X 126, Y 105) wants Madeline's Ledger. It is under the loose planks behind the bar (Perception 10, X -224, Y -77).
    - Leaving the building with the quest active, the white Raven appears, reminds you, and teleports off.
    - Back at He Who Was, he channels Madeline. Bonbon: [BARD][PERSUASION] "Yours is a classic tale of cowardice" DC 10, or the plain "Pathetic, you're a coward" Persuasion 10. Either satisfies him.
    - **Charles must not speak here.** Forgiving Madeline, stopping her stabbing, or attacking He Who Was before the ritual breaks the Oath of Vengeance. Making her stab twice enrages He Who Was into a fight.
  outcome: 'Raven Gloves (rare: summon Quothe the Raven, Blinds with its beak, once per short rest). Failed rolls still pay a lesser reward.'
  lockout: 'Forgiving her, or a second stab: no gloves and a fight. Leaving the Shadow-Cursed Lands closes it.'
- name: 'Find Ketheric Thorm''s Relic'
  steps: |-
    - Survive all three drinking rounds. On the third drink Thisobald rants about "her cage", buried in the Thorm tomb, and the quest starts (or updates if Z'rell already gave it).
    - After the first story you can ask who placed the curse and how he became what he is. After the second: how the Thorms sustain the shadows, what he knows of Ketheric, and how to defeat him.
  outcome: 'Points at the Grand Mausoleum and the Gauntlet of Shar (Reithwin Town page for the plaque puzzle).'
- name: Lift the Shadow Curse
  steps: |-
    - The wiki lists this quest for the building. The drinking-round questions cover who cursed the land and the Thorms' part in it. No objective moves here; verify in game.
  outcome: 'Lore only.'
- name: Investigate the Selûnite Resistance
  steps: |-
    - The Waning Moon: Consignments in the backroom lab records how Thisobald exposed the Mason to Ketheric. The quest itself runs through the Mason's Guild (its page). Verify in game whether the journal updates.
  outcome: 'Lore for the resistance thread.'
lockouts:
- what: 'Taking the road west of the Waning Moon after Ketheric is dead'
  closes: 'Act 2 and every Act 1 map. Halsin leaves for good if Lift the Shadow Curse is unresolved.'
  avoid: |-
    Settle these first. The game warns once before you cross.
    - **Halsin**: Thaniel and Oliver reunited, Ketheric dead.
    - **Barcus**: tell him about Wulbren.
    - **Rolan**: speak to him at the inn after Ketheric.
    - **Arabella**: told about her parents, at camp.
    - **Dolly**: freed from the Moonlantern (ring the bell once, never twice).
    - Charles's Stone respec at Withers and the Tiefling rewards, per the route.
- what: 'Crossing the footbridge north-west of the distillery before Ketheric is dead'
  closes: 'The rest of Act 2 until you break out: the Absolute''s camp beyond arrests the party into the Moonrise prison'
  avoid: |-
    Stop at the barn (X -248, Y -4). The stash is on this side of the footbridge.
- what: 'Refusing Thisobald''s drink or failing a Sleight of Hand roll'
  closes: 'The peaceful kill and its inspirations; no loot is lost'
  avoid: |-
    Send one talker in alone and mime the drinks with Asterion (Rogue lines, see NPCs). A failed Constitution save is safer than a failed mime: he attacks only on the third failed save.
npcs:
- name: Thisobald Thorm
  role: Boss (drinking contest)
  note: 'Stands at the bar; the first party member to reach mid-floor sits down and the contest starts. Three rounds, each: drink (Constitution save 14, 16, 18; or mime with Sleight of Hand 18, 18, 21; Rogue mime lines 16, 16, 18), then a story (Performance 16 to 21, Bards with advantage; a failed story gets one Deception 18 retry), then questions. Refusing a drink, failing a mime, or failing the story retry starts the fight. One failed save: Drunk until long rest (disadvantage on DEX and CHA checks). Two: Poisoned. Three: Unconscious 10 turns and he attacks. He bursts on the third drink. Same XP as killing him and the four zombies. Send Asterion: Rogue mime lines with Expertise, and the DC 16 stories (the Arcane Tower, the Underdark fortress, the hag, the phase spider, the bulette, Grym). A Hexblade line gives Charles Persuasion 16 in place of the first story.'
- name: Thisobald Thorm (the fight)
  role: Boss stats
  note: 'Large undead, 288 HP, AC 16. Numb: immune to Slashing, Piercing, Bludgeoning and Thunder. Roaring Belch. Extra Attack. Asterion''s fists and Bonbon''s arrows do nothing; Gale''s fire and Charles''s Shadow Blade (Psychic) and smites do the work. The four Blighted zombies (Actor, Barman, Patron, Troubador) shamble in from the floor and the gallery.'
- name: Raven
  role: 'He Who Was''s messenger'
  note: 'Appears outside once you leave with Punish the Wicked active. Reminder only.'
- name: 'Ch''r''ai Tska''an'
  role: Ambush (conditional)
  note: 'Githyanki raid at the footbridge north-west of the building, only if Vlaakith marked the party for death. The Qua''nith Psionic Detector rings here first. Drops and tactics on the Reithwin Town page.'
checks:
- what: 'Loose planks behind the bar (X -224, Y -77)'
  note: 'Perception 10. Madeline''s Ledger.'
- what: 'Trapped cage door to the storage nook (X -258, Y -96)'
  note: 'Perception 15 to see the trap, Sleight of Hand 14 to disarm, Sleight of Hand 5 to pick. Three rustic chests of alchemy ingredients inside, with Yellow Musk Creeper Petals (unlocks Potion of Superior Healing). Barrels in the far corner hold a woman''s skeleton.'
- what: 'Buried chests'
  note: 'Survival 18 at X -183, Y -51; Survival 10 at X -159, Y -113; Survival 16 at X -238, Y -87.'
- what: 'Brewer''s Alchemist stash, barn at X -248, Y -4'
  note: 'Dirt mound. Free if the Research Notes check passed, else Survival 21.'
- what: 'Message board in the front yard (X -182, Y -60)'
  note: 'Missing-pet notices; pairs with the heap of collars behind the Tollhouse. Banter only.'
tips: |-
  Wine and beer here are untouched by the curse and count as camp supplies.

  Chests at X -197, Y -89 (rustic), X -219, Y -86 and X -218, Y -45 (wooden) hold alchemy ingredients.

  If you would rather roll Performance with advantage, Bonbon can be the drinker instead: Constitution 14, 16, 18 flat. One failed save puts her Performance at disadvantage for the rest of the contest, which cancels the Bard advantage.
---
