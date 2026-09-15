---
slug: shadow-cursed-lands
name: Shadow-Cursed Lands
act: 2
order: 30
region: Shadow-Cursed Lands
wiki: Shadow-Cursed Lands
summary: 'The Act 2 region. Get curse protection first, then work Last Light Inn, the Ruined Battlefield, Reithwin, Moonrise and the Gauntlet against three cutoffs.'
arrive: |-
  Two entrances, both on the Ruined Battlefield. Travel to Moonrise Towers completes on arrival either way.

  - **Grymforge lift (north, the route this party takes).** The lift opens into a Sharran antechamber; its far gate exits at X: 121 Y: 229. The curse line is at X: 112 Y: 193. Lassandra's Harper scouts are at X: 74 Y: 152 and mark Last Light Inn on the map. Follow the path south-west; the inn is over the bridge at the north-west corner of the battlefield (waypoint X: -17 Y: 133).
  - **Rosymorn Monastery Trail (south-east).** The path comes out at X: 167 Y: -28; the curse line is at X: 139 Y: -33. A goblin sends you to the cultist camp at X: 87 Y: -49, where Kansif waits for a True Soul to summon Kar'niss. Do not summon him. Head north-west across the battlefield to the inn instead.

  Torchlight is enough on the roads and the battlefield. Reithwin, the mansion east of the inn and the ground around Moonrise need a Moonlantern or the Pixie Blessing.
curse: light
items:
- id: moonlantern
  name: Moonlantern
  for: any
  core: false
  where: 'Carried by Kar''niss at the Harper ambush house, X: 10 Y: -20 (his corpse or his hand-over). Also: Isobel at the inn hands over the same lantern if the Harpers took it, and a second, pixie-less lantern sits in a box by the desk in Balthazar''s room at Moonrise (Z''rell''s key).'
  how: 'Kill Kar''niss or talk him out of it (see the Kar''niss NPC entry). Loot the corpse; the Inspect Moonlantern dialogue starts on pickup. Disarming Kar''niss also makes him drop it.'
  note: 'Required to survive the region. Kar''niss after the Harper ambush, or Isobel/Balthazar. Only Kar''niss''s lantern holds Dolly; free her and the lantern becomes a Broken Moonlantern but the party gets the Pixie Blessing instead. A lantern in the weapon set gives Moonshield in a 13 m radius; switching to a ranged weapon keeps Moonshield and drops the light, so Shadow Step and Covert Critical work.'
- id: filigreed-feywild-bell
  name: Filigreed Feywild Bell
  for: any
  core: false
  where: 'Given by Dolly Dolly Dolly the moment she is released from Kar''niss''s Moonlantern.'
  how: 'Inspect Moonlantern, then Release the pixie (or the Rogue quick-unlock). Do not Smash the lantern: that curses the inspector with A Clown in Town. Ask her for help against the curse and she gives the bell.'
  note: 'The Pixie Blessing source. Ring it, answer "Dolly Dolly Dolly, Dolly; won''t you save me from my folly?" (or the "Oh, my lovely Dolly thrice" line) and the whole party is re-blessed. Any other answer polymorphs the speaker for a few turns. Keep it all game: the blessing drops on region changes.'
- id: shadow-of-menzoberranzan
  name: Shadow of Menzoberranzan
  for: any
  core: false
  where: 'loot.md lists it as a Kar''niss drop. The wiki lists it only in Ebonlake Grotto (Underdark, X: 52 Y: -70) next to Xargrim''s corpse, and Kar''niss''s loot table is Cruel Sting and the Moonlantern. Check his corpse anyway.'
  how: 'Loot Kar''niss after the ambush.'
  note: 'Head slot, dropped by Kar''niss (the drider carrying the Moonlantern). Invisibility 1/short rest while in shadow or darkness. A spare escape tool for any scout.'
  verify: true
- id: broken-moonlantern
  name: Broken Moonlantern
  for: any
  core: false
  where: 'On the ground at the top of the Grymforge lift, in the antechamber before the curse. Nere carries another; a third is in Balthazar''s hidden room at Moonrise.'
  how: 'Pick it up. Investigation DC 10 or Arcana DC 10 reveals it ran on a pixie.'
  note: 'Story item. Gale can combine one with a Dead Pixie at the table in Balthazar''s hidden room to make the Shadow Lantern (Moonshield plus a Conjure Shadow Lantern Wraith summon). No pixie to free.'
