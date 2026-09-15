---
slug: mind-flayer-colony
name: Mind Flayer Colony
act: 2
order: 130
region: Shadow-Cursed Lands
wiki: Mind Flayer Colony
summary: 'Ketheric''s last stand under Moonrise. Free Zevlor from the pods, take the Resonance Stone from Balthazar''s lab, kill Ketheric and the Apostle of Myrkul, and take his Netherstone.'
arrive: 'From the Moonrise Towers Rooftop after Ketheric flees at about 40% HP. Cross the thin bridge to the hollow side tower and jump down. The jump is an area change with no fall damage. Destroy the fleshy membrane at the entrance to move on. No fast travel and no camp until the exit portal; the Restoration Pod by the lift (X: 752 Y: -34) is the long rest.'
curse: none
items:
- id: resonance-stone
  name: Resonance Stone
  for: Asterion
  core: true
  where: 'Balthazar''s study in the Necrotic Laboratory, on the desk next to the Mind-Archive Interface, X: 692 Y: -114. The lab entrance is X: 715 Y: -50.'
  how: 'Clear the undead ambush at the lab entrance (a Death Shepherd, four Winged Horrors, four Greater Zombies, six Zombies; the Shepherd raises a Reconstituted enemy every round, so kill it first), then pick the stone up. No check.'
  note: 'Near the Mind-Archive Interface (Necrotic Laboratory), late Act 2. Triggers Charles''s respec (Warlock 5 / Paladin 4, Alert + Savage Attacker, Shadow Blade main hand) and Phalar Aluve moves to Bonbon. Asterion carries the 9 m aura; holster it vs Psychic attackers and mental-save effects. Steeped in Bliss hits everyone within 9 m, the party included: advantage on physical ability checks, disadvantage on INT/WIS/CHA saves, vulnerable to Psychic. Undead and constructs ignore it, so it does nothing against Ketheric or the Apostle. The wiki notes it sometimes stops working after Act 2.'
- id: ketherics-shield
  name: 'Ketheric''s Shield'
  for: Bonbon
  core: false
  where: 'On Ketheric Thorm in the final arena, X: 861 Y: -23. Loot his body after the Apostle dies.'
  how: 'Drops from the fight. The pickpocket alternative (disarm him, drop a two-handed weapon near him, wait for him to equip it, lift the shield on the rooftop or while he is still invulnerable) is skipped by the route because he drops it here.'
  note: 'Ketheric Thorm''s second fight, or pickpocketed earlier (drop a two-hander near him, wait for him to equip it, lift the shield). +2 AC, advantage on DEX saves, +1 spell save DC and spell attack. Bonbon''s OPTION over the Sentinel Shield when +1 DC matters. Also Shield Blow: a reaction that knocks a melee attacker Prone (STR save). Inactive-set passives unverified.'
- id: staff-of-cherished-necromancy
  name: Staff of Cherished Necromancy
  for: any
  core: false
  where: 'Not confirmed in the colony. loot.md lists it as a Balthazar drop; the wiki lists only Mystic Carrion at Philgrave''s Mansion (Act 3) as a source and does not list it on Balthazar. Balthazar is only in the colony if you gave him the Nightsong, which the good path does not.'
  how: 'On the good path Balthazar dies at his Gauntlet of Shar outpost. Check his body there. Verify in game.'
  note: 'Balthazar drop; on the good path he dies in the Gauntlet, so it usually drops THERE. Niche with no necromancer in this party. Very rare +2 quarterstaff: disadvantage on saves against your necromancy spells, and Life Essence lets you cast a necromancy spell without a slot after a spell kill.'
  verify: true
- id: ketherics-netherstone
  name: 'Ketheric''s Netherstone'
  for: any
  core: false
  where: 'Attached to Ketheric''s armour (Reaper''s Embrace) until picked up, X: 861 Y: -23.'
  how: 'Loot Ketheric''s body after the Apostle of Myrkul dies. Taking it completes Defeat Ketheric Thorm; the exit portal opens after the cutscenes.'
  note: 'One of three Netherstones that control the Crown of Karsus. Story item; the party carries it into Act 3.'
