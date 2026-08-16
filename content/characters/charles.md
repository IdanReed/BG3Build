---
nickname: Charles
builds:
- name: The Three Booms
  is_primary: true
  role: Melee crit-smite nova frontline
  class: Oathbreaker Paladin 7 / Hexblade Warlock 5
  race: Half-Orc (Dark Urge origin)
  race_notes: Savage Attacks (extra weapon die on melee crits) · Relentless Endurance · origin character, so Hag's Hair priority.
  background: Haunted One (Medicine, Intimidation) — the fixed Dark Urge background
  starting_stats:
    STR: 8
    DEX: 14
    CON: 16
    INT: 8
    WIS: 10
    CHA: 17
  stats_note: 'Point-buy 8/14/15/8/10/15 = all 27 (CON 15 and CHA 15 cost 9 each). Half-Orc +2 → CHA 17, +1 → CON 16. Fully spent, no leftovers.'
  ability_targets: CHA 17 → 18 (Hag's Hair) → 20 (Mirror of Loss); CON stays 16.
  feats:
  - at: Act 1 char 6 (Paladin 4)
    feat: Great Weapon Master (temporary)
    note: 'Phalar Aluve is Versatile, so its two-handed attacks qualify for All In (−5 attack / +10 damage). Darkness-Arrow advantage offsets the penalty. Replaced at the Resonance Stone respec.'
  - at: Late Act 2 Resonance Stone respec (Warlock 4 feat; usually char 9)
    feat: Dual Wielder
    note: Replaces GWM. Required to hold 3d8 Shadow Blade main hand with Versatile Phalar off-hand; also +1 AC.
  - at: Late Act 2 Resonance Stone respec (Paladin 4 feat; usually char 9)
    feat: Savage Attacker
    note: Rerolls Shadow Blade, Phalar Aluve and Divine Smite damage dice. The off-hand Phalar swing is the seventh attack when the bonus action is free.
  weapon_plan: 'ACT 1–mid ACT 2 — two-handed bound Phalar Aluve + GWM, Darkness Arrows for advantage. LATE ACT 2 — respec at char 9 to Warlock 5 / Paladin 4, GWM → Dual Wielder, 3d8 Shadow Blade main hand + Phalar off-hand inside the Stone aura.'
  creation:
    level1_class: Warlock 1 (Hexblade patron)
    level1_gains: 'Pact Magic (1 × L1 short-rest slot), Hexblade''s Curse (bonus action), Bind Hexed Weapon (attack with CHA). Pact of the Blade waits until Warlock 3.'
    subclass_choice: Hexblade patron (Warlock 1)
    proficiencies:
      armor_weapons: Medium armour, shields and martial weapons (Hexblade). Multiclassing into Paladin does NOT grant heavy armour — use medium, or self-proficient Helldusk Armour.
      saving_throws: WIS + CHA (Warlock).
      skills: 2 Warlock picks + Haunted One (Medicine, Intimidation).
    starting_cantrips: 2 at Warlock 1 — Eldritch Blast + Booming Blade.
    starting_spells: Hex + Armour of Agathys; the Hexblade L1 package adds Shield and Wrathful Smite.
    notes: 'Act 1 stops Warlock at 2 — Hexblade gives CHA weapon binding and Devil''s Sight, then Paladin 1–5 gives Smite at char 4, temporary GWM at 6, Extra Attack at 7. Paladin 6 for Aura of Protection if char 8 lands before the Stone. Use farmed Darkness Arrows instead of learning Darkness. ⚠ Keep the oath intact until the Stone respec so Withers will help; break it afterward and stay Oathbreaker.'
  spells:
    note: A smite platform, not a spell-slinger. Act 1 — free Darkness Arrows let him hold Hex, Bless or Divine Favour while two-handing Phalar. Post-Stone — self-cast Darkness + 3d8 Shadow Blade is the default psychic package.
    mandatory:
    - spell: Divine Smite
      level: Feature (Paladin 2)
      school: Class feature — Radiant
      save: None (melee weapon attack roll)
      when: char 4
      why: 'The build''s core. Expend any slot on a melee hit: 2d8 Radiant at L1, +1d8 per slot level above 1st (cap 5d8 at an L4 slot), +1d8 vs Fiends/Undead; dice DOUBLE on a crit. Not a prepared spell and not stopped by Counterspell — set the Critical-Hit Divine Smite reactions to auto-confirm.'
    - spell: Inquisitor's Might
      level: Channel Oath (Oath of Vengeance, Paladin 1)
      guide_level: 3
      school: Oath action — Radiant
      save: None (the Daze rider has NO saving throw)
      when: char 3
      why: 'THE ACT 1 DAMAGE BUTTON, live from character level 3. Bonus Action + the single Channel Oath charge: for 2 turns the target''s weapon attacks deal an additional +CHA modifier RADIANT damage and can Daze enemies for 1 turn, with no save on the Daze. At CHA 17 that is +3 per weapon hit, rising to +5 at CHA 20. Three things make it better than it looks: (1) the radiant damage triggers Luminous Armour''s Radiating Shockwaves and any radiant-keyed rider, (2) it has a 9m range and can target an ALLY — on Asterion''s 4–6 unarmed hits per turn it is worth far more raw damage than on Charles''s 1–2 swings, so decide per fight who gets it, and (3) the Daze has no saving throw at all. ⚠ Only ONE Channel Oath charge per short rest, and from Paladin 3 it competes with Vow of Enmity.'
    - spell: Shadow Blade
      level: '2'
      guide_level: 9
      school: Illusion
      save: None (bonus action to summon)
      when: Late Act 2 Resonance Stone respec (Warlock 5, usually char 9)
      why: 'POST-STONE core weapon, not an Act-1 pick. Level-3 pact slots start it at 3d8 Psychic, lasting until long rest with no concentration and using CHA once bound. The Stone doubles the Psychic; Devil''s Sight + self-cast Darkness supply advantage and defence.'
    - spell: Wrathful Smite
      level: '1'
      guide_level: 1
      school: Evocation
      save: WIS save (to avoid Frightened)
      when: char 1 (Hexblade) / char 4 (Paladin 2)
      why: 1d6 psychic on one weapon hit, and can Frighten. Coexists with concentration-free Darkness Arrows in Act 1, but competes with self-cast Darkness after the respec.
    recommended:
    - spell: Hex
      level: '1'
      guide_level: 1
      school: Enchantment
      save: None (rider on each hit)
      when: char 1 (Warlock 1)
      why: +1d6 Necrotic per hit plus disadvantage on a chosen ability. Runs inside concentration-free arrow darkness and activates Strange Conduit Ring; competes with self-cast Darkness after the respec.
    - spell: Shield
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None (reaction, +5 AC)
      when: char 1 (Hexblade L1 expanded)
      why: Reaction +5 AC to dodge an incoming hit; no concentration — a strong survival pick for a melee body.
    - spell: Armour of Agathys
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None
      when: char 1–6
      why: Temp HP + Cold retaliation scaling with the pact slot — 15 temp HP / 15 Cold from a Warlock-5 L3 slot. No concentration.
    - spell: Bless
      level: '1'
      guide_level: 4
      school: Enchantment
      save: None (concentration)
      when: char 4 (Paladin 2)
      why: '+1d4 to attack rolls and saves for up to 3 allies — 4 if upcast to a level 2 slot, which covers the whole party. Rated S-tier and the Paladin''s default early concentration. Offsets Great Weapon Master and runs inside concentration-free arrow darkness. THE ROUTINE: from the Underdark onward, cast it while holding the STAFF OF ARCANE BLESSING, so every target also gets Mystra''s Blessing (+1d4 to spell attack rolls) — that is +1d4 accuracy on each of Gale''s 3–7 Scorching Ray rays. Then swap back to Phalar. ⚠ Charles remains the party''s ONLY Bless caster: the Whispering Promise applies the same condition and therefore does NOT stack with this, and is not enhanced by the staff. The ring covers char 1–3 and any fight where Charles concentrates on Hex or Darkness instead.'
    - spell: Aid
      level: '2'
      guide_level: 7
      school: Abjuration
      save: None
      when: char 7 (Paladin 5), and again from char 10 post-respec
      why: 'FREE PARTY DURABILITY, and the party''s only source — Aid is Cleric or Paladin only, and this party has no Cleric. Self-centred 9m radius, +5 maximum HP per party member (+5 more per slot level above 2nd), lasting UNTIL LONG REST with NO Concentration. Downed allies also come back with an extra hit point. One level 2 slot per long rest for a permanent +5 to +15 across four characters is close to free on a party with a single healer. ⚠ Cast it AFTER summoning anything you want covered. Aid stacks with one source of temporary HP, but temp-HP sources never stack with each other — so run Armour of Agathys OR the illithid Shield of Thralls, not both.'
    - spell: Divine Favour
      level: '1'
      guide_level: 4
      school: Evocation
      save: None (concentration)
      when: char 4 (Paladin 2)
      why: +1d4 Radiant on every Phalar hit for 3 turns — the Act-1 personal-damage option when Bless is covered elsewhere.
    - spell: Command
      level: '1'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: char 4 (Paladin 2)
      why: 'Rated the #3 spell in the game — cheap control (Drop / Halt / Approach) to open a nova or peel an enemy caster, and it uses NO Concentration, so it coexists with Bless. ⚠ RUN IT AS A MASS DISABLE, not just single-target: Command gains an extra target per slot level above 1st, so a level 3 or 4 Paladin slot disables a whole cluster for the turn Charles needs to close. That is often worth more than converting the same slot into one Divine Smite. ⚠ Does not work on Undead.'
    - spell: Hellish Rebuke
      level: '1'
      guide_level: 2
      school: Evocation
      save: DEX save (half on save)
      when: char 2 (Warlock pick) / post-respec Oathbreaker oath spell
      why: Reaction fire damage when hit. Replaceable during the Warlock progression, then returns free as an always-prepared Oathbreaker spell.
    - spell: Darkness
      level: '2'
      guide_level: 9
      school: Evocation
      save: None (Concentration)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'POST-STONE default concentration. Enemies that cannot see through it are Blinded and attack at disadvantage; Devil''s Sight gives Charles advantage. Powers Strange Conduit, but excludes Hex, Bless, Divine Favour and the smite spells. Act 1 uses arrows.'
    - spell: Misty Step
      level: '2'
      guide_level: 9
      school: Conjuration
      save: None (bonus action)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Bonus-action mobility to reach a priority target, cross hazards or escape a bad melee position.
    - spell: Counterspell
      level: '3'
      guide_level: 9
      school: Abjuration
      save: Reaction
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Pact-slot reaction for enemy spells dangerous enough to justify delaying a Smite or Shadow Blade recast.
    - spell: Spiteful Suffering
      level: Channel Oath (not a spell)
      school: Oathbreaker Channel Oath — Necrotic
      save: CHA save
      when: immediately after the Act 2 respec and oath break (Paladin 3)
      why: 1d4+CHA Necrotic per turn AND all attackers gain Advantage on the target — a self-contained advantage/crit source when Risky Ring is not equipped.
    - spell: Eldritch Blast
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: char 1 (Warlock 1)
      why: Ranged fallback for turns he cannot reach melee (2 beams at char 5, 3 at char 10) — real damage with Agonising Blast + CHA 20.
    - spell: Booming Blade
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Melee weapon attack roll
      when: char 1 (Warlock 1)
      why: The melee cantrip — Phalar in Act 1, Shadow Blade after the respec. Adds Thunder from char 5, once per Action even with Extra Attack, and triggers the Ring of Arcane Synergy for 2 turns.
    - spell: Mage Hand
      level: Cantrip
      guide_level: 9
      school: Conjuration
      save: None
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Third-cantrip exploration and object manipulation with no attack roll or saving throw.
    - spell: Crown of Madness
      level: '2'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: char 10 (Oathbreaker oath spell)
      why: Always-prepared Oathbreaker control that can turn a humanoid on a nearby creature. Situational and competes with Darkness, but costs no Warlock spell pick.
    alternatives:
    - spell: Bone Chill
      level: Cantrip
      school: Necromancy
      save: Ranged spell attack
      when: Warlock cantrip alternative
      why: Ranged anti-healing and advantage against Undead — take it over Mage Hand when that niche beats exploration utility.
    - spell: Minor Illusion
      level: Cantrip
      school: Illusion
      save: None
      when: Warlock cantrip alternative
      why: Pulls nearby creatures toward a distraction before combat, setting up an ambush or isolating a target with no roll or save.
    - spell: Protection from Evil and Good
      level: '1'
      school: Abjuration
      save: None (Concentration)
      when: Warlock spell alternative
      why: Aberrations, Celestials, Elementals, Fey, Fiends and Undead attack the target at Disadvantage and cannot Charm, Frighten or Possess it. Competes with Darkness.
    - spell: Mirror Image
      level: '2'
      school: Illusion
      save: None
      when: Warlock spell alternative
      why: Non-concentration defence — three duplicates give +9 AC, one vanishing per missed attack.
    - spell: Hold Person
      level: '2'
      school: Enchantment
      save: WIS save
      when: Warlock spell alternative
      why: Paralyses a humanoid so melee hits within 3m auto-crit — a self-contained smite setup when Bonbon is not controlling the target. Concentration.
    - spell: Hunger of Hadar
      level: '3'
      school: Conjuration
      save: DEX save (Acid damage)
      when: Warlock 5 alternative
      why: 'Rated S-tier, warlock-exclusive among this party''s classes, and called one of the best layered-control spells in the game. Large difficult-terrain zone that Blinds, deals Cold at the start of enemy turns and Acid at the end. The honest cost is that it takes the Darkness concentration slot, so it is a per-fight choice: Hunger of Hadar when the fight is a crowd, Darkness when Charles needs the Devil''s Sight advantage lane for himself.'
    - spell: Blink
      level: '3'
      school: Transmutation
      save: None
      when: Hexblade expanded spell at Warlock 5
      why: Non-concentration defence — a chance to go Ethereal at the end of each turn, untargetable until his next.
  leveling:
  - char_level: 1
    class: Warlock 1 (Hexblade)
    gains:
    - Pact Magic (one level 1 short-rest slot)
    - Hexblade's Curse
    - Bind Hexed Weapon (attack using CHA)
    - Medium armour, shields, and martial weapons
    recommendations:
    - category: Patron
      recommendation: Hexblade
      note: The CHA weapon package, armour proficiencies and curse that define the build.
    - category: Cantrips
      recommendation:
      - Eldritch Blast
      - Booming Blade
      note: A scaling ranged fallback plus the melee cantrip that later triggers the Ring of Arcane Synergy.
    - category: Spells
      recommendation:
      - Hex
      - Armour of Agathys
      note: Sustained damage when Darkness is unnecessary, and durable non-concentration temp HP.
    - category: Hexblade spells
      recommendation:
      - Shield
      - Wrathful Smite
      note: Free at Warlock 1. Shield is the defensive reaction; Wrathful Smite is situational concentration.
  - char_level: 2
    class: Warlock 2
    gains:
    - Two Eldritch Invocation selections
    - Second Pact Magic slot
    recommendations:
    - category: Invocations
      recommendation:
      - Devil's Sight
      - Agonising Blast
      note: Devil's Sight enables the Darkness plan; Agonising Blast scales the ranged fallback with CHA.
    - category: Spell
      recommendation: Hellish Rebuke
      note: Reaction damage before Warlock progression pauses for the rest of Act 1.
  - char_level: 3
    class: Paladin 1
    gains:
    - Lay on Hands
    - Divine Sense
    - Temporary Paladin oath
    recommendations:
    - category: Oath
      recommendation: Oath of Vengeance
      note: 'This level also grants Channel Oath (1 charge, short-rest recharge) and, with Vengeance, INQUISITOR''S MIGHT at Paladin class level 1. That is a real Act 1 damage button, not a formality — see the Inquisitor''s Might entry under mandatory spells. The oath is broken into Oathbreaker after the Resonance Stone respec, which avoids paying to restore it before Withers will respec Charles. For the whole of Act 1, treat Inquisitor''s Might as an active damage source and spend the charge every fight.'
  - char_level: 4
    class: Paladin 2
    gains:
    - Divine Smite
    - Paladin Spellcasting
    - Fighting Style selection
    recommendations:
    - category: Fighting style
      recommendation: Defence
      note: '⚠ NOT Duelling — it cannot coexist with Great Weapon Master here. Duelling requires "a melee weapon that is not Two-Handed in ONE hand, and no weapon in the other" (a shield is allowed). Great Weapon Master: All In requires "a melee weapon you are Proficient with and are wielding in BOTH hands", and the wiki adds that it applies "when off-hand is empty". The two can never be active on the same attack, so Duelling only makes sense if Charles abandons GWM for a Phalar + shield build — which this plan does not do. Defence''s always-on +1 AC remains the pick. Great Weapon Fighting is the theoretical damage alternative, but BG3 words it as "a Two-Handed melee weapon" and Phalar Aluve is VERSATILE, not Two-Handed, so it may not apply at all — verify in-game before spending the pick on it, and note the gain would only be ~+1.2 per hit on a single 1d10 die.'
    - category: Prepared spells
      recommendation:
      - Bless
      - Divine Favour
      - Command
      note: Arrow darkness is concentration-free, so Bless or Divine Favour stays up inside it; the rest of the slots become Divine Smites.
  - char_level: 5
    class: Paladin 3
    gains:
    - Divine Health
    - Oath of Vengeance subclass actions
    recommendations:
    - category: Subclass path
      recommendation: Keep the oath intact through Act 1 — but now you must CHOOSE a Channel Oath use
      note: 'Paladin 3 adds Vow of Enmity (Bonus Action + Channel Oath charge, 3m, advantage on attack rolls against one enemy for 10 turns). ⚠ It draws on the SAME single short-rest Channel Oath charge as Inquisitor''s Might, so from here each short rest buys one or the other. Rough guide: Vow of Enmity for a long boss fight (10 turns of advantage offsets GWM''s −5 and doubles the crit rate that drives the smite nova — and the wiki notes a self-cast bug that extends the advantage to ALL targets), Inquisitor''s Might for a short fight or when you want the radiant rider and the free Daze. Break the oath only after the planned Act-2 respec.'
  - char_level: 6
    class: Paladin 4
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Great Weapon Master
      note: 'Versatile Phalar Aluve qualifies for All In, but ONLY while wielded in both hands with the OFF-HAND EMPTY — no shield, no off-hand weapon. Devil''s Sight advantage from a Darkness Arrow, Vow of Enmity, and Bless all offset the −5 attack penalty; the +10 damage is the Act-1 spike. GWM is what rules out the Duelling fighting style and any shield variant of this build.'
  - char_level: 7
    class: Paladin 5
    gains:
    - Extra Attack
    - Level 2 Paladin spells
    recommendations:
    - category: Rotation
      recommendation: Booming Blade or Phalar attack → Extra Attack
      note: Two attacks per Action in the two-handed GWM phase; spend Smite reactions on crits and priority hits.
  - char_level: 8
    class: Paladin 6 (pre-Stone continuation)
    gains:
    - Aura of Protection
    recommendations:
    - category: Timing
      recommendation: Keep the Act-1 Phalar/GWM package until the Resonance Stone
      note: The Stone normally arrives late enough that char 8 comes first. Aura of Protection is the best interim Paladin level and helps the party inside the later Stone aura.
  - char_level: 9
    class: RESPEC at the Resonance Stone — Warlock 5 / Paladin 4
    gains:
    - Pact of the Blade and Deepened Pact
    - Level 3 Pact slots and 3d8 Shadow Blade
    - Self-cast Darkness and Counterspell
    - Dual Wielder replaces Great Weapon Master
    - Paladin 2 Divine Smite
    - Paladin 3 oath features
    - Paladin 4 Savage Attacker
    recommendations:
    - category: Warlock feat
      recommendation: Dual Wielder
      note: Required for Shadow Blade main hand + Phalar off-hand; GWM no longer applies and the respec removes it.
    - category: Paladin feat
      recommendation: Savage Attacker
      note: The usual char-9 respec has levels for both feats. If the Stone lands at level 8, take Warlock 5 / Paladin 3 for Dual Wielder and add Paladin 4 / Savage Attacker next level.
    - category: Warlock spells
      recommendation:
      - Shadow Blade
      - Darkness
      - Counterspell
      - Misty Step
      note: Shadow Blade is immediately 3d8 from the level-3 pact slots; Darkness + Devil's Sight replace the Act-1 arrow dependency.
    - category: Subclass path
      recommendation: Break the freshly selected Paladin oath → Oathbreaker
      note: Keeping the Act-1 oath intact makes this free. If he became an Oathbreaker earlier, pay the Oathbreaker Knight to restore the oath before Withers will respec him, then break it again.
  - char_level: 10
    class: Paladin 5
    gains:
    - Extra Attack (stacks with Deepened Pact outside Honour Mode for three attacks)
    - Level 2 Paladin spells
    - Oathbreaker spells Darkness and Crown of Madness
  - char_level: 11
    class: Paladin 6
    gains:
    - Aura of Protection
  - char_level: 12
    class: Paladin 7
    gains:
    - Aura of Hate
  itemization:
    act1:
    - id: early-hexed-weapon
      item: Early pact-bound weapon (temporary)
      wiki: false
      slot: weapons
      note: Before Phalar, bind the best main-hand weapon so it attacks with CHA. Hexblade can bind Two-Handed or Versatile — keep the off-hand empty so Versatile weapons use the larger die and later qualify for GWM.
    - id: phalar-aluve-two-handed
      item: Phalar Aluve (selected two-handed weapon)
      slot: weapons
      note: ACT-1 DEFAULT from the Underdark. Bind as the Hexed Weapon, off-hand empty, so the Versatile longsword uses 1d10 and GWM All In adds +10 from char 6. Pre-cast Shriek and keep it equipped — the 6m aura covers Charles and Asterion.
    - id: staff-of-arcane-blessing
      item: Staff of Arcane Blessing (pre-combat swap)
      slot: weapons
      note: 'Arcane Tower BASEMENT, Underdark — the elevator buttons only appear if someone carries Bernard''s Guiding Light ring. NOT a combat weapon; a buff stick he swaps in before a fight. Every Bless cast by its WIELDER also applies Mystra''s Blessing, +1d4 to spell attack rolls, to each blessed creature. Charles is already spending his concentration on Bless, so the routine costs only the swap: hold staff → upcast Bless to a level 2 slot for all four → swap to Phalar and activate Shriek. Gale is the payoff, gaining +1d4 accuracy on every ray. Rated A on the staves tier list, which calls it "excellent for Scorching Ray." ⚠ Does NOT enhance the Whispering Promise''s version of Bless.'
    - id: arrows-of-darkness
      item: Arrows of Darkness (farm)
      slot: consumables
      note: 'ACT-1 and early-ACT-2 advantage engine. 3m cloud, 3 turns, no Concentration — so Devil''s Sight grants advantage while Charles holds Bless, Divine Favour or Hex. Prefer Bonbon placing it; if Charles fires it, do so before switching to Phalar and activating Shriek. Restock from arrow vendors — the build stops Warlock at 2 until the Stone.'
    - id: dual-hand-crossbows-plus-one
      item: Dual Hand Crossbows +1
      slot: ranged weapons
      note: 'Ranged fallback and Darkness-Arrow launcher. Farm Dammon, Roah, Derryth and Jeera for +1 copies; the ranged set does not interfere with two-handed Phalar. ⚠ Keep expectations low — once he is standing inside his own Darkness the cloud blocks ranged attacks into and out of itself, so the slot is close to dead on any turn he is using the cloud properly.'
    - id: luminous-armour
      item: Luminous Armour
      slot: armour
      note: 'SELECTED chest once Divine Smite arrives at char 4. The Selûnite Outpost medium armour reaches AC 17 with DEX 14, and each Smite''s Radiant damage emits a Radiating Shockwave that penalises nearby enemy attacks. Rated #2 of the 20 best Act 1 items. ⚠ The video assigns it to a Spirit Guardians Cleric, which this party does not have — it earns its place here because Divine Smite, Inquisitor''s Might and Asterion''s Manifestation of Soul are all radiant, so the Shockwave has three separate triggers.'
    - id: boots-of-striding
      item: Boots of Striding
      slot: feet
      note: SELECTED boots, worn by Minthara in the Shattered Sanctum. Concentrating on Bless, Divine Favour or Hex grants Momentum and blocks Prone and forced movement — and Prone is the cheapest way a Paladin loses concentration. The same kill yields Gale's Spidersilk Armour.
    - id: amulet-of-misty-step
      item: Amulet of Misty Step
      slot: amulets
      note: SELECTED neck from Priestess Gut's chambers. Misty Step 1/short rest solves approach and elevation on a melee gish with no other mobility; Asterion already has Monk movement and the Night Walkers.
    - id: haste-helm
      item: Haste Helm
      slot: head
      note: 'SELECTED Act-1 head from the Moss-Covered Chest in the Blighted Village. Three turns of opening Momentum, and the Ring of Arcane Synergy keeps this slot free. Rated #19 of 20. ⚠ He keeps it rather than lending it out: he has the party''s worst initiative at d4+2 and the longest distance to close, whereas Asterion has Unarmoured Movement plus Step of the Wind and takes the Circlet of Psionic Revenge instead.'
    - id: gloves-of-the-growling-underdog
      item: Gloves of the Growling Underdog (early alternative)
      slot: hands
      note: Dror Ragzlin's treasure room. Advantage on melee attacks when 2+ enemies stand within 3m of the target — useful when conserving Darkness Arrows or when the cloud cannot cover the target.
    - id: gloves-of-baneful-striking
      item: Gloves of Baneful Striking (late default)
      slot: hands
      note: SELECTED late-Act-1 gloves from Lady Esther. A weapon hit gives the target −1d4 to saving throws for 2 turns, helping Asterion's Stun and the casters' control. Unlike Growling Underdog, this is not redundant inside Darkness.
    - id: auntie-ethel-s-hair-cha-17-18
      item: Auntie Ethel's Hair → CHA 17 → 18
      wiki: Auntie Ethel's Hair
      slot: consumables
      note: Raises Aura DCs, attack and smite accuracy, and prepared-spell count.
    - id: ring-of-arcane-synergy
      item: Ring of Arcane Synergy
      slot: rings
      note: 'Gish Far''aag, Crèche. Booming Blade damage → Arcane Synergy for 2 turns, adding CHA to subsequent weapon attacks. Pairs with Strange Conduit; Risky Ring replaces it in Act 2. ⚠ Do not also give him Bonbon''s Diadem of Arcane Synergy — it applies the same condition and will not stack with itself.'
    - id: strange-conduit-ring
      item: Strange Conduit Ring
      slot: rings
      note: '+1d4 Psychic on weapon attacks while Concentrating (Crèche), and rated #5 of the 20 best Act 1 items for exactly this kind of multiattacking, concentrating character. Hold Bless, Divine Favour or Hex inside a concentration-free arrow cloud, and self-cast Darkness powers it after the Stone respec while the Resonance Stone doubles the rider. ⚠ Per the wiki it covers melee, ranged and Thrown attacks but NOT Unarmed Strike, which is why it can never move to Asterion.'
    - id: act1-cloak-charles
      item: No cloak exists yet
      slot: cloaks
      note: 'Deliberately empty, and not an oversight. The Deathstalker Mantle is the ONLY magical cloak obtainable in Act 1 and it goes to Asterion, who converts kills into repositioning; every other cloak in the game — Cloak of Protection, Cunning Brume, Fleshmelter, Thunderskin, Vivacious, Derivation, Elemental Absorption — first appears in Act 2, and Displacement, the Weave, Shade-Slayer and Wavemother''s in Act 3. Charles goes bare-shouldered until Quartermaster Talli at Last Light.'
    act2:
    - id: self-cast-shadow-blade-upcast-to-3d8
      item: Self-cast Shadow Blade upcast to 3d8
      wiki: Shadow Blade (weapon)
      slot: weapons
      note: 'POST-RESONANCE DEFAULT. Keep two-handed Phalar/GWM until the late-Act-2 Stone pickup. Warlock 5 brings level-3 pact slots — summon a 3d8 Shadow Blade and bind THIS main hand to CHA so Deepened Pact applies, leaving Phalar unbound off-hand. Usual char-9 split is Warlock 5 / Paladin 4; Warlock 5 / Paladin 3 is the minimum if the Stone lands at level 8.'
    - id: phalar-aluve-offhand
      item: Phalar Aluve (selected off-hand)
      slot: weapons
      note: 'PARTY-DAMAGE DEFAULT after the Stone. Dual Wielder replaces GWM so Phalar sits beside the Light Shadow Blade, +1 AC. Pre-cast Shriek and keep Charles and Asterion inside its 6m aura (the Stone reaches 9m). Shriek fires 1d4 Thunder per qualifying party damage instance and −1d4 to enemy attacks and all saves — worth more than a personal-DPR off-hand. Phalar is unbound and Charles lacks Two-Weapon Fighting, so its bonus-action swing is last priority.'
    - id: render-of-mind-and-body-personal-alternative
      item: Render of Mind and Body (personal-DPR alternative)
      slot: weapons
      note: 'PRE-STONE, from Lann Tarv at Moonrise after convincing Z''rell to help. Light, so it pairs with Shadow Blade without Dual Wielder — a personal-only respec could take Savage Attacker plus a CHA ASI instead. Its advantaged off-hand hit gains +1d8 Psychic, doubled by the Stone, but buffs nothing else. Keep Phalar unless optimising Charles in isolation.'
    - id: knife-of-the-undermountain-king-personal-alternative
      item: Knife of the Undermountain King (personal crit alternative)
      slot: weapons
      note: Act-1 Crèche, and Light enough to pair with Shadow Blade without Dual Wielder. Its global −1 crit threshold and melee-die reroll make it his best crit stat-stick — but Bonbon uses the unique Knife as her melee off-hand stat stick for the same crit-range reason, and taking it costs Phalar Shriek. Not the party default.
    - id: sentinel-shield-defensive-alternative
      item: Sentinel Shield (defensive alternative)
      slot: off-hand
      note: PRE-STONE, from Lann Tarv at Moonrise. Shadow Blade is one-handed, so Charles can drop Phalar for +2 AC, +3 Initiative and advantage on Perception. For a long defensive stretch, respec Dual Wielder into +2 CHA; for one fight, the wasted feat is cheaper than another respec.
    - id: charge-bound-warhammer-physical-fallback
      item: Charge-Bound Warhammer (Psychic-immune fallback)
      slot: weapons
      note: PRE-STONE, from Dammon at Last Light. Against Psychic immunity, bind this main hand instead of Shadow Blade — effectively +2 with 1d6 Lightning, Deepened Pact still applies, Phalar still off-hand for Shriek. Against mere Psychic resistance, test the Stone first (Vulnerability and Resistance normally cancel), then holster it if the risk outweighs the multiplier.
    - id: resonance-stone-aura
      item: Resonance Stone aura (carried by Asterion)
      slot: party aura
      note: LATE ACT 2, Mind Flayer Colony — this pickup triggers the weapon respec. The 9m Steeped in Bliss aura makes eligible creatures Psychic-vulnerable, doubling Shadow Blade and Strange Conduit. ⚠ No effect on Undead or Constructs, and it also gives ALLIES Psychic Vulnerability plus disadvantage on mental saves. Asterion carries it within 9m of Charles, closing to 6m when both need Shriek; holster it against Psychic attackers and dangerous mental-save effects, and expect it to stop working once Act 2 ends.
    - id: adamantine-scale-mail
      item: Adamantine Scale Mail
      slot: armour
      note: 'ACT 2 CHEST, and the second Mithral ore. Medium armour, so he is proficient — AC 16 + DEX (max 2) = 18 with DEX 14, ATTACKERS CANNOT LAND CRITICAL HITS, all incoming damage reduced by 1, and melee attackers are sent Reeling. Crit immunity is the point: a critical hit roughly doubles the concentration-save DC, and he is holding Bless, Hex or Darkness in every fight while wearing a ring that gives him disadvantage on that save. ⚠ He CANNOT use Adamantine Splint — that is Heavy armour and multiclassing never grants heavy proficiency. The Splint mould and the other ore go to Bonbon.'
    - id: cloak-of-protection
      item: Cloak of Protection
      slot: cloaks
      note: 'HIS, not Gale''s. Quartermaster Talli at Last Light Inn. +1 Armour Class and +1 to Saving Throws. ⚠ THE ARBITRATION: exactly one exists, and it is the ONLY cloak in the entire Act 2 pool that touches saving throws at all. Charles is the one party member carrying a permanent, self-inflicted DISADVANTAGE on every save (Risky Ring) while holding the concentration, and he is the one standing in every area attack. Gale can be positioned out of danger and already has Constitution-save advantage from Spidersilk Armour plus save proficiency; Bonbon has War Caster and AC 18. Charles has none of those.'
    - id: risky-ring
      item: Risky Ring
      slot: rings
      note: 'Moonrise, from Araj Oblodra. Advantage on ALL attacks, disadvantage on saves — the crit-fishing engine. ⚠ Be honest about the cost: disadvantage on saves roughly squares his concentration-failure rate. Mitigate it in order — Aura of Protection at Paladin 6 adds his CHA modifier to his own and nearby allies'' saves, the Cloak of Protection above adds +1, and in Act 3 the Amulet of Greater Health''s advantage on Constitution saves cancels the disadvantage outright and returns those rolls to a straight d20.'
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      slot: rings
      note: 'Gauntlet of Shar, Self-Same Trial — on the ground where your shadow copy dies. Your first attack after a kill is a GUARANTEED crit: a free doubled smite every fight. It can be set to "Ask" in the Reactions tab and banked for the right target, and it applies to every target hit by a single AoE attack. ⚠ Per the wiki it applies to WEAPON attack rolls only, despite a broader tooltip, so it can never be reassigned to Gale to crit a Scorching Ray. ⚠ Using Control Undead on the shadow copy of an Oathbreaker Paladin instantly kills it but it will NOT drop the ring — kill the copy normally.'
    - id: ring-slot-2
      item: Shadow Blade Ring (costs no ring slot)
      wiki: Shadow Blade Ring
      slot: rings
      note: 'THE REASON THE RING MATH WORKS. As of Patch 8 the ring''s Shadow Blade no longer requires concentration and the blade lasts until long rest, and the wiki states plainly that "the ring can be unequipped after summoning the shadow blade." So it is not a third ring competing for a slot — it is a pre-combat button. Summon, unequip, put Risky Ring and Killer''s Sweetheart back on. Carry it as insurance for any fight where he cannot spend a pact slot on his own Shadow Blade.'
    - id: head-slot
      item: Covert Cowl
      wiki: Covert Cowl
      slot: head
      note: 'ACT 2 HEAD, from Last Light. −1 crit threshold while Obscured — and standing inside his own Darkness is Heavily Obscured, so it is live on every turn he plays the cloud correctly. It requires Light Armour proficiency, which he has and which medium-armour characters inherit. ⚠ It is illegal on Asterion, whose Unarmoured Defence breaks on any helmet marked as armour, so there is no contest for it.'
    - id: act2-hands-charles
      item: Gloves of Baneful Striking (held over)
      slot: hands
      note: 'Act 2 offers him no glove upgrade worth the swap, so the −1d4 to enemy saves stays on. The tempting alternative is Gloves of Belligerent Skies: Divine Smite is Radiant so every smite would Reverberate, and the wiki notes that Phalar Aluve''s Shriek Thunder — which normally fails to trigger them — "is changed in Honour difficulty, and functions as expected." They stay on Gale because he applies the rider 5–7 times a cast against Charles''s two swings.'
    act3:
    - id: shadow-blade-phalar-act3-default
      item: 3d8 Shadow Blade main hand + Phalar Aluve off-hand
      wiki: Shadow Blade (weapon)
      slot: weapons
      note: 'ACT-3 DEFAULT, carried over unchanged — bind Shadow Blade for CHA and Deepened Pact, Phalar off-hand for pre-cast Shriek, bonus-action swing only when free. Beats Render or the Knife because the party generates so many Shriek triggers. ⚠ Confirm the Stone aura still works after Act 2, and holster it when the Psychic and mental-save downside is unsafe.'
    - id: nyrulna-physical-fallback
      item: Nyrulna + Phalar Aluve (Act-3 physical fallback)
      slot: weapons
      note: 'OPTIONAL, from Akabi''s Chult jungle. Against Psychic-immune targets, bind Nyrulna main hand for +3, 1d6 Thunder, movement and fall-damage immunity, Phalar still off-hand. Charge-Bound Warhammer is the earlier one-handed fallback; neither beats Shadow Blade on targets that can take the Stone''s Psychic Vulnerability.'
    - id: helldusk-armour
      item: Helldusk Armour
      slot: armour
      note: 'ACT 3 CHEST, and he CAN wear it. Carried by Raphael in the House of Hope. AC 21 flat, Fire resistance, cannot be Burned, ALL INCOMING DAMAGE REDUCED BY 3, Infernal Retribution, a 1/long-rest Fly, and no Stealth penalty. ⚠ It is Heavy armour and multiclassing never grants heavy proficiency — but the wiki is explicit that the armour carries its own passive: "You are considered Proficient with this armour while wearing it." That single line is what lets a medium-armour Paladin/Warlock wear the best chest piece in the game. Flat AC 21 needs no DEX and beats Adamantine Scale Mail by 3 AC and 2 damage reduction.'
    - id: armour-of-agility-alternative
      item: Armour of Agility (save-focused alternative)
      slot: armour
      note: Sold by Gloomy Fentonson at the Stormshore Armoury. Medium, AC 17 plus his FULL Dexterity modifier and +2 to all Saving Throws, no Stealth penalty. Take it over Helldusk only if you would rather have +2 saves for concentration than flat AC 21 and −3 damage; with DEX 14 it lands at AC 19, so it trades 2 AC for 2 saves.
    - id: sarevok-s-horned-helmet
      item: Sarevok's Horned Helmet
      slot: head
      note: 'SELECTED OFFENSIVE HEAD, carried by Sarevok Anchev at the Murder Tribunal. Lowers the critical-hit threshold — stacking with Hexblade''s Curse and the Risky Ring''s advantage — and Dauntless makes him immune to Frightened and other emotion-altering conditions, which is a real Honour-Mode save on a frontliner. It requires Medium armour proficiency, which he has.'
    - id: helm-of-balduran
      item: Helm of Balduran (defensive alternative)
      slot: head
      note: 'From the Wyrmway (Ansur). Crit immunity, +1 AC and +1 to SAVING THROWS, 2 HP a turn and Stun immunity. Straight trade against Sarevok''s: this is defence and save-reliability, Sarevok''s is more crits. Take Balduran for long fights where he is holding concentration in the Risky Ring — though note Helldusk Armour does not give crit immunity the way Adamantine Scale Mail did, so this is the only place he can get it back in Act 3.'
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      slot: rings
      note: One guaranteed critical hit after Charles kills a creature. Bank it for a high-level Divine Smite to double the smite dice.
    - id: act3-ring2-charles
      item: Risky Ring (second slot, held over)
      slot: rings
      note: 'Advantage on every attack roll is the single largest crit-rate multiplier available and it is the engine of the whole build, so it keeps the slot. The save penalty is now fully answered: Amulet of Greater Health returns Constitution saves to a straight roll, and Helldusk Boots convert one failed save a turn into a success. Callous Glow Ring is the swap if you ever drop Risky — but it needs illuminated targets, which fights his own Darkness.'
    - id: helldusk-gloves
      item: Helldusk Gloves
      slot: hands
      note: 'SELECTED DEFAULT, from Haarlep in the House of Hope. +1d6 Fire on weapon attacks, and Infernal Acuity — nominally +1 spell attack and save DC, which the wiki notes actually lands as +1 to ALL attack rolls. The weapon rider applies on each of his many pact-weapon hits, roughly +17 across a seven-attack nova.'
    - id: craterflesh-gloves
      item: Craterflesh Gloves (Bhaal path only)
      slot: hands
      note: 'GATED ALTERNATIVE, and a large one. Sold by the Echo of Abazigal, which only opens if Charles completes Impress the Murder Tribunal and becomes an Unholy Assassin of Bhaal. Deals +1d6 Force on a critical hit — and per the wiki it actually lands as 2d6, because the crit doubles it, and it is one of the few damage riders that still works in Honour Mode. Charles is the party''s crit engine, so on a full auto-crit nova this is roughly +49 against Helldusk''s +17. ⚠ Arrives late in Act 3, so the Shadow Blade and Resonance Stone package carries the build regardless — treat this as a bonus of the Urge-embracing path, not a reason to choose it.'
    - id: helldusk-boots
      item: Helldusk Boots
      slot: feet
      note: 'ACT 3 BOOTS, in a locked Gilded Chest on the top floor of Wyrm''s Rock Fortress. Steadfast stops all forced movement and difficult terrain — replacing what Boots of Striding were doing — and Infernal Evasion lets him use his REACTION TO TURN A FAILED SAVING THROW INTO A SUCCESS. That is the direct answer to the Risky Ring on a concentration holder: one guaranteed save per turn, on the save that matters. ⚠ Contested with Gale, who cannot wear Boots of Persistence at all; Charles wins because he is the one with save disadvantage, and Gale has Armour of Landfall.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      slot: amulets
      note: 'ACT 3 NECK, on the leftmost pedestal in the House of Hope Archive. Sets Constitution to 23 and grants ADVANTAGE ON CONSTITUTION SAVING THROWS. Both halves matter here and nowhere else: +6 to concentration checks, and the advantage cancels the Risky Ring''s disadvantage so those rolls go back to a straight d20 at +CHA. ⚠ Contested with Gale — Charles wins because Armour of Landfall already gives Gale that same advantage, making it redundant on him, whereas only Charles has a disadvantage to cancel. Steal tip: it can be taken without the fight on a DC 20 Sleight of Hand if the Orphic Hammer, the Soul-Sworn Contract and Hope are left alone — an Asterion job.'
    - id: act3-cloak-charles
      item: Cloak of Protection (held over)
      slot: cloaks
      note: 'Kept from Act 2. Flat +1 AC and +1 saves never stops applying, and on the character with save disadvantage that is worth more than the conditional Act 3 cloaks. ⚠ Cloak of Displacement goes to Asterion, who has no armour and no damage reduction; Charles is behind AC 21 and −3 damage. ⚠ Mantle of the Holy Warrior looks tempting and is a trap on him — Crusader''s Mantle is CONCENTRATION, so it would evict the Bless, Hex or Darkness that is his actual job.'
    - id: act3-ranged-charles
      item: Hand Crossbows +2 (held over role)
      slot: ranged weapons
      note: 'Any +2 pair. The slot stays a formality: a Darkness cloud blocks ranged attacks into and out of itself, so on the turns he is playing his own cloud correctly he cannot shoot out of it anyway. Ne''er Misser would be the clever pick here — Magic Missile is not an attack roll and lands regardless — but it goes to Bonbon, whose engine is hand-crossbow hits.'
    - id: bhaalist-armour-unlock
      item: Bhaalist Armour (unlock it, do not wear it)
      slot: armour
      note: 'Sold by the Echo of Abazigal, and Charles as the Dark Urge is the one who unlocks the Murder Tribunal stock. Aura of Murder makes enemies within 3m Vulnerable to PIERCING damage. ⚠ NOT WORN, and the reason is specific: none of his damage is Piercing. Shadow Blade is Psychic, Phalar Aluve is Slashing, Divine Smite is Radiant. The aura would buff nobody — Asterion''s unarmed strikes are Bludgeoning, and Bonbon''s piercing bolts are fired from range, far outside a 3m aura. It also costs 5–7 AC against Helldusk. Buy it on the Bhaal path for completeness, then leave it in the chest.'
  playstyle: |-
    - **Act 1 through most of Act 2 — two-handed Phalar:** bind Phalar Aluve, keep the off-hand empty, pre-cast Shriek, and enter a farmed Darkness Arrow cloud with Devil's Sight. Maintain Bless, Divine Favour, or Hex because the cloud is concentration-free; toggle GWM All In when advantage makes the −5 acceptable.
    - **Darkness placement (matters now that Gale is a Fire Sorlock):** put the cloud so **Charles is inside it and his target is not**. He is then an unseen attacker — advantage in, disadvantage out — while the enemy stays visible and shootable for Gale. A Darkness cloud explicitly blocks ranged attacks *into and out of* itself, so an enemy standing inside it is one Gale cannot touch, and the party loses focus fire. This costs Charles nothing and lets Gale's Scorching Ray land on the same target, inside Phalar Shriek's 6m aura, where each ray picks up an extra 1d4 Thunder.
    - **Pre-cast Shriek for Gale, not just for yourself:** Shriek adds 1d4 Thunder every time an affected enemy takes damage, and Scorching Ray deals damage 3–7 separate times per cast. Activating Shriek before Gale's turn is worth roughly 7d4 on a single level-6 cast.
    - **Gale's light does not affect you:** the Coruscation Ring keys off *Gale* being illuminated, not the target, and Daylight only dispels Darkness at the instant it is cast. Keep using Darkness Arrows freely — just fire them after Gale's once-per-long-rest Daylight is already up.
    - **Late Act 2+ — Shadow + Stone:** on acquiring the Resonance Stone, usually respec at character level 9 to Warlock 5 / Paladin 4, replace GWM with Dual Wielder, summon 3d8 Shadow Blade main hand, and off-hand Phalar. Asterion carries the Stone within 9m to double the Psychic package.
    - **Once per long rest, out of combat:** cast **Aid** (upcast as high as you can spare) for a permanent party-wide max-HP buff that costs no concentration, and hold the **Staff of Arcane Blessing** when you cast **Bless** so every target also picks up Mystra's Blessing (+1d4 spell attack) — then swap back to Phalar. Charles is the party's only Bless caster and its only Aid caster, and both are S-tier.
    - **Act 1 turn structure:** pre-cast Shriek from stealth → turn 1 open with **Inquisitor's Might** as your bonus action (+CHA radiant on every weapon hit for 2 turns, plus a no-save Daze) → Booming Blade or a Phalar swing → smite only on crits. Hexblade's Curse goes on turn 2, since it competes with Inquisitor's Might for the bonus action. From Paladin 3, decide at the start of each fight whether the one Channel Oath charge buys Inquisitor's Might or Vow of Enmity.
    - **Give the buff away when it is worth more elsewhere:** Inquisitor's Might reaches 9m and can target an ally. Asterion's 4–6 unarmed hits per turn extract roughly three times the radiant damage Charles's 1–2 swings do, so on adds-heavy turns buff him instead.
    - **Nova:** attack a Held target, spending the largest Divine Smites first. At Paladin 5 after the respec, two three-attack Actions under Haste plus one Phalar off-hand attack reach seven auto-crit swings when the bonus action is free.
    - **Between novas:** fish for crits with advantage and the build's stacked crit-range bonuses; short rest to refill Warlock slots.
  nova:
    assumptions: 'Held target (every hit auto-crits), Darkness up, full 8-slot dump. Darkness holds Concentration, so Wrathful Smite/Hex/Bless are out; Strange Conduit stays. Smite dice double on a crit, Half-Orc adds a die, Savage Attacker rerolls everything. Flat weapon bonuses ride the weapon''s damage type so vulnerability doubles them; smites are radiant.'
    configs:
    - name: Shadow Blade + Resonance Stone (psychic ×2)
      lines:
      - line: Weapon swing — 7d8 + 15, psychic ×2
        count: 6
        each: 111.4
        total: 668
      - line: Phalar off-hand — 3d8 + 15 slashing
        count: 1
        each: 32.4
        total: 32
      - line: Divine Smite L3 — 9d8 radiant
        count: 2
        each: 52.3
        total: 105
      - line: Divine Smite L2 — 7d8 radiant
        count: 2
        each: 40.7
        total: 81
      - line: Divine Smite L1 — 5d8 radiant
        count: 3
        each: 29.1
        total: 87
      turn_total: 973
    caveats: 'Assumes Asterion''s shared Resonance Stone is active, the Savage-Attacker-rerolls-smite quirk, and Hexblade''s Curse''s +4 riding the weapon''s damage type. Conservatively excludes Phalar Shriek''s 1d4 Thunder per qualifying damage instance. Without the Stone, Shadow Blade loses the psychic doubling.'
---