- id: raven-gloves
  name: Raven Gloves
  for: any
  core: false
  where: 'Reward from He Who Was at his ritual circle, Ruined Battlefield X: 129 Y: 106.'
  how: 'Punish the Wicked: bring Madeline''s Ledger from the Waning Moon, then have Bonbon shame Madeline as a coward (Bard Persuasion DC 10) or make her stab herself once. Forgiving her or a second stab turns He Who Was hostile and forfeits the gloves.'
  note: 'Rare. Summon Quothe the Raven once per short rest; the familiar Blinds with its beak. Spare gloves, nobody in the plan wears them.'
- id: ritual-dagger-of-shar
  name: Ritual Dagger of Shar
  for: any
  core: false
  where: 'On the altar in the hidden room at the bottom of the Sharran Sanctuary, under Ketheric''s statue in Reithwin''s central square (X: -152 Y: -30).'
  how: 'Pass all three statue saves (DC 14 WIS, INT, CHA) to open the room. Taking or moving the dagger spawns the three Sentinels and locks the exit until they die. Shadowheart disapproves unless she takes it.'
  note: 'Uncommon +1 dagger, +1d4 Necrotic. Not plan gear; the fight is the cost. Skip unless you want the XP.'
quests:
- name: Seek Protection from the Shadow Curse
  steps: |-
    - Starts at the Grymforge lift. Carry torches until the inn.
    - At the inn: Jaheira, then Isobel upstairs for the Blessing of Selûne (survive Marcus). The blessing covers the light curse without a torch and resists magical Necrotic.
    - Once Isobel is saved, Branthos's squad waits on the inn bridge. Accept the ambush. They walk to the house at X: 10 Y: -20; catch up or go with them.
    - Talk to Branthos at the house to start it. When the convoy arrives, stay hidden and Kar'niss kills Vez, then signal the Harpers, or pick **Clear your throat** and talk him out of the lantern (see NPC entry). Bonbon does the talking.
    - Loot or accept the Moonlantern. Inspect it, release Dolly, take the bell. Blessing on all four.
  outcome: 'Pixie Blessing on the party, Filigreed Feywild Bell in the bag, a Broken Moonlantern as a souvenir. Reithwin is now open. Quest complete.'
  lockout: 'If the Harpers ambush without you and take the lantern, Isobel hands it over at the inn with Dolly still alive. Following the convoy to Moonrise instead ends the pixie for good.'
- name: Follow the Convoy
  steps: |-
    - Only offered from the Monastery Trail side: the cultist camp at X: 87 Y: -49, Kansif, the Spider's Lyre (Performance DC 16, result irrelevant) or an illithid check (WIS DC 14) summons Kar'niss.
    - **Do not take it.** Riding with the convoy forces the ambush fight against the Harpers with no talk-down, and if Kar'niss reaches Moonrise he climbs the wall with the lantern and Dolly dies inside it.
    - Once you have spoken to Lassandra and Isobel, the cultist camp despawns and this quest is gone. That is the intended state for this party.
  outcome: 'Skipped. The Moonlantern comes from the Harper ambush instead.'
  lockout: 'Kar''niss arriving at Moonrise with the lantern kills Dolly and the Pixie Blessing for the run.'
- name: Lift the Shadow Curse
  steps: |-
    - Ask Halsin at camp how to lift the curse. He names Thaniel, the land's spirit.
    - The clue is Art Cullagh, asleep in the inn infirmary, singing about Thaniel. Wake him with Malus Thorm's Battered Lute (House of Healing, Reithwin). Tell Halsin.
    - Meet Halsin at the lakeshore north of the inn, just outside Isobel's dome. Hold the portal **four turns** against three waves (Shadows, Wraiths, Shadow Mastiffs, Shadow Creepers, cursed Harpers, Fists, githyanki). Enemies target the portal first. Stack Bonbon and Gale on the stairs, kill the ranged ones.
    - Halsin returns with a sleeping Thaniel and joins as a companion. Now find Thaniel's other half: Oliver, at the House in Deep Shadows (Ruined Battlefield, X: 68 Y: 36, marked House of Flowers).
    - Tell Oliver who he is. He storms off through a portal to Reithwin's central square (X: -152 Y: -26). Follow it.
    - The Nightdome fight: Oliver sits in a dome that reflects damage twofold as Necrotic. **Never hit the dome.** Kill his summons instead: Mummy, Daddy and Shadow Plush each knock 60 Force off it, each Shadow Friend 10. He summons five Friends every round, so clear them every round.
    - When the dome breaks, be kind or let Halsin talk. Oliver always agrees. Thaniel wakes at camp by Halsin's tent.
  outcome: 'Halsin recruited, Thaniel awake at camp. The curse itself lifts only after Ketheric dies and you take the road to Baldur''s Gate.'
  lockout: 'Portal destroyed: Halsin lost forever. Nightdome destroyed by direct damage: Oliver stays hostile and the quest cannot finish. Leaving Act 2 with it unresolved: Halsin stays behind.'
