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
      why: 'THE ACT 1 FIX — available since character level 3 and previously unused by this plan. Bonus Action + the single Channel Oath charge: for 2 turns the target''s weapon attacks deal an additional +CHA modifier RADIANT damage and can Daze enemies for 1 turn, with no save on the Daze. At CHA 17 that is +3 per weapon hit, rising to +5 at CHA 20. Three things make it better than it looks: (1) the radiant damage triggers Luminous Armour''s Radiating Shockwaves and any radiant-keyed rider, (2) it has a 9m range and can target an ALLY — on Asterion''s 4–6 unarmed hits per turn it is worth far more raw damage than on Charles''s 1–2 swings, so decide per fight who gets it, and (3) the Daze has no saving throw at all. ⚠ Only ONE Channel Oath charge per short rest, and from Paladin 3 it competes with Vow of Enmity.'
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
      why: 'Rated S-tier, warlock-exclusive among this party''s classes, and called one of the best layered-control spells in the game — a stronger pick than its "alternative" placement suggests. Large difficult-terrain zone that Blinds, deals Cold at the start of enemy turns and Acid at the end. The honest cost is that it takes the Darkness concentration slot, so it is a per-fight choice: Hunger of Hadar when the fight is a crowd, Darkness when Charles needs the Devil''s Sight advantage lane for himself.'
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
      note: '⚠ CORRECTED — exactly TWO spells known at Warlock 1, not four. Hexblade''s expanded list (Shield, Wrathful Smite) is NOT free: the wiki is explicit that it "is folded into your choosable options — you still spend a spell known pick to learn one." So Shield and Wrathful Smite are two more OPTIONS competing for these same two picks, not bonus grants. Hex and Armour of Agathys win: sustained per-hit damage, and durable non-concentration temp HP. Wrathful Smite is recoverable free later from the Paladin prepared list at char 4, so spending a scarce Warlock pick on it is strictly worse.'
    - category: Skills
      recommendation:
      - Deception
      - Religion
      note: 'Two picks that are easy to miss on the creation screen. Do NOT take Intimidation — Half-Orc Menacing and the Haunted One background both grant it and proficiency does not stack. Matches the allocation already recorded in proficiencies.md.'
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
      recommendation: Oath of Vengeance — and USE it, do not treat it as a placeholder
      note: 'This level also grants Channel Oath (1 charge, short-rest recharge) and, with Vengeance, INQUISITOR''S MIGHT at Paladin class level 1. That is a real Act 1 damage button, not a formality — see the Inquisitor''s Might entry under mandatory spells. The oath is still broken into Oathbreaker after the Resonance Stone respec, which avoids paying to restore it before Withers will respec Charles; but for the whole of Act 1 it is an active damage source that the earlier version of this plan left unused.'
  - char_level: 4
    class: Paladin 2
    gains:
    - Divine Smite
    - Paladin Spellcasting
    - Fighting Style selection
    recommendations:
    - category: Fighting style
      recommendation: Defence (KEEP — Duelling is incompatible with this build)
      note: '⚠ DUELLING WAS CONSIDERED AND REJECTED. Duelling requires "a melee weapon that is not Two-Handed in ONE hand, and no weapon in the other" (a shield is allowed). Great Weapon Master: All In requires "a melee weapon you are Proficient with and are wielding in BOTH hands", and the wiki adds that it applies "when off-hand is empty". The two can never be active on the same attack, so Duelling only makes sense if Charles abandons GWM for a Phalar + shield build — which this plan does not do. Defence''s always-on +1 AC remains the pick. Great Weapon Fighting is the theoretical damage alternative, but BG3 words it as "a Two-Handed melee weapon" and Phalar Aluve is VERSATILE, not Two-Handed, so it may not apply at all — verify in-game before spending the pick on it, and note the gain would only be ~+1.2 per hit on a single 1d10 die.'
    - category: Prepared spells
      recommendation:
      - Bless
      - Divine Favour
      - Command
      - Wrathful Smite
      - Thunderous Smite
      note: 'FIVE prepared, not three — the count is Paladin level + CHA modifier (2 + 3 at CHA 17), and it re-opens every time CHA rises. Arrow darkness is concentration-free, so Bless or Divine Favour stays up inside it; the rest of the slots become Divine Smites. Wrathful Smite is the nova''s one prepared rider and is free here, which is why it was not worth a Warlock pick at char 1. Thunderous Smite outranks Searing Smite — "damage plus forced movement and prone, creating environmental kills and advantage" — and prone means melee advantage, feeding the crit-smite nova. Paladin prepared spells swap freely out of combat, so none of this is locked in.'
  - char_level: 5
    class: Paladin 3
    gains:
    - Divine Health
    - Oath of Vengeance subclass actions
    recommendations:
    - category: Subclass path
      recommendation: Keep the oath intact through Act 1 — but now you must CHOOSE a Channel Oath use
      note: 'Paladin 3 adds Vow of Enmity (Bonus Action + Channel Oath charge, 3m, advantage on attack rolls against one enemy for 10 turns). ⚠ It draws on the SAME single short-rest Channel Oath charge as Inquisitor''s Might, so from here each short rest buys one or the other. Rough guide: Vow of Enmity for a long boss fight (10 turns of advantage offsets GWM''s −5 and doubles the crit rate that drives the smite nova — and the wiki notes a self-cast bug that extends the advantage to ALL targets), Inquisitor''s Might for a short fight or when you want the radiant rider and the free Daze. Break the oath only after the planned Act-2 respec.'
    - category: Prepared spells
      recommendation:
      - Bless
      - Command
      - Divine Favour
      - Wrathful Smite
      - Thunderous Smite
      - Shield of Faith
      note: 'The prepared count rises to SIX (3 + CHA 3) — one net new pick, but the whole list re-opens, so it is easy to click through without noticing. Bane and Hunter''s Mark arrive FREE as Vengeance oath spells and do not consume a slot; Hunter''s Mark duplicates Hex''s +1d6-per-hit without spending Warlock concentration.'
  - char_level: 6
    class: Paladin 4
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Great Weapon Master (SELECTED — the damage pick)
      note: 'Versatile Phalar Aluve qualifies for All In, but ONLY while wielded in both hands with the OFF-HAND EMPTY — no shield, no off-hand weapon. Devil''s Sight advantage from a Darkness Arrow, Vow of Enmity, and Bless all offset the −5 attack penalty; the +10 damage is the Act-1 spike. Keeping GWM is what rules out the Duelling fighting style and the Adamantine Shield variant of this build.'
    - category: Prepared spells
      recommendation:
      - Bless
      - Command
      - Divine Favour
      - Wrathful Smite
      - Thunderous Smite
      - Shield of Faith
      - Protection from Evil and Good
      - Compelled Duel
      note: 'EIGHT prepared (4 + CHA 4 once Hag''s Hair lands) — a second selection on this level that is easy to miss behind the feat. That is 8 of the 11 level-1 Paladin spells that exist, so the real decision is what to leave out: Searing Smite ("worse than other special smites or simply spending the slot on Divine Smite"), Heroism, and Cure Wounds are all bottom-tier and are the three to drop.'
  - char_level: 7
    class: Paladin 5
    gains:
    - Extra Attack
    - Level 2 Paladin spells
    - 'Oath spells free and always prepared: Hold Person and Misty Step'
    recommendations:
    - category: Rotation
      recommendation: Booming Blade or Phalar attack → Extra Attack
      note: 'Two attacks per Action in the two-handed GWM phase; spend Smite reactions on crits and priority hits. NOTE the free oath spells: Hold Person is S tier — "completely prevents a humanoid target from acting and causes nearby attacks to critically hit" — so from here Charles can set up his OWN auto-crit nova instead of waiting on Bonbon to supply the Hold.'
    - category: Prepared spells
      recommendation:
      - Aid
      - Lesser Restoration
      note: 'NINE prepared (5 + CHA 4), and the level-2 list opens here — add these two on top of the char-6 level-1 core. Aid is S tier ("party-wide scaling") and Charles is the party''s ONLY source, since Aid is Cleric/Paladin-only and there is no Cleric. Skip Branding Smite (D tier — "poor damage or action economy compared with other uses of a second-level slot") and Magic Weapon, which Bind Hexed Weapon already makes redundant.'
  - char_level: 8
    class: Paladin 6 (pre-Stone continuation)
    gains:
    - Aura of Protection
    recommendations:
    - category: Timing
      recommendation: Keep the Act-1 Phalar/GWM package until the Resonance Stone
      note: The Stone normally arrives late enough that char 8 comes first. Aura of Protection is the best interim Paladin level and helps the party inside the later Stone aura.
    - category: Prepared spells
      recommendation: Magic Weapon or Protection from Poison
      note: 'TEN prepared (6 + CHA 4) — one more slot on a level that otherwise presents nothing, so it is the easiest to skip entirely. At 10 of the 16 Paladin spells the list is nearly exhaustive; take whichever of these two the next fight wants.'
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
    - category: Patron and skills
      recommendation:
      - Hexblade
      - Deception
      - Religion
      note: 'A Withers respec rebuilds from scratch and re-presents EVERY earlier choice, including these three. Restated here because a player following the rows literally would otherwise lose them.'
    - category: Warlock feat
      recommendation: Dual Wielder
      note: Required for Shadow Blade main hand + Phalar off-hand; GWM no longer applies and the respec removes it.
    - category: Paladin feat
      recommendation: Savage Attacker
      note: The usual char-9 respec has levels for both feats. If the Stone lands at level 8, take Warlock 5 / Paladin 3 for Dual Wielder and add Paladin 4 / Savage Attacker next level.
    - category: Pact Boon
      recommendation: Pact of the Blade
      note: 'A real three-way choice at Warlock 3 (Blade / Chain / Tome), not an automatic grant, and it is the prerequisite for Deepened Pact''s extra attack. "Blade Warlock can attack with Charisma, reducing Paladin''s multiple-attribute burden, while short-rest Pact slots become renewable smites."'
    - category: Invocations
      recommendation:
      - Devil's Sight
      - Agonising Blast
      - Repelling Blast
      note: 'THREE, not two — Warlock 5 grants 2 at W2 plus 1 at W5, and the third is never picked anywhere in the pre-respec rows. ⚠ Invocations cannot be swapped on level-up, so this respec is the only chance to set all three. Devil''s Sight is essentially mandatory — the entire self-cast-Darkness plan runs on it. Repelling Blast turns the already-Agonising Eldritch Blast fallback into ledge-kill control at no cost to the melee plan. AVOID Fiendish Vigour: its at-will False Life clashes with Armour of Agathys, because temp-HP sources never stack.'
    - category: Fighting style
      recommendation: Defence (again)
      note: 'Re-chosen at Paladin 2 during the respec, and the char-4 reasoning no longer applies now that GWM is gone. Duelling still requires an empty off-hand and he now dual-wields Shadow Blade + Phalar; Great Weapon Fighting still requires a Two-Handed weapon and Shadow Blade is one-handed. Defence''s +1 AC is the only style that actually functions on the post-Stone build.'
    - category: Warlock cantrips
      recommendation:
      - Eldritch Blast
      - Booming Blade
      - Mage Hand
      note: 'THREE cantrips at Warlock 5 (2 at W1, +1 at W4), all re-picked by the respec and none of them named in this row before. Booming Blade is what triggers the Ring of Arcane Synergy. Bone Chill and Minor Illusion are the alternates.'
    - category: Warlock spells
      recommendation:
      - Shadow Blade
      - Darkness
      - Counterspell
      - Misty Step
      - Armour of Agathys
      - Hunger of Hadar
      note: 'SIX spells known at Warlock 5, not four. Shadow Blade is immediately 3d8 from the level-3 pact slots; Darkness + Devil''s Sight replace the Act-1 arrow dependency. Armour of Agathys upcast from a level-3 pact slot is 15 temp HP / 15 Cold and costs no concentration. Hunger of Hadar is S tier ("blinds creatures inside, makes the area difficult terrain, and deals cold at the start of turns plus acid at the end") and Charles is the party''s only possible carrier. ⚠ EFFICIENCY FLAG: Darkness becomes a FREE always-prepared Oathbreaker oath spell one level later at char 10, and with no Warlock levels left this pick can never be swapped without a second respec — consider Hex here instead and cover the one-level gap with the Darkness arrows he already carries.'
    - category: Prepared spells
      recommendation:
      - Bless
      - Command
      - Divine Favour
      - Wrathful Smite
      - Thunderous Smite
      - Shield of Faith
      - Protection from Evil and Good
      - Compelled Duel
      note: 'EIGHT prepared (Paladin 4 + CHA 4), and LEVEL 1 ONLY — Paladin 4 has no level-2 slots, so Aid is genuinely unavailable until char 10. Bless is the highest-impact level-1 pick ("turns misses into hits… stacks with other accuracy improvements") and Command is ranked the #3 spell in the game — "level-one, non-concentration control that scales by adding targets when upcast" — which is exactly why it coexists with Bless concentration.'
    - category: Subclass path
      recommendation: Break the freshly selected Paladin oath → Oathbreaker
      note: Keeping the Act-1 oath intact makes this free. If he became an Oathbreaker earlier, pay the Oathbreaker Knight to restore the oath before Withers will respec him, then break it again.
  - char_level: 10
    class: Paladin 5
    gains:
    - Extra Attack (stacks with Deepened Pact outside Honour Mode for three attacks)
    - Level 2 Paladin spells
    - Oathbreaker spells Darkness and Crown of Madness
    recommendations:
    - category: Prepared spells
      recommendation:
      - Aid
      - Lesser Restoration
      - Magic Weapon
      note: 'TEN prepared (5 + CHA 5 once Mirror of Loss lands) and the level-2 list finally opens — add these on top of the char-9 level-1 core. Aid is S tier and Charles is the party''s only source. Darkness and Crown of Madness arrive FREE as Oathbreaker oath spells and cost no slot, which is what makes the char-9 Darkness pick redundant.'
  - char_level: 11
    class: Paladin 6
    gains:
    - Aura of Protection
    recommendations:
    - category: Prepared spells
      recommendation: Protection from Poison
      note: 'ELEVEN prepared (6 + CHA 5) — one more slot on a level whose only headline is the aura, so it is easy to skip. Branding Smite is the alternative if you want a non-radiant bonus-action smite for the radiant-resistant Act 3 enemies.'
  - char_level: 12
    class: Paladin 7
    gains:
    - Aura of Hate
    recommendations:
    - category: Prepared spells
      recommendation: Branding Smite (or any remaining level-1 spell)
      note: 'TWELVE prepared (7 + CHA 5) — that is 12 of the 16 Paladin spells that exist, so the only real decision left is which four to leave out: Searing Smite, Heroism, Cure Wounds and Branding Smite are the bottom-tier four. Four Oathbreaker oath spells (Hellish Rebuke, Inflict Wounds, Crown of Madness, Darkness) ride free on top of the twelve.'
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
      note: 'Arcane Tower BASEMENT, Underdark. NOT a combat weapon — a buff stick he swaps in before a fight. Every Bless cast by its WIELDER also applies Mystra''s Blessing, +1d4 to spell attack rolls, to each blessed creature. Charles was already spending his concentration on Bless, so the routine costs only the swap: hold staff → upcast Bless to a level 2 slot for all four → swap to Phalar and activate Shriek. Gale is the payoff, gaining +1d4 accuracy on every ray. It also grants its own Bless 1/long rest to any holder. ⚠ Does NOT enhance the Whispering Promise''s version of Bless.'
    - id: arrows-of-darkness
      item: Arrows of Darkness (farm)
      slot: consumables
      note: 'ACT-1 and early-ACT-2 advantage engine. 3m cloud, 3 turns, no Concentration — so Devil''s Sight grants advantage while Charles holds Bless, Divine Favour or Hex. Prefer Bonbon placing it; if Charles fires it, do so before switching to Phalar and activating Shriek. Restock from arrow vendors — the build stops Warlock at 2 until the Stone.'
    - id: dual-hand-crossbows-plus-one
      item: Dual Hand Crossbows +1
      slot: ranged weapons
      note: SELECTED ranged fallback and Darkness-Arrow launcher. Farm Dammon, Roah, Derryth and Jeera for +1 copies; the ranged set does not interfere with two-handed Phalar.
    - id: luminous-armour
      item: Luminous Armour
      slot: armour
      note: SELECTED chest once Divine Smite arrives at char 4. The Selûnite Outpost medium armour reaches AC 17 with DEX 14, and each Smite's Radiant damage emits a Radiating Shockwave that penalises nearby enemy attacks.
    - id: adamantine-scale-mail
      item: Adamantine Scale Mail (defensive alternative)
      slot: armour
      note: DEFENSIVE ALTERNATIVE from the party's second Mithral ore. Keeps medium-armour proficiency while adding crit immunity, 1 damage reduction and Reeling when a melee attacker hits. Luminous stays selected for its Radiating Shockwaves.
    - id: boots-of-striding
      item: Boots of Striding
      slot: feet
      note: SELECTED boots from Minthara. Concentrating on Bless, Divine Favour or Hex inside an arrow cloud grants Momentum and blocks Prone and forced movement; after the respec, self-cast Darkness supplies the concentration.
    - id: amulet-of-misty-step
      item: Amulet of Misty Step
      slot: amulets
      note: SELECTED neck from Priestess Gut's chambers. Misty Step 1/short rest solves approach and elevation; Asterion already has Monk movement, the Sentient Amulet and later the Night Walkers.
    - id: haste-helm
      item: Haste Helm
      slot: head
      note: SELECTED Act-1 head from the Blighted Village. Three turns of opening Momentum to reach priority targets, and the Ring of Arcane Synergy keeps this slot free. Asterion can borrow it when the speed is not needed.
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
      note: Gish Far'aag, Crèche. Booming Blade damage → Arcane Synergy for 2 turns, adding CHA to subsequent weapon attacks. Pairs with Strange Conduit without duplicating Bonbon's Diadem; Risky Ring replaces it in Act 2.
    - id: strange-conduit-ring
      item: Strange Conduit Ring
      slot: rings
      note: '+1d4 Psychic on weapon attacks while Concentrating (Crèche). Act 1 — hold Bless, Divine Favour or Hex inside concentration-free arrow darkness. After the respec, self-cast Darkness powers it and the Resonance Stone doubles the rider.'
    act2:
    - id: self-cast-shadow-blade-upcast-to-3d8
      item: Self-cast Shadow Blade upcast to 3d8
      wiki: Shadow Blade (weapon)
      slot: weapons
      note: 'POST-RESONANCE DEFAULT. Keep two-handed Phalar/GWM until the late-Act-2 Stone pickup. Warlock 5 brings level-3 pact slots — summon 3d8 Shadow Blade and bind THIS main hand to CHA so Deepened Pact applies, leaving Phalar unbound off-hand. Usual char-9 split is Warlock 5 / Paladin 4; Warlock 5 / Paladin 3 is the minimum if the Stone lands at level 8.'
    - id: phalar-aluve-offhand
      item: Phalar Aluve (selected off-hand)
      slot: weapons
      note: 'PARTY-DAMAGE DEFAULT after the Stone. Dual Wielder replaces GWM so Phalar stays beside the Light Shadow Blade, +1 AC. Pre-cast Shriek and keep Charles and Asterion inside its 6m aura (the Stone reaches 9m). Shriek fires 1d4 Thunder per qualifying party damage instance and −1d4 to enemy attacks and all saves — worth more than a personal-DPR off-hand here. Phalar is unbound and Charles lacks Two-Weapon Fighting, so its bonus-action swing is last priority.'
    - id: render-of-mind-and-body-personal-alternative
      item: Render of Mind and Body (personal-DPR alternative)
      slot: weapons
      note: 'PRE-STONE, from Lann Tarv at Moonrise after convincing Z''rell to help. Light, so it pairs with Shadow Blade without Dual Wielder — a personal-only respec could take Savage Attacker + a CHA ASI instead. Its advantaged off-hand hit gains +1d8 Psychic, doubled by the Stone, but buffs nothing else. Keep Phalar unless optimising Charles in isolation.'
    - id: knife-of-the-undermountain-king-personal-alternative
      item: Knife of the Undermountain King (personal crit alternative)
      slot: weapons
      note: Act-1 Crèche, and Light enough to pair with Shadow Blade without Dual Wielder. Its global −1 crit threshold and melee-die reroll make it his best crit stat-stick — but Bonbon already uses the unique Knife, and taking it loses Phalar Shriek. Not the party default.
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
      note: LATE ACT 2, Mind Flayer Colony — this pickup triggers the weapon respec. The 9m Steeped in Bliss aura makes eligible creatures Psychic-vulnerable, doubling Shadow Blade and Strange Conduit. ⚠ No effect on Undead or Constructs, and it also gives ALLIES Psychic Vulnerability plus disadvantage on mental saves. Asterion carries it within 9m of Charles, closing to 6m when both need Shriek; holster vs Psychic attackers and dangerous mental-save effects.
    - id: risky-ring
      item: Risky Ring
      slot: rings
      note: Moonrise, from Araj Oblodra. Advantage on ALL attacks, disadvantage on saves — the crit-fishing engine. Keep it behind Aura of Protection to offset the save penalty.
    - id: ring-slot-2
      item: Shadow Blade Ring (backup)
      wiki: Shadow Blade Ring
      slot: rings
      note: Summons a 2d8 psychic blade once per short rest. Strange Conduit Ring stays the default second ring for nova turns; carry this as insurance if Charles loses or cannot prepare his class-cast blade.
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      slot: rings
      note: 'Gauntlet of Shar, Self-Same Trial. Your first attack after a kill is a GUARANTEED crit — a free doubled smite every fight. ⚠ Per the wiki it applies to WEAPON attack rolls only, despite a tooltip that reads more broadly; it is perfect on Charles for exactly that reason, but it can never be reassigned to Gale to crit a Scorching Ray.'
    - id: head-slot
      item: Covert Cowl (Darkness option)
      wiki: Covert Cowl
      slot: head
      note: Last Light. −1 crit threshold while Obscured — the Darkness crit-fishing default. Once Bonbon swaps the Diadem for the Helmet of Arcane Acuity, Charles can borrow the Diadem for raw damage after Risky Ring displaces his Arcane Synergy Ring. (The Dark Justiciar Helmet is a second Covert-Critical head for Asterion.)
    act3:
    - id: shadow-blade-phalar-act3-default
      item: 3d8 Shadow Blade main hand + Phalar Aluve off-hand
      wiki: Shadow Blade (weapon)
      slot: weapons
      note: 'ACT-3 DEFAULT, unchanged from late Act 2 — bind Shadow Blade for CHA and Deepened Pact, Phalar off-hand for pre-cast Shriek, bonus-action swing only when free. Beats Render or the Knife because the party generates so many Shriek triggers. ⚠ Confirm the Stone aura still works after Act 2, and holster it when the Psychic/mental-save downside is unsafe.'
    - id: nyrulna-physical-fallback
      item: Nyrulna + Phalar Aluve (Act-3 physical fallback)
      slot: weapons
      note: 'OPTIONAL, from Akabi''s Chult jungle. Against Psychic-immune targets, bind Nyrulna main hand for +3, 1d6 Thunder, movement and fall-damage immunity, Phalar still off-hand. Charge-Bound Warhammer is the earlier one-handed fallback; neither beats Shadow Blade on targets that can take the Stone''s Psychic Vulnerability.'
    - id: sarevok-s-horned-helmet
      item: Sarevok's Horned Helmet
      slot: head
      note: SELECTED OFFENSIVE HEAD. Lowers the critical-hit threshold and grants Darkvision. Stacks with his other crit-range effects on targets that are not already Paralyzed.
    - id: helm-of-balduran
      item: Helm of Balduran (defensive alternative)
      slot: head
      note: 'THE ANSWER TO CHARLES''S CRIT PROBLEM, since he can use nothing from the Adamantine forge — he has medium armour only and never has a free off-hand for a shield. From the Wyrmway (Ansur), and medium-armour proficiency is all it needs. It grants crit immunity plus +1 AC and +1 to SAVING THROWS, and that last part directly offsets the Risky Ring''s permanent disadvantage on saves. Straight trade against Sarevok''s: this is defence and save-reliability, Sarevok''s is more crits. Take Balduran for long fights where he is holding concentration on Darkness while wearing the Risky Ring — the most fragile concentration in the party.'
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      slot: rings
      note: One guaranteed critical hit after Charles kills a creature. Save it for a high-level Divine Smite to double the smite dice.
    - id: helldusk-gloves
      item: Helldusk Gloves
      slot: hands
      note: 'SELECTED DEFAULT. Fire damage on weapon attacks plus better spell attacks and save DC. The weapon rider applies on each of his many pact-weapon hits — roughly +17 across a seven-attack nova.'
    - id: craterflesh-gloves
      item: Craterflesh Gloves (Bhaal path only)
      slot: hands
      note: 'GATED ALTERNATIVE, and a large one. Sold by the Echo of Abazigal, which only opens if Charles completes Impress the Murder Tribunal and becomes an Unholy Assassin of Bhaal. Deals +1d6 Force on a critical hit — and per the wiki it actually lands as 2d6, because the crit doubles it. Charles is the party''s crit engine (Held targets auto-crit, plus Killer''s Sweetheart, Risky Ring, Sarevok''s Helmet and Hexblade''s Curse), so on a full auto-crit nova this is roughly +49 against Helldusk''s +17. ⚠ Arrives late in Act 3, so the Shadow Blade + Resonance Stone package carries the build regardless — treat this as a bonus of the Urge-embracing path, not a reason to choose it.'
  playstyle: |-
    - **Act 1 through most of Act 2 — two-handed Phalar:** bind Phalar Aluve, keep the off-hand empty, pre-cast Shriek, and enter a farmed Darkness Arrow cloud with Devil's Sight. Maintain Bless, Divine Favour, or Hex because the cloud is concentration-free; toggle GWM All In when advantage makes the −5 acceptable.
    - **Darkness placement (matters now that Gale is a Fire Sorlock):** put the cloud so **Charles is inside it and his target is not**. He is then an unseen attacker — advantage in, disadvantage out — while the enemy stays visible and shootable for Gale. A Darkness cloud explicitly blocks ranged attacks *into and out of* itself, so an enemy standing inside it is one Gale cannot touch, and the party loses focus fire. This costs Charles nothing and lets Gale's Scorching Ray land on the same target, inside Phalar Shriek's 6m aura, where each ray picks up an extra 1d4 Thunder.
    - **Pre-cast Shriek for Gale, not just for yourself:** Shriek adds 1d4 Thunder every time an affected enemy takes damage, and Scorching Ray deals damage 3–7 separate times per cast. Activating Shriek before Gale's turn is worth roughly 7d4 on a single level-6 cast.
    - **Gale's light does not affect you:** the Coruscation Ring keys off *Gale* being illuminated, not the target, and Daylight only dispels Darkness at the instant it is cast. Keep using Darkness Arrows freely — just fire them after Gale's once-per-long-rest Daylight is already up.
    - **Late Act 2+ — Shadow + Stone:** on acquiring the Resonance Stone, usually respec at character level 9 to Warlock 5 / Paladin 4, replace GWM with Dual Wielder, summon 3d8 Shadow Blade main hand, and off-hand Phalar. Asterion carries the Stone within 9m to double the Psychic package.
    - **Once per long rest, out of combat:** cast **Aid** (upcast as high as you can spare) for a permanent party-wide max-HP buff that costs no concentration, and hold the **Staff of Arcane Blessing** when you cast **Bless** so every target also picks up Mystra's Blessing (+1d4 spell attack) — then swap back to Phalar. Charles is the party's only Bless caster and its only Aid caster; both are S-tier and neither was in the original plan.
    - **Act 1 turn structure (this is the fix for feeling weak at char 4):** pre-cast Shriek from stealth → turn 1 open with **Inquisitor's Might** as your bonus action (+CHA radiant on every weapon hit for 2 turns, plus a no-save Daze) → Booming Blade or a Phalar swing → smite only on crits. Hexblade's Curse goes on turn 2, since it competes with Inquisitor's Might for the bonus action. From Paladin 3, decide at the start of each fight whether the one Channel Oath charge buys Inquisitor's Might or Vow of Enmity.
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
