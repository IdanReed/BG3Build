---
nickname: Charles
builds:
- name: The Three Booms
  is_primary: true
  role: Melee crit-smite nova frontline + self-supplied Hold Person
  class: Oath of Vengeance Paladin 7 / Hexblade Warlock 5
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
  ability_scores:
  - ability: STR
    steps:
    - score: 8
      source: 'point-buy'
  - ability: DEX
    steps:
    - score: 14
      source: 'point-buy'
  - ability: CON
    steps:
    - score: 15
      source: 'point-buy'
    - score: 16
      source: '+1 Racial'
  - ability: INT
    steps:
    - score: 8
      source: 'point-buy'
  - ability: WIS
    steps:
    - score: 10
      source: 'point-buy'
  - ability: CHA
    steps:
    - score: 15
      source: 'point-buy'
    - score: 17
      source: '+2 Racial'
    - score: 18
      source: '+1 Hag''s Hair'
    - score: 20
      source: '+2 Mirror of Loss, Act 3'
  locked_decisions: 'FOUR things are fixed for the whole run and everything else is built around them. (1) GLOVES OF BATTLEMAGE''S POWER from Act 2 onward — the Arcane Acuity engine. (2) LUMINOUS ARMOUR in every act — the Radiant Shockwave engine. (3) OATH OF VENGEANCE, never broken — Inquisitor''s Might is the per-hit radiant that feeds the Shockwave. (4) CONCENTRATION IS HOLD PERSON — he sets up his own auto-crit nova and holds nothing else.'
  feats:
  - at: Act 1 char 6 (Paladin 4)
    feat: Great Weapon Master (temporary)
    note: 'Phalar Aluve is Versatile, so two-handed attacks qualify for All In (−5 attack / +10 damage). Darkness-Arrow advantage and Vow of Enmity offset the penalty. Replaced at the Resonance Stone respec.'
  - at: Late Act 2 Resonance Stone respec (Warlock 4 feat; usually char 9)
    feat: Dual Wielder
    note: Replaces GWM. Required to hold 3d8 Shadow Blade main hand with Versatile Phalar off-hand; also +1 AC.
  - at: Late Act 2 Resonance Stone respec (Paladin 4 feat; usually char 9)
    feat: Savage Attacker
    note: Rerolls Shadow Blade, Phalar Aluve and Divine Smite damage dice. The off-hand Phalar swing is the seventh attack when the bonus action is free.
  weapon_plan: 'ACT 1–mid ACT 2 — two-handed bound Phalar Aluve + GWM, Darkness Arrows for advantage. LATE ACT 2 — respec at char 9 to Warlock 5 / Paladin 4, GWM → Dual Wielder, 3d8 Shadow Blade main hand + Phalar off-hand inside the Stone aura. ⚠ Against Psychic-immune targets, bind Phalar main hand instead — it is already in the off-hand and deals Slashing.'
  creation:
    level1_class: Warlock 1 (Hexblade patron)
    level1_gains: 'Pact Magic (1 × L1 short-rest slot), Hexblade''s Curse (bonus action), Bind Hexed Weapon (attack with CHA). Pact of the Blade waits until Warlock 3.'
    subclass_choice: Hexblade patron (Warlock 1)
    proficiencies:
      armor_weapons: 'Medium armour, shields and martial weapons (Hexblade). Multiclassing into Paladin does NOT grant heavy armour — which is fine, because Luminous Armour is medium and locked in for the whole run. ⚠ This is also why the GRYMSKULL HELM is illegal on him: it requires Heavy Armour proficiency.'
      saving_throws: WIS + CHA (Warlock).
      skills: 2 Warlock picks + Haunted One (Medicine, Intimidation).
    starting_cantrips: 2 at Warlock 1 — Eldritch Blast + Booming Blade.
    starting_spells: '2 at Warlock 1 — Hex + Armour of Agathys — then a third at Warlock 2 (Shield) and six by Warlock 5. The Hexblade expanded list is NOT free; see the char-1 row.'
    notes: 'Warlock 1 first is deliberate and stays that way: at STR 8 he needs Bind Hexed Weapon from the first fight, and heavy armour proficiency is worth nothing to a build locked to Luminous Armour. Act 1 stops Warlock at 2 — Hexblade gives CHA weapon binding and Devil''s Sight, then Paladin 1–5 gives Inquisitor''s Might at char 3, Smite at char 4, temporary GWM at 6, and Extra Attack at 7. Paladin 6 for Aura of Protection if char 8 lands before the Stone. Use farmed Darkness Arrows instead of learning Darkness. The oath is NEVER broken, so there is no Oathbreaker Knight to pay and no oath bookkeeping at the respec.'
  spells:
    note: 'A smite platform that sets up its own nova. HIS CONCENTRATION IS HOLD PERSON AND NOTHING ELSE — Bless, Divine Favour, Hex, Darkness, Branding Smite and Wrathful Smite are all Concentration and are therefore out of the rotation. Darkness comes from farmed arrows instead, which costs no Concentration; Bless comes from Asterion. Hunger of Hadar is the one deliberate exception, swapped in only for fights where nothing is Holdable.'
    mandatory:
    - spell: Hold Person
      source: granted
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (55:42) — paralysis costs turns and gives automatic crits within 10 ft; humanoids only, best with high save DC'
      level: '2'
      guide_level: 7
      school: Enchantment
      save: WIS save (Concentration)
      when: char 7 (Paladin 5) — FREE always-prepared Oath of Vengeance spell
      why: 'THE CONCENTRATION, and the reason the nova works. Paralysed humanoids take automatic critical hits from melee within 3m, and a crit doubles every smite die. It arrives FREE as a Vengeance oath spell at Paladin 5, so it costs no Warlock pick and no prepared slot. ⚠ The DC is what matters, and the Gloves of Battlemage''s Power are what raise it: Arcane Acuity adds +1 spell save DC per remaining turn, up to +10. Build stacks with a swing or a smite first, then Hold. ⚠ Humanoids only — see Hunger of Hadar for everything else. ⚠ Holding this excludes every other Concentration spell he owns; that is the intended trade.'
    - spell: Inquisitor's Might
      level: Channel Oath (Oath of Vengeance, Paladin 1)
      guide_level: 3
      school: Oath action — Radiant
      save: None (the Daze rider has NO saving throw)
      when: char 3, and every fight thereafter
      why: 'THE DAMAGE BUTTON AND THE RADIANT ENGINE, live from character level 3. Bonus Action + the single Channel Oath charge: for 2 turns the target''s weapon attacks deal an additional +CHA modifier RADIANT damage and can Daze, with no save on the Daze. At CHA 17 that is +3 per weapon hit, rising to +5 at CHA 20. Three reasons it is mandatory: (1) it is the ONLY per-hit Radiant source he can run, because every other one — Divine Favour, Branding Smite, Crusader''s Mantle — is Concentration or out of level range, and Radiant damage is what triggers LUMINOUS ARMOUR''S Radiant Shockwave; (2) it needs no Concentration, so it coexists with Hold Person; (3) the Daze has no saving throw at all. It also reaches 9m and can target an ALLY — on Asterion''s 4–6 unarmed hits it extracts far more raw damage than on Charles''s swings, but the Shockwave only fires on the WEARER''S own Radiant damage, so keep it on Charles whenever the Orb stack matters.'
    - spell: Divine Smite
      level: Feature (Paladin 2)
      school: Class feature — Radiant
      save: None (melee weapon attack roll)
      when: char 4
      why: 'The build''s core, and the second Radiant Shockwave trigger. Expend any slot on a melee hit: 2d8 Radiant at L1, +1d8 per slot level above 1st (cap 5d8 at an L4 slot), +1d8 vs Fiends/Undead; dice DOUBLE on a crit. Not a prepared spell and not stopped by Counterspell — set the Critical-Hit Divine Smite reactions to auto-confirm. Paladin 7 plus Warlock 5 is roughly nine slots per rest cycle, which is the whole reason this build novas harder than a shallow Paladin dip.'
    - spell: Shadow Blade
      tier: S
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (38:25) — all-day 2d8 finesse psychic weapon with advantage in the dark; broken with the Resonance Stone'
      level: '2'
      guide_level: 9
      school: Illusion
      save: None (bonus action to summon)
      when: Late Act 2 Resonance Stone respec (Warlock 5, usually char 9)
      why: 'POST-STONE core weapon. Level-3 pact slots start it at 3d8 Psychic, lasting until long rest with NO Concentration — which is exactly why it fits a build whose Concentration is spoken for. The Stone doubles the Psychic; Devil''s Sight plus an arrow cloud supplies advantage and defence.'
    recommended:
    - spell: Shield
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (43:07) — reaction +5 AC that only prompts when it turns a hit into a miss; worth a class dip on its own'
      level: '1'
      guide_level: 9
      school: Abjuration
      save: None (reaction, +5 AC)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'NEW PICK, and it matters more than it used to. Locking Luminous Armour means he never gets Adamantine Scale Mail''s crit immunity or Helldusk''s AC 21, so he stands at AC 17–18 all game. Shield is a reaction, costs no Concentration, and is the cheapest way to turn a hit that would break Hold Person into a miss.'
    - spell: Mirror Image
      tier: B
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (12:14) — +9 AC without concentration makes the AI stop targeting you, but costly every fight'
      level: '2'
      guide_level: 9
      school: Illusion
      save: None
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'NEW PICK. Three duplicates give +9 AC and cost NO Concentration — the best non-concentration defence available to him, and the direct answer to a locked AC 17 chest. Each miss removes one duplicate. Pre-cast it in any fight where he expects to be the target.'
    - spell: Armour of Agathys
      tier: A
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (7:37) — solid for any warlock, game-breaking on an Abjuration Wizard whose Arcane Ward preserves the temp HP'
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None
      when: char 1, and re-picked at the respec
      why: 'Temp HP plus Cold retaliation scaling with the pact slot — 15 temp HP / 15 Cold from a Warlock-5 L3 slot, with no Concentration. ⚠ Temp-HP sources never stack with each other, so run this OR the illithid Shield of Thralls, and cast Aid after it rather than before.'
    - spell: Aid
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (4:52) — party-wide max HP for the whole day, no concentration; multiplies summon survivability when upcast'
      level: '2'
      guide_level: 7
      school: Abjuration
      save: None
      when: char 7 (Paladin 5), and again from char 10 post-respec
      why: 'FREE PARTY DURABILITY and the party''s only source — Aid is Cleric or Paladin only and there is no Cleric. Self-centred 9m radius, +5 maximum HP per member (+5 more per slot level above 2nd), lasting UNTIL LONG REST with NO Concentration. Downed allies come back with an extra hit point. ⚠ Cast it AFTER summoning anything you want covered.'
    - spell: Command
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (28:37) — concentration-free turn denial that upcasts to multiple enemies; every higher-level slot competes with it'
      level: '1'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: char 4 (Paladin 2)
      why: 'Rated the #3 spell in the game and it uses NO Concentration, so it coexists with Hold Person. ⚠ RUN IT AS A MASS DISABLE: Command gains an extra target per slot level above 1st, so a level 2 Paladin slot disables a cluster for the turn he needs to close. Its DC rides Arcane Acuity from the gloves, same as Hold Person. ⚠ Does not work on Undead.'
    - spell: Counterspell
      tier: S
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (25:08) — top-five spell; trades a reaction for an enemy turn. NO SCROLLS EXIST, so it must be learnt on level-up'
      level: '3'
      guide_level: 9
      school: Abjuration
      save: Reaction
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Pact-slot reaction for enemy spells dangerous enough to justify delaying a Smite or a Shadow Blade recast. No Concentration.
    - spell: Hunger of Hadar
      tier: S
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (9:07) — no-save blind plus difficult terrain traps enemies inside; layer over Plant Growth to end fights. Acid save DC bugged to 12'
      level: '3'
      guide_level: 9
      school: Conjuration
      save: DEX save (Concentration)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'THE DELIBERATE CONCENTRATION EXCEPTION, and the answer to Hold Person''s humanoid-only limit. Rated S tier, warlock-exclusive in this party, and the only thing he can do with his Concentration when nothing is Holdable — non-humanoid bosses, Undead, Constructs. Large difficult-terrain zone that Blinds, deals Cold at the start of enemy turns and Acid at the end, and pairs with Repelling Blast to shove escapers back in. ⚠ It is Hold Person OR this, never both; on non-humanoid fights Bonbon attempts Hold Monster instead and Charles takes the zone.'
    - spell: Misty Step
      source: granted
      tier: S
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (14:50) — top-five spell; bonus-action 60 ft teleport that every honour mode character should have access to'
      level: '2'
      guide_level: 7
      school: Conjuration
      save: None (bonus action)
      when: char 7 (Paladin 5) — FREE always-prepared Oath of Vengeance spell
      why: 'FREE from the oath, which is why it no longer costs a Warlock pick. Bonus-action mobility to reach a priority target, cross hazards or leave a bad melee position.'
    - spell: Wrathful Smite
      tier: B
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (59:16) — 1d6 plus two turns of Frightened on a WIS save; now also a Hexblade spell after Patch 8'
      level: '1'
      guide_level: 4
      school: Evocation
      save: WIS save (Concentration)
      when: char 4 (Paladin 2) — prepared, but rarely cast
      why: '⚠ KEPT PREPARED, NOT IN THE ROTATION. It is Concentration, so casting it drops Hold Person and the auto-crit nova with it. Free from the Paladin list, so it costs nothing to keep prepared for fights where nothing is Holdable and Hunger of Hadar is not worth the slot. Same logic rules out BRANDING SMITE: it is Radiant and would feed the Shockwave, but it is Concentration, so Booming Blade plus Divine Smite remains the rider package.'
    - spell: Eldritch Blast
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (23:10) — best damage cantrip; separate attack rolls give reliability, crit chances and per-beam riders'
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: char 1 (Warlock 1)
      why: 'Ranged fallback for turns he cannot reach melee (2 beams at char 5, 3 at char 10). Real damage with Agonising Blast plus CHA 20, and Repelling Blast turns it into ledge control. Its attack rolls also ride Arcane Acuity, unlike his weapon swings.'
    - spell: Booming Blade
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (16:31) — free thunder damage riding a normal weapon attack; once per action, so haste and Action Surge multiply it'
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Melee weapon attack roll
      when: char 1 (Warlock 1)
      why: 'The melee cantrip — Phalar in Act 1, Shadow Blade after the respec. Adds Thunder from char 5, once per Action even with Extra Attack, triggers the Ring of Arcane Synergy for 2 turns, AND triggers the Gloves of Battlemage''s Power. It is the cheapest way to put the first Arcane Acuity stacks up before casting Hold Person.'
    - spell: Bane
      source: granted
      tier: B
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (12:55) — never worth a slot early; good late against bosses immune to stronger control, since few resist it'
      level: '1'
      guide_level: 5
      school: Enchantment
      save: CHA save (Concentration)
      when: char 5 (Paladin 3) — FREE always-prepared Oath of Vengeance spell
      why: Free from the oath and costs no slot, but it is Concentration and therefore never cast. Listed only so the oath grant is on the record; Phalar Shriek covers the save-debuff role without Concentration.
    - spell: Hunter's Mark
      source: granted
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (22:04) — the ranger''s Hex; weapon attacks only, but the damage matches your weapon type'
      level: '1'
      guide_level: 5
      school: Divination
      save: None (Concentration)
      when: char 5 (Paladin 3) — FREE always-prepared Oath of Vengeance spell
      why: Free from the oath. Duplicates Hex's +1d6-per-hit, but it is Concentration, so it is off the table for the same reason. On the record only.
    - spell: Mage Hand
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (33:23) — costs a short-rest charge, but scouts, triggers traps, throws potions and soaks one enemy attack'
      level: Cantrip
      guide_level: 9
      school: Conjuration
      save: None
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Third-cantrip exploration and object manipulation with no attack roll or saving throw. Also throws water bottles and potions without spending his own action.
    alternatives:
    - spell: Hex
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (21:08) — d6 on every attack roll all day, reapplied free on kills; enormous on multi-attack casters'
      level: '1'
      school: Enchantment
      save: None (Concentration)
      when: char 1 pick, dropped at the respec
      why: '+1d6 Necrotic per hit and disadvantage on an ability. Correct in Act 1 while arrow darkness keeps Concentration free, and it also powers the Strange Conduit Ring — but Hold Person takes the slot permanently from char 7, so it does not survive into the post-respec list.'
    - spell: Darkness
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (29:56) — blocks ranged attacks both ways; core of the devil''s sight darkness strategy'
      level: '2'
      school: Evocation
      save: None (Concentration)
      when: Deliberately NOT picked
      why: '⚠ DROPPED ON PURPOSE, and this frees a Warlock pick. Self-cast Darkness would compete with Hold Person for Concentration, and farmed ARROWS OF DARKNESS produce the same 3m cloud with none of that cost. Devil''s Sight does not care which source made the cloud. Keep buying arrows all game rather than spending an unswappable pick here.'
    - spell: Bone Chill
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (12:42) — turns off enemy healing with no save and blanks undead attack rolls; not the go-to damage cantrip'
      level: Cantrip
      school: Necromancy
      save: Ranged spell attack
      when: Warlock cantrip alternative
      why: Ranged anti-healing and advantage against Undead — take it over Mage Hand when that niche beats exploration utility.
    - spell: Blink
      tier: C
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (16:31) — C ONLY FOR SOLO PLAY; in a party it just redirects aggro to allies and he says do not cast it'
      level: '3'
      school: Transmutation
      save: None
      when: Hexblade expanded spell at Warlock 5
      why: Non-concentration defence — a chance to go Ethereal at the end of each turn, untargetable until his next. The third contender alongside Shield and Mirror Image if he wants pure evasion instead of AC.
    - spell: Protection from Evil and Good
      tier: C
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (34:45) — disadvantage for aberrations and undead plus BROKEN TOOLTIP (real effect is blanket Frightened immunity, no charm protection); costs concentration'
      level: '1'
      school: Abjuration
      save: None (Concentration)
      when: Prepared-slot alternative
      why: Strong against Aberrations, Celestials, Elementals, Fey, Fiends and Undead, but Concentration, so it is in the same dead pile as Bless and Hex.
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
      picks: 1
      recommendation: Hexblade
      note: The CHA weapon package, armour proficiencies and curse that define the build.
    - category: Cantrips
      picks: 2
      recommendation:
      - Eldritch Blast
      - Booming Blade
      note: A scaling ranged fallback plus the melee cantrip that later triggers both the Ring of Arcane Synergy and the Gloves of Battlemage's Power.
    - category: Spells
      picks: 2
      recommendation:
      - Hex
      - Armour of Agathys
      note: '⚠ Exactly TWO spells known at Warlock 1, not four. The Hexblade expanded list is folded into your choosable options — Shield and Wrathful Smite are two more OPTIONS competing for these same two picks, not bonus grants. Hex and Armour of Agathys win here: sustained per-hit damage while arrow darkness keeps Concentration free, and durable non-concentration temp HP. Wrathful Smite becomes preparable off the Paladin list at char 4, and Shield is the Warlock-2 pick on the very next level.'
    - category: Skills
      picks: 2
      recommendation:
      - Deception
      - Religion
      note: 'Easy to miss on the creation screen. Do NOT take Intimidation — Half-Orc Menacing and the Haunted One background both grant it and proficiency does not stack. Matches proficiencies.md.'
  - char_level: 2
    class: Warlock 2
    gains:
    - Two Eldritch Invocation selections
    - Second Pact Magic slot
    recommendations:
    - category: Invocations
      picks: 2
      recommendation:
      - Devil's Sight
      - Agonising Blast
      note: Devil's Sight is what makes an arrow cloud into an advantage engine; Agonising Blast scales the ranged fallback with CHA.
    - category: Warlock spell
      picks: 1
      recommendation: Shield
      note: 'HIDDEN BEHIND THE INVOCATIONS: Warlock 2 raises Spells Known from 2 to 3, so there is a third level-1 pick on this level and it is easy to click past. Shield is it — a reaction, no Concentration, and the cheapest protection for a build that never rises above AC 17–18. This is the pick the respec row means by "Shield is re-picked". The other candidates are Wrathful Smite (Hexblade expanded), Hellish Rebuke and Protection from Evil and Good; Wrathful Smite is preparable off the Paladin list from char 4 anyway, so spending the pick on it would waste it.'
  - char_level: 3
    class: Paladin 1
    gains:
    - Lay on Hands
    - Divine Sense
    - Channel Oath (1 charge, short-rest recharge)
    - 'Oath of Vengeance: Inquisitor''s Might'
    recommendations:
    - category: Oath
      picks: 1
      recommendation: Oath of Vengeance — PERMANENT, never broken
      note: 'This is a locked decision, not a temporary stop on the way to Oathbreaker. Vengeance is the only oath that supplies a NON-CONCENTRATION, PER-HIT RADIANT rider, and Radiant damage is what triggers Luminous Armour''s Shockwave. It also hands over HOLD PERSON and MISTY STEP free at Paladin 5, which is where his whole nova setup comes from. The costs, accepted knowingly: Paladin 7 gives Relentless Avenger instead of Oathbreaker''s Aura of Hate (roughly +65 on a full nova, since the Resonance Stone doubles its flat +CHA), and Darkness and Crown of Madness never arrive free. ⚠ Not breaking the oath also deletes all the old Oathbreaker-Knight bookkeeping — there is nothing to pay and nothing to restore before Withers will respec him. If Divine Smite alone later proves to be enough of an Orb source, Oathbreaker becomes worth revisiting; that decision is deferred past Act 2.'
    - category: Rotation
      recommendation: Spend the Channel Oath charge on Inquisitor's Might every fight
      note: 'From here, opening with Inquisitor''s Might is the default. +CHA Radiant on every weapon hit for 2 turns means every swing fires a Radiant Shockwave and stacks Radiating Orb on everything within 3m.'
  - char_level: 4
    class: Paladin 2
    gains:
    - Divine Smite
    - Paladin Spellcasting
    - Fighting Style selection
    recommendations:
    - category: Fighting style
      picks: 1
      recommendation: Defence
      note: '⚠ NOT Duelling — it cannot coexist with Great Weapon Master. Duelling needs a non-Two-Handed melee weapon in ONE hand and nothing in the other; GWM: All In needs a weapon wielded in BOTH hands with the off-hand empty. They can never be active on the same attack. Great Weapon Fighting is worded for "a Two-Handed melee weapon" and Phalar Aluve is VERSATILE, so it may not apply at all. Defence''s always-on +1 AC is the pick, and it matters more on a build locked to AC 17.'
    - category: Prepared spells
      picks: 5
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      note: 'FIVE prepared (Paladin level + CHA modifier), and the list re-opens every time CHA rises. ⚠ BLESS IS DELIBERATELY ABSENT — it is Concentration, and Asterion casts it off the Staff of Arcane Blessing instead. Command is the standout because it needs no Concentration. Divine Favour and Shield of Faith are listed as on-the-record Concentration options he will not actually cast; the rest of the slots become Divine Smites.'
  - char_level: 5
    class: Paladin 3
    gains:
    - Divine Health
    - Vow of Enmity and Abjure Enemy
    recommendations:
    - category: Oath spells
      granted: true
      recommendation:
      - Bane
      - Hunter's Mark
      note: 'FREE AND ALWAYS PREPARED, straight from Oath of Vengeance at Paladin 3 — no Warlock spell-known pick and no prepared slot, and neither spell is on the general Paladin list, so the oath is his only route to them. Bane is the one with a use (−1d4 to enemy attacks and saves), but it is Concentration, so in practice it sits idle once Hold Person owns the slot from char 7.'
    - category: Channel Oath budget
      recommendation: Inquisitor's Might by default; Vow of Enmity only in Act 1 boss fights
      note: 'Paladin 3 adds Vow of Enmity (Bonus Action, 3m, advantage on attacks against one enemy for 10 turns) and it draws on the SAME single short-rest charge as Inquisitor''s Might, so each short rest buys one or the other. Rough guide: Vow of Enmity for a long Act 1 boss fight, where 10 turns of advantage offsets GWM''s −5 and doubles the crit rate — the wiki also notes a self-cast bug extending the advantage to all targets. Inquisitor''s Might everywhere else, and ALWAYS from Act 2 onward, because the Risky Ring supplies advantage on every attack by then and the radiant rider becomes the scarcer resource.'
    - category: Prepared spells
      picks: 6
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      note: 'SIX prepared now (Paladin 3 + CHA 3), or seven if the Hag''s Hair has already landed — the count is Paladin level + CHA modifier and it moves the moment CHA does. Easy to miss, because the level looks like it is only about Channel Oath. The char-4 five carry over and ONE SLOT IS DELIBERATELY LEFT OPEN — nothing else on the level-1 list earns a permanent seat, and Paladin prepared spells swap freely out of combat, so keep it free for the fight in front of you (Compelled Duel to peel a caster, Bless on a day someone else carries Concentration).'
  - char_level: 6
    class: Paladin 4
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Great Weapon Master
      note: 'Versatile Phalar qualifies for All In, but ONLY wielded in both hands with the OFF-HAND EMPTY. Arrow-darkness advantage and Vow of Enmity offset the −5; the +10 damage is the Act-1 spike. GWM is what rules out Duelling and any shield variant.'
    - category: Prepared spells
      picks: 8
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      - Protection from Evil and Good
      - Compelled Duel
      note: 'EIGHT prepared (4 + CHA 4 once Hag''s Hair lands) — a second selection on this level, easy to miss behind the feat. Protection from Evil and Good and Compelled Duel are the two new ones; one slot still stays open for a situational pick. Leave out Searing Smite, Heroism and Cure Wounds; they are the bottom tier.'
  - char_level: 7
    class: Paladin 5
    gains:
    - Extra Attack
    - Level 2 Paladin spells
    recommendations:
    - category: Oath spells
      granted: true
      recommendation:
      - Hold Person
      - Misty Step
      note: 'THE TWO THAT DEFINE THE BUILD, AND BOTH ARE FREE. Oath of Vengeance grants them always-prepared at Paladin 5 — no Warlock spell-known pick, no prepared slot, and neither is on the general Paladin list. This is exactly why HOLD PERSON IS ABSENT FROM HIS WARLOCK SIX and why Misty Step gets dropped from it at the respec: paying a pick for either would be paying twice.'
    - category: The nova comes online
      recommendation: Hold Person becomes his permanent Concentration
      note: 'THE PIVOT OF THE WHOLE BUILD. Hold Person arrives free from the oath — no Warlock pick, no prepared slot. Paralysed humanoids take automatic critical hits from melee within 3m, so from here he sets up his own nova instead of waiting on Bonbon. Everything else that wanted Concentration is now permanently out. Misty Step also arrives free, which is why it is not in the Warlock list.'
    - category: Prepared spells
      picks: 9
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      - Protection from Evil and Good
      - Compelled Duel
      - Aid
      - Lesser Restoration
      note: 'NINE prepared (5 + CHA 4) and the level-2 list opens. Aid and Lesser Restoration are the new pair and they fill the list exactly — no open slot on this level. Aid is S tier and Charles is the party''s ONLY source. Skip Branding Smite — it IS Radiant and would feed the Shockwave, but it is Concentration, so it can never be cast alongside Hold Person. Skip Magic Weapon; Bind Hexed Weapon makes it redundant.'
  - char_level: 8
    class: Paladin 6 (pre-Stone continuation)
    gains:
    - Aura of Protection
    recommendations:
    - category: Timing
      recommendation: Keep the Act-1 Phalar/GWM package until the Resonance Stone
      note: 'The Stone normally arrives late enough that char 8 comes first. Aura of Protection is the best interim Paladin level, it adds his CHA modifier to the party''s saves, and it is the first line of defence for the Hold Person concentration he is about to start carrying under the Risky Ring.'
    - category: Prepared spells
      picks: 10
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      - Protection from Evil and Good
      - Compelled Duel
      - Aid
      - Lesser Restoration
      note: 'TEN prepared (6 + CHA 4). Paladin 6 quietly adds a tenth slot behind Aura of Protection, and the char-7 nine carry straight over. Nothing new is needed, so the last slot stays open — prepare Protection from Poison or Magic Weapon on the day a fight actually asks for it.'
  - char_level: 9
    class: RESPEC at the Resonance Stone — Warlock 5 / Paladin 4
    gains:
    - Pact of the Blade and Deepened Pact
    - Level 3 Pact slots and 3d8 Shadow Blade
    - Dual Wielder replaces Great Weapon Master
    - Paladin 4 Savage Attacker
    recommendations:
    - category: Patron and skills
      picks: 3
      recommendation:
      - Hexblade
      - Deception
      - Religion
      note: A Withers respec rebuilds from scratch and re-presents every earlier choice, including these three. ⚠ Take WARLOCK first again — Paladin-first would only buy heavy armour proficiency, which a Luminous Armour build never uses.
    - category: Oath
      picks: 1
      recommendation: Oath of Vengeance again — do NOT break it
      note: Re-select Vengeance so Inquisitor's Might, Hold Person and Misty Step all come back. There is no oath break anywhere in this plan.
    - category: Oath spells
      granted: true
      recommendation:
      - Bane
      - Hunter's Mark
      note: 'WHAT THE RESPEC COSTS HIM. Coming back at Paladin 4 he only re-earns the Paladin-3 oath grant, so Bane and Hunter''s Mark are free again but HOLD PERSON AND MISTY STEP ARE NOT — those need Paladin 5 and do not return until char 10. Bridge the gap with Hunger of Hadar or Bonbon''s Hold; do NOT spend one of the six Warlock picks to paper over two levels.'
    - category: Warlock feat
      picks: 1
      recommendation: Dual Wielder
      note: Required for Shadow Blade main hand + Phalar off-hand; GWM no longer applies and the respec removes it.
    - category: Paladin feat
      picks: 1
      recommendation: Savage Attacker
      note: The usual char-9 respec has levels for both feats. If the Stone lands at level 8, take Warlock 5 / Paladin 3 for Dual Wielder and add Paladin 4 / Savage Attacker next level.
    - category: Pact Boon
      picks: 1
      recommendation: Pact of the Blade
      note: A real three-way choice at Warlock 3 (Blade / Chain / Tome), and the prerequisite for Deepened Pact's extra attack.
    - category: Invocations
      picks: 3
      recommendation:
      - Devil's Sight
      - Agonising Blast
      - Repelling Blast
      note: 'THREE, not two — 2 at Warlock 2 plus 1 at Warlock 5. ⚠ Invocations cannot be swapped on level-up, so this respec is the only chance to set all three. Devil''s Sight is mandatory; the arrow-cloud plan runs on it. Repelling Blast turns Eldritch Blast into ledge control and shoves escapers back into Hunger of Hadar. AVOID Fiendish Vigour — its at-will False Life clashes with Armour of Agathys, because temp-HP sources never stack.'
    - category: Fighting style
      picks: 1
      recommendation: Defence (again)
      note: Re-chosen at Paladin 2 during the respec. Duelling still needs an empty off-hand and he now dual-wields; Great Weapon Fighting still needs a Two-Handed weapon and Shadow Blade is one-handed. Defence's +1 AC is the only style that functions.
    - category: Warlock cantrips
      picks: 3
      recommendation:
      - Eldritch Blast
      - Booming Blade
      - Mage Hand
      note: THREE cantrips at Warlock 5 (2 at W1, +1 at W4), all re-picked by the respec. Booming Blade is what triggers both the Ring of Arcane Synergy and the Battlemage's Power gloves.
    - category: Warlock spells
      picks: 6
      recommendation:
      - Shadow Blade
      - Counterspell
      - Armour of Agathys
      - Shield
      - Mirror Image
      - Hunger of Hadar
      note: 'SIX spells known at Warlock 5, and this list changed. ⚠ DARKNESS IS OUT — it competes with Hold Person for Concentration and the farmed arrows do the same job for free. ⚠ MISTY STEP IS OUT — it now arrives free as a Vengeance oath spell. Those two freed picks go to SHIELD and MIRROR IMAGE, both non-concentration defence, which is what a build locked to Luminous Armour at AC 17 actually needs. Hunger of Hadar stays as the non-humanoid Concentration alternative. Hex is dropped because Hold Person owns the slot permanently.'
    - category: Prepared spells
      picks: 8
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Compelled Duel
      - Protection from Evil and Good
      note: 'EIGHT prepared (Paladin 4 + CHA 4), and LEVEL 1 ONLY — Paladin 4 has no level-2 slots, so Aid is unavailable until char 10. Command is the one that actually gets cast, because it needs no Concentration and its DC rides the gloves'' Arcane Acuity. THREE SLOTS STAY OPEN: the level-1 leftovers (Divine Favour, Shield of Faith, Bless) are all Concentration and will never be cast over Hold Person, so prepare them only as day-to-day filler.'
  - char_level: 10
    class: Paladin 5
    gains:
    - Extra Attack (stacks with Deepened Pact outside Honour Mode for three attacks)
    - Level 2 Paladin spells
    recommendations:
    - category: Oath spells
      granted: true
      recommendation:
      - Hold Person
      - Misty Step
      note: 'Free and always prepared again at Paladin 5, which restores the nova setup the respec took away for two levels. Still no Warlock pick and still no prepared slot.'
    - category: Prepared spells
      picks: 10
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Compelled Duel
      - Protection from Evil and Good
      - Aid
      - Lesser Restoration
      note: 'TEN prepared (5 + CHA 5 once Mirror of Loss lands) and the level-2 list re-opens. Aid and Lesser Restoration are the two new ones; three slots stay open for situational picks. Aid is S tier and Charles is the party''s only source. Hold Person returns free here, restoring the nova setup the respec briefly took away.'
  - char_level: 11
    class: Paladin 6
    gains:
    - Aura of Protection
    recommendations:
    - category: Prepared spells
      picks: 11
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Compelled Duel
      - Protection from Evil and Good
      - Aid
      - Lesser Restoration
      - Protection from Poison
      note: 'ELEVEN prepared (6 + CHA 5) — Protection from Poison is the only addition worth naming, and three slots stay open. Aura of Protection returning matters twice over here: it protects the party''s saves and it props up the Hold Person concentration he carries under the Risky Ring.'
  - char_level: 12
    class: Paladin 7
    gains:
    - Relentless Avenger
    recommendations:
    - category: The Paladin 7 trade
      recommendation: Relentless Avenger, accepted in exchange for Inquisitor's Might
      note: 'Vengeance''s Paladin-7 feature is Relentless Avenger — hit with an Opportunity Attack and gain 4.5m movement next turn. It is weak, and it is the accepted price of keeping the oath: Oathbreaker''s Aura of Hate would have added +CHA to melee weapon damage, doubled by the Resonance Stone, for roughly +65 on a full nova. The trade is worth it because Inquisitor''s Might is the only non-concentration per-hit Radiant source that keeps Luminous Armour firing.'
    - category: Prepared spells
      picks: 12
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Compelled Duel
      - Protection from Evil and Good
      - Aid
      - Lesser Restoration
      - Protection from Poison
      - Divine Favour
      - Shield of Faith
      - Bless
      - Magic Weapon
      note: 'TWELVE prepared (7 + CHA 5) — 12 of the 16 Paladin spells that exist, so the list finally fills with nothing left open. The four left out are Searing Smite, Heroism, Cure Wounds and Branding Smite. ⚠ The last four ON the list are seat-fillers, not rotation: Divine Favour, Shield of Faith and Bless are Concentration and lose to Hold Person every time, and Magic Weapon is redundant with Bind Hexed Weapon — prepared spells cost nothing to hold, so they ride along. Four Vengeance oath spells (Bane, Hunter''s Mark, Hold Person, Misty Step) are free on top of the twelve.'
  itemization:
    act1:
    - id: early-hexed-weapon
      item: Early pact-bound weapon (temporary)
      wiki: false
      slot: weapons
      note: Before Phalar, bind the best main-hand weapon so it attacks with CHA. Hexblade can bind Two-Handed or Versatile — keep the off-hand empty so Versatile weapons use the larger die and later qualify for GWM.
    - id: phalar-aluve-two-handed
      item: Phalar Aluve
      tier: S
      tier_note: 'The BEST WEAPON TYPE in BG3 - Versatile Weapons Honor Mode Tier List and Guide - Act 1 (30:10) — one of the best weapons in the game even ignoring the strongest thing it does'
      slot: weapons
      bis: true
      note: ACT-1 DEFAULT from the Underdark. Bind as the Hexed Weapon, off-hand empty, so the Versatile longsword uses 1d10 and GWM All In adds +10 from char 6. Pre-cast Shriek and keep it equipped — the 6m aura covers Charles and Asterion.
    - id: haste-helm
      item: Haste Helm
      tier: S
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (27:11) — wanted somewhere in just about every party; it opens up combat options'
      rank: '#19'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #19 of 20 — three turns of Momentum at combat start decides whether a turn matters'
      slot: head
      note: 'ACT-1 HEAD, from the Moss-Covered Chest in the Blighted Village. Three turns of opening Momentum, and the Ring of Arcane Synergy keeps this slot free. ⚠ He keeps it rather than lending it out: he has the party''s worst initiative at d4+2 and the longest distance to close. ⚠ The GRYMSKULL HELM is NOT an option at any point — it requires Heavy Armour proficiency, which a Warlock-first medium-armour build never gets.'
    - id: luminous-armour
      item: Luminous Armour
      tier: S
      tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (22:22) — a game-winning armour; the list had no S tier until this item was given one'
      rank: '#2'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #2 of 20 — Radiating Shockwave stacks Radiating Orb across an encounter'
      slot: armour
      bis: true
      note: 'LOCKED CHEST FOR THE WHOLE RUN, from the Selûnite Outpost. Medium armour, AC 15 + DEX (max 2) = 17. Every point of Radiant damage he deals fires a RADIANT SHOCKWAVE, spreading Radiating Orb in a 3m radius: −1 to attack rolls per remaining turn, stacking duration on reapplication up to −10. He has exactly two Radiant sources feeding it — Inquisitor''s Might on every weapon hit, and Divine Smite — which is precisely why the oath is Vengeance and not Oathbreaker. ⚠ The accepted cost: no Adamantine Scale Mail crit immunity in Act 2 and no Helldusk Armour AC 21 in Act 3. Shield, Mirror Image, Helm of Balduran and Aura of Protection are the compensation.'
    - id: act1-hands-charles
      item: Glove slot
      slot: hands
      wiki: false
      note: 'A PLACEHOLDER BY DESIGN. His actual best-in-slot is the Gloves of Battlemage''s Power, and it does not exist until the Reithwin Tollhouse in Act 2, so nothing here is worth committing to. Take whichever of these the next fight wants.'
      options:
      - id: gloves-of-the-growling-underdog
        item: Gloves of the Growling Underdog
        tier: B
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (32:54) — advantage when surrounded is powerful but the positioning work is punishing'
        note: 'DEFAULT. Dror Ragzlin''s treasure room. Advantage on melee attacks when 2+ enemies stand within 3m of the target — a free advantage source before the Risky Ring, and while Vow of Enmity is still competing with Inquisitor''s Might for the single Channel Oath charge.'
      - id: opt-gloves-of-baneful-striking
        item: Gloves of Baneful Striking
        tier: A
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (18:20) — strong, but the character has to be built around them'
        note: 'Lady Esther, late Act 1. A weapon hit gives the target −1d4 to saving throws for 2 turns. Better than Growling Underdog on any turn the party needs a save to land — Asterion''s Stun, or his own Command.'
      - id: opt-gloves-of-power
        item: Gloves of Power
        tier: B
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (31:21) — swapped in and out around Sleight of Hand rather than worn full time'
        note: "Za'krug at the Grove gate. A branded wearer's hits inflict Absolute's Bane, −1d4 to attacks and saves. Weakest of the three in a fight, but free and early."
    - id: boots-of-striding
      item: Boots of Striding
      tier: A
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (16:09) — always worth looking at for the characters they suit'
      slot: feet
      bis: true
      note: 'SELECTED boots, worn by Minthara in the Shattered Sanctum. Concentrating grants Momentum and blocks Prone and forced movement — and Prone is the cheapest way a Paladin loses concentration. He is now ALWAYS concentrating (Hold Person), so this is live in every fight. ⚠ Boots of Stormy Clamour would chain Reverberation off his own Radiating Orb, but they stay on GALE, who applies conditions far more often. The same kill yields Gale''s Spidersilk Armour.'
    - id: amulet-of-misty-step
      item: Amulet of Misty Step
      tier: A
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (10:19) — awesome, because it patches a weakness a party may not otherwise cover'
      slot: amulets
      note: SELECTED neck from Priestess Gut's chambers. Misty Step 1/short rest solves approach and elevation before Paladin 5 grants the spell free. Asterion already has Monk movement and the Night Walkers.
    - id: ring-of-arcane-synergy
      item: Ring of Arcane Synergy
      tier: A
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (21:54) — an extremely powerful effect, but a better source of it exists for most builds'
      slot: ring 1
      note: 'Gish Far''aag, Crèche. Booming Blade damage → Arcane Synergy for 2 turns, adding CHA to subsequent weapon attacks. ⚠ Do not also give him Bonbon''s Diadem of Arcane Synergy — same condition, will not stack with itself.'
    - id: strange-conduit-ring
      item: Strange Conduit Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (44:11) — easy to keep active all the time, and it raises damage output dramatically'
      rank: '#5'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #5 of 20 — 1d4 psychic on every weapon attack while concentrating'
      slot: ring 2
      bis: true
      note: '+1d4 Psychic on weapon attacks while Concentrating (Crèche), rated #5 of the 20 best Act 1 items for exactly this kind of multiattacking concentrator. It used to depend on him holding Hex or Bless inside an arrow cloud; now that HOLD PERSON is his permanent Concentration it is simply always on, and the Resonance Stone later doubles the rider. ⚠ Per the wiki it covers melee, ranged and Thrown but NOT Unarmed Strike, which is why it can never move to Asterion.'
    - id: arrows-of-darkness
      item: Arrows of Darkness
      tier: S
      tier_note: 'ZMCimWeIxCk (28:35) — PLACED IN S+ TIER: concentration-free Darkness cast as an attack; only S tier without warlocks or blind-immunity gear'
      wiki: Arrow of Darkness
      slot: consumables
      bis: true
      note: 'THE DARKNESS SOURCE FOR THE ENTIRE RUN, not just Act 1. 3m cloud, 3 turns, NO Concentration — which is the whole point, because Hold Person owns his Concentration permanently and the Darkness spell was therefore dropped from his Warlock picks. Devil''s Sight does not care what made the cloud. Prefer Bonbon placing it; if Charles fires it, do so before switching to Phalar and activating Shriek. Keep restocking from arrow vendors in every act.'
    - id: dual-hand-crossbows-plus-one
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      slot: ranged weapons
      note: 'ACT 1–2 RANGED, a pair, and mainly a Darkness-Arrow launcher. Farm Dammon, Roah, Derryth and Jeera for +1 copies; the ranged set does not interfere with two-handed Phalar. ⚠ Keep expectations low — once he stands inside his own cloud it blocks ranged attacks into and out of itself. Hellrider''s Longbow replaces these in Act 3.'
    - id: auntie-ethel-s-hair-cha-17-18
      item: Auntie Ethel's Hair
      slot: consumables
      note: CHARISMA 17 → 18. Raises Aura DCs, attack and smite accuracy, Inquisitor's Might's radiant rider, the Hold Person DC, and his prepared-spell count.
    - id: act1-cloak-charles
      item: No cloak exists yet
      slot: cloaks
      note: 'Deliberately empty, not an oversight. The Deathstalker Mantle is the only magical cloak obtainable in Act 1 and it goes to Asterion; every other cloak in the game first appears in Act 2 or Act 3. Charles goes bare-shouldered until Quartermaster Talli at Last Light.'
    act2:
    - id: self-cast-shadow-blade-upcast-to-3d8
      item: Shadow Blade
      wiki: Shadow Blade (weapon)
      slot: weapons
      bis: true
      note: 'POST-RESONANCE DEFAULT. Keep two-handed Phalar/GWM until the late-Act-2 Stone pickup. Warlock 5 brings level-3 pact slots — summon a 3d8 Shadow Blade and bind THIS main hand to CHA so Deepened Pact applies, leaving Phalar unbound off-hand. Costs no Concentration, which is why it suits a build whose Concentration is committed. ⚠ Against Psychic-immune targets, bind Phalar main hand instead.'
    - id: phalar-aluve-offhand
      item: Phalar Aluve
      tier: S
      tier_note: 'The BEST WEAPON TYPE in BG3 - Versatile Weapons Honor Mode Tier List and Guide - Act 1 (30:10) — one of the best weapons in the game even ignoring the strongest thing it does'
      slot: weapons
      bis: true
      note: 'PARTY-DAMAGE DEFAULT after the Stone. Dual Wielder replaces GWM so Phalar sits beside the Light Shadow Blade, +1 AC. Pre-cast Shriek and keep Charles and Asterion inside its 6m aura (the Stone reaches 9m). Shriek fires 1d4 Thunder per qualifying party damage instance and −1d4 to enemy attacks and all saves, with no save and no Concentration — worth more than a personal-DPR off-hand. Phalar is unbound and he lacks Two-Weapon Fighting, so its bonus-action swing is last priority.'
    - id: gloves-of-battlemage-s-power
      item: Gloves of Battlemage's Power
      tier: A
      tier_note: 'The BEST GLOVES In Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (18:12) — A on the list''s own terms: he says A tier if the Arcane Acuity effect worked, and placed it in D only because it was bugged when he recorded. This run treats the effect as working, so the A stands'
      slot: hands
      bis: true
      note: 'THE ACUITY ENGINE, and a locked slot from the moment it is found: Reithwin Tollhouse, locked opulent chest on the second floor, in the room with two locked doors. Hitting with a spell or cantrip that uses a weapon grants ARCANE ACUITY — +1 spell attack roll and +1 SPELL SAVE DC per remaining turn, up to +10. The confirmed triggers are every Shadow Blade weapon attack, Booming Blade, any smite spell, and Divine Smite — and a smite spell chaining into a Divine Smite reaction triggers it TWICE. This is what makes HOLD PERSON land, and Command with it, and it is why Charles has the party''s best save DC before Bonbon''s Helmet of Arcane Acuity arrives. ⚠ Acuity duration drops by 2 every time he takes damage, so build stacks and cast Hold Person before the enemy''s turn. ⚠ The accepted cost is the whole rest of the glove progression: Baneful Striking, Helldusk Gloves and Craterflesh Gloves (roughly +49 on a full nova, Bhaal path) are all forgone.'
    - id: act2-armour-charles
      item: Luminous Armour
      tier: S
      tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (22:22) — a game-winning armour; the list had no S tier until this item was given one'
      rank: '#2'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #2 of 20 — Radiating Shockwave stacks Radiating Orb across an encounter'
      held: 1
      slot: armour
      bis: true
      note: 'CARRIED OVER — locked. Adamantine Scale Mail is the item this displaces, and its crit immunity was protecting concentration, so the Helm of Balduran becomes the plan for getting that back in Act 3. The Splint mould and both Mithral ores now go elsewhere.'
    - id: act2-head-charles
      item: Covert Cowl
      tier: A
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (17:07) — shows up in a lot of builds, though some versions of them want something else'
      wiki: Covert Cowl
      slot: head
      note: 'ACT-2 HEAD, from Last Light. −1 crit threshold while Obscured — and standing inside an arrow cloud is Heavily Obscured, so it is live on every turn he plays the cloud correctly. Requires Light Armour proficiency, which medium-armour characters inherit. ⚠ Illegal on Asterion, whose Unarmoured Defence breaks on any helmet marked as armour, so there is no contest.'
    - id: act2-feet-charles
      item: Boots of Striding
      tier: A
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (16:09) — always worth looking at for the characters they suit'
      held: 1
      slot: feet
      note: CARRIED OVER. Momentum and immunity to Prone and forced movement, live in every fight now that Hold Person keeps him permanently concentrating. Helldusk Boots replace them in Act 3.
    - id: act2-amulet-charles
      item: Neck slot
      slot: amulets
      wiki: false
      note: 'GENUINELY OPEN IN ACT 2. The Amulet of Misty Step was carrying this slot, and Paladin 5 hands him Misty Step free as a Vengeance oath spell, so its whole reason for being there is gone. Nothing in the Act 2 pool is clearly best for him and the Amulet of Greater Health in Act 3 is the real answer, so treat this as a parking space.'
      options:
      - id: amulet-of-misty-step-act2
        item: Amulet of Misty Step
        tier: A
        tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (10:19) — awesome, because it patches a weakness a party may not otherwise cover'
        held: true
        note: 'Simply keeping it costs nothing, and a second Misty Step per short rest is still a second escape.'
      - id: opt-spineshudder-amulet-charles
        item: Spineshudder Amulet
        tier: S
        tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:42) — busted on multi-hit spells'
        note: 'Applies Reverberation when he is hit. He is the frontliner who gets hit most, so it turns incoming attacks into a stacking enemy debuff — but Gale wants it too.'
      - id: opt-amulet-of-restoration
        item: Amulet of Restoration
        tier: S
        tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (23:45) — some character should have this equipped'
        note: 'Derryth Bonecloak, Underdark. Grants Healing Word and Mass Healing Word once each per long rest. It needs no class access, so on him it is a free party-wide heal — and a Whispering Promise trigger if anyone is wearing one.'
    - id: risky-ring
      item: Risky Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:21) — too good to leave at home, given a way to cover the saving-throw downside'
      slot: ring 1
      bis: true
      note: 'Moonrise, from Araj Oblodra. Advantage on ALL attacks, disadvantage on saves — the crit-fishing engine, and it replaces the Ring of Arcane Synergy. It also makes Vow of Enmity redundant, which is what frees the Channel Oath charge for Inquisitor''s Might every fight. ⚠ Be honest about the cost: disadvantage on saves roughly squares his concentration-failure rate, and he is now ALWAYS holding Hold Person. Mitigate in order — Aura of Protection at Paladin 6, the Cloak of Protection below, Helm of Balduran''s crit immunity in Act 3, and the Amulet of Greater Health, which cancels the disadvantage on Constitution saves outright.'
    - id: act2-ring2-charles
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'A REAL CHOICE, not a default. Risky Ring owns the first slot; this one swings on whether the fight has kills to bank. Both candidates are strong and neither is wrong.'
      options:
      - id: killer-s-sweetheart
        item: Killer's Sweetheart
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (14:36) — very good for builds rolling a lot of damage dice, but only one encounter per day'
        note: 'Gauntlet of Shar, Self-Same Trial — on the ground where your shadow copy dies. Your first attack after a kill is a GUARANTEED crit, which is a free doubled smite every fight. Set it to Ask in the Reactions tab and bank it for the biggest slot. WARNING weapon attack rolls only. Best in fights with adds to kill first.'
      - id: opt-strange-conduit-act2
        item: Strange Conduit Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (44:11) — easy to keep active all the time, and it raises damage output dramatically'
        rank: '#5'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #5 of 20 — 1d4 psychic on every weapon attack while concentrating'
        note: 'Now that Hold Person guarantees he is always Concentrating, its +1d4 Psychic is live on every single swing and the Resonance Stone doubles it. Across a seven-attack nova that beats one banked crit, so prefer it in long boss fights with nothing to kill early.'
    - id: shadow-blade-ring
      item: Shadow Blade Ring
      tier: B
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (36:56) — better for builds that hold concentration easily; narrower otherwise'
      slot: other
      note: 'NOT a third ring. As of Patch 8 the ring''s Shadow Blade needs no concentration and lasts until long rest, and the wiki states the ring can be unequipped after summoning. Summon, unequip, put Risky Ring and Killer''s Sweetheart back on. Carry it as insurance for any fight where he cannot spend a pact slot on his own blade.'
    - id: cloak-of-protection
      item: Cloak of Protection
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (13:30) — excellent, and someone in the party will almost certainly be wearing it'
      slot: cloaks
      bis: true
      note: 'HIS, not Gale''s. Quartermaster Talli at Last Light Inn. +1 Armour Class and +1 to Saving Throws. ⚠ THE ARBITRATION: exactly one exists, and it is the only cloak in the Act 2 pool that touches saving throws. Charles carries a permanent self-inflicted DISADVANTAGE on every save (Risky Ring) while holding the party''s Hold Person, and he stands in every area attack. Gale can be positioned out of danger and has Constitution-save advantage from Spidersilk plus save proficiency; Bonbon has War Caster and AC 18.'
    - id: act2-ranged-charles
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      held: 1
      slot: ranged weapons
      note: CARRIED OVER as the Darkness-Arrow launcher, still a pair. Still close to a dead slot on any turn he is standing in his own cloud, which is most of them.
    - id: resonance-stone-aura
      item: Resonance Stone
      slot: other
      note: 'LATE ACT 2, Mind Flayer Colony — this pickup triggers the weapon respec. The 9m Steeped in Bliss aura makes eligible creatures Psychic-vulnerable, doubling Shadow Blade and Strange Conduit. ⚠ No effect on Undead or Constructs, and it also gives ALLIES Psychic Vulnerability plus disadvantage on mental saves — which is a real cost on a party whose Hold Person concentration matters. Asterion carries it within 9m of Charles, closing to 6m when both need Shriek; holster it against Psychic attackers and dangerous mental-save effects, and expect it to stop working once Act 2 ends.'
    act3:
    - id: shadow-blade-phalar-act3-default
      item: Shadow Blade
      held: 2
      wiki: Shadow Blade (weapon)
      slot: weapons
      bis: true
      note: 'CARRIED OVER unchanged — a 3d8 Shadow Blade in the main hand, bound for CHA and Deepened Pact, with Phalar Aluve off-hand for pre-cast Shriek, bonus-action swing only when free. Beats Render of Mind and Body or the Knife of the Undermountain King because the party generates so many Shriek triggers. ⚠ Against Psychic-immune targets, bind Phalar main hand. ⚠ Confirm the Stone aura still works after Act 2, and holster it when the Psychic and mental-save downside is unsafe.'
    - id: act3-head-charles
      item: Helm of Balduran
      tier: S
      tier_note: 'Is EVERY Act 3 Helmet Awesome? - BG3 Helmets Tier List and Guide - Act 3 (17:36) — purely defensive, yet any character wanting a defensive option wants this'
      slot: head
      bis: true
      note: 'SELECTED ACT-3 HEAD, from the Wyrmway (Ansur). Attackers cannot land critical hits, +1 AC, +1 to SAVING THROWS, 2 HP per turn and Stun immunity. Requires Medium armour proficiency, which he has. ⚠ This is now the ONLY crit-immunity source left to him, because locking Luminous Armour gave up Adamantine Scale Mail — and a critical hit roughly doubles the concentration save DC on the Hold Person he carries under the Risky Ring. That is why it beats Sarevok''s Horned Helmet, which offers more crits but no protection for the concentration the whole nova depends on.'
    - id: act3-armour-charles
      item: Luminous Armour
      tier: S
      tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (22:22) — a game-winning armour; the list had no S tier until this item was given one'
      rank: '#2'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #2 of 20 — Radiating Shockwave stacks Radiating Orb across an encounter'
      held: 1
      slot: armour
      bis: true
      note: 'CARRIED OVER — locked for the whole run. This is where the cost is largest: Helldusk Armour would have given AC 21 flat and −3 to all incoming damage, and he gives that up to keep the Radiant Shockwave engine. Helm of Balduran, Shield, Mirror Image and Aura of Protection carry the defensive load instead.'
    - id: act3-hands-charles
      item: Gloves of Battlemage's Power
      tier: A
      tier_note: 'The BEST GLOVES In Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (18:12) — A on the list''s own terms: he says A tier if the Arcane Acuity effect worked, and placed it in D only because it was bugged when he recorded. This run treats the effect as working, so the A stands'
      held: 2
      slot: hands
      bis: true
      note: 'CARRIED OVER — locked. This is the other place the lock costs real damage: Helldusk Gloves (+1d6 Fire per hit, roughly +17 a nova, plus a wiki-confirmed +1 to all attack rolls) and Craterflesh Gloves (+2d6 Force on a crit, roughly +49 on a full auto-crit nova, Bhaal path only) are both forgone. Accepted, because Arcane Acuity is what makes Hold Person land and Hold Person is what makes every swing a crit.'
    - id: act3-feet-charles
      item: Helldusk Boots
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (1:00:13) — the saving throw makes the wearer extremely safe in almost every circumstance'
      slot: feet
      bis: true
      note: 'ACT-3 BOOTS, in a locked Gilded Chest on the top floor of Wyrm''s Rock Fortress. Steadfast stops all forced movement and difficult terrain — replacing Boots of Striding — and Infernal Evasion lets him use his REACTION TO TURN A FAILED SAVING THROW INTO A SUCCESS. That is the direct answer to the Risky Ring on the character holding the party''s Hold Person. ⚠ Contested with Gale, who cannot wear Boots of Persistence at all; Charles wins because he is the one with save disadvantage.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 3 (13:32) — the only real decision left is who to put it on'
      slot: amulets
      bis: true
      note: 'ACT-3 NECK, on the leftmost pedestal in the House of Hope Archive. Sets Constitution to 23 and grants ADVANTAGE ON CONSTITUTION SAVING THROWS. Both halves matter only here: +6 to concentration checks, and the advantage cancels the Risky Ring''s disadvantage so those rolls go back to a straight d20. On a build whose entire nova rests on keeping Hold Person up, this is the single most important Act 3 pickup. ⚠ Contested with Gale — Charles wins because Armour of Landfall already gives Gale that advantage. Steal tip: DC 20 Sleight of Hand if the Orphic Hammer, the Soul-Sworn Contract and Hope are left alone — an Asterion job.'
    - id: act3-ring1-charles
      item: Risky Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:21) — too good to leave at home, given a way to cover the saving-throw downside'
      held: 2
      slot: ring 1
      bis: true
      note: 'CARRIED OVER. Advantage on every attack roll is the largest crit-rate multiplier available and the engine of the build, so it keeps the slot. The save penalty is now fully answered by the Amulet of Greater Health and Helldusk Boots.'
    - id: act3-ring2-charles
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'Same choice as Act 2, and still genuinely open. Bank a crit or ride a permanent psychic rider.'
      options:
      - id: opt-killers-sweetheart-act3
        item: Killer's Sweetheart
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (14:36) — very good for builds rolling a lot of damage dice, but only one encounter per day'
        note: 'One guaranteed critical hit after a kill. Bank it for the largest Divine Smite, since a crit doubles every smite die. Weapon attack rolls only.'
      - id: opt-strange-conduit-act3
        item: Strange Conduit Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (44:11) — easy to keep active all the time, and it raises damage output dramatically'
        rank: '#5'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #5 of 20 — 1d4 psychic on every weapon attack while concentrating'
        note: 'Hold Person guarantees he is always Concentrating, so its +1d4 Psychic is live on every swing and the Resonance Stone doubles it. Across a seven-attack nova this beats one banked crit in long fights.'
      - id: opt-callous-glow-ring-charles
        item: Callous Glow Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
        note: '+2 Radiant per hit against ILLUMINATED targets — and Radiant would feed Luminous Armour. The catch is it needs light, which fights his own darkness, and it is currently Gale''s.'
    - id: act3-cloak-charles
      item: Cloak of Protection
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (13:30) — excellent, and someone in the party will almost certainly be wearing it'
      held: 2
      slot: cloaks
      bis: true
      note: 'CARRIED OVER. Flat +1 AC and +1 saves never stops applying, and on the character with save disadvantage holding the party''s Hold Person it beats the conditional Act 3 cloaks. ⚠ Cloak of Displacement goes to Asterion. ⚠ Mantle of the Holy Warrior is a trap here — Crusader''s Mantle is CONCENTRATION, so it would evict Hold Person.'
    - id: act3-ranged-charles
      item: Hellrider's Longbow
      wiki: Hellrider Longbow
      slot: ranged weapons
      bis: true
      note: 'ACT-3 RANGED, from Rivington, and the fix for the build''s one structural weakness. Passive +3 INITIATIVE in a slot that is otherwise a formality — a Darkness cloud blocks ranged attacks into and out of itself, so he cannot shoot out of it anyway. He has the party''s worst initiative at d4+2, so +3 is close to doubling it, and going first is what lets him build Acuity and land Hold Person before the enemy acts. ⚠ Bonbon lists this only as an initiative alternative and stays on hand crossbows for her Acuity engine, so there is no real contest.'
    - id: bhaalist-armour-unlock
      item: Bhaalist Armour
      tier: S
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (42:20) — piercing vulnerability aura breaks the game; LOCKED BEHIND A STORY EVENT, SOME RUNS ONLY'
      slot: other
      note: 'Sold by the Echo of Abazigal, and Charles as the Dark Urge unlocks the Murder Tribunal stock. Aura of Murder makes enemies within 3m Vulnerable to PIERCING. ⚠ NOT WORN — none of his damage is Piercing (Shadow Blade is Psychic, Phalar is Slashing, Divine Smite is Radiant), it would buff nobody, and the chest slot is locked to Luminous Armour anyway. Buy it on the Bhaal path for completeness and leave it in the chest.'
    progression:
    - id: prog-head
      item: 'Head: Haste Helm → Covert Cowl → Helm of Balduran'
      slot: head
      note: 'Act 1 Haste Helm (Blighted Village) → Act 2 Covert Cowl (Last Light) → Act 3 Helm of Balduran (Ansur). Momentum while he is slow and far away, then crit-threshold reduction once he lives inside a cloud, then crit IMMUNITY — which is the only way back to the protection Adamantine Scale Mail would have given. ⚠ Grymskull Helm is illegal all run: Heavy Armour proficiency.'
    - id: prog-armour
      item: 'Chest: Luminous Armour, all three acts (LOCKED)'
      slot: armour
      note: One chest for the whole run. Radiant Shockwave is the engine, fed by Inquisitor's Might on every hit and by Divine Smite. Forgoes Adamantine Scale Mail's crit immunity and Helldusk Armour's AC 21 and −3 damage.
    - id: prog-hands
      item: 'Hands: Gloves of the Growling Underdog → Gloves of Battlemage''s Power (LOCKED from Act 2)'
      slot: hands
      note: Act 1 Growling Underdog (Dror Ragzlin) as a pure stopgap advantage source → Act 2 and Act 3 Gloves of Battlemage's Power (Reithwin Tollhouse), which never come off. Forgoes Baneful Striking, Helldusk Gloves and Craterflesh Gloves.
    - id: prog-feet
      item: 'Boots: Boots of Striding → Helldusk Boots'
      slot: feet
      note: Act 1–2 Striding (Minthara) → Act 3 Helldusk Boots (Wyrm's Rock). Both protect the Hold Person concentration; Helldusk does it better, turning one failed save per turn into a success. Boots of Stormy Clamour stay on Gale.
    - id: prog-cloaks
      item: 'Cloak: none available → Cloak of Protection'
      slot: cloaks
      note: Empty through Act 1 because the only Act 1 magical cloak is the Dark Urge Mantle he hands to Asterion. Cloak of Protection (Talli) from Act 2 onward — the only Act 2 cloak that touches saving throws, which is exactly what the Risky Ring costs him.
    - id: prog-amulets
      item: 'Amulet: Amulet of Misty Step → Amulet of Greater Health'
      slot: amulets
      note: Act 1–2 Misty Step (Priestess Gut), lower value once Paladin 5 grants the spell free → Act 3 Greater Health (House of Hope Archive), which is what makes the Risky Ring safe on a permanent concentrator.
    - id: prog-ring1
      item: 'Ring 1: Ring of Arcane Synergy → Risky Ring'
      slot: ring 1
      note: Ring of Arcane Synergy in Act 1, adding his Charisma modifier to weapon damage once he lands a condition → Risky Ring from Act 2, which is permanent advantage on attack rolls at the cost of saving throws his Paladin aura is best placed in the party to absorb.
    - id: prog-ring2
      item: 'Ring 2: Strange Conduit Ring → Killer''s Sweetheart'
      slot: ring 2
      note: Strange Conduit Ring while he is holding Concentration on Hold Person, which is nearly every fight → Killer's Sweetheart from Act 2 for a guaranteed critical once per fight, with Strange Conduit kept as the long-fight swap.
      slot: rings
      note: Act 1 Arcane Synergy and Strange Conduit (both Crèche) → Act 2–3 Risky Ring (Araj) and Killer's Sweetheart (Self-Same Trial). Strange Conduit is a live alternative all run, because Hold Person guarantees he is always Concentrating. The Shadow Blade Ring needs no slot — summon, then unequip.
    - id: prog-weapons
      item: 'Melee: bound weapon → two-handed Phalar Aluve + GWM → 3d8 Shadow Blade + Phalar off-hand'
      slot: weapons
      note: The build's one real respec. Two-handed Phalar with Great Weapon Master carries Act 1 through most of Act 2; the late-Act-2 Resonance Stone triggers the swap to Dual Wielder, Shadow Blade main hand and Phalar off-hand for Shriek.
    - id: prog-ranged
      item: 'Ranged: Dual Hand Crossbows +1 → Hellrider''s Longbow'
      slot: ranged weapons
      note: Acts 1–2 the crossbows exist to launch Darkness Arrows. Act 3 Hellrider's Longbow (Rivington) converts a dead slot into +3 initiative, which is the build's one real structural weakness.
    - id: prog-consumables
      item: 'Consumables: Arrows of Darkness, all three acts'
      slot: consumables
      note: NOT a stopgap. Because Hold Person owns his Concentration permanently, the Darkness spell was dropped from his Warlock picks and farmed arrows are the darkness source for the entire run. Keep restocking. Auntie Ethel's Hair takes CHA to 18 in Act 1.
  playstyle: |-
    - **The one-line version:** stand in an arrow cloud, spend the Channel Oath charge on Inquisitor's Might, build Arcane Acuity with a Booming Blade, Hold Person the priority target, then dump smites into a body that auto-crits.
    - **Concentration is Hold Person and nothing else.** Bless, Hex, Divine Favour, Darkness, Wrathful Smite and Branding Smite are all Concentration and all out. Asterion supplies Bless off the Staff of Arcane Blessing; darkness comes from farmed arrows, which cost nothing to hold. The only time he concentrates on something else is a non-humanoid fight, where Hunger of Hadar replaces Hold Person and Bonbon attempts Hold Monster.
    - **Act 1 turn structure:** pre-cast Shriek from stealth → open with **Inquisitor's Might** as the bonus action (+CHA radiant on every weapon hit for 2 turns, plus a no-save Daze) → Booming Blade or a Phalar swing → smite only on crits. Hexblade's Curse goes on turn 2, since it competes with Inquisitor's Might for the bonus action.
    - **One Channel Oath charge per short rest.** In Act 1 that is a real choice: Vow of Enmity for a long boss fight, Inquisitor's Might otherwise. From Act 2 the Risky Ring supplies advantage on every attack, so Inquisitor's Might becomes the automatic answer and stays that way.
    - **Radiant is the debuff engine, not just damage.** Every point of Radiant he deals fires Luminous Armour's Radiant Shockwave, stacking Radiating Orb on everything within 3m at −1 attack per remaining turn, up to −10. Inquisitor's Might on every hit plus Divine Smite is the whole supply, which is why the oath is never broken.
    - **Acuity sequencing matters.** Arcane Acuity builds off hits and decays by 2 every time he takes damage, so land a Booming Blade or a smite BEFORE casting Hold Person, and cast it before the enemy's turn. **Gale always Hastes Charles and Bonbon**, and the extra action is what lets him build stacks and Hold in the same turn.
    - **Darkness placement:** put the cloud so **Charles is inside it and his target is not**. He is an unseen attacker — advantage in, disadvantage out — while the enemy stays visible for Gale. A cloud blocks ranged attacks *into and out of* itself, so an enemy standing inside it is one Gale cannot touch.
    - **Pre-cast Shriek for Gale, not just yourself:** Shriek adds 1d4 Thunder every time an affected enemy takes damage, and Scorching Ray damages 3–7 separate times per cast. Activating it before Gale's turn is worth roughly 7d4 on a single level-6 cast.
    - **Late Act 2+ — Shadow + Stone:** on acquiring the Resonance Stone, respec at character level 9 to Warlock 5 / Paladin 4, replace GWM with Dual Wielder, summon 3d8 Shadow Blade main hand and off-hand Phalar. Asterion carries the Stone within 9m. Re-select Oath of Vengeance; do not break it.
    - **Once per long rest, out of combat:** cast **Aid** (upcast as high as you can spare) for a permanent party-wide max-HP buff that costs no concentration. Charles is the party's only Aid source.
    - **Nova:** Hold a humanoid, then spend the largest Divine Smites first into guaranteed crits. At Paladin 5 after the respec, two three-attack Actions under Haste plus one Phalar off-hand swing reach seven auto-crit attacks when the bonus action is free.
    - **Defensive reads:** he is AC 17–18 for the whole run with no crit immunity until Act 3. Pre-cast Mirror Image in fights where he expects to be focused, keep Shield for the reaction that would otherwise break Hold Person, and stay inside Aura of Protection range of the party rather than running ahead.
---
