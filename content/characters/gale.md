---
nickname: Gale
builds:
- name: The Powder Keg
  is_primary: true
  role: Fire striker + non-concentration Command control + party Haste engine
  class: Sorcerer 11 (Draconic Bloodline — Red) / Fiend Warlock 1
  at_a_glance:
    armour: Light armour + shields (Human Civil Militia) — never wear a shield, both hands hold staves
    elixir: Elixir of Vigilance every long rest — +5 Initiative and Surprise immunity
    concentration: Twinned Haste on Charles and Bonbon — Command needs no concentration, so it runs beside it
  race: Gale (Human)
  race_notes: 'Human: +2 CHA and +1 DEX, Civil Militia (shields, light armour, spear/pike/halberd/glaive), one extra skill, +25% carry weight. He joins as a Wizard — respec with Withers into this build. ⚠ Early Act 1: feed the Netherese orb 3 magic items to clear Arcane Hunger.'
  background: Sage (Arcana, History) — Gale's default
  starting_stats:
    STR: 8
    DEX: 16
    CON: 14
    INT: 8
    WIS: 10
    CHA: 17
  stats_note: 'Point-buy 8/15/14/8/10/15, then Human +2 CHA and +1 DEX. DEX is his entire AC — Draconic Resilience, Spidersilk Armour and Armour of Landfall are all 13 + DEX. Nothing in the build keys off WIS.'
  ability_targets: 'CHA 17 → 18 (Hag''s Hair, modded) → 20 (Mirror of Loss, Cloister of Sombre Embrace in Act 3; DC 25 Religion check + 60% roll: Enhance Ability, Guidance, quicksave first). No ASI is needed, which is what frees both feats. Keep Birthright bagged for dialogue.'
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
      source: '+2 Mirror of Loss, Act 3 — DC 25 Religion check + 60% roll'
  metamagic:
  - Twinned + Extended (Sorc 2)
  - Quickened (Sorc 3)
  - Careful (Sorc 10 / char 11)
  feats:
  - at: Sorc 4 (char 4)
    feat: Dual Wielder
    note: 'Holds two non-Light staves: Spellsparkler + Melf''s in Acts 1–2, Markoheshkir + Rhapsody in Act 3. ⚠ Both hands are full for the whole run, so he can never carry a shield.'
  - at: Sorc 8 (char 9)
    feat: 'Elemental Adept: Fire'
    note: 'Fire damage pierces resistance and cannot roll a 1, on every ray, with no set-up turn. Act 3 is dense with fire-resistant enemies. ⚠ The resistance-piercing covers spells and attacks; the no-1 clause is spells only.'
  feats_note: 'Two feats only, at Sorc 4 and Sorc 8 (character levels 4 and 9). Dual Wielder and Elemental Adept take both, so there is no Alert and no War Caster — the Vigilance elixir and CON-save-advantage armour cover those gaps.'
  key_spells:
  - Scorching Ray (the damage engine — every rider applies per ray)
  - Fireball (cluster AoE; safe near allies only from char 11)
  - Haste (Twinned onto two martials, from char 5)
  - Command (no Concentration, so it runs beside Haste)
  - Hold Person / Hold Monster (the auto-crit setup)
  - Counterspell (upcast from a Sorcerer slot to skip the INT check)
  - 'Daylight: Enchant Item (keeps Gale lit for Coruscation)'
  - Ice Storm (non-concentration AoE; cast it last)
  - Cone of Cold (fire-immune fights; doubles on a Wet target)
  - Chain Lightning (fire-immune fights)
  creation:
    level1_class: 'Sorcerer 1 from character level 1. One respec only: the Withers respec out of Wizard when he joins.'
    level1_gains: Sorcerer Spellcasting (CHA), Draconic Bloodline with Red (Fire) ancestry, Draconic Resilience (unarmoured AC 13 + DEX, +1 HP per Sorcerer level), a free Burning Hands, and CON + CHA saving-throw proficiency.
    subclass_choice: 'Draconic Bloodline, Red ancestry. Any Fire ancestry works; Red grants Burning Hands free. The Fire ancestry is what makes Elemental Affinity add CHA to Fire damage at Sorc 6.'
    proficiencies:
      armor_weapons: 'Light armour and shields from Human Civil Militia, plus quarterstaffs, daggers, darts, slings and light crossbows from Sorcerer. Never wear a shield once Dual Wielder is taken.'
      saving_throws: CON + CHA from character level 1 — no window without CON-save proficiency.
      skills: Sage (Arcana, History) + 2 Sorcerer picks + 1 Human extra.
    starting_cantrips: 'Fire Bolt, Friends, Minor Illusion and Mage Hand. Cantrips are permanent and combat use stops after character level 3, so pick for utility.'
    starting_spells: 'Shield and Magic Missile, plus the free Burning Hands. Keep Magic Missile for the whole run — it never misses and nobody else in the party has one.'
    notes: 'Gale supplies no Guidance, Bless, Healing Word, Bane or Create Water — see the party plan''s Act 1 coverage table for who owns each.'
  spells:
    note: 'Sorcerer is a KNOWN caster: 12 spells known at Sorc 11 plus the free Burning Hands, with one replacement available per level from Sorc 2. Warlock 1 adds Command and Hex as separately-known spells.'
    mandatory:
    - spell: Scorching Ray
      tier: A
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (31:43) — each ray applies on-hit riders and stacks fire Arcane Acuity, but not efficient enough to win fights alone'
      level: '2'
      guide_level: 3
      school: Evocation
      save: Ranged spell attack (one roll per ray)
      when: Sorc 3 (char 3)
      why: 'The damage engine. 3 rays at level 2, +1 per slot level above; a level-6 slot fires 7. Each ray is its own attack roll and damage instance, so every flat rider and every Arcane Acuity stack applies per ray.'
    - spell: Command
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (28:37) — concentration-free turn denial that upcasts to multiple enemies; every higher-level slot competes with it'
      level: '1'
      guide_level: 7
      school: Enchantment
      save: WIS save
      when: Warlock 1 (char 7)
      why: 'The reason for the Warlock level: no Concentration, so it runs beside Twinned Haste. Extended doubles it to two turns, and it casts from any Sorcerer slot. ⚠ No effect on Undead.'
    - spell: Haste
      tier: S
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (6:12) — the most direct action-economy buff in the game. ON HONOUR MODE the extra action gives only one attack, not Extra Attack'
      level: '3'
      guide_level: 5
      school: Transmutation
      save: None (Concentration)
      when: Sorc 5 (char 5)
      why: 'Twinned for 3 sorcery points onto two of Charles / Asterion / Gale — Charles + Asterion for adds, Gale + Charles for a single boss. ⚠ Ending it leaves both targets Lethargic.'
    - spell: Fireball
      tier: B
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (38:58) — B not S: 13ft radius not 20ft, fire is widely resisted, Dex save for half. Do not cast it just because it is iconic'
      level: '3'
      guide_level: 6
      school: Evocation
      save: DEX save
      when: Sorc 6 (char 6)
      why: 'For clusters of 4+ only, and on-element for Elemental Affinity, Flame of Wrath and Elemental Adept. Discharge Markoheshkir Heat into it. ⚠ Careful Spell arrives at char 11 — before that, never into your own melee.'
    - spell: Counterspell
      tier: S
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (25:08) — top-five spell; trades a reaction for an enemy turn. NO SCROLLS EXIST, so it must be learnt on level-up'
      level: '3'
      guide_level: 5
      school: Abjuration
      save: Reaction (no check at equal/higher slot)
      when: Sorc 5 (char 5) — replaces Cloud of Daggers
      why: 'Reaction denial that costs no Action and no Concentration; it competes with Shield. ⚠ Against a spell above your slot level it rolls INT and Gale has INT 8 — upcast from a higher Sorcerer slot to remove the check.'
    - spell: Hold Person
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (55:42) — paralysis costs turns and gives automatic crits within 10 ft; humanoids only, best with high save DC'
      level: '2'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: Sorc 4 (char 4)
      why: 'Paralysed humanoids take automatic critical hits from ANY attack within 3 m, Gale''s rays included. Concentration, so he holds it instead of Haste and Bonbon usually owns the lane. Hold Monster at Sorc 9.'
    - spell: 'Daylight: Enchant Item'
      tier: C
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (29:44) — a bigger Light cantrip for a level 3 slot; worth it mainly against Act 3 vampires, who are vulnerable to it'
      level: '3'
      guide_level: 8
      school: Evocation
      save: None
      when: Sorc 7 (char 8)
      why: 'Cast out of combat on Bonbon''s melee main hand; it is bugged to last until long rest. The 15 m radius travels with her and keeps Gale lit for Coruscation. ⚠ Needs a main-hand weapon, so never Asterion.'
    - spell: Chain Lightning
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (9:31) — 360 average damage on four wet enemies, but often needs two casts to end a fight'
      level: '6'
      guide_level: 12
      school: Evocation
      save: DEX save
      when: Sorc 11 (char 12)
      why: 'The fire-immune answer — House of Hope, Raphael, the red dragon. Markoheshkir''s Bolts of Doom also grants it free once per short rest, so the single level-6 slot stays free for a 7-ray Scorching Ray.'
    recommended:
    - spell: Shield
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (43:07) — reaction +5 AC that only prompts when it turns a hit into a miss; worth a class dip on its own'
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None (Reaction, +5 AC)
      when: Sorc 1 (char 1)
      why: Gives his otherwise-dead level-1 slots a job and costs no Concentration. It competes with Counterspell for the Reaction.
    - spell: Magic Missile
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (32:13) — cannot miss, ignores line of sight, splits across targets, and every flat rider applies per missile'
      level: '1'
      guide_level: 1
      school: Evocation
      save: None (always hits)
      when: Sorc 1 (char 1) — kept for the whole run
      why: 'Never misses and needs no save, which nothing else in this build offers. Use it to finish a low-HP caster or on a turn where Scorching Ray would whiff. Nobody else in the party carries one.'
    - spell: Hold Monster
      tier: A
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (30:07) — paralysis is devastating but costs a level 5 slot and caps at two targets'
      level: '5'
      guide_level: 10
      school: Enchantment
      save: WIS save
      when: Sorc 9 (char 10)
      why: The non-humanoid auto-crit setup. Concentration, so cast it only in fights where someone else supplies Haste.
    - spell: Hex
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (21:08) — d6 on every attack roll all day, reapplied free on kills; enormous on multi-attack casters'
      level: '1'
      school: Enchantment
      save: None (Concentration)
      when: Warlock 1 (char 7)
      why: 'The second Warlock spell known. A per-ray rider, but Concentration, so it competes with Haste — a modded-difficulty option. Armour of Agathys is the defensive alternative pick.'
    - spell: 'Chromatic Orb: Fire'
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (23:44) — damage plus a chosen surface with no concentration; ice surfaces are near-stuns and it bypasses immunities'
      level: '1'
      guide_level: 2
      school: Evocation
      save: Ranged spell attack
      when: Sorc 2 (char 2) — replaced by Cloud of Daggers at Sorc 3
      why: On-element single-target damage for the one level before Scorching Ray, and it lays a fire surface. Gone from character level 3 onward.
    - spell: Cloud of Daggers
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (21:07) — no save and no attack roll; ~20 guaranteed damage per target before enemies act'
      level: '2'
      guide_level: 3
      school: Conjuration
      save: None (no attack roll, no save)
      when: Sorc 3 (char 3) — replaced by Counterspell at Sorc 5
      why: '4d4 on cast and 4d4 again at the start of each enemy turn, with no roll and no save. Park it in a doorway or on a caster for characters 3–4.'
    - spell: Ice Storm
      tier: A
      tier_note: 'Spells tier list, level 4, part 2 (Freedom of Movement through Wall of Fire) (20:00) — A because the 20 ft ice surface costs NO CONCENTRATION; the best follow-up after a control spell'
      level: '4'
      guide_level: 9
      school: Evocation
      save: DEX save
      when: Sorc 8 (char 9)
      why: 'Non-concentration 4th-level AoE, so it drops while he holds Twinned Haste, and the ice surface knocks enemies prone. ⚠ Cast it LAST in the turn — his own fire melts the ice, and Ray of Frost re-freezes it.'
    - spell: Cone of Cold
      tier: B
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 5 (12:02) — only worth it doubled up on wet grouped enemies; best AoE burst for hexblade warlocks'
      level: '5'
      guide_level: 11
      school: Evocation
      save: CON save
      when: Sorc 10 (char 11)
      why: '8d8 cold in a cone with no Concentration, so it fires while he holds Haste, and it works on fire-immune enemies. Throw a water bottle with Mage Hand first — Wet doubles cold damage.'
    - spell: Burning Hands
      tier: C
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (18:26) — weak damage on a bad save; only Light Domain clerics, who get it free, will cast it'
      source: granted
      level: '1'
      guide_level: 1
      school: Evocation
      save: DEX save
      when: Sorc 1 (char 1) — FREE from Red ancestry
      why: Free from Red ancestry, so it spends no spell-known pick. Worth casting as on-element AoE for the first few levels and it stays known all run.
    - spell: Fire Bolt
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (24:40) — highest raw damage for wizards and sorcerers, and it lights fires at 60 feet'
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: Sorc 1 (char 1)
      why: 'On-element chip damage for the first three levels. Cantrips stop mattering once Scorching Ray arrives, which is also why the Potent Robe is refused.'
    - spell: Friends
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (26:48) — advantage on Charisma checks; COUNTS AS A CRIME ON TACTICIAN AND HONOUR MODE, so hide or fast-travel afterwards'
      level: Cantrip
      guide_level: 1
      school: Enchantment
      save: None (Concentration)
      when: Sorc 1 (char 1)
      why: 'Backup Charisma advantage; Bonbon is the party face. ⚠ The target turns hostile when it ends, so never cast it somewhere you intend to stay.'
    - spell: Minor Illusion
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (35:56) — moves NPCs with no save or roll; clusters enemies for AoE, sets ambushes, pulls enemies one at a time'
      level: Cantrip
      guide_level: 1
      school: Illusion
      save: None
      when: Sorc 1 (char 1)
      why: Groups enemies before combat for a bigger opening Fireball, and moves NPCs off Asterion's theft routes.
    - spell: Mage Hand
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (33:23) — costs a short-rest charge, but scouts, triggers traps, throws potions and soaks one enemy attack'
      level: Cantrip
      guide_level: 1
      school: Conjuration
      save: None
      when: Sorc 1 (char 1)
      why: 'Scouting and object work. Its Throw also puts a water bottle down for a 2 m Wet splash, which sets up Cone of Cold, Chain Lightning or Ray of Frost — never a fire cast, because Wet resists fire.'
    - spell: Light
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (30:38) — hands-free, concentration-free light lasting all day; most parties need some light source'
      level: Cantrip
      guide_level: 4
      school: Evocation
      save: None
      when: Sorc 4 (char 4) — fifth cantrip
      why: 'A slot-free way to keep GALE lit so the Coruscation Ring fires, covering Act 2 before Daylight at char 8. ⚠ Confirm in play that a Light-lit character registers as Illuminated.'
    - spell: Bone Chill
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (12:42) — turns off enemy healing with no save and blanks undead attack rolls; not the go-to damage cantrip'
      level: Cantrip
      guide_level: 7
      school: Necromancy
      save: Ranged spell attack
      when: Warlock 1 (char 7) — second Warlock cantrip
      why: 'The second Warlock cantrip. It blocks enemy healing with no save and gives undead disadvantage on attacks, which covers the Act 2 Undead that Command cannot touch.'
    - spell: Ray of Frost
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (41:42) — movement debuff lets you kite as a stun, doubles on wet enemies, and freezes surfaces'
      level: Cantrip
      guide_level: 11
      school: Evocation
      save: Ranged spell attack
      when: Sorc 10 (char 11) — sixth cantrip
      why: 'The sixth cantrip, easy to miss — char 11 is the only level after char 4 that grants one. Slot-free cold for the fire-immune fights, doubled on a Wet target, and it re-freezes Ice Storm''s surface.'
    - spell: Globe of Invulnerability
      tier: S
      tier_note: 'ULTIMATE SPELLS GUIDE - [Updated] BG3 Spells Tier List - Level 6 (26:18) — total damage immunity wins most boss fights outright; get one cast into every Honour party'
      level: '6'
      school: Abjuration
      save: None (Concentration)
      when: scroll only in this build
      why: Chain Lightning takes the single level-6 spell known, so buy two or three Globe scrolls in Act 3 instead.
  leveling:
    respecs:
    - label: Lv 1–12 · Sorcerer-first, no respec
      note: 'Sorcerer 1–6, Fiend Warlock 1 at character 7, then Sorcerer 7–11. CON + CHA saves from level 1. The only respec is the initial Withers respec out of Wizard.'
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
          note: 'Fire ancestry is what makes Elemental Affinity add CHA to Fire damage at Sorc 6. Red grants Burning Hands free; Gold and Brass grant Disguise Self and Sleep.'
        - category: Ancestry spell
          granted: true
          recommendation: Burning Hands
          note: 'FREE — it spends no spell-known pick. That is the reason to take Red over Gold or Brass, and it stays known for the whole run at no cost.'
        - category: Cantrips
          picks: 4
          recommendation:
          - Fire Bolt
          - Friends
          - Minor Illusion
          - Mage Hand
          note: Cantrips are permanent and combat use stops after character level 3, so choose utility over damage scaling.
        - category: Spells
          picks: 2
          recommendation:
          - Shield
          - Magic Missile
          note: 'Both are keepers. Magic Missile never misses and stays for the whole run; Counterspell arrives at Sorc 5 off the Cloud of Daggers slot instead of displacing it.'
        - category: Skills
          picks: 3
          recommendation:
          - Persuasion
          - Insight
          - Perception
          note: 'THREE picks: 2 from Sorcerer, 1 from Human Versatility. Do not re-pick Arcana — Sage already grants it and proficiency does not stack. ⚠ Check at the Withers respec screen that the Human free skill is still selectable.'
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
          note: 'Quickened is not selectable until Sorc 3. Twinned carries the Haste engine; Extended turns Command into a two-turn lockdown.'
        - category: Spell
          picks: 1
          recommendation: 'Chromatic Orb: Fire'
          note: On-element single-target damage for the one level before Scorching Ray arrives.
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
          note: 'Scorching Ray on the bonus action, which is the whole loop: Quickened damage with the bonus action, Command or a second spell with the Action.'
        - category: Spell
          picks: 1
          recommendation: Scorching Ray
          note: The build's core spell, and from character 3 it also charges the Spellsparkler.
        - category: Replacement
          picks: 1
          optional: true
          recommendation: 'Chromatic Orb: Fire → Cloud of Daggers'
          note: 'Use the replacement slot — it used to sit idle here. Cloud of Daggers is 4d4 on cast and 4d4 again at the start of each enemy turn, with no roll and no save.'
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
          note: 'Lets him hold Spellsparkler + Melf''s First Staff, and later Markoheshkir + Rhapsody — neither pair is Light. Both hands are full from here, so no shield.'
        - category: Cantrip
          picks: 1
          recommendation: Light
          note: Keeps Gale lit for the Coruscation Ring without spending a slot, well before Daylight.
        - category: Spell
          picks: 1
          recommendation: Hold Person
          note: A second source of the paralysis that makes any attack within 3 m an automatic critical hit, his own rays included.
      - char_level: 5
        class: Sorcerer 5
        gains:
        - Level 3 Sorcerer spells
        - Five Sorcery Points
        recommendations:
        - category: Spell
          picks: 1
          recommendation: Haste
          note: The party Haste engine comes online here. Twinned costs 3 sorcery points.
        - category: Replacement
          picks: 1
          optional: true
          recommendation: Cloud of Daggers → Counterspell
          note: 'Counterspell one level earlier than the old plan. ⚠ Upcast it from a higher Sorcerer slot — against a spell above your slot level it rolls INT, and Gale has INT 8.'
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
          note: 'Primary AoE, now on-element for Elemental Affinity: +5 damage per instance at CHA 20.'
        - category: Replacement
          picks: 1
          optional: true
          recommendation: None — keep Magic Missile
          note: 'The Sorc 6 replacement slot is now unused. Counterspell was already taken at Sorc 5, so Magic Missile stays: it never misses and nobody else in the party has it.'
      - char_level: 7
        class: Fiend Warlock 1
        gains:
        - 'Pact Magic: 2 Warlock cantrips and 2 Warlock spells known — all four are picks'
        - 'Fiend Expanded Spell List: Burning Hands and Command become choosable options'
        - One level-1 pact slot (recharges on SHORT rest)
        - Dark One's Blessing (temporary HP on a kill)
        - Light armour proficiency (redundant — Civil Militia already grants it)
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
          note: 'Command is the pickup. Hex competes with Haste for Concentration, so treat it as a modded-difficulty option; Armour of Agathys is the defensive alternative.'
        - category: Cantrips
          picks: 2
          recommendation:
          - Eldritch Blast
          - Bone Chill
          note: 'Bone Chill covers the Act 2 Undead that Command cannot touch. Eldritch Blast is an occasional ranged option, not a plan — Agonizing Blast is a Warlock 2 invocation he never reaches. ⚠ Do not take Friends; he already knows it.'
      - char_level: 8
        class: Sorcerer 7
        gains:
        - Level 4 Sorcerer spells
        - Seven Sorcery Points
        recommendations:
        - category: Spell
          picks: 1
          recommendation: 'Daylight'
          note: 'Take the Enchant Item variant in play. Level 4 slots also mean a 5-ray Scorching Ray, the cast that caps Arcane Acuity at 10.'
      - char_level: 9
        class: Sorcerer 8
        gains:
        - Eight Sorcery Points
        - Feat or Ability Score Improvement selection
        recommendations:
        - category: Feat
          picks: 1
          recommendation: 'Elemental Adept: Fire'
          note: 'Pierces fire resistance and removes 1s from every fire damage die, per ray, with no set-up turn. Act 3 is dense with fire-resistant enemies.'
        - category: Spell
          picks: 1
          recommendation: Ice Storm
          note: 'A-tier non-concentration AoE, so it drops while he holds Twinned Haste. ⚠ Cast it last in the turn — his own fire melts the ice, and Ray of Frost re-freezes it.'
      - char_level: 10
        class: Sorcerer 9
        gains:
        - Level 5 Sorcerer spells
        - Nine Sorcery Points
        recommendations:
        - category: Spell
          picks: 1
          recommendation: Hold Monster
          note: Extends the auto-crit setup to non-humanoids for the fights where Bonbon is concentrating on something else.
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
          note: Finally lets him drop Fireball on a cluster that Charles or Asterion is standing in.
        - category: Cantrip
          picks: 1
          recommendation: Ray of Frost
          note: 'The sixth cantrip — char 11 is the only level after char 4 that grants one. 3d8 slot-free cold for the fire-immune fights, and it re-freezes Ice Storm''s ice.'
        - category: Spell
          picks: 1
          recommendation: Cone of Cold
          note: '8d8 cold with no Concentration, so it fires while he holds Haste. Throw a water bottle with Mage Hand first — Wet doubles cold damage.'
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
          note: 'The fire-immune answer for the House of Hope and Raphael. A level-6 Scorching Ray also fires 7 rays — the build''s single biggest turn.'
  itemization:
    act1:
    - id: the-spellsparkler
      item: The Spellsparkler
      tier: A
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (26:53) — stacks Lightning Charges fast on multi-hit casters, though Melf''s is broader'
      slot: weapons
      note: 'MAIN HAND, from Counsellor Florrick at Waukeen''s Rest for Rescue the Grand Duke. Every Scorching Ray instance grants 2 Lightning Charges: +1 attack rolls, +1 Lightning damage, 1d8 burst at five stacks. ⚠ Do not feed it to the Netherese orb.'
    - id: melf-s-first-staff
      item: Melf's First Staff
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (15:30) — probably best in slot for most spellcasters for all of Act 1'
      slot: weapons
      note: 'OFF HAND, from Blurg in the Underdark, equipped from character level 4 once Dual Wielder is taken. +1 spell save DC and +1 spell attack rolls, and the attack bonus applies to every ray. ⚠ Before char 4 he holds Spellsparkler alone.'
    - id: shadespell-circlet
      item: The Shadespell Circlet
      tier: S
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (41:43) — needs setup to get value, but spell save DC increases are that powerful'
      slot: head
      note: ACT 1 HEAD, from Omeluum after Help Omeluum Investigate the Parasite. +1 spell save DC while Gale is obscured. Treat it as a rental — the Hat of Fire Acuity replaces it permanently in Act 2.
    - id: act1-feet-gale
      item: Boot slot
      slot: feet
      wiki: false
      note: 'OPEN, and honestly so. Nothing fits: The Speedy Lightfeet, Boots of Striding, Boots of Elemental Momentum and Vital Conduit Boots all require Medium Armour, which Sorcerer/Warlock never grants. Evasive Shoes fix the slot at Last Light in Act 2.'
      options:
      - id: opt-night-walkers-gale
        item: Disintegrating Night Walkers
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (19:19) — probably the best boots in the game'
        rank: '#11'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #11 of 20 — short-rest Misty Step plus immunity to most movement-restricting surfaces'
        note: 'DECIDED, but for ACT 3 rather than here — Asterion wears them from Nere in Grymforge until he moves to the Kushigo boots. No slipping on grease or ice, no Web, Entangle or Ensnare, and a short-rest Misty Step.'
      - id: opt-watersparkers-gale
        item: The Watersparkers
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (35:24) — core item for lightning-charge builds; needs water and the Sparkswall ring'
        note: 'Gilded chest in Minthara''s area of the Shattered Sanctum. Electrifies water he stands in and pays 3 Lightning Charges a turn for it. ⚠ Wants The Sparkswall so he is not electrocuted by his own puddle.'
      - id: opt-boots-of-aid-and-comfort-gale
        item: Boots of Aid and Comfort
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (4:11) — 3 temp HP on every heal; combines with Hellrider''s Pride and Whispering Promise'
        note: Sold by Grat the Trader at the Goblin Camp. 3 temporary hit points to anyone he heals, and Gale heals nobody. Listed only so the slot's whole field is visible.
    - id: gloves-of-belligerent-skies
      item: Gloves of Belligerent Skies
      tier: A
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (20:24) — excellent for specific builds and decent across a wide variety of them'
      slot: hands
      bis: true
      note: 'LATE ACT 1 HANDS, in the elegant chest in the Crèche Inquisitor''s Chamber. Thunder, Lightning or Radiant damage applies 2 turns of Reverberation — once the Callous Glow Ring is online that is every ray. ⚠ Charles has a claim; Gale procs it 5–7 times a cast.'
    - id: pearl-of-power-amulet
      item: Pearl of Power Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (35:16) — a mainstay once acquired'
      slot: amulets
      note: ACT 1 NECK, from Omeluum. One spell slot of level 3 or lower back every long rest — normally another Haste or Scorching Ray.
    - id: spidersilk-armour
      item: Spidersilk Armour
      tier: S
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (16:13) — S specifically for light-armour casters, which is not what it looks designed for'
      slot: armour
      bis: true
      note: 'ACT 1 CHEST, worn by Minthara in the Shattered Sanctum — the same kill as Charles''s Boots of Striding. AC 12 + DEX, +1 Stealth, and ADVANTAGE ON CONSTITUTION SAVES, his only protection for Twinned Haste. ⚠ Costs 1 AC versus unarmoured; take the trade.'
    - id: elixir-of-vigilance
      item: Elixir of Vigilance
      tier: S
      tier_note: '9BcQXb37Bik (57:59) — rated S+ ABOVE THE SCALE: a free Alert feat, and +5 on a d4 initiative roll means going first'
      slot: consumables
      note: 'Drink one every long rest, all game. +5 Initiative and Surprise immunity until the next rest, about 25 gp from Danthelon''s, Kith in Grymforge, or Popper at the Circus. This is the Alert feat he cannot afford.'
    - id: bow-of-awareness
      item: Bow of Awareness
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (16:30) — going first is among the best things you can do in an Honour run'
      slot: ranged weapons
      note: ACT 1 ranged filler for +1 Initiative in a slot he leaves empty. He never fires it; the Hellrider Longbow replaces it in Act 3 for +3.
    - id: ring-of-protection
      item: Ring of Protection
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (34:55) — raises the party''s average AC; give it to the easiest-to-hit member'
      rank: '#20'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #20 of 20 — +1 AC and all saves fits almost anyone, for the whole game'
      slot: ring 1
      note: 'HIS, not Asterion''s — Mol''s reward for Steal the Sacred Idol once the Grove resolves. +1 AC and +1 to all saves on the party''s lowest-AC body, which doubles as concentration insurance for Twinned Haste.'
    - id: ring-of-mind-shielding
      item: Ring of Mind-Shielding
      tier: D
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (32:22) — a weak situational effect by the point in the game where you get it'
      slot: ring 2
      note: 'From Omeluum in the Ebonlake Grotto after his quest — persuade, intimidate, pay, trade a story, or pickpocket. Advantage on saves against Charmed, and a charmed Gale is a dropped Haste and a Fireball pointed at his own party.'
    - id: act1-cloak-gale
      item: No cloak exists yet
      slot: cloaks
      note: Deliberately empty. The only magical cloak in Act 1 is the Dark Urge's Deathstalker Mantle and it goes to Asterion. His slot opens at Last Light in Act 2.
    act2:
    - id: hat-of-fire-acuity
      item: Hat of Fire Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (28:32) — removes enemies as threats almost instantly with a lot of builds'
      slot: head
      bis: true
      note: 'CORE — the item that turns the build on. Carried by the Strange Ox at Dammon''s in Last Light Inn. Fire damage grants 2 turns of Arcane Acuity, capped at 10, each +1 spell attack and +1 DC; one 5-ray cast caps it. ⚠ Do not kill the Ox at the Grove.'
    - id: callous-glow-ring
      item: Callous Glow Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
      slot: ring 1
      bis: true
      note: 'DAMAGE ring, in the opulent chest in the vault room near Balthazar in the Gauntlet of Shar. +2 Radiant per damage instance against an ILLUMINATED target, so up to +14 on a level-6 cast, and the radiant re-procs Belligerent Skies. ⚠ Take it off against Shar worshippers and Justiciars.'
    - id: coruscation-ring
      item: Coruscation Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (6:49) — good even outside Radiating Orb builds, and incredible inside them'
      slot: ring 2
      bis: true
      note: 'THE illumination engine, in a trapped heavy chest in the Last Light cellar. It applies Radiating Orb while the WEARER is lit, which makes the target Illuminated and switches on Callous Glow. Keep the light on Gale, not on the target.'
    - id: act2-ring2-gale-flex
      item: Second ring alternatives
      slot: ring 2
      wiki: false
      note: Coruscation Ring is the default because it converts his illuminated spell damage into Radiating Orb. These are the swaps worth knowing.
      options:
      - id: ring-of-mental-inhibition
        item: Ring of Mental Inhibition
        tier: B
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (24:59) — powerful if the party is carefully built around it, but it needs very specific builds'
        note: House in Deep Shadows. Mental Fatigue on every failed save against him, compounding his own DC. Wear it in fights where Command matters more than rider damage.
      - id: opt-ring-of-free-action-gale
        item: Ring of Free Action
        tier: C
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (21:55) — some minor uses; a swap-in against enemies that paralyse or Hold Person'
        note: Ignore difficult terrain, plus immunity to Paralysed and Restrained. Wear it against enemies that paralyse, since it protects the Twinned Haste concentration.
    - id: spineshudder-amulet
      item: Spineshudder Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:42) — busted on multi-hit spells'
      slot: amulets
      note: 'CORE neck, in the Mimic in Isobel''s bedroom on the upper floor of Moonrise. Reverberation on every ranged spell-attack hit, so 3–7 times a cast. With Belligerent Skies that is roughly 28 turns of Reverberation per Scorching Ray against a threshold of 5, so single targets go Prone repeatedly.'
    - id: cloak-of-protection-gale
      item: Cloak of Protection
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (13:30) — excellent, and someone in the party will almost certainly be wearing it'
      slot: cloaks
      note: 'NOT HIS. Charles takes it to cancel the Risky Ring''s save disadvantage; Gale already has CON-save advantage from Spidersilk plus save proficiency from level 1. Recorded so the trade is visible.'
    - id: thunderskin-cloak
      item: Thunderskin Cloak
      tier: D
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (19:42) — needs a reverberation build and a fixed DC13 Constitution save; will practically never trigger'
      slot: cloaks
      note: 'HIS ACT 2 CLOAK, sold by Araj Oblodra at Moonrise. A Reverberating creature that damages him makes a DC 13 CON save or is Dazed — no Reactions, disadvantage on WIS saves, no DEX bonus to AC. He is the party''s biggest Reverberation source, and Dazed feeds his Command.'
    - id: act2-armour-gale
      item: Spidersilk Armour
      tier: S
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (16:13) — S specifically for light-armour casters, which is not what it looks designed for'
      held: 1
      slot: armour
      bis: true
      note: CARRIED OVER, and never swapped. Advantage on Constitution saving throws is what protects Twinned Haste, and it is also why the Potent Robe is refused.
    - id: act2-hands-gale
      item: Gloves of Belligerent Skies
      tier: A
      tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (20:24) — excellent for specific builds and decent across a wide variety of them'
      held: 1
      slot: hands
      bis: true
      note: CARRIED OVER. Reverberation on Thunder, Lightning or Radiant damage, applied 3–7 times a cast, which is why these live on him rather than on Charles.
    - id: act2-feet-gale
      item: Evasive Shoes
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (46:17) — a lot of parties will simply use them'
      slot: feet
      bis: true
      note: 'HIS SLOT IS FIXED HERE, sold by Mattis at Last Light Inn. +1 Armour Class and +1 Acrobatics, no proficiency requirement, contested by nobody. Fewer hits means fewer concentration saves. ⚠ Boots of Persistence, Vital Conduit Boots and The Speedy Lightfeet all need Medium Armour he never gets.'
      options:
      - id: opt-acrobat-shoes-gale
        item: Acrobat Shoes
        tier: D
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (36:55) — advantage on Dex saves is available elsewhere; not worth the boot slot'
        note: 'THE ALTERNATIVE, sold by Barcus Wroot at his Last Light workshop. ADVANTAGE ON DEXTERITY SAVING THROWS — the one save nothing else in his kit covers, and the save that Fireballs and breath weapons take Twinned Haste off him with.'
    - id: act2-weapons-gale
      item: The Spellsparkler
      tier: A
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (26:53) — stacks Lightning Charges fast on multi-hit casters, though Melf''s is broader'
      held: 1
      slot: weapons
      note: CARRIED OVER main hand. Lightning Charges off every separate Scorching Ray instance. No enchantment bonus, so it is a rider stick rather than an accuracy stick.
    - id: act2-offhand-gale
      item: Melf's First Staff
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (15:30) — probably best in slot for most spellcasters for all of Act 1'
      held: 1
      slot: weapons
      note: CARRIED OVER off hand, legal only because Dual Wielder was taken at character level 4 — neither staff is Light. This is the +1 spell save DC and +1 spell attack rolls.
    - id: act2-ranged-gale
      item: Bow of Awareness
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (16:30) — going first is among the best things you can do in an Honour run'
      held: 1
      slot: ranged weapons
      note: CARRIED OVER, and purely for the passive initiative. He never fires it.
    - id: drakethroat-glaive
      item: Drakethroat Glaive
      tier: S
      tier_note: 'GunWjIpdxb0 (39:52) — free daily Elemental Weapon cast onto any weapon without spending your own slot'
      wiki: Drakethroat Glaive
      slot: other
      note: 'BACKPACK ITEM, 960 gp from Roah Moonglow at Moonrise, never equipped in combat. Once per long rest equip it and Twin Draconic Elemental Weapon (3 sorcery points) onto Bonbon''s Titanstring and Charles''s main hand: +1 attack rolls and +1d4 COLD each, every day. ⚠ Drop the bow at his feet, inside 1.5 m.'
    act3:
    - id: markoheshkir
      item: Markoheshkir
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (44:41) — universal caster best in slot: +1 DC and attacks, Arcane Battery, elemental attunement'
      slot: weapons
      bis: true
      note: 'CORE main hand, in a Globe of Invulnerability in Ramazith''s Tower (See Invisibility, then a DC 20 Arcana check). +1 spell attack and DC, plus Arcane Battery. Attune Flame of Wrath: +proficiency Fire damage per ray, and a free Fireball and Wall of Fire once each per short rest. ⚠ Attune only after Armour of Landfall is on.'
    - id: rhapsody
      item: Rhapsody
      tier: S
      tier_note: 'The BEST ROGUE WEAPONS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Part 2 (43:01) — +3 to everything, and best in slot as a stat stick even for characters not swinging it'
      slot: weapons
      note: 'CORE off hand, carried by Cazador Szarr. Scarlet Remittance stacks +1 attack, damage and spell save DC per kill, up to 3, and the damage applies per ray. ⚠ Stacks build only on living hostiles and are lost when it is unequipped, so once it is at +3 it stays in his hand.'
    - id: staff-of-spellpower
      item: Staff of Spellpower
      tier: S
      tier_note: 'The BEST STAVES in Baldur''s Gate 3 - Honor Mode Tier List and Guide (48:32) — a mainstay; refreshing a spell slot on any slot for any purpose is that good'
      slot: weapons
      note: 'CARRY BOTH. +1 spell save DC and +1 spell attack immediately, plus a second Arcane Battery for one more free spell of any level per long rest. It is the off hand until Rhapsody has its three living kills, and on any day that opens against undead or constructs.'
    - id: spellmight-gloves
      item: Spellmight Gloves
      tier: B
      tier_note: 'The BEST GLOVES In BG3 COMPLETE - Honor Mode Tier List and Guide - Act 3 (38:34) — B for Honour mode specifically; called absolutely busted for critical-hit warlocks on Tactician or below'
      slot: hands
      note: 'ACT 3 HANDS, rewarded by Lucretious for Find Dribbles the Clown at the Circus, and pickpocketable. −5 spell attack for +1d8 damage. Cast the first Scorching Ray with them OFF to build Arcane Acuity, then switch them ON. ⚠ Confirm on the first cast whether the +1d8 lands per ray.'
    - id: armour-of-landfall
      item: Armour of Landfall
      tier: A
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (31:23) — +1 save DC, Con save advantage and Plant Growth per short rest; only 13 AC'
      slot: armour
      note: 'CORE armour, sold by Lorroakan''s Projection or Rolan on the ground floor of Sorcerous Sundries. AC 13 + DEX, +1 spell save DC, Plant Growth once per short rest, and ADVANTAGE ON CONSTITUTION SAVES — the advantage that makes Markoheshkir''s Heat safe to carry while concentrating.'
    - id: cloak-of-the-weave
      item: Cloak of the Weave
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (28:30) — best in slot for any caster'
      slot: cloaks
      note: 'ACT 3 CLOAK, sold by Helsik at the Devil''s Fee once her special stock is unlocked. Take it for the flat +1 spell save DC and +1 spell attack rolls. ⚠ Its Absorb Elements ability lacks the passives it needs and does not work.'
    - id: hellriders-longbow
      item: Hellrider Longbow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (53:35) — +3 initiative from an unused slot; he would put it in S+ if it existed'
      wiki: Hellrider Longbow
      slot: ranged weapons
      note: 'HIS ranged stat stick, sold by Ferg Drogher in Rivington. +3 Initiative and advantage on Perception, upgrading the Bow of Awareness; with the standing Vigilance elixir that is +8 without a feat. ⚠ Ferg sells nothing while Shadowheart is nearby unless she killed the Nightsong.'
    - id: helldusk-boots-gale
      item: Helldusk Boots
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (1:00:13) — the saving throw makes the wearer extremely safe in almost every circumstance'
      slot: feet
      note: 'NOT HIS. Charles takes them for the Prone immunity he needs as the frontliner, and Infernal Evasion is once per long rest, not once per turn. Gale has no Prone cover; the Night Walkers give ice-footing and a Misty Step instead. Recorded so the trade is visible.'
    - id: act3-feet-gale
      item: Disintegrating Night Walkers
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (19:19) — probably the best boots in the game'
      rank: '#11'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #11 of 20 — short-rest Misty Step plus immunity to most movement-restricting surfaces'
      slot: feet
      bis: true
      note: 'ACT 3 FEET, free once Asterion moves to the Boots of Uninhibited Kushigo — originally Nere in Grymforge. No slipping on Snowburst or Ice Storm ice, immune to Web, Entangle and Ensnare, Misty Step once per short rest. ⚠ No Prone immunity.'
      options:
      - id: opt-evasive-shoes-gale-a3
        item: Evasive Shoes
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (46:17) — a lot of parties will simply use them'
        held: 2
        note: THE OPTION, carried over from Last Light. +1 Armour Class and +1 Acrobatics. Wear them in fights with no ice and no need for a Misty Step.
      - id: opt-acrobat-shoes-gale-a3
        item: Acrobat Shoes
        tier: D
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (36:55) — advantage on Dex saves is available elsewhere; not worth the boot slot'
        held: 2
        note: From Barcus Wroot at Last Light. ADVANTAGE ON DEXTERITY SAVING THROWS — the one save nothing else in his kit covers, and the one Twinned Haste usually dies to.
      - id: opt-boots-of-psionic-movement
        item: Boots of Psionic Movement
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (54:03) — bonus-action Fly once per long rest; strong for parties skipping illithid powers'
        note: Bonus-action Fly once per long rest, plus +1 to Dexterity saving throws. Everyone communes at the start of Act 3 and gets Fly, so only the Dexterity-save bonus is left to argue for.
      - id: opt-boots-of-speed-gale
        item: Boots of Speed
        tier: A
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (11:29) — bonus-action double move; some party member almost always wants it (captions garble the letter)'
        rank: '#14'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #14 of 20 — bonus-action Dash gives anyone Rogue-grade mobility'
        note: Free once Bonbon moves to the Boots of Brilliance in Act 2. Bonus-action double move, which is how he gets clear of his own Heat aura.
    - id: act3-amulet-gale
      item: Spineshudder Amulet
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:42) — busted on multi-hit spells'
      held: true
      slot: amulets
      note: 'CARRIED OVER for the whole of Act 3 — his Reverberation engine, and nothing replaces it. ⚠ The Amulet of Greater Health goes to Charles; its Constitution-save advantage is redundant on Gale, who already has that from Armour of Landfall.'
    - id: act3-ring1-gale
      item: Callous Glow Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
      held: 2
      slot: ring 1
      note: CARRIED OVER. +2 Radiant on every damage instance against an illuminated target, which on a multi-ray build is 3–7 times a cast.
    - id: act3-ring2-gale
      item: Coruscation Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (6:49) — good even outside Radiating Orb builds, and incredible inside them'
      held: 2
      slot: ring 2
      note: CARRIED OVER. Radiating Orb whenever he deals spell damage while illuminated, which is why the light source stays on him rather than on the target.
    - id: act3-head-gale
      item: Hat of Fire Acuity
      tier: S
      tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (28:32) — removes enemies as threats almost instantly with a lot of builds'
      held: 2
      slot: head
      bis: true
      note: CARRIED OVER, and it stays to the end. Arcane Acuity up to +10 spell save DC, capped almost immediately on 3–7 fire instances a cast. This is what makes his Command stick.
    - id: birthright
      item: Birthright
      tier: A
      tier_note: 'Is EVERY Act 3 Helmet Awesome? - BG3 Helmets Tier List and Guide - Act 3 (4:42) — +2 Charisma is powerful, but narrowly beaten by the other Act 3 options'
      slot: head
      note: 'BAGGED as an out-of-combat dialogue swap. +2 Charisma to 22, but the head slot belongs permanently to the Hat of Fire Acuity and without Acuity the build stops working. Bonbon''s head is locked the same way.'
    - id: act3-drakethroat-glaive
      item: Drakethroat Glaive
      tier: S
      tier_note: 'GunWjIpdxb0 (39:52) — free daily Elemental Weapon cast onto any weapon without spending your own slot'
      wiki: Drakethroat Glaive
      held: 2
      slot: other
      note: 'CARRIED OVER in the backpack, still never equipped in combat. The daily Twinned enchant runs to the end of the game, COLD both times: Charles''s 3d8 Shadow Blade, summoned before the cast, and Bonbon''s Titanstring dropped on the ground next to him.'
    progression:
    - id: prog-head
      item: 'Head: The Shadespell Circlet → Hat of Fire Acuity'
      slot: head
      note: 'Act 1 Shadespell (Omeluum) as a rental → Hat of Fire Acuity (Strange Ox, Last Light) from Act 2 to the end. ⚠ Do not kill the Strange Ox at the Grove in Act 1.'
    - id: prog-armour
      item: 'Chest: Spidersilk Armour → Armour of Landfall'
      slot: armour
      note: Act 1–2 Spidersilk (Minthara) → Act 3 Armour of Landfall (Sorcerous Sundries). Both are worn for ADVANTAGE ON CONSTITUTION SAVING THROWS, the only thing protecting Twinned Haste.
    - id: prog-hands
      item: 'Hands: Gloves of Belligerent Skies → Spellmight Gloves'
      slot: hands
      note: Act 1–2 Belligerent Skies (Crèche) for the Reverberation engine → Act 3 Spellmight (Circus, Find Dribbles the Clown). Cast the first Scorching Ray with Spellmight off so Acuity covers the −5.
    - id: prog-feet
      item: 'Boots: open → Evasive Shoes → Disintegrating Night Walkers'
      slot: feet
      note: 'Empty through Act 1 — every other option needs Medium Armour → Evasive Shoes (Mattis, Last Light) from Act 2 → Disintegrating Night Walkers in Act 3, free once Asterion moves to Kushigo. Acrobat Shoes are the Dexterity-save swap.'
    - id: prog-cloaks
      item: 'Cloak: none available → Thunderskin Cloak → Cloak of the Weave'
      slot: cloaks
      note: Empty in Act 1 → Thunderskin (Araj, Moonrise) in Act 2, which Dazes anything Reverberating that hits him → Cloak of the Weave (Helsik) in Act 3 for the flat +1 spell save DC and +1 spell attack.
    - id: prog-amulets
      item: 'Amulet: Pearl of Power → Spineshudder Amulet'
      slot: amulets
      note: Act 1 Pearl (Omeluum) for a free slot each rest → Act 2–3 Spineshudder (Mimic in Isobel's bedroom), which applies Reverberation on ranged spell-attack hits and so fires 3–7 times per Scorching Ray.
    - id: prog-ring1
      item: 'Ring 1: Ring of Protection → Callous Glow Ring'
      slot: ring 1
      note: Ring of Protection from Mol in Act 1, on the party's lowest-AC body → Callous Glow Ring from Act 2, whose +2 radiant applies to every ray while the target is lit.
    - id: prog-ring2
      item: 'Ring 2: Ring of Mind-Shielding → Coruscation Ring'
      slot: ring 2
      note: Ring of Mind-Shielding from Omeluum in Act 1 as concentration insurance → Coruscation Ring from Act 2, which lights the target that Callous Glow then punishes. Ring of Mental Inhibition is the swap for Command-heavy fights.
    - id: prog-weapons
      item: 'Main hand: The Spellsparkler → Markoheshkir'
      slot: weapons
      note: Spellsparkler builds Lightning Charges off every Scorching Ray instance but carries no enchantment bonus → Markoheshkir from Act 3 for +1 spell save DC and spell attack, Arcane Battery and an elemental attunement. Staff of Spellpower is the per-fight swap.
    - id: prog-offhand
      item: 'Off hand: Melf''s First Staff → Rhapsody'
      slot: weapons
      note: Melf's First Staff carries Acts 1–2 for +1 spell save DC and +1 spell attack rolls → Rhapsody in Act 3, whose +3 to everything applies per ray. Dual Wielder at character level 4 is what makes either pair legal.
    - id: prog-ranged
      item: 'Ranged: Bow of Awareness → Hellrider Longbow'
      slot: ranged weapons
      note: A stat-stick slot he never fires. Bow of Awareness (+1 Initiative) in Acts 1–2 → Hellrider Longbow (+3, Ferg Drogher, Rivington) in Act 3.
    - id: prog-consumables
      item: 'Elixir: Elixir of Vigilance, every long rest, all game'
      slot: consumables
      note: +5 Initiative and Surprise immunity, the substitute for the Alert feat this build cannot afford. Initiative is d4 + DEX, so +5 is larger than the whole die. No competing elixir on Gale.
  playstyle: |-
    - **Once per long rest:** cast Daylight (Enchant Item) on Bonbon's melee main hand — the Knife of the Undermountain King until the Resonance Stone, Phalar Aluve after. It keeps Gale lit for the Coruscation chain.
    - **Once per long rest, from Act 2:** equip the Drakethroat Glaive and Twin Draconic Elemental Weapon (3 sorcery points) onto Charles's main hand and Bonbon's Titanstring on the ground beside him. **Choose COLD every day.** From the Resonance Stone on, cast it *after* Charles summons his Shadow Blade.
    - **Before initiative:** on any fight you can see coming, pre-cast Twinned Haste. It lasts 10 turns, so turn 1's Action goes to Scorching Ray instead.
    - **Turn 1:** Quickened Scorching Ray (bonus action) into the highest-HP target with Spellmight Gloves OFF. A level-4 slot fires 5 rays and caps Arcane Acuity at 10. Switch Spellmight ON after that.
    - **Then pick a job each turn:** more Scorching Ray on a single target, Fireball on a cluster of 4+, or Extended Command on anything you want disabled. Command is not Concentration, so it never costs Haste.
    - **Stand within 3 m of a Held target.** Paralysed gives automatic crits to *any* attack inside 3 m, so all 5–7 rays crit. ⚠ Unverified: whether a ranged spell attack inside enemy reach takes Threatened disadvantage.
    - **Discharge Markoheshkir Heat into Fireball, never Scorching Ray.** A multi-hit spell consumes Heat on the first hit only; an area spell adds it to every target. Use the free Flame of Wrath Fireball.
    - **No fire into Charles's Hunger of Hadar.** Cast Armour of Landfall's Plant Growth (once per short rest) into the zone for a no-save lock, then keep Fireball, Scorching Ray and Heat outside it — fire burns Plant Growth away.
    - **Grouping:** Command: Approach pulls scattered enemies into one Fireball.
    - **Fire-immune fights** (House of Hope, Raphael, the red dragon, Yurgir): switch Markoheshkir to Bolts of Doom for a free Chain Lightning and Lightning Bolt each short rest, and lead with Cone of Cold or Ice Storm. Twinned Haste, Command and Counterspell are the rest of his contribution.
    - **Fire-vulnerability setup** (an exploit, and this is a non-Honour run): throw an Elixir of Fire Resistance at the target, have Bonbon hit it with Arsonist's Oil, then throw a second elixir to overwrite the resistance. The target ends Vulnerable to fire and every ray doubles.
    - **Do not** drop Fireball on Charles or Asterion before Careful Spell arrives at character level 11.
  traps:
  - 'Strange Ox: do NOT kill it at the Druid Grove in Act 1. It only carries the Hat of Fire Acuity from Last Light onward, and that hat is the build. Missing it in Act 2 is recoverable — the Ox reappears in Rivington.'
  - 'Flame of Wrath is a PER-FIGHT toggle, not a permanent attunement. Its Heat self-damage forces a CON save against Twinned Haste every turn and strips 2 turns of Arcane Acuity per tick, and Callous Glow adds +2 radiant to Gale''s own tick while he is lit. Do not attune before Armour of Landfall.'
  - 'Only two feats, at Sorc 4 and Sorc 8. No Alert and no War Caster: the Vigilance elixir covers initiative, and Spidersilk then Armour of Landfall cover concentration.'
  - 'Spellmight Gloves: probably +1d8 per ray (one build video says so; the wiki is silent). Confirm on the first cast — per ray is best in slot, once per spell is a −5 penalty on every roll for nothing.'
  - 'Fireball friendly fire: Careful Spell is the fourth metamagic at Sorc 10 (character level 11). Before that, Fireball is an adds-cluster tool and Scorching Ray is the boss tool.'
  - 'Idle pact slot: try converting it to a sorcery point at a short rest on any day Command is not needed. Unverified — try it once and record the answer.'
  - 'Long rests: this build burns spell slots fast. Bank camp supplies and buy Potions of Angelic Slumber in Act 3.'
  - 'Command does not work on Undead, and neither Hold spell works on crit-immune enemies. Act 2 is dense with Undead — lean on Fireball and Scorching Ray there.'
  - 'Respec cost: bank about 100 gp for the Withers respec out of Wizard, and re-pick metamagic and spells to match this plan. There are no further respecs.'
---
