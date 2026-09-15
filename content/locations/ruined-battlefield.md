---
slug: ruined-battlefield
name: Ruined Battlefield
act: 2
order: 50
region: Shadow-Cursed Lands
wiki: Ruined Battlefield
summary: 'The eastern half of the Shadow-Cursed Lands: Rolan''s rescue, the Shadow Mastiff Alpha for Asterion''s ring, the House in Deep Shadows for Gale''s ring, and the Harper ambush site.'
arrive: |-
  You are already on it: both region entrances (Grymforge gate X: 121 Y: 229, Monastery Trail path X: 167 Y: -28) open onto the battlefield. Waypoint: Shadowed Battlefield X: 46 Y: 17, mid-map. Last Light Inn is over the bridge at the north-west corner; Reithwin is across the stream to the west by three bridges (X: -59 Y: -80 main, X: -59 Y: -22 to the Mason's Guild, X: -59 Y: -112 wooden footbridge to the Tollhouse pier).

  One trip covers Rolan, the mastiffs and the house: inn to Shadowed Battlefield waypoint, east to the House in Deep Shadows, back west and south along the stream to the mastiff camp (X: -49 Y: 36), then on to Rolan at the south end (X: -52 Y: -110). Long rest after.
curse: light
items:
- id: shadow-cloaked-ring
  name: Shadow-Cloaked Ring
  for: Asterion
  core: true
  where: 'On the Shadow Mastiff Alpha''s corpse. It spawns in the fenced, torch-lit camp north of the ruined pottery, X: -49 Y: 36 (wiki also gives X: -39 Y: 37), beside True Soul Korliss''s body.'
  how: 'Destroy every everburning torch in the camp (Arcana DC 14 names them Continual Flame). Three Shadow Mastiffs and the Alpha appear and attack. Bring your own light: Shadowblend makes them invisible and Shadow Veil resists non-magical damage while they are obscured. Terrifying Howl is a WIS save vs Frightened; Shadowjaw Bite is 2d6+3 with a STR save vs Prone.'
  note: 'Shadow Mastiff Alpha at the Ruined Battlefield; destroy the everburning torches nearby to make it appear. +1d4 vs Lightly or Heavily Obscured or shadow creatures, on unarmed attacks too. Asterion''s Act 2 damage ring; it stays on for Charles''s Darkness in Act 3. Also boosts Throw attacks.'
- id: ring-of-mental-inhibition
  name: Ring of Mental Inhibition
  for: Gale
  core: true
  where: 'House in Deep Shadows, X: 68 Y: 36, just east of the Shadowed Battlefield waypoint. Locked wooden chest inside the house at X: 76 Y: 39.'
  how: 'Sleight of Hand DC 10. Entering the house starts Oliver''s hide-and-seek; loot the chest before or after, the chest does not care.'
  note: 'Locked chest in the House in Deep Shadows, east of the Shadowed Battlefield waypoint. A foe failing a save vs Gale''s spells gains Mental Fatigue for 2 turns. Swap in over Coruscation for control fights. Does not fire on saves to shake off an existing effect (Hold Person end-of-turn saves), nor on surface, cloud or wall spells. Wiki bug note: it also fires on allies who fail saves against Gale.'
- id: ring-of-shadows
  name: Ring of Shadows
  for: any
  core: false
  where: 'Oliver, House in Deep Shadows X: 76 Y: 37.'
  how: 'Play both rounds of his hide-and-seek; win or lose, he hands it over. Round two summons Mummy, Daddy and Doggy (Wraiths) who hunt the party while you look for him; turn-based mode starts and everyone hides. Send Asterion alone. If the Wraiths spot you, kill them and Oliver still pays out as "second prize". Pickpocketing it mid-round swaps the reward for a plain silver band.'
  note: 'Uncommon. Pass Without Trace once per long rest (+10 Stealth to the group). Cast it and unequip; the effect stays. Good for the stealth openers in the party gameplan.'
- id: penumbral-armour
  name: Penumbral Armour
  for: any
  core: false
  where: 'Locked opulent chest in the abandoned mansion east of Last Light Inn, X: 33 Y: 145. The only path is from the inn''s inner yard at X: -10 Y: 166 (signposted). Deep curse inside: torches and Isobel''s blessing fail here; Moonlantern or Pixie Blessing only.'
  how: 'Sleight of Hand DC 16. A DC 10 Survival buried treasure sits by the far entrance at X: 26 Y: 170. Two skeletons on the bed each hold a Gold Ring. The root breach in the big room drops into the Last Light cellar; do not use it before you have entered the inn by the bridge or the whole inn turns hostile.'
  note: 'Rare light armour, AC 12 + DEX, +3 Stealth while obscured. Not plan gear (Asterion wears Graceful Cloth), sell or bag it.'
- id: ring-of-twilight
  name: Ring of Twilight
  for: any
  core: false
  where: 'Round tower south of the pottery along the riverbank, X: -34 Y: -12. Locked traveller''s chest under the pottery shelf.'
  how: 'An armed tripwire crosses the door. The Key (Old Pottery) is in the conic vase on the shelf above the chest, or Sleight of Hand DC 10.'
  note: 'Rare. +1 AC while obscured. Situational; Asterion could wear it in Darkness fights but the plan rings are better.'
- id: gloomstrand-shield
  name: Gloomstrand Shield
  for: any
  core: false
  where: 'Larger of two locked traveller''s chests on the wooden pier past Rolan''s fight, X: -60 Y: -114, next to the half-ruined footbridge to the Tollhouse.'
  how: 'Sleight of Hand DC 10 each, or the Key (Reithwin Tollhouse). The smaller chest is random loot.'
  note: 'Uncommon +2 shield, +1 Stealth. Spare. Charles''s shield line is +2 Shield, Adamantine, Walking Fortress.'
- id: hammergrim-mist-amulet
  name: Hammergrim Mist Amulet
  for: any
  core: false
  where: 'Locked chest inside the Harper ambush house, X: -12 Y: -7, east of the Tollhouse.'
  how: 'Sleight of Hand DC 10, or the Key (Harpers'' Ambush) beside the skeleton on the house roof at X: -5 Y: -1.'
  note: 'Uncommon. Fog Cloud (level 1) once per long rest, no concentration. A free obscurement for Asterion''s ring or an escape.'
- id: thermoarcanic-gloves
  name: Thermoarcanic Gloves
  for: any
  core: false
  where: 'Worn by Kansif: the cultist camp at X: 87 Y: -49, or his corpse after the Harper ambush.'
  how: 'Kill him in the ambush. The talk-down sends him into the curse with the gloves; he reappears as a Shadow-Cursed Undead in Reithwin south of Ketheric''s statue and can be killed there.'
  note: 'Uncommon. 2 turns of Heat whenever the wearer deals Fire damage, once per attack; Scorching Ray counts each ray. Gale''s gloves slot is Belligerent Skies, so this is a bag item or a sell.'
- id: cruel-sting
  name: Cruel Sting
  for: any
  core: false
  where: 'Kar''niss''s corpse at the ambush house, X: 10 Y: -20 (weapon listed at X: 0 Y: -15).'
  how: 'Kill him. The talk-down keeps the sword on him; find the undead convoy in Reithwin later.'
  note: 'Rare +1 longsword with Ensnaring Strands (short rest). The +1d4 Poison vs Restrained needs a drow wielder. Fresh off his corpse it keeps Spindleweb Fanatic (+1d6 Psychic) until a long rest. Nobody in the plan swings a longsword.'
- id: luminous-gloves
  name: Luminous Gloves
  for: any
  core: false
  where: 'Potter''s Chest on the wall of the ruined pottery, X: -52 Y: 11.'
  how: 'Four Meazels ambush in the pottery (Perception DC 18 spots them). Then Sleight of Hand DC 14, or the Potter''s Chest Key behind a movable brick (Perception DC 10 near X: -34 Y: 13). The chest also holds an Idol of Selûne and the note that starts Investigate the Selûnite Resistance.'
  note: 'Uncommon. Radiant damage applies 2 turns of Radiating Orb; +1 STR saves. Charles''s hands are taken by Battlemage''s Power, and Luminous Armour already does this job.'
- id: ring-of-self-immolation
  name: Ring of Self Immolation
  for: any
  core: false
  where: 'Locked wooden chest on the platform of the tower north of the Shambling Mound ambush, X: 29 Y: 63.'
  how: 'The key lies by the skeleton with the Ragged Diary on the second floor at X: 28 Y: 53, or pick the lock.'
  note: 'Uncommon. Self Immolation: set yourself on fire for Heat, short rest. Gale has Draconic fire already; sell.'
- id: frost-prince
  name: Frost Prince
  for: any
  core: false
  where: 'Gilded chest at X: 88 Y: -95, south-east, the bait for a blight ambush.'
  how: 'Three Needle Blights and three Vine Blights spring when you open it. Fire clears blights fast.'
  note: 'Uncommon amulet. Ice Knife (level 1) once per long rest. Sell.'
- id: ironwood-club
  name: Ironwood Club
  for: any
  core: false
  where: 'Shadow-Cursed Shambling Mound corpse at the ambush X: 42 Y: 58.'
  how: 'Perception DC 30 to spot the ambush; assume you will not. Six Needle Blights, two Vine Blights, two cursed Harpers and the Mound. Kill the Mound; it resists Cold, Fire and Necrotic.'
  note: 'Uncommon +1 club, +1d4 with Shillelagh. Halsin fodder or a sell.'
- id: family-ring
  name: Family Ring
  for: any
  core: false
  where: 'Animal burrow on a rocky ledge below Ellie May''s grave and the graverobber''s camp, X: 108 Y: 128.'
  how: 'Two Perception DC 10 checks from the grave follow beast tracks to the burrow.'
  note: 'Uncommon. +2 Death Saving Throws. Sell.'
- id: dark-justiciar-mask
  name: Dark Justiciar Mask
  for: any
  core: false
  where: 'Beside Inquisitor Verzen Wranlock''s skeleton under a tree at X: -30 Y: -88, up the hill from Rolan''s fight.'
  how: 'Pick it up. Loot the skeleton too: the Investigation Notes start Investigate the Selûnite Resistance.'
  note: 'Uncommon helmet, +1 Intimidation. Bonbon wears the Helmet of Arcane Acuity, so this is a camp hat.'
- id: severed-head
  name: Severed Head
  for: any
  core: false
  where: 'Large bird''s nest near the child''s burlap sack at X: 84 Y: -71, south-east battlefield.'
  how: 'Pick it up from the nest.'
  note: 'Quest item in disguise: it unlocks Balthazar''s secret lab in Moonrise Towers (Broken Moonlantern, Dead Pixie, the Shadow Lantern table). Carry it there.'
- id: inscribed-githyanki-slate
  name: Inscribed Githyanki Slate
  wiki: Inscribed Githyanki Slate (map)
  for: any
  core: false
  where: 'Dead githyanki scout at X: -54 Y: -80, near the main bridge to the Tollhouse.'
  how: 'Loot the corpse (no Speak with Dead).'
  note: 'Quest item. Progresses Find the Githyanki Crèche with a route to Crèche Y''llek if you have not been. The route does the Crèche first (stops 1 and 2); keep it as a reminder if you skipped it.'
- id: grey-scouts-journal
  name: Grey Scout's Journal
  for: any
  core: false
  where: 'Dead duergar on top of a rock at X: 19 Y: 17, south-west of the House in Deep Shadows.'
  how: 'Loot the corpse. A DC 10 Survival buried chest with gold and an arrow sits beside him.'
  note: 'Reading it marks the House in Deep Shadows on the map. Harper Lightspark''s journal on the rock at X: 93 Y: 107 does the same.'
- id: potters-chest-key
  name: Potter's Chest Key
  for: any
  core: false
  where: 'Behind a movable brick in the pottery wall, X: -34 Y: 13.'
  how: 'Perception DC 10.'
  note: 'Opens the Potter''s Chest (Luminous Gloves, Idol of Selûne, Selûnite note). Saves a DC 14 pick.'
- id: key-old-pottery
  name: Key (Old Pottery)
  for: any
  core: false
  where: 'Conic vase on the shelf at X: -33 Y: -13 in the round tower south of the pottery.'
  how: 'Search the vase.'
  note: 'Opens the traveller''s chest under the same shelf: Ring of Twilight.'
- id: key-harpers-ambush
  name: 'Key (Harpers'' Ambush)'
  for: any
  core: false
  where: 'Roof of the ambush house, next to a skeleton at X: -5 Y: -1.'
  how: 'Jump up after the fight.'
  note: 'Opens the chest at X: -12 Y: -7: Hammergrim Mist Amulet.'
quests:
- name: Find Rolan in the Shadows
  steps: |-
    - Rolan drinks at the inn bar (X: -78 Y: 148) until Isobel is saved and you fast travel or long rest; then he is gone. The children Umi and Ide start the quest, but it triggers with or without it.
    - He is at the south end of the battlefield, on the east bank south of the main Tollhouse bridge, **X: -52 Y: -110**. Incinerated shadow remains at X: -35 Y: -95 mark the path down.
    - Approaching pulls you into his fight with the last two Shadows. Kill them. Gale's fire, Bonbon's Flourish; it is short.
    - He goes back to the inn embarrassed and asks you to save Cal and Lia (Moonrise prison). Speak to him there to close the quest.
    - Rescue the Tieflings pays out through him at the inn (about 450 gp) only before you leave Act 2.
  outcome: 'Rolan alive at the inn; the family reunion after the prison break; Rolan sides against Lorroakan automatically in Act 3 if both siblings live.'
  lockout: 'Long rest or leave the area once you are close and he dies of the curse. Rescuing Cal and Lia before your first inn visit can leave him already gone or bug him dead.'
- name: Lift the Shadow Curse
  wiki: Lift the Shadow Curse
  steps: |-
    - The House in Deep Shadows (X: 68 Y: 36, "House of Flowers") is where Oliver, Thaniel's shadow half, lives. Flowers grow around it. Two dead githyanki: Teth'ka at X: 75 Y: 43 answers Speak with Dead.
    - Play his two rounds of hide-and-seek early for the Ring of Shadows. Refusing summons Mummy, Daddy and Doggy at once.
    - Come back after Halsin rescues Thaniel and tell Oliver who he is. He leaves through a portal to Reithwin's square. Follow it for the Nightdome fight. Full steps on the Shadow-Cursed Lands page.
  outcome: 'Ring of Shadows now; Halsin and Thaniel later.'
  lockout: 'Never damage the Nightdome directly; kill the summons. See the region page.'
- name: Seek Protection from the Shadow Curse
  steps: |-
    - The Harper ambush house is at X: 10 Y: -20. Meet Branthos's squad there after accepting at the inn bridge. Talk to Branthos to spring it. Talk-down and Dolly on the Shadow-Cursed Lands page.
    - After: Cruel Sting and Thermoarcanic Gloves from the bodies, Hammergrim Mist Amulet from the chest inside, key on the roof.
  outcome: 'Moonlantern, then the Pixie Blessing.'
- name: Punish the Wicked
  steps: |-
    - He Who Was and Madeline's corpse at the ritual circle, X: 129 Y: 106, east of the inn. Take the quest. The ledger is in the Waning Moon; judgement and oath rules on the Shadow-Cursed Lands page.
  outcome: 'Raven Gloves.'
- name: Investigate the Selûnite Resistance
  steps: |-
    - Starts from the Investigation Notes on Inquisitor Wranlock's skeleton (X: -30 Y: -88, near Rolan) or the note in the Potter's Chest (X: -52 Y: 11, after the Meazels).
    - Leads to the Last Light cellar (Halfred's Note by the Selûne shrine) and the Mason's Guild basement (the Tower-Shaped Key from Mattis, the Mason's Log). Those steps are on the inn and Reithwin pages; the basement is also where the Helmet of Arcane Acuity is.
  outcome: 'Lore only. Completes at the Mason''s Log.'
- name: Find the Githyanki Crèche
  steps: |-
    - The dead githyanki at X: -54 Y: -80 carries an Inscribed Githyanki Slate that maps the route to Crèche Y'llek if the crèche is still unvisited.
  outcome: 'Quest marker for the Crèche. The Monastery Trail exit at X: 167 Y: -28 is the way there; closed after the Shadowfell.'
lockouts:
- what: 'Long rest or leaving after approaching Rolan'
  closes: 'Rolan, his Act 3 help against Lorroakan, the ~450 gp Tiefling reward'
  avoid: |-
    Rescue him in one go on the same trip as the mastiffs. Once you have seen him, finish the fight. No camp until he has walked off toward the inn.
- what: 'Rolan leaves the inn on the first fast travel or long rest after Isobel is saved'
  closes: 'Nothing yet, but the clock on the previous lockout starts'
  avoid: |-
    Talk to him at the bar before Isobel if you want the first conversation; it is not required. Do the ambush and Dolly first, then go south for him before you rest.
- what: 'Attacking the Shadow Mastiff camp in the dark'
  closes: 'Nothing, but Shadowblend and Shadow Veil make the pack invisible and resistant'
  avoid: |-
    Destroy the torches, then light the field yourself before they close: Light on Charles's shield or Gale's Dancing Lights. The Pixie Blessing protects you; it does not illuminate.
- what: 'Entering the mansion east of the inn without deep-curse protection'
  closes: 'Party members drop to the curse inside'
  avoid: |-
    Penumbral Armour waits until you have the Pixie Blessing or a lantern. The signpost at X: -10 Y: 166 is the warning.
- what: 'Refusing Oliver''s game or pickpocketing him mid-round'
  closes: 'The Ring of Shadows becomes a fight or a silver band'
  avoid: |-
    Say yes to both rounds. Hide Asterion, walk to Oliver's invisible model, done.
- what: 'Dropping into the inn cellar from the mansion roots before entering the inn properly'
  closes: 'The whole inn turns hostile'
  avoid: |-
    Enter the inn by the bridge first. Use the roots only afterwards, as a shortcut to the Coruscation Ring chest.
npcs:
- name: Rolan
  role: 'Rescue target (Lvl 3 evoker, 26 HP)'
  note: 'X: -52 Y: -110, on the bank south of the main bridge. Two Shadows left when you arrive. Fire Bolt, Magic Missile, Thunderwave on his side. Saving him is a Folk Hero inspiration.'
- name: Shadow Mastiff Alpha
  role: 'Boss: drops the Shadow-Cloaked Ring (Lvl 6, 44 HP, AC 14)'
  note: 'Spawns with three Shadow Mastiffs when the everburning torches at X: -49 Y: 36 are destroyed. Knockdown Jaws, Terrifying Howl (WIS), Shadowblend (invisible while obscured), Shadow Veil (resists non-magical B/P/S while obscured), Sunlight Weakness. Low saves across the board: Hold Monster from Bonbon lands.'
- name: Oliver
  role: 'Hide-and-seek, Thaniel''s shadow half'
  note: 'House in Deep Shadows. Arcana DC 14 or Monk Insight DC 14 reads him. Rewards the Ring of Shadows after two rounds. Later the Nightdome fight in Reithwin. Full entry on the region page.'
- name: He Who Was
  role: 'Quest-giver, hidden vendor'
  note: 'Ritual circle X: 129 Y: 106. Punish the Wicked. Trade button in dialogue: scrolls, Divine Bone Shards, Xorn Scales. Full entry on the region page.'
- name: Lassandra
  role: 'Harper scout'
  note: 'First contact from the Grymforge side at X: 74 Y: 152. Six Shadows and cursed Yonas attack mid-dialogue. Marks the inn. Keep Karrow and Meygan alive for the Folk Hero inspiration.'
- name: Kar'niss and the convoy
  role: 'Ambush target'
  note: 'The ambush house is X: 10 Y: -20. Kar''niss (drider, 184 HP), Kansif (Fireball), Bedi, Gronag, Vez, Lora. Talk-down and stats on the region page. Drops: Moonlantern, Cruel Sting, Thermoarcanic Gloves.'
- name: Meazels
  role: 'Pottery ambush'
  note: 'Four in the ruined pottery at X: -43 Y: 8. Perception DC 18 spots them. Garrotte and Shadow Teleport; keep Gale away from the walls.'
- name: Weary Traveller (Elminster)
  role: 'Gale''s quest'
  note: 'Stands in the Sharran ruins at the Grymforge lift exit if Gale has eaten a magic item. Talk to him with Gale. Region page has the rest.'
checks:
- what: 'Everburning torches'
  note: 'Arcana DC 14 at the fenced camp X: -49 Y: 36 identifies Continual Flame. Break all of them to spawn the mastiffs. Korliss''s backpack by the fence gate: Potion of Greater Healing and his journal.'
- what: 'Pottery ambush'
  note: 'Perception DC 18 on approach to X: -43 Y: 8 reveals four Meazels. Potter''s Chest Key: Perception DC 10 at X: -34 Y: 13 finds the movable brick.'
- what: 'Blight ambushes'
  note: 'X: 42 Y: 58 (Shambling Mound, Ironwood Club) and X: 67 Y: 107 (Bagida''s chest, key on her skeleton at X: 91 Y: 82) are Perception DC 30. X: 88 Y: -95 (Frost Prince chest) has no check; the chest is the bait.'
- what: 'Dead raven'
  note: 'X: 30 Y: 114. Arcana DC 15 warns you off. Touching it spawns twelve Shadow-Cursed Ravens. The roof chest nearby (X: 41 Y: 111) is minor loot; key on the skeleton at X: 57 Y: 113.'
- what: 'Tripwire tower'
  note: 'Armed tripwire across the door of the round tower at X: -34 Y: -12. Disarm or step over; the Ring of Twilight chest is inside.'
- what: 'Ellie May''s grave'
  note: 'Near the graverobber''s camp at X: 73 Y: 151. Two Perception DC 10 checks lead to the Family Ring burrow.'
- what: 'Buried treasure'
  note: 'Survival: X: 26 Y: 170 (DC 10, mansion), X: 18 Y: 14 (DC 10, by the Grey Scout), X: 41 Y: 0 (DC 10, south of the house), X: 84 Y: 123 (DC 10), X: 92 Y: -101 (DC 10), X: 135 Y: 181 (DC 10) and X: 136 Y: 182 (DC 16), X: -2 Y: -59 (DC 18), X: -32 Y: -96 (DC 18, hill above Rolan).'
- what: 'Dead Druid''s camp'
  note: 'X: 109 Y: 183 by the lift path. Heavy chest in the cart (gold, ingredients), a Nature DC 18 on the journal, a buried chest at the clearing''s end.'
- what: 'Dead tieflings'
  note: 'X: -11 Y: 59, Investigation DC 14. Zevlor''s caravan survivors who did not make it. No Speak with Dead.'
- what: 'Siege engines'
  note: 'History DC 14 near X: 11 Y: -42 for lore on the Justiciar and druid war. Nothing to loot beyond plain weapons on skeletons.'
tips: |-
  **Curse here is light.** A torch or Isobel's blessing covers the whole battlefield except the mansion east of the inn. Do the mansion after Dolly.

  **Order for the one trip.** Shadowed Battlefield waypoint, east to the House in Deep Shadows (Ring of Mental Inhibition, Oliver's game, Ring of Shadows), west to the pottery (Meazels, Luminous Gloves, tripwire tower for the Ring of Twilight), north a step to the mastiff camp (Shadow-Cloaked Ring), then south down the bank to Rolan and the pier chests (Gloomstrand Shield). Inquisitor Wranlock's skeleton and the githyanki slate are on the way. Long rest at the end, not before.

  **Ambush loot** at X: 10 Y: -20 is a separate trip with the Harpers: Cruel Sting, Thermoarcanic Gloves, Hammergrim Mist Amulet, key on the roof.

  **Loose ends.** He Who Was (X: 129 Y: 106) and the Family Ring are on the east side near the lift path; grab them on arrival or when you return for the Crèche. The Severed Head from the nest at X: 84 Y: -71 goes to Moonrise for Balthazar's lab. Camp from the battlefield uses the cursed camp layout but is safe.

  **Chests in plain sight** (all Sleight of Hand DC 10 or unlocked): X: -41 Y: -54 heavy, X: -1 Y: -41 heavy (key in a sack at X: -30 Y: -35), X: 27 Y: 71 heavy, X: 112 Y: -39 heavy, X: 73 Y: 142 wooden, X: 106 Y: 85 wooden (key in a sack at X: 78 Y: 85, Perception DC 10), X: 32 Y: -6 wooden. Random loot; skip if short on time.
---
