---
slug: mountain-pass
name: 'Mountain Pass & Rosymorn Monastery'
act: 1
order: 10
region: Mountain Pass
wiki: Mountain Pass
summary: 'The overland road to the Shadow-Cursed Lands. Lady Esther''s shop, the Holy Lance Helm, the Dawnmaster''s Crest puzzle and the Blood of Lathander, with Crèche Y''llek underneath.'
arrive: |-
  From the Risen Road, west of Waukeen's Rest, at about X: -86 Y: 550. The road west at X: -146 Y: 569 crosses into the Rosymorn Monastery Trail (arrive at X: -48 Y: -183). The Goblin Camp has a second entrance at X: -160 Y: 332 that skips the githyanki patrol.

  From Act 2, walk out of the Ruined Battlefield at X: -142 Y: -127 into the trail, or fast travel to the Trielta Crags waypoint (X: -62 Y: -146). The Rosymorn Monastery waypoint is at X: 17 Y: 23. Closed for good once you enter the Shadowfell.
curse: none
items:
- id: holy-lance-helm
  name: Holy Lance Helm
  for: Charles
  core: true
  where: 'Painted chest on the monastery roof, east side, X: 120 Y: 35. Reach it from the eagle nest by a few jumps east.'
  how: 'Climb the Knotted Roots at X: 57 Y: 52 to the roof and jump east past the nest. Placate the eagles first (see the eagle entry) or the jumps happen mid-fight.'
  note: 'Charles''s Act 2 head. When an attack misses him, Smite the Graceless deals Radiant: that fires a Luminous shockwave and refills Arcane Acuity on enemy turns. Needs Medium Armour (Hexblade). +1 Constitution saves.'
- id: graceful-cloth
  name: Graceful Cloth
  wiki: The Graceful Cloth
  for: Asterion
  core: true
  where: 'Lady Esther''s camp, X: -43 Y: -129, east and downhill from the Trielta Crags waypoint.'
  how: 'Buy. Base price 800 gp. She trades whether or not you take her egg quest.'
  note: '+2 DEX (cap 20) and Cat''s Grace (advantage on DEX checks, half fall damage), +1 DEX saves. Asterion''s chest until the Vest of Soul Rejuvenation; keep it bagged for theft afterwards. The +2 DEX does not stack with the Gloves of Dexterity.'
- id: gloves-of-cinder-and-sizzle
  name: Gloves of Cinder and Sizzle
  for: Asterion
  core: true
  where: 'Lady Esther''s camp, X: -43 Y: -129.'
  how: 'Buy. Base price 240 gp.'
  note: '+1d4 Fire per unarmed hit + a level-3 Scorching Ray 1/long rest. Prefer Sparkle Hands vs metal or fire resistance.'
- id: gloves-of-baneful-striking
  name: Gloves of Baneful Striking
  for: Charles
  core: true
  where: 'Lady Esther''s camp, X: -43 Y: -129.'
  how: 'Buy. Base price 90 gp.'
  note: 'Weapon hit → −1d4 to the target''s saves for 2 turns, helping Asterion''s Stun and the casters'' control. The wiki notes the penalty applies to all saves, not just the wearer''s next spell.'
- id: periapt-of-wound-closure
  name: Periapt of Wound Closure
  for: any
  core: false
  where: 'Lady Esther''s camp, X: -43 Y: -129.'
  how: 'Buy. Base price 125 gp.'
  note: 'Auto-stabilise when Downed + every heal on the wearer restores maximum. Only heals received by the wearer are maximised.'
