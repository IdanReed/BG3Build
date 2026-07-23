---
nickname: Asterion
builds:
- name: The Fist in the Dark
  is_primary: true
  role: Mobile Open-Hand monk — stun-lock striker, psychic flurry, party thief
  class: Open Hand Monk 9 / Thief Rogue 3
  build_order: Rogue 1 (creation, Expertise) → Monk 1–9 → Rogue 2 → Thief 3. No further respec after the initial rebuild.
  race: Astarion (High Elf / Vampire Spawn)
  race_notes: 'Fey Ancestry (advantage vs Charm, no magical Sleep), Darkvision, one High Elf wizard cantrip, bonus-action Vampire Bite. He must fight UNARMOURED and UNARMED — armour, a shield, or a non-monk weapon disables Martial Arts / Unarmoured Defence / Flurry. His Graceful Cloth is Clothing (not armour) and Bracers of Defence work only while unarmoured, so both still fit.'
  background: Charlatan (Deception + Sleight of Hand) — Astarion's fixed origin background (can't be changed, even via respec).
  starting_stats:
    STR: 8
    DEX: 17
    CON: 14
    INT: 10
    WIS: 16
    CHA: 8
  stats_note: 'DEX is everything — unarmed attack, Unarmoured AC (10 + DEX + WIS), Stunning-Strike DC, and pickpocket. WIS adds AC + Manifestation/Kushigo rider damage. STR stays 8 and is supplied by a daily Giant Strength elixir (see feats). High Elf +2 DEX / +1 WIS already applied.'
  ability_targets: 'DEX 17 → 18 (Hag''s Hair) → 20 (Graceful Cloth''s +2, worn all game) — Mirror NOT needed on DEX. Redirect the Mirror of Loss to WIS: 16 → 18. STR stays 8 (the elixir overrides it).'
  feats:
  - at: Monk 4 (char 5)
    feat: Tavern Brawler
    note: 'The engine: adds your STR modifier to unarmed attack rolls AND damage a second time. Drink an Elixir of Giant Strength each long rest — once STR > DEX it ALSO drives your attack rolls and Stunning-Strike DC (BG3 monk DCs use the higher of DEX/STR). Cloud Giant (STR 27, +8) is the ceiling.'
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
  combat_style: Unarmed (fists) only, unarmoured, on a daily Giant Strength elixir — never a weapon or armour.
  creation:
    level1_class: Rogue 1 (taken at character creation / first class in the respec)
    level1_gains: 'Expertise in 2 skills (Sleight of Hand + Stealth) + Sneak Attack 1d6 (vestigial once he punches — Sneak Attack needs a finesse weapon, not fists). MUST be the creation class so Expertise lands on the thief skills.'
    subclass_choice: 'Way of the Open Hand is chosen at Monk 3; Thief at Rogue 3. Rogue 1 has no subclass.'
    proficiencies:
      armor_weapons: 'Rogue: Light armour; Simple weapons, Hand Crossbows, Longswords, Rapiers, Shortswords. Monk adds Simple + Shortsword proficiency and the unarmed/Martial-Arts kit — but you fight UNARMED and UNARMOURED (a weapon or armour disables Martial Arts / Flurry / Unarmoured Defence).'
      saving_throws: 'Dexterity + Intelligence (Rogue, the creation class). Monk grants no extra save proficiency (multiclassing never does) — but DEX saves + Evasion (Monk 7) cover the ones that matter.'
      skills: 'Rogue picks 4 skills + Expertise in 2 (Sleight of Hand + Stealth) at level 1; Charlatan background adds Deception + Sleight of Hand. NOTE: this split reaches only Rogue 3 — so ONE Expertise pair (no Rogue-6 second pair) and NO Reliable Talent (Rogue 11). See pickpocket.'
    starting_cantrips: 'None from class. High Elf picks one wizard cantrip at creation — take a utility one (Friends / Light / Blade Ward); it barely matters for a puncher.'
    starting_spells: None — this is a Ki/martial build, not a caster.
    notes: 'Astarion (companion) — respec at Withers. Take Rogue 1 FIRST for Expertise, then pour into Monk (the combat identity), and finish the Thief dip for the second bonus action. 2 feats total (Monk 4 + Monk 8). Fights unarmed + unarmoured with a daily Giant Strength elixir; keeps DEX for pickpocketing.'
  spells:
    note: 'Not a caster — these are the Ki abilities and features that define the turn. Mandatory = the core loop; Recommended = the situational toolkit.'
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
      why: 'Action = two unarmed strikes; the Martial-Arts bonus strike and Flurry stack on top.'
    - spell: 'Tavern Brawler + Giant Strength elixir'
      level: Feat (Monk 4) + consumable
      school: N/A
      save: None
      when: char 5
      why: 'Daily Elixir of Giant Strength; TB adds that STR mod to every unarmed attack AND damage a second time, and (STR > DEX) drives attack rolls + Stun DC. The accuracy/damage backbone.'
    recommended:
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
    respecs:
    - label: As recruited
      note: Astarion joins as a level-1 Rogue (Assassin path). Do NOT level him as-is — respec at Withers into this build as soon as you can afford it (~100g).
      rows:
      - char_level: 1
        class: Rogue 1 (Assassin — as recruited)
        gains: Recruited state only; a placeholder until the Withers respec.
    - label: Respec → Open Hand Monk / Thief
      note: 'Rebuild from level 1. Take Rogue 1 FIRST (Expertise: Sleight of Hand + Stealth), then Monk 1–9 for the combat identity, then Rogue 2 → Thief 3 for the second bonus action. Feats at Monk 4 (Tavern Brawler) + Monk 8 (Alert).'
      rows:
      - char_level: 1
        class: Rogue 1
        gains: 'Expertise (Sleight of Hand + Stealth); Sneak Attack 1d6 (vestigial once unarmed); DEX + INT saves'
      - char_level: 2
        class: Monk 1
        gains: Unarmoured Defence (AC 10 + DEX + WIS); Martial Arts (DEX unarmed, Deft Strikes 1d4, bonus Unarmed Strike); Flurry of Blows; Ki 2
      - char_level: 3
        class: Monk 2
        gains: Unarmoured Movement (+3m); Patient Defense; Step of the Wind (Dash/Disengage)
      - char_level: 4
        class: Monk 3
        gains: 'Way of the Open Hand (Flurry: Topple/Stagger/Push); Deflect Missiles; Martial Arts die → 1d6'
      - char_level: 5
        class: Monk 4
        gains: 'Feat: Tavern Brawler; Slow Fall'
      - char_level: 6
        class: Monk 5
        gains: Extra Attack; Stunning Strike
      - char_level: 7
        class: Monk 6
        gains: 'Manifestation (Mind/Body/Soul) + Wholeness of Body; Ki-Empowered Strikes (unarmed count as magical); Improved Unarmoured Movement'
      - char_level: 8
        class: Monk 7
        gains: Evasion; Stillness of Mind
      - char_level: 9
        class: Monk 8
        gains: 'Feat: Alert'
      - char_level: 10
        class: Monk 9
        gains: 'Ki Resonation (Punch → Blast); Advanced Unarmoured Movement; Martial Arts die → 1d8; Ki 10'
      - char_level: 11
        class: Rogue 2
        gains: Cunning Action (Dash / Disengage / Hide as a bonus action)
      - char_level: 12
        class: Rogue 3 (Thief)
        gains: Fast Hands (2nd bonus action → double Flurry); Second-Story Work; Supreme Sneak (Invisibility, 1/short rest)
    variant:
      label: '3-feat variant — Monk 8 / Thief 4'
      note: 'Drop Monk 9 → Rogue 4 instead (Monk 8 / Thief 4). Trades Ki Resonation + the 1d8 Martial-Arts die + a Ki point for a THIRD feat (take +2 WIS, or Alert/ASI) and slightly deeper Rogue. Take it if you value the extra feat over the Monk-9 nova.'
  itemization:
    act1:
    - id: graceful-cloth
      item: Graceful Cloth
      note: 'Graceful Cloth (Lady Esther, Rosymorn trail). Cat''s Grace = advantage on DEX checks (stealing) + DEX toward 20; it''s Clothing, so it doesn''t break Unarmoured Defence and stays on all game.'
    - id: bracers-of-defence
      item: Bracers of Defence
      note: 'Bracers of Defence (Blighted Village cellar). +2 AC while unarmoured — takes the gloves slot until the Act-3 Gloves of Soul Catching.'
    - id: gloves-of-thievery
      item: Gloves of Thievery
      note: 'Gloves of Thievery (Brem, Zhentarim) — pickpocket backup; keep in the bag once Bracers of Defence take the gloves slot (Graceful Cloth already covers stealing advantage).'
    - id: elixir-of-giant-strength
      item: Elixir of Giant Strength (daily)
      note: 'Hill Giant (STR 21) early → Cloud Giant (STR 27) later. Powers Tavern Brawler damage AND — since STR > DEX — his attack rolls and Stunning-Strike DC. Occupies the one-elixir-per-rest slot.'
    - id: deathstalker-mantle
      item: Deathstalker Mantle
      note: 'Deathstalker Mantle (Dark Urge reward; Charles hands it over). Invisible for 2 turns on a kill — reposition and re-engage; perfect for a diving monk.'
    - id: sentient-amulet
      item: Sentient Amulet
      note: 'Sentient Amulet (Grymforge, Adamantine chest). Ki Restoration (restore 2 Ki, 1/long rest) + Shatter — a cheap early neck that refuels Flurries. (Mind the WIS-save Hysterical side effect on the rare version.)'
    act2:
    - id: resonance-stone
      item: Resonance Stone (carries it)
      note: 'Resonance Stone (Mind Flayer Colony, late Act 2). He places/carries it — Manifestation of Mind psychic + Psionic Overload across 4–6 hits/turn are all doubled. ⚠ Its aura also makes the party (and him — no Gnome Cunning) psychic-vulnerable + disadvantaged on mental saves; keep it inside Charles''s Aura of Protection, or skip it vs psychic/mind enemies.'
    - id: keep-bracers-cloth
      item: Keep Bracers of Defence + Graceful Cloth
      note: 'No armour swaps — Bracers (AC) + Graceful Cloth (pickpocket) carry Act 2. Armour of Uninhibited Kushigo (Grymforge, Act 1) is a chest alternative (Kushigo Counter on Patient Defense) if you drop the stealing advantage that fight.'
    - id: hat-of-kushigo-skip
      item: 'Hat of Uninhibited Kushigo — SKIP'
      note: 'Sold at Last Light (Talli) but its bonus is +1 spell save DC on unarmed hits — useless for a monk with no spell saves. Not for this build.'
    act3:
    - id: gloves-of-soul-catching
      item: Gloves of Soul Catching
      note: 'Gloves of Soul Catching (House of Hope — Hope''s reward). +1d10 Force per unarmed hit, +2 CON, and once/turn heal 10 HP OR +5 to an attack/save. Best-in-slot monk gloves; replaces Bracers.'
    - id: mask-of-soul-perception
      item: Mask of Soul Perception
      note: 'Mask of Soul Perception (Devil''s Fee — locked chest in Helsik''s room, DC 20). +2 to Attack rolls, Initiative, and Perception; Detect Thoughts. Headgear.'
    - id: boots-of-uninhibited-kushigo
      item: Boots of Uninhibited Kushigo
      note: 'Boots of Uninhibited Kushigo (Astral Plane — Prelate Lir''i''c, at the start of Act 3). Adds your WIS modifier to every unarmed strike — flat damage on every hit.'
    - id: ring-of-protection-flex
      item: Ring of Protection + flex ring
      note: 'Ring of Protection (+1 AC/saves) plus a flex (Crusher''s Ring for +move, or a flat +SoH ring for a rare hard pickpocket). Amulet: keep the Sentient Amulet for Ki, or a defensive neck.'
  playstyle: |-
    - **Pre-fight:** drink an Elixir of Giant Strength (STR → TB damage + attack + Stun DC); toggle Manifestation of Mind (psychic) on; position near the Resonance Stone (Act 2+). Alert usually means you act first.
    - **Open on the priority target:** Step of the Wind (bonus) or just move in → Extra Attack (2 unarmed) + Martial-Arts bonus strike, and **Stunning Strike** the first hit on the boss (CON save vs your STR-based DC) → Stunned sets up Charles's auto-crits. Bonus action = Flurry of Blows (Topple to knock Prone, or Stagger vs a caster).
    - **Once Thief 3 / Wholeness of Body is online:** a SECOND Flurry per turn — 6+ unarmed hits, each carrying Soul Fist (1d10 force) + Manifestation (1d4 + WIS psychic, doubled by the Stone) + Boots of Kushigo (+WIS) + Psionic Overload (doubled). That flurry of doubled psychic is a bigger Stone payoff than the old single Shadow-Blade strike.
    - **Mobility/defense:** dive backline casters, Deflect Missiles vs archers, Patient Defense when focused, Deathstalker invisibility on a kill to reposition. Ki Resonation → Blast to finish a cluster.
    - **Vs undead / stun-immune / legendary-resistant bosses:** Stunning Strike may bounce — lean on raw Flurry + Topple (Prone → advantage) and switch Manifestation to Soul (radiant) if they resist psychic.
    - **Out of combat:** the party thief — see pickpocket.
  pickpocket:
    note: 'Still the party thief, but WITHOUT Rogue 11 Reliable Talent — steals are no longer floor-guaranteed. Expertise (Rogue 1) + advantage (Graceful Cloth) still clear nearly every Act 1–2 lift; save-scum the rare high-DC item.'
    math: 'At char 12: DEX 20 (+5) + proficiency +4 doubled by Expertise (+8) = +13 flat, rolled with advantage from the Graceful Cloth. No Reliable-Talent floor, so a low roll CAN fail — but advantage makes that rare, and most targets sit well under the number. Guidance / Bardic Inspiration do NOT apply to the background pickpocket roll; only flat Sleight-of-Hand gear lowers it.'
    gear: 'Graceful Cloth (all game — advantage + DEX toward 20, and it''s clothing so Unarmoured Defence still works); Gloves of Thievery as a backup advantage source; a flat +SoH ring (Smuggler''s Ring +2 / Gloves of Power +1) swapped in for a rare over-floor target.'
    fallback: 'For a must-have high-DC item: quicksave-scum, Enthrall the vendor (ally-cast), or hand the lift to another member. Escape/laundering is unchanged from any thief — turn-based mode to freeze timers, break line of sight, split stolen loot to a clean member, wait out the investigation.'
  traps:
  - 'Must stay UNARMED + UNARMOURED: a weapon (even a monk shortsword) or any armour/shield disables Martial Arts, Flurry, and Unarmoured Defence — and a weapon loses Tavern Brawler + all the unarmed riders (Soul Fist, Manifestation, Boots of Kushigo).'
  - 'The Giant Strength elixir is load-bearing (attack, damage, Stun DC) and occupies the one-elixir-per-long-rest slot — no Bloodlust/Battlemage elixir at the same time. Bank a stack.'
  - 'Stunning Strike is a CON save: bosses with high CON, legendary resistance, or undead may shrug it — do not build the whole turn around it landing.'
  - 'No Reliable Talent (only Rogue 3) — pickpocketing is no longer guaranteed on high-DC items; save-scum or use flat +SoH gear.'
  - 'Resonance Stone debuffs the party''s mental saves and makes HIM psychic-vulnerable (no Gnome Cunning) — cluster it in Charles''s Aura of Protection or leave it holstered vs psychic enemies.'
  - 'Only 2 feats (Monk 4 + Monk 8). If that stings, use the Monk 8 / Thief 4 variant for a 3rd feat (loses Ki Resonation).'
  illithid:
    note: 'His illithid save DC is WIS (~16) — his newest countable class is Monk (Thief-Rogue is ignored for spell DC), NOT the dead INT it looks like — and he carries the Resonance Stone, whose aura gives enemies disadvantage on INT saves. So he is the party''s active AoE nuker: Black Hole + Mind Blast (INT-save powers). Psionic Overload is still his STANDOUT damage (+1d4 psychic per hit across a 4–6-hit flurry, doubled by the Stone), with Luck of the Far Realms alongside. Do NOT give him Awakened (bonus action is Flurry/Step). See the tadpole plan.'
  scores:
    fit: 5
    fun: 5
    power: 4
---
