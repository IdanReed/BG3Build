---
slug: house-of-healing
name: House of Healing
act: 2
order: 90
region: Shadow-Cursed Lands
wiki: House of Healing
summary: 'Malus Thorm''s undead hospital in the north-west corner of Reithwin: the Battered Lute that wakes Art Cullagh, Arabella''s parents, and the Eversight Ring for Asterion in the morgue lab.'
arrive: 'Deep curse. Pixie Blessing or a lit Moonlantern in hand, nothing less. Reithwin Town waypoint (X -78 Y -46), then west across town; the Grand Mausoleum waypoint (X -173 Y 80) is closer once unlocked. Front door on the south side into the lobby (X -199 Y -16, Sister Sinda); graveyard gate at X -152 Y 20; alley door to the morgue at X -219 Y 16; vines from the Mason''s Guild back balcony and yards drop into the graveyard. The morgue is a separate building west of the hospital, reached by the paved path from the ward''s side door. Outside it: two Shadows, a Wraith, a Shadow Mastiff and three shadow-cursed humanoids.'
curse: deep
items:
- id: eversight-ring
  name: Eversight Ring
  for: Asterion
  core: true
  where: 'Morgue lab, the room straight across from the entry hall past the zombie crypt. Locked, trapped chest in the corner at X 9 Y -981 (opulent chest on the ring page).'
  how: 'Sleight of Hand DC 14 to disarm, DC 14 to pick. Clear or cover the poison vents in the zombie crypt first. The lab door opens with the Necrotic Laboratory Spare Key from the dead Harper in the workshop.'
  note: 'Immunity to Blinded, and the wearer sees through magical darkness (the wiki confirms this even though the tooltip does not). Asterion fights unblinded inside Charles''s Darkness (nobody shoots into or out of the cloud). loot.md says take it before Ketheric falls or the Colony is cleared. The wiki lists no such cutoff and the route returns to Reithwin after Ketheric; the certain cutoff is the road to Act 3. Take it on the Reithwin run (stop 9) anyway.'
  verify: true
- id: battered-lute
  name: Battered Lute
  for: any
  core: false
  where: 'On Malus Thorm''s body in the operating theatre (X -201 Y 49).'
  how: 'Talk him into killing himself or kill him, then loot the corpse. 35 XP on pickup.'
  note: 'Quest item for Wake Art Cullagh. Play it at Art''s bed in Last Light Inn. Otherwise a plain lute.'
- id: surgeons-subjugation-amulet
  name: 'Surgeon''s Subjugation Amulet'
  for: any
  core: false
  where: 'Worn by Malus Thorm (X -201 Y 49).'
  how: 'Loot his body.'
  note: 'Rare. Once per long rest, a critical hit on a humanoid Paralyses it for 2 turns. Paralysed within 3 m is an auto-crit for everyone, so this is a spare Hold on a crit turn for Charles or Asterion.'
- id: poisoners-gloves
  name: 'Poisoner''s Gloves'
  for: any
  core: false
  where: 'Painted chest in the corner of Malus Thorm''s office, the small room north of the theatre (X -199 Y 78).'
  how: 'Sneak in along the upper level; the surgeons'' vision cones cover only the centre of the theatre. Office doors: key on the desk or Sleight of Hand DC 10.'
  note: 'Rare. Any Poison damage forces a Constitution save (DC 13) or Poisoned. No plan slot; sell (240 gp).'
- id: key-malus-thorm-office
  name: 'Key (Malus Thorm Office)'
  for: any
  core: false
  where: 'Desk in Malus Thorm''s office (X -200 Y 77).'
  how: 'Pick it up.'
  note: 'Opens the two graveyard doors of the office. Both are also Sleight of Hand DC 10 from either side.'
- id: surgery-and-physiology
  name: 'Surgery and Physiology: A Sharran''s Primer'
  for: any
  core: false
  where: 'Same desk (X -199 Y 77).'
  how: 'Read it before talking to Malus.'
  note: 'Unlocks two DC 18 lines in his dialogue (Intimidation or Persuasion) that make the nurses kill him. Without it the talk-down needs two DC 21 Persuasion checks.'