- id: blood-of-lathander
  name: Blood of Lathander
  wiki: The Blood of Lathander
  for: any
  core: false
  where: 'Secret Chamber pedestal under the crèche, X: 1068 Y: -779. Entered from the west alcove of the Inquisitor''s Chamber in Crèche Y''llek.'
  how: |-
    - Get the Dawnmaster's Crest first (altar puzzle below).
    - In the Inquisitor's Chamber, turn the two Lathander statues at X: 1330 Y: -660: north statue east, south statue west. The south one is jammed: Grease it (a Grease Bottle lies behind the Lathander statue in the monastery hall) or pass a passive Athletics DC 25. W'wargaz does not stop you.
    - Corridor: three barriers, each fed by an Energy Source. Shoot the source (Magic Missile works without climbing). Dawnbreaker traps fire a cone that shoves 20 m into the chasm; turn-based mode starts by itself. Disarm each with Sleight of Hand DC 14 or stay out of the cone.
    - Put the crest in the pedestal slot BEFORE touching the mace. 145 XP, no trap.
  note: 'Rosymorn puzzle, Dawnmaster''s Crest. +3 mace with Sunbeam (level 6, 1/long rest) and a party self-revive-at-0-HP aura: Lathander''s Blessing, 1/long rest, 2d6 to the wielder and 1d6 to allies within 9 m. Don''t miss it. Lathander''s Light (6 m) blinds fiends and undead (CON DC 14), dispels the shadow curse like a torch, and counts as illumination for the Callous Glow Ring.'
- id: dawnmasters-crest
  name: 'Dawnmaster''s Crest'
  for: any
  core: false
  where: 'Dawnmasters'' Memorial, upper level, X: 75 Y: 57. Hidden compartment in the wall opens when the four altars are filled.'
  how: |-
    - Longsword is already on Welkinglory's altar (north-west).
    - Drop or throw a battleaxe on Vaseid (south-west), a warhammer on Seed (north-east), a mace on Stockhold (south-east). Any weapon of the right type works, not just the Ceremonial ones. A wrong type bounces back and can knock you Prone.
    - Solving it gives the whole party Morninglord's Radiance (+1d4 Radiant on weapon attacks until long rest).
    - Bypass: passive Perception DC 10 reveals the compartment, Sleight of Hand DC 30 opens it. That loses the Radiance buff.
  note: 'Disarms the Blood of Lathander trap. Without it the vault self-destructs and takes the crèche with it.'
- id: ceremonial-mace
  name: Ceremonial Mace
  for: any
  core: false
  where: 'Firewine storage, ground floor, on a drunk Kobold (about X: 40 Y: 28). Enter through the broken window at X: 64 Y: 31 west of the main doors.'
  how: 'Kill or pickpocket the kobold. Many kobolds are passed out with Firewine Belly; some hide in barrels that weigh 10 instead of 40. The Rusty Mace in Dawnmaster Stockhold''s grave (X: 123 Y: -6) also fits the altar.'
  note: '+1 mace. Puzzle piece for Stockhold''s altar. Picking it up starts Find the Blood of Lathander.'
- id: ceremonial-battleaxe
  name: Ceremonial Battleaxe
  for: any
  core: false
  where: 'Guardian of Faith room, upper level east. Crumbling Wall at X: 103 Y: 38 (Perception DC 15), or the enchanted door at X: 95 Y: 46 (Sleight of Hand DC 15), or smash the wall at X: 106 Y: 38.'
  how: 'The axe lies at the Guardian''s feet. Picking it up (or looting the skeletons under it) makes the Guardian attack. Looting the Gilded Chest and the seated skeleton is free. Leave by the wall breach; the door carries Morninglord''s Bulwark.'
  note: '+1 battleaxe. Puzzle piece for Vaseid''s altar. Any battleaxe works instead; Witchbreaker from Jeera is one.'
- id: ceremonial-warhammer
  name: Ceremonial Warhammer
  for: any
  core: false
  where: 'Bottom of the eagle nest on the roof, X: 79 Y: 39.'
  how: 'Placating the eagles does not cover the nest itself; stepping in starts the fight. Options: fight (the Ancient Giant Eagle calls 3 to 5 more eagles), or Fog Cloud / Darkness plus Invisibility to grab it unseen. Any warhammer works; Skybreaker does not (light hammer).'
  note: '+1 warhammer. Puzzle piece for Seed''s altar.'
