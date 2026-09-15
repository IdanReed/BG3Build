---
route:
- act: 1
  title: 'Crèche first, then the pass'
  intro: |-
    The party stands at Rosymorn Monastery at about character level 7. Everything on the Act 1 map, the crèche included, closes for good the moment the party enters the Shadowfell in Act 2, so the monastery and the crèche are finished before the road down. Locations and cutoffs are from bg3.wiki; gear assignments are from the Loot tab and the character pages.
  steps:
  - step: 1
    location: mountain-pass
    title: 'Rosymorn Monastery'
    do: |-
      - **Lady Esther**, on the trail: Graceful Cloth and Gloves of Cinder and Sizzle for Asterion, Gloves of Baneful Striking for Charles. The Periapt of Wound Closure is optional.
      - **Holy Lance Helm** for Charles: painted chest on the top level of the monastery. The giant eagles hold the roof.
      - **Dawnmaster's Crest**: solve the ceremonial-weapon altar now, but leave the Blood of Lathander in its vault until the crèche is done.
    leave: 'Into Crèche Y''llek through the monastery.'
    warn: 'Taking the Blood of Lathander without the crest starts the monastery''s self-destruct. Do it last, with the crest.'
  - step: 2
    location: creche-yllek
    title: 'Crèche Y''llek, all of it'
    do: |-
      - **A'jak'nir Jeera**: Gloves of Dexterity and the Knife of the Undermountain King for Bonbon. Buy or steal the rest of her stock; she is gone once the crèche turns hostile. The Gloves trigger Bonbon's Withers respec.
      - **Zaith'isk**: a player character sits in it while Ghustil Stornugoss is alive; pass the saves for permanent Awakened.
      - **Inquisitor's Chamber**: Circlet of Psionic Revenge for Asterion, Diadem of Arcane Synergy for Bonbon, Gloves of Belligerent Skies for Gale (elegant chest), Necklace of Elemental Augmentation (display case).
      - **Gish Far'aag**: Ring of Arcane Synergy for Charles. The Strange Conduit Ring is Charles's too.
      - **Vlaakith**: the audience turns the crèche hostile. Fight out, then back to the monastery for the Blood of Lathander with the crest.
    leave: 'Down the Mountain Pass road into the Shadow-Cursed Lands. The road lands the party in the west, near Reithwin.'
    warn: 'Nothing here is reachable after the Shadowfell.'