- id: hospital-library-key
  name: Hospital Library Key
  for: any
  core: false
  where: 'Heavy chest next to Sister Sinda''s counter (X -205 Y -4). A second copy is inside the library.'
  how: 'Open the chest. Or skip the key: library door Sleight of Hand DC 10, roots up from the upper theatre at X -193 Y 59, or the roof.'
  note: 'Library above the theatre, reached by the lift at X -199 Y 26: two gilded chests (DC 10 each, X -203 Y 57 and X -211 Y 43), one with alchemy ingredients. The bookcases around the theatre roll uncommon or rare scrolls.'
- id: key-sinda
  name: 'Key (Sinda)'
  for: any
  core: false
  where: 'On Sister Sinda.'
  how: 'Pickpocket or loot.'
  note: 'Unlocks her counter (X -205 Y -6): alchemy ingredients.'
- id: true-loves-embrace
  name: 'True Love''s Embrace'
  for: any
  core: false
  where: 'Skeleton on a mattress behind Sinda''s counter (X -212 Y 0).'
  how: 'Loot the skeleton.'
  note: 'Rare ring. Casts Warding Bond once per long rest on whoever wears the matching True Love''s Caress. The bond survives taking both rings off until death or a long rest, so cast it and swap back to plan rings.'
- id: true-loves-caress
  name: 'True Love''s Caress'
  for: any
  core: false
  where: 'Graveyard, skeleton against a tombstone on the road between the House of Healing and the Mason''s Guild (X -147 Y 43).'
  how: 'Perception 5 to notice the skeleton.'
  note: 'Rare ring, the other half of the pair. The wearer receives the Warding Bond.'
- id: shars-temptation
  name: 'Shar''s Temptation'
  for: any
  core: false
  where: 'Crate under a bet list at the end of the eastern gallery, by the wooden ladder (X -193 Y 12).'
  how: 'Open the crate.'
  note: 'Uncommon amulet: Charm Person once per short rest. Face utility for Bonbon; no plan slot.'
- id: boots-of-apparent-death
  name: Boots of Apparent Death
  for: any
  core: false
  where: 'Graveyard charnel behind a locked iron gate (X -160 Y 47), in the sarcophagus.'
  how: 'Gate is Sleight of Hand DC 10.'
  note: 'Rare. Feign Death once per short rest. Novelty; sell (190 gp).'
- id: icebite-robe
  name: Icebite Robe
  for: any
  core: false
  where: 'Unlocked graveyard charnel (X -155 Y 64), in one of the sarcophagi.'
  how: 'Open the sarcophagi.'
  note: 'Rare clothing: Cold resistance and Armour of Agathys at level 3 once per long rest. Gale keeps Armour of Landfall; bag or sell (800 gp).'
- id: strange-tendril-amulet
  name: Strange Tendril Amulet
  for: any
  core: false
  where: 'Morgue entry hall, hidden room. Wooden chest at X 85 Y -1007.'
  how: 'Perception 10 reveals a button at X 82 Y -998. Press it.'
  note: 'Rare amulet: Evard''s Black Tentacles at level 4 once per long rest. Concentration, so it costs a lane; all four lanes are taken. Sell (190 gp).'
- id: firzus-ring-of-trading
  name: 'Firzu''s Ring of Trading'
  for: any
  core: false
  where: 'Charred corpse in the same hidden room (X 82 Y -1006).'
  how: 'Loot it.'
  note: 'Uncommon: Deception +1. Swap onto Bonbon for a talk.'
- id: bided-time
  name: Bided Time
  for: any
  core: false
  where: 'Morgue, mortuary workshop south of the zombie crypt (door at X 50 Y -992). Locked heavy chest at X 46 Y -1005.'
  how: 'Sleight of Hand DC 14.'
  note: 'Uncommon clothing: 2 turns of Arcane Charge (+2 spell damage to Threatened targets) when hit in melee. Not for Gale; sell (250 gp).'
- id: necrotic-laboratory-spare-key
  name: Necrotic Laboratory Spare Key
  for: any
  core: false
  where: 'Dead Harper in the mortuary workshop (X 47 Y -1009).'
  how: 'Loot the corpse.'
  note: 'Opens the locked Morgue Lab door off the zombie crypt, the room with the Eversight Ring.'
- id: research-notes
  name: Research Notes
  wiki: 'Research Notes (House of Healing)'
  for: any
  core: false
  where: 'Desk in the mortuary workshop (X 47 Y -1010), with Olam''s Journal.'
  how: 'Read it.'
  note: 'Olam''s log of spells tried against the curse; the "Vita Cava" line made the Living Armour in the pit. The wiki ties it to no quest. If it updates Lift the Shadow Curse in game, note it.'
  verify: true
