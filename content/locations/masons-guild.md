---
slug: masons-guild
name: 'Mason''s Guild'
act: 2
order: 80
region: Shadow-Cursed Lands
wiki: 'Mason''s Guild'
summary: 'Reithwin''s guildhall and the Selûnite resistance hideout under it: the Helmet of Arcane Acuity for Bonbon, an Infernal Iron for Dammon, and the end of Investigate the Selûnite Resistance.'
arrive: 'Deep curse. All of Reithwin needs the Pixie Blessing or a lit Moonlantern in hand; torches and Isobel''s blessing do nothing here. Reithwin Town waypoint (X -78 Y -46), then north-east. Ways in: the ruined bridge from the Ruined Battlefield at X -59 Y -22 to the eastern gate, either gate off the streets or the central square, or the vines up from the Reithwin Graveyard. Basement: the Ornate Hatch in the corner of the farthest ground-floor room (X -127 Y 26), or the Control Wheel on the side balcony (X -129 Y 23), which runs a lift down to the cellar.'
curse: deep
items:
- id: helmet-of-arcane-acuity
  name: Helmet of Arcane Acuity
  for: Bonbon
  core: true
  where: 'Secret basement. Gilded chest behind the altar at the far end of the Mason''s Hall (X 107 Y -758).'
  how: 'Perception 15 to see the trap. Sleight of Hand DC 21 to disarm, then DC 14 for the lock. Picking before disarming fires a level 4 Guiding Bolt, DC 15 save. Send Asterion alone with a Trap Disarm Toolkit; the others wait out of the blast.'
  note: 'Act 2: the Mason''s Guild is in Reithwin, not the Act 3 Lower City. Every weapon hit that deals damage gives 2 turns of Arcane Acuity (+spell attack and save DC per stack). This is the Bard''s control engine: Slashing Flourish to stack it, then the Band control spell. Light Armour, +1 Dexterity saves. Bonbon wears it for the rest of Act 2.'
- id: tower-shaped-key
  name: Tower-Shaped Key
  for: any
  core: false
  where: 'Not here. Mattis sells it at Last Light Inn. If Mattis is dead it is in a cobwebbed pouch behind the main bar.'
  how: 'Ask Mattis if he sells anything special. Pay 1,000 gp, or talk: Deception 14 (Mol said I could have it) then a DC 6 follow-up, or Persuasion 14 then a DC 6 follow-up.'
  note: 'Opens the Keyholed Herald in the basement. Without it the Herald is Sleight of Hand DC 18.'
- id: infernal-iron
  name: Infernal Iron
  for: any
  core: false
  where: 'Backyard, on the ground at X -102 Y 18 (the item page says X -105 Y 18).'
  how: 'Pick it up.'
  note: 'For Dammon at Last Light Inn. Karlach''s engine first if she is in camp; otherwise Flawed Helldusk Armour, then Helmet, then Gloves, in that fixed order. Asterion''s Gloves need the third spare piece. Crafting closes at the Shadowfell.'
- id: masons-log
  name: 'Mason''s Log'
  for: any
  core: false
  where: 'Stone table at the end of the Mason''s Hall (X 108 Y -748).'
  how: 'Walk to the table. Five Shadows and a Wraith attack about halfway there. Read it.'
  note: 'Morfred''s journal. Reading it completes Investigate the Selûnite Resistance. The "man who was no man" is Raphael; this deal is the origin of Yurgir''s contract on the Dark Justiciars.'
- id: masons-letter
  name: 'Mason''s Letter'
  for: any
  core: false
  where: 'Same table (X 107 Y -743).'
  how: 'Read it.'
  note: 'Morfred to his brother Halfred: he built Moonrise and its prison and wants to help the Harpers break in. Lore only.'
- id: note-from-the-mason
  name: Note from the Mason
  for: any
  core: false
  where: 'Pinned to the wall inside the passage the Keyholed Herald opens.'
  how: 'Read it.'
  note: 'A threat to thieves. The reinforced chest around the corner is the trap it warns about.'
- id: moonrise-diagram
  name: Moonrise Diagram
  for: any
  core: false
  where: 'Table on the eastern gallery (X 122 Y -737), beside the secret-door button.'
  how: 'Read it.'
  note: 'Adds a stash in the Moonrise Towers prison dungeon to the map. The bookcase next to it holds a random uncommon or rare spell scroll; every other bookcase is common books.'
- id: potion-of-speed
  name: Potion of Speed
  for: any
  core: false
  where: 'Heavy chest behind the secret door on the eastern gallery.'
  how: 'Perception 10 reveals a button at X 123 Y -739. Press it. The chest also holds a Potion of Invisibility, a Potion of Glorious Vaulting and an Elixir of Darkvision.'
  note: 'Haste in a bottle for a fight where Gale''s Twinned Haste goes elsewhere.'
- id: scroll-of-knock
  name: Scroll of Knock
  for: any
  core: false
  where: 'Second heavy chest behind the same secret door.'
  how: 'Same button. The chest is all scrolls.'
  note: 'Knock opens locks Asterion cannot pick, including the surgical bed in the House of Healing.'
