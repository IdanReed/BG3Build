---
nickname: Asterion
builds:
- name: The Fist in the Dark
  is_primary: true
  role: Mobile Open-Hand monk — stun-lock striker, psychic flurry, party thief
  class: Open Hand Monk 9 / Thief Rogue 3
  build_order: Rogue 1 (creation, Expertise) → Monk 1–9 → Rogue 2 → Thief 3. No respec after the initial rebuild.
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: 'Fey Ancestry (advantage vs Charm, no magical Sleep), Darkvision, one High Elf wizard cantrip, bonus-action Vampire Bite. ⚠ Must stay unarmoured and shieldless; after Tavern Brawler both melee hands stay empty so Attack/Extra Attack are unarmed. Graceful Cloth is Clothing, not armour, and Bracers of Defence work unarmoured and shieldless.'
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background, unchangeable even by respec.
  starting_stats:
    STR: 8
    DEX: 17
    CON: 14
    INT: 10
    WIS: 16
    CHA: 8
  stats_note: 'Point-buy 8/15/14/10/15/8 = all 27 (DEX 15 + WIS 15 cost 9 each); High Elf +2 → DEX 17, +1 → WIS 16. DEX drives unarmed attack, Unarmoured AC (10 + DEX + WIS), Stun DC and pickpocket; STR comes from the daily elixir.'
  ability_targets: 'MODDED Hair: DEX 17 → 18 → 20 via Graceful Cloth (its +2 caps at 20). Mirror of Loss goes to WIS 16 → 18. STR stays 8 because the elixir overrides it.'
  feats:
  - at: Monk 4 (char 5)
    feat: Tavern Brawler
    note: 'The engine, and one of only TWO S+ feats in the tier list (Alert is the other — Asterion takes both, and nobody else in the party takes either). Adds your STR modifier to unarmed attack rolls AND damage a second time. Drink Giant Strength each long rest and UNEQUIP Corellon''s Grace so main-action attacks are empty-hand punches. Once STR > DEX it also drives attack rolls and the Stun DC (BG3 monk DCs use the higher of DEX/STR). Cloud Giant (STR 27, +8) is the ceiling. ⚠ SCOPE: the feat also covers Throw and Improvised Melee Weapon attacks, neither of which requires empty hands — only the base Unarmed Strike action needs "no melee weapons equipped." Asterion punches, so the hands-empty rule binds him exactly as written, but it never blocks a thrown consumable.'
  - at: Monk 8 (char 9)
    feat: Alert
    note: '+5 Initiative and immunity to Surprise — with DEX 20 that is a near-guaranteed first turn to open-strike and Stun the priority target before it acts. (Alternative: +2 WIS for more AC and rider damage.)'
  key_abilities:
  - Flurry of Blows — Open Hand variants Topple (Prone) / Stagger (no Reactions) / Push
  - Stunning Strike — the party's on-demand hard control
  - Manifestation of Mind — +psychic per unarmed hit, DOUBLED by the Resonance Stone
  - Ki Resonation (Punch → Blast) — AoE finisher
  - Step of the Wind / Patient Defense / Deflect Missiles — mobility + defense
  - Fast Hands (Thief) → two Flurries of Blows per turn
  combat_style: 'Char 2–4 — Corellon''s Grace improves Flurry punches and saves and gives a stronger pre-feat main attack. Char 5 — Tavern Brawler takes over: unequip every melee weapon, stay unarmoured and shieldless, drink a daily Giant Strength elixir, punch.'
  creation:
    level1_class: Rogue 1 (taken at character creation / first class in the respec)
    level1_gains: '4 Rogue skill proficiencies (Stealth, Investigation, Acrobatics, Insight) + Expertise in 2 of them (Sleight of Hand + Stealth) + Sneak Attack 1d6 (vestigial once he punches — it needs a finesse weapon, not fists). MUST be the creation class so Expertise lands on the thief skills.'
    subclass_choice: Open Hand (Monk 3) · Thief (Rogue 3)
    proficiencies:
      armor_weapons: Unarmed and unarmoured — required for Martial Arts / Flurry / Unarmoured Defence.
      saving_throws: DEX + INT (Rogue).
      skills: 'Charlatan (Deception, Sleight of Hand) + Elf Keen Senses (Perception) + 4 Rogue picks (Stealth, Investigation, Acrobatics, Insight). Expertise: Sleight of Hand + Stealth (Rogue 1). Only Rogue 3, so no second Expertise pair and no Reliable Talent.'
    starting_cantrips: 'One High Elf racial cantrip, but it is NOT selectable on a recruited companion — race-related choices are fixed and the respec does not re-present them. Read it off the save; nothing in the build depends on it.'
    starting_spells: None — Ki/martial build.
    notes: '2 feats (Monk 4 + Monk 8). Rogue 1 FIRST for Expertise, then Monk 1–9, then Thief. Daily Giant Strength elixir; DEX stays for pickpocketing.'
  spells:
    note: Not a caster. His build-defining Ki abilities and martial features appear at their unlock levels in the Leveling guide; this panel tracks the one High Elf racial cantrip.
    mandatory:
    - spell: Flurry of Blows (+ Open Hand variants)
      level: Feature (Monk 1; Open Hand variants Monk 3)
      school: Ki — Bludgeoning + rider
      save: 'Topple: DEX · Push: STR · Stagger: none (weapon-action DC)'
      when: char 2 (Monk 1) / char 4 (Monk 3)
      why: 'Bonus action + 1 Ki → two unarmed strikes. Open Hand adds Topple (Prone → allies attack at advantage), Stagger (no Reactions) and Push (5m + fall damage). With Fast Hands or Wholeness of Body, Flurry TWICE per turn.'
    - spell: Stunning Strike
      level: Feature (Monk 5)
      school: Ki — control
      save: CON save (DC 8 + prof + higher of DEX/STR)
      when: char 6 (Monk 5)
      why: 'The party contribution — 1 Ki on a hit, CON save or Stunned (auto-fails STR/DEX saves, attacked at advantage, loses its turn). Locks bosses and hands Charles free crits. The DC rides the elixir''s STR, up to +8.'
    - spell: Manifestation of Mind
      level: Feature (Open Hand, Monk 6)
      school: Toggle — Psychic
      save: None
      when: char 7 (Monk 6)
      why: Every unarmed strike deals +1d4 + WIS PSYCHIC. At 4–6 hits a turn, ALL of it doubles under the Resonance Stone — how the Monk joins the psychic engine without a Shadow Blade. Toggle to Soul/Body for radiant/necrotic vs psychic-resistant foes.
    - spell: Extra Attack
      level: Feature (Monk 5)
      school: N/A
      save: None
      when: char 6 (Monk 5)
      why: With both melee hands empty, the Action supplies two unarmed strikes; the Martial-Arts bonus strike and Flurry stack on top.
    - spell: 'Tavern Brawler + Giant Strength elixir'
      level: Feat (Monk 4) + consumable
      school: N/A
      save: None
      when: char 5
      why: Daily Elixir of Giant Strength. TB adds that STR mod to every unarmed attack AND damage a second time, and once STR > DEX it drives attack rolls and the Stun DC. The accuracy and damage backbone.
    recommended:
    - spell: Minor Illusion
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: char 1 (High Elf racial cantrip — fixed, not selectable)
      why: 'Would be the ideal pick — S tier for pulling creatures toward a distraction with no save, redirecting sightlines for stealth and theft without touching his low INT — but a recruited companion''s racial cantrip is locked at creation and the respec does not re-present it. Listed here as the thing to hope for, not a pick to make; check the save for what he actually has.'
    - spell: Ki Resonation (Punch → Blast)
      level: Feature (Open Hand, Monk 9)
      school: Ki — detonate
      save: CON save
      when: char 10 (Monk 9)
      why: Punch to mark a target Resonating, then Blast to detonate an AoE around it (party and summons excluded) — a nova finisher on clustered packs.
    - spell: Step of the Wind
      level: Feature (Monk 2)
      school: Ki — mobility
      save: None
      when: char 3 (Monk 2)
      why: Bonus-action Dash/Disengage (jumping is free) — dive the backline, reposition, leave melee without opportunity attacks.
    - spell: Patient Defense
      level: Feature (Monk 2)
      school: Ki — defense
      save: None
      when: char 3 (Monk 2)
      why: Bonus action + Ki → attackers have Disadvantage and he has advantage on DEX saves. The survival button for a no-armour body.
    - spell: Deflect Missiles
      level: Feature (Monk 3)
      school: Reaction
      save: None
      when: char 4 (Monk 3)
      why: Reduce a ranged attack by 1d10 + DEX + monk level (often to 0) and optionally hurl it back — a hard counter to archers.
    - spell: Wholeness of Body
      level: Feature (Open Hand, Monk 6)
      school: Ki — heal + economy
      save: None
      when: char 7 (Monk 6)
      why: 'Action: heal 3× monk level, refund half his Ki, and gain an EXTRA bonus action for 3 turns — two Flurries per turn even before the Thief dip. Once per long rest.'
    - spell: Fast Hands (Thief)
      level: Feature (Thief, Rogue 3)
      school: N/A
      save: None
      when: char 12 (Thief 3)
      why: A permanent second bonus action → Flurry of Blows TWICE per turn (2 Ki, 4 extra strikes) on top of the Attack action; also fuels Cunning Action utility.
    - spell: Vampire Bite
      level: Racial (Vampire Spawn)
      school: Bonus action — Necrotic + heal
      save: None
      when: char 1
      why: A free bonus-action heal/buff on a grappled or downed foe, mostly out of combat — minor in the flurry economy, but it costs nothing.
  leveling:
  - char_level: 1
    class: Rogue 1
    gains:
    - Sneak Attack 1d6
    - Four Rogue skill proficiencies
    - Expertise selections ×2
    - DEX + INT saving-throw proficiency
    - Vampire Bite (Astarion origin action)
    recommendations:
    - category: Skills
      recommendation:
      - Stealth
      - Investigation
      - Acrobatics
      - Insight
      note: 'SIX picks land on this level, not two — Rogue grants 4 skill proficiencies BEFORE the 2 Expertise picks, and it is easy to click past them. Stealth is mandatory rather than optional: Charlatan supplies Sleight of Hand and Elf Keen Senses supplies Perception, but nothing grants Stealth, so without picking it here the Expertise: Stealth choice below has no valid target. Investigation is the party''s only coverage — Charles, Gale and Bonbon all lack it. Acrobatics rides DEX 17→20 and Insight rides WIS 16→18. ALTERNATIVE worth considering: swap Insight (already covered by Gale and Bonbon) for Athletics — on the daily Giant Strength elixir Asterion hits STR 27, making him the party''s only viable shove/grapple carrier; update proficiencies.md to match if you take it.'
    - category: Expertise
      recommendation:
      - Sleight of Hand
      - Stealth
      note: The reason Rogue must be the first class; these power stealing and scouting for the whole run.
    - category: Racial cantrip
      recommendation: Fixed — not a choice
      note: '⚠ NOT a selection. Astarion is a recruited companion, and the wiki is explicit that race-related choices carry over unchanged: "the selectable aspects of any given race, such as a high elf''s choice of cantrip, also remain fixed" (Withers, Services). The Withers respec will not re-present it, so he keeps whatever Larian assigned. Check the cantrip on the save rather than planning around it. If it turns out to be Bone Chill that is a fine outcome — A tier, "targets AC at range, prevents healing, and gives undead disadvantage on attacks" — and nothing in this build depends on the cantrip either way.'
  - char_level: 2
    class: Monk 1
    gains:
    - Unarmoured Defence
    - Martial Arts (DEX-based unarmed attacks and a bonus unarmed strike)
    - Flurry of Blows
    - Martial Arts die 1d4
  - char_level: 3
    class: Monk 2
    gains:
    - Unarmoured Movement
    - Patient Defence
    - Step of the Wind (Dash and Disengage)
  - char_level: 4
    class: Monk 3
    gains:
    - Deflect Missiles
    - Martial Arts die 1d6
    recommendations:
    - category: Subclass
      recommendation: Way of the Open Hand
      note: Adds Topple, Stagger and Push variants to Flurry of Blows.
  - char_level: 5
    class: Monk 4
    gains:
    - Slow Fall
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Tavern Brawler
      note: Adds the Giant-Strength modifier to unarmed attack and damage rolls a second time — the build's accuracy and damage engine.
  - char_level: 6
    class: Monk 5
    gains:
    - Extra Attack
    - Stunning Strike (Melee and Unarmed)
  - char_level: 7
    class: Monk 6
    gains:
    - Manifestation of Body, Mind, and Soul
    - Wholeness of Body
    - Ki-Empowered Strikes
  - char_level: 8
    class: Monk 7
    gains:
    - Evasion
    - Stillness of Mind
  - char_level: 9
    class: Monk 8
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Alert
      note: +5 Initiative and immunity to Surprise let him disable a priority target before it acts. A +2 WIS ASI is the defensive alternative.
  - char_level: 10
    class: Monk 9
    gains:
    - Advanced Unarmoured Movement
    - Ki Resonation attacks and Blast
    - Martial Arts die 1d8
  - char_level: 11
    class: Rogue 2
    gains:
    - Cunning Action (Dash, Disengage, and Hide)
  - char_level: 12
    class: Rogue 3 (Thief)
    gains:
    - Fast Hands (permanent second bonus action)
    - Second-Story Work
    recommendations:
    - category: Subclass
      recommendation: Thief
      note: Fast Hands enables two Flurries per turn — the whole reason for the three-level Rogue tail.
  itemization:
    act1:
    - id: corellon-s-grace
      item: Corellon's Grace (levels 2–4 only)
      slot: weapons
      note: EARLY ONLY, from Auntie Ethel. Before Tavern Brawler the staff attack is a solid main Action, Natural Pugilist improves bonus-action and Flurry punches, and unarmoured gives +2 saves. ⚠ UNEQUIP at char 5 — Attack/Extra Attack otherwise swing the staff and lose Tavern Brawler, even though Flurry still works.
    - id: dual-hand-crossbows-plus-one
      item: Dual Hand Crossbows +1
      slot: ranged weapons
      note: Act-1 weapon traders. Rogue proficiency gives a main-hand shot plus a bonus-action off-hand shot when melee is out of reach. Ranged set only, so the melee hands stay empty for Tavern Brawler.
    - id: graceful-cloth
      item: Graceful Cloth
      wiki: The Graceful Cloth
      slot: armour
      note: 'Lady Esther, Rosymorn trail. Cat''s Grace = advantage on DEX checks (stealing) plus DEX toward 20. It is Clothing, so Unarmoured Defence still works — worn all game.'
    - id: bracers-of-defence
      item: Bracers of Defence
      slot: hands
      note: DEFAULT DEFENCE. Blighted Village cellar. +2 AC unarmoured and shieldless. Swap to the offensive gloves below when faster kills beat 2 AC.
    - id: the-sparkle-hands
      item: The Sparkle Hands (offensive alternative)
      slot: hands
      note: EARLY OFFENCE. Decrepit Sanctuary, Sunlit Wetlands. 2 Lightning Charges per unarmed hit — charges add attack and damage, periodically burst for 1d8 Lightning, and grant advantage against metal-armoured enemies and constructs.
    - id: gloves-of-cinder-and-sizzle
      item: Gloves of Cinder and Sizzle (offensive alternative)
      slot: hands
      note: LATE-ACT-1 OFFENCE. Lady Esther. +1d4 Fire per unarmed hit, so a Flurry turn applies it repeatedly, plus a level-3 Scorching Ray 1/long rest. Prefer Sparkle Hands vs metal or fire resistance.
    - id: gloves-of-thievery
      item: Gloves of Thievery
      slot: hands
      note: Brem, Zhentarim — pickpocket backup. Keep them bagged once Bracers of Defence take the glove slot, since Graceful Cloth already covers stealing advantage.
    - id: elixir-of-giant-strength
      item: Elixir of Giant Strength (daily)
      wiki: Elixir of Hill Giant Strength
      slot: consumables
      note: Hill Giant (STR 21) early → Cloud Giant (STR 27) later. Powers Tavern Brawler damage and, since STR > DEX, his attack rolls and Stunning-Strike DC. Occupies the one-elixir-per-rest slot.
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      wiki: The Deathstalker Mantle
      slot: cloaks
      note: Dark Urge reward, handed over by Charles. Invisible for 2 turns on a kill — reposition and re-engage, perfect for a diving monk.
    - id: disintegrating-night-walkers
      item: Disintegrating Night Walkers
      slot: feet
      note: Nere, Grymforge. Free Misty Step once per short rest plus immunity to difficult terrain from surfaces, Enwebbed and Entangled — the permanent combat boots over Boots of Speed.
    - id: ring-of-protection
      item: Ring of Protection
      slot: rings
      note: Mol's reward for Steal the Sacred Idol after the Grove resolves. +1 AC and all saving throws — Asterion gets it because he is the exposed unarmoured melee character.
    - id: crusher-s-ring
      item: Crusher's Ring
      slot: rings
      note: DEFAULT second combat ring. Take it from Crusher at the Goblin Camp for +3m movement; it stacks with Longstrider and reaches the priority target without spending a bonus action.
    - id: sentient-amulet
      item: Sentient Amulet
      slot: amulets
      note: Grymforge, Adamantine chest. Ki Restoration (2 Ki, 1/long rest) plus Shatter — a cheap early neck that refuels Flurries. Mind the WIS-save Hysterical side effect on the rare version.
    - id: armour-of-uninhibited-kushigo
      item: Armour of Uninhibited Kushigo (defensive alternative)
      slot: armour
      note: Grymforge, for returning Sergeant Thrinn's boots. During Patient Defence, Kushigo Counter gives a reaction unarmed strike when an attacker misses. Graceful Cloth stays default — use this only for a counter fight.
    - id: haste-helm-late-act1
      item: Haste Helm (situational loan)
      slot: head
      note: Charles normally keeps it — his Ring frees the head slot. Borrow it when Charles does not need the speed, though Monk movement makes the loan optional.
    act2:
    - id: resonance-stone
      item: Resonance Stone (carries it)
      wiki: Resonance Stone
      slot: other
      note: 'Resonance Stone (Mind Flayer Colony, late Act 2). He places/carries it — Manifestation of Mind psychic + Psionic Overload across 4–6 hits/turn are all doubled. NEW SYNERGY since Gale became a Fire Sorlock: the aura also gives enemies disadvantage on mental saving throws, and Command and both Hold spells are WIS saves — so anything standing near Asterion is close to unable to resist Gale''s control on top of an Arcane Acuity DC in the low 30s. Keep the Stone near the enemies Gale intends to Command. ⚠ Its aura also makes the party (and him — no Gnome Cunning) psychic-vulnerable + disadvantaged on mental saves; keep it inside Charles''s Aura of Protection, or skip it vs psychic/mind enemies.'
    - id: eversight-ring
      item: Eversight Ring (Darkness fights)
      wiki: Eversight Ring
      slot: rings
      note: House of Healing morgue. Prevents Blindness — equip it when Asterion must fight beside Charles inside magical Darkness; keep Ring of Protection in ordinary encounters.
    act3:
    - id: gloves-of-soul-catching
      item: Gloves of Soul Catching
      slot: hands
      note: House of Hope, Hope's reward. +1d10 Force per unarmed hit, +2 CON, and once/turn heal 10 HP OR +5 to an attack or save. Best-in-slot monk gloves; replaces Bracers.
    - id: mask-of-soul-perception
      item: Mask of Soul Perception
      slot: head
      note: Devil's Fee — locked chest in Helsik's room, DC 20. +2 to Attack rolls, Initiative and Perception, plus Detect Thoughts.
    - id: boots-of-uninhibited-kushigo
      item: Boots of Uninhibited Kushigo
      slot: feet
      note: Astral Plane — Prelate Lir'i'c, at the start of Act 3. Adds his WIS modifier to every unarmed strike, so flat damage on every hit.
  playstyle: |-
    - **Prep:** drink Giant Strength, enable Manifestation of Mind, and carry the Resonance Stone from Act 2 onward.
    - **Turn:** Stunning Strike the priority target, then Flurry: Topple (or Stagger against casters). Thief 3 adds a second Flurry.
    - **If Stun fails:** raw Flurries + Topple; switch Manifestation to Soul against psychic resistance.
  pickpocket:
    note: |-
      The party thief. Only Rogue 3, so there is no Reliable Talent floor and a steal CAN fail on a low roll. Expertise plus Graceful Cloth advantage still clears nearly every Act 1–2 lift; save-scum the rare high-DC item.

      Must-have high-DC item: quicksave-scum, Enthrall the vendor (ally-cast), or hand the lift to someone else. Escape is standard — turn-based mode to freeze timers, break line of sight, pass loot to a clean member, wait out the investigation.
    success_math: 'At char 12: DEX 20 (+5) + prof 4 doubled by Expertise (+8) = +13 flat, with Graceful Cloth advantage. No Reliable-Talent floor, so a low roll CAN fail — rare, and most targets sit well under. ⚠ Guidance and Bardic Inspiration do NOT apply to the background pickpocket roll; only flat Sleight-of-Hand gear does.'
    gear:
    - item: The Graceful Cloth
      effect: 'Cat''s Grace — advantage on DEX checks (stealing) plus DEX toward 20. Clothing, so Unarmoured Defence still works. Worn all game.'
      where: Lady Esther, Rosymorn Monastery Trail (Act 1)
    - item: Gloves of Thievery
      effect: Advantage on Sleight of Hand — the backup once the Cloth takes the glove slot.
      where: Brem, Zhentarim Basement (Act 1)
    - item: Smuggler's Ring (+2) / Gloves of Power (+1)
      wiki:
      - Smuggler's Ring
      - Gloves of Power
      effect: Flat +Sleight of Hand — the only lever that beats an over-floor target; swap in for that one lift.
      where: Various vendors / loot
  traps:
  - 'From char 5 onward, stay UNARMOURED, SHIELDLESS and EMPTY-HANDED. A monk weapon does not disable Martial Arts, Flurry or special unarmed commands, but ordinary main-action attacks swing it and lose Tavern Brawler and the unarmed riders.'
  - 'The Giant Strength elixir is load-bearing (attack, damage, Stun DC) and takes the one-elixir-per-long-rest slot — no Bloodlust or Battlemage alongside it. Bank a stack.'
  - 'Stunning Strike is a CON save — high-CON bosses, legendary resistance and undead may shrug it. Do not build the whole turn around it landing.'
  - 'No Reliable Talent (only Rogue 3) — high-DC pickpocketing can fail; save-scum or use flat +SoH gear.'
  - 'The Resonance Stone debuffs the party''s mental saves and makes HIM psychic-vulnerable (no Gnome Cunning) — cluster it in Charles''s Aura of Protection or leave it holstered against psychic enemies.'
  - 'Only 2 feats (Monk 4 + Monk 8), both spent on Tavern Brawler and Alert. A Monk 8 / Thief 4 split buys a third feat at the cost of Ki Resonation — a real option, but not this plan.'
  illithid:
    note: 'Ability Drain — A-tier, free passive, and his alone in this party. Once per turn when he makes an attack roll, the target''s matching ability drops by 1 (Strength or Dexterity for unarmed strikes), degrading the enemy''s own offence, and it counts as inflicting a condition. ⚠ Once per TURN, not per hit, so it does not scale with his 4–6 strikes. Also worth buying Luck of the Far Realms for him: Charles''s stacked crit-threshold gear makes the reaction fire early on hits that were already crits, whereas Asterion stacks none and gets a reliable trigger. ⚠ Cull the Weak is mutually exclusive with Non-Lethal Attacks — toggle it off before any knockout you need to leave alive. Alert makes him the first-turn Black Hole carrier — the pull has no save, and targets inside the Stone aura roll its secondary Slow save at disadvantage vs his DC 17. He still has two Flurries afterward; when grouping is unnecessary, pre-cast Psionic Overload and keep the Action for two attacks. Cull the Weak handles mob cleanup — off when a kill must trigger Deathstalker. Bonbon keeps Mind Blast. NOT Awakened — his bonus actions are Flurries/Step.'
---