- name: Punish the Wicked
  steps: |-
    - He Who Was sits at a ritual circle on the Ruined Battlefield, X: 129 Y: 106, east of the inn, communing with Madeline's corpse. Agree to help without asking for pay.
    - Madeline's Ledger is under a loose plank behind the bar of the Waning Moon, Reithwin, X: -223 Y: -78 (Perception check).
    - Bring it back. He channels Madeline. Bonbon talks: **[BARD] [PERSUASION] Yours is a classic tale of cowardice** (DC 10) shames her and satisfies him. Or the plain Persuasion coward line (DC 10), or one stab (DC 14).
    - **Charles is Oath of Vengeance.** Forgiving her, stopping her mid-stab, or attacking He Who Was before the ritual breaks his oath. Shaming her does not.
    - A failed roll fades the connection; he still rewards you. Do not forgive her and do not order a second stab; both make him attack.
  outcome: 'Raven Gloves. Killing him instead gives his body loot and an extra fight (Burden of Time: disadvantage on saves for non-elves within 3 m; Shadow Spear 1d6 + 4d12 Necrotic).'
  lockout: 'Forgiving Madeline or a second stab: he attacks, no gloves.'
lockouts:
- what: 'Kar''niss reaches Moonrise with the lantern'
  closes: 'Dolly, the Pixie Blessing and the bell for the run'
  avoid: |-
    Never ride with the convoy. Ambush it with Branthos's Harpers from the inn side and take the lantern there. Balthazar's lantern at Moonrise has no pixie.
- what: 'Turning the lantern mechanism twice'
  closes: 'Dolly dies; the lantern still works but no blessing, no bell'
  avoid: |-
    In the Inspect Moonlantern dialogue pick **Release the pixie**. Never pick *Turn the mechanism* (Crown and Ancients oathbreak on the first turn, death on the second). Never *Smash the lantern* (clown facepaint curse). Never *Ignore the pixie*.
- what: 'The Dark Urge crushes Dolly'
  closes: 'Pixie Blessing, and Charles''s oath'
  avoid: |-
    Let Bonbon or Asterion inspect the lantern. If Charles does it, take **[DARK URGE] Refuse to crush her. Ask her for help against the shadow curse.** Crushing her is an oathbreak for every Paladin oath and gives nothing but an inspiration.
- what: 'Isobel dies during Marcus''s attack'
  closes: 'Every inn vendor and quest, Branthos''s ambush, Rolan''s family reunion, Art Cullagh'
  avoid: |-
    Keep her above 0 HP. Kill Marcus and the winged ghouls fast; she is the win condition. See the Last Light Inn page.
- what: 'Attacking the Nightdome directly'
  closes: 'Lift the Shadow Curse, Halsin as a companion'
  avoid: |-
    Kill Oliver's summons only. Mummy, Daddy and Shadow Plush each deal 60 Force to the dome; Shadow Friends 10. If Oliver is left hostile after the dome breaks, Dominate Person is the reported fix.
- what: 'Halsin''s portal is destroyed'
  closes: 'Halsin forever; the curse cannot be lifted'
  avoid: |-
    Four turns, three waves, portal is the enemy priority. Pre-buff, hold the stairs, shoot the archers and casters first. No fast travel or camp mid-fight.
- what: 'Elminster never reaches Gale'
  closes: 'Gale leaves for good after the Apostle of Myrkul or at Wyrm''s Lookout'
  avoid: |-
    Gale must have eaten at least one magic item. The Weary Traveller stands in the Sharran ruins where the Grymforge lift exits, or near the Monastery Trail entrance, or on the Moonrise bridge, or turns up at camp on a long rest. Talk to him with Gale. Do not fight him.
- what: 'Walking past the footbridge north-west of the Waning Moon before Ketheric is dead'
  closes: 'Nothing permanent, but the party is arrested and dumped in Moonrise prison'
  avoid: |-
    Stay east of the Road to Baldur's Gate waypoint (X: -265 Y: -36) until Ketheric is dead. The Absolute's army camps behind that bridge all act.
