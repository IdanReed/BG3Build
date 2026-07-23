---
nickname: Asterion
builds:
- name: The Ambusher — Melee Shadow-Blade (Config A)
  is_primary: true
  role: Melee stealth assassin / DEX-save nuker / scout
  class: Arcane Trickster Rogue 11 / War Domain Cleric 1
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: Fey Ancestry (no Charm/Sleep), Perception proficiency, extra cantrip, bonus-action Bite. No Superior Darkvision or innate stealth-advantage, so Hide leans on Reliable Talent + Expertise (still floor-10 reliable); Shadow Blade's dim-light advantage still works at melee range.
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background (can't be changed, even via respec)
  starting_stats:
    STR: 8
    DEX: 17
    CON: 14
    INT: 12
    WIS: 15
    CHA: 8
  stats_note: High Elf floating +2 DEX / +1 WIS already applied.
  ability_targets: 'DEX 17 → 18 (Hag''s Hair) → 20 (Graceful Cloth''s +2, worn all game) — so the Mirror of Loss is NOT needed on DEX. Redirect the Mirror to WIS: WIS 15 → 17 (R8 feat) → 19 (Mirror of Loss) for better scroll/Command DC + mental saves.'
  feats:
  - at: R4
    feat: Savage Attacker
    note: Melee-only; rerolls Shadow Blade + Sneak dice.
  - at: R8
    feat: +2 WIS
    note: → 17 (scroll/Cleric DC + WIS saves).
  - at: R10
    feat: Alert
    note: +5 initiative + immune to Surprise — guaranteed-first-turn ambush. Chosen over Dual Wielder, whose off-hand attack can't carry Sneak Attack and is dead when the bonus action is always Hide.
  casting: 'AT spells = INT (utility: Shield, Disguise Self, Shadow Blade). Stolen scrolls + Cleric spells = WIS (Cleric taken after Rogue 1 → scrolls key off WIS).'
  key_spells:
  - 'AT: Shield, Disguise Self, Shadow Blade'
  - 'Cleric (WIS): Create Water, Command, Guidance'
  - Offense = stolen scrolls (see spells → recommended; note the real DEX-save cold is Ice Storm, not Cone of Cold)
  creation:
    level1_class: Rogue 1
    level1_gains: Expertise in 2 skills (Sleight of Hand + Stealth) + Sneak Attack (1d6). MUST be the character-creation class so Expertise covers the right skills and the stolen-scroll DC keys off the later WIS dip.
    subclass_choice: Arcane Trickster is chosen at Rogue 3 (character level 4), not at creation.
    proficiencies:
      armor_weapons: 'Rogue base: Light armour; Simple weapons, Hand Crossbows, Longswords, Rapiers, Shortswords. The War Cleric dip (char 2) adds Medium + Heavy armour, Shields, and Martial weapons (Heavy only because it''s a subclass grant).'
      saving_throws: Dexterity + Intelligence (Rogue, the creation class). The Cleric dip grants NO save proficiencies (multiclassing never does).
      skills: 'Rogue picks 4 skills and Expertise in 2 (Sleight of Hand + Stealth) at level 1; Astarion''s Charlatan background grants Sleight of Hand + Deception (so Stealth comes from a Rogue skill pick, not the background). Expertise #2 (Perception + Investigation) comes at Rogue 6.'
    starting_cantrips: None from the class at Rogue 1 (AT casting starts at Rogue 3). Astarion (High Elf) picks 1 racial wizard cantrip at creation — take Booming Blade.
    starting_spells: None at Rogue 1 — the first AT spells (3) are learned at Rogue 3 (char 4).
    notes: Astarion (High Elf / Vampire Spawn). 3 feats total (Rogue 4/8/10 — Rogue uniquely gets a bonus feat at level 10). Rogue-first ordering makes stolen-scroll DCs key off WIS via the War Cleric dip.
  spells:
    note: 'AT class spells key off INT; the stolen scrolls and Cleric spells key off WIS (Rogue-first ordering). Mandatory = the loop depends on it; Recommended = flex + the stolen-scroll arsenal. CORRECTION: the plan''s ''DEX-save cold'' scrolls are mostly CON saves — Ice Storm is the real DEX-save cold option.'
    mandatory:
    - spell: Mage Hand
      level: Cantrip (free)
      school: Conjuration
      save: None
      when: char 4 (Rogue 3, Mage Hand Legerdemain)
      why: 'Invisible + permanent hand: scouts, flanks to enable Sneak Attack in the open, and throws water bottles (no action) to set up Wet. Core to both configs.'
    - spell: Booming Blade
      level: Cantrip
      school: Evocation
      save: Melee weapon attack (DEX)
      when: char 1 (High Elf racial) / char 4 (Rogue 3)
      why: Once-per-turn Sneak-Attack delivery in melee; weapon damage + thunder-on-move, scales at char 5 & 11. Central to Config A.
    - spell: Shield
      level: '1'
      school: Abjuration
      save: None (reaction)
      when: char 4 (Rogue 3, any-school pick)
      why: +5 AC and Magic Missile immunity — the frail assassin's main survival button. Abjuration, so it needs the any-school pick or a Replacement.
    - spell: Shadow Blade
      level: '2'
      school: Illusion
      save: None (bonus action to summon)
      when: char 8 (Rogue 7, via replacement)
      why: 2d8 (3d8 upcast) psychic shortsword, advantage vs dim-light/dark targets, lasts until long rest, no concentration. Config A's main weapon — psychic doubled by the Resonance Stone, auto-crit vs Held.
    - spell: Guidance
      level: Cantrip
      school: Divination
      save: None
      when: char 2 (War Cleric dip)
      why: +1d4 to interactive ability checks — dialogue, lockpicking/disarming, and the confront-check if a theft goes wrong. ⚠ Does NOT apply to the background pickpocket Steal roll (variable dice don't attach). Still a fine utility cantrip; just not a stealing booster.
    - spell: Create Water
      level: '1'
      school: Transmutation
      save: None
      when: char 2 (War Cleric dip)
      why: Applies Wet (double Lightning/Cold) to set up Gale's lightning and your own cold scrolls. Config A only.
    - spell: Command
      level: '1'
      school: Enchantment
      save: WIS save
      when: char 2 (War Cleric dip)
      why: Single-target hard control (Halt / Drop / Flee), keys off WIS; can be forced to disadvantage via Magical Ambush. Config A only.
    recommended:
    - spell: Disguise Self
      level: '1'
      school: Illusion
      save: None
      when: char 4 (Rogue 3)
      why: Infiltration / skip-fights and a fresh identity after a botched steal (both configs).
    - spell: Fog Cloud
      level: '1'
      school: Conjuration
      save: None
      when: char 4+ (any-school pick / replacement)
      why: Self-made obscurement to Hide (arms Magical Ambush) and to feed the Eversight-Ring darkness combo.
    - spell: Misty Step
      level: '2'
      school: Conjuration
      save: None
      when: char 8+ (Rogue 7, replacement)
      why: Reposition/escape without relying solely on the Night Walkers / Amulet of Misty Step item copies.
    - spell: Healing Word
      level: '1'
      school: Evocation
      save: None
      when: char 2 (War Cleric dip)
      why: Bonus-action ranged revive/heal for a party with no dedicated healer; clutch when out of Hide range.
    - spell: Ice Storm (scroll)
      level: '4'
      school: Evocation
      save: DEX save
      when: stolen scroll (DC uses WIS)
      why: The ACTUAL DEX-save cold option the plan wants (Cold + Bludgeoning) — works fully with Magical Ambush; use this rather than the CON-save cold nukes below when DEX-save is the goal.
    - spell: Chain Lightning (scroll)
      level: '6'
      school: Evocation
      save: DEX save
      when: stolen scroll
      why: True DEX-save AoE; works fully with Magical Ambush (direct-damage save spell).
    - spell: Cone of Cold (scroll)
      level: '5'
      school: Evocation
      save: CON save (NOT DEX)
      when: stolen scroll
      why: Big cold nuke, but a Constitution save — contradicts the plan's 'DEX-save cold' label. Magical Ambush still disadvantages the save; Evasion is irrelevant to it.
    - spell: Otiluke's Freezing Sphere (scroll)
      level: '6'
      school: Evocation
      save: CON save (NOT DEX)
      when: stolen scroll
      why: Large cold burst, but also a CON save (not DEX) — same correction as Cone of Cold.
  leveling:
  - char_level: 2
    class: War Cleric 1
    gains: WIS casting; medium/heavy armour + shields + martial; War Priest; Create Water, Command, Guidance
  - char_level: 3
    class: Rogue 2
    gains: Cunning Action (bonus-action Hide — arms Magical Ambush + Sneak Attack)
  - char_level: 4
    class: Rogue 3
    gains: 'Arcane Trickster: invisible Mage Hand; Booming Blade; Shield, Disguise Self'
  - char_level: 5
    class: Rogue 4
    gains: 'Feat: Savage Attacker'
  - char_level: 6
    class: Rogue 5
    gains: Uncanny Dodge
  - char_level: 7
    class: Rogue 6
    gains: 'Expertise #2 (Perception + Investigation)'
  - char_level: 8
    class: Rogue 7
    gains: Evasion + 2nd-level slots → Shadow Blade; Sneak Attack 4d6
  - char_level: 9
    class: Rogue 8
    gains: 'Feat: +2 WIS (→17)'
  - char_level: 10
    class: Rogue 9
    gains: Magical Ambush (Hide → targets have disadvantage vs your spells/scrolls)
  - char_level: 11
    class: Rogue 10
    gains: 'Feat: Dual Wielder (or Alert) + 3rd cantrip'
  - char_level: 12
    class: Rogue 11
    gains: Reliable Talent (never roll <10 on proficient checks); Sneak Attack 6d6
  itemization:
    act1:
    - id: graceful-cloth
      item: Graceful Cloth
      note: Graceful Cloth (advantage on stealing — wear all game)
    - id: gloves-of-thievery
      item: Gloves of Thievery
      note: Gloves of Thievery
    - id: knife-of-the-undermountain-king
      item: Knife of the Undermountain King
      note: Knife of the Undermountain King (main-hand until Shadow Blade, crit 19–20)
    - id: night-walkers-boots-amulet-of-misty-step
      item: Night Walkers boots + Amulet of Misty Step
      note: Night Walkers boots + Amulet of Misty Step (2 free warps/short rest)
    - id: hoard-superior-elixir-of-arcane-cultivation-battlemage-elixirs
      item: Hoard Superior Elixir of Arcane Cultivation + Battlemage Elixirs
      note: Hoard Superior Elixir of Arcane Cultivation + Battlemage Elixirs
    act2:
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      note: Deathstalker Mantle (Invisible on kill — reposition + re-ambush)
    - id: bracers-of-defence
      item: Bracers of Defence
      note: Bracers of Defence (+2 AC, no armour)
    - id: eversight-ring
      item: Eversight Ring
      note: Eversight Ring (House of Healing, Reithwin — grab it THIS act; it's missable) — see through your own Darkness, the 'Asterion' combo
    - id: retire-the-old-tank-gear-you-re-squishy-now
      item: Retire the old tank gear — you're squishy now
      note: Retire the old tank gear — you're squishy now
    act3:
    - id: self-cast-shadow-blade
      item: Self-cast Shadow Blade
      note: 'Self-cast Shadow Blade (3d8) main-hand + Light off-hand: Rhapsody OR Bloodthirst (Orin — Improved Critical, crit −1 on all attacks; the better crit off-hand)'
    - id: eversight-ring
      item: Eversight Ring
      note: Eversight Ring (carried over from Act 2 — the Darkness 'Asterion' combo)
    - id: carries-the-resonance-stone
      item: Carries the Resonance Stone
      note: Carries the Resonance Stone (doubles your + the Paladin's psychic — but Astarion eats its mental-save debuff, so cluster near the Paladin's Aura of Protection)
    - id: neck-slot-free
      item: Neck slot free
      note: Neck slot free (Amulet of Greater Health went to the Bard to guard Hold Monster) — use a defensive amulet (e.g. Amulet of the Harpers / a save-boosting neck); your survival is Uncanny Dodge + Evasion + Shield, not CON
    - id: ne-er-misser-hellfire-hand-crossbow
      item: Ne'er Misser + Hellfire Hand Crossbow
      note: Ne'er Misser + Hellfire Hand Crossbow (ranged backup)
  playstyle: |-
    - **Pre-cast Shadow Blade** at long rest (Superior Elixir of Arcane Cultivation → L3 slot → 3d8, lasts all day, no concentration).
    - **Each turn:** bonus-action Hide (arms Magical Ambush AND the advantage for Sneak Attack) → Booming Blade + Shadow Blade + Sneak Attack as one huge psychic strike; the Sneak Attack adopts the blade's psychic type, so the Resonance Stone doubles the whole strike and a Held target auto-crits it.
    - Between strikes, crouch and cast a stolen DEX-save scroll (cold-first) at disadvantage via Magical Ambush.
    - The invisible Mage Hand throws water for the Sorcerer or parks by a target to guarantee Sneak Attack.
    - Vanish with Cunning Action Disengage → fog + Eversight, or Misty Step.
    - **CO-EQUAL with Config B** (no single 'primary'): run Config A for Act-2 psychic-nova set-pieces vs LIVING bosses (Resonance Stone ×2 + Hold auto-crit); it's fragile and Stone-dependent, so switch to Config B for undead/immune bosses and safer backline turns.
  traps:
  - 'Magical Ambush needs the Hide ACTION (not mere invisibility); only helps DEX-save direct-damage scrolls fully (control spells: initial save only; surface spells: none).'
  - The 3d8 upcast needs the SUPERIOR Elixir of Arcane Cultivation (base/Greater give only L1/L2 slots).
  - The Eversight 'Asterion' combo is an Act 3 item and collapses vs enemies with Devil's Sight.
  - Only 3 feats on an 11/1 split.
  pickpocket:
    note: 'Asterion is the party''s thief — this is how he lifts key gear, scrolls, and buff sources with near-certainty, and gets away clean on the rare miss. ⚠ CORRECTION: pickpocketing resolves as a BACKGROUND d20 roll, so variable dice like Guidance and Bardic Inspiration do NOT apply to it — only FLAT Sleight-of-Hand bonuses (gear) change the number. The guaranteed ceiling is therefore fixed by Reliable Talent + flat gear, not buffs. Applies to both configs (the War Cleric dip''s Guidance is for dialogue/other checks, not the steal).'
    check_formula: 'Pickpocketing rolls Sleight of Hand: d20 + DEX mod + proficiency, with Expertise DOUBLING proficiency. At char 12 with DEX 20 (+5) and Expertise (+8) that''s a +13 flat. Reliable Talent (Rogue 11) floors the raw d20 at 10 on proficient skills, so his minimum result is 10 + 13 = 23 and a natural 1 can''t auto-fail. Proficiency does NOT stack from multiple sources; only Expertise raises it.'
    success_math: The number the UI shows is a 'roll target' = the raw d20 you need (flat bonuses already subtracted), NOT the DC. Reliable Talent floors the die at 10, so ANY item with roll target ≤ 10 (underlying DC ≤ 23) is a GUARANTEED steal with zero setup. To beat a HIGHER target you must add FLAT Sleight-of-Hand gear (Smuggler's Ring +2 → target ≤ 12; + Gloves of Power +1 → ≤ 13) — Guidance and Bardic Inspiration do NOT apply to the background pickpocket roll. Advantage (Graceful Cloth) doesn't raise the guaranteed floor but makes mid/high targets very likely. Virtually every merchant item sits at DC ≤ 23, so Asterion auto-succeeds on nearly all of them; for the rare over-floor item use flat gear, or Enthrall the vendor and steal freely.
    detection: 'Pickpocketing requires being HIDDEN; opening/closing the steal window is free while unseen (only clicking Steal rolls). A failed steal and ''caught possessing stolen goods'' are SEPARATE crimes. On a fail the victim attacks or offers a Deception/Intimidation/Persuasion check (pass = they watch you; a 2nd catch = arrest). Even a SUCCESS starts a delayed investigation: the victim searches for a few turns — if you stay out of sight/range until it expires, the whole party is permanently safe (you can then wear the stolen item openly). An accused character carrying no session-stolen loot always proves innocence.'
    modifiers:
    - source: DEX 20 (+5)
      effect: +5 flat, baked into the displayed roll target
      stacks: Flat, capped at the DEX 20 ceiling
      how: Self — DEX 17 → 18 (Hag's Hair) → 20 (Mirror of Loss); Graceful Cloth's +2 helps reach 20 but doesn't exceed it
    - source: Proficiency + Expertise (+8)
      effect: Proficiency +4 doubled by Expertise, baked into the displayed target
      stacks: Proficiency doesn't stack across sources; Expertise doubles the one bonus
      how: Self — Charlatan background + Rogue both grant Sleight of Hand proficiency; Rogue level-1 Expertise doubles it
    - source: Reliable Talent (Rogue 11)
      effect: Treats any d20 under 10 as a 10; removes natural-1 auto-fail → result ≥ 23
      stacks: A floor, not a bonus — turns every DC ≤ 23 item into an auto-steal
      how: Self — class feature at Rogue 11
    - source: Guidance (+1d4) — DOES NOT APPLY to the steal
      effect: Variable dice don't attach to the background pickpocket roll. Guidance DOES help the confront-check dialogue on a fail, and normal skill checks (lockpicking, disarming) — just not the Steal roll itself
      stacks: N/A for pickpocketing
      how: Common misconception — the War Cleric dip's Guidance is for dialogue/other checks, not stealing
    - source: Graceful Cloth → Cat's Grace
      effect: Advantage on ALL Dexterity checks incl. Sleight of Hand (2d20 take higher)
      stacks: Advantage does NOT stack — this alone fills the advantage slot
      how: Self — worn all game, passive always on
    - source: Gloves of Thievery
      effect: Advantage on Sleight of Hand
      stacks: Redundant with the Graceful Cloth (advantage doesn't stack) — backup only
      how: Self — Brem, Zhentarim basement
    - source: Bardic Inspiration — DOES NOT APPLY to the steal
      effect: 'Same background-roll problem as Guidance: a Bardic Inspiration die can''t be added to the pickpocket roll. Save it for the confront-check dialogue on a fail'
      stacks: N/A for pickpocketing
      how: Ally — useful for the social save if caught, not the lift
    - source: Flat SoH item bonuses (Smuggler's Ring +2, Gloves of Power +1)
      effect: Directly LOWER the displayed roll target — the ONLY lever that beats an over-floor target
      stacks: Additive and reflected in the UI number
      how: Self via gear swap — reserve for a rare over-DC-23 item; stack both for +3
    - source: Bless (+1d4) — DOES NOT APPLY
      effect: Nothing for stealing — Bless only buffs Attack Rolls and Saving Throws, not ability checks
      stacks: N/A
      how: Common misconception — verified useless for pickpocketing
    gear:
    - item: The Graceful Cloth
      effect: 'Cat''s Grace: Advantage on all DEX checks + up to +2 DEX (cap 20) — the single most important stealing item; makes every other advantage source redundant'
      where: Lady Esther, Rosymorn Monastery Trail (Act 1)
    - item: Gloves of Thievery
      effect: Advantage on Sleight of Hand (backup to the Cloth)
      where: Brem, Zhentarim basement (Act 1)
    - item: Amulet of Misty Step
      effect: Bonus-action Misty Step, no slot — instant break-line-of-sight escape
      where: Priestess Gut's chambers, Goblin Camp (Act 1)
    - item: Disintegrating Night Walkers
      effect: Bonus-action Misty Step (1/short rest) + web/grease immunity — 2nd free escape teleport
      where: True Soul Nere, Grymforge (Act 1)
    - item: Deathstalker Mantle
      effect: Invisible for 2 turns on a KILL (in combat) — NOT a theft-escape tool; kill-gated, does not trigger on a failed steal
      where: Dark Urge reward (Sceleritas Fel); Charles hands it to Asterion
    - item: Optional flat-bonus ring (Smuggler's Ring +2 / Gloves of Power +1)
      effect: Additive flat SoH that directly lowers the displayed target — for a rare over-DC-24 item
      where: Various vendors/loot; swap in only when needed
    setup_by_act:
      note: 'Key point on ''combat vs pickpocket gear'': Asterion basically does NOT swap. The Graceful Cloth is Clothing (not armour), so it stacks with Bracers of Defence, and its Cat''s Grace already gives advantage on Sleight of Hand — so his everyday combat kit steals at advantage with nothing to change. Gloves of Thievery become redundant once the Cloth is on. The only situational swap is a flat +SoH ring for a rare over-floor item, in for that one lift then back out. All swaps are free out of combat.'
      acts:
      - act: 1
        standing_kit: Graceful Cloth worn as the chest slot the moment you buy it from Lady Esther (Cat's Grace = advantage on DEX checks + DEX toward 18/20); Gloves of Thievery (Brem, Zhentarim basement) as an advantage backup.
        combat_vs_steal: No swap needed — the Cloth's advantage covers Sleight of Hand, so your normal light-armour kit already steals at advantage. Keep Gloves of Thievery in the bag unless you're not wearing the Cloth.
        buffs: None help the steal roll — Guidance/Bardic Inspiration don't apply to the background pickpocket check. DEX is only 17→18 here, so lean on advantage (Cloth) + Reliable Talent's floor; for a high-target item, swap in a flat +SoH ring. (Guidance is still worth casting for the confront-check dialogue if you get caught.)
        targets: Arron & Volo (Grove), Brem & Sparkle (Zhent basement), A'jak'nir Jeera + quartermaster (Crèche), Lady Esther. Lift scrolls, potions, gold; almost every Act 1 DC is under your guaranteed floor.
      - act: 2
        standing_kit: Same Graceful Cloth. When you equip Bracers of Defence (+2 AC, no-armour) they take the GLOVES slot that Gloves of Thievery use.
        combat_vs_steal: 'Still no steal-swap: wear Bracers of Defence full-time for the AC — the Cloth carries the stealing advantage, so the Gloves of Thievery are redundant. Only swap in a flat +SoH ring for a rare hard target.'
        buffs: DEX is 20 by now (Hag's Hair + Mirror if you've visited) → the flat +13 + Reliable Talent floor covers essentially everything. No steal-buffs needed; keep a flat +SoH ring handy for outliers.
        targets: Moonrise vendors (Araj Oblodra, Quartermaster Talli), Last Light Inn traders (Mattis, the Harpers). Clear scrolls, elixirs, and gear before the Act 2 point-of-no-return (Moonrise assault).
      - act: 3
        standing_kit: Graceful Cloth + Bracers of Defence. This is where a flat-bonus swap actually matters for the priciest vendor stock.
        combat_vs_steal: Combat kit and heist kit are the same. For an over-floor item, hot-swap a Smuggler's Ring (+2 SoH) or Gloves of Power (+1) into a ring/gloves slot just for that lift, then swap back. Do NOT rely on Disguise-Self identity resets — they don't work in the Lower City.
        buffs: Advantage from the Cloth + the floor handle almost everything. For the priciest over-floor items, swap a flat +SoH ring or Enthrall the vendor (Guidance/Bardic Inspiration don't apply). Toggle turn-based to freeze the investigation timer while you clear a whole vendor.
        targets: Sorcerous Sundries (scroll wall — Chain Lightning, Cone of Cold, Freezing Sphere), Lower City fences (Roah Moonglow), the Devil's Fee, circus/vendor stock. Highest-value heists in the game — but Lower City crime enforcement is the strictest, so launder aggressively.
    escape_options:
    - option: Quicksave / reload (non-Honour)
      how: THE reliable net. Quicksave before each steal; reload on a botched roll or getaway. Asterion rarely fails the roll (floor 23), so this mainly insures the escape / investigation sweep.
    - option: Turn-based mode
      how: 'Toggle ON before stealing: freezes patrols, the victim, and the post-theft investigation timer so you set up Hide and manage vision cones at your own pace. Each party member is an independent thief with its own check and caught-state.'
    - option: Break line of sight, wait out the search
      how: After a steal, immediately leave the victim's sight and the search radius; Hide (Cunning Action; near-automatic via Reliable Talent + Expertise). Wait a few turns for the investigation to expire → whole party permanently safe.
    - option: Hide in Fog Cloud / Darkness
      how: Auto stealth success inside — enemy sight cones don't reach in (unless Devil's Sight). Good for the initial Hide and for vanishing after.
    - option: Misty Step / Night Walkers / Amulet of Misty Step
      how: Bonus-action teleport (2–3 free/short rest) to break line of sight and clear the search area. Repositioning only — combine with waiting out the investigation.
    - option: Split loot / send to camp
      how: An accused character holding NO session-stolen goods proves innocence automatically. Keep stolen items off Asterion (hand to a clean character or send to the camp chest); use other members as extra thieves.
    - option: Enthrall (ally-cast)
      how: If the victim is Enthralled when they notice the theft, no investigation starts and no suspicion is placed. Best cast by someone OTHER than the thief.
    - option: Feign Death (ally-cast) on a caught member
      how: Stops NPCs initiating conversation with the caught character; guards usually disperse before it wears off.
    - option: Confront-check / return / drop
      how: On a first catch, pass the offered Deception/Intimidation/Persuasion check; stealing can sometimes be undone by dropping the item, pickpocketing sometimes by returning it.
    - option: Disguise Self (limited)
      how: Commit disguised, then dismiss (or vice-versa) to shed the culprit tag — works ONCE per character per jail and NOT in Act 3's Lower City.
    - option: NOT the Deathstalker Mantle
      how: Its invisibility triggers only on a KILL in combat — a failed steal is not a kill, so it can't pre-empt or undo being caught. It's a combat re-ambush cloak, not a theft escape.
    failure_flow:
      note: 'If you''re NOT reloading (self-imposed no-save-scum, or you just don''t want to reload) here''s the no-reload contingency for the exact chain you described: fail → dialogue → likely fail the social check → combat → vanish. Reality check: with Reliable Talent (floor 23) Asterion almost never fails the actual Sleight of Hand roll — the real risk is the post-theft investigation or a botched CONFRONT check. And his CHA is 8, so plan to FAIL the offered social save.'
      steps:
      - step: 1
        trigger: Roll fails / you're spotted
        do: The victim opens a dialogue or turns hostile. The theft dialogue offers a Deception / Intimidation / Persuasion check to talk your way out; returning the item can defuse a first offense.
      - step: 2
        trigger: The offered social check (you'll probably fail it)
        do: 'At CHA 8 Asterion flunks Deception/Persuasion more often than not. Better options: hand the conversation to Bonbon (the face) if he''s in range, pre-buff with Guidance/Friends, or just accept the fail and drop to step 3. Intimidation can be easier if the target is weak-willed.'
      - step: 3
        trigger: Talk fails → they call it in / attack
        do: 'Two branches: (a) it goes LOUD → combat as guards/victim aggro; or (b) a delayed ''Thief!'' investigation starts and reinforcements begin converging on your last known position.'
      - step: 4
        trigger: Break contact (the 'fog cloud or something' step)
        do: Bonus-action Hide (Reliable Talent ≈ automatic) → drop Fog Cloud or Darkness on yourself (auto-Obscured; enemy sight cones can't see in without Devil's Sight) → Cunning Action Disengage/Dash or a bonus-action Misty Step (Night Walkers / Amulet of Misty Step) out of the search radius. Toggle turn-based mode to do this at your own pace.
      - step: 5
        trigger: It went to combat
        do: If witnesses must die to clear the crime, burst them down — this is where the party nova (or a Fog-Cloud-then-AoE) shines — then leave the area so no survivor reports you. A kill in combat procs the Deathstalker Mantle (Invisible) to slip away and reposition.
      - step: 6
        trigger: Launder & reset
        do: 'Send stolen goods to camp or a clean party member (an accused character carrying no session-stolen loot auto-proves innocence). Wait out the investigation timer out of sight → the whole party goes permanently clean and can wear the loot openly. Worst case (Act 3 Lower City, no Disguise-Self reset): leave to a different district and let the heat cool.'
    procedure: |-
      0 — Standing kit: wear the Graceful Cloth (permanent Cat's Grace = advantage on DEX checks + DEX toward 20) all game; Gloves of Thievery as backup. Confirm DEX 20. This alone gives +13 flat, advantage, and (Rogue 11) a floor-10 die = guaranteed steal on any DC ≤ 23 item.
      1 — Isolate: split Asterion from the party and approach the target alone, so a botched job only implicates him and no ally is caught holding loot.
      2 — Confirm flat gear: the Graceful Cloth already gives advantage. For a high-target item, swap in a Smuggler's Ring (+2) / Gloves of Power (+1) — these LOWER the shown target. (Guidance/Bardic Inspiration do NOT help the steal roll.)
      3 — Quicksave.
      4 — Turn-based ON: freeze patrols, the victim, and the investigation timer.
      5 — Hide: bonus-action Hide (Cunning Action; near-automatic). If a vision cone is a problem, use Fog Cloud/Darkness (auto-hide).
      6 — Read targets: open the steal window (free while unseen). Roll target ≤ 10 = auto-lift; advantage from the Cloth makes higher targets very likely. Prioritize high value / low target (key gear, scrolls, buff sources). For a rare over-floor item, swap in a flat +SoH ring (Smuggler's/Gloves of Power) or just Enthrall the vendor and steal freely — Guidance/Bardic Inspiration won't help the roll.
      7 — Steal item by item: one per pickpocket. To pull more from the same NPC, re-hide or hand off to a second hidden member. Reload if a roll would fail.
      8 — Escape BEFORE the alert matures: break line of sight and leave the search radius — Cunning Action Disengage/Dash or a bonus-action Misty Step. Do NOT rely on the Deathstalker Mantle. Stay out of sight until the 'Thief!' investigation expires.
      9 — Launder the loot: keep stolen goods off Asterion if guards may sweep. If caught anyway: pass the confront check, return/drop the item, or have an ally Enthrall / Feign Death — or reload.
      10 — Turn-based OFF and resume.
  scores:
    fit: 4
    fun: 4
    power: 3
- name: The Ambusher — Ranged Sniper (Config B)
  is_primary: false
  role: Backline stealth sniper / DEX-save nuker / scout
  class: Arcane Trickster Rogue 11 / Fighter 1 (Archery)
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: Same as Config A. The Deathstalker Mantle covers the invisibility a Duergar would've given innately.
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background (can't be changed, even via respec)
  starting_stats:
    STR: 8
    DEX: 17
    CON: 14
    INT: 14
    WIS: 10
    CHA: 8
  ability_targets: 'DEX 17 → 18 (Hag''s Hair) → 20 (Graceful Cloth''s +2) — Mirror NOT needed on DEX. Redirect the Mirror to INT: INT 14 → 16 (R10 feat) → 18 (Mirror of Loss) for higher scroll DC.'
  feats:
  - at: R4
    feat: Sharpshooter
    note: Not Savage Attacker — that's melee-only and does nothing for crossbows. Toggle the −5 OFF while you still need reliable hits (it doesn't fight an acuity engine here, but accuracy from stealth matters).
  - at: R8
    feat: Alert
    note: First turn to open from stealth; immune to surprise.
  - at: R10
    feat: +2 INT
    note: Scroll DC → INT 16 (with the Mirror to 18). Dropped the Dual Wielder option — off-hand attacks can't carry Sneak Attack and are dead on a crossbow build.
  casting: Everything keys off INT (Fighter has no casting stat, so AT spells AND scrolls both use INT) — single-stat simplicity.
  key_spells:
  - 'AT: Shield, Disguise Self, Shadow Blade (backup)'
  - Offense = stolen scrolls (INT DC) + Ne'er Misser force Sneak Attack
  creation:
    level1_class: Rogue 1
    level1_gains: Expertise in 2 skills (Sleight of Hand + Stealth) + Sneak Attack (1d6). Character-creation class.
    subclass_choice: Arcane Trickster is chosen at Rogue 3 (character level 4).
    proficiencies:
      armor_weapons: 'Rogue base: Light armour; Simple weapons, Hand Crossbows, Longswords, Rapiers, Shortswords. The Fighter 1 dip (char 2) adds Medium armour, Shields, Martial weapons + the Archery fighting style — NO Heavy armour (multiclassing never grants it).'
      saving_throws: Dexterity + Intelligence (Rogue). The Fighter dip grants NO save proficiency (multiclass) — the 'CON save' the plan lists for Asterion is incorrect; he keeps Rogue's DEX+INT.
      skills: 'Rogue picks 4 skills + Expertise in 2 (Sleight of Hand + Stealth) at level 1; Astarion''s Charlatan background adds Sleight of Hand + Deception (Stealth comes from a Rogue pick). Expertise #2 (Perception + Investigation) at Rogue 6.'
    starting_cantrips: None from the class at Rogue 1. Astarion (High Elf) picks Booming Blade as his racial cantrip at creation (melee backup).
    starting_spells: None at Rogue 1 — first AT spells (3) at Rogue 3 (char 4).
    notes: 'Astarion. Single-stat INT: Fighter has no casting stat, so BOTH AT spells and stolen scrolls key off INT. 3 feats total (Rogue 4/8/10).'
  spells:
    note: Everything keys off INT (single-stat simplicity). Config B's damage is crossbows (Ne'er Misser force Sneak Attack), so its 'spells' are mostly the Fighter features + utility + the scroll arsenal. Mandatory = the loop depends on it; Recommended = flex + scrolls.
    mandatory:
    - spell: 'Fighting Style: Archery'
      level: Feature (Fighter 1)
      school: N/A (passive)
      save: None
      when: char 2 (Fighter 1)
      why: +2 to ranged attack rolls — the sole reason for the dip on a hand-crossbow sniper (Ne'er Misser + Hellfire Hand Crossbow).
    - spell: Mage Hand
      level: Cantrip (free)
      school: Conjuration
      save: None
      when: char 4 (Rogue 3)
      why: 'Invisible hand: scouts, throws water bottles for Wet (no action), and flanks to enable Sneak Attack.'
    - spell: Shield
      level: '1'
      school: Abjuration
      save: None (reaction)
      when: char 4 (Rogue 3, any-school pick)
      why: +5 AC and Magic Missile immunity — main survival button.
    - spell: Second Wind
      level: Feature (Fighter 1)
      school: N/A (class action)
      save: None
      when: char 2 (Fighter 1)
      why: 'Free with the level: bonus-action self-heal (1d10 + Fighter level), short-rest recharge — a minor panic button for the frail assassin.'
    recommended:
    - spell: Booming Blade
      level: Cantrip
      school: Evocation
      save: Melee weapon attack (DEX)
      when: char 1 (High Elf racial) / char 4
      why: Melee Sneak-Attack delivery when forced into adjacency; backup to the crossbows.
    - spell: Shadow Blade
      level: '2'
      school: Illusion
      save: None (bonus action)
      when: char 8 (Rogue 7, replacement)
      why: Darkness/adjacency melee backup only in Config B (no Resonance Stone psychic payoff since the primary weapon is a crossbow).
    - spell: Disguise Self
      level: '1'
      school: Illusion
      save: None
      when: char 4 (Rogue 3)
      why: Infiltration / fresh identity after a botched steal.
    - spell: Fog Cloud
      level: '1'
      school: Conjuration
      save: None
      when: char 4+
      why: Self-obscure to Hide (arms Magical Ambush) and feed the Eversight darkness combo.
    - spell: Misty Step
      level: '2'
      school: Conjuration
      save: None
      when: char 8+ (replacement)
      why: Reposition/escape beyond the item teleports.
    - spell: Ice Storm (scroll)
      level: '4'
      school: Evocation
      save: DEX save
      when: stolen scroll (DC uses INT)
      why: The real DEX-save cold AoE (works fully with Magical Ambush) — prefer over the CON-save cold nukes when DEX-save is the goal.
    - spell: Chain Lightning (scroll)
      level: '6'
      school: Evocation
      save: DEX save
      when: stolen scroll
      why: True DEX-save AoE; full Magical Ambush benefit.
    - spell: Cone of Cold (scroll)
      level: '5'
      school: Evocation
      save: CON save (NOT DEX)
      when: stolen scroll
      why: Big cold nuke but a CON save — contradicts the plan's 'DEX-save cold' label; Magical Ambush still disadvantages the save.
  leveling:
  - char_level: 2
    class: Fighter 1
    gains: Archery fighting style (+2 ranged); medium armour + shields + martial weapons — but NO save proficiency (multiclass dips grant none; Asterion keeps Rogue's DEX + INT saves)
  - char_level: 3
    class: Rogue 2
    gains: Cunning Action (bonus-action Hide)
  - char_level: 4
    class: Rogue 3
    gains: 'Arcane Trickster: invisible Mage Hand; Booming Blade; Shield, Disguise Self'
  - char_level: 5
    class: Rogue 4
    gains: 'Feat: Sharpshooter'
  - char_level: 6
    class: Rogue 5
    gains: Uncanny Dodge
  - char_level: 7
    class: Rogue 6
    gains: 'Expertise #2 (Perception + Investigation)'
  - char_level: 8
    class: Rogue 7
    gains: Evasion + 2nd-level slots → Shadow Blade (adjacency backup); Sneak Attack 4d6
  - char_level: 9
    class: Rogue 8
    gains: 'Feat: Alert'
  - char_level: 10
    class: Rogue 9
    gains: Magical Ambush
  - char_level: 11
    class: Rogue 10
    gains: 'Feat: flex + 3rd cantrip'
  - char_level: 12
    class: Rogue 11
    gains: Reliable Talent; Sneak Attack 6d6
  itemization:
    act1:
    - id: graceful-cloth
      item: Graceful Cloth
      note: Graceful Cloth (advantage on stealing)
    - id: gloves-of-thievery
      item: Gloves of Thievery
      note: Gloves of Thievery
    - id: two-1-hand-crossbows
      item: Two +1 Hand Crossbows
      note: Two +1 Hand Crossbows (placeholder)
    - id: knife-of-the-undermountain-king
      item: Knife of the Undermountain King
      note: Knife of the Undermountain King (early melee backup)
    - id: night-walkers-amulet-of-misty-step
      item: Night Walkers + Amulet of Misty Step
      note: Night Walkers + Amulet of Misty Step
    - id: hoard-superior-elixir-of-arcane-cultivation-battlemage-elixirs
      item: Hoard Superior Elixir of Arcane Cultivation + Battlemage Elixirs
      note: Hoard Superior Elixir of Arcane Cultivation + Battlemage Elixirs
    act2:
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      note: Deathstalker Mantle (Invisible on kill)
    - id: bracers-of-defence
      item: Bracers of Defence
      note: Bracers of Defence (+2 AC, no armour)
    - id: keep-stealing-scrolls
      item: Keep stealing scrolls
      note: Keep stealing scrolls
    act3:
    - id: ne-er-misser
      item: Ne'er Misser
      note: Ne'er Misser (main-hand — force Sneak Attack, bypasses resistances, free L3 Magic Missile). Available a whole act early at Moonrise (Act 2)
    - id: hellfire-hand-crossbow
      item: Hellfire Hand Crossbow
      note: Hellfire Hand Crossbow (off-hand)
    - id: eversight-ring
      item: Eversight Ring
      note: Eversight Ring (Darkness 'Asterion' combo — grab it in Act 2 at Reithwin's House of Healing; it's missable)
    - id: neck-slot-free
      item: Neck slot free
      note: Neck slot free (Amulet of Greater Health went to Gale) — use a defensive amulet; the backline sniper needs CON even less than Config A
    - id: does-not-carry-the-resonance-stone
      item: Does NOT carry the Resonance Stone
      note: Does NOT carry the Resonance Stone (backline — force damage doesn't benefit; the Paladin runs the self-contained Pike + Bhaalist instead)
  playstyle: |-
    - Identical Hide → Magical-Ambush loop as Config A, but **from the backline** — snipe a Sneak-Attack crossbow shot (force, via Ne'er Misser) or a disadvantaged AoE scroll, never entering melee.
    - Mage Hand still throws water for the Sorcerer and flanks to enable Sneak Attack.
    - The cleanest positional split from the melee Paladin.
    - **CO-EQUAL with Config A** (no single 'primary'): this is the safe default — backline, no Stone/Elixir dependency, and it works fine vs undead; pick Config A when you want the higher psychic-nova ceiling on a living boss.
  traps:
  - Savage Attacker is melee-only — useless on crossbows; take Sharpshooter instead.
  - Same Magical Ambush / Superior Elixir / Eversight caveats as Config A.
  - Loses the psychic-×2 / Hold-auto-crit Shadow-Blade payoff (crossbows aren't psychic) and the War Cleric's Create Water / Guidance / WIS-saves; gains range safety, +2 accuracy, one-stat simplicity.
  - 'Pickpocketing: see Config A''s pickpocket section — identical. (Guidance/Bardic Inspiration don''t help the steal roll in either config, so Config B losing self-Guidance costs nothing for stealing; use flat +SoH gear for hard targets.)'
  scores:
    fit: 5
    fun: 4.5
    power: 3.5
---