- id: key-rosymorn-monastery
  name: Key (Rosymorn Monastery)
  for: any
  core: false
  where: 'Raider Add''ath, one of the two githyanki at the monastery gate.'
  how: 'Kill her in the gate cutscene fight. Opens the main gates at X: 74 Y: 45. The lever at X: 78 Y: 49 inside does the same.'
  note: 'Only matters if you let the githyanki lock the gate.'
- id: elaborate-slate
  name: Elaborate Slate
  for: any
  core: false
  where: 'Sarth Baretha, leader of the githyanki patrol at X: -101 Y: 555.'
  how: 'Loot or pickpocket. Arcana DC 10 to read; Lae''zel reads it free. The patrol leaves after a peaceful talk, so this needs the fight.'
  note: 'Marks the crèche on the map. Not needed if you already know where it is. Baretha also carries a Githyanki Greatsword, Githyanki Half Plate, an Elixir of Hill Giant Strength and a Potion of Invisibility if unused.'
- id: silver-sword-of-the-astral-plane
  name: Silver Sword of the Astral Plane
  for: any
  core: false
  where: 'Kith''rak Voss, at the patrol.'
  how: 'Disarm him before the dialogue triggers (from about X: -139 Y: 561): Command (Drop), Heat Metal, Disarming Attack. He locks you into dialogue on approach and flies off at the first hostile act. His saves are high; expect reloads.'
  note: 'Legendary +3 greatsword. Nobody in this party swings a two-hander, so this is a 1300 gp base sale or a skip. Otherwise it comes from Voss in Act 3.'
  verify: true
- id: scroll-of-revivify
  name: Scroll of Revivify
  for: any
  core: false
  where: 'Small room above the Dawnmasters'' Memorial, behind an Iron Gate. Climb the Knotted Roots at the end of the balcony outside the memorial (Dirt Mound at X: 80 Y: 86 on the way).'
  how: 'Sleight of Hand DC 14. An Opulent Chest sits in the same room.'
  note: 'Useful if a Repulsion Mine on the crags pushes someone into the chasm.'
- id: greater-elixir-of-arcane-cultivation
  name: Greater Elixir of Arcane Cultivation
  for: any
  core: false
  where: 'Broken Lathander effigy at the cable-car landing, X: -17 Y: 23, among the pilgrims'' donations.'
  how: 'Pick up. A Potion of Greater Healing and gold lie with it.'
  note: 'Extra level 2 spell slot until long rest. Save it for a hard fight day.'
quests:
- name: Travel through the Mountain Pass
  steps: |-
    - Sub-quest of Travel to Moonrise Towers. Halsin gives it after the Grove is saved; he recommends the Underdark but both routes are open and you can do both before the Shadowfell.
    - Walk west from the Mountain Pass into the trail. At the Trielta Crags fork take the west road: two Death Shepherds, a Ghast and four Ghouls at X: -91 Y: -119 attack on sight and cannot be skipped. Kill the Death Shepherds first; they raise the dead.
    - Continue west then south to the Shadow-Cursed Lands entrance at X: -143 Y: -129.
  outcome: 'Completes when you set foot in the Shadow-Cursed Lands. The Grymforge lift completes it the same way.'
  lockout: 'Crossing at X: -146 Y: 569 auto-resolves Save the Refugees and other Wilderness quests. Entering the Shadow-Cursed Lands starts Act 2.'
- name: Find the Githyanki Crèche
  steps: |-
    - Zorru in the Grove points here. The patrol stands at X: -101 Y: 555 as you approach from the Risen Road; a red dragon burns the Flaming Fists first (WIS save DC 15 or Frightened).
    - Talk to Kith'rak Voss (paths under his npcs entry). Peaceful or not, he leaves on the dragon and sends you to the crèche in Rosymorn Monastery.
    - If it turns into a fight, Baretha's Elaborate Slate marks the crèche.
    - Continue in Crèche Y'llek: the Zaith'isk in the infirmary.
  outcome: 'Progresses. Ends at the Zaith''isk in the crèche.'