- what: 'Taking the road west of the Waning Moon (Act 3 exit)'
  closes: 'Everything in Act 2. Halsin stays behind if Lift the Shadow Curse is unresolved. Rescue the Tieflings rewards are void in Act 3.'
  avoid: |-
    Only after Ketheric. Before the road: Halsin's quest complete (Thaniel and Oliver reunited), Rolan spoken to at the inn, Barcus told about Wulbren, Arabella told about her parents and her ring collected, the Tiefling rewards collected, Dolly freed. The game warns before the transition; take the warning seriously. The Emperor offers the Astral-Touched Tadpole on the way; all four commune, per the Tadpole tab.
- what: 'Entering the Shadowfell (Gauntlet of Shar)'
  closes: 'Act 1 maps, the Crèche, Dammon''s crafting, Moonrise as a friendly place, the prison rescue'
  avoid: |-
    Run the pre-Shadowfell checklist in the route before the Nightsong. See the Gauntlet of Shar page.
- what: 'A long rest while Rolan is out in the curse'
  closes: 'Rolan'
  avoid: |-
    See the Ruined Battlefield page. He leaves the inn the moment Isobel is saved and you fast travel or rest; rescue him before the next long rest.
npcs:
- name: Kar'niss
  role: 'Boss: Moonlantern bearer (drider, Lvl 6, 184 HP, AC 19)'
  note: |-
    Convoy guide for the Absolute. Talk-down path, only when ambushing with the Harpers from the inn side: pick **Clear your throat to make yourself known** (no check). Greeting: **The Absolute protected me** or the Bard line; never Shadowheart's or a Cleric line, those start combat. First check: **[BARD] [DECEPTION] Our wondrous Queen dropped me a message** (DC 10) or plain Deception DC 14. Second check: **[BARD] [DECEPTION] Vale, idiotae!** (DC 14), or **[OATH OF VENGEANCE] [INTIMIDATION]** DC 14 from Charles, or plain Deception or Intimidation DC 14. He hands over the lantern and the convoy walks into the dark; they reappear as Shadow-Cursed Undead south of Ketheric's statue in Reithwin, hostile. If you fight: Spindleweb Fanaticism gives his allies +1d6 Psychic, Multiattack triggers on any wounded target (3x 1d8+4), Venom Claws 3d6+3 plus 2d8 Poison. Alert, cannot be surprised. Drops Cruel Sting and the Moonlantern.
- name: Dolly Dolly Dolly
  role: 'Pixie in the Moonlantern'
  note: 'Free her, take the bell, ask nicely. Speak to her any time by ringing the Filigreed Feywild Bell. If freed, Jelliwig in Act 3 (Stop the Presses) recognises the party.'
- name: Lassandra
  role: 'Harper scout, first contact from the Grymforge side'
  note: 'At X: 74 Y: 152 with Karrow, Meygan and Yonas. Yonas is taken by Shadows mid-dialogue; six Shadows plus cursed Yonas attack. Keep the other three alive. She marks Last Light Inn on the map. Vengeance Paladin and Monk intro lines are safe.'
- name: Branthos
  role: 'Harper, runs the convoy ambush'
  note: 'Patrols the inn plaza; after Jaheira and once Isobel is saved, waits on the inn bridge with Elindale, Lassandra, Manus and Skywin. Accept his ambush. Talk to him again at the ambush house to trigger it. He dies off-screen at Moonrise during the Harper assault.'
- name: He Who Was
  role: 'Quest-giver and hidden vendor'
  note: 'Shadar-kai at X: 129 Y: 106 with a white raven. Gives Punish the Wicked. No vendor icon, but the Trade button in dialogue works: scrolls, valuables, Divine Bone Shards and Xorn Scales. Lvl 6 ranger with Misty Presence (goes invisible after taking damage) if it comes to blows.'
- name: Oliver
  role: 'Thaniel''s shadow half'
  note: 'House in Deep Shadows. Two rounds of hide-and-seek give the Ring of Shadows; refusing to play summons Mummy, Daddy and Doggy. After Halsin rescues Thaniel, confronting Oliver sends him to Reithwin for the Nightdome fight. Arcana DC 14 (or Monk Insight DC 14) reads his true nature.'
- name: Thaniel
  role: 'Spirit of the land'
  note: 'Comes through Halsin''s portal asleep, wakes at camp when Oliver rejoins him. Talking to him confirms the curse lifts only after Ketheric.'
- name: Elminster (Weary Traveller)
  role: 'Gale''s quest'
  note: 'Appears once Gale has eaten a magic item: the Sharran ruins at the Grymforge lift exit, the Monastery Trail entrance, the Moonrise bridge, or camp on a long rest. Follows you to camp and stabilises the orb. Do not attack; he has no loot and it kills Gale''s quest.'