- id: trap-disarm-toolkit
  name: Trap Disarm Toolkit
  for: any
  core: false
  where: 'Workbench in the farthest ground-floor room (X -117 Y 31), next to the Ornate Hatch, with Thieves'' Tools and a Scroll of Burning Hands.'
  how: 'Pick it up before going down.'
  note: 'Disarming any trap consumes one. Both gilded chests and the gargoyle statues (Sleight of Hand DC 10 each) need it.'
- id: barkskin-recipe
  name: Barkskin Recipe
  for: any
  core: false
  where: 'Ground floor of the main building (X -110 Y 3).'
  how: 'Pick it up.'
  note: 'Unlocks the Elixir of Barkskin recipe: Salts of Gnarled Tree Bark plus a Mud Mephit Wing or Laculite suspension.'
quests:
- name: Investigate the Selûnite Resistance
  steps: |-
    - Starts at Inquisitor Verzen Wranlock's skeleton on the Ruined Battlefield (X -35 Y -88, Investigation Notes) or at the Potter's Chest (X -52 Y 11, lock DC 14; its key is at X -34 Y 13 behind a Perception check).
    - Progresses at Last Light Inn: the Tower-Shaped Key from Mattis, and Halfred's Note on the Selûnite shrine in the cellar past the Meenlocks.
    - Here: Perception 10 in the basement reveals the Keyholed Herald on the western wall. Open it with the key or Sleight of Hand DC 18.
    - Walk the Mason's Hall to the table. Kill the five Shadows and the Wraith. Read the Mason's Log.
  outcome: 'Quest complete. Morfred''s deal with Raphael explains Yurgir''s contract in the Gauntlet of Shar. Morfred himself is the Infernal Mason in the House of Hope in Act 3.'
- name: 'The Hellion''s Heart'
  steps: |-
    - Take the Infernal Iron from the backyard (X -102 Y 18).
    - Give it to Dammon at Last Light Inn. Karlach's engine first if she is in camp; otherwise the next Flawed Helldusk piece.
  outcome: 'Karlach''s Heart Ablaze, or one Flawed Helldusk piece for the party.'
  lockout: 'Dammon stops crafting once the party enters the Shadowfell.'
lockouts:
- what: 'Entering the Shadowfell with the Infernal Iron still in the bag'
  closes: 'Dammon''s Flawed Helldusk piece from this iron'
  avoid: |-
    Hand the iron to Dammon on the next Last Light Inn visit. The pre-Shadowfell checklist (stop 15) checks this.
- what: 'Taking the road west of the Waning Moon to Act 3'
  closes: 'Reithwin and everything left in this basement, the Helmet included'
  avoid: |-
    Loot the Helmet on the Reithwin run (stop 8). The game warns before the road.
npcs:
- name: Korrilla
  role: Cameo
  note: 'Raphael''s agent, watching from X -110 Y -20 by the central gates. She teleports away when approached; a fast party gets one throwaway line. No fight, no quest.'
- name: Wraith and five Shadows
  role: Ambush
  note: 'Spawn about halfway to the table, gallery or floor, whichever route you take. The trigger is distance to the table. Approach from Stealth so the party acts first.'
- name: Gargoyle Statues
  role: Trap
  note: 'Three Fire Bolt gargoyles in a niche behind the first reinforced chest. They wake only on a failed disarm of that chest. Sleight of Hand DC 10 with a Trap Disarm Toolkit crumbles one; they can also be destroyed.'
checks:
- what: 'Keyholed Herald, basement western wall (X 129 Y -692; the key page says X 123 Y -688)'
  note: 'Perception 10 to see it. Tower-Shaped Key or Sleight of Hand DC 18. Opens the passage to the secret area.'
- what: 'Reinforced gilded chest (X 104 Y -700), left past the passage'
  note: 'Perception 15 shows the trap; disarm and lock are both Sleight of Hand DC 14. A failed disarm raises two portcullises around whoever is at the chest, opens the wall behind it on three Fire Bolt gargoyles, and starts turn-based mode. The chest weighs 250 kg and cannot be moved. Send Asterion alone with a toolkit and keep the other three back at the passage, or skip it. Contents are not listed on the wiki; verify in game.'
- what: 'Gilded chest behind the altar (X 107 Y -758)'
  note: 'Perception 15, disarm DC 21, lock DC 14. Guiding Bolt trap. Helmet of Arcane Acuity.'
- what: 'Eastern gallery button (X 123 Y -739)'
  note: 'Perception 10. Opens a secret door to two heavy chests: potions (Speed, Invisibility, Glorious Vaulting, Elixir of Darkvision) and scrolls (Knock).'
- what: 'Odd-looking bones on the marble plinth, ground floor'
  note: 'Perception check, no DC on the wiki. The Grand Mason''s remains. Inspiration for Guild Artisan and Entertainer backgrounds only.'
- what: 'Roof and balcony'
  note: 'Heavy chest with gold on the roof (X -113 Y 0). Two skeletons at X -115 Y 22: alchemy ingredients, gold, a Potion of Greater Healing.'
tips: |-
  - Order inside: Barkskin Recipe, workbench toolkit, backyard iron, then down the hatch. Herald, skip or solo the first chest, table fight, log and letter, altar chest, gallery button and diagram.
  - Asterion picks every lock here. The Helmet chest is the only DC 21; a Guiding Bolt at one Monk is survivable, so pick it even if the disarm fails.
  - Bonbon puts the Helmet on as soon as it drops. Nothing here waits on the Tollhouse.
---