- id: reapers-embrace
  name: 'Reaper''s Embrace'
  for: any
  core: false
  where: 'Worn by Ketheric Thorm, X: 861 Y: -23.'
  how: 'Loot his body after the Apostle dies.'
  note: 'Very rare heavy armour, AC 19. Magical Plate (all incoming damage -2), Reaper''s Rigidity toggle (cannot be moved; disadvantage on DEX saves), Howl of the Dead (Numb nearby creatures, short rest). Disadvantage on Stealth. Not in the plan. 6,400 gp base price, so sell it.'
- id: ketherics-warhammer
  name: 'Ketheric''s Warhammer'
  for: any
  core: false
  where: 'Carried by Ketheric Thorm in both fights, X: 861 Y: -23.'
  how: 'Drops here, or disarm him in either fight and pick it up. If you took it on the rooftop he swings a plain Flail of Myrkul down here.'
  note: 'Rare +1 versatile warhammer, +1d4 Psychic. Backbreaker (Prone), Concussive Smash (Daze), Weakening Strike. Not in the plan.'
- id: blade-of-oppressed-souls
  name: Blade of Oppressed Souls
  for: any
  core: false
  where: 'Necrotic Laboratory, in the heap of skulls behind the Flesh-Wrought door, X: 747 Y: -138.'
  how: 'Solve the brain-mapping puzzle at the neural button (X: 737 Y: -112). The door cannot be lockpicked or Knocked.'
  note: 'Rare +1 versatile longsword, +1d4 Psychic. Crowning Strike (short rest) can inflict Crown of Madness. Not in the plan.'
- id: circlet-of-mental-anguish
  name: Circlet of Mental Anguish
  for: any
  core: false
  where: 'On the skeleton beside the Waking Mind jar, X: 748 Y: -141, behind the puzzle door.'
  how: 'Solve the brain-mapping puzzle, then loot the skeleton.'
  note: 'Rare circlet. Psychic Leech: regain 1d4 HP when an enemy fails a CHA, INT or WIS save against your spell or cantrip. Gale and Bonbon both wear Acuity hats, so this stays in the bag.'
- id: braindrain-gloves
  name: Braindrain Gloves
  for: any
  core: false
  where: 'Same skeleton as the Circlet, X: 748 Y: -141.'
  how: 'Solve the puzzle, loot the skeleton.'
  note: 'Uncommon gloves. Mental Interference: your Psychic damage also inflicts Mental Fatigue for 2 turns. Asterion''s Psionic Overload riders would trigger it, but his slot is the Flawed Helldusk Gloves.'
- id: waking-mind
  name: Waking Mind
  for: any
  core: false
  where: 'Brain jar behind the puzzle door, X: 749 Y: -138, next to the Blade.'
  how: 'Solve the puzzle, take the jar, put it on the Mind-Archive Interface (X: 699 Y: -117) and talk through the Slack-Skinned Head. Ask what aid it offers, then agree to purge or consume its mind (the Illithid line). Insight 18 catches its lie; the truth changes nothing about the reward.'
  note: 'Grants the permanent Githzerai Mind Barrier: advantage on INT saves. One character only. Give it to Gale: a failed INT save against a mind flayer stun drops Twinned Haste. Lost on death, even after Revivify.'
- id: mind-flayer-parasite-specimen
  name: Mind Flayer Parasite Specimen
  for: any
  core: false
  where: 'Left-most brine pool in the room behind the Tadpoling Centre, near Mizora''s pod.'
  how: 'Perception 16 to spot it in the pool.'
  note: 'Goes straight into the illithid power tree. See the Tadpole tab for who spends it.'