- name: Steal a Githyanki Egg
  steps: |-
    - Lady Esther at X: -43 Y: -129. Agree to fetch an egg. Persuasion DC 21 gets 466 gp up front (only Bonbon should roll this).
    - The egg is in the crèche Hatchery (see that page). Bring it back here.
    - Hand-in options: the real egg (449 gp); an Owlbear Egg from the Wilderness with Nature, Deception or Persuasion DC 21 (485 gp on the Persuasion line, and the trick works even with the egg in the camp chest); keep the egg for 1000 gp from Havkelaag in Act 3 or Lae'zel's epilogue.
    - You can also cheat her on first meeting with the Owlbear Egg and skip the crèche part entirely.
  outcome: 'Gold. The real egg has an Act 3 cost: Ptaris hatches, kills Esther and the Society of Brilliance including Omeluum, and Retrieve Omeluum never appears. The owlbear swap has no downside.'
  lockout: 'Kicking the egg over the cliff (Dark Urge option) breaks Charles''s oath and turns Esther hostile. Refusing to hand over after taking the advance turns her hostile.'
- name: 'Help Kith''rak Voss'
  steps: |-
    - Not startable here. Voss only sets it up: the Mountain Pass talk is his first appearance. After the Vlaakith audience in the crèche he visits camp on the next long rest or fast travel and asks you to meet him at Sharess' Caress in Act 3.
    - Let him talk. If Lae'zel attacks him at camp the Act 3 quest and the Silver Sword reward are gone.
  outcome: 'Act 3: Silver Sword of the Astral Plane for showing him the Orphic Hammer.'
- name: Find the Blood of Lathander
  steps: |-
    - Starts when you pick up any Ceremonial weapon or read the plaque under the Lathander statue.
    - Collect a mace, a battleaxe and a warhammer (items above), place them in the Dawnmasters' Memorial, take the crest and read the Note to the Next Dawnmaster.
    - Enter the crèche, open the statue passage in the Inquisitor's Chamber, clear the corridor, place the crest, take the mace.
  outcome: 'The Blood of Lathander, safe, crèche intact.'
  lockout: 'Taking the mace without the crest starts a four-turn self-destruct that levels the monastery and the crèche.'
- name: 'Reclaim the Blue Jay''s Nest'
  steps: |-
    - Blue Jay at X: -59 Y: -19 on the path between the cable-car stops. Needs Speak with Animals. He wants the giant eagles off the roof.
    - Kill both eagles (non-lethal also works; the jay finishes them).
    - Report back. He marks Blue Jay's Find at X: -6 Y: -29.
  outcome: '10 XP and a buried chest of low-value loot. Survival DC 25 or digging at the spot finds it without the quest. If the eagles die before you talk to him, he vanishes and leaves the key to the stash in his nest.'
- name: The Wizard of Waterdeep
  steps: |-
    - The Weary Traveller stops you at X: -133 Y: -161 on the trail north of the undead fight, if you have not met him in the Shadow-Cursed Lands yet. The talk starts on its own and needs Gale in the party.
  outcome: 'Progresses Gale''s companion quest.'
lockouts:
- what: 'Walking west at X: -146 Y: 569 into the Rosymorn Monastery Trail'
  closes: 'Auto-resolves Save the Refugees, Raid the Emerald Grove, Hunt the Devil, Rescue the Druid Halsin, Rescue the Gnome, Rescue the Grand Duke, Save the Goblin Sazza and Save the First Druid'
  avoid: 'Finish the Wilderness first. The game warns before the crossing. The Grove itself and the rest of Act 1 stay open until the Shadowfell.'
- what: 'Entering the Shadowfell at the bottom of the Gauntlet of Shar'
  closes: 'The whole Act 1 map: this pass, the monastery, the crèche and Esther'
  avoid: 'The route does the crèche first (stops 1 and 2), long before the Gauntlet. Do not free the Nightsong with anything here undone.'
