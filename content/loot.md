---
loot_guide:
- act: 1
  areas:
  - area: Nautiloid (Prologue)
    items: []
    events:
    - name: Recruit Lae'zel
      note: Freed from her pod on the ship.
    - name: Tadpole / Illithid Powers unlock
      note: Infected here; the Dream Guardian unlocks the tree later.
  - area: Ravaged Beach / Dank Crypt & Camp
    items:
    - name: Silver Pendant
      for: Shared utility swap
      core: true
      note: 'On a skeleton at the Harper outpost southwest of the Grove (X: 152 Y: 366). Grants Guidance at will. MANDATORY PICKUP: there is no Cleric level anywhere in the party, so this pendant is the ONLY source of Guidance for the whole run. Grab it before the Grove and keep it as a shared exploration swap. Do not feed it to Gale''s orb.'
    - name: Deathstalker Mantle
      wiki: The Deathstalker Mantle
      for: Asterion
      core: true
      note: DARK URGE ONLY — Sceleritas Fel, at camp. Kill → Invisible 2 turns, once per turn. Charles receives it and hands it to Asterion.
    events:
    - name: Withers — recruit + RESPEC
      note: Dank Crypt sarcophagus (Overgrown Ruins). Respec 100g, revive, hirelings — required for every respec in this plan.
    - name: Recruit Shadowheart, Astarion, Gale
      note: Beach/cliffs area.
  - area: Emerald Grove
    items:
    - name: Ring of Protection
      for: Gale
      core: true
      note: 'Mol''s reward for Steal the Sacred Idol, after the Grove resolves (not pickpocketed). +1 AC and +1 to all saving throws, and the item guides say to put it on the party''s lowest AC — that is Gale, at AC 15 in Spidersilk Armour against Asterion''s 21 unarmoured. The save bonus is also concentration insurance for Twinned Haste, which the whole party plan rests on. Asterion takes the Bracing Band at Grymforge instead and loses nothing.'
    - name: Corellon's Grace
      for: Asterion
      core: true
      note: 'Auntie Ethel. LEVELS 2–4 ONLY: +1 to Flurry/bonus punches, +2 saves unarmoured. ⚠ Unequip at char 5 — main-action attacks otherwise swing the staff and lose Tavern Brawler.'
    - name: Safeguard Shield
      for: any
      core: false
      note: 'Sold by Dammon. +2 AC and +1 to all saving throws. NOT GALE''S — Dual Wielder at character level 4 fills both his hands with staves, so he can never hold a shield. Bonbon is the only other shield-proficient member, and both her melee hands hold stat sticks she never swings (Club of Hill Giant Strength and the Knife of the Undermountain King, whose crit-threshold reduction is global); treat this as a sellable or a stopgap for her before the Adamantine Splint at Grymforge.'
    - name: Broodmother's Revenge
      for: Bonbon
      core: true
      note: Save the Grove, talk Kagha down, then knock her out non-lethally while isolated. Any healing coats Titanstring for +1d6 Poison per projectile, 2 turns — potion up before a Flourish nova. Skip vs poison immunity.
    - name: The Whispering Promise
      wiki: The Whispering Promise
      for: Bonbon
      core: true
      note: 'THE LEVEL 1–3 BLESS FIX. Volo (or Grat at the Goblin Camp), ~40g. Healing a creature gives it +1d4 to attacks and saves for 2 turns, no Concentration. ⚠ It applies the SAME condition as the Bless spell, so it does NOT stack with Charles''s Bless and is NOT enhanced by the Staff of Arcane Blessing — its job is the char 1–3 window before Charles has Bless at all, and later any turn Charles concentrates on Hex or Darkness instead. Best trigger is a THROWN Potion of Healing, which blesses every creature it splashes; Bonbon''s bonus-action Healing Word covers one, and it also fires Broodmother''s Revenge. Works even on a target at full HP. ⚠ Consumable by Gale — do not feed it to the orb.'
    - name: Hellrider's Pride
      wiki: Hellrider's Pride
      for: any
      core: false
      note: 'Zevlor (loot, steal, or the Kagha quest reward). Healing another creature gives it resistance to weapon Bludgeoning/Piercing/Slashing for 2 turns. Rated #6 of 20 Act 1 items, and still not a standing pick: the glove slot is spoken for on every member — Bonbon wears Gloves of Dexterity (the #1 item), Charles Gloves of Baneful Striking, Asterion Bracers of Defence, Gale Gloves of Belligerent Skies. Bag it and swap it in for a stretch of heavy physical damage, which is when Blade Ward is worth more than any of those.'
    - name: Gloves of Power
      for: any
      core: false
      note: 'Za''krug at the Grove gate. +1 Sleight of Hand; a branded wearer''s hits inflict Absolute''s Bane (−1d4 attacks and saves). Pickpocket helper, not a +attack/DC item.'
    - name: Sorrow
      for: any
      core: false
      note: Hidden Vault at the Wolf altar (Enclave Library puzzle). +1 reach glaive with Sorrowful Lash — decent early reach weapon.
    events:
    - name: ⚠ Strange Ox — DO NOT KILL IT HERE
      note: 'The wandering Strange Ox in the Grove carries the Hat of Fire Acuity ONLY from Act 2 onward — kill it here and you get just the Shapeshifter''s Boon Ring, and Gale''s entire build loses the item it depends on. Leave it alone; kill it at Dammon''s blacksmith in Last Light Inn in Act 2. If you miss it there, it reappears in Rivington on a hill west of the requisitioned barn in Act 3.'
    - name: Save the Grove
      note: Central Act 1 hub — good (kill the goblin leaders) vs evil (raid with Minthara).
    - name: Recruit Wyll
      note: Training tieflings at the grove.
  - area: Sunlit Wetlands (Auntie Ethel)
    items:
    - name: The Sparkle Hands
      for: Asterion
      core: true
      note: Chest under the giant tree, Decrepit Sanctuary. Lightning Charges per unarmed hit → advantage vs metal armour and constructs. Offensive Bracers alternative.
    - name: Auntie Ethel's Hair
      for: any
      core: true
      note: 'Vanilla: one permanent +1, uncapped. Modded run: one per member — Charles/Bonbon/Gale CHA 17→18, Asterion DEX 17→18.'
    events:
    - name: Get the Hag's Hair
      note: Fight Ethel below 20% HP, then let her take a turn to offer the bargain. Accept → Hair, she escapes; killing her gives nothing. Letting her go can break non-Devotion oaths — fine for Charles's Oathbreaker path.
    - name: Rescue Mayrina
      note: Bitter Divorce questline.
  - area: Blighted Village & Whispering Depths
    items:
    - name: Haste Helm
      for: Charles
      core: true
      note: 'Moss-Covered Chest in the Blighted Village. Three turns of opening Momentum, and Charles keeps it: he has the party''s worst initiative at d4+2 and the longest distance to close, while the Ring of Arcane Synergy supplies his damage rider without consuming the head slot. ⚠ It does not go to Asterion — he has Unarmoured Movement plus Step of the Wind, and his head takes the Circlet of Psionic Revenge. ⚠ Gale has no repositioning of his own until Draconic Fly at character level 12, but his head slot is committed to the Shadespell Circlet and then the Hat of Fire Acuity, so this is never his.'
    - name: Bracers of Defence
      for: Asterion
      core: true
      note: Apothecary's secret cellar. +2 AC unarmoured and shieldless — Asterion's AC.
    - name: Sussur weapons (Dagger/Greatsword)
      wiki:
      - Sussur Dagger
      - Sussur Greatsword
      for: any
      core: false
      note: Blacksmith craft with Sussur Tree Bark (Whispering Depths). On-hit Silence — shuts down enemy casters.
    events:
    - name: The Necromancy of Thay
      note: Permanent Speak with Dead (risky WIS saves). Locked gate, opened with the Dark Amethyst.
    - name: Whispering Depths / Sussur Tree
      note: Silence-bark + Dark Amethyst; Phase Spider Matriarch; a pit drops to the Underdark.
  - area: Goblin Camp
    items:
    - name: Amulet of Misty Step
      for: Charles
      core: true
      note: Gilded chest, Priestess Gut's chambers. Misty Step 1/short rest — solves Charles's approach and elevation.
    - name: Crusher's Ring
      for: Asterion
      core: true
      note: Dialogue or loot from Crusher. +3m speed, stacks with Longstrider — Asterion's second combat ring.
    - name: Gloves of Archery
      for: Bonbon
      core: true
      note: Grat. Proficiency is redundant, but +2 damage per ranged hit — Bonbon's early glove.
    - name: Bow of Awareness
      for: Gale
      core: true
      note: Roah Moonglow, Shattered Sanctum. Fills Gale's unused ranged slot purely for +1 Initiative, to land Haste or Wet first.
    - name: Hand Crossbow +1
      for: Charles + Asterion
      core: true
      note: Farm four copies — Dammon, Roah Moonglow, Derryth Bonecloak, A'jak'nir Jeera. A pair each for Charles and Asterion as ranged fallback.
    - name: Arrows of Darkness
      wiki: Arrow of Darkness
      for: Charles
      core: true
      note: 'Restock from arrow vendors after rests and level-ups. 3m cloud, 3 turns, no Concentration: Bonbon places it, Charles swaps to Phalar and activates Shriek, and Devil''s Sight grants advantage while he holds Bless, Divine Favour or Hex.'
    - name: Boots of Striding
      for: Charles
      core: true
      note: Minthara. Start a concentration buff before entering the cloud → Momentum, plus immunity to Prone and forced movement while concentrating. After the Resonance respec, self-cast Darkness supplies it.
    - name: Gloves of the Growling Underdog
      for: Charles
      core: false
      note: Dror Ragzlin's treasure room. Advantage on melee attacks with 2+ enemies within 3m of the target — for when Darkness Arrows run short; redundant once Risky Ring lands.
    - name: Spidersilk Armour
      for: Gale
      core: true
      note: 'Gale''s Act 1 chest, and the answer to his concentration problem. Worn by Minthara in the Shattered Sanctum — the same kill that yields Charles''s Boots of Striding, so it costs nothing extra. AC 12 + DEX and +1 Stealth, but the reason is ADVANTAGE ON CONSTITUTION SAVING THROWS, which protects Twinned Haste from Act 1 instead of waiting for Armour of Landfall in Act 3. Gale has light armour from Human Civil Militia, and this is his only chest item. ⚠ Costs exactly 1 AC versus going unarmoured (Draconic Resilience is 13 + DEX); Gale has no War Caster and no feat left for one, so the advantage is his only concentration protection for two whole acts.'
    - name: Goblin-leader loot (Gut / Ragzlin / Minthara)
      wiki: false
      for: any
      core: false
      note: Assorted +1 weapons, potions and gold — sweep the Shattered Sanctum before it turns hostile.
    events:
    - name: Volo's Ersatz Eye — permanent See Invisibility
      note: Rescue caged Volo, let him operate at camp → 9m See Invisibility. Dialogue only.
    - name: Recruit Halsin / Minthara
      note: Free Halsin (good) or side with the goblins for Minthara (evil, raids the Grove).
  - area: Zhentarim Hideout (Waukeen's Rest / Risen Road)
    items:
    - name: The Spellsparkler
      for: Gale
      core: true
      note: Florrick's reward for the Waukeen's Rest rescue. Quarterstaff — casting builds Lightning Charges. Gale's early staff.
    - name: Gloves of Thievery
      for: Asterion
      core: true
      note: Brem, after Find the Missing Shipment. Advantage on Sleight of Hand — core thief glove.
    - name: Titanstring Bow
      for: Bonbon
      core: true
      note: Brem. Bonbon's Act-1 ranged weapon — Hill Giant club + Knife in the melee set, Bloodlust when adds can trigger it, Hill Giant elixir for a lone boss.
    - name: Zhentarim vendor stock (Brem / Sparkle)
      wiki: false
      for: any
      core: false
      note: Smokepowder Bombs and Barrels, scrolls, misc gear. The one-stop Act 1 shop, and steal-friendly.
    events:
    - name: Rescue the Grand Duke (Waukeen's Rest fire)
      note: Save Florrick → The Spellsparkler + the Flaming Fist plotline.
    - name: Recruit Karlach
      note: Risen Road. Anders' paladins want her dead — help her or kill her for the reward.
  - area: Underdark
    items:
    - name: Boots of Stormy Clamour
      for: Gale
      core: true
      note: Omeluum (Ebonlake Grotto), after his parasite quest. Inflicting a condition → 2 turns of Reverberation.
    - name: Boots of Speed
      wiki: Boots of Speed
      for: Bonbon
      core: true
      note: 'Worn by Thulla in the Ebonlake Grotto — the same Underdark stop as Omeluum, so it costs no detour. A bonus-action Dash, ranked #14 of the Act 1 top 20 for handing any character Rogue-grade mobility, and Bonbon is the fit: she has no innate movement of her own and an otherwise-empty Act 1 boot slot, so this is the item that stops her wasting turns out of position. ⚠ NOT ASTERION''S — Step of the Wind already gives him bonus-action Dash and Disengage from Monk 2, so the boots would buy him nothing while displacing the Night Walkers. ⚠ Charles keeps BOOTS OF STRIDING, whose immunity to Prone and forced movement while concentrating is load-bearing for him. ⚠ The item guide flags the opportunity-attack rider as bugged, reportedly applying to the WEARER — take these for the Dash, not the defensive text. Boots of Brilliance take the slot in Act 2.'
    - name: Pearl of Power Amulet
      for: Gale
      core: true
      note: Omeluum, same quest. One L3-or-lower slot back per long rest — an extra Haste, Lightning Bolt or Counterspell.
    - name: Melf's First Staff
      for: Gale
      core: true
      note: 'Sold by Blurg. +1 Spell Save DC and +1 spell attacks. Gale holds it OFF-HAND alongside Spellsparkler permanently from character level 4, once Dual Wielder makes the pair legal — neither staff is Light — and the +1 spell attack applies to every individual Scorching Ray ray.'
    - name: The Shadespell Circlet + The Lifebringer
      wiki:
      - The Shadespell Circlet
      - The Lifebringer
      for: Gale
      core: true
      note: Omeluum sells Shadespell (+1 Spell Save DC while obscured — Gale's head). Blurg sells Lifebringer (3 temp HP on gaining Lightning Charges — the defensive alternative).
    - name: Luminous Armour
      for: Charles
      core: true
      note: Selûnite Outpost, trapped chest behind a hidden door. AC 15 + up to 2 DEX; Radiant Smites emit Radiating Shockwaves that penalise nearby enemy attacks.
    - name: Phalar Aluve
      for: Charles
      core: true
      note: 'Longsword in stone near the Selûnite Outpost. ACT 1–mid ACT 2: bind, two-hand, GWM at char 6, Darkness Arrows for advantage. LATE ACT 2 after the Resonance Stone: GWM → Dual Wielder, 3d8 Shadow Blade main hand, Phalar off-hand. Pre-cast Shriek and keep it equipped — the 6m aura covers Charles and Asterion.'
    - name: Staff of Arcane Blessing
      wiki: Staff of Arcane Blessing
      for: Asterion
      core: true
      note: 'ASTERION''S, not Charles''s. Arcane Tower BASEMENT, leaning against a table; the elevator buttons only appear if someone carries Bernard''s Guiding Light ring. It GRANTS Bless as a level 1 spell once per long rest, so the holder needs no Paladin or Cleric level to cast it, and every Bless its wielder casts also applies Mystra''s Blessing, a second +1d4 that lands only on SPELL attack rolls. Asterion holds it, casts Bless out of combat, then unequips it and fights with empty hands - he is the only member with no other use for Concentration. Charles cannot be the Bless caster because his Concentration is permanently Hold Person, and Gale cannot because his is permanently Twinned Haste. WARNING the free cast is 1/long rest and Bless at level 1 covers only THREE creatures. WARNING do not let Gale consume it.'
    - name: Caustic Band + Club of Hill Giant Strength
      wiki:
      - Caustic Band
      - Club of Hill Giant Strength
      for: Bonbon
      core: true
      note: Caustic Band (Derryth) — +2 Acid per weapon hit, scaling with Flourish projectiles. Club from the broken Arcane Tower stool — Light main hand beside the Knife, and STR 19 frees the elixir slot for Bloodlust.
    - name: Elixirs of Bloodlust
      wiki: Elixir of Bloodlust
      for: Bonbon
      core: true
      note: Craft from Worg Fangs; check Cyrel, Derryth, Stonemason Kith. Non-Honour, a kill grants an extra Action that benefits from Extra Attack. Hill Giant Strength instead for a lone boss.
    - name: Ring of Mind-Shielding
      for: Gale
      core: true
      note: Omeluum's parasite-quest reward in the Ebonlake Grotto (persuade, intimidate, pay, trade a story or pickpocket). Advantage on saves against Charmed, and the wearer cannot be possessed or read. Gale's second Act 1 ring beside the Ring of Protection — a charmed Gale is a dropped Haste and a Fireball pointed at his own party, so this is concentration insurance as much as a saving throw.
    events:
    - name: Help Omeluum
      note: Myconid Colony. Reward includes the Amulet of Misty Step or a ring, and opens his shop.
    - name: Arcane Tower
      note: Reactivate the tower; loot the Club of Hill Giant Strength, the Staff of Arcane Blessing in the basement, and scrolls.
  - area: Grymforge
    items:
    - name: Disintegrating Night Walkers
      for: Asterion
      core: true
      note: True Soul Nere. Bonus-action Misty Step 1/short rest + immunity to Web, Entangle and grease-slip.
    - name: Adamantine Splint Armour
      for: Bonbon
      core: true
      note: 'FIRST MITHRAL ORE, poured with the Splint mould. AC 18 flat, ATTACKERS CANNOT LAND CRITICAL HITS, all incoming damage reduced by 2, and melee attackers are sent Reeling. Bonbon is the party''s only Heavy-armour wearer — Fighter 1 taken first grants it, Charles has medium only, Asterion must stay unarmoured and Gale is light-armour-only. Crit immunity is what protects Hold Monster: a concentration save is "DC equal to half the damage taken, or 10, whichever is higher," so a crit roughly doubles the DC, and it also stops Hold Person and Sleeping from handing attackers automatic crits against her. ⚠ NO ADAMANTINE SHIELD IS FORGED. The wiki confirms only the AC BONUS carries over from an inactive melee set, so a shield parked behind her hand crossbows would not bring crit immunity with it — the Splint gives her that outright, and she keeps the Knife of the Undermountain King in her melee off-hand for its global crit-threshold reduction. Protecty Sparkswall stays the swap-in for fights where +1 spell save DC beats 6 AC.'
    - name: Adamantine Scale Mail
      for: Charles
      core: true
      note: 'SECOND MITHRAL ORE, and NO LONGER CHARLES''S CHEST. Medium armour, AC 16 + DEX (max 2) = 18, attackers cannot land critical hits, all incoming damage reduced by 1, and melee attackers are sent Reeling. Charles is now LOCKED to Luminous Armour in every act for its Radiant Shockwave, so he forgoes this crit immunity - which is why he takes the Helm of Balduran in Act 3 to get it back. The second ore is therefore free for whoever wants durability.'
    - name: Grymskull Helm
      wiki: Grymskull Helm
      for: Bonbon
      core: true
      note: 'FREE CRIT IMMUNITY — dropped by Grym, the boss you must kill to use the forge anyway, requiring only heavy armour proficiency, which Bonbon has from Fighter 1. Grants "attackers can''t land Critical Hits on the wearer" plus Fire resistance, for zero ore. HER EARLY STOPGAP HEAD: wear it on the way to the Crèche and retire it the moment the Diadem of Arcane Synergy lands, then the Helmet of Arcane Acuity takes the slot permanently from Act 2.'
    - name: The Protecty Sparkswall
      for: Bonbon
      core: true
      note: Trapped bridge chest at the end of the Grymforge bridge. +1 Spell Save DC for Hold Person, Hypnotic Pattern, Fear, Slow and Glyph — Bonbon's early-Act-1 chest, and the price is low clothing AC at range until the forge. The Adamantine Splint becomes her default the moment it is poured; keep Sparkswall bagged for the fights where +1 spell save DC beats 6 AC.
    - name: Wondrous Gloves
      for: Bonbon
      core: false
      note: Mimic near the Harper cache. +1 AC and an extra Bardic Inspiration = another Slashing Flourish, at the cost of Gloves of Dexterity accuracy.
    - name: Bracing Band
      for: Asterion
      core: true
      note: 'Sergeant Thrinn''s reward for Find the Missing Boots — a free permanent +1 AC almost nobody takes. "After shoving an enemy, the wearer gains a +1 to their Armour Class until their next turn," and per the wiki the trigger is not just Shove: FLURRY OF BLOWS: PUSH is named explicitly. Asterion throws Push as one of his three Open Hand Flurry variants, so on any turn he pushes something the bonus is simply always up — on the party member with no armour to fall back on. ⚠ Thrinn gives ONE of two rewards; take this over the Armour of Uninhibited Kushigo.'
    - name: Armour of Uninhibited Kushigo
      for: Asterion
      core: false
      note: Sergeant Thrinn, for returning her boots — the OTHER half of the choice above, so taking it costs the Bracing Band. Patient Defence gains a reaction unarmed counterattack on a miss. Graceful Cloth is his standing chest anyway, so the Band wins.
    - name: Sentient Amulet
      for: Asterion
      core: true
      note: Locked Adamantine chest near the Lava Elemental. Ki Restoration (2 Ki, 1/long rest) — the Monk's best Act 1 neck. ⚠ The rare version can inflict Hysterical on a failed WIS save.
    events:
    - name: Adamantine Forge
      note: Pour Mithral + mould, then fight Grym (lure him onto the forge). One-time crafting.
    - name: True Soul Nere
      note: Free the deep gnomes or side with the duergar; loot Nere for the Night Walkers.
  - area: Mountain Pass / Rosymorn Monastery / Crèche Y'llek
    items:
    - name: Holy Lance Helm
      for: Charles
      core: true
      note: 'Painted chest on the top level of Rosymorn Monastery. CHARLES''S ACT 2 HEAD, replacing the Covert Cowl. Ignore the printed damage — Smite the Graceless is 1d4 on a fixed DC 14 Dexterity save. Take it for what the Radiant tick plugs into: Radiant damage fires a Luminous Armour shockwave, so it spreads Radiating Orb ON ENEMY TURNS, and the Gloves of Battlemage''s Power research confirms it as a trigger, so it refills Arcane Acuity between his turns — the direct answer to Acuity decaying by 2 every time he is hit. Self-reinforcing, because it only fires when an attack MISSES and Radiating Orb at −10 makes enemies miss constantly. Requires Medium Armour proficiency, which Hexblade grants.'
    - name: Graceful Cloth
      wiki: The Graceful Cloth
      for: Asterion
      core: true
      note: Lady Esther, Rosymorn trail. +2 DEX (cap 20) + Cat's Grace (advantage on DEX checks, helps stealing). Asterion's all-game chest.
    - name: Gloves of Cinder and Sizzle
      for: Asterion
      core: true
      note: Lady Esther. +1d4 Fire per unarmed hit + a level-3 Scorching Ray 1/long rest. Prefer Sparkle Hands vs metal or fire resistance.
    - name: Knife of the Undermountain King
      for: Bonbon
      core: true
      note: A'jak'nir Jeera. Bonbon's melee off-hand beside the Light club. Organ Rearranger lowers the crit threshold for Titanstring and spell attacks; the low-die reroll is melee-only.
    - name: Gloves of Dexterity
      for: Bonbon
      core: true
      note: A'jak'nir Jeera (Crèche). DEX 18 — lets the Bard dump DEX and pump CHA.
    - name: Gloves of Baneful Striking
      for: Charles
      core: true
      note: Lady Esther. Weapon hit → −1d4 to the target's saves for 2 turns, helping Asterion's Stun and the casters' control.
    - name: Circlet of Psionic Revenge
      for: Asterion
      core: true
      note: 'Carried by Githyanki Inquisitor Ch''r''ai W''wargaz in the Crèche Inquisitor''s Chamber. Succeed on a saving throw and the creature that forced it takes 1d4 Psychic — doubled from Act 2 by the Resonance Stone he carries. HIS ONLY LEGAL HEAD: per the wiki, "Helmets and Gloves marked as Light, Medium or Heavy Armour count as armour, and prevent Unarmoured Defence from working," which rules out the Covert Cowl and the Dark Justiciar Helmet for him permanently; this circlet carries no proficiency requirement. ⚠ The +1 to mental saves printed on it is Githyanki-only and he does not get it. Mask of Soul Perception finally replaces it in Act 3.'
    - name: Diadem of Arcane Synergy
      for: Bonbon
      core: true
      note: Ardent Jhe'rezath, Inquisitor's Chamber. Once a spell condition lands, +CHA to each subsequent ranged weapon attack for 2 turns — Titanstring Flourishes exploit it best. Replaced by the Helmet of Arcane Acuity in Act 2.
    - name: Ring of Arcane Synergy
      for: Charles
      core: true
      note: Gish Far'aag, Crèche Y'llek. Booming Blade damage → +CHA to subsequent bound-weapon attacks for 2 turns. Same non-stacking condition as the Diadem, so the Diadem goes to Bonbon.
    - name: Strange Conduit Ring
      for: Charles
      core: true
      note: Crèche Y'llek. +1d4 Psychic on weapon attacks while Concentrating. Resonance Stone vulnerability and crits multiply the dice.
    - name: Gloves of Belligerent Skies
      for: Gale
      core: true
      note: 'Elegant chest in the Inquisitor''s Chamber. Thunder, Lightning or RADIANT damage applies 2 turns of Reverberation, and once the Callous Glow Ring is online in Act 2 every Scorching Ray ray deals 2 radiant, so these proc per ray. ⚠ Charles has a real claim — Divine Smite is Radiant, and the wiki notes Phalar Aluve''s Shriek Thunder triggers them correctly in Honour Mode specifically — but they stay with Gale, who applies the rider 5–7 times per cast against Charles''s two swings. ⚠ Triggers once per attack, so an AoE hits only its first logged target.'
    - name: Necklace of Elemental Augmentation
      for: Gale
      core: false
      note: Inquisitor's Chamber display case. +CHA to native elemental cantrips — for after Pearl of Power is spent, or low-resource fights.
    - name: Periapt of Wound Closure
      for: any
      core: false
      note: Lady Esther. Auto-stabilise + always heal maximum.
    - name: A'jak'nir Jeera — githyanki vendor stock
      wiki: false
      for: any
      core: false
      note: Githyanki weapons, medium armour, whetstones, and the core Gloves of Dexterity / Knife. Clear it (buy or steal) before the Crèche locks.
    - name: Rosymorn / Crèche side-loot
      wiki: false
      for: any
      core: false
      note: 'Boots, potions, githyanki gear, and the Dawnmaster''s Crest path to the Blood of Lathander. (Everlasting Vigour +2 STR is Araj''s Act 2 potion, not a Rosymorn item.)'
    events:
    - name: Blood of Lathander (legendary mace)
      wiki: The Blood of Lathander
      note: Rosymorn puzzle, Dawnmaster's Crest. +3 mace with Sunbeam and a party self-revive-at-0-HP aura — don't miss it.
    - name: Zaith'isk → 'Awakened' permanent buff
      note: Crèche infirmary machine. Pass DC 12/15/18 → permanent Awakened (Illithid powers as bonus actions). A failure is a permanent −2 stat.
- act: 2
  areas:
  - area: Shadow-Cursed Lands
    items:
    - name: Moonlantern
      for: any
      core: false
      note: Required to survive the region. Kar'niss after the Harper ambush, or Isobel/Balthazar.
    - name: Shadow of Menzoberranzan
      for: any
      core: false
      note: Head slot, dropped by Kar'niss (the drider carrying the Moonlantern). Cast Invisibility 1/short rest while in shadow/darkness — excellent for any stealth or scout character (a strong alternative escape/ambush tool alongside Asterion's kit).
    - name: Shadow-Cloaked Ring
      for: Asterion
      core: true
      note: 'THE ACT 2 DAMAGE RING. Carried by the Shadow Mastiff Alpha at the Ruined Battlefield — destroy the everburning torches nearby to make it appear. +1d4 against Lightly or Heavily Obscured creatures and creatures made of shadow, and the wiki names weapon AND UNARMED attacks explicitly, which most riders do not. Nearly everything in the Shadow-Cursed Lands qualifies, so it is roughly +12 across a full Flurry turn. It stays on into Act 3 for obscured interiors and Charles''s Darkness.'
    - name: Ring of Mental Inhibition
      for: Gale
      core: true
      note: 'In a locked chest in the House in Deep Shadows, just east of the Shadowed Battlefield waypoint. When a foe fails a saving throw against Gale''s spells they gain Mental Fatigue for 2 turns, stacking the odds for the next Command — and applying a condition also triggers Boots of Stormy Clamour. ⚠ Per the wiki it does NOT trigger on the saves a creature makes to shake off an existing effect, so it will not extend Hold Person. Swap it in over Coruscation for control-focused fights.'
    events:
    - name: Free the pixie (Dolly Dolly Dolly)
      note: Freeing the pixie grants permanent Pixie's Blessing — curse immunity without the lantern. Missable.
  - area: Last Light Inn
    items:
    - name: Cloak of Protection
      for: Charles
      core: true
      note: 'Quartermaster Talli at Last Light Inn. +1 Armour Class and +1 to Saving Throws. THE ARBITRATION: exactly one exists, and it is the ONLY cloak in the entire Act 2 pool that touches saving throws at all. Charles is the one party member carrying a permanent, self-inflicted DISADVANTAGE on every save from the Risky Ring while holding concentration in melee, and he is the one standing in every area attack. Gale can be positioned out of danger and already has Constitution-save advantage from Spidersilk Armour; Bonbon has War Caster and AC 18. He keeps it through Act 3.'
    - name: Amulet of the Harpers
      for: Asterion
      core: true
      note: 'Quartermaster Talli, Last Light Inn. ADVANTAGE ON WISDOM SAVING THROWS plus Shield 1/long rest. It replaces the Sentient Amulet, and the timing is set by the Resonance Stone: the Stone''s aura hands the whole party disadvantage on mental saves, and advantage cancels that back to a straight roll for the member carrying it. It is also the Act 2 answer to Hold Person, Fear and Dominate.'
    - name: Flawed Helldusk Gloves
      for: Asterion
      core: true
      note: 'Crafted by Dammon at Last Light Inn once he has been given the THIRD piece of Infernal Iron. Unarmed attacks deal an extra 1d4 Necrotic and can inflict Bleeding, plus +1 to Strength saves, and there is no armour tag so Unarmoured Defence survives. Across five strikes a turn that is roughly +12 damage against the +2 AC the Bracers of Defence were giving — take the damage while Act 2 enemies are still soft. ⚠ Budget the Infernal Iron deliberately; the same pieces upgrade Karlach''s engine.'
    - name: Cloak of Cunning Brume
      for: Bonbon
      core: true
      note: 'Sold by Mattis at Last Light Inn for about 70g. Disengaging also creates a 2m fog cloud for a turn, obscuring and blinding everything inside it — a genuine backline escape button for the moment something closes on her. An honest cheap fill: the Act 2 cloak pool is built for melee (Fleshmelter and Thunderskin both trigger on being hit) and the one unconditional cloak goes to Charles. She upgrades to Wavemother''s Cloak in Act 3.'
    - name: Shadow Blade Ring
      wiki: Shadow Blade Ring
      for: Charles
      core: true
      note: Arabella's reward for Find Arabella's Parents, delivered at camp. Bonus-action Shadow Blade, short-rest recharge, no concentration — Charles's backup blade.
    - name: Coruscation Ring
      for: Gale
      core: true
      note: 'Trapped chest in a hidden cellar room. THE ILLUMINATION ENGINE: it applies Radiating Orb when the WEARER is illuminated — the target does not need to be lit. Radiating Orb then makes the target Illuminated, which switches on Callous Glow''s +2 radiant, which procs Gloves of Belligerent Skies'' Reverberation. Since only GALE needs light, this never conflicts with Charles standing in a Darkness cloud. Keep Gale lit with the Light cantrip early, then Daylight (Enchant Item) on Bonbon''s weapon from character level 8.'
    - name: Covert Cowl
      wiki: Covert Cowl
      for: Charles
      core: true
      note: 'Cellar, on a Meenlock. NOW THE ALTERNATE ACT 2 HEAD, behind the Holy Lance Helm: −1 crit threshold while Obscured, and standing inside his own Darkness is Heavily Obscured. ⚠ Same redundancy that demoted Risky Ring and Killer''s Sweetheart — you cannot improve on a guaranteed crit, so a lowered crit threshold is worth nothing on any turn the target is Held. Keep it bagged for fights with nothing Holdable. It requires Light Armour proficiency, which medium-armour characters inherit. ⚠ Illegal on Asterion, whose Unarmoured Defence breaks on any helmet tagged as armour, so there is no contest for it.'
    - name: Hat of Fire Acuity
      for: Gale
      core: true
      note: '⚠⚠ THE build-defining item — carried by the Strange Ox at Dammon''s blacksmith. Kill it HERE (not in the Act 1 Grove, where it does not yet carry the hat). Dealing Fire damage grants 2 turns of Arcane Acuity: +1 spell attack AND +1 spell save DC per remaining turn, capped at 10, losing 1 per turn and 2 per hit taken. Each Scorching Ray ray deals Fire damage separately, so one level-4 cast (5 rays) takes Gale from 0 to the cap. Missed it? The Ox reappears in Rivington in Act 3.'
    - name: Evasive Shoes
      for: Gale
      core: true
      note: 'Sold by Mattis at Last Light — buy them here and carry them forward, because they become GALE''S ACT 3 BOOTS. +1 Armour Class and +1 Acrobatics. A modest pick forced by a hard constraint: Boots of Persistence and Vital Conduit Boots BOTH require Medium Armour proficiency, which Sorcerer 11 / Warlock 1 never grants, so the two obvious caster boots are illegal on him, and the Helldusk Boots go to Charles. Boots of Stormy Clamour keep the slot through Acts 1–2 while the Reverberation engine is the plan.'
    - name: Potent Robe
      for: Gale
      core: false
      note: 'Alfira hands it over at Last Light in ACT 2 — ONLY if she survived Act 1 (as the Dark Urge, Charles must knock her out before camp, not kill her). NOT WORN: its whole effect is adding CHA to CANTRIP damage, and this build stops casting cantrips in combat after character level 3, so wearing it would trade away Spidersilk Armour''s Constitution-save advantage — the only thing protecting Twinned Haste — for nothing. Sell it or keep it as a generic robe.'
    events:
    - name: Protect Isobel — DON'T let the inn fall
      note: Stop the assassin Marcus. If she dies the moonshield drops and the inn — vendors and quests — is lost. Missable.
    - name: Dammon (Karlach)
      note: Second-stage infernal-engine upgrade + hellish gear.
  - area: Moonrise Towers
    items:
    - name: Risky Ring
      for: Charles
      core: true
      note: Araj Oblodra. Advantage on all attacks, disadvantage on saves — Charles's crit enabler. Re-sold in Act 3 if missed.
    - name: Ne'er Misser
      for: Bonbon
      core: true
      note: Roah Moonglow. Force-damage hand crossbow; pair with Hellfire for the multi-hit Acuity setup from Act 2.
    - name: Spineshudder Amulet
      for: Gale
      core: true
      note: 'In a Mimic in Isobel''s bedroom (upper floor, Moonrise). CORE. It applies Reverberation on ranged SPELL-ATTACK hits only — not weapon hits, not save spells — which is exactly what Gale makes, 3–7 times per Scorching Ray. With Boots of Stormy Clamour it reliably stacks Reverberation to Prone: five stacks force a Constitution save that the condition''s own penalty makes effectively DC 15. Nothing in Act 3 replaces it.'
    - name: Spellcrux Amulet
      for: Bonbon
      core: true
      note: 'ACT 2 NECK, worn by the Warden in the Moonrise Towers Prison. Replenish an expended spell slot of ANY level as a BONUS ACTION, once per long rest. On a Bard 11 with a single level-6 slot that is literally a second six-target Command or a second Hold Monster, recovered mid-fight without spending her action. It replaces Broodmother''s Revenge, whose poison coating needs a per-turn heal she no longer has time for once the Acuity loop starts.'
    - name: Thunderskin Cloak
      for: Gale
      core: true
      note: 'HIS ACT 2 CLOAK, sold by Araj Oblodra at Moonrise. When a creature with Reverberation damages the wearer it must make a DC 13 Constitution save or be Dazed — no Reactions, disadvantage on Wisdom saves, and it loses its Dexterity bonus to AC. The synergy is structural rather than incidental: Gale is the party''s largest source of Reverberation (Spineshudder, Stormy Clamour and Belligerent Skies all stack it), so anything that reaches him is already Reverberating, and the Dazed WIS penalty then feeds his own Command. Cloak of the Weave replaces it in Act 3.'
    - name: Drakethroat Glaive
      wiki: Drakethroat Glaive
      for: Gale
      core: true
      note: 'Sold by Roah Moonglow. NOT a weapon for this party — a once-per-long-rest party buff. It grants Draconic Elemental Weapon (cast as a level 3 spell), which enchants a weapon for +1 Attack Rolls and +1d4 elemental damage UNTIL LONG REST, and it can target an ally''s main-hand weapon or a weapon on the ground. Gale is proficient with glaives (Human Civil Militia) and, per the wiki, "a Sorcerer of level 3 and higher can target TWO weapons using Metamagic: Twinned Spell" — so out of combat he equips the glaive, Twins the enchant onto two party weapons, and swaps back to his staves. Stacks with Magic Weapon; does not stack with other Elemental Weapon variants. ⚠ Charles''s Shadow Blade is re-summoned each rest, so enchant Phalar Aluve or Bonbon''s crossbows instead. ⚠ Patch 8 changed the effect from +1 enchantment (attack AND damage) to +1 attack rolls only; confirm in play whether it actually holds Concentration, since the tooltip and the condition disagree.'
    - name: Moonrise Towers vendor & prison loot
      wiki: false
      for: any
      core: false
      note: Talli and the traders sell heavy armour, martial weapons and scrolls; the prison and temple levels hide gear and story items. ⚠ Clear it before the assault — point of no return.
    events:
    - name: Araj Oblodra — permanent +2 STR
      note: Astarion bites her on request → Potion of Everlasting Vigour, a PERMANENT +2 Strength drinkable by any PC. Astarion disapproves.
  - area: Gauntlet of Shar
    items:
    - name: Killer's Sweetheart
      for: Charles
      core: true
      note: 'Self-Same Trial. After a kill, your next attack is a GUARANTEED crit; refreshes on long rest. Charles banks it for the largest Divine Smite, since a crit doubles every smite die. WARNING it applies to WEAPON attack rolls only, so it can never move to a caster. The old Oathbreaker caveat about Control Undead on the clone no longer applies - Charles keeps the Vengeance oath and never becomes an Oathbreaker.'
    - name: Callous Glow Ring
      for: Gale
      core: true
      note: 'Opulent chest in the vault room near Balthazar. +2 Radiant damage against ILLUMINATED creatures — the wiki names Scorching Ray among the multi-instance spells that apply it per instance, so up to +14 on a level-6 cast, and the radiant damage also procs Gloves of Belligerent Skies. ⚠ It stays with Gale rather than moving to Asterion or Bonbon because his ray count is the highest in the party and his own Coruscation Ring is what illuminates the target in the first place, so wear the pair together. ⚠ Take it off against Shar worshippers and Justiciars.'
    - name: Hellfire Hand Crossbow
      for: Bonbon
      core: true
      note: 'Yurgir. Pairs with Ne''er Misser for Bonbon''s Act 2 Acuity engine — both are Light, so no Dual Wielder feat is needed. ⚠ Breaking Yurgir''s contract via Raphael forfeits it.'
    - name: Boots of Brilliance
      for: Bonbon
      core: true
      note: Heavy chest in the room just north of Yurgir. Restores one Bardic Inspiration charge per long rest. Slashing Flourish consumes an Inspiration on every multi-target turn, and once the Acuity loop replaces raw repositioning she is Inspiration-starved rather than mobility-starved — so these take the slot from the Boots of Speed.
    - name: Dark Justiciar Half-Plate & Spear of Night
      wiki:
      - Dark Justiciar Half-Plate
      - Spear of Night
      for: any
      core: false
      note: Silent Library hidden chamber, tied to Shadowheart's arc.
    - name: Full Dark Justiciar set (Mask / Gauntlets / Helmet)
      wiki:
      - Dark Justiciar Mask
      - Dark Justiciar Gauntlets (Rare)
      - Dark Justiciar Helmet
      for: any
      core: false
      note: Pieces span Grymforge and the Gauntlet. The Helmet grants Covert Critical while Obscured — a second Darkness head. Asterion wants Mask of Soul Perception later.
    - name: Umbral Gems (progression) + trial loot
      wiki: false
      for: any
      core: false
      note: One gem per trial, needed to reach the Nightsong, plus incidental gear. No trial is optional loot.
    events:
    - name: The Three Trials + Umbral Gems
      wiki: false
      note: Soft-Step / Self-Same / Faith-Leap, one gem each; a 4th from Yurgir → opens the way to the Nightsong.
    - name: Nightsong / Dame Aylin choice
      note: Free Dame Aylin (camp ally, helps kill Ketheric) vs kill her for Shar. Pivotal, tied to Shadowheart.
    - name: Mirror of Loss here is CRACKED
      note: Non-functional. The working +2-ability Mirror is in ACT 3 (Cloister of Sombre Embrace).
  - area: Mind Flayer Colony
    items:
    - name: Resonance Stone
      for: Asterion
      core: true
      note: Near the Mind-Archive Interface (Necrotic Laboratory), late Act 2. Triggers Charles's respec — char 9 to Warlock 5 / Paladin 4, GWM → Dual Wielder, two-handed Phalar → 3d8 Shadow Blade main hand + Phalar off-hand, Savage Attacker. Asterion carries the 9m aura, doubling his psychic riders and Charles's Shadow Blade/Strange Conduit. Holster it vs psychic damage or dangerous mental saves.
    - name: Staff of Cherished Necromancy
      for: any
      core: false
      note: Balthazar drop — on the good path he dies in the Gauntlet, so it usually drops THERE. Niche with no necromancer in this party.
    events:
    - name: Apostle of Myrkul
      note: Ketheric's final form — freeing the Nightsong earlier gives crucial aid.
    - name: Astral-Touched Tadpole / the Emperor
      note: A permanent, one-time character change. This plan COMMUNES rather than eats, so all four transform — see the Tadpole tab.
  - area: Reithwin Town — Mason's Guild
    items:
    - name: Gloves of Battlemage's Power
      wiki: Gloves of Battlemage's Power
      for: Charles
      core: true
      note: 'REITHWIN TOLLHOUSE, not the Mason''s Guild - a locked opulent chest on the SECOND FLOOR, in the room with two locked doors. THE ITEM CHARLES''S WHOLE BUILD RUNS ON, and it is locked into his hands slot from here to the end of the run. Hitting a target with a spell or cantrip that uses a weapon grants ARCANE ACUITY: +1 spell attack roll and +1 SPELL SAVE DC per remaining turn, up to +10. Confirmed triggers are every Shadow Blade weapon attack, Booming Blade, any smite spell, and Divine Smite - and a smite spell chaining into a Divine Smite reaction triggers it TWICE. That DC is what makes HOLD PERSON land, and Hold Person is what makes every swing an automatic critical hit. It also gives him the party''s best save DC before Bonbon''s Helmet of Arcane Acuity arrives. WARNING Acuity duration drops by 2 every time he takes damage, so build stacks and cast Hold Person before the enemy turn. WARNING taking this forgoes Gloves of Baneful Striking, Helldusk Gloves and Craterflesh Gloves for the rest of the run.'
    - name: Helmet of Arcane Acuity
      for: Bonbon
      core: true
      note: ACT 2 — the Mason's Guild is in Reithwin, not the Act 3 Lower City. Locked, trapped Gilded Chest in the secret basement. Weapon hits stack Acuity (+spell attack and save DC) — the Bard's control engine.
    - name: Reithwin Town side-loot
      wiki: false
      for: any
      core: false
      note: Tower of the Sun/Waning Moon light puzzle, the apothecary, the Thorm mansion, Gerringothe's gold hoard, Mason's Guild vault scrolls. Sweep it while the moonlantern or pixie holds the curse off.
    events:
    - name: Thorm Mausoleum puzzle
      note: Press the family plaques in mural order → the way to the Gauntlet of Shar.
    - name: Oathbreaker Knight (Charles)
      note: 'NO LONGER RELEVANT - kept only so the old plan is not silently dropped. Charles keeps the Oath of Vengeance permanently and never breaks it, because Inquisitor''s Might is the only non-concentration per-hit Radiant source that feeds Luminous Armour. There is nothing to pay and nothing to restore before Withers will respec him at the Resonance Stone.'
  - area: House of Healing (Reithwin) — MISSABLE
    items:
    - name: Eversight Ring
      wiki: Eversight Ring
      for: Asterion
      core: true
      note: 'ACT 2 — locked opulent chest, morgue lab. Immunity to Blinded lets Asterion fight beside Charles inside Darkness. ⚠ MISSABLE: take it BEFORE defeating Ketheric or clearing the Colony, or the Shadow-Cursed Lands lock forever.'
    - name: House of Healing alchemy & surgeon loot
      wiki: false
      for: any
      core: false
      note: The morgue and operating theatre are full of alchemy ingredients, potions and gear; Malus Thorm drops scalpels and healing supplies.
    events:
    - name: Malus Thorm (the Surgeon)
      note: Optional fight — the nurses and Malus guard the morgue holding the Eversight Ring.
- act: 3
  areas:
  - area: Rivington
    items:
    - name: Hellrider's Longbow
      wiki: Hellrider Longbow
      for: Gale
      core: true
      note: 'RESOLVED — IT IS GALE''S. Charles takes the Vicious Shortbow instead, whose Dolor Amarus is worth about +28 a nova turn to an auto-crit build, so he no longer needs this and Gale keeps +3 Initiative on top of Elixir of Vigilance. The original arbitration is kept below in case the Bhaal path is not taken, in which case this comes back to Charles. FORMERLY CHARLES''S: Sold by Ferg Drogher in Rivington. Heightened Awareness gives +3 Initiative and advantage on Perception. Charles has the party''s worst initiative at d4+2 and his ranged slot is otherwise dead, because a Darkness cloud blocks ranged attacks into and out of itself - so this converts a wasted slot into the fix for his one structural weakness, and going first is what lets him stack Arcane Acuity and land Hold Person before the enemy acts. WARNING THE COST: this was Gale''s, and Gale acting earlier is what puts Twinned Haste up sooner - which is itself what gives Charles the extra action to build Acuity and Hold in the same turn. If Haste is landing too late in practice, give the bow back to Gale and cover Charles with the Fistbreaker Helm or a Sentinel Shield instead.'
    - name: Boots of Uninhibited Kushigo
      wiki: Boots of Uninhibited Kushigo
      for: Asterion
      core: true
      note: 'MISSABLE, and easy to walk past — carried by Prelate Lir''i''c in the ASTRAL PLANE as you enter Act 3, not in Rivington itself. Adds Asterion''s Wisdom modifier to every Unarmed Strike''s damage, so it is flat damage on all 4–6 hits per turn. With the Mirror of Loss taking him to WIS 18 that is +4 a hit. Grab it during the Astral Prism sequence before the act moves on.'
    - name: Strange Ox (second chance)
      wiki: false
      for: Gale
      core: false
      note: 'If the Hat of Fire Acuity was missed at Last Light in Act 2, the Strange Ox reappears here on a hill west of the requisitioned barn. This is the last chance at the item Gale''s build depends on.'
    - name: Nyrulna
      for: any
      core: false
      note: Circus of the Last Days reward. Legendary returning trident with a Thunder AoE burst — best-in-slot for throwing builds.
    - name: Band of the Mystic Scoundrel
      for: Bonbon
      core: true
      note: AKABI's Circus wheel — the jackpot teleports you ALONE to a Chult jungle where it sits in a backpack (Nyrulna too). Enchantment/Illusion as a BONUS action after a weapon hit. ⚠ NOT at Sorcerous Sundries, and ~16 spins closes the wheel.
    - name: Spellmight Gloves
      for: Gale
      core: true
      note: 'Lucretious''s reward for Find Dribbles the Clown at the Circus (also pickpocketable). CORE. −5 to spell attack rolls for +1d8 damage, which is excellent precisely because Scorching Ray is an attack roll firing 3–7 times. MANAGE THEM: first cast of a fight with the gloves OFF to build Arcane Acuity, then switch them ON once Acuity covers the −5. ⚠ VERIFY ON THE FIRST CAST whether the +1d8 applies per ray or once per spell — on a 7-ray cast the two readings are +7d8 (best in slot) versus +1d8 for a −5 penalty on all seven rolls (actively harmful).'
    - name: Rivington vendors & Requisitioned Barn
      wiki: false
      for: any
      core: false
      note: Ferg Drogher, the Circus traders and the Open Hand temple — early Act 3 gear, arrows and scrolls; the barn has a hidden cellar.
    events:
    - name: Circus of the Last Days
      note: Side content and vendors, a few unique items and story hooks.
  - area: Wyrm's Rock Fortress / Wyrm's Crossing
    items:
    - name: Helldusk Boots
      for: Charles
      core: true
      note: 'ACT 3 BOOTS, in a locked Gilded Chest on the TOP FLOOR of Wyrm''s Rock Fortress — not in the House of Hope with the rest of the set. Steadfast stops all forced movement and difficult terrain, replacing what the Boots of Striding were doing, and Infernal Evasion lets him spend his REACTION TO TURN A FAILED SAVING THROW INTO A SUCCESS. That is the direct answer to the Risky Ring on a concentration holder: one guaranteed save per turn, on the save that matters. ⚠ Gale would love them too, but Charles is the one carrying save disadvantage and Gale has Armour of Landfall.'
    - name: Cloak of Displacement
      for: Asterion
      core: true
      note: 'Sold by Entharl Danthelon at Danthelon''s Dancing Axe, Wyrm''s Crossing. At the start of his turn, enemies take DISADVANTAGE on attack rolls against him until he takes damage. He is the only party member with neither armour nor damage reduction, so it is worth more here than on Charles behind AC 21 and −3 damage. Useful wiki quirk: Displaced is not stripped by anything the game does not count as a hit, including a successful save against a damage-dealing spell.'
    events:
    - name: Wyrm's Rock is a one-way gate
      note: The fortress is the route from Rivington into the Lower City. Sweep the top floor and the Gilded Chest on the way through.
  - area: Sorcerous Sundries / Ramazith's Tower
    items:
    - name: Markoheshkir
      for: Gale
      core: true
      note: 'Ramazith''s Tower, inside a Globe of Invulnerability (See Invisibility to spot the lever, then DC 20 Arcana to disable the globe). +1 spell attack and DC, plus Arcane Battery for one free spell of any level. Attune Kereska''s Favour to FLAME OF WRATH: Fire resistance, +proficiency bonus to Fire spell damage applied per ray, and Heat generation. ⚠ Heat deals unavoidable self-damage each turn and threatens Twinned Haste — do not attune Flame of Wrath until Armour of Landfall is equipped.'
    - name: Armour of Landfall
      for: Gale
      core: true
      note: 'Sold by Lorroakan''s Projection or Rolan on the SUNDRIES GROUND FLOOR (1700g). AC 13 + DEX light armour, +1 Spell Save DC, and — the real reason — ADVANTAGE ON CONSTITUTION SAVING THROWS. That advantage replaces the Halfling Luck and the War Caster feat this build cannot have, and it is what makes Markoheshkir''s Heat safe to carry while concentrating on Twinned Haste. Gale''s Human Civil Militia already grants light-armour proficiency, so the Warlock dip is not needed to wear it.'
    - name: Vest of Soul Rejuvenation
      for: Asterion
      core: true
      note: 'ACT 3 CHEST, and the piece that finally beats Graceful Cloth. Sold by Rolan at Sorcerous Sundries, or by Lorroakan''s Projection if Rolan is dead. +2 Armour Class on an unarmoured build, 1d4 healing on a successful save against a spell, and Greater Kushigo Counter — a REACTION unarmed strike against any attacker that misses, carrying every one of his riders. It also completes the Soul set beside Gloves of Soul Catching and the Mask of Soul Perception. ⚠ Losing the Cloth costs advantage on Sleight of Hand; keep it bagged and swap back for theft.'
    - name: Stolen scrolls (Chain Lightning, Freezing Sphere, Cone of Cold)
      wiki:
      - Scroll of Chain Lightning
      - Scroll of Otiluke's Freezing Sphere
      - Scroll of Cone of Cold
      for: Bonbon / Gale
      core: false
      note: Buy or steal as situational ammunition for the real casters. Asterion has no Magical Ambush.
    - name: Quickspell Gloves
      for: any
      core: false
      note: Rolan. Cantrip as a BONUS action, 1/short rest.
    - name: Robe of the Weave
      for: any
      core: false
      note: Ramazith's Tower, inside a Globe of Invulnerability (needs See Invisibility + Arcana DC20). +2 AC, +1 Spell Save DC and Attack, heal 1d6 on a successful save vs a spell.
    events:
    - name: Lorroakan vs Nightsong choice
      note: Protect Dame Aylin or side with Lorroakan. Does NOT award Gontr Mael — that drops from the Steel Watcher Titan.
  - area: Cloister of Sombre Embrace (House of Grief)
    items: []
    events:
    - name: Mirror of Loss — permanent +2 ability (the REAL one)
      note: The working Mirror. Religion DC20 / Arcana DC25 (or read the note), then pray to Shar (DC25) for a permanent +2, cap 24. The whole plan assumes it — every PC should visit.
  - area: Stormshore Tabernacle
    items:
    - name: Amulet of the Devout
      for: nobody — sell it
      core: false
      note: 'Main offering chest in the basement. +2 spell save DC and an extra Channel Divinity charge. NOBODY IN THIS PARTY WEARS IT: the wiki says it "only works with Channel Divinity, and is thus less helpful to Paladins" — BG3 renamed the Paladin resource to Channel OATH, so Charles gets nothing from the recharge, and there is no Cleric anywhere in the party. Gale''s neck belongs to Spineshudder, Bonbon''s to Spellcrux and Charles''s to the Amulet of Greater Health. ⚠️ Looting it from the offering chest inflicts the Castigated By Divinity curse on the looter UNLESS Jaheira takes it while wearing Khalid''s Gift. Sell it, or leave it in the chest.'
    - name: Armour of Agility
      for: Bonbon
      core: true
      note: 'ACT 3 CHEST, sold by Gloomy Fentonson at the Stormshore Armoury beside the Tabernacle. Medium armour that adds her FULL Dexterity modifier — AC 17 + 4 = 21 at DEX 18 — plus +2 to ALL saving throws and no Stealth penalty. It beats the Adamantine Splint by 3 AC and 2 saves; the trade is losing crit immunity, so keep the Splint bagged for any fight where she is being focused and Arcane Acuity keeps getting stripped. ⚠ Do not take Medium Armour Master or Magic Initiate: Cleric on her — the wiki notes either feat breaks the full-Dexterity passive.'
    events:
    - name: The curse trap
      note: Don't brick the amulet — Jaheira + Khalid's Gift loots the chest cleanly.
  - area: Temple of Bhaal / Murder Tribunal
    items:
    - name: Sarevok's Horned Helmet
      for: Charles
      core: true
      note: Sarevok, Murder Tribunal. Lower crit threshold + on-kill bonuses — crit-fish core.
    - name: Bloodthirst
      for: optional weapon attacker
      core: false
      note: Orin. Legendary +2 dagger with crit and hand-specific passives, but Charles keeps Phalar Aluve to sustain Shriek.
    - name: Crimson Mischief
      for: any
      core: false
      note: Also Orin. Hand-specific dual-wield bonuses, but Charles keeps Phalar beside Shadow Blade for Shriek.
    - name: Ring of Murderous Opportunity + Sword of Chaos
      wiki:
      - Ring of Murderous Opportunity
      - Sword of Chaos
      for: any
      core: false
      note: Ring (Orin) — bonus damage and extra reaction attacks, strong for an assassin. Sword of Chaos (Sarevok) — +2 wounding longsword.
    - name: Vicious Shortbow
      for: Charles
      core: true
      note: 'GATED — BHAAL PATH ONLY, sold by the Echo of Abazigal, and he never fires it. Dolor Amarus is listed on THE HOLDER rather than the main hand, and the wiki states it applies to ALL weapon attacks while a weapon carrying the feature is equipped: +7 flat on every critical hit. Every swing against a Held target crits, so that is about +28 on the standard nova and +70 on the Terazul turn, out of a ranged slot that was dead anyway because a Darkness cloud blocks ranged attacks both ways. Ranged and melee weapon sets are separate, so it costs nothing off Shadow Blade or Phalar. ⚠ Taking this hands the Hellrider Longbow back to Gale. ⚠ No Bhaal path means no bow — fall back to the Hellrider Longbow in Rivington.'
    - name: Echo of Abazigal stock (GATED — Bhaal path only)
      wiki:
      - Craterflesh Gloves
      - Bhaalist Armour
      - Assassin of Bhaal Cowl
      for: Charles
      core: false
      note: 'GATED BONUS, not a plan dependency — these unlock only if Charles completes Impress the Murder Tribunal and becomes an Unholy Assassin of Bhaal (the VICIOUS SHORTBOW above is the same vendor behind the same gate, and is the one item here the plan now actually commits to), and they arrive late enough in Act 3 that the Shadow Blade + Resonance Stone package carries the build either way. Documented so the cost of resisting the Urge is visible. CRATERFLESH GLOVES are the real prize: +1d6 Force on a critical hit, which the wiki notes actually lands as 2d6 because the crit doubles it — on a Held target where all seven swings auto-crit that is roughly +49 a turn, against about +17 from Helldusk Gloves. BHAALIST ARMOUR gives +2 Initiative and Aura of Murder (enemies within 3m become Vulnerable to Piercing, radius raised from 2m in Patch 8) — worth nothing to Charles''s Psychic Shadow Blade, but it doubles Bonbon''s Piercing crossbow and Titanstring damage against anything engaging him; costs Luminous Armour''s Radiating Shockwaves. ASSASSIN OF BHAAL COWL is +2 Initiative, which matters more than it looks because BG3 rolls initiative on a d4.'
    events:
    - name: Murder questline (Dark Urge)
      note: Charles IS the Dark Urge — this arc and its embrace-or-resist choice are his story climax.
  - area: House of Hope (Raphael)
    items:
    - name: Amulet of Greater Health
      for: Charles
      core: true
      note: 'Leftmost pedestal in the Archive. Sets Constitution to 23 and grants ADVANTAGE ON CONSTITUTION SAVING THROWS. Both halves land on Charles and nowhere else: +6 to concentration checks, and the advantage cancels the Risky Ring''s permanent disadvantage outright, returning those rolls to a straight d20. ⚠ It is redundant on the other two — Bonbon has War Caster and Gale has Armour of Landfall, so only Charles has a disadvantage for it to cancel. Steal tip: it can be taken without the fight on a DC 20 Sleight of Hand if the Orphic Hammer, the Soul-Sworn Contract and Hope are left alone — an Asterion job.'
    - name: Gloves of Soul Catching
      wiki: Gloves of Soul Catching
      for: Asterion
      core: true
      note: 'BEST-IN-SLOT MONK GLOVES — Hope hands these over when freed. +1d10 Force on EVERY unarmed strike, which at 4–6 hits a turn is one of the largest single damage sources in the party, plus Constitution +2 (to 20). Soul Catching also gives, once per turn on an unarmed hit, a free choice of 10 HP of healing OR +5 to one attack roll or saving throw. Replaces Bracers of Defence. ⚠ Per the wiki the tooltip is wrong in several ways: it is a granted free action rather than automatic healing, and it is a flat +5 rather than Advantage. It is also stripped if he takes damage with no temporary HP.'
    - name: Helldusk Gloves
      for: Charles
      core: true
      note: Fire damage on weapon hits plus better spell attacks and DC — applied on each of Charles's many Shadow Blade hits. ⚠ If the Bhaal path is taken, Craterflesh Gloves beat these substantially on a crit-fishing nova (roughly +49 a turn against +17).
    - name: Helldusk Armour
      for: Charles
      core: true
      note: 'ACT 3 CHEST, carried by Raphael. AC 21 flat, Fire resistance, cannot be Burned, ALL INCOMING DAMAGE REDUCED BY 3, Infernal Retribution, a 1/long-rest Fly and no Stealth penalty. ⚠ It is HEAVY armour and multiclassing never grants heavy proficiency — but the wiki is explicit that it carries its own passive: "You are considered Proficient with this armour while wearing it." That single line is what lets a medium-armour Paladin/Warlock wear the best chest piece in the game. Flat AC 21 needs no DEX and beats the Adamantine Scale Mail by 3 AC and 2 damage reduction; the Armour of Agility is the save-focused alternative if +2 saves beat flat AC, but it goes to Bonbon.'
    - name: Orphic Hammer + Infernal Rapier
      wiki:
      - Orphic Hammer
      - Infernal Rapier
      for: any
      core: false
      note: The Hammer frees Orpheus (story); the Rapier is a strong CHA-scaling weapon.
    - name: House of Hope vault (Korrilla / Hope's reward)
      wiki: false
      for: any
      core: false
      note: The boudoir and archive hold a big gold and gem hoard, Elixirs of Universal Resistance and scrolls; Hope hands over gear if freed. Loot during the fight.
    events:
    - name: Raphael fight
      note: Beat Raphael (or loot during the Hope rescue) for the House of Hope gear.
  - area: Cazador's Palace
    items:
    - name: Rhapsody
      for: Gale
      core: true
      note: 'Carried by Cazador Szarr. CORE off-hand: Scarlet Remittance stacks +1 attack roll, +1 damage, AND +1 spell save DC per kill (max 3), and this build is the rare one that uses all three — the damage applying per Scorching Ray ray. Gale wields it off-hand behind Markoheshkir, which requires Dual Wielder. ⚠ Per the wiki, since Patch 5 it only builds stacks on killing living hostile targets. Asterion''s unarmed Monk still cannot use it.'
    - name: Cazador's palace loot (ritual chamber & kennels)
      wiki: false
      for: any
      core: false
      note: Gold hoard, potions of Vampirism, the Ritual Dagger, trapped ritual-chamber gear. Sweep it during Astarion's questline — it does not reopen.
    events:
    - name: Astarion's Ascension choice
      note: 'MAJOR — ascend Astarion (power boost, darker) vs stay a Spawn (Vampire weaknesses, the ''good'' arc). Affects Asterion directly.'
  - area: Steel Watch Foundry
    items:
    - name: Gontr Mael
      for: Bonbon
      core: false
      note: 'Steel Watcher Titan, Control Centre. Legendary +3 longbow with Celestial Haste once per long rest. ⚠ AN OPENING-ROUND SWAP, NEVER THE DEFAULT: it is Two-Handed, so equipping it cancels the dual-hand-crossbow set that is her whole Arcane Acuity engine — three or four Acuity-stacking hits a turn traded for two. Fire the Haste, then swap back to Ne''er Misser and the Hellfire. ⚠ It does not drop if the Titan is killed by the Atrophied condition.'
    events:
    - name: Disable the Steel Watch
      note: Destroy the Foundry to weaken the endgame assault; loot the Titan first.
  - area: Lower City (Zhentarim / vendors)
    items:
    - name: Ne'er Misser
      for: Bonbon
      core: false
      note: Roah Moonglow — Moonrise in Act 2, here if missed. Pairs with Hellfire; its force damage bypasses many resistances.
    - name: Birthright
      for: nobody — bagged as a dialogue swap
      core: false
      note: 'Sold at Sorcerous Sundries by Rolan / Lorroakan''s projection (ground floor). +2 Charisma helm (cap 22). NOBODY WEARS IT IN COMBAT: both Charisma characters have their heads locked to Acuity hats — Gale to the Hat of Fire Acuity, Bonbon to the Helmet of Arcane Acuity — and +2 Charisma is +1 spell save DC against Acuity''s +10. Keep it bagged and swap it on out of combat for Persuasion, Deception and Intimidation checks on whichever of them is the face; the wiki notes it stacks with the Mirror of Loss for Charisma 24.'
    - name: Cloak of the Weave
      for: Gale
      core: true
      note: 'Sold by Helsik at the Devil''s Fee, but ONLY once her special stock is unlocked through dialogue. +1 Spell Save DC and +1 spell attack rolls — Gale''s best-in-slot cloak, and the spell attack applies per ray. ⚠ Per the wiki its Absorb Elements ability is bugged and non-functional; buy it for the flat +1/+1.'
    - name: Ring of Free Action
      for: Asterion
      core: true
      note: Araj Oblodra at Crimson Draughts in the Lower City, or from her at Moonrise back in Act 2. Ignore difficult terrain and CANNOT BE PARALYSED OR RESTRAINED. His Night Walkers already cover Web, Entangle and Grease but not those two, and Paralysed is what turns a dived monk into a pile of free critical hits. It takes the ring slot the Eversight Ring held, which goes back in the bag for fights inside Charles's Darkness.
    - name: Boots of Persistence
      for: Bonbon
      core: true
      note: Sold by Dammon at the Forge of the Nine in the Lower City. Permanent Freedom of Movement and Longstrider — Freedom of Movement makes a Ring of Free Action unnecessary for her and keeps the second ring slot on the Caustic Band. Medium armour proficiency is required and Fighter 1 supplies it. ⚠ Gale cannot wear these at all (Sorcerer/Warlock never grants medium armour) and the Helldusk Boots go to Charles, so this is the allocation that leaves nobody stranded.
    - name: Wavemother's Cloak
      for: Bonbon
      core: true
      note: 'ACT 3 CLOAK, in an opulent chest behind Allandra Grey''s desk on the upper floor of the Water Queen''s House. Once per turn in combat it grants Water Layer Protection until she takes damage: +2 AC, +2 to saving throws, Fire resistance and immunity to Burning. On a backline controller who is rarely hit, that refreshes every turn and effectively never falls off — worth more to her than a flat +1/+1, and it leaves the Cloak of Displacement free for Asterion, who has no armour at all.'
    - name: Helm of Balduran + Wyrmway loot (Ansur)
      wiki:
      - Helm of Balduran
      for: any
      core: false
      note: Wyrmway, from the Counting House basement → the Ansur fight. Regen + crit immunity, one of the best defensive helms in the game; the trials en route also give gear.
    - name: Facemaker's Boutique + Devil's Fee
      wiki: false
      for: any
      core: false
      note: Figaro sells headwear and cast-a-spell hats; Helsik sells rare rings, scrolls and Netherese/ritual gear. Prime stealing targets.
    events:
    - name: Iron Throne (time-sensitive)
      note: Rescue Duke Ravengard and the gnomes before it floods — a real timer.
---