- id: mols-eyepatch
  name: 'Mol''s Eyepatch'
  for: any
  core: false
  where: 'On the desk in Balthazar''s study, X: 693 Y: -111, beside the Resonance Stone.'
  how: 'Pick it up.'
  note: 'Advances Find Mol: she is not in the colony, and the quest moves to Baldur''s Gate. Mol takes it back in the Guildhall in Act 3. Urchin background: Amateur Optician inspiration.'
- id: morgue-cage-key
  name: Morgue Cage Key
  for: any
  core: false
  where: 'On Chop, the bugbear butcher in the Morgue, X: 663 Y: -74.'
  how: 'Talk to Us first, then Chop: Persuasion 14, Intimidation 18, or the Illithid Wisdom line. A failed check makes Chop hostile. Or pickpocket it (Asterion), or lockpick the cage (Sleight of Hand 14) out of his sight.'
  note: 'Opens the cage holding Us. Only matters if Us survived the Nautiloid.'
- id: summon-us
  name: Summon Us
  for: any
  core: false
  where: 'Spawns in the inventory of whoever opens Us''s cage in the Morgue, X: 663 Y: -74.'
  how: 'Free Us with the Morgue Cage Key or a Sleight of Hand 14 lockpick.'
  note: 'Conjure Us once per short rest: a 55 HP intellect devourer with physical and Necrotic resistance, Devour Intellect and Synaptic Discharge. Only if Us was freed on the Nautiloid and survived. Us stays with the party after the colony and looks like a kitty to outsiders.'
- id: infernal-rapier
  name: Infernal Rapier
  for: any
  core: false
  where: 'Reward from Mizora at her pod in the brine pool room, X: 676 Y: 39.'
  how: 'Wyll must be in the active party. Free Mizora with the unleash device (right side) or smash the pod (STR 14), then Persuasion 14 for a reward. She gives the rapier to Wyll.'
  note: 'Very rare +2 rapier that attacks and damages with the spellcasting modifier, +1 spell save DC, Planar Ally: Cambion once per long rest. Wyll''s weapon; only reachable with him in the party. Skip if Wyll stays in camp.'
- id: prayer-for-forgiveness
  name: Prayer for Forgiveness
  for: any
  core: false
  where: 'On the desk in Balthazar''s study, X: 695 Y: -111, next to the Resonance Stone.'
  how: 'Read it.'
  note: 'A letter from the Dark Urge to Bhaal with a note appended by Balthazar. Backstory for Charles; no mechanical effect.'