- what: 'Failing Voss''s interrogation, or showing him the artefact, or letting him read a tadpole in your head'
  closes: 'Peaceful passage; the patrol attacks'
  avoid: |-
    - Bonbon talks, not Charles: Persuasion DC 15, then Arcana DC 10 to spot Detect Thoughts and WIS DC 10 to resist, then Persuasion DC 15. A Warlock or Sorcerer skips the Arcana check and resists at DC 5.
    - With Lae'zel in the party: nod to her, then Persuasion DC 10 'play along'. Anything else turns them hostile.
    - Never produce the artefact and never say you are infected.
    - The fight is winnable at level 5+ and drops the slate and githyanki gear, so a failure costs little.
- what: 'Leaving Lae''zel alone at the patrol'
  closes: 'Lae''zel dies if she runs to Voss and the party walks away'
  avoid: 'Follow her when she breaks off, or leave her in camp for this visit.'
- what: 'Camp confrontation after the patrol: Shadowheart holds a knife to Lae''zel'
  closes: 'One of the two companions, permanently'
  avoid: 'On the long rest after meeting the patrol, wake up and pass Persuasion DC 10. Defending Lae''zel by force makes Shadowheart hostile; doing nothing kills Lae''zel.'
- what: 'Handing Esther the real egg'
  closes: 'Retrieve Omeluum in Act 3; Omeluum, Esther and Havkelaag die to Ptaris'
  avoid: 'Give her the Owlbear Egg with a DC 21 check, or keep the githyanki egg.'
- what: 'Dark Urge egg kick in front of Esther, or telling her the egg is destroyed, or refusing after her advance'
  closes: 'Esther as a vendor; Charles''s oath on the kick'
  avoid: 'Buy all four plan items before you touch the egg dialogue. Never pick the kick line with Charles.'
- what: 'Opening the crest compartment with Sleight of Hand DC 30 instead of the puzzle'
  closes: 'Morninglord''s Radiance for the party (+1d4 Radiant weapon damage until long rest)'
  avoid: 'Do the puzzle. The buff is once per run and cannot be regained. Voss''s camp visit forces a long rest that clears it anyway, so use it the same day.'
- what: 'Taking the Blood of Lathander without the crest in the slot'
  closes: 'Crèche Y''llek and everything left in it if the Lance fires: Jeera''s stock, the Zaith''isk, the egg, the Inquisitor''s Chamber loot. The crèche turns hostile the moment the trap trips'
  avoid: |-
    - Crest first, slot first, mace second.
    - If it trips anyway: four turns. The mace-taker is caged behind a forcefield (Misty Step or Dimension Door out, or shoot the Energy Source under the pedestal at X: 1063 Y: -788). A portal behind the pedestal goes to the roof. Placing the crest after the fact also stops the Lance but closes the portal, so whoever stays to place it walks out alone.
    - Destroying the four Lathander Solar Machines also saves the crèche.
- what: 'Letting the githyanki at the gate walk in with the cultists'
  closes: 'The main doors, until the lever at X: 78 Y: 49 inside'
  avoid: 'Attack them in the cutscene prompt to keep the gate open, or enter by the broken window at X: 64 Y: 31 or the Knotted Roots above the waypoint.'
npcs:
- name: 'Kith''rak Voss'
  role: Boss (dialogue only)
  note: 'Githyanki knight on the red dragon Qudenos, at the patrol. He never fights here; hostile action makes him fly off and the patrol attacks. Talk paths are in the lockout above. Charles has an Oath of Vengeance line (Persuasion DC 15) and, as a Warlock, skips the Arcana check. Disarming him before dialogue drops the Silver Sword of the Astral Plane. He returns to camp after the crèche.'