- name: Kansif and the convoy camp
  role: 'Cultist relay (Monastery Trail side)'
  note: 'X: 87 Y: -49: Kansif (Lvl 5 evoker, Fireball), Bedi, Gronag, Vez, Lora. Gronag baits a hyena into the curse; stop him for a Dark Urge inspiration. Kansif wears the Thermoarcanic Gloves. The camp despawns once you have met Lassandra and Isobel.'
checks:
- what: 'Curse lines'
  note: 'X: 112 Y: 193 (north) and X: 139 Y: -33 (south-east): the greenish-black emanations. Cross without light and turn-based mode starts; 2d4 Necrotic doubling each turn, cap 16d4. A party member killed in it revives as Shadow-Cursed Undead; kill and resurrect them.'
- what: 'Sharran Sanctuary plaques'
  note: 'Around the base of Ketheric''s statue, Reithwin square X: -152 Y: -30. Three Perception DC 10 checks find three plaques. Read them north, west, east and the south face drops open. Entertainer and Sage inspirations.'
- what: 'Sharran Sanctuary statues'
  note: 'Three statues, one blessing each until long rest: south-east WIS +5, north-east INT +5, centre CHA +5. Each is a DC 14 save of that stat; different characters may roll. Failure gives -5 instead and spawns three Sentinels who lock the exit. Clerics have advantage on all three, Warlocks on CHA. Shadowheart auto-passes while loyal to Shar and has disadvantage after freeing the Nightsong. All three passed opens the altar room: Religion DC 10 for a blood rite that yields an Elixir of Necrotic Resistance, Potion of Angelic Reprieve, Scroll of Revivify and Scroll of Blight.'
- what: 'Broken Moonlantern at the lift'
  note: 'Investigation DC 10 or Arcana DC 10 reveals the pixie dust.'
- what: 'Feywild Bell riddle'
  note: 'Correct answers: "Dolly Dolly Dolly, Dolly; won''t you save me from my folly?" or "Oh, my lovely Dolly thrice who is so very sweet and nice". Wrong answers polymorph the speaker (toad, pig, cow).'
tips: |-
  **Curse mechanics.** Three states share one stack (SCL_SAFE): Moonshield from a lantern, Pixie Blessing, or the Shadow Curse itself. Light curse (battlefield, roads): a torch, Light, Dancing Lights, Produce Flame, Daylight, a glowing weapon, or Isobel's Blessing of Selûne. Deep curse (Reithwin around its waypoint, the mansion east of the inn, the approach to Moonrise): only a Moonlantern, the Shadow Lantern or the Pixie Blessing; weak lights are snuffed. Shadowheart is immune to the light curse only, and only while loyal to Shar. Remove Curse clears the condition until you re-enter. Last Light Inn and Moonrise Towers are protected zones.

  **Blessing of Selûne** comes from Isobel's prayer after Marcus; it covers everyone including camp companions for the act and survives her death. **Pixie Blessing** comes from Dolly and is stronger, hands-free, and shared with anyone who joins the party. It can fall off when you change regions (Act 1 trips, the Shadowfell). Ring the bell and ask nicely.

  **Waypoints.** Last Light Inn X: -17 Y: 133; Shadowed Battlefield X: 46 Y: 17; Reithwin Town X: -78 Y: -46; Grand Mausoleum X: -173 Y: 80; Moonrise Towers X: -157 Y: -97; Road to Baldur's Gate X: -265 Y: -36.

  **Sub-pages.** Last Light Inn (vendors, Isobel, Rolan, Art, Dammon, the Hat). Ruined Battlefield (Rolan's rescue, Shadow Mastiff Alpha, House in Deep Shadows, ambush loot). Reithwin Town (Tollhouse, Mason's Guild, House of Healing, Waning Moon, the acuity run). Moonrise Towers (friendly visit, prison, rooftop). Gauntlet of Shar (Yurgir, trials, Balthazar, Nightsong).

  **Exit.** The road west of the Waning Moon, past the footbridge and the Absolute's camp, is the way to Act 3 and opens only after Ketheric. Before you take it: Halsin's quest complete, Rolan spoken to, Barcus told about Wulbren, Arabella told and her Shadow Blade Ring collected, Tiefling rewards collected, Dolly freed, Charles's Stone respec done. Leaving with Lift the Shadow Curse unfinished means Halsin waves you off at the road and is never seen again.
---