quests:
- name: Defeat Ketheric Thorm
  steps: |-
    - **Jaheira.** She comes to the hollow tower after the rooftop fight. To come down she takes a party slot. Recruit her as a full companion now; she is the Act 3 Harper thread. If she stays a follower she waits on the roof until Ketheric is dead, then asks to join on the Moonrise main floor.
    - **Explore first.** Ketheric waits. Do the Tadpoling Centre, the Morgue, the Barracks and the Necrotic Laboratory before the lift in the east. Intellect devourers in the corridors stay neutral unless a fight starts near them.
    - **Restoration Pod.** Right of the lift at X: 752 Y: -34. A full long rest: HP, slots, Bardic Inspiration, Channel Divinity, item charges. Unlimited uses outside Honour mode. It does not reset short rests.
    - **The Chosen.** The lift cutscene shows Ketheric, Gortash and Orin with the Netherbrain and Duke Ravengard. Gale offers to detonate the orb. Say no; yes is game over. Acolyte background: A Piece of Three inspiration. Outlander: From Head to Toe on the lift.
    - **Talk.** Step past the three steps and Ketheric threatens you. Persuasion 18 makes him give himself to Myrkul and skips phase 1. The check only appears if you found the Letter to Ketheric in his Moonrise bedroom and passed Persuasion 18 or Intimidation 21 on the rooftop.
    - **Free Aylin.** She is held by spectral hands, and Ketheric is Invulnerable while she is. Use Help on her. Scratch (Find Familiar) can Help; send him in invisible on turn 1. Once free she charges Ketheric.
    - **Phase 1.** Ketheric (AC 22, 145 HP on Balanced, Aura of Hate, Deadly Orders, Incubate Death), a Mind Flayer on the right overlooking the arena, four Intellect Devourers from below it, four Necromites on the left platform. Kill the Mind Flayer first; its stun ends Gale's Haste. A STR 18 character can throw it into the chasm east of the platform. Clear the Necromites before phase 2 or the Apostle eats them. He is undead: no Hold Person, no Command. Prone, Blinded or Faerie Fire for advantage against his AC. Disarm removes his Smites. Reaper's Rigidity cancels his DEX-save advantage. Any character who dies within 12 m of him raises a Skeletal Involucre.
    - **Phase 2, Apostle of Myrkul.** 245 HP on Balanced, AC 19, cannot move, Magical Plate -2 damage, resists Necrotic and Cold, immune to Poison. Its Bone Chilled aura on the platform blocks healing; Disengage to the edge to heal. Up to four Necromites spawn each round at the arena edges, and Consume the Faithful eats one for Finger of Death (plus an 8d8 heal on Tactician). Kill the necromites and it never casts it. Reaper's Scythe knocks back 4 m: melee stand with the spikes at their back, or Disarm the scythe. Gaze of the Dead frightens (CON save) once a round, and again as a legendary action when attacked. Darkness or Hunger of Hadar blind it. Wall of Fire ticks on it every turn. Gale's fire is unresisted.
    - **Loot.** Ketheric's body: Netherstone, Ketheric's Shield, Warhammer, Reaper's Embrace. Then the portal to the Moonrise ground floor.
  outcome: 'Netherstone in hand and the act''s main quest complete. Portal to the Moonrise Towers main floor; Last Light Inn is reachable again. Isobel and Aylin reunite and ask to stay at camp. Jaheira asks to join if she is not a companion yet. Haunted One background: Lesser of the Three inspiration.'
  lockout: 'Gale''s orb in the cutscene ends the game.'
- name: Find Zevlor
  steps: |-
    - Tadpoling Centre: first left past the membrane, behind a Flesh-Wrought door. Ten pods. Right of the entrance: empty, Mind Flayer, empty, **Zevlor (X: 694 Y: 14)**, Mind Flayer. Left: empty (traces of Duke Ravengard), Mind Flayer, Manip Shuurga, Mind Flayer, Gauntlet Yeva. Cyan buttons under occupied pods describe the occupant.
    - The Neural Apparatus at X: 689 Y: 17 controls every pod at once: open, purge, or leave. Choose **open**. Purge kills everyone inside, Zevlor included. Leave lets you come back to the choice.
    - Fight: four Mind Flayers and six Intellect Devourers. Zevlor, Yeva and Shuurga fight with you. Keep Gale's Fireball and any Cloud of Daggers off them; party damage can turn them hostile.
    - Talk to Zevlor after. He admits the Absolute enthralled him with the promise of his Paladin status back. Tell him he can still be worthy; he leads the survivors out. Verify the exact line in game.
    - Approval: opening the pods pleases Shadowheart and Karlach, and Astarion disapproves.
  outcome: 'Quest complete. Zevlor and a Hellrider platoon join Gather Your Allies for the Netherbrain assault. Yeva reports Ravengard was taken from his pod alive not long before.'
  lockout: 'Purging the pods, or never opening them: Zevlor dies, and in Act 3 Orin leaves his corpse at camp.'
