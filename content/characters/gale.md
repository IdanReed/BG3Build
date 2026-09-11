---
nickname: Gale
builds:
- name: The Powder Keg
  is_primary: true
  role: Fire striker + non-concentration Command control + party Haste engine
  class: Sorcerer 11 (Draconic Bloodline — Red) / Fiend Warlock 1
  at_a_glance:
    armour: Light armour + shields (Human Civil Militia, Warlock 1) — never a shield in practice, both hands hold staves
    elixir: Vigilance every long rest — +5 Initiative and Surprise immunity, the Alert feat he cannot afford
    concentration: Twinned Haste on Charles and Bonbon — Command is his control because it needs none
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
  stats_note: 'Point-buy base 8/15/14/8/10/15 = all 27 points (DEX 15 and CHA 15 cost 9 each, CON 14 costs 7, WIS 10 costs 2). Then Human +2 → CHA 17 and +1 → DEX 16. DEX 16 is load-bearing: Draconic Resilience sets unarmoured AC to 13 + DEX, and both Spidersilk Armour and Armour of Landfall are 13 + DEX light armour, so DEX is Gale''s entire AC. WIS sits at 10 because nothing in the build keys off it.'
  ability_targets: 'MODDED Hair: CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss, Cloister of Sombre Embrace in Act 3). CHA 20 is the target and no ASI is needed to reach it, which is what frees both feats for Dual Wielder and Elemental Adept. Birthright (+2 CHA → 22) is NOT worn by anyone in this party: Gale''s head belongs permanently to the Hat of Fire Acuity and Bonbon''s to the Helmet of Arcane Acuity, and +2 Charisma is +1 spell save DC against Acuity''s +10. Keep it bagged as an out-of-combat dialogue swap.'
  ability_scores:
  - ability: STR
    steps:
    - score: 8
      source: 'point-buy'
  - ability: DEX
    steps:
    - score: 15
      source: 'point-buy'
    - score: 16
      source: '+1 Racial'
  - ability: CON
    steps:
    - score: 14
      source: 'point-buy'
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
  metamagic:
  - Twinned + Extended (Sorc 2)
  - Quickened (Sorc 3)
  - Careful (Sorc 10 / char 11)
  feats:
  - at: Sorc 4 (char 4)
    feat: Dual Wielder
    note: 'Unusual for a caster, but this build wields two staves as stat sticks: Spellsparkler + Melf''s in Act 1, then Markoheshkir + Rhapsody in Act 3. Neither pair is Light, so Dual Wielder is mandatory to hold both. COST: both hands are full for the whole run, so Gale can never carry a shield — Spidersilk Armour in Act 1 and Armour of Landfall in Act 3 supply the Constitution-save advantage that protects Twinned Haste instead.'
  - at: Sorc 8 (char 9)
    feat: 'Elemental Adept: Fire'
    note: 'Effectively mandatory in THIS party, though the tier lists rate the feat only B in general — worth knowing you are spending one of two feats on a B-tier pick while Alert (S+) goes unbought. The published guide says to skip Elemental Adept if you have a bow archer who can mass-apply Arsonist''s Oil with Arrows of Many Targets or Volley; Bonbon shoots Titanstring all game but Swords Bard has no Volley, so the mass-apply would hang on a scarce stock of Arrows of Many Targets and in practice she strips fire resistance one target at a time, and Act 3 is dense with fire-resistant enemies. ⚠ READ THE WIKI TEXT, NOT THE TABLETOP RULE: in BG3 you "CANNOT ROLL A 1" on Fire damage dice rather than treating 1s as 2s — still excellent here because Scorching Ray rolls so many dice. And the resistance-piercing covers "spells you cast AND attacks you make," not spells alone; only the no-1 clause is spell-only.'
  feats_note: 'ONLY TWO FEATS. Sorcerer grants them at Sorc 4 and Sorc 8 = character levels 4 and 9; the Warlock level grants none and Sorc 12 is never reached. Dual Wielder and Elemental Adept consume both, so there is no room for Alert, War Caster, or an ASI — initiative and concentration are gear problems on this build.'
  key_spells:
  - Scorching Ray (the core damage engine — every rider applies per ray)
  - Fireball (AoE; Careful Spell only arrives at char 11)
  - Haste (Twinned — the party engine, online at char 5)
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
    notes: 'CON + CHA save proficiency from character level 1, and Twinned Haste online at character level 5. Gale supplies no Guidance, Bless, Healing Word, Bane or Create Water — see the party plan''s Act 1 coverage table for who owns each of those instead.'
  spells:
    note: 'Sorcerer is a KNOWN caster (learn on level-up, replace 1 per level); 12 spells known at Sorc 11, plus the free Burning Hands. The Warlock level adds Command and Hex as separately-known Warlock spells. Mandatory = the Scorching Ray damage engine, Twinned Haste, and Command; Recommended = flex utility.'
    mandatory:
    - spell: Scorching Ray
      tier: A
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (31:43) — each ray applies on-hit riders and stacks fire Arcane Acuity, but not efficient enough to win fights alone'
      level: '2'
      guide_level: 3
      school: Evocation
      save: Ranged spell attack (one roll per ray)
      when: Sorc 3 (char 3)
      why: 'THE build — though note the tier lists rate the spell itself only A, precisely because its value is "multi-hit riders, not efficiency," which is exactly how this build uses it. 3 rays at level 2, +1 ray per slot level above 2nd (a level 6 slot fires 7). Each ray is a separate attack roll AND a separate damage instance, so every flat rider applies to EVERY ray. ⚠ CONFIRMED per-ray by name on the wiki: Elemental Affinity: Damage and the Callous Glow Ring. INFERRED but not individually stated: Rhapsody and Markoheshkir''s +proficiency, which are covered only by the general rule that bonus damage from passives and conditions applies per instance. Spellmight''s +1d8 is NOT addressed anywhere — see the traps. That means +5 CHA, +2 Callous Glow, +3 Rhapsody, +4 Markoheshkir, +1d8 Spellmight, and Phalar Aluve''s Shriek 1d4 Thunder (Charles''s until the Resonance Stone, Bonbon''s from her melee set after) all multiply by the ray count. It is also the Hat of Fire Acuity engine: each ray deals Fire damage and grants 2 turns of Arcane Acuity, so one level-4 cast caps Gale at 10 stacks.'
    - spell: Command
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (28:37) — concentration-free turn denial that upcasts to multiple enemies; every higher-level slot competes with it'
      level: '1'
      guide_level: 7
      school: Enchantment
      save: WIS save
      when: Warlock 1 (char 7)
      why: 'The single biggest reason to take the Warlock level: Command does NOT use Concentration, so Gale can hold Twinned Haste and still control every turn. Extended Spell doubles the condition to two turns. Approach also groups enemies for Fireball. Does not work on Undead.'
    - spell: Haste
      tier: S
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (6:12) — the most direct action-economy buff in the game. ON HONOUR MODE the extra action gives only one attack, not Extra Attack'
      level: '3'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Sorc 5 (char 5)
      why: 'Single-target so Twinnable; spend 3 Sorcery Points to Haste two of Charles / Asterion / Gale, online at character level 5. Ending Haste makes both targets Lethargic. ⚠ WHO GETS IT: Gale''s own hasted action is a second Scorching Ray, so self-Haste genuinely competes with hasting both martials — Charles + Asterion for adds-heavy fights, Gale + Charles for single-boss fights.'
    - spell: Fireball
      tier: B
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (38:58) — B not S: 13ft radius not 20ft, fire is widely resisted, Dex save for half. Do not cast it just because it is iconic'
      level: '3'
      guide_level: 6
      school: Evocation
      save: DEX save
      when: Sorc 6 (char 6)
      why: 'Primary AoE, and now on-element — Elemental Affinity, Flame of Wrath, and Elemental Adept all apply. ⚠ The tier lists rate Fireball only B — "do not cast it solely because it is iconic." It is correct to keep here because it is on-element for three separate multipliers, but do not prioritise it over another Scorching Ray on a single target; it earns its slot on clusters of 4+. ⚠ Careful Spell does not arrive until Sorc 10 (char 11), so for most of the run Fireball is an adds-cluster tool only and must not be dropped on Charles or Asterion.'
    - spell: Counterspell
      tier: S
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (25:08) — top-five spell; trades a reaction for an enemy turn. NO SCROLLS EXIST, so it must be learnt on level-up'
      level: '3'
      guide_level: 6
      school: Abjuration
      save: Reaction (no check at equal/higher slot)
      when: Sorc 6 (char 6) — replaces Magic Missile
      why: Shuts down enemy casters without using Concentration or an Action; competes with Shield for the Reaction, and both are worth keeping.
    - spell: Hold Person
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (55:42) — paralysis costs turns and gives automatic crits within 10 ft; humanoids only, best with high save DC'
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Sorc 4 (char 4)
      why: 'Paralysed humanoids take automatic critical hits from melee within 3m — Charles''s smite setup. Concentration, so Gale can only hold this INSTEAD of Haste; usually Bonbon owns the Hold lane and Gale owns Haste + Command. Take Hold Monster at Sorc 9 for non-humanoids.'
    - spell: 'Daylight: Enchant Item'
      tier: C
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (29:44) — a bigger Light cantrip for a level 3 slot; worth it mainly against Act 3 vampires, who are vulnerable to it'
      level: '3'
      guide_level: 8
      school: Evocation
      save: None
      when: Sorc 7 (char 8)
      why: 'Cast on an ally''s main-hand weapon out of combat; it is bugged to last until long rest, so this is a once-per-rest chore rather than a combat action. 15m radius that travels with the carrier. Its purpose is to keep GALE illuminated so the Coruscation Ring fires — see the illumination chain in the itemization notes. ⚠ Requires the target to hold a main-hand weapon, which rules out Asterion (empty hands for Tavern Brawler); Bonbon''s melee main hand is the clean carrier — the Knife of the Undermountain King until the Resonance Stone, Phalar Aluve after. Darkness is only dispelled at the moment of casting, so Charles''s Darkness Arrows fired afterwards are unaffected.'
    - spell: Chain Lightning
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (9:31) — 360 average damage on four wet enemies, but often needs two casts to end a fight'
      level: '6'
      guide_level: 12
      school: Evocation
      save: DEX save
      when: Sorc 11 (char 12)
      why: 'The answer to fire-immune enemies, which is a real gap now that the party has no lightning caster. Reserved for the House of Hope, Raphael, and the red dragon. Buy Globe of Invulnerability scrolls for the fights where you would rather have that instead.'
    recommended:
    - spell: Shield
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (43:07) — reaction +5 AC that only prompts when it turns a hit into a miss; worth a class dip on its own'
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None (Reaction, +5 AC)
      when: Sorc 1 (char 1)
      why: Gives Gale's otherwise-dead level-1 slots a job in the late game and sharply improves survival without touching Concentration.
    - spell: Hold Monster
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (30:07) — paralysis is devastating but costs a level 5 slot and caps at two targets'
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Sorc 9 (char 10)
      why: The non-humanoid version of the auto-crit setup. Concentration, so use it only in fights where someone else supplies Haste.
    - spell: Hex
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (21:08) — d6 on every attack roll all day, reapplied free on kills; enormous on multi-attack casters'
      level: '1'
      school: Enchantment
      save: None (Concentration)
      when: Warlock 1 (char 7)
      why: 'The second Warlock spell known. A per-ray damage rider in theory, but it uses Concentration and therefore competes with Haste — effectively a modded-difficulty option only. Armour of Agathys is the defensive alternative pick.'
    - spell: 'Chromatic Orb: Fire'
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (23:44) — damage plus a chosen surface with no concentration; ice surfaces are near-stuns and it bypasses immunities'
      level: '1'
      guide_level: 2
      school: Evocation
      save: Ranged spell attack
      when: Sorc 2 (char 2)
      why: 'Early on-element single-target damage before Scorching Ray arrives at char 3, and it creates a fire surface. ⚠ Rated S-tier — "exceptionally highly" — so think twice before treating it as a throwaway replacement candidate; its other elemental modes also cover the fire-immune enemies Gale otherwise has no answer to before Chain Lightning at char 12.'
    - spell: Ice Storm
      tier: A
      tier_note: 'Spells tier list, level 4, part 2 (Freedom of Movement through Wall of Fire) (20:00) — A because the 20 ft ice surface costs NO CONCENTRATION; the best follow-up after a control spell'
      level: '4'
      guide_level: 9
      school: Evocation
      save: DEX save
      when: Sorc 7+ (char 8+) — optional pick
      why: 'A-tier and NOT Concentration, which is the whole reason to consider it: Gale can drop it on a cluster while still holding Twinned Haste, unlike every other AoE of its size. It also lays an ice surface for prone control. Off-element, so it gets no Elemental Affinity, Flame of Wrath or Elemental Adept — take it only if the fire-resistance problem in Act 3 turns out worse than Elemental Adept can fix.'
    - spell: Burning Hands
      tier: C
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (18:26) — weak damage on a bad save; only Light Domain clerics, who get it free, will cast it'
      source: granted
      level: '1'
      guide_level: 1
      school: Evocation
      save: DEX save
      when: Sorc 1 (char 1) — FREE from Red ancestry
      why: Does not consume a spell-known pick. Genuinely useful for the first few levels as on-element AoE, and it is the reason to pick Red over Gold or Brass.
    - spell: Enhance Ability
      tier: B
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (36:31) — cast a couple of times a run; worth preparing for the few unavoidable skill checks'
      level: '2'
      guide_level: 3
      school: Transmutation
      save: None (Concentration)
      when: Sorc 3+ (replacement candidate)
      why: Out-of-combat advantage on a chosen ability check. Concentration, so treat it as an exploration mode only.
    - spell: Dimension Door
      tier: C
      tier_note: 'Spells tier list, level 4, part 1 (Banishment through Fire Shield) (25:57) — good in roughly three timed traversal encounters; jumping or Misty Step covers everything else'
      level: '4'
      guide_level: 9
      school: Conjuration
      save: None
      when: Sorc 8 (char 9)
      why: Repositions Gale and one ally out of a collapsing fight; also solves several Act 3 traversal problems.
    - spell: Telekinesis
      tier: B
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (41:29) — repeatable no-weight-limit throw for repositioning; BUGGED, a first-cast save cancels concentration'
      level: '5'
      guide_level: 11
      school: Transmutation
      save: STR save
      when: Sorc 10 (char 11)
      why: Concentration control that can repeatedly reposition a dangerous target or throw it from height. Competes with Haste, so it is a situational pick.
    - spell: Fire Bolt
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (24:40) — highest raw damage for wizards and sorcerers, and it lights fires at 60 feet'
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1 (char 1)
      why: 'On-element chip damage for the first three levels. This build stops using cantrips in combat after Scorching Ray arrives, so do not build around it — which is also why the Potent Robe, whose whole effect is CHA to cantrip damage, is not part of this loadout.'
    - spell: Friends
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (26:48) — advantage on Charisma checks; COUNTS AS A CRIME ON TACTICIAN AND HONOUR MODE, so hide or fast-travel afterwards'
      level: Cantrip
      guide_level: 1
      school: Enchantment
      save: None (Concentration)
      when: Sorc 1 (char 1)
      why: 'Advantage on Charisma checks. Bonbon is the party face, so this is a backup rather than a plan; the target turns hostile when it ends, so never use it somewhere you intend to stay.'
    - spell: Minor Illusion
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (35:56) — moves NPCs with no save or roll; clusters enemies for AoE, sets ambushes, pulls enemies one at a time'
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: Sorc 1 (char 1)
      why: Groups enemies before combat starts, which sets up a bigger opening Fireball and relocates NPCs for Asterion's theft routes.
    - spell: Mage Hand
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (33:23) — costs a short-rest charge, but scouts, triggers traps, throws potions and soaks one enemy attack'
      level: Cantrip
      guide_level: 1
      school: Conjuration
      save: None
      when: Sorc 1 (char 1)
      why: 'Exploration and object manipulation. It also covers the party''s lost Create Water: drop a water bottle where the Hand can reach and use its Throw for a 2m Wet splash when something needs to be Wet.'
    - spell: Light
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (30:38) — hands-free, concentration-free light lasting all day; most parties need some light source'
      level: Cantrip
      guide_level: 4
      school: Evocation
      save: None
      when: Sorc 4 (char 4) — fifth cantrip
      why: 'A free, slot-less way to keep GALE illuminated so the Coruscation Ring works, covering the whole stretch of Act 2 before Daylight is learned at char 8. Cast it on Gale''s own staff or on a nearby ally. ⚠ Worth confirming in play that a Light-lit character registers as Illuminated for Coruscation; if not, use an ordinary torch or Daylight.'
    - spell: Bone Chill
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (12:42) — turns off enemy healing with no save and blanks undead attack rolls; not the go-to damage cantrip'
      level: Cantrip
      guide_level: 7
      school: Necromancy
      save: Ranged spell attack
      when: Warlock 1 (char 7) — second Warlock cantrip
      why: 'A tier — "targets AC at range, prevents healing, and gives undead disadvantage on attacks." Take it with the Warlock cantrip slot rather than Friends, which Gale already knows from Sorcerer 1. It covers the Act 2 Undead that Command cannot touch.'
    - spell: Ray of Frost
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (41:42) — movement debuff lets you kite as a stun, doubles on wet enemies, and freezes surfaces'
      level: Cantrip
      guide_level: 11
      school: Evocation
      save: Ranged spell attack
      when: Sorc 10 (char 11) — sixth cantrip
      why: 'S tier — "the best broadly available elemental attack: Wet doubles its cold damage, the hit reduces movement without a save, and water can freeze into ice that knocks enemies prone." The sixth cantrip is easy to miss because it is the only one granted after char 4. Off-element on purpose: it is slot-free damage for the fire-immune fights where this build otherwise contributes little until Chain Lightning.'
    - spell: Globe of Invulnerability
      tier: S
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (26:18) — total damage immunity wins most boss fights outright; get one cast into every Honour party'
      level: '6'
      school: Abjuration
      save: None (Concentration)
      when: scroll only in this build
      why: 'Chain Lightning takes the single level-6 spell known, so buy Globe scrolls in Act 3 for the two or three fights that want it instead.'
    - spell: Misty Step
      tier: S
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (14:50) — top-five spell; bonus-action 60 ft teleport that every honour mode character should have access to'
      level: '2'
      guide_level: 4
      school: Conjuration
      save: None (bonus action)
      when: replacement candidate
      why: 'Escape mobility, and a low priority: Gale''s bonus action is normally committed to a Quickened Scorching Ray, and Draconic Fly arrives at Sorc 11.'
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
        - Draconic Ancestry (Red) — Fire becomes his ancestry damage type
        - CON + CHA saving-throw proficiency
        recommendations:
        - category: Subclass
          picks: 1
          recommendation: Draconic Bloodline — Red (Fire)
          note: 'Fire ancestry is what makes Elemental Affinity add CHA to Scorching Ray and Fireball at Sorc 6. Red grants Burning Hands free; Gold and Brass are also Fire but grant Disguise Self and Sleep instead.'
        - category: Ancestry spell
          granted: true
          recommendation: Burning Hands
          note: 'FREE, and it does not consume one of the two spell-known picks — Red ancestry simply grants it at Sorcerer 1. That is the reason to take Red over Gold or Brass, which grant Disguise Self and Sleep instead. Genuinely useful on-element AoE for the first few levels, and it stays known for the whole run at no cost.'
        - category: Cantrips
          picks: 4
          recommendation:
          - Fire Bolt
          - Friends
          - Minor Illusion
          - Mage Hand
          note: Cantrips are permanent and this build stops using them in combat after char 3, so choose utility over damage scaling.
        - category: Spells
          picks: 2
          recommendation:
          - Shield
          - Magic Missile
          note: 'Magic Missile gives way to Counterspell at Sorc 6. ⚠ The tier lists rate BOTH Shield and Magic Missile S, so weigh this one in play: Magic Missile NEVER MISSES, a genuinely rare property on a build whose entire damage output is attack rolls, and it is the clean answer to a turn where Scorching Ray would whiff or to finishing a low-HP caster. To keep it, drop a different flex spell for Counterspell instead.'
        - category: Skills
          picks: 3
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
          picks: 2
          recommendation:
          - Twinned Spell
          - Extended Spell
          note: 'Quickened is not selectable until Sorcerer 3. Twinned carries the Haste engine; Extended is what turns Command into a two-turn lockdown later.'
        - category: Spell
          picks: 1
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
          picks: 1
          recommendation: Quickened Spell
          note: 'Converts Scorching Ray into a bonus action, which is the whole gameplay loop: Quickened damage with the bonus action, then Extended Command or a second spell with the Action.'
        - category: Spell
          picks: 1
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
          picks: 1
          recommendation: Dual Wielder
          note: 'Lets Gale hold Spellsparkler + Melf''s First Staff together (neither is Light), and later Markoheshkir + Rhapsody. Both hands are full from here on, so no shield for the rest of the run.'
        - category: Cantrip
          picks: 1
          recommendation: Light
          note: Keeps Gale illuminated for the Coruscation Ring without spending a slot, well before Daylight is learned.
        - category: Spell
          picks: 1
          recommendation: Hold Person
          note: A second source of the paralysis that turns Charles's smites into automatic critical hits.
      - char_level: 5
        class: Sorcerer 5
        gains:
        - Level 3 Sorcerer spells
        - Five Sorcery Points
        recommendations:
        - category: Spell
          picks: 1
          recommendation: Haste
          note: The party Haste engine comes online here. Twinned costs 3 Sorcery Points.
      - char_level: 6
        class: Sorcerer 6
        gains:
        - 'Elemental Affinity: Damage (add CHA modifier to Fire spell damage)'
        - 'Elemental Affinity: Resistance (1 Sorcery Point → Fire resistance until long rest)'
        - Six Sorcery Points
        recommendations:
        - category: Spell
          picks: 1
          recommendation: Fireball
          note: Primary AoE, now boosted by Elemental Affinity.
        - category: Replacement
          picks: 1
          optional: true
          recommendation: Magic Missile → Counterspell
          note: 'Use the level-up replacement slot here. Elemental Affinity is the single biggest power spike in the build: +5 damage per ray at CHA 20.'
      - char_level: 7
        class: Fiend Warlock 1
        gains:
        - 'Pact Magic: 2 Warlock cantrips and 2 Warlock spells known — all four are picks'
        - 'Fiend Expanded Spell List: Burning Hands and Command become choosable options'
        - One level-1 pact slot (recharges on SHORT rest)
        - Dark One's Blessing (temporary HP on a kill)
        - Light armour proficiency (redundant — Gale already has it from Civil Militia)
        recommendations:
        - category: Patron
          picks: 1
          recommendation: The Fiend
          note: Fiend is what puts Command on the Warlock list. This is the only Warlock level Gale ever takes.
        - category: Spells
          picks: 2
          recommendation:
          - Command
          - Hex
          note: 'Command is the pickup. Hex is a concentration-competing damage rider that is mostly for modded difficulty; Armour of Agathys is the defensive alternative.'
        - category: Cantrips
          picks: 2
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
          picks: 1
          recommendation: 'Daylight'
          note: 'Take the Enchant Item variant in play. Level 4 slots also mean a 5-ray Scorching Ray, which is exactly the cast that caps Arcane Acuity at 10 stacks.'
      - char_level: 9
        class: Sorcerer 8
        gains:
        - Eight Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          picks: 1
          recommendation: 'Elemental Adept: Fire'
          note: 'Fire is the most resisted damage type in Act 3 and Bonbon''s Titanstring has no Volley to mass-apply Arsonist''s Oil. Also removes 1s from every Fire damage die.'
        - category: Spell
          picks: 1
          recommendation: Dimension Door
          note: Escape and traversal utility.
      - char_level: 10
        class: Sorcerer 9
        gains:
        - Level 5 Sorcerer spells
        - Nine Sorcery Points
        recommendations:
        - category: Spell
          picks: 1
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
          picks: 1
          recommendation: Careful Spell
          note: 'Finally lets Gale drop Fireball on a cluster that Charles or Asterion is standing in. Until this level, Fireball is an adds-only tool.'
        - category: Cantrip
          picks: 1
          recommendation: Ray of Frost
          note: 'The sixth cantrip — easy to miss, because this is the only level after char 4 that grants one. S tier: "the best broadly available elemental attack — Wet doubles its cold damage, the hit reduces movement without a save, and water can freeze into ice that knocks enemies prone." It patches this build''s one structural hole for free: Gale contributes almost nothing to the fire-immune fights (House of Hope, Raphael, the red dragon, Yurgir) until Chain Lightning at char 12, and a cantrip costs no slot. 3d8 at this level. Bone Chill is already taken at char 7, so Ray of Frost is the non-overlapping pick.'
        - category: Spell
          picks: 1
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
          picks: 1
          recommendation: Chain Lightning
          note: 'The fire-immune answer for the House of Hope and Raphael. A level-6 Scorching Ray also fires 7 rays, which is the build''s single biggest turn.'
  itemization:
    act1:
    - id: the-spellsparkler
      item: The Spellsparkler
      tier: A
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (26:53) — stacks Lightning Charges fast on multi-hit casters, though Melf''s is broader'
      slot: weapons
      note: 'SELECTED main hand, rewarded by Counsellor Florrick at Waukeen''s Rest for Rescue the Grand Duke. Rated A on the staves tier list, which names Scorching Ray specifically: each of the 3–5 separate damage instances grants 2 Lightning Charges, and charges give +1 to attack rolls and +1 Lightning damage, bursting for 1d8 at five stacks. ⚠ It carries no enchantment bonus, so it is a rider stick, not an accuracy stick — that is Melf''s job. ⚠ It is "Consumable by Gale" — wield it, do not feed it to the Netherese orb.'
    - id: melf-s-first-staff
      item: Melf's First Staff
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (15:30) — probably best in slot for most spellcasters for all of Act 1'
      slot: weapons
      note: 'SELECTED off hand from Blurg in the Underdark, equipped from character level 4 once Dual Wielder is taken. +1 Spell Save DC and +1 spell attack rolls, and the staves tier list rates it S — "the defining early caster bonus… often best through Acts 1 and 2." The +1 spell attack applies to every single ray, and the +1 DC is what carries his Command and Hold Person. ⚠ Neither staff is Light, so Dual Wielder is what makes the pair legal at all; before character level 4 he holds Spellsparkler alone.'
    - id: shadespell-circlet
      item: The Shadespell Circlet
      tier: S
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (41:43) — needs setup to get value, but spell save DC increases are that powerful'
      slot: head
      note: ACT 1 HEAD, from Omeluum after Help Omeluum Investigate the Parasite. +1 Spell Save DC while Gale is obscured. It is replaced permanently by the Hat of Fire Acuity in Act 2, so treat it as an Act 1 rental.
    - id: act1-feet-gale
      item: Boot slot
      slot: feet
      wiki: false
      note: 'OPEN, AND HONESTLY SO. The Boots of Stormy Clamour used to sit here and now go to CHARLES, because Gale''s Reverberation payload does not exist yet in Act 1 — Gloves of Belligerent Skies need Thunder, Lightning or Radiant damage and he casts fire, and Coruscation, Callous Glow and Spineshudder are all Act 2 pickups. His only Act 1 condition to convert was Command. ⚠ There is no good replacement: The Speedy Lightfeet, Boots of Striding, Boots of Elemental Momentum and Vital Conduit Boots ALL require Medium Armour proficiency, which Sorcerer/Warlock never grants, and the two best non-armour pairs in the act are already allocated. Evasive Shoes fix the slot properly at Last Light in Act 2.'
      options:
      - id: opt-night-walkers-gale
        item: Disintegrating Night Walkers
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (19:19) — probably the best boots in the game'
        rank: '#11'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #11 of 20 — short-rest Misty Step plus immunity to most movement-restricting surfaces'
        note: 'THE REALLOCATION WORTH CONSIDERING, currently Asterion''s from Nere in Grymforge. Rated the best boots in the game and #11 of the Act 1 top 20, and the relevant half is IMMUNITY TO BEING KNOCKED PRONE — Prone ends Concentration outright, and Gale carries Twinned Haste permanently while Asterion''s Bless is the one Concentration in the party nobody minds losing. Asterion also already has bonus-action Dash and Disengage from Step of the Wind, so the Misty Step is the smaller half of the item for him. Not taken by default because it re-cuts his kit, not just this slot.'
      - id: opt-watersparkers-gale
        item: The Watersparkers
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (35:24) — core item for lightning-charge builds; needs water and the Sparkswall ring'
        note: 'Non-armour, so legal on him, and in a gilded chest in Minthara''s area of the Shattered Sanctum — the same stop as Charles''s Boots of Striding. Electrifies water he stands in and pays 3 Lightning Charges a turn for doing it. Situational to the point of being a swap-in, and it wants The Sparkswall to stop him being electrocuted by his own puddle.'
      - id: opt-boots-of-aid-and-comfort-gale
        item: Boots of Aid and Comfort
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (4:11) — 3 temp HP on every heal; combines with Hellrider''s Pride and Whispering Promise'
        note: 'Sold by Grat the Trader at the Goblin Camp. 3 temporary hit points to anyone he heals — rated S on the strength of the healing set, and worth nothing here, because Gale heals nobody. Listed only so the slot''s whole field is visible.'
    - id: gloves-of-belligerent-skies
      item: Gloves of Belligerent Skies
      tier: A
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (20:24) — excellent for specific builds and decent across a wide variety of them'
      slot: hands
      bis: true
      note: 'SELECTED late-Act-1 gloves, in the elegant chest in the Crèche Inquisitor''s Chamber. Thunder, Lightning or RADIANT damage applies 2 turns of Reverberation — and once the Callous Glow Ring is online in Act 2 every ray deals 2 radiant, so these proc per ray. ⚠ Charles has a real claim on them (Divine Smite is Radiant, and the wiki notes Phalar Aluve''s Shriek Thunder triggers them correctly in Honour Mode specifically) — they stay with Gale because he applies the rider 5–7 times per cast against Charles''s two swings.'
    - id: pearl-of-power-amulet
      item: Pearl of Power Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (35:16) — a mainstay once acquired'
      slot: amulets
      note: SELECTED resource neck from Omeluum. Restores one spell slot of level 3 or lower each long rest — normally another Haste or Scorching Ray. This build empties its slots fast, so a free one every rest is real.
    - id: spidersilk-armour
      item: Spidersilk Armour
      tier: S
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (16:13) — S specifically for light-armour casters, which is not what it looks designed for'
      slot: armour
      bis: true
      note: 'SELECTED Act 1 chest, and the answer to this build''s worst structural problem. Worn by Minthara in the Shattered Sanctum — the same kill that yields Charles''s Boots of Striding, so it costs nothing extra to acquire. AC 12 + DEX and +1 Stealth, but the reason to wear it is ADVANTAGE ON CONSTITUTION SAVING THROWS. Gale has no War Caster, no feat left to buy one, and no shield once Dual Wielder fills both hands, so this is his only protection for Twinned Haste — and it arrives in Act 1 rather than waiting for Armour of Landfall in Act 3. ⚠ Costs exactly 1 AC versus going unarmoured, since Draconic Resilience is 13 + DEX; take the trade, because Haste is the concentration the entire party plan is built on.'
    - id: elixir-of-vigilance
      item: Elixir of Vigilance
      tier: S
      tier_note: '9BcQXb37Bik (57:59) — rated S+ ABOVE THE SCALE: a free Alert feat, and +5 on a d4 initiative roll means going first'
      slot: consumables
      note: 'SELECTED standing elixir — drink one every long rest, exactly as Asterion drinks Giant Strength. +5 Initiative AND immunity to Surprise, lasting until long rest, for about 25g from Danthelon''s, Kith in Grymforge, or Popper at the Circus. THIS IS WHAT REPLACES THE ALERT FEAT Gale cannot afford: BG3 rolls initiative on a d4 + DEX, not a d20, so +5 is larger than the entire die. Gale is the only party member with no competing elixir — Asterion and Bonbon need Giant Strength and Charles wants Bloodlust — so the one-elixir-per-rest slot is free for him.'
    - id: bow-of-awareness
      item: Bow of Awareness
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (16:30) — going first is among the best things you can do in an Honour run'
      slot: ranged weapons
      note: ACT 1 ranged filler. +1 Initiative in a slot he otherwise leaves empty, stacking with the standing Elixir of Vigilance. He never fires it; Hellrider Longbow replaces it in Act 3 for +3.
    - id: ring-of-protection
      item: Ring of Protection
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (34:55) — raises the party''s average AC; give it to the easiest-to-hit member'
      rank: '#20'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #20 of 20 — +1 AC and all saves fits almost anyone, for the whole game'
      slot: ring 1
      note: 'HIS, not Asterion''s. Mol''s reward for Steal the Sacred Idol once the Grove resolves, and rated #20 of 20 with the note that it should "shore up the party''s lowest AC." That is Gale: Spidersilk puts him at AC 15, against Asterion''s 21 unarmoured. The +1 to all saving throws is also concentration insurance for Twinned Haste, which is what the party plan rests on. Asterion takes the Bracing Band instead and loses nothing.'
    - id: ring-of-mind-shielding
      item: Ring of Mind-Shielding
      tier: D
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (32:22) — a weak situational effect by the point in the game where you get it'
      slot: ring 2
      note: 'Offered by Omeluum in the Ebonlake Grotto after his quest — persuade, intimidate, pay, trade a story, or pickpocket. Advantage on saving throws against Charmed. A charmed Gale is a dropped Haste and a Fireball pointed at his own party, so this is concentration protection as much as it is a save. The wiki calls it "particularly useful in Act One" for the Harpies'' Luring Song.'
    - id: act1-cloak-gale
      item: No cloak exists yet
      slot: cloaks
      note: Deliberately empty. The only magical cloak obtainable anywhere in Act 1 is the Dark Urge's Deathstalker Mantle, which goes to Asterion. Gale's slot opens at Last Light in Act 2.
    act2:
    - id: hat-of-fire-acuity
      item: Hat of Fire Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (28:32) — removes enemies as threats almost instantly with a lot of builds'
      slot: head
      bis: true
      note: 'CORE — the item that turns the build on. Carried by the Strange Ox at Dammon''s blacksmith in Last Light Inn. Dealing Fire damage grants 2 turns of Arcane Acuity, capped at 10; each remaining turn is +1 spell attack AND +1 spell save DC. Because each Scorching Ray ray deals Fire damage separately, one level-4 cast (5 rays) takes Gale from 0 to the 10 cap. ⚠ DO NOT kill the Strange Ox at the Druid Grove in Act 1 — it does not carry the hat until Last Light. If you miss it in Act 2, the Ox reappears in Rivington on a hill west of the requisitioned barn in Act 3.'
    - id: callous-glow-ring
      item: Callous Glow Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
      slot: ring 1
      bis: true
      note: 'DAMAGE ring, in the opulent chest in the vault room near Balthazar in the Gauntlet of Shar. +2 Radiant damage against ILLUMINATED targets — and the wiki names Scorching Ray explicitly among the multi-instance spells that apply it per instance, so up to +14 on a level-6 cast. The radiant damage also procs Gloves of Belligerent Skies. ⚠ Take it off against Shar worshippers and Justiciars. ⚠ It stays with Gale rather than moving to Asterion or Bonbon because his ray count is the highest in the party and his own Coruscation Ring is what illuminates the target in the first place.'
    - id: coruscation-ring
      item: Coruscation Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (6:49) — good even outside Radiating Orb builds, and incredible inside them'
      slot: ring 2
      bis: true
      note: 'THE illumination engine, in a trapped heavy chest in the Last Light cellar. Per the wiki, Coruscation applies Radiating Orb when the WEARER is illuminated — the target does not need to be lit. Radiating Orb then makes the target Illuminated, which is what switches on Callous Glow. So the chain is: light on GALE → ray 1 applies Radiating Orb → the target is now lit → rays 2+ each add Callous Glow''s 2 radiant → which re-procs Belligerent Skies. Radiating Orb is also −1 to the target''s attack rolls per remaining turn, so it is a party-wide accuracy debuff. Charles can stand in his Darkness cloud the entire time; none of this touches him.'
    - id: act2-ring2-gale-flex
      item: Second ring alternatives
      slot: ring 2
      wiki: false
      note: 'Coruscation Ring is the default because it converts his illuminated spell damage into Radiating Orb. These are the swaps worth knowing.'
      options:
      - id: ring-of-mental-inhibition
        item: Ring of Mental Inhibition
        tier: B
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (24:59) — powerful if the party is carefully built around it, but it needs very specific builds'
        note: 'House in Deep Shadows. Applies Mental Fatigue whenever an enemy fails a save against him, compounding with his own DC. Take it in fights where his Command matters more than his rider damage.'
      - id: opt-ring-of-free-action-gale
        item: Ring of Free Action
        tier: C
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (21:55) — some minor uses; a swap-in against enemies that paralyse or Hold Person'
        note: 'Ignore difficult terrain and immunity to Paralysed and Restrained. Broadly good on anyone, and it protects the Twinned Haste concentration he can never afford to drop.'
    - id: spineshudder-amulet
      item: Spineshudder Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:42) — busted on multi-hit spells'
      slot: amulets
      note: 'CORE neck, in the Mimic in Isobel''s bedroom on the upper floor of Moonrise. It applies Reverberation on ranged SPELL-ATTACK hits only — which is exactly what Gale makes, 3–7 times a cast. Paired with the Gloves of Belligerent Skies, which fire on the Callous Glow radiant of every ray, that is roughly 28 turns of Reverberation from one Scorching Ray against a threshold of 5, so single targets go Prone repeatedly: five stacks force a Constitution save that the same condition''s own penalty makes effectively DC 15. This pair is the whole engine, which is why the Boots of Stormy Clamour could leave for Charles without costing him anything.'
    - id: cloak-of-protection-gale
      item: Cloak of Protection
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (13:30) — excellent, and someone in the party will almost certainly be wearing it'
      slot: cloaks
      note: 'NOT HIS, though he is the obvious candidate. It is the only cloak in the Act 2 pool that touches saving throws, and exactly one exists. Charles gets it because he carries a permanent DISADVANTAGE on every save from the Risky Ring while holding concentration in melee; Gale already has Constitution-save advantage from Spidersilk Armour plus save proficiency from level 1, and can be positioned out of danger. Recorded here so the decision is visible rather than silent.'
    - id: thunderskin-cloak
      item: Thunderskin Cloak
      tier: D
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (19:42) — needs a reverberation build and a fixed DC13 Constitution save; will practically never trigger'
      slot: cloaks
      note: 'HIS ACT 2 CLOAK, sold by Araj Oblodra at Moonrise. When a creature with Reverberation damages the wearer, it must make a DC 13 Constitution save or be Dazed — no Reactions, disadvantage on Wisdom saves, and it loses its Dexterity bonus to AC. The synergy is real rather than incidental: Gale is the party''s largest source of Reverberation (Spineshudder and Belligerent Skies each fire per ray), so essentially anything that reaches him is already Reverberating, and the Dazed WIS-save penalty then feeds his own Command.'
    - id: act2-armour-gale
      item: Spidersilk Armour
      tier: S
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (16:13) — S specifically for light-armour casters, which is not what it looks designed for'
      held: 1
      slot: armour
      bis: true
      note: 'CARRIED OVER, and never swapped. Advantage on Constitution saving throws is what protects Twinned Haste, the single effect this party is built around. It is also why the Potent Robe is refused.'
    - id: act2-hands-gale
      item: Gloves of Belligerent Skies
      tier: A
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (20:24) — excellent for specific builds and decent across a wide variety of them'
      held: 1
      slot: hands
      bis: true
      note: 'CARRIED OVER. Thunder, Lightning or Radiant damage applies Reverberation — and a multi-ray cast applies it 3-7 times, which is why these live on him rather than on Charles.'
    - id: act2-feet-gale
      item: Evasive Shoes
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (46:17) — a lot of parties will simply use them'
      slot: feet
      bis: true
      note: 'HIS SLOT IS FIXED HERE, sold by Mattis at Last Light Inn. +1 Armour Class and +1 Acrobatics, rated S by the boots list, no proficiency requirement, and contested by nobody. A flat AC point is concentration protection on a caster whose only job is keeping Twinned Haste up — the fewer hits, the fewer saves. ⚠ Modest, and forced: Boots of Persistence, Vital Conduit Boots and The Speedy Lightfeet all require Medium Armour proficiency, which Sorcerer 11 / Warlock 1 never grants, and Helldusk goes to Charles. ⚠ Boots of Stormy Clamour are no longer his — by Act 2 he applies roughly 28 turns of Reverberation per Scorching Ray from Belligerent Skies and Spineshudder alone, against a threshold of 5, so the boots were adding nothing he was not already three times over.'
      options:
      - id: opt-acrobat-shoes-gale
        item: Acrobat Shoes
        tier: D
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (36:55) — advantage on Dex saves is available elsewhere; not worth the boot slot'
        note: 'THE ALTERNATIVE, and arguably the better one, sold by Barcus Wroot at his Last Light workshop. ADVANTAGE ON DEXTERITY SAVING THROWS, which is the exact save Gale has no cover for — Armour of Landfall and Spidersilk both hand him Constitution-save advantage, and nothing in the kit touches Dexterity. Fireballs and breath weapons are what actually take Twinned Haste off him. Rated D by the boots list on the grounds that the effect is available elsewhere; it is not available elsewhere on this character.'
    - id: act2-weapons-gale
      item: The Spellsparkler
      tier: A
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (26:53) — stacks Lightning Charges fast on multi-hit casters, though Melf''s is broader'
      held: 1
      slot: weapons
      note: 'CARRIED OVER main hand. Lightning Charges off every separate Scorching Ray instance. It carries no enchantment bonus, so it is a rider stick rather than an accuracy stick.'
    - id: act2-offhand-gale
      item: Melf's First Staff
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (15:30) — probably best in slot for most spellcasters for all of Act 1'
      held: 1
      slot: weapons
      note: 'CARRIED OVER off hand, legal only because Dual Wielder was taken at character level 4 — neither staff is Light. This is the +1 Spell Save DC and +1 spell attack rolls that the Incandescent Staff does not give.'
    - id: act2-ranged-gale
      item: Bow of Awareness
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (16:30) — going first is among the best things you can do in an Honour run'
      held: 1
      slot: ranged weapons
      note: 'CARRIED OVER, and purely for the passive initiative. He never fires it.'
    - id: drakethroat-glaive
      item: Drakethroat Glaive
      tier: S
      tier_note: 'GunWjIpdxb0 (39:52) — free daily Elemental Weapon cast onto any weapon without spending your own slot'
      wiki: Drakethroat Glaive
      slot: other
      note: 'BACKPACK ITEM — bought from Roah Moonglow at Moonrise for 960 gp and NEVER EQUIPPED IN COMBAT, because both hands belong to the staves. It is carried for one action per long rest: Draconic Elemental Weapon, a free level 3 cast off the item. Human Civil Militia gives Gale the glaive proficiency, and Twinned Spell (3 sorcery points) doubles the cast, so out of combat he equips the glaive, Twins the enchant onto BONBON''S TITANSTRING BOW and CHARLES''S MAIN HAND, and swaps the staves back. Titanstring is her ranged weapon all game, so the bow half never changes; Charles''s half is the one-handed Phalar Aluve behind his shield until the Resonance Stone and the 3d8 Shadow Blade after it, so from the Stone on he summons the blade first. Each target gets +1 Attack Rolls and +1d4 of one chosen element until long rest, stacking with Magic Weapon. ⚠ It only takes a weapon on the ground or an ally''s MAIN-HAND weapon, so Titanstring has to be dropped at his feet and re-equipped afterwards; Charles is targeted directly. ⚠ Both targets must be inside the 1.5m melee range, so drop the bow next to Charles. ⚠ Pick a damage type the fight ahead is not resistant to — Gale''s Elemental Adept: Fire does nothing for an ally''s weapon.'
    act3:
    - id: markoheshkir
      item: Markoheshkir
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (44:41) — universal caster best in slot: +1 DC and attacks, Arcane Battery, elemental attunement'
      slot: weapons
      bis: true
      note: 'CORE main hand, in a Globe of Invulnerability in Ramazith''s Tower (See Invisibility plus a DC 20 Arcana check to disable the globe). Rated S and called the universal caster best-in-slot. +1 spell attack and DC, plus Arcane Battery for one free spell of any level. Attune Kereska''s Favour to FLAME OF WRATH: fire resistance, +proficiency bonus to Fire spell damage applied per ray, and Heat generation. ⚠ Attuning also starts unavoidable Heat self-damage each turn, which threatens Twinned Haste — do not attune until Armour of Landfall is equipped.'
    - id: rhapsody
      item: Rhapsody
      tier: S
      tier_note: 'The BEST ROGUE WEAPONS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Part 2 (43:01) — +3 to everything, and best in slot as a stat stick even for characters not swinging it'
      slot: weapons
      note: 'CORE off hand, carried by Cazador Szarr. Scarlet Remittance stacks +1 attack, damage AND spell save DC per kill, up to 3. This build uses all three, and the damage applies per ray. Requires Dual Wielder to hold alongside Markoheshkir. ⚠ Per the wiki, as of Patch 5 it only builds stacks on killing living hostile targets, and the stacks are lost when the dagger is unequipped — so once he is at +3, it stays in his hand; verify in play whether the stacks survive a long rest.'
    - id: staff-of-spellpower
      item: Staff of Spellpower
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (48:32) — a mainstay; refreshing a spell slot on any slot for any purpose is that good'
      slot: weapons
      note: 'CARRY BOTH. Rated S. Gives +1 spell save DC and +1 spell attack IMMEDIATELY, plus its own Arcane Battery — a second free spell of any level per long rest, stacking with Markoheshkir''s. It is the off-hand until Rhapsody has its three living kills, and on any day that starts against undead or constructs, where Rhapsody cannot build a stack; once Rhapsody sits at +3 it stays, because unequipping it drops the stacks. Two free high-level spells per rest is a large swing for a build this slot-hungry.'
    - id: spellmight-gloves
      item: Spellmight Gloves
      tier: B
      tier_note: 'The BEST GLOVES In BG3 COMPLETE - Honor Mode Tier List and Guide - Act 3 (38:34) — B for Honour mode specifically; called absolutely busted for critical-hit warlocks on Tactician or below'
      slot: hands
      note: 'ACT 3 HANDS. Rewarded by Lucretious for Find Dribbles the Clown at the Circus, and pickpocketable. −5 to spell attack rolls for +1d8 damage — excellent precisely because Scorching Ray is an attack roll. MANAGE THEM: cast the first Scorching Ray with the gloves OFF to build Arcane Acuity, then switch them ON once Acuity covers the −5. ⚠ VERIFY ON THE FIRST CAST whether the +1d8 applies per ray or once per spell; the traps section explains why the two readings differ by roughly 27 damage.'
    - id: armour-of-landfall
      item: Armour of Landfall
      tier: A
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (31:23) — +1 save DC, Con save advantage and Plant Growth per short rest; only 13 AC'
      slot: armour
      note: 'CORE armour, sold by Lorroakan''s Projection or Rolan on the ground floor of Sorcerous Sundries. AC 13 + DEX light armour, +1 Spell Save DC, and — the real reason — ADVANTAGE ON CONSTITUTION SAVING THROWS. That advantage is what replaces the Halfling Luck and War Caster this build cannot have, and it is what makes Markoheshkir''s Heat damage safe to carry while concentrating on Twinned Haste. Warlock 1 supplies the Light Armour proficiency, and so does Human Civil Militia. ⚠ Robe of the Weave is the pure-damage alternative (+2 AC and +1 spell attack/DC) but has no Constitution-save advantage, so it loses for a Haste-concentration build.'
    - id: cloak-of-the-weave
      item: Cloak of the Weave
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (28:30) — best in slot for any caster'
      slot: cloaks
      note: 'ACT 3 CLOAK, sold by Helsik at the Devil''s Fee once her special stock is unlocked. +1 Spell Save DC and +1 spell attack rolls. ⚠ The wiki notes its Absorb Elements ability lacks the passives needed to function; take it for the flat +1/+1, which is what the build actually wants, and value it at that.'
    - id: hellriders-longbow
      item: Hellrider Longbow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (53:35) — +3 initiative from an unused slot; he would put it in S+ if it existed'
      wiki: Hellrider Longbow
      slot: ranged weapons
      note: 'HIS — the contest with Bonbon is settled by the item itself. Sold by Ferg Drogher in Rivington. Heightened Awareness gives +3 to Initiative and advantage on Perception, and it upgrades the Bow of Awareness he has been carrying since Act 1. ⚠ THE DECIDER: Bonbon''s ranged slot belongs to Titanstring for the whole game, and a bow cannot share it — she has no free ranged slot, and Gale has one he never otherwise uses. He holds it purely as a stat stick and never fires it; on top of the standing Elixir of Vigilance that is +8 initiative without a feat. ⚠ Ferg Drogher sells nothing if Shadowheart is nearby, unless she killed the Nightsong in Act 2.'
    - id: helldusk-boots-gale
      item: Helldusk Boots
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (1:00:13) — the saving throw makes the wearer extremely safe in almost every circumstance'
      slot: feet
      note: 'NOT HIS, and less close than it used to read. Infernal Evasion — spend a Reaction to turn a failed saving throw into a success — is ONCE PER LONG REST per the wiki, not once per turn, so it is an emergency button rather than standing concentration insurance. What actually decides the slot is the immunity to Prone, since Prone ends Concentration outright, and Charles is the frontliner who gets knocked down. Gale already has Constitution-save advantage from Armour of Landfall. Recorded so the trade is visible.'
    - id: act3-feet-gale
      item: Evasive Shoes
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (46:17) — a lot of parties will simply use them'
      held: 2
      slot: feet
      bis: true
      note: 'CARRIED OVER from Last Light and never replaced. +1 Armour Class and +1 Acrobatics. ⚠ NO BEST-IN-SLOT EXISTS FOR HIM: the Act 3 boots he would actually want are all locked out or spoken for — Boots of Persistence and Vital Conduit Boots require Medium Armour proficiency he never gets, Helldusk goes to Charles on the Prone immunity, and Boots of Uninhibited Kushigo are Asterion''s. Any of the below is a fine substitution.'
      options:
      - id: opt-acrobat-shoes-gale-a3
        item: Acrobat Shoes
        tier: D
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (36:55) — advantage on Dex saves is available elsewhere; not worth the boot slot'
        held: 2
        note: 'Same trade as Act 2 and it does not change: swap +1 AC for ADVANTAGE ON DEXTERITY SAVING THROWS. Dexterity is the one save nothing else in his kit covers, and it is the one Twinned Haste usually dies to.'
      - id: opt-boots-of-psionic-movement
        item: Boots of Psionic Movement
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (54:03) — bonus-action Fly once per long rest; strong for parties skipping illithid powers'
        note: 'Bonus-action Fly once per long rest, plus +1 to Dexterity saving throws. Real value on a backline caster who occasionally has to leave a melee lane, and the party is skipping illithid powers, so nothing else supplies flight.'
      - id: opt-boots-of-speed-gale
        item: Boots of Speed
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (11:29) — bonus-action double move; some party member almost always wants it (captions garble the letter)'
        rank: '#14'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #14 of 20 — bonus-action Dash gives anyone Rogue-grade mobility'
        note: 'Free once Bonbon moves to Boots of Brilliance in Act 2. Doubling movement as a bonus action is never wasted on a caster who wants distance from his own Heat aura.'
    - id: act3-amulet-gale
      item: Spineshudder Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:42) — busted on multi-hit spells'
      held: true
      slot: amulets
      note: 'Stays for the whole of Act 3. It is his Reverberation engine and nothing replaces it. ⚠ Amulet of Greater Health goes to Charles: its Constitution-save advantage would be redundant on Gale, who already has that from Armour of Landfall, whereas Charles has the Risky Ring''s disadvantage for it to cancel. ⚠ Amulet of the Devout is not taken by anyone — its Channel Divinity charge is dead on a Paladin, who spends Channel OATH, and looting it from the Stormshore Tabernacle offering chest curses the looter with Castigated By Divinity.'
    - id: act3-ring1-gale
      item: Callous Glow Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
      held: 2
      slot: ring 1
      note: 'CARRIED OVER. +2 Radiant on every damage instance against an ILLUMINATED target, which on a multi-ray build is applied 3-7 times a cast.'
    - id: act3-ring2-gale
      item: Coruscation Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (6:49) — good even outside Radiating Orb builds, and incredible inside them'
      held: 2
      slot: ring 2
      note: 'CARRIED OVER. Inflicts Radiating Orb whenever he deals spell damage while illuminated — the reason he keeps a light source on himself rather than on the target.'
    - id: act3-head-gale
      item: Hat of Fire Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (28:32) — removes enemies as threats almost instantly with a lot of builds'
      held: 2
      slot: head
      bis: true
      note: 'CARRIED OVER, and it stays to the end. Every instance of Fire damage grants Arcane Acuity, up to +10 spell save DC — on a Fire Sorlock throwing 3-7 fire instances a cast it caps almost immediately, and it is what makes his Command stick.'
    - id: birthright
      item: Birthright
      tier: A
      tier_note: 'Is EVERY Act 3 Helmet Awesome? - BG3 Helmets Tier List and Guide - Act 3 (4:42) — +2 Charisma is powerful, but narrowly beaten by the other Act 3 options'
      slot: head
      note: 'Would give +2 Charisma to a maximum of 22, but the head slot belongs permanently to the Hat of Fire Acuity and without Acuity the build stops working. ⚠ It does not go to Bonbon either — her head is locked to the Helmet of Arcane Acuity for the same reason, and +2 Charisma is +1 spell save DC against Acuity''s +10. Keep it bagged as an out-of-combat Charisma swap for dialogue checks on whichever of them is the face.'
    - id: act3-drakethroat-glaive
      item: Drakethroat Glaive
      tier: S
      tier_note: 'GunWjIpdxb0 (39:52) — free daily Elemental Weapon cast onto any weapon without spending your own slot'
      wiki: Drakethroat Glaive
      held: 2
      slot: other
      note: 'CARRIED OVER in the backpack, still never equipped in combat. The daily Twinned enchant runs to the end of the game. Targets in Act 3 are Charles''s 3d8 Shadow Blade, summoned before the cast, and Bonbon''s Titanstring Bow, still her ranged weapon and still dropped on the ground next to Charles.'
    progression:
    - id: prog-head
      item: 'Head: The Shadespell Circlet → Hat of Fire Acuity'
      slot: head
      note: Act 1 Shadespell (Omeluum) as a rental → Hat of Fire Acuity (Strange Ox at Last Light) permanently from Act 2. The Hat is the build; do not kill the Strange Ox at the Grove in Act 1, because it does not carry the hat until Last Light.
    - id: prog-armour
      item: 'Chest: Spidersilk Armour → Armour of Landfall'
      slot: armour
      note: Act 1–2 Spidersilk (Minthara) → Act 3 Armour of Landfall (Sorcerous Sundries). Both are chosen for the same reason and nothing else — ADVANTAGE ON CONSTITUTION SAVING THROWS, which is the only thing protecting Twinned Haste on a build with no War Caster and no shield.
    - id: prog-hands
      item: 'Hands: Gloves of Belligerent Skies → Spellmight Gloves'
      slot: hands
      note: Act 1–2 Belligerent Skies (Crèche) for the Reverberation engine → Act 3 Spellmight (Circus, Find Dribbles the Clown). Spellmight's −5 to hit needs Arcane Acuity to cover it, so cast the first Scorching Ray with them off.
    - id: prog-feet
      item: 'Boots: open → Evasive Shoes'
      slot: feet
      note: 'Empty through Act 1, because his Reverberation payload does not come online until Act 2 and the Boots of Stormy Clamour therefore go to Charles → Evasive Shoes (Mattis, Last Light) from Act 2 onward, with Acrobat Shoes (Barcus Wroot) the swap if Dexterity-save advantage is wanted over the AC point. A modest slot forced by a hard rule — Boots of Persistence, Vital Conduit Boots and The Speedy Lightfeet all require Medium Armour proficiency, which Sorcerer/Warlock never grants.'
    - id: prog-cloaks
      item: 'Cloak: none available → Thunderskin Cloak → Cloak of the Weave'
      slot: cloaks
      note: Empty in Act 1 → Thunderskin (Araj) in Act 2, which Dazes anything Reverberating that hits him and he is the party's biggest Reverberation source → Cloak of the Weave (Helsik) in Act 3 for the flat +1 spell save DC and +1 spell attack.
    - id: prog-amulets
      item: 'Amulet: Pearl of Power → Spineshudder Amulet'
      slot: amulets
      note: Act 1 Pearl (Omeluum) for a free slot each rest → Act 2–3 Spineshudder (Mimic in Isobel's bedroom), which applies Reverberation on ranged spell-attack hits and therefore fires 3–7 times per Scorching Ray.
    - id: prog-ring1
      item: 'Ring 1: Ring of Protection → Callous Glow Ring'
      slot: ring 1
      note: Ring of Protection from Mol in Act 1, because he is the party's lowest-AC body → Callous Glow Ring from Act 2, whose +2 radiant applies to every single Scorching Ray ray while he is lit.
    - id: prog-ring2
      item: 'Ring 2: Ring of Mind-Shielding → Coruscation Ring'
      slot: ring 2
      note: Ring of Mind-Shielding from Omeluum in Act 1 as concentration insurance on the Twinned Haste carrier → Coruscation Ring from Act 2, which pairs with Callous Glow because it lights the target that Callous Glow then punishes. Ring of Mental Inhibition is the swap for Command-spam fights.
    - id: prog-weapons
      item: 'Main hand: The Spellsparkler → Markoheshkir'
      slot: weapons
      note: The Spellsparkler builds Lightning Charges off every separate Scorching Ray instance but carries no enchantment bonus → Markoheshkir from Act 3 is the universal caster best in slot, adding +1 spell save DC and spell attacks, Arcane Battery, and an elemental attunement. Staff of Spellpower is the per-fight swap when a second sixth-level slot matters more.
    - id: prog-offhand
      item: 'Off hand: Melf''s First Staff → Rhapsody'
      slot: weapons
      note: Dual Wielder at character level 4 is what makes either pair legal, since none of these staves are Light. Melf's First Staff carries Acts 1–2 for its +1 spell save DC and +1 spell attack rolls → Rhapsody takes over in Act 3, where its +3 to everything applies to every ray. Melf's goes in the bag once Rhapsody arrives. Staff of Spellpower covers the off hand until Rhapsody has its three living kills.
    - id: prog-ranged
      item: 'Ranged: Bow of Awareness → Hellrider Longbow'
      slot: ranged weapons
      note: A pure stat-stick slot he never fires. +1 Initiative in Act 1 becomes +3 in Act 3. He wins the Hellrider contest by default because Bonbon's ranged slot is Titanstring's for the whole game.
    - id: prog-consumables
      item: 'Elixir: Elixir of Vigilance, every long rest, all game'
      slot: consumables
      note: +5 Initiative and Surprise immunity, and the substitute for the Alert feat this build cannot afford. Initiative in BG3 is d4 + DEX, so +5 is larger than the whole die. He is the only party member with no competing elixir.
  playstyle: |-
    - **Once per long rest:** cast Daylight (Enchant Item) on Bonbon's melee main hand — the Knife of the Undermountain King until the Resonance Stone, Phalar Aluve after. It lasts until the next rest and keeps Gale lit for the Coruscation chain.
    - **Once per long rest, from Act 2:** take the Drakethroat Glaive out of the backpack, equip it, and cast Draconic Elemental Weapon with Twinned Spell (3 sorcery points) — one charge onto Charles's main hand (the one-handed Phalar Aluve behind his shield until the Resonance Stone, the 3d8 Shadow Blade after) and one onto Bonbon's Titanstring lying on the ground next to him — all game, since Titanstring is never replaced. Re-equip the staves; hand the bow back. From the Stone on, do this *after* Charles summons his Shadow Blade, not before.
    - **Turn 1:** Twinned Haste (Action) if nobody else supplies it, then a Quickened Scorching Ray (bonus action) into a high-HP target with Spellmight Gloves OFF. A level-4 slot fires 5 rays and takes Arcane Acuity to its 10 cap.
    - **Turn 1 onward:** switch Spellmight Gloves ON. Acuity now covers the −5.
    - **Then pick a job each turn:** more Scorching Ray at a single target, Fireball at a cluster of 4+, or Extended Command at everything you want disabled. Command is not Concentration, so it never costs you Haste.
    - **Grouping:** Command: Approach pulls scattered enemies into one Fireball.
    - **Fire-immune fights** (House of Hope, Raphael, the red dragon, Yurgir): switch Markoheshkir to a lightning attunement and lead with Chain Lightning. Gale's damage drops sharply in these — plan on Twinned Haste, Command and Counterspell being his contribution.
    - **Do not** drop Fireball on Charles or Asterion before Careful Spell arrives at character level 11.
  traps:
  - 'Strange Ox: do NOT kill it at the Druid Grove in Act 1. It only carries the Hat of Fire Acuity from Last Light onward, and that hat is the build. Missing it in Act 2 is recoverable — the Ox reappears in Rivington in Act 3 — but killing it early is not.'
  - 'Heat fights the rest of the Act 3 kit — TREAT FLAME OF WRATH AS A PER-FIGHT TOGGLE, not a permanent attunement. Markoheshkir''s Flame of Wrath deals unavoidable self-damage every turn, and three separate interactions compound it: (1) Elemental Adept: Fire does NOT protect Gale — it pierces enemy resistance, it does not reduce damage he takes; (2) the Callous Glow Ring adds +2 radiant to Gale''s OWN Heat tick whenever he is Illuminated, and the Coruscation chain keeps him Illuminated on purpose, so his damage ring amplifies his own self-damage; (3) any damage taken strips 2 turns of Arcane Acuity, so every tick chips the exact stat the build exists to stack, on top of forcing a CON save against Twinned Haste. Gale is Human, so there is no Halfling Luck. Do not attune Flame of Wrath until Armour of Landfall is equipped, and consider dropping Coruscation in fights where Acuity uptime matters more than the radiant riders.'
  - 'Only two feats: Sorc 4 and Sorc 8 (character levels 4 and 9). Dual Wielder and Elemental Adept consume both, so there is no Alert and no War Caster — both gaps are covered by consumables and gear instead. Alert is replaced by a standing Elixir of Vigilance (+5 Initiative, Surprise immunity, no competing elixir on Gale). War Caster is replaced by Spidersilk Armour''s CON-save advantage from Act 1, upgraded to Armour of Landfall in Act 3. Note the published tier lists rate Elemental Adept only B while Alert is one of two S+ feats — the Vigilance elixir is what makes spending a feat on Elemental Adept acceptable.'
  - 'SPELLMIGHT GLOVES ARE UNTESTED — verify before building around them. The whole case for promoting them to core is that −5 spell attack / +1d8 damage applies to EACH Scorching Ray ray, but the wiki never addresses whether the +1d8 is per attack roll or once per spell, and Spellmight is absent from the per-instance notes that DO explicitly name Elemental Affinity and the Callous Glow Ring. On a 7-ray cast the two readings are +7d8 (~31, best in slot) versus +1d8 (~4.5 for a −5 penalty on all seven rolls, actively harmful). Test it on a single cast the moment they are acquired.'
  - 'Fireball friendly fire: Careful Spell is the fourth metamagic at Sorc 10 (character level 11). For the entire run before that, Fireball is an adds-cluster tool and Scorching Ray is the boss tool.'
  - 'Long rests: this build burns spell slots fast, especially if you lean into damage rather than Command. Bank camp supplies and use Potions of Angelic Slumber in Act 3.'
  - 'Command does not work on Undead, and neither Hold spell works on crit-immune enemies — the same gap Bonbon already has. Act 2 has a lot of Undead; lean on Fireball and Scorching Ray there.'
  - 'Warlock slot question: the published Command-spam loop assumes Gale can cast Command from ordinary Sorcerer slots, not only from his single short-rest pact slot. Confirm this in play at character level 7 — if Command is restricted to the pact slot, the control lane is once per short rest and Bonbon stays the primary controller.'
  - 'Respec cost: Gale joins as a Wizard — bank ~100g for the Withers respec into Sorcerer, and re-pick metamagic and spells to match this plan. There are no further respecs.'
---
