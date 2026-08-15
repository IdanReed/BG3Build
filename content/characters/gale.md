---
nickname: Gale
builds:
- name: The Powder Keg
  is_primary: true
  role: Fire striker + non-concentration Command control + party Haste engine
  class: Sorcerer 11 (Draconic Bloodline — Red) / Fiend Warlock 1
  race: Gale (Human)
  race_notes: 'Human (BG3): a freely-assigned +2/+1 ability bonus like every race (the CHA 17 in starting_stats is 15 point-buy + the +2 racial), ''Civil Militia'' proficiency with Shields + Light armour + spear/pike/halberd/glaive (no trident), one extra skill, and +25% carry weight — stat-neutral vs any other race, so it costs nothing. IMPORTANT FOR THIS BUILD: Civil Militia already grants LIGHT ARMOUR, so Gale does not need the Warlock dip to wear Armour of Landfall — the dip is justified by Command alone. The published guide recommends Halfling for Luck (no nat-1s on the many Scorching Ray attack rolls and on Heat CON saves); Gale is a fixed origin Human, so that safety net is unavailable and Armour of Landfall''s Constitution-save advantage becomes the replacement. NETHERESE ORB: only an EARLY-Act-1 issue — the 3-item ''The Wizard of Waterdeep'' quest; feed Gale 3 magic items and the hunger resolves (Elminster later quells it entirely). Ignoring it stacks escalating Arcane Hunger debuffs (disadvantage on saves → attacks → half move) and only the final ignored stage is fatal — it is NOT an Act 1–2 resource drain. Recruited as a Wizard; respec via Withers into this Draconic-Red Sorcerer / Fiend Warlock build.'
  background: Sage (Arcana, History) — Gale's default
  starting_stats:
    STR: 8
    DEX: 16
    CON: 14
    INT: 8
    WIS: 10
    CHA: 17
  stats_note: 'Point-buy base 8/15/14/8/10/15 = all 27 points (DEX 15 and CHA 15 cost 9 each, CON 14 costs 7, WIS 10 costs 2). Then Human +2 → CHA 17 and +1 → DEX 16. DEX 16 matters more than on the old Storm build: Draconic Resilience sets unarmoured AC to 13 + DEX, and Armour of Landfall is 13 + DEX light armour, so DEX is Gale''s entire AC. WIS drops to 10 because there is no longer a Cleric dip keying off it.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss, Cloister of Sombre Embrace in Act 3). CHA 20 is the target and no ASI is needed to reach it, which is what frees both feats for Dual Wielder and Elemental Adept. Birthright (+2 CHA → 22) is NOT usable here: the head slot belongs permanently to the Hat of Fire Acuity, so Birthright goes to Bonbon.'
  metamagic:
  - Twinned + Extended (Sorc 2)
  - Quickened (Sorc 3)
  - Careful (Sorc 10 / char 11)
  feats:
  - at: Sorc 4 (char 4)
    feat: Dual Wielder
    note: 'Unusual for a caster, but this build wields two staves as stat sticks: Spellsparkler + Melf''s in Act 1, then Markoheshkir + Rhapsody in Act 3. Neither pair is Light, so Dual Wielder is mandatory to hold both. COST: Gale gives up the Safeguard Shield (+2 AC, +1 all saves) that previously protected his Haste concentration on the Storm build.'
  - at: Sorc 8 (char 9)
    feat: 'Elemental Adept: Fire'
    note: 'Effectively mandatory in THIS party, though the tier lists rate the feat only B in general — worth knowing you are spending one of two feats on a B-tier pick while Alert (S+) goes unbought. The published guide says to skip Elemental Adept if you have a bow archer who can mass-apply Arsonist''s Oil with Arrows of Many Targets or Volley; Bonbon moves to dual hand crossbows in Act 2 and has no such option, so she can only strip fire resistance one target at a time, and Act 3 is dense with fire-resistant enemies. ⚠ TWO WORDING CORRECTIONS from the wiki: BG3''s text is "you CANNOT ROLL A 1" on Fire damage dice, not the tabletop "treat 1s as 2s" — still excellent here because Scorching Ray rolls so many dice. And the resistance-piercing is BROADER than usually stated: it applies to "spells you cast AND attacks you make," not spells alone; only the no-1 clause is spell-only.'
  feats_note: 'ONLY TWO FEATS. Sorcerer grants them at Sorc 4 and Sorc 8 = character levels 4 and 9; the Warlock level grants none and Sorc 12 is never reached. Dual Wielder and Elemental Adept consume both, so there is no room for Alert, War Caster, or an ASI — initiative and concentration are gear problems on this build.'
  key_spells:
  - Scorching Ray (the core damage engine — every rider applies per ray)
  - Fireball (AoE; Careful Spell only arrives at char 11)
  - Haste (Twinned — the party engine, now online at char 5)
  - Command (Warlock — NOT Concentration, so it coexists with Haste)
  - Hold Person / Hold Monster (Charles's auto-crit setup)
  - Counterspell
  - 'Daylight: Enchant Item (illumination for the Coruscation → Callous Glow chain)'
  - Chain Lightning (the answer to fire-immune enemies)
  creation:
    level1_class: Sorcerer 1 from character level 1. There are NO respecs in this build after the initial Withers respec out of Wizard.
    level1_gains: Sorcerer Spellcasting (CHA), Draconic Bloodline with Red (Fire) ancestry, Draconic Resilience (unarmoured AC 13 + DEX, +1 HP per Sorcerer level), a free Burning Hands from the Red ancestry, and CON + CHA saving-throw proficiency from character level 1.
    subclass_choice: 'Draconic Bloodline, Red ancestry. Any Fire ancestry works (Red, Gold, or Brass); Red is chosen for the free Burning Hands. The ancestry choice is what makes Elemental Affinity at Sorc 6 add Gale''s CHA modifier to Fire damage.'
    proficiencies:
      armor_weapons: 'Light armour and shields from Human Civil Militia (kept for the whole run), plus quarterstaffs, daggers, darts, slings, and light crossbows from Sorcerer. Warlock 1 also grants light armour, which is redundant here. Gale never wears a shield after Dual Wielder.'
      saving_throws: CON + CHA from character level 1 — no Cleric bridge, so there is no window without CON-save proficiency this time.
      skills: Sage (Arcana, History) + 2 Sorcerer picks + Human extra.
    starting_cantrips: 'Fire Bolt, Friends, Minor Illusion, and Mage Hand. Cantrips are permanent (no replacement), and this build stops using them for damage after character level 3, so pick for utility rather than scaling.'
    starting_spells: 'Shield and Magic Missile, plus the free Burning Hands from Red ancestry. Magic Missile is a placeholder that gets replaced by Counterspell at Sorc 6.'
    notes: 'CON + CHA saves from level 1 is a real upgrade over the old Cleric-first bridge, and Twinned Haste now lands at character level 5 instead of 6. The cost is that the party loses Gale''s Guidance, Bless, Healing Word, Bane, and Create Water entirely — see the party plan''s Act 1 coverage table for where each of those moves.'
  spells:
    note: 'Sorcerer is a KNOWN caster (learn on level-up, replace 1 per level); 12 spells known at Sorc 11, plus the free Burning Hands. The Warlock level adds Command and Hex as separately-known Warlock spells. Mandatory = the Scorching Ray damage engine, Twinned Haste, and Command; Recommended = flex utility.'
    mandatory:
    - spell: Scorching Ray
      level: '2'
      guide_level: 3
      school: Evocation
      save: Ranged spell attack (one roll per ray)
      when: Sorc 3 (char 3)
      why: 'THE build — though note the tier lists rate the spell itself only A, precisely because its value is "multi-hit riders, not efficiency," which is exactly how this build uses it. 3 rays at level 2, +1 ray per slot level above 2nd (a level 6 slot fires 7). Each ray is a separate attack roll AND a separate damage instance, so every flat rider applies to EVERY ray. ⚠ CONFIRMED per-ray by name on the wiki: Elemental Affinity: Damage and the Callous Glow Ring. INFERRED but not individually stated: Rhapsody and Markoheshkir''s +proficiency, which are covered only by the general rule that bonus damage from passives and conditions applies per instance. Spellmight''s +1d8 is NOT addressed anywhere — see the traps. That means +5 CHA, +2 Callous Glow, +3 Rhapsody, +4 Markoheshkir, +1d8 Spellmight, and Charles''s Phalar Shriek 1d4 Thunder all multiply by the ray count. It is also the Hat of Fire Acuity engine: each ray deals Fire damage and grants 2 turns of Arcane Acuity, so one level-4 cast caps Gale at 10 stacks.'
    - spell: Command
      level: '1'
      guide_level: 7
      school: Enchantment
      save: WIS save
      when: Warlock 1 (char 7)
      why: 'The single biggest reason to take the Warlock level, and the reason this build beats the old Storm chassis in this party: Command does NOT use Concentration, so Gale can hold Twinned Haste and still control every turn. Extended Spell doubles the condition to two turns. Approach also groups enemies for Fireball. Does not work on Undead.'
    - spell: Haste
      level: '3'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Sorc 5 (char 5)
      why: 'Single-target so Twinnable; spend 3 Sorcery Points to Haste two of Charles / Asterion / Gale. Arrives a level EARLIER than on the old Storm build, which needed a char-6 respec. Ending Haste makes both targets Lethargic. NEW TENSION: Gale''s own hasted action is a second Scorching Ray, so self-Haste now genuinely competes with hasting both martials.'
    - spell: Fireball
      level: '3'
      guide_level: 6
      school: Evocation
      save: DEX save
      when: Sorc 6 (char 6)
      why: 'Primary AoE, and now on-element — Elemental Affinity, Flame of Wrath, and Elemental Adept all apply. ⚠ The tier lists rate Fireball only B — "do not cast it solely because it is iconic." It is correct to keep here because it is on-element for three separate multipliers, but do not prioritise it over another Scorching Ray on a single target; it earns its slot on clusters of 4+. ⚠ Careful Spell does not arrive until Sorc 10 (char 11), so for most of the run Fireball is an adds-cluster tool only and must not be dropped on Charles or Asterion.'
    - spell: Counterspell
      level: '3'
      guide_level: 6
      school: Abjuration
      save: Reaction (no check at equal/higher slot)
      when: Sorc 6 (char 6) — replaces Magic Missile
      why: Shuts down enemy casters without using Concentration or an Action; competes with Shield for the Reaction, and both are worth keeping.
    - spell: Hold Person
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Sorc 4 (char 4)
      why: 'Paralysed humanoids take automatic critical hits from melee within 3m — Charles''s smite setup. Concentration, so Gale can only hold this INSTEAD of Haste; usually Bonbon owns the Hold lane and Gale owns Haste + Command. Take Hold Monster at Sorc 9 for non-humanoids.'
    - spell: 'Daylight: Enchant Item'
      level: '3'
      guide_level: 8
      school: Evocation
      save: None
      when: Sorc 7 (char 8)
      why: 'Cast on an ally''s main-hand weapon out of combat; it is bugged to last until long rest, so this is a once-per-rest chore rather than a combat action. 15m radius that travels with the carrier. Its purpose is to keep GALE illuminated so the Coruscation Ring fires — see the illumination chain in the itemization notes. ⚠ Requires the target to hold a main-hand weapon, which rules out Asterion (empty hands for Tavern Brawler); Bonbon''s hand crossbows are the clean carrier. Darkness is only dispelled at the moment of casting, so Charles''s Darkness Arrows fired afterwards are unaffected.'
    - spell: Chain Lightning
      level: '6'
      guide_level: 12
      school: Evocation
      save: DEX save
      when: Sorc 11 (char 12)
      why: 'The answer to fire-immune enemies, which is a real gap now that the party has no lightning caster. Reserved for the House of Hope, Raphael, and the red dragon. Buy Globe of Invulnerability scrolls for the fights where you would rather have that instead.'
    recommended:
    - spell: Shield
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None (Reaction, +5 AC)
      when: Sorc 1 (char 1)
      why: Gives Gale's otherwise-dead level-1 slots a job in the late game and sharply improves survival without touching Concentration.
    - spell: Hold Monster
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Sorc 9 (char 10)
      why: The non-humanoid version of the auto-crit setup. Concentration, so use it only in fights where someone else supplies Haste.
    - spell: Hex
      level: '1'
      school: Enchantment
      save: None (Concentration)
      when: Warlock 1 (char 7)
      why: 'The second Warlock spell known. A per-ray damage rider in theory, but it uses Concentration and therefore competes with Haste — effectively a modded-difficulty option only. Armour of Agathys is the defensive alternative pick.'
    - spell: 'Chromatic Orb: Fire'
      level: '1'
      guide_level: 2
      school: Evocation
      save: Ranged spell attack
      when: Sorc 2 (char 2)
      why: 'Early on-element single-target damage before Scorching Ray arrives at char 3, and it creates a fire surface. ⚠ Rated S-tier — "exceptionally highly" — so think twice before treating it as a throwaway replacement candidate; its other elemental modes also cover the fire-immune enemies Gale otherwise has no answer to before Chain Lightning at char 12.'
    - spell: Ice Storm
      level: '4'
      guide_level: 9
      school: Evocation
      save: DEX save
      when: Sorc 7+ (char 8+) — optional pick
      why: 'A-tier and NOT Concentration, which is the whole reason to consider it: Gale can drop it on a cluster while still holding Twinned Haste, unlike every other AoE of its size. It also lays an ice surface for prone control. Off-element, so it gets no Elemental Affinity, Flame of Wrath or Elemental Adept — take it only if the fire-resistance problem in Act 3 turns out worse than Elemental Adept can fix.'
    - spell: Burning Hands
      level: '1'
      guide_level: 1
      school: Evocation
      save: DEX save
      when: Sorc 1 (char 1) — FREE from Red ancestry
      why: Does not consume a spell-known pick. Genuinely useful for the first few levels as on-element AoE, and it is the reason to pick Red over Gold or Brass.
    - spell: Enhance Ability
      level: '2'
      guide_level: 3
      school: Transmutation
      save: None (Concentration)
      when: Sorc 3+ (replacement candidate)
      why: Out-of-combat advantage on a chosen ability check. Concentration, so treat it as an exploration mode only.
    - spell: Dimension Door
      level: '4'
      guide_level: 9
      school: Conjuration
      save: None
      when: Sorc 8 (char 9)
      why: Repositions Gale and one ally out of a collapsing fight; also solves several Act 3 traversal problems.
    - spell: Telekinesis
      level: '5'
      guide_level: 11
      school: Transmutation
      save: STR save
      when: Sorc 10 (char 11)
      why: Concentration control that can repeatedly reposition a dangerous target or throw it from height. Competes with Haste, so it is a situational pick.
    - spell: Fire Bolt
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1 (char 1)
      why: 'On-element chip damage for the first three levels. This build stops using cantrips in combat after Scorching Ray arrives, so do not build around it — and note this is why the Potent Robe (CHA to cantrip damage) is a much weaker pickup than it was for the Storm build.'
    - spell: Friends
      level: Cantrip
      guide_level: 1
      school: Enchantment
      save: None (Concentration)
      when: Sorc 1 (char 1)
      why: 'Advantage on Charisma checks. Bonbon is the party face, so this is a backup rather than a plan; the target turns hostile when it ends, so never use it somewhere you intend to stay.'
    - spell: Minor Illusion
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: Sorc 1 (char 1)
      why: Groups enemies before combat starts, which sets up a bigger opening Fireball and relocates NPCs for Asterion's theft routes.
    - spell: Mage Hand
      level: Cantrip
      guide_level: 1
      school: Conjuration
      save: None
      when: Sorc 1 (char 1)
      why: 'Exploration and object manipulation. It also covers the party''s lost Create Water: drop a water bottle where the Hand can reach and use its Throw for a 2m Wet splash when something needs to be Wet.'
    - spell: Light
      level: Cantrip
      guide_level: 5
      school: Evocation
      save: None
      when: Sorc 4 (char 4) — fifth cantrip
      why: 'A free, slot-less way to keep GALE illuminated so the Coruscation Ring works, covering the whole stretch of Act 2 before Daylight is learned at char 8. Cast it on Gale''s own staff or on a nearby ally. ⚠ Worth confirming in play that a Light-lit character registers as Illuminated for Coruscation; if not, use an ordinary torch or Daylight.'
    - spell: Globe of Invulnerability
      level: '6'
      school: Abjuration
      save: None (Concentration)
      when: scroll only in this build
      why: 'Chain Lightning takes the single level-6 spell known, so buy Globe scrolls in Act 3 for the two or three fights that want it instead.'
    - spell: Misty Step
      level: '2'
      guide_level: 4
      school: Conjuration
      save: None (bonus action)
      when: replacement candidate
      why: 'Escape mobility. Lower priority than on the Storm build because Gale''s bonus action is usually committed to a Quickened Scorching Ray, and because Draconic Fly arrives at Sorc 11.'
  leveling:
    respecs:
    - label: Lv 1–12 · Sorcerer-first, no respec
      note: 'Single clean path — the published guide states there are no respecs needed, and this party does not add one. Sorcerer 1–6, the single Warlock level at character 7, then Sorcerer to 11. CON + CHA saves from level 1. The only respec Gale needs is the initial Withers respec out of Wizard when he is recruited.'
      rows:
      - char_level: 1
        class: Sorcerer 1
        gains:
        - Sorcerer Spellcasting (Charisma)
        - Draconic Resilience (unarmoured AC 13 + DEX, +1 HP per Sorcerer level)
        - Draconic Ancestry (Red) — free Burning Hands
        - CON + CHA saving-throw proficiency
        recommendations:
        - category: Subclass
          recommendation: Draconic Bloodline — Red (Fire)
          note: 'Fire ancestry is what makes Elemental Affinity add CHA to Scorching Ray and Fireball at Sorc 6. Red grants Burning Hands free; Gold and Brass are also Fire but grant Disguise Self and Sleep instead.'
        - category: Cantrips
          recommendation:
          - Fire Bolt
          - Friends
          - Minor Illusion
          - Mage Hand
          note: Cantrips are permanent and this build stops using them in combat after char 3, so choose utility over damage scaling.
        - category: Spells
          recommendation:
          - Shield
          - Magic Missile
          note: 'The plan replaces Magic Missile with Counterspell at Sorc 6 — but the tier lists rate BOTH Shield and Magic Missile S, so reconsider the swap in play. Magic Missile NEVER MISSES, which is a genuinely rare property on a build whose entire damage output is attack rolls; it is the clean answer to a turn where Scorching Ray would whiff, or for finishing a low-HP caster. If you keep it, drop a different flex spell for Counterspell instead.'
        - category: Skills
          recommendation:
          - Persuasion
          - Insight
          - Perception
          note: 'THREE picks, not two: Sorcerer grants 2 and Human Versatility grants 1 more of any kind. Sage already supplies Arcana and History, and proficiency does not stack, so do not re-pick Arcana. Persuasion is the only Sorcerer-list skill that rides the CHA 20 this build targets and makes Gale the fallback face when Bonbon is benched; Perception is the one skill worth duplicating across the party because BG3 rolls passive Perception per member. ⚠ The Human free skill is a character-creation choice — check at the Withers respec screen whether Perception is still re-selectable on the origin Gale or already locked.'
      - char_level: 2
        class: Sorcerer 2
        gains:
        - Font of Magic
        - Two Sorcery Points
        - Two Metamagic selections
        recommendations:
        - category: Metamagic
          recommendation:
          - Twinned Spell
          - Extended Spell
          note: 'Quickened is not selectable until Sorcerer 3. Twinned carries the Haste engine; Extended is what turns Command into a two-turn lockdown later.'
        - category: Spell
          recommendation: 'Chromatic Orb: Fire'
          note: On-element single-target damage to bridge the two levels before Scorching Ray.
      - char_level: 3
        class: Sorcerer 3
        gains:
        - Level 2 Sorcerer spells
        - Third Metamagic selection
        - Three Sorcery Points
        recommendations:
        - category: Metamagic
          recommendation: Quickened Spell
          note: 'Converts Scorching Ray into a bonus action, which is the whole gameplay loop: Quickened damage with the bonus action, then Extended Command or a second spell with the Action.'
        - category: Spell
          recommendation: Scorching Ray
          note: The build's core spell. From here Gale's damage comes almost entirely from this one card.
      - char_level: 4
        class: Sorcerer 4
        gains:
        - Fifth Sorcerer cantrip
        - Four Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: Dual Wielder
          note: 'Lets Gale hold Spellsparkler + Melf''s First Staff together (neither is Light). Later it is what allows Markoheshkir + Rhapsody. He loses the Safeguard Shield permanently.'
        - category: Cantrip
          recommendation: Light
          note: Keeps Gale illuminated for the Coruscation Ring without spending a slot, well before Daylight is learned.
        - category: Spell
          recommendation: Hold Person
          note: A second source of the paralysis that turns Charles's smites into automatic critical hits.
      - char_level: 5
        class: Sorcerer 5
        gains:
        - Level 3 Sorcerer spells
        - Five Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Haste
          note: 'The party Haste engine arrives a full level earlier than on the old Storm build. Twinned costs 3 Sorcery Points.'
      - char_level: 6
        class: Sorcerer 6
        gains:
        - 'Elemental Affinity: Damage (add CHA modifier to Fire spell damage)'
        - 'Elemental Affinity: Resistance (1 Sorcery Point → Fire resistance until long rest)'
        - Six Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Fireball
          note: Primary AoE, now boosted by Elemental Affinity.
        - category: Replacement
          recommendation: Magic Missile → Counterspell
          note: 'Use the level-up replacement slot here. Elemental Affinity is the single biggest power spike in the build: +5 damage per ray at CHA 20.'
      - char_level: 7
        class: Fiend Warlock 1
        gains:
        - Command and Hex as Warlock spells known
        - Eldritch Blast and one more Warlock cantrip
        - One level-1 pact slot (recharges on SHORT rest)
        - Dark One's Blessing (temporary HP on a kill)
        - Light armour proficiency (redundant — Gale already has it from Civil Militia)
        recommendations:
        - category: Patron
          recommendation: The Fiend
          note: Fiend is what puts Command on the Warlock list. This is the only Warlock level Gale ever takes.
        - category: Spells
          recommendation:
          - Command
          - Hex
          note: 'Command is the pickup. Hex is a concentration-competing damage rider that is mostly for modded difficulty; Armour of Agathys is the defensive alternative.'
        - category: Cantrips
          recommendation:
          - Eldritch Blast
          - Bone Chill
          note: 'Eldritch Blast is unimpressive here — Agonizing Blast is an invocation at Warlock 2, which Gale never reaches. Take it for the occasional ranged option, not as a plan. ⚠ Do NOT take Friends as the second cantrip: Gale already knows it from Sorcerer 1 and the game will not let you re-pick a known cantrip. Bone Chill (A tier — "targets AC at range, prevents healing, and gives undead disadvantage on attacks") is the right second pick because char 7 lands in Act 2, where Command does not work on the Undead. Toll the Dead is the equivalent WIS-save alternative.'
      - char_level: 8
        class: Sorcerer 7
        gains:
        - Level 4 Sorcerer spells
        - Seven Sorcery Points
        recommendations:
        - category: Spell
          recommendation: 'Daylight'
          note: 'Take the Enchant Item variant in play. Level 4 slots also mean a 5-ray Scorching Ray, which is exactly the cast that caps Arcane Acuity at 10 stacks.'
      - char_level: 9
        class: Sorcerer 8
        gains:
        - Eight Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          recommendation: 'Elemental Adept: Fire'
          note: 'Fire is the most resisted damage type in Act 3 and this party has no bow archer to mass-apply Arsonist''s Oil. Also removes 1s from every Fire damage die.'
        - category: Spell
          recommendation: Dimension Door
          note: Escape and traversal utility.
      - char_level: 10
        class: Sorcerer 9
        gains:
        - Level 5 Sorcerer spells
        - Nine Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Hold Monster
          note: Extends the auto-crit setup to non-humanoids for the fights where Bonbon is already concentrating on something else.
      - char_level: 11
        class: Sorcerer 10
        gains:
        - Fourth Metamagic selection
        - Sixth Sorcerer cantrip
        - Ten Sorcery Points
        recommendations:
        - category: Metamagic
          recommendation: Careful Spell
          note: 'Finally lets Gale drop Fireball on a cluster that Charles or Asterion is standing in. Until this level, Fireball is an adds-only tool.'
        - category: Cantrip
          recommendation: Ray of Frost
          note: 'The sixth cantrip — easy to miss, because this is the only level after char 4 that grants one. S tier: "the best broadly available elemental attack — Wet doubles its cold damage, the hit reduces movement without a save, and water can freeze into ice that knocks enemies prone." It patches this build''s one structural hole for free: Gale contributes almost nothing to the fire-immune fights (House of Hope, Raphael, the red dragon, Yurgir) until Chain Lightning at char 12, and a cantrip costs no slot. 3d8 at this level. Bone Chill is already taken at char 7, so Ray of Frost is the non-overlapping pick.'
        - category: Spell
          recommendation: Telekinesis
          note: Situational concentration control; it competes with Haste, so it stays a niche pick.
      - char_level: 12
        class: Sorcerer 11
        gains:
        - Level 6 Sorcerer spells and the single level-6 slot
        - Fly (Draconic Bloodline level 11)
        - Eleven Sorcery Points
        recommendations:
        - category: Spell
          recommendation: Chain Lightning
          note: 'The fire-immune answer for the House of Hope and Raphael. A level-6 Scorching Ray also fires 7 rays, which is the build''s single biggest turn.'
  itemization:
    act1:
    - id: the-spellsparkler
      item: The Spellsparkler
      slot: weapons
      note: 'SELECTED main hand from Counsellor Florrick at Waukeen''s Rest. Even better on this build than on the Storm one: Scorching Ray''s 3–5 separate damage instances build Lightning Charges extremely fast. ⚠ It is "Consumable by Gale" — wield it, do not feed it to the Netherese orb.'
    - id: melf-s-first-staff
      item: Melf's First Staff
      slot: weapons
      note: 'SELECTED off hand from Blurg in the Underdark, equipped from character level 4 once Dual Wielder is taken. +1 Spell Save DC and +1 spell attack rolls. On the Storm build this was an either/or swap with Spellsparkler; on this build Dual Wielder lets Gale hold BOTH, and the +1 spell attack matters on every single ray.'
    - id: shadespell-circlet
      item: The Shadespell Circlet
      slot: head
      note: 'BRIDGE head from Omeluum after Help Omeluum Investigate the Parasite. +1 Spell Save DC while Gale is obscured. It is replaced permanently by the Hat of Fire Acuity in Act 2, so treat it as an Act 1 rental.'
    - id: boots-of-stormy-clamour
      item: Boots of Stormy Clamour
      slot: feet
      note: 'SELECTED boots from Omeluum. Inflicting a condition applies 2 turns of Reverberation. Much stronger here than on the Storm build, because Gale now inflicts conditions constantly — Radiating Orb from Coruscation, Mental Fatigue from the Ring of Mental Inhibition, and Command itself.'
    - id: gloves-of-belligerent-skies
      item: Gloves of Belligerent Skies
      slot: hands
      note: 'SELECTED late-Act-1 gloves from the Crèche Inquisitor''s Chamber. Thunder/Lightning/RADIANT damage applies 2 turns of Reverberation — and once the Callous Glow Ring is online in Act 2, every ray deals 2 radiant, so these proc per ray. They stay competitive until Spellmight Gloves arrive in Act 3, at which point compare raw damage against the Reverberation-to-Prone engine.'
    - id: pearl-of-power-amulet
      item: Pearl of Power Amulet
      slot: amulets
      note: 'SELECTED resource neck from Omeluum. Restores one spell slot of level 3 or lower each long rest — normally another Haste or Scorching Ray. This build is famously long-rest hungry, so the free slot matters more than it did before.'
    - id: spidersilk-armour
      item: Spidersilk Armour
      slot: armour
      note: 'SELECTED Act 1 chest, and the answer to this build''s worst structural problem. Worn by Minthara in the Shattered Sanctum — the same kill that yields Charles''s Boots of Striding, so it costs nothing extra to acquire. AC 12 + DEX and +1 Stealth, but the reason to wear it is ADVANTAGE ON CONSTITUTION SAVING THROWS. Gale has no War Caster, no feat left to buy one, and no Safeguard Shield after Dual Wielder, so this is his only protection for Twinned Haste — and it arrives in Act 1 rather than waiting for Armour of Landfall in Act 3. ⚠ Costs exactly 1 AC versus going unarmoured, since Draconic Resilience is 13 + DEX; take the trade, because Haste is the concentration the entire party plan is built on.'
    - id: elixir-of-vigilance
      item: Elixir of Vigilance (daily)
      wiki: Elixir of Vigilance
      slot: consumables
      note: 'SELECTED standing elixir — drink one every long rest, exactly as Asterion drinks Giant Strength. +5 Initiative AND immunity to Surprise, lasting until long rest, for about 25g from Danthelon''s, Kith in Grymforge, or Popper at the Circus. THIS REPLACES THE ALERT FEAT Gale cannot afford: BG3 rolls initiative on a d4 + DEX, not a d20, so +5 is larger than the entire die. Gale is the only party member with no competing elixir — Asterion needs Giant Strength and Bonbon wants Bloodlust — so the one-elixir-per-rest slot is free for him. This also settles the Hellrider''s Longbow contest in Bonbon''s favour permanently.'
    - id: bow-of-awareness
      item: Bow of Awareness
      slot: ranged weapons
      note: 'DEMOTED to a filler stat stick. +1 Initiative in an otherwise unused slot — worth taking because the slot is empty, but no longer the plan for Gale''s initiative. The standing Elixir of Vigilance gives +5 and Surprise immunity, which is strictly better and does not compete with Bonbon for Hellrider''s Longbow.'
    - id: bracers-of-defence
      item: Bracers of Defence (CONTESTED — goes to Asterion)
      slot: hands
      note: 'The published Sorlock guide calls these an early core item, and Gale does qualify (no armour, no shield). This party gives them to Asterion, whose unarmoured AC is doing more work. Gale sits at AC 13 + DEX 3 = 16 from Draconic Resilience through Act 1 and relies on Shield for spikes.'
    - id: safeguard-shield
      item: Safeguard Shield (DROPPED from this build)
      slot: shields
      note: 'Was core on the Storm build for +2 AC and +1 to all saves protecting Haste concentration. Dual Wielder at character level 4 takes the off-hand permanently, so Gale gives this up. It is the main defensive regression of the switch — free it for another party member.'
    act2:
    - id: hat-of-fire-acuity
      item: Hat of Fire Acuity
      slot: head
      note: 'CORE — the item that turns the build on. Carried by the Strange Ox at Dammon''s blacksmith in Last Light Inn. Dealing Fire damage grants 2 turns of Arcane Acuity, capped at 10; each remaining turn is +1 spell attack AND +1 spell save DC. Because each Scorching Ray ray deals Fire damage separately, one level-4 cast (5 rays) takes Gale from 0 to the 10 cap. ⚠ DO NOT kill the Strange Ox at the Druid Grove in Act 1 — it does not carry the hat until Last Light. If you miss it in Act 2, the Ox reappears in Rivington on a hill west of the requisitioned barn in Act 3.'
    - id: ring-of-mental-inhibition
      item: Ring of Mental Inhibition
      slot: rings
      note: 'CONTROL ring, in a locked chest in the House in Deep Shadows, just east of the Shadowed Battlefield waypoint. When a foe fails a save against Gale''s spells they gain Mental Fatigue for 2 turns, which stacks the odds on the next Command. ⚠ Per the wiki it does NOT trigger on the saves a creature makes to shake off an existing effect, so it does not extend Hold Person. It also feeds Boots of Stormy Clamour, since applying it is inflicting a condition.'
    - id: callous-glow-ring
      item: Callous Glow Ring
      slot: rings
      note: 'DAMAGE ring, in the opulent chest in the vault room near Balthazar in the Gauntlet of Shar. +2 Radiant damage against ILLUMINATED targets — applied per ray, so up to +14 on a level-6 Scorching Ray. The radiant damage also procs Gloves of Belligerent Skies. ⚠ Take it off against Shar worshippers and Justiciars.'
    - id: coruscation-ring
      item: Coruscation Ring
      slot: rings
      note: 'THE illumination engine, and the reason the light rules do not conflict with Charles. Per the wiki, Coruscation applies Radiating Orb when the WEARER is illuminated — the target does not need to be lit. Radiating Orb then makes the target Illuminated, which is what switches on Callous Glow. So the chain is: light on GALE → ray 1 applies Radiating Orb → the target is now lit → rays 2+ each add Callous Glow''s 2 radiant → which re-procs Belligerent Skies. Charles can stand in his Darkness cloud the entire time; none of this touches him. ⚠ Three good rings for two slots — run Callous Glow + Coruscation for damage fights and swap Coruscation for Mental Inhibition when the plan is Command spam.'
    - id: spineshudder-amulet
      item: Spineshudder Amulet
      slot: amulets
      note: 'PROMOTED TO CORE by this build. In the Mimic in Isobel''s bedroom on the upper floor of Moonrise. It applies Reverberation on ranged SPELL-ATTACK hits only — which made it near-worthless for the old save-based Storm nukes, and makes it excellent now that Gale''s main spell is 3–7 spell attacks per cast. Combined with Boots of Stormy Clamour it reliably knocks single targets Prone.'
    - id: evasive-shoes
      item: Evasive Shoes (damage-focus alternative)
      slot: feet
      note: 'Sold by Mattis at Last Light. Swap in over Boots of Stormy Clamour for fights where Gale is purely nuking and the Reverberation engine is not the plan.'
    - id: potent-robe
      item: Potent Robe (DEMOTED)
      slot: armour
      note: 'Alfira at Last Light, only if she survived Act 1. Adds CHA to CANTRIP damage — which was strong for the old Shocking Grasp turns and is nearly dead here, since this build stops casting cantrips in combat after character level 3. Keep it only as a generic robe until Armour of Landfall.'
    act3:
    - id: markoheshkir
      item: Markoheshkir
      slot: weapons
      note: 'CORE main hand, in a Globe of Invulnerability in Ramazith''s Tower (See Invisibility + DC 20 Arcana to disable the globe). +1 spell attack and DC, plus Arcane Battery for one free spell of any level. Attune Kereska''s Favour to FLAME OF WRATH (not Bolts of Doom as on the old build): fire resistance, +proficiency bonus to Fire spell damage, and Heat generation. ⚠ Attuning also starts unavoidable Heat self-damage each turn, which threatens Twinned Haste — hold off on attuning until Armour of Landfall is equipped.'
    - id: rhapsody
      item: Rhapsody
      slot: weapons
      note: 'CORE off hand, carried by Cazador Szarr. Scarlet Remittance stacks +1 attack, damage, AND spell save DC per kill, up to 3. This build uses all three, and the damage applies per ray. Requires Dual Wielder to hold alongside Markoheshkir. ⚠ Per the wiki, as of Patch 5 it only builds on killing living hostile targets.'
    - id: staff-of-spellpower
      item: Staff of Spellpower (off-hand swap)
      slot: weapons
      note: 'CARRY BOTH, SWAP PER FIGHT. Rated S-tier. Gives +1 spell save DC and +1 spell attack IMMEDIATELY, plus its own Arcane Battery — a second free spell of any level per long rest, stacking with Markoheshkir''s. Rhapsody is better in long, adds-heavy fights that actually generate kills, because its damage bonus applies per ray and its stacks reach +3/+3/+3. Spellpower is better in short boss fights and against undead or constructs, where Rhapsody may never build a single stack (since Patch 5 it only stacks on killing LIVING hostile targets). Two free high-level spells per rest is a large swing for a build this long-rest hungry.'
    - id: spellmight-gloves
      item: Spellmight Gloves
      slot: hands
      note: 'PROMOTED TO CORE by this build. Rewarded by Lucretious for Find Dribbles the Clown at the Circus (pickpocketable). −5 to spell attack rolls for +1d8 damage — previously rejected for Gale because Storm''s core nukes were save-based, and now excellent because Scorching Ray is an attack roll. MANAGE THEM: cast the first Scorching Ray with the gloves OFF to build Arcane Acuity, then switch them ON once Acuity covers the −5.'
    - id: armour-of-landfall
      item: Armour of Landfall
      slot: armour
      note: 'CORE armour, sold by Lorroakan''s Projection or Rolan on the ground floor of Sorcerous Sundries. AC 13 + DEX light armour, +1 Spell Save DC, and — the real reason — ADVANTAGE ON CONSTITUTION SAVING THROWS. That advantage is what replaces the Halfling Luck and War Caster this build cannot have, and it is what makes Markoheshkir''s Heat damage safe to carry while concentrating on Twinned Haste.'
    - id: cloak-of-the-weave
      item: Cloak of the Weave
      slot: cloaks
      note: 'Sold by Helsik at the Devil''s Fee once her special stock is unlocked. +1 Spell Save DC and +1 spell attack rolls. ⚠ The wiki notes its Absorb Elements ability is bugged and non-functional; take it for the flat +1/+1, which is what the build actually wants.'
    - id: hellriders-longbow
      item: Hellrider's Longbow (CONTESTED with Bonbon)
      slot: ranged weapons
      note: 'Sold by Ferg Drogher in Rivington. The published guide says it should always go to the Sorlock on fire parties, but this party''s loot plan assigns it to Bonbon, who needs to land the first weapon hit to open her Band of the Mystic Scoundrel loop. Gale has no Alert feat, so whoever loses this keeps Bow of Awareness and drinks an Elixir of Vigilance for the fights where going first is critical.'
    - id: birthright
      item: Birthright (NOT usable on this build)
      slot: head
      note: 'Would give +2 CHA, but the head slot belongs permanently to the Hat of Fire Acuity — without Acuity the whole build stops working. Birthright goes to Bonbon instead.'
  playstyle: |-
    - **Once per long rest:** cast Daylight (Enchant Item) on Bonbon's main-hand weapon. It lasts until the next rest and keeps Gale lit for the Coruscation chain.
    - **Turn 1:** Twinned Haste (Action) if nobody else supplies it, then a Quickened Scorching Ray (bonus action) into a high-HP target with Spellmight Gloves OFF. A level-4 slot fires 5 rays and takes Arcane Acuity to its 10 cap.
    - **Turn 1 onward:** switch Spellmight Gloves ON. Acuity now covers the −5.
    - **Then pick a job each turn:** more Scorching Ray at a single target, Fireball at a cluster of 4+, or Extended Command at everything you want disabled. Command is not Concentration, so it never costs you Haste.
    - **Grouping:** Command: Approach pulls scattered enemies into one Fireball.
    - **Fire-immune fights** (House of Hope, Raphael, the red dragon, Yurgir): switch Markoheshkir to a lightning attunement and lead with Chain Lightning. Gale contributes far less to these than the old Storm build did — plan around it.
    - **Do not** drop Fireball on Charles or Asterion before Careful Spell arrives at character level 11.
  traps:
  - 'Strange Ox: do NOT kill it at the Druid Grove in Act 1. It only carries the Hat of Fire Acuity from Last Light onward, and that hat is the build. Missing it in Act 2 is recoverable — the Ox reappears in Rivington in Act 3 — but killing it early is not.'
  - 'Heat fights the rest of the Act 3 kit — TREAT FLAME OF WRATH AS A PER-FIGHT TOGGLE, not a permanent attunement. Markoheshkir''s Flame of Wrath deals unavoidable self-damage every turn, and three separate interactions make that worse than the old note implied: (1) Elemental Adept: Fire does NOT protect Gale — it pierces enemy resistance, it does not reduce damage he takes; (2) the Callous Glow Ring adds +2 radiant to Gale''s OWN Heat tick whenever he is Illuminated, and the Coruscation chain keeps him Illuminated on purpose, so his damage ring amplifies his own self-damage; (3) any damage taken strips 2 turns of Arcane Acuity, so every tick chips the exact stat the build exists to stack, on top of forcing a CON save against Twinned Haste. Gale is Human, so there is no Halfling Luck. Do not attune Flame of Wrath until Armour of Landfall is equipped, and consider dropping Coruscation in fights where Acuity uptime matters more than the radiant riders.'
  - 'Only two feats: Sorc 4 and Sorc 8 (character levels 4 and 9). Dual Wielder and Elemental Adept consume both, so there is no Alert and no War Caster — but BOTH gaps are now solved by consumables and gear rather than left open. Alert is replaced by a standing Elixir of Vigilance (+5 Initiative, Surprise immunity, no competing elixir on Gale). War Caster is replaced by Spidersilk Armour''s CON-save advantage from Act 1, upgraded to Armour of Landfall in Act 3. Note the published tier lists rate Elemental Adept only B while Alert is one of two S+ feats — the Vigilance elixir is what makes spending a feat on Elemental Adept acceptable.'
  - 'SPELLMIGHT GLOVES ARE UNTESTED — verify before building around them. The whole case for promoting them to core is that −5 spell attack / +1d8 damage applies to EACH Scorching Ray ray, but the wiki never addresses whether the +1d8 is per attack roll or once per spell, and Spellmight is absent from the per-instance notes that DO explicitly name Elemental Affinity and the Callous Glow Ring. On a 7-ray cast the two readings are +7d8 (~31, best in slot) versus +1d8 (~4.5 for a −5 penalty on all seven rolls, actively harmful). Test it on a single cast the moment they are acquired.'
  - 'Fireball friendly fire: Careful Spell is the fourth metamagic at Sorc 10 (character level 11). For the entire run before that, Fireball is an adds-cluster tool and Scorching Ray is the boss tool.'
  - 'Long rests: this build burns slots much faster than the Storm chassis, especially if you lean into damage rather than Command. Bank camp supplies and use Potions of Angelic Slumber in Act 3.'
  - 'Command does not work on Undead, and neither Hold spell works on crit-immune enemies — the same gap Bonbon already has. Act 2 has a lot of Undead; lean on Fireball and Scorching Ray there.'
  - 'Warlock slot question: the published Command-spam loop assumes Gale can cast Command from ordinary Sorcerer slots, not only from his single short-rest pact slot. Confirm this in play at character level 7 — if Command is restricted to the pact slot, the control lane is once per short rest and Bonbon stays the primary controller.'
  - 'Respec cost: Gale joins as a Wizard — bank ~100g for the Withers respec into Sorcerer, and re-pick metamagic and spells to match this plan. There are no further respecs.'
---