- id: surgeons-research-notes
  name: 'Surgeon''s Research Notes'
  for: any
  core: false
  where: 'Morgue lab desk (X 16 Y -988), next to a Karabasan''s Poison.'
  how: 'Read it. Perception 15 at the desk reveals a lever.'
  note: 'Malus''s paralytic research (Sage inspiration). The lever plus the one by the metal door (X 45 Y -973) opens the Ominous Crevice; without both the door is Sleight of Hand DC 30.'
- id: karabasans-gift
  name: 'Karabasan''s Gift'
  for: any
  core: false
  where: 'One in the morgue lab (X 15 Y -988). One each on Sisters Sinda, Anya, Geanne, Hunna and Vanessa.'
  how: 'Pick it up; loot or pickpocket the nurses.'
  note: 'Rare grenade. Thrown: 2 m radius, Constitution save DC 15 or Paralysed for 2 turns. Paralysed within 3 m is an auto-crit, so this is a Hold for anything Hold Person cannot touch. Six of them here.'
- id: elixir-of-hill-giant-strength
  name: Elixir of Hill Giant Strength
  for: any
  core: false
  where: 'Bloodbank shelves in the morgue lab, with a Potion of Greater Healing and a Potion of Superior Healing.'
  how: 'Pick it up.'
  note: 'Bonbon''s daily Titanstring elixir. Save it.'
- id: fleshmelter-cloak
  name: Fleshmelter Cloak
  for: any
  core: false
  where: 'Ominous Crevice, locked gilded chest on the ledge opposite the exit, above the pit (X 29 Y -930).'
  how: 'Open the crevice with both levers (lab lever behind Perception 15, plus the one at the door). Walk the outer ledges; Misty Step or Feather Fall helps. The chest is a Sleight of Hand lock with no DC on the wiki.'
  note: 'Uncommon: 1d4 Acid to anything that hits the wearer in melee. No plan slot.'
- id: protective-plate
  name: Protective Plate
  for: any
  core: false
  where: 'Bottom of the pit, on the Hollow Armour (X 44 Y -942).'
  how: 'Descend into the acid vapour. A Hollow Armour and three Fetid Oozes attack on sight. Kill the armour.'
  note: 'Uncommon heavy armour: AC 18, Necrotic resistance, no Stealth penalty. The pit fight is optional; skip it if short on time.'
- id: assassins-shortsword
  name: 'Assassin''s Shortsword'
  for: any
  core: false
  where: 'Stone ledge west of the House of Healing (starts at X -235 Y 54), on one of two skeletons at X -252 Y 36.'
  how: 'Walk the ledge and loot the skeleton.'
  note: 'Uncommon +1 shortsword, advantage on Stealth. Nobody swings one; sell.'
- id: watchers-shield
  name: 'Watcher''s Shield'
  for: any
  core: false
  where: 'The other skeleton on the same ledge (X -250 Y 36).'
  how: 'Loot it.'
  note: 'Uncommon +2 shield, advantage on Perception. Bonbon''s plan shield is the Safeguard, then the Sentinel Shield from Moonrise; this one goes to whoever leads exploration.'
quests:
- name: Wake Art Cullagh
  steps: |-
    - Start at Last Light Inn: talk to Art in the north ground-floor room, or to Fist J'ehlar. Tell Halsin.
    - Here: reach Malus Thorm in the operating theatre. Talk him down (see npcs) or kill him. Loot the Battered Lute.
    - Back at the inn, play the lute at Art's bed. He wakes and asks for Halsin.
  outcome: 'Art wakes and Lift the Shadow Curse moves to the lakeshore portal (hold it four turns). Inspirations for Noble, Entertainer and Sage backgrounds.'
  lockout: 'Art dies if Isobel is taken or killed; Speak with Dead on his body still gives the Thaniel lead. Entering the Shadowfell with him still asleep closes it (route cutoff 1).'
- name: Lift the Shadow Curse
  steps: |-
    - The lute is the only thing this building adds. Everything after it (portal, Oliver, Thaniel) happens at the inn, the House in Deep Shadows and camp.
  outcome: 'Halsin as a permanent companion; the curse lifts after Ketheric dies and the party leaves for Act 3.'