- name: Sarth Baretha and the githyanki patrol
  role: Enemies (optional)
  note: 'Baretha (Fighter, Disarming Attack, Action Surge), Raiders Chost and Zastri, Gish For''reth. They fight only if the Voss talk fails. Loot: Elaborate Slate, Githyanki Greatsword, Githyanki Half Plate, Githyanki Longsword +1, Githyanki Crossbow, potions. Soldier background earns Conquer the Conquerors for killing them.'
- name: Ellyka
  role: Tiefling scout
  note: 'Crouched at X: -116 Y: 552 watching the patrol. Refuses to join. Her corpse turns up in the crèche prison.'
- name: Lady Esther
  role: Vendor and quest-giver
  note: 'Camp at X: -43 Y: -129. Sells the Graceful Cloth (800 base), Gloves of Cinder and Sizzle (240), Gloves of Baneful Striking (90), Periapt of Wound Closure (125), plus Boots of Elemental Momentum, Cacophony, Hoppy, Winter''s Clutches, Arrows of Undead Slaying and Aberration Slaying. Trades regardless of the egg quest. Battle Master 5 with Extra Attack and Menacing Attack; if she turns hostile she can drop a party member in one turn. She stays put even if the monastery blows up.'
- name: Blue Jay
  role: Quest-giver (Speak with Animals)
  note: 'X: -59 Y: -19 over a nest with a key. Wants the eagles gone. Reward: the location of a buried chest at X: -6 Y: -29.'
- name: Weary Traveller
  role: 'Gale''s quest'
  note: 'X: -133 Y: -161, north of the undead fight. Auto-dialogue that advances The Wizard of Waterdeep if not already met in Act 2.'
- name: 'Raider Add''ath and Warrior Ith''dul'
  role: Gate githyanki
  note: 'Herd three halfling cultists into the crèche and shoot Corliss in the back. Attack via the prompt to keep the gate open. Add''ath carries the Key (Rosymorn Monastery). They reappear at Jeera''s trade post inside if left alive.'
- name: Ancient Giant Eagle
  role: Roof guardian
  note: 'Nest at X: 79 Y: 39 with her son Xavier. Approach with Animal Handling DC 18, or with Speak with Animals active pass Persuasion DC 15 ("I''m just interested in the big device"). Either lets you explore the whole roof, but not step into the nest. In combat she uses Gale (knockback + Prone on a roof with chasm edges) and Cry for Help brings 3 to 5 more eagles. Drops Eagle Feathers.'
- name: Kobold Looters, Scouts and Inventor
  role: Firewine storage
  note: 'Nine looters, four scouts and an inventor at X: 45 Y: 37, most drunk on Firewine. Some hide in barrels (listen for *Gulp*; a barrel weighing 10 has one inside). One scout holds the Ceremonial Mace. Sneak past or clear them.'
- name: Gremishkas
  role: Ambush in the old library
  note: 'Nine invisible Gremishkas in the upper-level hall behind the doors at X: 54 Y: 41 (crying is audible). Arcana DC 15 recalls their Magic Allergy: spells cast near them provoke them. Fight with weapons. Their three nests hold random uncommon scrolls and potions.'
- name: Guardian of Faith
  role: Spell guardian
  note: 'Ancient Guardian of Faith spell in the sealed room at X: 103 Y: 38. Passive until you lift the Ceremonial Battleaxe or loot the skeletons under it. Grab the axe and jump back out through the breach.'
- name: Death Shepherds, Ghast, Ghouls
  role: Trail fight
  note: 'X: -91 Y: -119, on the only road to the Shadow-Cursed Lands. Death Shepherds raise fallen undead; kill them first. The Zealot corpse nearby answers Speak with Dead and carries a Missive From Moonrise. An Opulent Chest sits on the cart.'
checks:
- what: 'Buried chest at X: -73 Y: 539 (Mountain Pass)'
  note: 'Survival DC 20. Gold, a gem and a scroll.'
