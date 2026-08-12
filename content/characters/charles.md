---
nickname: Charles
builds:
- name: The Three Booms
  is_primary: true
  role: Melee crit-smite nova frontline
  class: Oathbreaker Paladin 7 / Hexblade Warlock 5
  race: Half-Orc (Dark Urge origin)
  race_notes: Savage Attacks (extra weapon die on melee crits); Relentless Endurance; origin char → Hag's Hair priority.
  background: Haunted One (Medicine, Intimidation) — the fixed Dark Urge background
  starting_stats:
    STR: 8
    DEX: 14
    CON: 16
    INT: 8
    WIS: 10
    CHA: 17
  stats_note: 'Point-buy base 8/14/15/8/10/15 = all 27 (CON 15 + CHA 15 cost 9 each). Half-Orc +2 → CHA 17, +1 → CON 16 (+3). Fully spent — no leftovers.'
  ability_targets: CHA 17 → 18 (Hag's Hair) → 20 (Mirror of Loss); CON stays 16.
  feats:
  - at: Act 1 char 6 (Paladin 4)
    feat: Great Weapon Master (temporary)
    note: 'Phalar Aluve is Versatile, so its two-handed attacks qualify for All In''s −5 attack/+10 damage. Darkness-Arrow advantage offsets the penalty. Replace this feat during the Resonance Stone respec.'
  - at: Late Act 2 Resonance Stone respec (Warlock 4 feat; usually char 9)
    feat: Dual Wielder
    note: 'Replaces Great Weapon Master. Required to keep 3d8 Shadow Blade main hand with Versatile Phalar Aluve off-hand; also grants +1 AC.'
  - at: Late Act 2 Resonance Stone respec (Paladin 4 feat; usually char 9)
    feat: Savage Attacker
    note: Rerolls Shadow Blade, Phalar Aluve, and Divine Smite damage dice; the off-hand Phalar attack supplies the bonus-action seventh swing when available.
  weapon_plan: 'ACT 1 through most of ACT 2: bind and two-hand Phalar Aluve with Great Weapon Master, using Darkness Arrows for Devil''s Sight advantage. LATE ACT 2 after acquiring the Resonance Stone: usually respec at character level 9 to Warlock 5 / Paladin 4, replace GWM with Dual Wielder, and use 3d8 Shadow Blade main hand + Phalar off-hand inside the Stone''s psychic-vulnerability aura.'
  creation:
    level1_class: Warlock 1 (Hexblade patron)
    level1_gains: Pact Magic (1 × L1 short-rest slot), Hexblade's Curse (bonus action), Bind Hexed Weapon (attack with CHA). Pact Boon (Pact of the Blade) is not until Warlock 3.
    subclass_choice: Hexblade patron (Warlock 1)
    proficiencies:
      armor_weapons: 'Medium armour + shields + martial (Hexblade, Warlock 1). Multiclassing into Paladin does not grant heavy-armour proficiency; use medium armour or self-proficient Helldusk Armour.'
      saving_throws: WIS + CHA (Warlock).
      skills: 2 Warlock picks + Haunted One (Medicine, Intimidation).
    starting_cantrips: 2 known at Warlock 1 — take Eldritch Blast + Booming Blade.
    starting_spells: Take Hex + Armour of Agathys; the Hexblade L1 expanded package adds Shield and Wrathful Smite.
    notes: 'ACT 1 deliberately stops Warlock at 2: Hexblade supplies CHA weapon binding and Devil''s Sight, while Paladin 1–5 delivers Divine Smite at character level 4, the temporary Great Weapon Master feat at 6, and Extra Attack at 7. Continue Paladin 6 for Aura of Protection if character level 8 arrives before the late-Act-2 Resonance Stone. Bind two-handed Phalar Aluve and use farmed Darkness Arrows instead of learning Darkness. Keep the Paladin oath intact until the Stone respec to avoid paying the Oathbreaker Knight before Withers will help; after respeccing, break the oath and remain Oathbreaker.'
  spells:
    note: 'Charles is a smite platform, not a spell-slinger. In Act 1, concentration-free Darkness Arrows let him maintain Hex, Bless, or Divine Favour while fighting with two-handed Phalar. After the Resonance Stone respec, self-cast Darkness and 3d8 Shadow Blade become the default psychic package.'
    mandatory:
    - spell: Divine Smite
      level: Feature (Paladin 2)
      school: Class feature — Radiant
      save: None (melee weapon attack roll)
      when: char 4
      why: 'The build''s core. Expend any slot on a melee hit: 2d8 Radiant at L1, +1d8 per slot level above 1st (cap 5d8 at an L4 slot), +1d8 vs Fiends/Undead; dice DOUBLE on a crit. Not a prepared spell and not stopped by Counterspell — set the Critical-Hit Divine Smite reactions to auto-confirm.'
    - spell: Shadow Blade
      level: '2'
      guide_level: 9
      school: Illusion
      save: None (bonus action to summon)
      when: Late Act 2 Resonance Stone respec (Warlock 5, usually char 9)
      why: 'POST-STONE core weapon, not an Act-1 pick. The respec immediately supplies level-3 pact slots, so self-cast Shadow Blade starts at 3d8 Psychic, lasts until long rest without concentration, and uses CHA after binding. Asterion carries the nearby Resonance Stone to double its Psychic damage; Devil''s Sight + self-cast Darkness supplies advantage and defence.'
    - spell: Wrathful Smite
      level: '1'
      guide_level: 1
      school: Evocation
      save: WIS save (to avoid Frightened)
      when: char 1 (Hexblade) / char 4 (Paladin 2)
      why: 'Adds 1d6 psychic to one weapon hit and can Frighten. It can coexist with concentration-free Darkness Arrows in Act 1, but after the respec it competes with self-cast Darkness.'
    recommended:
    - spell: Hex
      level: '1'
      guide_level: 1
      school: Enchantment
      save: None (rider on each hit)
      when: char 1 (Warlock 1)
      why: '+1d6 Necrotic per hit plus disadvantage on a chosen ability. In Act 1 it can run inside concentration-free Arrow darkness and activate Strange Conduit Ring; after the respec it competes with self-cast Darkness.'
    - spell: Shield
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None (reaction, +5 AC)
      when: char 1 (Hexblade L1 expanded)
      why: Reaction +5 AC to dodge an incoming hit; not concentration; strong survival pick for a melee body.
    - spell: Armour of Agathys
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None
      when: char 1–6
      why: Temp HP + Cold retaliation that scales with the pact slot — 15 temp HP / 15 Cold from a Warlock-5 L3 pact slot. Not concentration.
    - spell: Bless
      level: '1'
      guide_level: 4
      school: Enchantment
      save: None (concentration)
      when: char 4 (Paladin 2)
      why: '+1d4 to attack rolls and saves for up to 3 allies. It offsets Great Weapon Master in Act 1 and can run inside concentration-free Arrow darkness.'
    - spell: Divine Favour
      level: '1'
      guide_level: 4
      school: Evocation
      save: None (concentration)
      when: char 4 (Paladin 2)
      why: 'Adds 1d4 Radiant to every Phalar hit for 3 turns. Arrow-created Darkness does not require concentration, so this is the Act-1 personal-damage option when Bless is supplied elsewhere.'
    - spell: Command
      level: '1'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: char 4 (Paladin 2)
      why: Cheap single-target control (Drop / Halt / Approach) to open a nova or peel an enemy caster.
    - spell: Hellish Rebuke
      level: '1'
      guide_level: 2
      school: Evocation
      save: DEX save (half on save)
      when: char 2 (Warlock pick) / post-respec Oathbreaker oath spell
      why: Reaction fire damage when hit. It can be replaced during the Warlock progression, then returns as a free always-prepared Oathbreaker spell.
    - spell: Darkness
      level: '2'
      guide_level: 9
      school: Evocation
      save: None (Concentration)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'POST-STONE default concentration spell. Enemies that cannot see through it are Blinded, attack Charles with disadvantage, and grant him advantage through Devil''s Sight. It powers Strange Conduit Ring but excludes Hex, Bless, Divine Favour, and the smite spells. Act 1 uses concentration-free Darkness Arrows instead.'
    - spell: Misty Step
      level: '2'
      guide_level: 9
      school: Conjuration
      save: None (bonus action)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Bonus-action mobility for reaching a priority target, crossing hazards, or escaping a bad melee position.
    - spell: Counterspell
      level: '3'
      guide_level: 9
      school: Abjuration
      save: Reaction
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Pact-slot reaction defence for enemy spells dangerous enough to justify delaying a Smite or Shadow Blade recast.
    - spell: Spiteful Suffering
      level: Channel Oath (not a spell)
      school: Oathbreaker Channel Oath — Necrotic
      save: CHA save
      when: immediately after the Act 2 respec and oath break (Paladin 3)
      why: 1d4+CHA Necrotic/turn AND grants all attackers Advantage on the target — a self-contained advantage/crit-fishing source when the Risky Ring isn't equipped.
    - spell: Eldritch Blast
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: char 1 (Warlock 1)
      why: Ranged fallback for turns he can't reach melee (2 beams at char 5, 3 at char 10); a real option with Agonising Blast + CHA 20.
    - spell: Booming Blade
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Melee weapon attack roll
      when: char 1 (Warlock 1)
      why: 'Selected melee cantrip: use it with two-handed Phalar in Act 1 and Shadow Blade after the respec. It adds Thunder damage from character level 5, works with Extra Attack but is limited to one cast per Action, and triggers the Ring of Arcane Synergy for 2 turns.'
    - spell: Mage Hand
      level: Cantrip
      guide_level: 9
      school: Conjuration
      save: None
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Third-cantrip exploration and object-manipulation utility that does not depend on a spell attack or saving throw.
    - spell: Crown of Madness
      level: '2'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: char 10 (Oathbreaker oath spell)
      why: Always-prepared Oathbreaker control that can force a humanoid to attack a nearby creature. It is situational and competes with Darkness for Concentration, but costs no Warlock spell selection.
    alternatives:
    - spell: Bone Chill
      level: Cantrip
      school: Necromancy
      save: Ranged spell attack
      when: Warlock cantrip alternative
      why: Ranged anti-healing utility and advantage against Undead; take it instead of Mage Hand when that combat niche matters more than exploration utility.
    - spell: Minor Illusion
      level: Cantrip
      school: Illusion
      save: None
      when: Warlock cantrip alternative
      why: Pulls nearby creatures toward a distraction before combat, helping the party set up an ambush or isolate a target without relying on an attack roll or save.
    - spell: Protection from Evil and Good
      level: '1'
      school: Abjuration
      save: None (Concentration)
      when: Warlock spell alternative
      why: 'Strong defensive preparation against Aberrations, Celestials, Elementals, Fey, Fiends, and Undead: their attacks against the target have Disadvantage, and they cannot Charm, Frighten, or Possess it. Competes with Darkness.'
    - spell: Mirror Image
      level: '2'
      school: Illusion
      save: None
      when: Warlock spell alternative
      why: Non-concentration defence for a melee frontliner; three duplicates initially grant +9 AC, with one duplicate disappearing whenever an attack misses.
    - spell: Hold Person
      level: '2'
      school: Enchantment
      save: WIS save
      when: Warlock spell alternative
      why: Paralyses a humanoid so melee hits from within 3m automatically crit. A strong self-contained smite setup when Bonbon is not controlling the target; Concentration.
    - spell: Hunger of Hadar
      level: '3'
      school: Conjuration
      save: DEX save (Acid damage)
      when: Warlock 5 alternative
      why: Large difficult-terrain zone that Blinds creatures inside and deals Cold damage at the start of their turns plus possible Acid damage at the end. Excellent group control, but it uses Concentration instead of Darkness.
    - spell: Blink
      level: '3'
      school: Transmutation
      save: None
      when: Hexblade expanded spell at Warlock 5
      why: Non-concentration defence with a chance to enter the Ethereal Plane at the end of each turn, keeping Charles untargetable until his next turn.
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
      note: Supplies the CHA weapon package, armour proficiencies, and curse that define the build.
    - category: Cantrips
      recommendation:
      - Eldritch Blast
      - Booming Blade
      note: A scaling ranged fallback plus the melee weapon cantrip that later activates the Ring of Arcane Synergy.
    - category: Spells
      recommendation:
      - Hex
      - Armour of Agathys
      note: Sustained damage when Darkness is unnecessary and durable non-concentration temporary HP.
    - category: Hexblade spells
      recommendation:
      - Shield
      - Wrathful Smite
      note: Automatically granted by the Hexblade at Warlock 1; Shield is the defensive reaction, while Wrathful Smite is a situational concentration option.
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
      note: Devil's Sight enables the Darkness melee plan; Agonising Blast makes the ranged fallback scale with CHA.
    - category: Spell
      recommendation: Hellish Rebuke
      note: Useful reaction damage before the build pauses Warlock progression for the rest of Act 1.
  - char_level: 3
    class: Paladin 1
    gains:
    - Lay on Hands
    - Divine Sense
    - Temporary Paladin oath
    recommendations:
    - category: Oath
      recommendation: Oath of Vengeance (keep intact temporarily)
      note: 'Use the oath''s normal tools during Act 1 and delay becoming an Oathbreaker until after the Resonance Stone respec. This avoids paying to restore the oath before Withers will respec Charles.'
  - char_level: 4
    class: Paladin 2
    gains:
    - Divine Smite
    - Paladin Spellcasting
    - Fighting Style selection
    recommendations:
    - category: Fighting style
      recommendation: Defence
      note: Always-on AC is the best fit for a two-handed frontliner who already gains damage from Great Weapon Master.
    - category: Prepared spells
      recommendation:
      - Bless
      - Divine Favour
      - Command
      note: Arrow-created Darkness is concentration-free, so Bless or Divine Favour can stay active inside it; most remaining slots become Divine Smites.
  - char_level: 5
    class: Paladin 3
    gains:
    - Divine Health
    - Oath of Vengeance subclass actions
    recommendations:
    - category: Subclass path
      recommendation: Keep the oath intact through Act 1
      note: Vow of Enmity supplies a non-consumable advantage option when Darkness Arrows are unnecessary or unavailable. Break the oath only after the planned Act-2 respec.
  - char_level: 6
    class: Paladin 4
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      recommendation: Great Weapon Master
      note: Two-handed Phalar qualifies for All In. Devil's Sight advantage from a Darkness Arrow and Bless offset the −5 attack penalty; the +10 damage is the Act-1 spike.
  - char_level: 7
    class: Paladin 5
    gains:
    - Extra Attack
    - Level 2 Paladin spells
    recommendations:
    - category: Rotation
      recommendation: Booming Blade or Phalar attack → Extra Attack
      note: The two-handed GWM phase now makes two attacks per Action; use Smite reactions on crits and priority hits.
  - char_level: 8
    class: Paladin 6 (pre-Stone continuation)
    gains:
    - Aura of Protection
    recommendations:
    - category: Timing
      recommendation: Keep the Act-1 Phalar/GWM package until the Resonance Stone
      note: The Stone is normally acquired late enough in Act 2 that character level 8 arrives first. Aura of Protection is the strongest interim Paladin level and helps protect the party inside the later Stone aura.
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
      note: Required for Shadow Blade main hand + Phalar Aluve off-hand; Great Weapon Master no longer applies and is removed by the respec.
    - category: Paladin feat
      recommendation: Savage Attacker
      note: The usual character-level-9 respec has enough levels for both feats. If the Stone is acquired at level 8, use Warlock 5 / Paladin 3 for Dual Wielder and take Paladin 4 / Savage Attacker on the next level.
    - category: Warlock spells
      recommendation:
      - Shadow Blade
      - Darkness
      - Counterspell
      - Misty Step
      note: Shadow Blade is immediately 3d8 from the level-3 pact slots; Darkness and Devil's Sight replace the Act-1 arrow dependency.
    - category: Subclass path
      recommendation: Break the freshly selected Paladin oath → Oathbreaker
      note: 'Keeping the Act-1 oath intact makes this free. If Charles became an Oathbreaker earlier, he must first pay the Oathbreaker Knight to restore his oath before Withers permits the respec, then break it again.'
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
      note: 'Before Phalar Aluve, bind the best available main-hand weapon with Bind Hexed Weapon so it attacks using CHA. The Hexblade action can bind a Two-Handed or Versatile weapon; leave the off-hand empty so Versatile weapons use their larger die and later qualify for Great Weapon Master.'
    - id: phalar-aluve-two-handed
      item: Phalar Aluve (selected two-handed weapon)
      slot: weapons
      note: 'ACT-1 DEFAULT from the Underdark. Bind Phalar as the Hexed Weapon and keep the off-hand empty so the Versatile longsword uses 1d10 and Great Weapon Master: All In adds +10 damage from character level 6. Pre-cast Shriek when possible and keep the sword equipped; its 6m aura covers Charles and Asterion.'
    - id: arrows-of-darkness
      item: Arrows of Darkness (farm)
      slot: consumables
      note: 'ACT-1 and early-ACT-2 advantage engine. Prefer having Bonbon place the cloud so Charles can keep Phalar active; if Charles must fire it, do so before switching to Phalar and activating Shriek. The concentration-free 3m cloud lasts 3 turns, letting Devil''s Sight grant advantage while Charles maintains Bless, Divine Favour, or Hex. Restock from arrow vendors because the build deliberately stops Warlock at level 2 until the Resonance Stone.'
    - id: dual-hand-crossbows-plus-one
      item: Dual Hand Crossbows +1
      slot: ranged weapons
      note: 'SELECTED ranged-slot fallback and Darkness-Arrow launcher. Farm Dammon, Roah, Derryth, and Jeera for +1 copies; the ranged set does not interfere with two-handed Phalar.'
    - id: luminous-armour
      item: Luminous Armour
      slot: armour
      note: 'SELECTED chest after Divine Smite arrives at character level 4. The Selûnite Outpost medium armour reaches AC 17 with DEX 14, and each Divine Smite''s Radiant damage emits a Radiating Shockwave that penalises nearby enemy attacks.'
    - id: adamantine-scale-mail
      item: Adamantine Scale Mail (defensive alternative)
      slot: armour
      note: 'DEFENSIVE ALTERNATIVE forged from the party''s second Mithral ore. It preserves Charles''s medium-armour proficiency while providing crit immunity, 1 damage reduction, and Reeling when a melee attacker hits. Luminous Armour remains selected for its Radiating Shockwaves.'
    - id: boots-of-striding
      item: Boots of Striding
      slot: feet
      note: 'SELECTED boots from Minthara. Concentrating on Bless, Divine Favour, or Hex inside an Act-1 Darkness Arrow grants Momentum and prevents Charles from being knocked Prone or moved; after the respec, self-cast Darkness supplies the concentration.'
    - id: amulet-of-misty-step
      item: Amulet of Misty Step
      slot: amulets
      note: 'SELECTED neck from Priestess Gut''s chambers. Misty Step once per short rest solves Charles''s approach and elevation problems; Asterion already has Monk movement, the Sentient Amulet, and later the Night Walkers.'
    - id: haste-helm
      item: Haste Helm
      slot: head
      note: 'SELECTED Act-1 head from the Blighted Village. Three turns of opening Momentum help Charles reach priority targets; the Ring of Arcane Synergy supplies his Arcane Synergy without consuming this slot. Asterion can borrow it when Charles does not need the approach speed.'
    - id: gloves-of-the-growling-underdog
      item: Gloves of the Growling Underdog (early alternative)
      slot: hands
      note: 'Dror Ragzlin''s treasure-room gloves grant advantage on melee weapon attacks when at least two enemies stand within 3m of the target. Useful when conserving Darkness Arrows or when the cloud cannot cover the priority target.'
    - id: gloves-of-baneful-striking
      item: Gloves of Baneful Striking (late default)
      slot: hands
      note: 'SELECTED late-Act-1 gloves from Lady Esther. A weapon hit gives the target −1d4 to saving throws for 2 turns, helping Asterion''s Stun and the casters'' control after Charles connects. Unlike Growling Underdog, their effect is not redundant inside Darkness.'
    - id: auntie-ethel-s-hair-cha-17-18
      item: Auntie Ethel's Hair → CHA 17 → 18
      wiki: Auntie Ethel's Hair
      slot: consumables
      note: Auntie Ethel's Hair → CHA 17 → 18 (raises Aura DCs, attack/smite accuracy, and prepared-spell count)
    - id: ring-of-arcane-synergy
      item: Ring of Arcane Synergy
      slot: rings
      note: 'SELECTED second ring from Gish Far''aag in the Crèche. Damaging an enemy with a Phalar Booming Blade grants Arcane Synergy for 2 turns, adding Charles''s CHA modifier to subsequent weapon attacks. It pairs with Strange Conduit without duplicating Bonbon''s Diadem; Risky Ring can replace it in Act 2.'
    - id: strange-conduit-ring
      item: Strange Conduit Ring
      slot: rings
      note: 'Strange Conduit Ring (Crèche) adds 1d4 Psychic to weapon attacks while Concentrating. In Act 1, maintain Bless, Divine Favour, or Hex inside concentration-free Arrow darkness. After the respec, self-cast Darkness powers it and the Resonance Stone doubles its Psychic rider.'
    act2:
    - id: self-cast-shadow-blade-upcast-to-3d8
      item: Self-cast Shadow Blade upcast to 3d8
      wiki: Shadow Blade (weapon)
      slot: weapons
      note: 'POST-RESONANCE DEFAULT. Keep two-handed Phalar/GWM through early and mid Act 2; the Shadow Blade switch begins only after the late-Act-2 Resonance Stone pickup. Warlock 5 immediately supplies level-3 pact slots: summon 3d8 Shadow Blade, bind THIS main-hand weapon to CHA so Deepened Pact applies, and leave Phalar unbound in the off-hand. The usual character-level-9 split is Warlock 5 / Paladin 4; Warlock 5 / Paladin 3 is the minimum if the Stone is acquired at level 8.'
    - id: phalar-aluve-offhand
      item: Phalar Aluve (selected off-hand)
      slot: weapons
      note: 'SELECTED PARTY-DAMAGE DEFAULT after the Stone. Dual Wielder replaces Act 1''s Great Weapon Master so Phalar can remain equipped beside the Light Shadow Blade; the feat also grants +1 AC. Pre-cast Shriek whenever possible, then keep Charles and Asterion within its tighter 6m aura (the Stone reaches 9m). Shriek''s 1d4 Thunder triggers from every qualifying party damage instance and penalises affected enemies'' attacks and all saves by 1d4, outweighing a personal-DPR off-hand in this multi-hit party. Phalar is not bound and Charles lacks Two-Weapon Fighting, so its bonus-action swing is secondary—use it only after Curse, mobility, and other bonus-action priorities.'
    - id: render-of-mind-and-body-personal-alternative
      item: Render of Mind and Body (personal-DPR alternative)
      slot: weapons
      note: 'AVAILABLE BEFORE THE STONE from Lann Tarv at Moonrise after convincing Z''rell to provide additional aid. This Light shortsword can sit beside the Light Shadow Blade without Dual Wielder; a personal-only respec can therefore take Savage Attacker + CHA ASI instead. Its own advantaged off-hand hit gains +1d8 Psychic, doubled by the Stone, but it does not buff Shadow Blade or the rest of the party. Keep Phalar selected unless Charles is being optimised in isolation.'
    - id: knife-of-the-undermountain-king-personal-alternative
      item: Knife of the Undermountain King (personal crit alternative)
      slot: weapons
      note: 'ALREADY AVAILABLE from the Act-1 Crèche and Light enough to pair with Shadow Blade without Dual Wielder. Its global −1 critical threshold and melee-die reroll make it Charles''s strongest crit-stat-stick alternative, but Bonbon already uses the unique Knife to improve Titanstring and spell-attack crits. Reassigning it also loses Phalar Shriek, so this is not the party default.'
    - id: sentinel-shield-defensive-alternative
      item: Sentinel Shield (defensive alternative)
      slot: off-hand
      note: 'AVAILABLE BEFORE THE STONE from Lann Tarv at Moonrise. Shadow Blade is one-handed, so Charles can use this shield for +2 AC, +3 Initiative, and advantage on Perception while dropping Phalar. For an extended defensive setup, respec Dual Wielder into +2 CHA or another useful feat; for a one-fight swap, accepting the temporarily wasted feat is cheaper than another respec.'
    - id: charge-bound-warhammer-physical-fallback
      item: Charge-Bound Warhammer (Psychic-immune fallback)
      slot: weapons
      note: 'AVAILABLE BEFORE THE STONE from Dammon at Last Light. Against Psychic immunity, bind this main-hand weapon instead of Shadow Blade: while bound it is effectively +2 and adds 1d6 Lightning, Deepened Pact still applies, and Dual Wielder still permits Phalar off-hand for Shriek. Against mere Psychic resistance, first test the Stone—Vulnerability and Resistance normally cancel—then holster the Stone if its defensive risk is worse than the multiplier.'
    - id: resonance-stone-aura
      item: Resonance Stone aura (carried by Asterion)
      slot: party aura
      note: 'LATE ACT 2 in the Mind Flayer Colony; this pickup triggers the weapon respec. Its 9m Steeped in Bliss aura makes eligible nearby creatures vulnerable to Psychic damage, doubling Shadow Blade and Strange Conduit. It does not affect Undead or Constructs, and it also gives allies Psychic Vulnerability plus disadvantage on mental saves. Asterion carries it, stays within 9m of Charles, and closes to 6m when both need Phalar Shriek; holster it against Psychic attackers, dangerous mental-save effects, and encounters where the target cannot receive the aura.'
    - id: risky-ring
      item: Risky Ring
      slot: rings
      note: 'Risky Ring (Moonrise — Araj Oblodra): advantage on ALL attacks (disadvantage on saves) — the crit-fishing engine; keep it behind Aura of Protection to offset the save penalty'
    - id: ring-slot-2
      item: Shadow Blade Ring (backup)
      wiki: Shadow Blade Ring
      slot: rings
      note: 'The Shadow Blade Ring summons a 2d8 psychic blade once per short rest. Strange Conduit Ring remains the default second ring for nova turns; carry this as insurance if Charles loses or cannot prepare his class-cast blade.'
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      slot: rings
      note: 'Killer''s Sweetheart (Gauntlet of Shar — Self-Same Trial): your first attack after a kill is a GUARANTEED crit → a free doubled smite every fight'
    - id: head-slot
      item: Covert Cowl (Darkness option)
      wiki: Covert Cowl
      slot: head
      note: 'Head slot: Covert Cowl (Last Light — −1 crit while Obscured) is the Darkness crit-fishing default. After Bonbon replaces the Diadem with the Helmet of Arcane Acuity, Charles can borrow the Diadem for raw damage when his Act-1 Arcane Synergy Ring has been displaced by Risky Ring. (A 2nd Covert-Critical head — the Dark Justiciar Helmet — lets Asterion run one too.)'
    act3:
    - id: shadow-blade-phalar-act3-default
      item: 3d8 Shadow Blade main hand + Phalar Aluve off-hand
      wiki: Shadow Blade (weapon)
      slot: weapons
      note: 'ACT-3 DEFAULT continues the late-Act-2 setup: bind Shadow Blade for CHA and Deepened Pact, leave Phalar off-hand for pre-cast Shriek, and use its bonus-action attack only when free. This remains the party-damage choice over Render or the Knife because Asterion, Bonbon, and Charles produce many Shriek triggers. Confirm that the Resonance Stone aura still functions after leaving Act 2 and holster it whenever its Psychic/mental-save downside is unsafe.'
    - id: nyrulna-physical-fallback
      item: Nyrulna + Phalar Aluve (Act-3 physical fallback)
      slot: weapons
      note: 'OPTIONAL from Akabi''s Chult jungle in Rivington. Against Psychic-immune targets, bind Nyrulna main hand for its +3 enchantment, extra 1d6 Thunder, movement, and fall-damage immunity while Dual Wielder keeps Phalar off-hand. Charge-Bound Warhammer remains the earlier one-handed fallback; neither replaces Shadow Blade against targets that safely receive the Stone''s Psychic Vulnerability.'
    - id: sarevok-s-horned-helmet
      item: Sarevok's Horned Helmet
      slot: head
      note: 'Sarevok''s Horned Helmet reduces the critical-hit threshold and grants Darkvision. It stacks with Charles''s other crit-range effects for targets that are not already Paralyzed.'
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      slot: rings
      note: 'Killer''s Sweetheart turns one attack into a guaranteed critical hit after Charles kills a creature. Saving it for a high-level Divine Smite doubles the smite dice.'
    - id: helldusk-gloves
      item: Helldusk Gloves
      slot: hands
      note: 'Helldusk Gloves add fire damage to weapon attacks and improve spell attacks and spell save DC. The weapon rider is applied on each of Charles''s many pact-weapon hits.'
  playstyle: |-
    - **Act 1 through most of Act 2 — two-handed Phalar:** bind Phalar Aluve, keep the off-hand empty, pre-cast Shriek, and enter a farmed Darkness Arrow cloud with Devil's Sight. Maintain Bless, Divine Favour, or Hex because the cloud is concentration-free; toggle GWM All In when advantage makes the −5 acceptable.
    - **Late Act 2+ — Shadow + Stone:** on acquiring the Resonance Stone, usually respec at character level 9 to Warlock 5 / Paladin 4, replace GWM with Dual Wielder, summon 3d8 Shadow Blade main hand, and off-hand Phalar. Asterion carries the Stone within 9m to double the Psychic package.
    - **Nova:** attack a Held target, spending the largest Divine Smites first. At Paladin 5 after the respec, two three-attack Actions under Haste plus one Phalar off-hand attack reach seven auto-crit swings when the bonus action is free.
    - **Between novas:** fish for crits with advantage and the build's stacked crit-range bonuses; short rest to refill Warlock slots.
  nova:
    assumptions: Held target (every hit auto-crits), Darkness active, full 8-slot dump. Darkness occupies Concentration, so Wrathful Smite/Hex/Bless are excluded; Strange Conduit remains active. Smites double their dice on a crit; Half-Orc adds a die; Savage Attacker rerolls every die. Flat weapon bonuses ride the weapon's type so vulnerability can double them; smites are radiant.
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
    caveats: 'The estimate assumes Asterion''s shared Resonance Stone is active, the Savage-Attacker-rerolls-smite quirk, and Hexblade''s Curse''s +4 riding the weapon''s type. It conservatively excludes Phalar Shriek''s additional 1d4 Thunder damage per qualifying damage instance. Without the Resonance Stone, Shadow Blade loses the psychic doubling.'
---