- act: 2
  title: 'Acuity gear first, nothing locked out'
  intro: |-
    Assumes the good path: Isobel saved, Nightsong freed, Shadowheart and Halsin in camp. Three acuity pieces drive the order: the Hat of Fire Acuity (Gale) at the first stop, then the Gloves of Battlemage's Power (Charles) and the Helmet of Arcane Acuity (Bonbon), both in Reithwin. Reithwin is deep curse, so the only early protection is the Pixie Blessing from Kar'niss's Moonlantern; stops 4 to 6 exist to get that blessing fast. Everything else in Act 2 waits.
  cutoffs:
  - name: 'Entering the Shadowfell'
    closes: 'Every Act 1 map including the crèche and the Underdark, Act 1 camps, Dammon''s crafting, Moonrise as a friendly place (Araj gone, the Warden hostile, the prison rescue auto-fails), and Art Cullagh if he is still asleep.'
    note: 'The bottom of the Gauntlet of Shar, where the Nightsong is. Run the checklist at stop 15 first.'
  - name: 'A long rest while Rolan is out in the curse'
    closes: 'Rolan dies. He leaves the inn the moment Isobel is saved.'
  - name: 'The road west of the Waning Moon'
    closes: 'Act 2. Halsin leaves for good if his quest is unresolved. Barcus, Rolan, Arabella and Dolly must all be dealt with first. The game warns before you go.'
  steps:
  - step: 3
    location: shadow-cursed-lands
    title: 'Arrive, and go straight to the inn'
    do: |-
      - From the Mountain Pass you land in the west, near Reithwin. Do not enter Reithwin: it is deep curse and a torch is not enough there. Follow the road north to Last Light Inn; the Harper scouts point the way.
      - From the Grymforge lift you land at the north tip of the map, next to the inn. Lassandra's Harpers point you there.
      - Do not wander south yet.
    leave: 'Cross the bridge into Last Light Inn.'
    warn: 'No long rest from here until Rolan is rescued at stop 6.'
  - step: 4
    location: last-light-inn
    title: 'First visit'
    do: |-
      - **Isobel.** Jaheira at the gate, then Isobel upstairs. Marcus attacks during her blessing. She must survive or every inn vendor and quest is gone. Mol being taken is scripted.
      - **Hat of Fire Acuity.** The Strange Ox stands by Dammon's forge. Question it until it turns into a Phasm Ooze and fights. Kill it and loot the Hat for Gale. Keep Dammon out of the fight. Charles must not kill it in dialogue as the Dark Urge: that is an oathbreak.
      - **Dammon.** Karlach's upgrade first if she is in camp. Spare Infernal Iron becomes Flawed Helldusk Armour, then Helmet, then Gloves, in that fixed order. Asterion's Gloves need the third spare piece. Act 2 iron: Mason's Guild backyard, Balthazar's vault chest in the Gauntlet, Yurgir.
      - **Shop.** See the gold table. Talk Mattis out of the Tower-Shaped Key (DC 14 then DC 6) instead of paying 1,000 gp. It opens the Mason's Guild basement.
      - **Loot.** Snowburst Ring: bedroom north of the bar, loose plank, Perception 10, for Bonbon. Cellar: the Meenlock carries the Covert Cowl for Charles. Past the cracked wall, a trapped heavy chest (disarm DC 10, lock DC 14) holds the Coruscation Ring for Gale.
      - **Talk.** Rolan at the bar. Art Cullagh in the infirmary, then Halsin. Florrick, before any long rest. Barcus about Wulbren. Raphael and Mol upstairs. Arabella is not here; she waits at the Reithwin graveyard (stop 8).
      - **Branthos's Harpers.** Accept the convoy ambush. It only appears once Isobel is saved.
    leave: 'Out to the road for the convoy ambush. Still no long rest.'
  - step: 5
    location: shadow-cursed-lands
    title: 'Moonlantern and Pixie Blessing'
    do: |-
      - Ambush Kar'niss's convoy with the Harpers. With them present you can talk him out of the lantern without a fight.
      - Take the Moonlantern, ring its bell, and free Dolly. Do not turn the mechanism twice; that kills her. The whole party gets the Pixie Blessing and the lantern is spent. Keep it: if the blessing drops on a region change, ring the bell again.
    leave: 'South-east to the Ruined Battlefield for Rolan.'
    warn: 'Never follow the convoy to Moonrise instead. Kar''niss climbs the wall with the lantern, Dolly dies inside it, and the blessing is gone for the run. Balthazar''s lantern at Moonrise has no pixie.'
  - step: 6
    location: ruined-battlefield
    title: 'Rolan and the battlefield'
    do: |-
      - Rolan is at the south end of the Ruined Battlefield, south-east of the Tollhouse (X -52, Y -110). Approaching starts the Shadows fight. Once you are close, finish it; leaving or resting kills him.
      - Destroy the everburning torches at X -49, Y 36 to spawn the Shadow Mastiff Alpha, which drops the Shadow-Cloaked Ring for Asterion.
      - The House in Deep Shadows, east of the Shadowed Battlefield waypoint, has the Ring of Mental Inhibition for Gale.
    leave: 'Long rest is safe after this. Then Reithwin.'
  - step: 7
    location: reithwin-tollhouse
    title: 'Gerringothe and the Gloves'
    do: |-
      - Deep curse from here through stop 10; the blessing holds.
      - Gerringothe Thorm can be talked into shedding her gold; her hoard funds Moonrise.
      - Top floor: a Tollhouse Clerk's Key from the wooden desks on the north side opens the room with two locked double doors. The opulent chest inside (DC 10) holds the Gloves of Battlemage's Power. Charles wears them for the rest of the game.
    leave: 'Next door to the Mason''s Guild.'
  - step: 8
    location: masons-guild
    title: 'The Helmet'
    do: |-
      - Enter by the Ornate Hatch (X -127, Y 26) or the control-wheel lift.
      - Basement: a Perception 10 check reveals the Keyholed Herald: Tower-Shaped Key, or Sleight of Hand 18.
      - Leave the first reinforced gilded chest alone, or open it with the party parked back; a failed disarm drops portcullises and wakes three gargoyles.
      - Halfway to the table five Shadows and a Wraith attack.
      - The gilded chest behind the altar holds the Helmet of Arcane Acuity: Perception 15 to see the trap, disarm DC 21, lock DC 14. Picking before disarming fires a level 4 Guiding Bolt, DC 15 save. Bonbon wears it for the rest of Act 2.
      - Infernal Iron is in the backyard. A Perception 10 button on the eastern gallery opens two chests with a Potion of Speed and a Scroll of Knock.
      - **Arabella** waits at the Reithwin graveyard gate (X -153, Y 15), west of the guild and north of the Sharran monument. Agree to help and send her to camp. Do not tell her about her parents in the field.
    leave: 'Across town to the House of Healing.'
  - step: 9
    location: house-of-healing
    title: 'Malus, the ring, the lute'
    do: |-
      - Malus Thorm can be talked into operating on himself.
      - Morgue lab, locked opulent chest: Eversight Ring for Asterion.
      - Take the Battered Lute from Malus for Art Cullagh. Arabella's parents are here.
    leave: 'The Waning Moon is optional; otherwise back to the inn.'
  - step: 10
    location: waning-moon
    title: 'Thisobald (optional)'
    do: |-
      - No plan gear here. Thisobald is a fight or a drinking contest; skip it if time is short.
    leave: 'Back to Last Light Inn.'
  - step: 11
    location: last-light-inn
    title: 'Second visit: Art, Halsin, Arabella'
    do: |-
      - Play the lute for Art. He sends Halsin to the lakeshore portal: hold it four turns. If it breaks, Halsin is gone forever. Thaniel comes through.
      - At camp, tell Arabella about her parents. Told at camp she needs no check; told in the field it is a DC 14 Persuasion or she runs into the curse and dies. After the next long rest she hands over the Shadow Blade Ring for Charles.
      - Dammon: the third spare iron becomes the Flawed Helldusk Gloves for Asterion, if the iron is in hand.
    leave: 'Find Oliver at his cottage.'
  - step: 12
    location: shadow-cursed-lands
    title: 'Oliver and Thaniel'
    do: |-
      - Find Oliver at his cottage and reunite him with Thaniel through the summons. Do not attack the Nightdome directly.
    leave: 'To Moonrise Towers.'
  - step: 13
    location: moonrise-towers
    title: 'Friendly visit'
    do: |-
      - Bonbon talks at the gate and at Ketheric's trial. Accept Z'rell's relic task. Do not touch Ketheric and do not go to the rooftop; he is immortal until the Nightsong.
      - **Shop.** Roah Moonglow: Drakethroat Glaive for Gale's bag, Arrows of Many Targets. Lann Tarv: Sentinel Shield for Bonbon; pass one of his boasting checks for the discount. Araj Oblodra: Risky Ring for Charles, Thunderskin Cloak for Gale, and Astarion bites her for the Potion of Everlasting Vigour. She leaves Moonrise near the end of the act, so all of it happens now.
      - **Upper floor.** The Mimic in Isobel's old bedroom drops the Spineshudder Amulet for Gale.
      - **Prison.** Clear the guards first; the rest of the tower stays friendly. The Warden drops the Spellcrux Amulet for Bonbon and the Moonrise Guard's Key. Wulbren's hammer is in the Warden's office upstairs; give it to him. Break the back walls of cells 2 and 4, walk the prisoners to the boat and free the chains. No long rest or fast travel in the middle of this.
      - Skip the Ketheric's Shield pickpocket. He drops it at the end of the act.
    leave: 'To the Grand Mausoleum in Reithwin, with Shadowheart in the party.'
    warn: 'The prison rescue auto-fails after the Shadowfell.'
  - step: 14
    location: gauntlet-of-shar
    title: 'The Gauntlet, up to the Shadowfell'
    do: |-
      - Grand Mausoleum buttons: Moonrise Towers, Grief, General. Bring Shadowheart for the descent. If she is absent at the Nightsong she leaves for good, and with her present the Silent Library spear is mandatory.
      - **Yurgir.** Raphael offers the contract at the entrance. Talk Yurgir into killing his own or fight him; take his Umbral Gem. The heavy chest north of him holds the Boots of Brilliance for Bonbon.
      - **Trials.** Soft-Step, Self-Same, Faith-Leap. Killer's Sweetheart drops in the Self-Same Trial where the copy dies, for Charles.
      - **Balthazar.** Kill him at his outpost. The opulent chest in his vault holds the Callous Glow Ring for Gale and an Infernal Iron.
      - **Silent Library.** Teachings of Loss opens the Spear of Night and Dark Justiciar Half-Plate. No area damage near the shelves; a destroyed book locks the spear out.
      - One gem on the Pedestal of Reckoning runs the lift, three on the lower altar open the doors.
    leave: 'Stop at the lift down. Run the checklist first.'
  - step: 15
    title: 'Stop: pre-Shadowfell checklist'
    do: |-
      - Crèche and every Act 1 loose end
      - Dammon: third iron turned into Flawed Helldusk Gloves
      - Moonrise: Drakethroat, Sentinel Shield, Risky Ring, Thunderskin, Araj's potion, Spineshudder
      - Prisoners freed, Spellcrux Amulet in hand
      - Art awake, Halsin's portal held, Thaniel and Oliver reunited
      - Rolan back at the inn, Arabella told
      - Reithwin: Gloves, Helmet, Eversight, Shadow-Cloaked, Mental Inhibition
      - Gauntlet: Killer's Sweetheart, Boots of Brilliance, Callous Glow, Yurgir done
      - Shadowheart in the active party
    warn: 'Everything above is gone once the party enters the Shadowfell.'
  - step: 16
    location: gauntlet-of-shar
    title: 'Shadowfell: free the Nightsong'
    do: |-
      - Free Dame Aylin. She is the camp ally who makes Ketheric mortal.
    leave: 'Join Jaheira''s assault on Moonrise.'
  - step: 17
    location: moonrise-towers
    title: 'The assault'
    do: |-
      - Join Jaheira's assault and keep her alive; she is the Act 3 Harper thread.
      - Rooftop Ketheric, then down into the Colony.
    leave: 'Down the lift into the Mind Flayer Colony.'
  - step: 18
    location: mind-flayer-colony
    title: 'The Colony and Ketheric'
    do: |-
      - No camp or fast travel inside; the Restoration Pod by the lift is a long rest.
      - Zevlor is in the pods. Open them, never purge.
      - Necrotic Laboratory: the Resonance Stone is near the Mind-Archive Interface. Asterion carries it.
      - Mizora's pod matters only if Wyll is in camp.
      - Ketheric's final form drops Ketheric's Shield, Bonbon's option over the Sentinel Shield.
    leave: 'The portal returns you to Moonrise, and the inn is reachable again.'
  - step: 19
    location: shadow-cursed-lands
    title: 'Wrap up and the road to Act 3'
    do: |-
      - Charles's Stone respec at Withers: Warlock 5 / Paladin 4, Phalar Aluve to Bonbon, Knife to Charles's bag.
      - Tell Barcus about Wulbren, speak to Rolan at the inn, collect the Tiefling rewards.
      - Take the road west of the Waning Moon. The Emperor offers the Astral-Touched Tadpole on the way: all four commune, per the Tadpole tab.
    warn: 'Halsin, Barcus, Rolan, Arabella and Dolly must be settled before the road.'
  gold:
  - item: Cloak of Protection
    vendor: 'Talli, Last Light'
    gp: 200
    who: Charles
  - item: Amulet of the Harpers
    vendor: 'Talli, Last Light'
    gp: 125
    who: Asterion
  - item: Cloak of Cunning Brume
    vendor: 'Mattis, Last Light'
    gp: 70
    who: Bonbon
  - item: Evasive Shoes
    vendor: 'Mattis, Last Light'
    gp: 95
    who: Gale
  - item: Acrobat Shoes
    vendor: 'Barcus, Last Light'
    gp: 35
    who: 'Gale (option)'
  - item: Tower-Shaped Key
    vendor: 'Mattis, Last Light'
    gp: 1000
    who: any
    note: 'Or talk him out of it: DC 14, then DC 6.'
  - item: Drakethroat Glaive
    vendor: 'Roah Moonglow, Moonrise'
    gp: 960
    who: Gale
  - item: Sentinel Shield
    vendor: 'Lann Tarv, Moonrise'
    gp: 580
    who: Bonbon
  - item: Risky Ring
    vendor: 'Araj Oblodra, Moonrise'
    gp: 190
    who: Charles
  - item: Thunderskin Cloak
    vendor: 'Araj Oblodra, Moonrise'
    gp: 75
    who: Gale
---