- name: 'Find Arabella''s Parents'
  steps: |-
    - Arabella is at the graveyard gate (X -153 Y 15). Two Shadows attack; she entangles them. Agree to find her parents and let her stay at camp. Refusing either sends her into the curse to die.
    - Children's ward, east wing (X -185 Y 12): Locke and Komira on the cots. Walking up to them updates the quest. Sister Lidwin tends them; Deception or Sleight of Hand DC 14 convinces her they are cured and opens her shop.
    - Speak with Dead on Locke: killed by the surgeon sisters after the ambush; Zevlor urged surrender (Find Zevlor updates).
    - Tell Arabella at camp, kindly. She refuses to talk, then after a long rest hands over the Shadow Blade Ring and Arabella's Shadow Entangle.
  outcome: 'Shadow Blade Ring for Charles. Arabella stays in camp until the end of the act and returns in Act 3 as an ally for Gather Your Allies.'
  lockout: 'Telling her at the gate instead of camp is Persuasion or Intimidation DC 14 (or Detect Thoughts DC 10); a failure sends her into the curse. Never telling her: she leaves a note and is gone for good.'
- name: Find Zevlor
  steps: |-
    - Speak with Dead on Locke adds the entry that Zevlor urged the refugees to surrender. Zevlor himself is in a Mind Flayer pod in the Colony (X 694 Y 14) at the end of the act. Open the pods, never purge.
  outcome: 'Zevlor and a Hellrider squad for Gather Your Allies.'
lockouts:
- what: 'Arabella told about her parents before she reaches camp, and the DC 14 check fails'
  closes: 'Arabella: the Shadow Blade Ring, her Act 3 ally slot'
  avoid: |-
    - At the graveyard gate agree to find her parents and let her stay at camp. Say nothing about the bodies even if you already found them.
    - Break the news at camp with kindness. Long rest. Collect the ring.
- what: 'Refusing to help Arabella or to shelter her'
  closes: 'The same. She runs into the curse; her corpse is at X -176 Y -67 after a long rest.'
  avoid: |-
    Say yes to both.
- what: 'Entering the Shadowfell with Art Cullagh still asleep'
  closes: 'Wake Art Cullagh, Halsin''s portal, Halsin as a companion, Lift the Shadow Curse'
  avoid: |-
    Take the lute on the Reithwin run (stop 9) and play it at the inn before Moonrise or the Gauntlet.
- what: 'Taking the road west of the Waning Moon to Act 3'
  closes: 'Reithwin, the morgue and the Eversight Ring'
  avoid: |-
    Loot the morgue lab on the Reithwin run (stop 9). loot.md warns to do it before Ketheric falls or the Colony is cleared; the wiki does not confirm that earlier cutoff. Do not test it.
- what: 'Attacking Malus before the checks'
  closes: 'The talk-down inspirations and the Distressed Patient''s life. The lute and amulet still drop.'
  avoid: |-
    Read the Primer in his office first, then let Bonbon talk.
npcs:
- name: Malus Thorm
  role: Optional boss, holds the Battered Lute
  note: 'Read Surgery and Physiology in his office first, then let Bonbon talk. He blinds the patient and offers to cure the party. Pass one opener: Investigation DC 14 (Asterion has a Rogue line), Religion DC 14, or Persuasion DC 16; the Paladin line is an attack. Then, with the Primer read, Intimidation DC 18 or Persuasion DC 18 makes the nurses kill him. Without it, Persuasion DC 21 (a Bard line exists) has the nurses practise on each other, and a second Persuasion DC 21 (Bard line again) makes him stab himself; only that full path spares the patient. Any failed check starts the fight with Sisters Anya, Geanne, Hunna and Vanessa. Level 7, 276 HP, AC 18, Magic Resistance, Legendary Resistance against incapacitation three times, so Hold Person is a poor opener. His 8d8 tool attacks need a nurse to hand him an instrument, the nurses heal him and cast Wail of Loss together when he is hit, and below 40% HP he Multiattacks. Kill the nurses first. Drops the Battered Lute and the Surgeon''s Subjugation Amulet.'