- name: The Blade of Frontiers
  steps: |-
    - Only if Wyll was recruited and is alive. Bring him in the active party or the rapier is lost.
    - Mizora is in a detached pod in the brine pool room behind the Tadpoling Centre, X: 676 Y: 39. Talk first: Intimidation 16, History 16 or Performance 16 makes her agree to end Wyll's pact.
    - Her pod has two devices. Arcana 10 to read each (automatic if you deciphered the same glyphs on the Nautiloid). Left is **annihilate**, right is **unleash**. Use unleash, or smash the pod with STR 14.
    - With Wyll present, Persuasion 14 for a reward: the Infernal Rapier goes to Wyll.
  outcome: 'Mizora leaves, lifts Wyll''s gag about the pact, and cites a clause that keeps him bound six more months. She waits at Wyrm''s Rock in Act 3 and later joins Gather Your Allies.'
  lockout: 'Annihilate kills Wyll wherever he is. Leaving her in the pod fails the rescue and Wyll is dragged to Avernus at the end.'
- name: Find Mol
  steps: |-
    - Take Mol's Eyepatch from Balthazar's desk, X: 693 Y: -111.
    - She is not in the Tadpoling Centre or anywhere else in the colony.
  outcome: 'Quest moves to the road, then to Baldur''s Gate. Mol is in the Guildhall in Act 3 and takes the eyepatch back.'