- what: 'Dragon claw grooves at X: -67 Y: 537'
  note: 'Arcana DC 10 warns of the dragon before the cutscene. Flavour.'
- what: 'Heavy chests on the ramparts and in the cart at the Mountain Pass chokepoint'
  note: 'Random arrows and grenades. Flaming Fist shield under the bridge wreck at X: -148 Y: 568; a pouch with an Amethyst and a Pearl under the road sign.'
- what: 'Repulsion Mines on the trail north of the Lathander statue and on the crags below the cable-car station'
  note: 'Perception DC 15 each. Zero damage, but the shove kills anyone next to a chasm.'
- what: 'Cable Car Wheel at X: -47 Y: -74'
  note: 'Strength DC 15, one try per character, to bring the car up. Otherwise take the stairs west and pick down the mined crags. An Elegant Chest left of the stairs has an uncommon arrow and a Potion of Greater Healing.'
- what: 'Dirt Mound at X: -119 Y: -138 near the undead fight'
  note: 'Survival DC 10. A chest.'
- what: 'Lathander statue plaque on the trail (X: -62 Y: -133) and at the gate'
  note: 'Religion DC 10 identifies the monastery as Lathander''s.'
- what: 'Iron Gates in the Gremishka hall and beside the Lathander statue downstairs'
  note: 'Sleight of Hand DC 14 each. Library gates: an uncommon scroll or potion plus The Parables of Dawnmaster Vaseid (the missing stained-glass panel: battleaxe). Statue gates: Potion of Mind Reading, Scroll of Gust of Wind and the Blood of Lathander history books.'
- what: 'Locked door at X: 36 Y: 35 in the library'
  note: 'Opulent Chest. The Record of Complaints on the shelf explains the Gremishkas; the bookstand has the Potion of Animal Speaking recipe.'
- what: 'Crumbling Wall at X: 103 Y: 38'
  note: 'Perception DC 15. Guardian of Faith room with the Ceremonial Battleaxe and a Gilded Chest. Old Maintenance Records by the double doors at X: 102 Y: 27 hint that the west statue in the vault is jammed.'
- what: 'Buried chests around the memorial balcony'
  note: 'Dirt Mound at X: 80 Y: 86 (any Perception). Wooden chests at X: 50 Y: 63 (Survival DC 10) and X: 47 Y: 56 (Survival DC 16).'
- what: 'Magic Mouth bust on the ruined east staircase'
  note: 'Arcana DC 15. It screams; nothing attacks.'
- what: 'Skeleton behind the Lathander statue'
  note: 'History DC 10: run through with a githyanki sword. The Inventory of Takings slate and, north of the statue, a Dirt Mound and the Account of the Establishment of Crèche Y''llek slate (names Therezzyn and W''wargaz).'
- what: 'Roof surface'
  note: 'Twisting Vines entangle anyone stepping on them. Ancient Githyanki Warrior skeleton at X: 46 Y: 20 has a Githyanki Slate. Wooden Trunk on the perch by the mural: Potion of Greater Healing and Potion of Healing; pouch under the tree at X: 99 Y: 19 has another.'
tips: |-
  **Order for one clean visit.** Esther first (buy all four plan items before any egg talk). Cable car or crags down. Gate fight to keep the doors open. Firewine storage for the mace, then the crack in the north wall up to the upper level. Guardian room for the axe. Roof: placate the eagles, jump east for the Holy Lance Helm, then deal with the nest for the warhammer. Memorial puzzle, crest, Note. Down the east staircase to the Lathander hall, pull the lever, take the spiral stairs west into the crèche. The vault is done from inside the crèche; the crèche page has the order there.

  **Levels.** The wiki's XP awards here are keyed to level 6. The route does this at about character level 7, so nothing here is dangerous except the roof edge and the Dawnbreakers.

  **Morninglord's Radiance** is +1d4 Radiant on every weapon attack for the rest of the day and fires the Gloves of Belligerent Skies. Solve the puzzle, then do the crèche fights before you long rest.
---