- name: Sister Sinda
  role: Receptionist, holds Key (Sinda)
  note: 'Stops the party at the front door. Astarion passes with no roll. The Dark Urge passes with no roll by letting her inspect his head. Otherwise DC 16 (Deception, Performance, Persuasion or Intimidation; Bonbon has a Bard Performance line) or Charles''s Hexblade Deception line at DC 14. Or walk around her: the door to her right leads to the children''s ward and the gallery beyond it. Carries a Karabasan''s Gift and the counter key. Stays neutral; after Malus dies she says the doctor is absent.'
- name: Sister Lidwin (Anna Lidwin)
  role: 'Vendor, children''s ward'
  note: 'Fusses over Locke and Komira. Deception or Sleight of Hand DC 14 (Monk, Cleric and Druid Deception lines) convinces her they are cured; she then trades potions, poisons, alchemy ingredients and mostly rotten camp supplies. Stock includes Karabasan''s Poison and Purple Worm Toxin.'
- name: Sisters Anya, Geanne, Hunna and Vanessa
  role: 'Malus''s nurses'
  note: 'Each carries one +1 surgical tool (Artificial Leech, Bonesaw, Syringe, Trepan; not pickpocketable) and a Karabasan''s Gift (pickpocketable). In the fight they heal Malus, hand him instruments and cast Wail of Loss. The tools cannot be pickpocketed, only looted. If Malus dies and they live, they wander the upper theatre, neutral.'
- name: Arabella
  role: Quest-giver at the graveyard gate (X -153 Y 15)
  note: 'Agree to find her parents; agree to shelter her at camp. Bard, Druid and Wizard have lines about her Silvanus magic. Do not mention the bodies here.'
- name: Locke and Komira
  role: Corpses, children''s ward (X -185 Y 12)
  note: 'Arabella''s parents. Speak with Dead works on Locke only: killed by the surgeon sisters after fleeing the ambush; Zevlor wanted to surrender.'
- name: Distressed Patient
  role: Victim on the operating table
  note: 'Survives only if the nurses turn on each other and Malus kills himself. Afterwards investigate the bed and talk to him to free him, or cast Knock; the restraints cannot be picked. He runs off.'
checks:
- what: 'Graveyard skeleton on the road to the Mason''s Guild (X -146 Y 42)'
  note: 'Perception 5. True Love''s Caress.'
- what: 'Morgue entry hall wall (X 82 Y -998)'
  note: 'Perception 10 button. Hidden room: Strange Tendril Amulet, Firzu''s Ring of Trading.'
- what: 'Zombie crypt behind the morgue double doors'
  note: 'Three Zombies and three Greater Zombies lie on Poison Cloud vents; the room fills with poison when they rise. Fight from the doorway. Afterwards disarm the vents or cover each one.'
- what: 'Morgue lab desk (X 16 Y -988)'
  note: 'Perception 15 reveals a lever. With the lever by the metal door (X 45 Y -973) it opens the Ominous Crevice; the lock alone is DC 30.'
- what: 'Eversight chest (X 9 Y -981)'
  note: 'Trapped and locked, Sleight of Hand DC 14 each.'
- what: 'Buried treasure on the western ledge'
  note: 'Survival DC 14 at X -258 Y 28; Survival DC 10 at X -265 Y 15.'
- what: 'Charnel gate (X -160 Y 47)'
  note: 'Sleight of Hand DC 10. Boots of Apparent Death inside.'
- what: 'Library door by the lift (X -199 Y 26)'
  note: 'Hospital Library Key or Sleight of Hand DC 10. Two gilded chests inside, DC 10 each.'
tips: |-
  - Route: graveyard gate and Arabella first. Then the door right of Sinda into the children's ward (skips her checks): Lidwin, Locke, Shar's Temptation in the gallery. Spiral stairs up, along the upper theatre into the office: Primer, key, Poisoner's Gloves. Down to Malus. Morgue last: hidden room, zombie crypt, workshop, lab.
  - Malus has Legendary Resistance: three +10 saves against Hold, Stun and Paralyse. If it comes to a fight, Bonbon's Hold Monster and Asterion's Stunning Strike go on the nurses, and Charles smites Malus.
  - A vine bridge at X -190 Y 62 runs from the theatre roof to the Grand Mausoleum, and the Ominous Crevice exits north to the same cliffs.
  - Bird nests: Potion of Invisibility on the ward roof (X -200 Y -6); a second nest on the theatre roof (X -220 Y 45).
  - Malus counts toward Thorm Family Secrets and Town of Shadows for Sage and Entertainer backgrounds; talk before you swing.
---