- name: Lift the Shadow Curse
  steps: |-
    - The last objective is Kill Ketheric Thorm. Thaniel must already be rescued and Oliver reunited with him (Last Light lakeshore portal, then Oliver's cottage).
    - Kill Ketheric and the Apostle. The curse lifts when you leave the Shadow-Cursed Lands.
  outcome: 'Halsin becomes a permanent companion. If Thaniel and Oliver are not reunited, Halsin stays behind at the road and is gone for the rest of the game, in whatever gear he is wearing.'
  lockout: 'Taking the road with Thaniel and Oliver apart.'
- name: Rescue Wulbren
  steps: |-
    - After Ketheric, Wulbren has thoughts: speak to him at Moonrise Towers.
    - Tell Barcus about Wulbren before the road, if not already done at Last Light. Barcus gives the Brilliant Retort on completion.
  outcome: 'Quest complete. Barcus leads the Ironhand Gnomes to Angleiron''s Cellar in Act 3 and can become their leader.'
  lockout: 'Leaving the Shadow-Cursed Lands without telling Barcus. He assumes Wulbren is dead.'
- name: Rescue the Tieflings
  steps: |-
    - Collect the rewards at Last Light before the road: Alfira (and Lakrissa) give about 470 gp, three scrolls, three potions and the Potent Robe; Rolan behind the bar gives about 450 gp; Bex and Danis below the north bridge behind the ox stables give Bex's Handmade Cookies.
  outcome: 'Quest complete after all three groups are spoken to.'
  lockout: 'The rewards cannot be collected in Act 3.'
- name: Embrace Your Potential
  steps: |-
    - Parasite Specimen in the brine pool (Perception 16).
    - The Astral-Touched Tadpole is not in the colony. The Emperor offers it in the Astral Prism after the first long rest at Wyrm's Lookout on the road to Baldur's Gate, once the Dream Guardian is revealed as a mind flayer (Help Your Protector). Keep it alive in that fight or the game ends.
    - **All four commune, nobody eats.** Communing leaves the tadpole for the next member; eating consumes it and only one character transforms. See the Tadpole tab.
  outcome: 'Communing evolves each character into a partial illithid: Fly and the five inner powers free, inner-ring tadpoles refunded, elite ring open. Black eyes and veins, irreversible. Refusing needs a DC 21 Wisdom check if anyone has used a parasite. Halsin and Jaheira are not eligible.'
- name: Open Your Scars
  steps: |-
    - Charles only. Kressa Bonedaughter in the Barracks (X: 727 Y: 41) recognises an undisguised Dark Urge and talks about patching him together as the first tadpoling victim. The talk always ends in a fight. Performance 10 to play dumb skips the exposition and still ends in a fight.
    - The Ruptured Mind Flayer Pod left of Mizora: Investigation 10 (the blood is fresh), Charisma 10 (a laughing woman who betrayed you), or ask Astarion to smell it.
    - Prayer for Forgiveness on Balthazar's desk, X: 695 Y: -111. More notes in the Barracks chambers.
  outcome: 'Journal entries for Open Your Scars. After the Kressa fight Charles remembers being ambushed here on his own business.'
- name: The Wizard of Waterdeep
  steps: |-
    - At the Netherbrain cutscene Gale wants to detonate the orb. Talk him down. He turns his interest to the crown instead.
  outcome: 'Quest moves to Sorcerous Sundries in Act 3.'
  lockout: 'Detonating is an early game over.'
- name: Gather Your Allies
  wiki: Gather Your Allies (quest)
  steps: |-
    - Zevlor freed from his pod: Hellrider platoon.
    - Mizora freed with Wyll alive: she wants revenge on the Absolute.
    - Us freed from Chop's cage: the strange creature.
  outcome: 'Three allies for the Netherbrain assault in Act 3.'
lockouts:
- what: 'Purging the pods at the Neural Apparatus'
  closes: 'Find Zevlor, Zevlor''s Hellriders in Act 3, Yeva and Shuurga'
  avoid: |-
    Choose open. The pods cannot be worked one at a time. Leaving them shut is the same as purging for Zevlor: Orin kills him later.
- what: 'Party damage on Zevlor, Yeva or Shuurga during the pod fight'
  closes: 'They turn hostile; Zevlor dies'
  avoid: |-
    No Fireball, Cloud of Daggers or Flame Strike near the freed captives. Gale uses Scorching Ray on the Mind Flayers; Bonbon shoots; Charles and Asterion take the devourers.
- what: 'Mizora annihilated in her pod, or left there'
  closes: 'Wyll (annihilate kills him even from camp; left behind, he is dragged to Avernus at the end). The Infernal Rapier if Wyll is not in the party.'
  avoid: |-
    Bring Wyll. Arcana 10 on the devices; use the right-hand unleash device or smash the pod (STR 14). Never the left. Persuasion 14 for the rapier. If Wyll is not in camp at all, skip her; nothing here matters.
- what: 'Jaheira dies during the Moonrise assault or the rooftop fight'
  closes: 'Jaheira as a companion, The High Harper (Minsc) and Harper aid in Act 3'
  avoid: |-
    As a follower she cannot be revived. Keep her out of melee, or do not invite her as a follower for the assault. Recruit her fully at the hollow tower when Ketheric flees; she takes a party slot to come down.
- what: 'Gale detonates the Netherese Orb at the Netherbrain cutscene'
  closes: 'The game'
  avoid: |-
    Pick the lines that talk him down.
- what: 'Kressa Bonedaughter goes hostile'
  closes: 'Myrkul''s Gift: 10 temp HP, +1d4 Necrotic on weapon attacks, Cold and Necrotic resistance until the temp HP are gone'
  avoid: |-
    Deception 21 to stand her down, then ask again for the Gift (Persuasion 18 per the colony page; verify in game). An undisguised Dark Urge always fights her. Cast Disguise Self on Charles or keep him out of the conversation. The Gift shares the temp-HP slot with Armour of Agathys, so it is a fight buff, not a permanent one.
- what: 'The road west of the Waning Moon to Baldur''s Gate'
  closes: 'Every Act 2 map, Last Light Inn, Moonrise Towers, and every camp follower who is not settled'
  avoid: |-
    Final point of no return. The game warns before you go. Before taking it:
    - **Halsin**: Thaniel rescued and Oliver reunited, or he stays behind for good.
    - **Barcus**: told about Wulbren; Brilliant Retort collected. Wulbren spoken to at Moonrise.
    - **Rolan**: alive and spoken to at the inn; Cal and Lia reunited. He runs the Sorcerous Sundries desk in Act 3.
    - **Tiefling rewards**: Alfira's Potent Robe and gold, Rolan's gold, Bex's cookies. None can be claimed in Act 3.
    - **Arabella**: told about her parents and settled at camp with Withers; Shadow Blade Ring collected.
    - **Dolly**: freed from the Moonlantern, Filigreed Feywild Bell in hand.
    - **Charles's Stone respec** at Withers: Warlock 5 / Paladin 4, Alert + Savage Attacker, Shadow Blade main hand; Phalar Aluve to Bonbon, Knife of the Undermountain King to Charles's bag.
    - **Isobel and Aylin** invited to camp. **Jaheira** recruited.
    - Anything still wanted from a Last Light or Moonrise vendor.
npcs:
- name: Chop
  role: Morgue butcher
  note: 'Bugbear at X: 663 Y: -74 who cuts corpses into Intellect Devourers. Holds the Morgue Cage Key. Persuasion 14, Intimidation 18 or Illithid Wisdom after talking to Us. He asks to be killed but fights back; attacking him turns the Morgue devourers hostile, not Us, and the devourers outside stay neutral.'
- name: Us
  role: Caged ally
  note: 'Only if freed on the Nautiloid. Caged by Chop. Freeing it gives Summon Us.'
- name: Kressa Bonedaughter
  role: Myrkulite necromancer, Barracks
  note: 'X: 727 Y: 41 with Hairy Henry, Ironfinger and Maghtew Budj. Deception 21 stands her down; then Myrkul''s Gift for the whole party from one check. Level 8 evocation wizard: Fireball, Bone Chill, Incubate Death, Misty Step, Myrkulite Scourge. Recognises the Dark Urge; that fight cannot be avoided without a disguise.'
- name: Zevlor
  role: Pod captive, Find Zevlor
  note: 'Pod at X: 694 Y: 14. Level 4 Paladin; fights beside you once freed. Leaves to lead the survivors out; Hellriders in Act 3.'
- name: Gauntlet Yeva and Manip Shuurga
  role: Pod captives
  note: 'Fight beside you when freed. Yeva says Ravengard was taken from his pod alive shortly before. Shuurga only laments.'
- name: Mizora
  role: 'Pod captive, Wyll''s patron'
  note: 'Pod at X: 676 Y: 39. Unkillable in combat (Zariel''s Protection). Only the annihilate device kills her, and Wyll with her.'
- name: Slack-Skinned Head
  role: Mind-Archive Interface
  note: 'X: 699 Y: -117. Insert brain jars to talk to them. Eight jars: True Mind (X: 696 Y: -116), Willing Mind (X: 693 Y: -115), Waking Mind (puzzle room), Butchered Mind (Morgue shelf, X: 678 Y: -68), Closed Mind (Ironfinger''s room in the Barracks, X: 716 Y: 34), Fresh Mind (box by the lift, X: 750 Y: -8), plus Dark Mind and Slave Mind from the Nautiloid. Only the Waking Mind gives a buff; the Waking and Fresh Mind dialogues move companion approval.'
- name: 'Ketheric Thorm / Apostle of Myrkul'
  role: Boss
  note: 'Final arena X: 861 Y: -23. Level 11 Oathbreaker: AC 22, Divine and Blinding Smites, Deadly Orders, Incubate Death, Shield Bash reaction, resists Necrotic, immune to Poison. Becomes the Apostle (AC 19, 245 HP Balanced, immobile) when killed. Persuasion 18 skips his phase with the rooftop groundwork.'
- name: Dame Aylin
  role: Ally
  wiki: Aylin
  note: 'Chained by spectral hands in the arena because she was freed at the Nightsong. Help frees her and strips Ketheric''s Invulnerable. She crushes his remains afterward and reunites with Isobel.'
- name: Jaheira
  role: Recruitable companion
  note: 'Joins as a full companion at the hollow tower after the rooftop fight, taking a party slot. Otherwise on the Moonrise main floor after Ketheric dies.'
- name: Enver Gortash and Orin the Red
  role: Cutscene only
  note: 'Seen with the Netherbrain and Duke Ravengard at the bottom of the lift. They sail for Baldur''s Gate. Not fightable here.'
checks:
- what: 'Fleshy membrane at the entrance'
  note: 'Attack it to get in.'
- what: 'Brain-mapping puzzle, neural button X: 737 Y: -112'
  note: 'Connect Emotion, Speech, Memory and Reason each to its twin across the projection through intermediate nodes with no overlaps. Opens the Flesh-Wrought door (no lockpick, no Knock): Blade of Oppressed Souls, Waking Mind, Circlet, Braindrain Gloves, Desecrated Relief. Sage background: Brain Blast! inspiration.'
- what: 'Desecrated Relief behind the puzzle door'
  note: 'Interact for the Grand Design vision and a Dream Guardian comment. No reward.'
- what: 'Left-most brine pool behind the Tadpoling Centre'
  note: 'Perception 16; Mind Flayer Parasite Specimen.'
- what: 'Mizora''s pod devices'
  note: 'Arcana 10 each, automatic if read on the Nautiloid. Left annihilate, right unleash. STR 14 smashes the pod instead.'
- what: 'Ruptured Mind Flayer Pod left of Mizora'
  note: 'Dark Urge only. Investigation 10, Charisma 10, or Astarion smells the blood.'
- what: 'Two Rune Slates on Balthazar''s desk'
  note: 'Arcana 14 each. Lore on the fall of the illithid empire and this colony''s Elder Brain.'
- what: 'Us''s cage in the Morgue'
  note: 'Sleight of Hand 14. Out of Chop''s sight, or he starts the key dialogue.'
- what: 'Touch device in the Morgue'
  note: 'First use drops a corpse from the pipe; Speak with Dead works on it.'
- what: 'Kressa Bonedaughter'
  note: 'Deception 21 to avoid the fight; Persuasion 18 for Myrkul''s Gift (verify: the condition page says talking to her again after the Deception grants it). A character without a tadpole (Jaheira) needs Persuasion 16.'
- what: 'Ketheric''s last words'
  note: 'Persuasion 18, only after the rooftop groundwork (Letter to Ketheric from his bedroom, then Persuasion 18 or Intimidation 21 on the roof). Skips phase 1.'
- what: 'Aylin''s spectral chains'
  note: 'Help action, by any character or Scratch. An Invisible character reaches her unnoticed, but Help starts the cutscene.'
tips: |-
  - **Rest here.** The Restoration Pod at X: 752 Y: -34, right of the lift, is a free long rest with unlimited uses outside Honour mode. Use it after the exploration and again before the lift if anything is spent.
  - **Resonance Stone off for Ketheric.** Every enemy in the final arena is undead or a mind flayer. The Stone does nothing to them and gives your own party disadvantage on mental saves. Bag it before the lift.
  - **Control lanes.** Ketheric is undead: Charles's Hold Person and Gale's Command do not land. Use Prone, Blinded and Faerie Fire for advantage, and Disarm to remove his Smites. Hold Person still works on Kressa and her cultists.
  - **Rejuvenating Miasma.** Animate Dead needs no corpse anywhere in the colony. Not this party's tool.
  - **Approval.** Opening the pods costs Astarion approval. The Fresh Mind and Waking Mind dialogues also move companions.
  - **The Emperor.** The Dream Guardian is revealed as the Emperor, and the Astral-Touched Tadpole is offered, in the Astral Prism after the first long rest at Wyrm's Lookout on the road, past the point of no return. All four commune; see the Tadpole tab. Do not let the Emperor die in that fight.
  - **Necrotic Laboratory Spare Key** is not here despite the name. The wiki places it on a dead Harper in the House of Healing morgue in Reithwin (X: 47 Y: -1009), where it opens the Morgue Lab door in that building.
  - **After the portal.** Moonrise main floor: Jaheira, Wulbren, Isobel and Aylin. Last Light Inn: Barcus, Rolan, Alfira, Bex, vendors. Camp: Arabella, Withers for Charles's respec. Then the road west of the Waning Moon.
---
