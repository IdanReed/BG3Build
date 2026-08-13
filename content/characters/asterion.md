---
nickname: Asterion
builds:
- name: The Fist in the Dark
  is_primary: true
  role: Mobile Open-Hand monk — stun-lock striker, psychic flurry, party thief
  class: Open Hand Monk 9 / Thief Rogue 3
  build_order: Rogue 1 (creation, Expertise) → Monk 1–9 → Rogue 2 → Thief 3. No further respec after the initial rebuild.
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: 'Fey Ancestry (advantage vs Charm, no magical Sleep), Darkvision, one High Elf wizard cantrip, bonus-action Vampire Bite. He must remain unarmoured and shieldless; after Tavern Brawler arrives his melee hands stay empty so ordinary Attack/Extra Attack actions are unarmed. Corellon''s Grace is useful only before Tavern Brawler: it preserves Flurry and special unarmed commands, but ordinary main-action attacks swing the staff. Graceful Cloth is Clothing (not armour) and Bracers of Defence work while unarmoured and shieldless.'
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background (can't be changed, even via respec).
  starting_stats:
    STR: 8
    DEX: 17
    CON: 14
    INT: 10
    WIS: 16
    CHA: 8
  stats_note: 'Point-buy base 8/15/14/10/15/8 = all 27 (DEX 15 + WIS 15 cost 9 each); High Elf +2 → DEX 17, +1 → WIS 16 (+3). DEX drives unarmed attack, Unarmoured AC (10 + DEX + WIS), Stunning-Strike DC, and pickpocket; STR is supplied by a daily Giant Strength elixir.'
  ability_targets: 'MODDED Hair: DEX 17 → 18 (Hag''s Hair) → 20 from Graceful Cloth (its +2 is capped at 20). Mirror of Loss goes to WIS: 16 → 18. STR stays 8 because the elixir overrides it.'
  feats:
  - at: Monk 4 (char 5)
    feat: Tavern Brawler
    note: 'The engine: adds your STR modifier to unarmed attack rolls AND damage a second time. Drink an Elixir of Giant Strength each long rest and UNEQUIP Corellon''s Grace so ordinary main-action attacks use empty-hand punches. Once STR > DEX it ALSO drives your attack rolls and Stunning-Strike DC (BG3 monk DCs use the higher of DEX/STR). Cloud Giant (STR 27, +8) is the ceiling.'
  - at: Monk 8 (char 9)
    feat: Alert
    note: '+5 initiative + immunity to Surprise — with DEX 20 that is a near-guaranteed first turn to open-strike and Stun the priority target before it acts. (Alternative: +2 WIS for more AC + rider damage.)'
  key_abilities:
  - Flurry of Blows — Open Hand variants Topple (Prone) / Stagger (no Reactions) / Push
  - Stunning Strike — the party's on-demand hard control
  - Manifestation of Mind — +psychic per unarmed hit, DOUBLED by the Resonance Stone
  - Ki Resonation (Punch → Blast) — AoE finisher
  - Step of the Wind / Patient Defense / Deflect Missiles — mobility + defense
  - Fast Hands (Thief) → two Flurries of Blows per turn
  combat_style: 'At character levels 2–4, Corellon''s Grace improves Flurry punches and saving throws while supplying a stronger pre-feat main attack. At character level 5, Tavern Brawler becomes the engine: unequip every melee weapon, stay unarmoured and shieldless, drink a daily Giant Strength elixir, and make empty-hand attacks.'
  creation:
    level1_class: Rogue 1 (taken at character creation / first class in the respec)
    level1_gains: 'Expertise in 2 skills (Sleight of Hand + Stealth) + Sneak Attack 1d6 (vestigial once he punches — Sneak Attack needs a finesse weapon, not fists). MUST be the creation class so Expertise lands on the thief skills.'
    subclass_choice: Open Hand (Monk 3) · Thief (Rogue 3)
    proficiencies:
      armor_weapons: Unarmed & unarmoured — required for Martial Arts / Flurry / Unarmoured Defence.
      saving_throws: DEX + INT (Rogue).
      skills: 'Expertise: Sleight of Hand + Stealth (Rogue 1). Only Rogue 3 → no second Expertise pair and no Reliable Talent.'
      # (kept terse; detail on hover / in pickpocket)
    starting_cantrips: 'High Elf racial cantrip — take Minor Illusion: it has no attack roll or save, so Asterion''s INT does not matter, and it can pull sightlines before sneaking.'
    starting_spells: None — Ki/martial build.
    notes: '2 feats (Monk 4 + Monk 8). Rogue 1 FIRST for Expertise, then Monk 1–9, then Thief. Daily Giant Strength elixir; keeps DEX for pickpocketing.'
  spells:
    note: 'Asterion is not a caster. His build-defining Ki abilities and martial features appear at their unlock levels in the Leveling guide; this panel tracks his one High Elf racial cantrip.'
    mandatory:
    - spell: Flurry of Blows (+ Open Hand variants)
      level: Feature (Monk 1; Open Hand variants Monk 3)
      school: Ki — Bludgeoning + rider
      save: 'Topple: DEX · Push: STR · Stagger: none (weapon-action DC)'
      when: char 2 (Monk 1) / char 4 (Monk 3)
      why: 'Bonus action + 1 Ki → two unarmed strikes. Open Hand adds Topple (knock Prone → allies attack it at advantage), Stagger (no Reactions), Push (5m + fall damage). With Fast Hands / Wholeness of Body you Flurry TWICE per turn.'
    - spell: Stunning Strike
      level: Feature (Monk 5)
      school: Ki — control
      save: CON save (DC 8 + prof + higher of DEX/STR)
      when: char 6 (Monk 5)
      why: 'The party contribution: 1 Ki on a hit → CON save or Stunned (auto-fail STR/DEX saves, attacks vs it have advantage, it loses its turn). Locks bosses and hands Charles free crits. The DC rides the Giant elixir''s STR (up to +8).'
    - spell: Manifestation of Mind
      level: Feature (Open Hand, Monk 6)
      school: Toggle — Psychic
      save: None
      when: char 7 (Monk 6)
      why: 'Every unarmed strike deals +1d4 + WIS PSYCHIC. With 4–6 hits a turn, ALL of it is doubled by the Resonance Stone — this is how the monk plugs into the party''s psychic engine without a Shadow Blade. (Toggle to Soul/Body for radiant/necrotic vs psychic-resistant foes.)'
    - spell: Extra Attack
      level: Feature (Monk 5)
      school: N/A
      save: None
      when: char 6 (Monk 5)
      why: 'With both melee hands empty, the Action supplies two unarmed strikes; the Martial-Arts bonus strike and Flurry stack on top.'
    - spell: 'Tavern Brawler + Giant Strength elixir'
      level: Feat (Monk 4) + consumable
      school: N/A
      save: None
      when: char 5
      why: 'Daily Elixir of Giant Strength; TB adds that STR mod to every unarmed attack AND damage a second time, and (STR > DEX) drives attack rolls + Stun DC. The accuracy/damage backbone.'
    recommended:
    - spell: Minor Illusion
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: char 1 (High Elf racial cantrip)
      why: Pulls nearby creatures toward a distraction before combat, helping Asterion redirect sightlines for stealth and theft without relying on his low INT.
    - spell: Ki Resonation (Punch → Blast)
      level: Feature (Open Hand, Monk 9)
      school: Ki — detonate
      save: CON save
      when: char 10 (Monk 9)
      why: 'Punch to mark a target Resonating, then Blast to detonate an AoE around it (excludes party + summons) — a nova finisher on clustered packs.'
    - spell: Step of the Wind
      level: Feature (Monk 2)
      school: Ki — mobility
      save: None
      when: char 3 (Monk 2)
      why: 'Bonus-action Dash/Disengage (jumping is free) — dive the backline, reposition, escape melee without opportunity attacks. Covers the mobility the old Cunning-Action loop gave.'
    - spell: Patient Defense
      level: Feature (Monk 2)
      school: Ki — defense
      save: None
      when: char 3 (Monk 2)
      why: 'Bonus action + Ki → attackers have Disadvantage and you have advantage on DEX saves. The survival button for a no-armour body.'
    - spell: Deflect Missiles
      level: Feature (Monk 3)
      school: Reaction
      save: None
      when: char 4 (Monk 3)
      why: 'Reduce a ranged attack by 1d10 + DEX + monk level (often to 0) and optionally hurl it back — a hard counter to the archers that used to punish a squishy melee assassin.'
    - spell: Wholeness of Body
      level: Feature (Open Hand, Monk 6)
      school: Ki — heal + economy
      save: None
      when: char 7 (Monk 6)
      why: 'Action: heal 3×monk level, refund half your Ki, and gain an EXTRA bonus action for 3 turns (→ two Flurries/turn even before the Thief dip). Once per long rest.'
    - spell: Fast Hands (Thief)
      level: Feature (Thief, Rogue 3)
      school: N/A
      save: None
      when: char 12 (Thief 3)
      why: 'A permanent second bonus action → Flurry of Blows TWICE per turn (2 Ki, 4 extra strikes) on top of the Attack action; also fuels Cunning Action utility.'
    - spell: Vampire Bite
      level: Racial (Vampire Spawn)
      school: Bonus action — Necrotic + heal
      save: None
      when: char 1
      why: 'Astarion''s bite: a free bonus-action heal/buff on a grappled or downed foe (mostly out of combat) — minor in the flurry economy, but costs nothing.'
  leveling:
  - char_level: 1
    class: Rogue 1
    gains:
    - Sneak Attack 1d6
    - Expertise selections ×2
    - DEX + INT saving-throw proficiency
    - Vampire Bite (Astarion origin action)
    recommendations:
    - category: Expertise
      recommendation:
      - Sleight of Hand
      - Stealth
      note: These are the reason Rogue must be the first class; they power stealing and scouting for the entire run.
    - category: Racial cantrip
      recommendation: Minor Illusion
      note: Utility without an attack roll or saving throw, so the low INT score is irrelevant.
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
      note: Adds Topple, Stagger, and Push variants to Flurry of Blows.
  - char_level: 5
    class: Monk 4
    gains:
    - Slow Fall
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Tavern Brawler
      note: Adds the Giant-Strength modifier to unarmed attack and damage rolls a second time; this is the build's accuracy and damage engine.
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
      note: +5 Initiative and immunity to Surprise let Asterion disable a priority target before it acts. A +2 WIS ASI is the defensive alternative.
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
      note: Fast Hands enables two Flurries per turn and is the entire reason for the three-level Rogue tail.
  itemization:
    act1:
    - id: corellon-s-grace
      item: Corellon's Grace (levels 2–4 only)
      slot: weapons
      note: 'EARLY ONLY from Auntie Ethel in the Emerald Grove. Before Tavern Brawler, its staff attack is a solid main Action while Natural Pugilist improves bonus-action and Flurry punches, and being unarmoured grants +2 saving throws. UNEQUIP it at character level 5: ordinary Attack/Extra Attack commands otherwise swing the staff and lose Tavern Brawler, even though Flurry and special unarmed commands remain available.'
    - id: dual-hand-crossbows-plus-one
      item: Dual Hand Crossbows +1
      slot: ranged weapons
      note: 'SELECTED ranged-slot fallback from Act-1 weapon traders. Rogue proficiency supports a main-hand shot plus an off-hand bonus-action shot when Asterion cannot reach melee; these occupy only the ranged set, so his melee hands remain empty for Tavern Brawler.'
    - id: graceful-cloth
      item: Graceful Cloth
      wiki: The Graceful Cloth
      slot: armour
      note: 'Graceful Cloth (Lady Esther, Rosymorn trail). Cat''s Grace = advantage on DEX checks (stealing) + DEX toward 20; it''s Clothing, so it doesn''t break Unarmoured Defence and stays on all game.'
    - id: bracers-of-defence
      item: Bracers of Defence
      slot: hands
      note: 'DEFAULT DEFENCE. Bracers of Defence (Blighted Village cellar) grant +2 AC while unarmoured and shieldless. Keep them for dangerous fights, but swap to the offensive gloves below when faster kills are safer than 2 AC.'
    - id: the-sparkle-hands
      item: The Sparkle Hands (offensive alternative)
      slot: hands
      note: 'EARLY OFFENCE. The Sparkle Hands (Decrepit Sanctuary, Sunlit Wetlands) grant 2 Lightning Charges per unarmed hit. Charges add attack/damage, periodically burst for 1d8 Lightning, and grant advantage against metal-armoured enemies and constructs.'
    - id: gloves-of-cinder-and-sizzle
      item: Gloves of Cinder and Sizzle (offensive alternative)
      slot: hands
      note: 'LATE-ACT-1 OFFENCE. Lady Esther sells these on the Rosymorn trail. Every unarmed hit gains +1d4 Fire, so a Flurry turn applies the rider repeatedly; they also cast a level-3 Scorching Ray once per long rest. Prefer Sparkle Hands against metal targets or fire-resistant enemies.'
    - id: gloves-of-thievery
      item: Gloves of Thievery
      slot: hands
      note: 'Gloves of Thievery (Brem, Zhentarim) — pickpocket backup; keep in the bag once Bracers of Defence take the gloves slot (Graceful Cloth already covers stealing advantage).'
    - id: elixir-of-giant-strength
      item: Elixir of Giant Strength (daily)
      wiki: Elixir of Hill Giant Strength
      slot: consumables
      note: 'Hill Giant (STR 21) early → Cloud Giant (STR 27) later. Powers Tavern Brawler damage AND — since STR > DEX — his attack rolls and Stunning-Strike DC. Occupies the one-elixir-per-rest slot.'
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      wiki: The Deathstalker Mantle
      slot: cloaks
      note: 'Deathstalker Mantle (Dark Urge reward; Charles hands it over). Invisible for 2 turns on a kill — reposition and re-engage; perfect for a diving monk.'
    - id: disintegrating-night-walkers
      item: Disintegrating Night Walkers
      slot: feet
      note: 'Disintegrating Night Walkers (Nere, Grymforge). Free Misty Step once per short rest plus immunity to difficult terrain from surfaces, Enwebbed, and Entangled — the permanent combat boots over Boots of Speed.'
    - id: ring-of-protection
      item: Ring of Protection
      slot: rings
      note: 'Ring of Protection (Mol reward for Steal the Sacred Idol after resolving the Grove). +1 AC and all saving throws; Asterion gets it because he is the exposed unarmoured melee character.'
    - id: crusher-s-ring
      item: Crusher's Ring
      slot: rings
      note: 'DEFAULT second combat ring. Take it from Crusher at the Goblin Camp for +3m movement speed; it stacks with Longstrider and helps Asterion reach the priority target without spending a bonus action.'
    - id: sentient-amulet
      item: Sentient Amulet
      slot: amulets
      note: 'Sentient Amulet (Grymforge, Adamantine chest). Ki Restoration (restore 2 Ki, 1/long rest) + Shatter — a cheap early neck that refuels Flurries. (Mind the WIS-save Hysterical side effect on the rare version.)'
    - id: armour-of-uninhibited-kushigo
      item: Armour of Uninhibited Kushigo (defensive alternative)
      slot: armour
      note: 'ACT 1 — Grymforge reward for returning Sergeant Thrinn''s boots. While Patient Defence is active, Kushigo Counter allows a reaction unarmed strike against an attacker that misses. Graceful Cloth remains the selected default; use Kushigo only for a Patient-Defence counter fight.'
    - id: haste-helm-late-act1
      item: Haste Helm (situational loan)
      slot: head
      note: 'Charles normally keeps this because his Ring supplies Arcane Synergy without occupying the head slot. Asterion can borrow it when Charles does not need the approach speed, but Monk movement makes the loan optional.'
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
      note: 'Eversight Ring (House of Healing morgue) prevents Blindness. Equip it when Asterion must fight beside Charles inside magical Darkness; keep Ring of Protection in ordinary encounters.'
    act3:
    - id: gloves-of-soul-catching
      item: Gloves of Soul Catching
      slot: hands
      note: 'Gloves of Soul Catching (House of Hope — Hope''s reward). +1d10 Force per unarmed hit, +2 CON, and once/turn heal 10 HP OR +5 to an attack/save. Best-in-slot monk gloves; replaces Bracers.'
    - id: mask-of-soul-perception
      item: Mask of Soul Perception
      slot: head
      note: 'Mask of Soul Perception (Devil''s Fee — locked chest in Helsik''s room, DC 20). +2 to Attack rolls, Initiative, and Perception; Detect Thoughts. Headgear.'
    - id: boots-of-uninhibited-kushigo
      item: Boots of Uninhibited Kushigo
      slot: feet
      note: 'Boots of Uninhibited Kushigo (Astral Plane — Prelate Lir''i''c, at the start of Act 3). Adds your WIS modifier to every unarmed strike — flat damage on every hit.'
  playstyle: |-
    - **Prep:** drink Giant Strength, enable Manifestation of Mind, and carry the Resonance Stone from Act 2 onward.
    - **Turn:** Stunning Strike the priority target, then Flurry: Topple (or Stagger against casters). Thief 3 adds a second Flurry.
    - **If Stun fails:** use raw Flurries + Topple; switch Manifestation to Soul against psychic resistance.
  pickpocket:
    note: |-
      Still the party thief, but WITHOUT Rogue 11 Reliable Talent — steals are no longer floor-guaranteed. Expertise (Rogue 1) + advantage (Graceful Cloth) still clear nearly every Act 1–2 lift; save-scum the rare high-DC item.

      For a must-have high-DC item: quicksave-scum, Enthrall the vendor (ally-cast), or hand the lift to another member. Escape/laundering is unchanged from any thief — turn-based mode to freeze timers, break line of sight, split stolen loot to a clean member, wait out the investigation.
    success_math: 'At char 12: DEX 20 (+5) + proficiency +4 doubled by Expertise (+8) = +13 flat, rolled with advantage from the Graceful Cloth. No Reliable-Talent floor, so a low roll CAN fail — but advantage makes it rare, and most targets sit well under the number. Guidance / Bardic Inspiration do NOT apply to the background pickpocket roll; only flat Sleight-of-Hand gear lowers it.'
    gear:
    - item: The Graceful Cloth
      effect: 'Cat''s Grace — advantage on DEX checks (stealing) + DEX toward 20; it''s Clothing, so Unarmoured Defence still works. Worn all game.'
      where: Lady Esther, Rosymorn Monastery Trail (Act 1)
    - item: Gloves of Thievery
      effect: Advantage on Sleight of Hand — a backup once the Cloth takes the gloves slot.
      where: Brem, Zhentarim Basement (Act 1)
    - item: Smuggler's Ring (+2) / Gloves of Power (+1)
      wiki:
      - Smuggler's Ring
      - Gloves of Power
      effect: Flat +Sleight of Hand — the only lever that beats an over-floor target; swap in for that one lift.
      where: Various vendors / loot
  traps:
  - 'From character level 5 onward, stay UNARMOURED, SHIELDLESS, and EMPTY-HANDED. A monk weapon does not disable Martial Arts, Flurry, or special unarmed commands, but ordinary main-action attacks swing the weapon and therefore lose Tavern Brawler and unarmed riders.'
  - 'The Giant Strength elixir is load-bearing (attack, damage, Stun DC) and occupies the one-elixir-per-long-rest slot — no Bloodlust/Battlemage elixir at the same time. Bank a stack.'
  - 'Stunning Strike is a CON save: bosses with high CON, legendary resistance, or undead may shrug it — do not build the whole turn around it landing.'
  - 'No Reliable Talent (only Rogue 3) — pickpocketing is no longer guaranteed on high-DC items; save-scum or use flat +SoH gear.'
  - 'Resonance Stone debuffs the party''s mental saves and makes HIM psychic-vulnerable (no Gnome Cunning) — cluster it in Charles''s Aura of Protection or leave it holstered vs psychic enemies.'
  - 'Only 2 feats (Monk 4 + Monk 8). If that stings, use the Monk 8 / Thief 4 variant for a 3rd feat (loses Ki Resonation).'
  illithid:
    note: 'Alert makes him the party''s first-turn Black Hole carrier: the pull has no save, and targets inside the Resonance Stone aura roll its secondary Slow save with disadvantage against his WIS-based DC 17. After spending the Action on Black Hole he still has two Flurries; when grouping is unnecessary, pre-cast Psionic Overload and keep the Action for two more attacks. Cull the Weak handles mob cleanup; toggle it off when a kill must trigger Deathstalker invisibility. Bonbon keeps the save-dependent Mind Blast. Do NOT give Asterion Awakened because his bonus actions are Flurries/Step.'
---
