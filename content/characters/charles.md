---
nickname: Charles
builds:
- name: The Three Booms
  is_primary: true
  role: Melee crit-smite nova frontline + self-supplied Hold Person
  class: Oath of Vengeance Paladin 6 / Hexblade Warlock 6
  at_a_glance:
    armour: Medium armour + shields (Hexblade) — Luminous Armour locked, a shield in the off-hand from the Grove
    elixir: 'Bloodlust on days with a Holdable target; Elixir of Heroism (+1d4 attacks and saves) when nothing is Holdable. Never Giant Strength — he attacks with CHA.'
    concentration: Hold Person — Hunger of Hadar only when nothing is Holdable
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
  stats_note: 'Point-buy 8/14/15/8/10/15, all 27 points spent. Half-Orc +2 to CHA and +1 to CON on the creation screen.'
  ability_targets: 'CHA 17 → 18 (Hag''s Hair) → 20 (Mirror of Loss: DC 25 Religion check + 60% roll, so Enhance Ability, Guidance and a quicksave first); CON stays 16.'
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
  locked_decisions: 'Five locks: Gloves of Battlemage''s Power from Act 2, Luminous Armour every act, Oath of Vengeance unbroken, Concentration on Hold Person only, and a shield in the off-hand from the Grove on. ⚠ The shield rules out Great Weapon Master and Dual Wielder.'
  feats:
  - at: Act 1 char 6 (Paladin 4)
    feat: Alert
    note: '+5 Initiative and Surprise immunity, permanently: d4+2 becomes d4+7, so Hold Person lands before the enemy acts. Great Weapon Master is not taken — the bonus attack was weighed and lost to Savage Attacker.'
  - at: Late Act 2 Resonance Stone respec (Warlock 4 feat; usually char 9)
    feat: Alert (re-picked)
    note: Take Alert again when the respec re-presents the Warlock-4 feat. Dual Wielder is not needed — Shadow Blade is one-handed and the off-hand holds the shield.
  - at: Late Act 2 Resonance Stone respec (Paladin 4 feat; usually char 9)
    feat: Savage Attacker
    note: Rerolls Shadow Blade, Booming Blade and Divine Smite damage dice on every auto-crit swing.
  weapon_plan: 'Act 1 — Phalar Aluve from the Underdark, bound as the Hexed Weapon, always behind a shield: plain Grove shield, then the Adamantine Shield. Char 9 respec — 3d8 Shadow Blade main hand. Act 3 — Viconia''s Walking Fortress. ⚠ Bind the Knife of the Undermountain King against Psychic-immune targets.'
  creation:
    level1_class: Warlock 1 (Hexblade patron)
    level1_gains: 'Pact Magic (1 × L1 short-rest slot), Hexblade''s Curse (bonus action, once per short rest; 20% free proc on a hexed-weapon hit; heals Warlock level + CHA when the target dies), Bind Hexed Weapon (attack with CHA).'
    subclass_choice: Hexblade patron (Warlock 1)
    proficiencies:
      armor_weapons: 'Medium armour, shields and martial weapons from Hexblade. ⚠ The Paladin levels add no heavy armour, which is why the GRYMSKULL HELM is illegal on him all run.'
      saving_throws: WIS + CHA (Warlock).
      skills: 2 Warlock picks + Haunted One (Medicine, Intimidation).
    starting_cantrips: 2 at Warlock 1 — Eldritch Blast + Booming Blade.
    starting_spells: '2 at Warlock 1 — Hex + Armour of Agathys — then a third at Warlock 2 (Shield), six by Warlock 5 and a seventh at Warlock 6. ⚠ The Hexblade expanded list costs picks; see the char-1 row.'
    notes: 'Take Warlock 1 first at creation and again at the respec — at STR 8 he needs Bind Hexed Weapon from the first fight. Stop Warlock at 2 in Act 1, then Paladin 1–5. The oath is never broken.'
  spells:
    note: 'A smite platform that sets up its own nova. Concentration is Hold Person only — Bless, Divine Favour, Hex, Darkness and both smite spells stay uncast. Hunger of Hadar is the one swap, for un-Holdable fights.'
    mandatory:
    - spell: Hold Person
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (55:42) — paralysis costs turns and gives automatic crits within 10 ft; humanoids only, best with high save DC'
      source: granted
      level: '2'
      guide_level: 7
      school: Enchantment
      save: WIS save (Concentration)
      when: char 7 (Paladin 5) — FREE always-prepared Oath of Vengeance spell
      why: 'THE CONCENTRATION. Paralysed humanoids take automatic critical hits from any attack within 3 m, and a crit doubles every smite die. Free from the oath at Paladin 5. Upcast from an L3 pact slot to Hold two humanoids at the same DC. ⚠ Humanoids only.'
    - spell: Inquisitor's Might
      level: Channel Oath (Oath of Vengeance, Paladin 1)
      guide_level: 3
      school: Oath action — Radiant
      save: None (the Daze rider has NO saving throw)
      when: char 3, and every fight thereafter
      why: 'THE DAMAGE BUTTON, from char 3. Bonus action plus the Channel Oath charge: for 2 turns his weapon hits add +CHA Radiant and can Daze with no save. That Radiant is what fires Luminous Armour''s Shockwave, and it costs no Concentration.'
    - spell: Divine Smite
      level: Feature (Paladin 2)
      school: Class feature — Radiant
      save: None (melee weapon attack roll)
      when: char 4
      why: 'Expend any slot on a melee hit for 2d8 Radiant, +1d8 per slot level above 1st, and the dice double on a crit. Set the Critical-Hit Divine Smite reactions to auto-confirm. Paladin 6 plus Warlock 6 is eight slots a rest cycle.'
    - spell: Shadow Blade
      tier: S
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (38:25) — all-day 2d8 finesse psychic weapon with advantage in the dark; broken with the Resonance Stone'
      level: '2'
      guide_level: 9
      school: Illusion
      save: None (bonus action to summon)
      when: Late Act 2 Resonance Stone respec (Warlock 5, usually char 9)
      why: 'POST-STONE core weapon. An L3 pact slot makes it 3d8 Psychic until long rest with no Concentration, and the Resonance Stone doubles the Psychic. It carries its own advantage against Lightly or Heavily Obscured targets, so it needs no arrow cloud.'
    recommended:
    - spell: Shield
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (43:07) — reaction +5 AC that only prompts when it turns a hit into a miss; worth a class dip on its own'
      level: '1'
      guide_level: 9
      school: Abjuration
      save: None (reaction, +5 AC)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'Reaction +5 AC, no Concentration, and the cheapest way to turn a hit that would break Hold Person into a miss. Re-picked at the respec.'
    - spell: Mirror Image
      tier: B
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (12:14) — +9 AC without concentration makes the AI stop targeting you, but costly every fight'
      level: '2'
      guide_level: 9
      school: Illusion
      save: None
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'Three duplicates, +9 AC, no Concentration — the answer to a chest locked at AC 17. Pre-cast it in any fight where he expects to be the focus; each miss removes a duplicate.'
    - spell: Armour of Agathys
      tier: A
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (7:37) — solid for any warlock, game-breaking on an Abjuration Wizard whose Arcane Ward preserves the temp HP'
      level: '1'
      guide_level: 1
      school: Abjuration
      save: None
      when: char 1, and re-picked at the respec
      why: 'Temp HP plus Cold retaliation off the pact slot, no Concentration. ⚠ Temp-HP sources never stack, so run this or the illithid Shield of Thralls, and cast Aid after it. Skip it on Elixir of Heroism days.'
    - spell: Aid
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (4:52) — party-wide max HP for the whole day, no concentration; multiplies summon survivability when upcast'
      level: '2'
      guide_level: 7
      school: Abjuration
      save: None
      when: char 7 (Paladin 5), and again from char 10 post-respec
      why: 'Party-wide +5 maximum HP until long rest, no Concentration, 9 m self-centred, and Charles is the party''s only source. ⚠ Cast it after summoning anything you want covered.'
    - spell: Command
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (28:37) — concentration-free turn denial that upcasts to multiple enemies; every higher-level slot competes with it'
      level: '1'
      guide_level: 4
      school: Enchantment
      save: WIS save
      when: char 4 (Paladin 2)
      why: 'No Concentration, so it runs alongside Hold Person. Upcast for one extra target per slot level to disable a cluster while he closes. Its DC rides Arcane Acuity. ⚠ Does not work on Undead.'
    - spell: Counterspell
      tier: S
      tier_note: 'Level 3 spells tier list, part 1 (A-G) (25:08) — top-five spell; trades a reaction for an enemy turn. NO SCROLLS EXIST, so it must be learnt on level-up'
      level: '3'
      guide_level: 9
      school: Abjuration
      save: Reaction
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'Pact-slot reaction, no Concentration. ⚠ L3 only, so it covers spells of level 3 and below outright; against anything higher it rolls INT, and his INT is 8.'
    - spell: Hunger of Hadar
      tier: S
      tier_note: 'Level 3 spells tier list, part 2 (H-W) (9:07) — no-save blind plus difficult terrain traps enemies inside; layer over Plant Growth to end fights. Acid save DC bugged to 12'
      level: '3'
      guide_level: 9
      school: Conjuration
      save: DEX save (Concentration)
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: 'THE CONCENTRATION SWAP for fights with nothing Holdable — non-humanoids, Undead, Constructs. A blinding difficult-terrain zone with Cold and Acid ticks, and Repelling Blast shoves escapers back in. ⚠ Hold Person or this, never both.'
    - spell: Misty Step
      tier: S
      tier_note: 'Spells tier list, level 2, part 2 (Knock through Web) (14:50) — top-five spell; bonus-action 60 ft teleport that every honour mode character should have access to'
      source: granted
      level: '2'
      guide_level: 7
      school: Conjuration
      save: None (bonus action)
      when: char 7 (Paladin 5) — FREE always-prepared Oath of Vengeance spell
      why: 'Free from the oath at Paladin 5, so it costs no Warlock pick. Bonus-action mobility to reach a priority target or leave a bad melee position.'
    - spell: Wrathful Smite
      tier: B
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (59:16) — 1d6 plus two turns of Frightened on a WIS save; now also a Hexblade spell after Patch 8'
      level: '1'
      guide_level: 4
      school: Evocation
      save: WIS save (Concentration)
      when: char 4 (Paladin 2) — prepared, but rarely cast
      why: '⚠ KEPT PREPARED, NEVER CAST — it is Concentration, so casting it drops Hold Person. Free off the Paladin list, so it costs nothing to hold for un-Holdable fights.'
    - spell: Eldritch Blast
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (23:10) — best damage cantrip; separate attack rolls give reliability, crit chances and per-beam riders'
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Ranged spell attack
      when: char 1 (Warlock 1)
      why: 'Ranged fallback for turns he cannot reach melee. Agonising Blast adds CHA per beam and Repelling Blast shoves escapers back into Hunger of Hadar. Its attack rolls ride Arcane Acuity; his weapon swings do not.'
    - spell: Booming Blade
      tier: S
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (16:31) — free thunder damage riding a normal weapon attack; once per action, so haste and Action Surge multiply it'
      level: Cantrip
      guide_level: 1
      school: Evocation
      save: Melee weapon attack roll
      when: char 1 (Warlock 1)
      why: 'The melee cantrip and the Acuity opener — lead with it every turn. It triggers the Ring of Arcane Synergy and the Gloves of Battlemage''s Power, and it fires once per Action even with Extra Attack.'
    - spell: Bane
      tier: B
      tier_note: 'Level 1 spells tier list, [Updated] part 1 (Animal Friendship to Goodberry) (12:55) — never worth a slot early; good late against bosses immune to stronger control, since few resist it'
      source: granted
      level: '1'
      guide_level: 5
      school: Enchantment
      save: CHA save (Concentration)
      when: char 5 (Paladin 3) — FREE always-prepared Oath of Vengeance spell
      why: Free from the oath and on the record only — it is Concentration, so it is never cast over Hold Person.
    - spell: Hunter's Mark
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (22:04) — the ranger''s Hex; weapon attacks only, but the damage matches your weapon type'
      source: granted
      level: '1'
      guide_level: 5
      school: Divination
      save: None (Concentration)
      when: char 5 (Paladin 3) — FREE always-prepared Oath of Vengeance spell
      why: Free from the oath and on the record only — Concentration, so it never displaces Hold Person.
    - spell: Mage Hand
      tier: A
      tier_note: 'Cantrips tier list, [Updated] Patch 8 (33:23) — costs a short-rest charge, but scouts, triggers traps, throws potions and soaks one enemy attack'
      level: Cantrip
      guide_level: 9
      school: Conjuration
      save: None
      when: Late Act 2 Resonance Stone respec (Warlock 5)
      why: Third cantrip at the respec. Scouts, manipulates objects and throws water bottles or potions without spending his Action.
    alternatives:
    - spell: Hex
      tier: S
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (21:08) — d6 on every attack roll all day, reapplied free on kills; enormous on multi-attack casters'
      level: '1'
      school: Enchantment
      save: None (Concentration)
      when: char 1 pick, dropped at the respec
      why: '+1d6 Necrotic per hit, and it powers the Strange Conduit Ring — but it is Concentration. Correct in Act 1 only; dropped at the respec once Hold Person owns the slot.'
    - spell: Darkness
      tier: S
      tier_note: 'Spells tier list, level 2, part 1 (Aid through Invisibility) (29:56) — blocks ranged attacks both ways; core of the devil''s sight darkness strategy'
      level: '2'
      school: Evocation
      save: None (Concentration)
      when: Deliberately NOT picked
      why: '⚠ DELIBERATELY NOT PICKED. Self-cast Darkness competes with Hold Person for Concentration, and farmed Arrows of Darkness make the same cloud for free. Keep buying arrows in every act.'
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
      why: Non-concentration defence — a chance to go Ethereal at the end of each turn. The third contender alongside Shield and Mirror Image.
    - spell: Protection from Evil and Good
      tier: C
      tier_note: 'Level 1 spells tier list, [Updated] part 2 (Grease to Wrathful Smite) (34:45) — disadvantage for aberrations and undead plus BROKEN TOOLTIP (real effect is blanket Frightened immunity, no charm protection); costs concentration'
      level: '1'
      school: Abjuration
      save: None (Concentration)
      when: Prepared-slot alternative
      why: Strong against Aberrations, Fey, Fiends and Undead, but Concentration, so it stays in the dead pile with Bless and Hex.
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
      note: A scaling ranged fallback plus the melee cantrip that triggers the Ring of Arcane Synergy and the Gloves of Battlemage's Power.
    - category: Spells
      picks: 2
      recommendation:
      - Hex
      - Armour of Agathys
      note: '⚠ Exactly TWO spells known at Warlock 1, not four — the Hexblade expanded list competes for the same two picks. Take Hex and Armour of Agathys; Shield is the Warlock-2 pick on the next level.'
    - category: Skills
      picks: 2
      recommendation:
      - Deception
      - Religion
      note: 'Easy to miss on the creation screen. ⚠ Do NOT take Intimidation — Half-Orc Menacing and Haunted One both grant it, and proficiency does not stack.'
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
      note: Devil's Sight lets him fight unblinded inside a Darkness cloud; Agonising Blast scales the ranged fallback with CHA.
    - category: Warlock spell
      picks: 1
      recommendation: Shield
      note: 'HIDDEN BEHIND THE INVOCATIONS: Warlock 2 raises Spells Known from 2 to 3, so click through to a third level-1 pick. Take Shield — a reaction, no Concentration, on a build that never passes AC 20.'
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
      note: 'LOCKED, never broken. Vengeance is the only oath with a non-Concentration per-hit Radiant rider, and Radiant is what fires Luminous Armour''s Shockwave. It also hands Hold Person and Misty Step over free at Paladin 5.'
    - category: Rotation
      recommendation: Spend the Channel Oath charge on Inquisitor's Might every fight
      note: Open every fight with Inquisitor's Might. +CHA Radiant on every weapon hit for 2 turns means every swing fires a Shockwave and stacks Radiating Orb within 3 m.
  - char_level: 4
    class: Paladin 2
    gains:
    - Divine Smite
    - Paladin Spellcasting
    - Fighting Style selection
    recommendations:
    - category: Fighting style
      picks: 1
      recommendation: Duelling
      note: 'DUELLING — he fights one-handed behind a shield from the Grove on, and a shield is not a weapon, so the style''s empty-hand clause is satisfied. +2 damage on every swing.'
    - category: Prepared spells
      picks: 5
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      note: 'FIVE prepared (Paladin level + CHA modifier), and the list re-opens whenever CHA rises. ⚠ Bless is deliberately absent — it is Concentration, and Asterion casts it off the Staff of Arcane Blessing. Unused slots become Divine Smites.'
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
      note: 'FREE AND ALWAYS PREPARED from Oath of Vengeance at Paladin 3 — no Warlock pick and no prepared slot. Both are Concentration, so neither is cast once Hold Person owns the slot at char 7.'
    - category: Channel Oath budget
      recommendation: Inquisitor's Might by default; Vow of Enmity only in Act 1 boss fights
      note: 'One short-rest charge buys Inquisitor''s Might or Vow of Enmity, not both. Take Vow of Enmity only for a long Act 1 boss fight; from Act 2 the Risky Ring supplies advantage, so it is always Inquisitor''s Might.'
    - category: Prepared spells
      picks: 6
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Divine Favour
      - Shield of Faith
      note: 'SIX prepared now (Paladin 3 + CHA 3), seven once the Hag''s Hair lands — the count is Paladin level + CHA modifier. Leave one slot open and prepare for the fight in front of you.'
  - char_level: 6
    class: Paladin 4
    gains:
    - Feat or Ability Score Improvement selection
    recommendations:
    - category: Feat
      picks: 1
      recommendation: Alert
      note: 'THE PERMANENT FEAT. +5 Initiative and Surprise immunity on the party''s slowest body, so Hold Person lands before the enemy acts. Great Weapon Master is not taken — he fights behind a shield.'
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
      note: 'EIGHT prepared (4 + CHA 4 once the Hag''s Hair lands) — a second selection on this level, easy to miss behind the feat. Leave one slot open. Skip Searing Smite, Heroism and Cure Wounds.'
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
      note: 'BOTH FREE at Paladin 5 — no Warlock pick and no prepared slot. This is why Hold Person is absent from his Warlock list, and why Misty Step is dropped from it at the respec.'
    - category: The nova comes online
      recommendation: Hold Person becomes his permanent Concentration
      note: 'THE PIVOT. Hold Person becomes his permanent Concentration, so he sets up his own auto-crit nova instead of waiting on Bonbon. Everything else that wanted Concentration is out for good.'
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
      note: 'NINE prepared (5 + CHA 4) and the level-2 list opens. Aid and Lesser Restoration fill it exactly, so no slot stays open. ⚠ Skip Branding Smite — Radiant, but Concentration. Skip Magic Weapon; Bind Hexed Weapon replaces it.'
  - char_level: 8
    class: Paladin 6 (pre-Stone continuation)
    gains:
    - Aura of Protection
    recommendations:
    - category: Timing
      recommendation: Cast Aura of Protection once, and keep the Phalar + Adamantine Shield package until the Resonance Stone
      note: '⚠ CAST AURA OF PROTECTION ONCE on this level — it is not on by default and a respec removes it. 3 m radius, +CHA to every party save, and it is the first line of defence for the Hold Person he is about to carry.'
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
      note: 'TEN prepared (6 + CHA 4). Paladin 6 adds a tenth slot behind Aura of Protection and the char-7 nine carry over, so leave the last one open for the day''s fight.'
  - char_level: 9
    class: RESPEC at the Resonance Stone — Warlock 5 / Paladin 4
    gains:
    - Pact of the Blade and Deepened Pact
    - Level 3 Pact slots and 3d8 Shadow Blade
    - Alert re-picked (Warlock 4 feat)
    - Paladin 4 Savage Attacker
    recommendations:
    - category: Patron and skills
      picks: 3
      recommendation:
      - Hexblade
      - Deception
      - Religion
      note: '⚠ Take WARLOCK first again — a Withers respec rebuilds from scratch, and Paladin-first would only buy heavy armour proficiency this build never uses. Re-pick Deception and Religion.'
    - category: Oath
      picks: 1
      recommendation: Oath of Vengeance again — do NOT break it
      note: Re-select Vengeance so Inquisitor's Might, Hold Person and Misty Step all come back. There is no oath break anywhere in this plan.
    - category: Oath spells
      granted: true
      recommendation:
      - Bane
      - Hunter's Mark
      note: 'WHAT THE RESPEC COSTS. At Paladin 4 he only re-earns the Paladin-3 grant, so Hold Person and Misty Step are gone until char 10. Bridge with Hunger of Hadar or Bonbon''s Hold; spend no Warlock pick on it.'
    - category: Warlock feat
      picks: 1
      recommendation: Alert
      note: Re-pick Alert. Dual Wielder is never needed — Shadow Blade is one-handed and the off-hand holds the Adamantine Shield.
    - category: Paladin feat
      picks: 1
      recommendation: Savage Attacker
      note: 'Savage Attacker. ⚠ If the Stone lands at level 8, take Warlock 5 / Paladin 3 for Alert and add Paladin 4 with Savage Attacker on the next level.'
    - category: Pact Boon
      picks: 1
      recommendation: Pact of the Blade
      note: A real three-way choice at Warlock 3, and the prerequisite for Deepened Pact's extra attack.
    - category: Invocations
      picks: 3
      recommendation:
      - Devil's Sight
      - Agonising Blast
      - Repelling Blast
      note: 'THREE, not two — 2 at Warlock 2 plus 1 at Warlock 5. ⚠ Invocations cannot be swapped on level-up, so set all three here. Avoid Fiendish Vigour; its False Life clashes with Armour of Agathys.'
    - category: Fighting style
      picks: 1
      recommendation: Duelling (again)
      note: Re-chosen at Paladin 2 during the respec. Shadow Blade is one-handed behind a shield, so Duelling's +2 rides every swing and the Stone doubles it.
    - category: Warlock cantrips
      picks: 3
      recommendation:
      - Eldritch Blast
      - Booming Blade
      - Mage Hand
      note: THREE cantrips at Warlock 5 (2 at W1, +1 at W4), all re-picked. Booming Blade triggers the Ring of Arcane Synergy and the Battlemage's Power gloves.
    - category: Warlock spells
      picks: 6
      recommendation:
      - Shadow Blade
      - Counterspell
      - Armour of Agathys
      - Shield
      - Mirror Image
      - Hunger of Hadar
      note: 'SIX known at Warlock 5. ⚠ Darkness is out — the arrows do it free — and Misty Step is out, free from the oath; those two picks go to Shield and Mirror Image. Hex is dropped because Hold Person owns the slot.'
    - category: Prepared spells
      picks: 8
      recommendation:
      - Command
      - Wrathful Smite
      - Thunderous Smite
      - Compelled Duel
      - Protection from Evil and Good
      note: 'EIGHT prepared (Paladin 4 + CHA 4), LEVEL 1 ONLY — Paladin 4 has no level-2 slots, so Aid waits for char 10. Three slots stay open; the level-1 leftovers are all Concentration and never get cast.'
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
      note: Free and always prepared again at Paladin 5, which restores the nova setup the respec took away for two levels.
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
      note: 'TEN prepared (5 + CHA 5 once Mirror of Loss lands) and the level-2 list re-opens. Aid and Lesser Restoration are the new pair, and three slots stay open for the day''s fight.'
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
      note: 'ELEVEN prepared (6 + CHA 5); Protection from Poison is the only addition worth naming. ⚠ CAST AURA OF PROTECTION AGAIN — the respec removed it, and it props up the Hold Person concentration he carries under the Risky Ring.'
  - char_level: 12
    class: Warlock 6
    gains:
    - Accursed Spectre
    - Seventh Warlock spell known
    recommendations:
    - category: Accursed Spectre
      recommendation: Curse the nova target; a kill within 18 m raises a spectre on a reaction
      note: 'When Charles or an ally kills a creature under Hexblade''s Curse, a reaction raises a 10-turn spectre — 31 HP, AC 14, Devour Soul heals Charles, Pluck Soul pulls 5 m. ⚠ Not on constructs, elementals, oozes, plants or undead.'
    - category: Warlock spells
      picks: 1
      recommendation:
      - Darkness
      note: 'The seventh spell known. Darkness as a spare cloud, or a Warlock Hold Person for a second Hold off a short-rest slot. ⚠ Self-cast Darkness still costs Concentration, so the arrows stay the default.'
  nova:
    assumptions: |
      Character 12 (Paladin 6 / Warlock 6), CHA 20, proficiency +4, **non-Honour rules**. Every number assumes a HELD humanoid with Charles inside 3 m, so every attack auto-hits and is an automatic critical hit.
      - **Resonance Stone** within 9 m for Psychic vulnerability, **Phalar Shriek** up from Bonbon within 6 m, **Savage Attacker** and Half-Orc Savage Attacks rerolling every die.
      - Smite fuel is six Paladin slots (4 × L1, 2 × L2). ⚠ Keep both L3 pact slots for Counterspell, Shield and the two-target Hold Person.
      - Set the L2 Critical Hit Divine Smite reaction to auto-confirm and leave L1 and L3 on Ask.
      - The arithmetic, the without-Stone figures and what each engine assumes: docs/build-notes-charles.md.
    configs:
    - name: 'Standard nova — Hasted, Held target'
      lines:
      - line: 'PREP, the two turns before — Hexblade''s Curse on the target, then Inquisitor''s Might, one bonus action each, so the nova turn''s bonus action is free.'
        count: '—'
        each: '—'
        total: '—'
      - line: 'Booming Blade lead + Divine Smite. Booming Blade adds 2d8 Thunder on impact, doubled to 4d8 by the crit.'
        count: 1
        each: 175
        total: 175
      - line: 'Extra Attack ×2 — Paladin 5 and Deepened Pact stack outside Honour — each + Divine Smite'
        count: 2
        each: 152
        total: 304
      - line: 'Duelling — +2 on every one-handed swing, Psychic through Shadow Blade and so doubled by the Stone'
        count: 3
        each: 4
        total: 12
      - line: 'Dolor Amarus (Vicious Shortbow held in the ranged slot) — +7 flat on every critical hit, and every swing crits'
        count: 3
        each: 7
        total: 21
      - line: 'Haste action — Hold Person at DC 27, Command, or Hunger of Hadar. No damage, but it sets up the next nova.'
        count: 1
        each: 0
        total: 0
      turn_total: 512
    - name: 'Ceiling — Haste + Terazul + Elixir of Bloodlust'
      lines:
      - line: 'PREP — Hexblade''s Curse and Inquisitor''s Might on the two prior turns, one bonus action each; Elixir of Bloodlust out of combat. Terazul needs no bonus action and stacks with Hastened.'
        count: '—'
        each: '—'
        total: '—'
      - line: 'Booming Blade lead — it recharges per Action, so once in each of the three attack actions (base + Haste + Terazul)'
        count: 3
        each: 135
        total: 404
      - line: 'Extra Attack ×2 inside each of those three actions — outside Honour the Hastened and Bloodlust actions do get Extra Attack'
        count: 6
        each: 111
        total: 668
      - line: 'Duelling — +2 per swing, doubled by the Stone, across all nine swings'
        count: 9
        each: 4
        total: 36
      - line: 'Divine Smite on 7 of the 9 attacks — every slot he owns (1 × L3 pact, 2 × L2, 4 × L1)'
        count: 7
        each: '29–52'
        total: 251
      - line: 'Hexblade''s Curse — +proficiency per damage roll, weapon-typed and so doubled by the Stone'
        count: 9
        each: 8
        total: 72
      - line: 'Dolor Amarus (Vicious Shortbow held in the ranged slot) — +7 flat per critical hit across all nine swings'
        count: 9
        each: 7
        total: 63
      - line: 'Fourth action, granted by Bloodlust on the kill — Hold Person / Command'
        count: 1
        each: 0
        total: 0
      turn_total: 1494
    caveats: |
      - ⚠ **Check the target for crit immunity before spending slots.** Adamantine Scale Mail, Adamantine Splint Armour, the Grymskull Helm, the Helldusk Helmet and the Helm of Balduran all cancel Hold Person's guaranteed crits.
      - ⚠ **Bloodlust's extra action needs a kill that turn.** Kill a Held add and leave the boss Held, or upcast Hold Person from an L3 pact slot and hold two humanoids.
      - ⚠ **Terazul and Haste both end in Lethargic** — a full turn unable to move or act, and Terazul runs only 2 turns, so the bill arrives immediately.
      - ⚠ **Verify whether extra actions get Extra Attack in your install.** If they do not, the ceiling turn collapses to roughly 700.
      - Spreads, simulations, the Dolor Amarus per-rider question and the rejected leads: docs/build-notes-charles.md.
  itemization:
    act1:
    - id: early-hexed-weapon
      item: Early pact-bound weapon (temporary)
      wiki: false
      slot: weapons
      note: Before Phalar, bind the best one-handed weapon so it attacks with CHA, and buy a plain Shield from the first Grove vendor that stocks one.
    - id: phalar-aluve-two-handed
      item: Phalar Aluve
      tier: S
      tier_note: 'The BEST WEAPON TYPE in BG3 - Versatile Weapons Honor Mode Tier List and Guide - Act 1 (30:10) — one of the best weapons in the game even ignoring the strongest thing it does'
      slot: weapons
      bis: true
      note: 'ACT-1 DEFAULT, from the Underdark. Bind it as the Hexed Weapon and one-hand it behind the shield. Pre-cast SHRIEK — always Shriek, never Sing — and keep it equipped; the 6 m aura covers Charles and Asterion. It goes to Bonbon at the Stone.'
    - id: plain-shield-charles
      item: Shield
      tier: S
      tier_note: '5wATdII3wmI (7:41) — all non-magical variants combined; +2 AC in the early game is a huge snowballing bonus'
      wiki: Shield (item)
      slot: off-hand
      note: 'HIS FIRST SHIELD — a plain +2 AC Shield from any Grove vendor, and Hexblade grants shield proficiency. It holds the slot until the Adamantine Shield is poured at the Forge. ⚠ The Safeguard Shield is Bonbon''s.'
    - id: adamantine-shield
      item: Adamantine Shield
      tier: S
      tier_note: '5wATdII3wmI (11:49) — best defensive shield all game: Shield Bash, Reeling on misses, no critical hits against you'
      rank: '#13'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #13 of 20 — critical-hit immunity without needing medium or heavy armour proficiency'
      slot: off-hand
      bis: true
      note: 'THE SECOND MITHRAL ORE, poured with the Shield mould at the Forge. +2 AC, attackers cannot land critical hits, and a melee miss sends the attacker Reeling. Wear it until the Helm of Balduran covers crits in Act 3.'
    - id: haste-helm
      item: Haste Helm
      tier: S
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (27:11) — wanted somewhere in just about every party; it opens up combat options'
      rank: '#19'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #19 of 20 — three turns of Momentum at combat start decides whether a turn matters'
      slot: head
      note: 'ACT-1 HEAD, from the Moss-Covered Chest in the Blighted Village. Three turns of opening Momentum on the party''s slowest body. ⚠ The GRYMSKULL HELM is illegal all run — it needs Heavy Armour proficiency.'
    - id: luminous-armour
      item: Luminous Armour
      tier: S
      tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (22:22) — a game-winning armour; the list had no S tier until this item was given one'
      rank: '#2'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #2 of 20 — Radiating Shockwave stacks Radiating Orb across an encounter'
      slot: armour
      bis: true
      note: 'LOCKED CHEST FOR THE WHOLE RUN, from the Selûnite Outpost. Every point of Radiant he deals fires a RADIANT SHOCKWAVE, spreading Radiating Orb 3 m for up to −10 to attack rolls. ⚠ It hits non-allied creatures only, neutrals included — allies are safe, neutral NPCs are not.'
    - id: act1-hands-charles
      item: Glove slot
      slot: hands
      wiki: false
      note: 'A PLACEHOLDER BY DESIGN — his best-in-slot is the Gloves of Battlemage''s Power and it does not exist until Act 2. Wear whichever of these the next fight wants.'
      options:
      - id: gloves-of-the-growling-underdog
        item: Gloves of the Growling Underdog
        tier: B
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (32:54) — advantage when surrounded is powerful but the positioning work is punishing'
        note: 'DEFAULT. Dror Ragzlin''s treasure room. Advantage on melee attacks when 2+ enemies stand within 3 m of the target — a free advantage source before the Risky Ring.'
      - id: opt-gloves-of-baneful-striking
        item: Gloves of Baneful Striking
        tier: A
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (18:20) — strong, but the character has to be built around them'
        note: 'Lady Esther, late Act 1. A weapon hit gives the target −1d4 to saving throws for 2 turns. Swap it in on any turn the party needs a save to land.'
      - id: opt-gloves-of-power
        item: Gloves of Power
        tier: B
        tier_note: 'The MOST IMPORTANT ITEMS in BG3 - Gloves Tier List and Guide - Act 1 (31:21) — swapped in and out around Sleight of Hand rather than worn full time'
        note: "Za'krug at the Grove gate. A branded wearer's hits inflict Absolute's Bane, −1d4 to attacks and saves. Weakest of the three, but free and early."
    - id: boots-of-striding
      item: Boots of Striding
      tier: A
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (16:09) — always worth looking at for the characters they suit'
      slot: feet
      bis: true
      note: 'FLEX SLOT FROM ACT 1, and in Act 1 the default is Stormy Clamour. Minthara''s drop. Focused Stride blocks Prone and forced movement, which is what protects Concentration — switch to these at char 7 when Hold Person arrives.'
      options:
      - id: opt-boots-of-stormy-clamour-charles-a1
        item: Boots of Stormy Clamour
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (12:32) — the best way to apply Reverberation, and many builds are based on it'
        rank: '#7'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #7 of 20 — any condition also applies Reverberation; build-defining later'
        note: 'THE ACT 1 DEFAULT, from Omeluum in the Ebonlake Grotto. Inflicting a condition also inflicts 2 turns of Reverberation, and every Radiant Shockwave is a condition, so every swing procs. ⚠ One target per trigger, so it is single-target pressure.'
    - id: amulet-of-misty-step
      item: Amulet of Misty Step
      tier: A
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (10:19) — awesome, because it patches a weakness a party may not otherwise cover'
      slot: amulets
      note: SELECTED neck, from Priestess Gut's chambers. Misty Step once per short rest solves approach and elevation until Paladin 5 grants the spell free.
    - id: ring-of-arcane-synergy
      item: Ring of Arcane Synergy
      tier: A
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (21:54) — an extremely powerful effect, but a better source of it exists for most builds'
      slot: ring 1
      note: 'Gish Far''aag, Crèche. A Booming Blade hit grants Arcane Synergy for 2 turns, adding CHA to subsequent weapon attacks. ⚠ Never run it alongside Bonbon''s Diadem of Arcane Synergy — the condition does not stack with itself.'
    - id: strange-conduit-ring
      item: Strange Conduit Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (44:11) — easy to keep active all the time, and it raises damage output dramatically'
      rank: '#5'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #5 of 20 — 1d4 psychic on every weapon attack while concentrating'
      slot: ring 2
      bis: true
      note: '+1d4 Psychic on weapon attacks while Concentrating, from the Crèche. Hold Person keeps it live permanently and the Resonance Stone doubles it. ⚠ It does not cover Unarmed Strike, so it can never move to Asterion.'
    - id: arrows-of-darkness
      item: Arrows of Darkness
      tier: S
      tier_note: 'ZMCimWeIxCk (28:35) — PLACED IN S+ TIER: concentration-free Darkness cast as an attack; only S tier without warlocks or blind-immunity gear'
      wiki: Arrow of Darkness
      slot: consumables
      bis: true
      note: 'THE DARKNESS SOURCE FOR THE WHOLE RUN. 3 m cloud, 3 turns, no Concentration. It blocks ranged attacks both ways and Blinds enemies inside it, and Devil''s Sight lets Charles fight on. ⚠ Advantage only lands on enemies without darkvision, which is a minority. Restock every act.'
    - id: dual-hand-crossbows-plus-one
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      slot: ranged weapons
      note: 'ACT 1–2 RANGED, a pair, and mainly a Darkness-Arrow launcher. Farm Dammon, Roah, Derryth and Jeera for +1 copies. ⚠ Standing in his own cloud blocks ranged attacks both ways, so expect nothing else from the slot.'
    - id: elixir-charles
      item: Elixir of Bloodlust
      tier: S
      tier_note: '9BcQXb37Bik (22:44) — extra action per kill; on Honour that action gets no Extra Attack, on Tactician or below it does'
      slot: consumables
      note: 'Every long rest on days with a Holdable target: a kill buys another Action. Never Giant Strength; he attacks with CHA.'
      options:
      - id: opt-elixir-of-heroism-charles
        item: Elixir of Heroism
        tier: A
        tier_note: '9BcQXb37Bik (41:48) — day-long bless that stacks with the real spell; very top of A, nearly S'
        note: 'Days with nothing to Hold: +1d4 to attack rolls and saving throws until long rest, stacks with Bless. No Armour of Agathys that day.'
    - id: auntie-ethel-s-hair-cha-17-18
      item: Auntie Ethel's Hair
      slot: consumables
      note: CHARISMA 17 → 18. Raises Aura DCs, attack and smite accuracy, Inquisitor's Might's radiant rider, the Hold Person DC, and his prepared-spell count.
    - id: act1-cloak-charles
      item: No cloak exists yet
      slot: cloaks
      note: 'Deliberately empty. The Deathstalker Mantle is Act 1''s only magical cloak and it goes to Asterion, so he is bare-shouldered until Quartermaster Talli at Last Light.'
    act2:
    - id: self-cast-shadow-blade-upcast-to-3d8
      item: Shadow Blade
      wiki: Shadow Blade (weapon)
      slot: weapons
      bis: true
      note: 'POST-RESONANCE DEFAULT. Keep Phalar and the Adamantine Shield until the late-Act-2 Stone pickup, then summon a 3d8 Shadow Blade off an L3 pact slot and bind it main hand for CHA. ⚠ Bind the Knife of the Undermountain King against Psychic-immune targets.'
    - id: act2-offhand-charles
      item: Adamantine Shield
      tier: S
      tier_note: '5wATdII3wmI (11:49) — best defensive shield all game: Shield Bash, Reeling on misses, no critical hits against you'
      rank: '#13'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #13 of 20 — critical-hit immunity without needing medium or heavy armour proficiency'
      held: 1
      slot: off-hand
      bis: true
      note: 'CARRIED OVER, and the off-hand for good — Shadow Blade is one-handed. +2 AC and crit immunity on the body holding Hold Person. ⚠ Phalar Aluve moves to Bonbon here, so keep the melee cluster within 6 m of her for Shriek.'
    - id: gloves-of-battlemage-s-power
      item: Gloves of Battlemage's Power
      tier: A
      tier_note: 'The BEST GLOVES In Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (18:12) — A on the list''s own terms: he says A tier if the Arcane Acuity effect worked, and placed it in D only because it was bugged when he recorded. This run treats the effect as working, so the A stands'
      slot: hands
      bis: true
      note: 'THE ACUITY ENGINE and a locked slot. Reithwin Tollhouse, locked opulent chest on the second floor. A spell or cantrip that uses a weapon grants +1 spell save DC per remaining turn, up to +10. ⚠ Every hit cuts the duration by 2, so Hold before the enemy''s turn.'
    - id: act2-armour-charles
      item: Luminous Armour
      tier: S
      tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (22:22) — a game-winning armour; the list had no S tier until this item was given one'
      rank: '#2'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #2 of 20 — Radiating Shockwave stacks Radiating Orb across an encounter'
      held: 1
      slot: armour
      bis: true
      note: CARRIED OVER — locked. Crit immunity comes from the Adamantine Shield in the off-hand instead of the chest.
    - id: act2-head-charles
      item: Holy Lance Helm
      tier: S
      tier_note: 'The MOST BROKEN Item Slot in Baldur''s Gate 3 - Helmets Tier List and Guide - Act 1 (33:55) — radiant retaliation with no cooldown; chains with radiating orb and reverberation gear'
      slot: head
      bis: true
      note: 'ACT-2 HEAD, from a painted chest on the top level of Rosymorn Monastery, replacing the Covert Cowl. Its Radiant tick fires a Shockwave on ENEMY turns and refills Arcane Acuity between his own, which answers Acuity decay. ⚠ Act 3 takes the Helm of Balduran instead.'
      options:
      - id: opt-covert-cowl-act2
        item: Covert Cowl
        tier: A
        tier_note: 'BAN These Items - BG3 Helmets Tier List and Guide - Act 2 (17:07) — shows up in a lot of builds, though some versions of them want something else'
        wiki: Covert Cowl
        note: 'THE NON-HELD ALTERNATIVE, from Last Light. −1 crit threshold while Obscured, and an arrow cloud is Heavily Obscured. ⚠ Worth nothing against a Held target, so swap it in only for fights with nothing Holdable.'
    - id: act2-feet-charles
      item: Boots of Striding
      tier: A
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (16:09) — always worth looking at for the characters they suit'
      held: 1
      slot: feet
      note: 'CARRIED OVER, and now the default half of the flex. Prone ends Concentration with no save, so Prone immunity is the most important defensive job on him. Swap to Stormy Clamour only when nothing can knock him down.'
      options:
      - id: opt-boots-of-stormy-clamour-charles-a2
        item: Boots of Stormy Clamour
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (12:32) — the best way to apply Reverberation, and many builds are based on it'
        rank: '#7'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #7 of 20 — any condition also applies Reverberation; build-defining later'
        held: 1
        note: 'THE FLEX, and Act 2 is its peak: the Holy Lance Helm''s Radiant retaliation fires on enemy turns, and each one is another Reverberation on whoever missed. ⚠ Shared with Asterion — whoever inflicts more conditions that fight wears them. The cost is Prone immunity.'
    - id: act2-amulet-charles
      item: Neck slot
      slot: amulets
      wiki: false
      note: 'GENUINELY OPEN. Misty Step arrives free from the oath at Paladin 5, so the amulet''s reason for being here is gone, and the Amulet of Greater Health in Act 3 is the real answer. Treat this as a parking space.'
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
        note: '⚠ DO NOT TAKE IT. Crackling Resonance fires on the wearer''s own ranged spell attacks, not on being hit, and his only one is Eldritch Blast. It is Gale''s.'
      - id: opt-amulet-of-restoration
        item: Amulet of Restoration
        tier: S
        tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (23:45) — some character should have this equipped'
        note: 'Derryth Bonecloak, Underdark. Healing Word and Mass Healing Word once each per long rest with no class requirement — a free party heal out of a slot he has nothing better for.'
    - id: strange-conduit-act2
      item: Strange Conduit Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (44:11) — easy to keep active all the time, and it raises damage output dramatically'
      rank: '#5'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #5 of 20 — 1d4 psychic on every weapon attack while concentrating'
      slot: ring 1
      bis: true
      note: 'LOCKED RING FROM ACT 2. Hold Person keeps him Concentrating, so the +1d4 Psychic is live on every swing and the Stone doubles it. It is the only ring he owns that still pays out against a Held target.'
    - id: act2-ring2-charles
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'THE FLEX SLOT, and one question decides it: is the target Held? Held means Arcane Synergy, because advantage and a banked crit are worth nothing on an auto-crit. Un-Holdable means Risky Ring.'
      options:
      - id: risky-ring
        item: Risky Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:21) — too good to leave at home, given a way to cover the saving-throw downside'
        note: 'Moonrise, from Araj Oblodra. Advantage on all attacks, disadvantage on saves; it makes Vow of Enmity redundant and frees the Channel Oath charge. ⚠ The save disadvantage taxes the Hold Person concentration — cover it with the Adamantine Shield, Aura of Protection and the Amulet of Greater Health.'
      - id: ring-of-arcane-synergy-act2
        item: Ring of Arcane Synergy
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (21:54) — an extremely powerful effect, but a better source of it exists for most builds'
        note: 'THE HELD-TARGET PICK, and nobody else wants it after Act 1. A Booming Blade hit switches Arcane Synergy on for 2 turns: +CHA per weapon attack on top of the pact weapon''s own, doubled by the Stone. ⚠ Never alongside Bonbon''s Diadem.'
      - id: killer-s-sweetheart
        item: Killer's Sweetheart
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (14:36) — very good for builds rolling a lot of damage dice, but only one encounter per day'
        note: 'Gauntlet of Shar, Self-Same Trial — on the ground where your shadow copy dies. The first attack after a kill is a guaranteed crit; set it to Ask and bank it. ⚠ Worth nothing against a Held target, so it is a fallback only.'
    - id: shadow-blade-ring
      item: Shadow Blade Ring
      tier: B
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (36:56) — better for builds that hold concentration easily; narrower otherwise'
      slot: other
      note: 'NOT a third ring. Its Shadow Blade needs no Concentration and lasts until long rest, and the ring can be unequipped after summoning. Carry it for fights where he cannot spare a pact slot.'
    - id: cloak-of-protection
      item: Cloak of Protection
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (13:30) — excellent, and someone in the party will almost certainly be wearing it'
      slot: cloaks
      bis: true
      note: 'HIS, not Gale''s. Quartermaster Talli at Last Light Inn. +1 Armour Class and +1 to Saving Throws. ⚠ Exactly one exists, and it goes to the body carrying permanent save disadvantage from the Risky Ring.'
    - id: act2-ranged-charles
      item: Hand Crossbow +1
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (13:57) — best Act 1 hand crossbow; a pair is the highest damage archer setup'
      held: 1
      slot: ranged weapons
      note: CARRIED OVER as the Darkness-Arrow launcher, still a pair. Close to a dead slot on any turn he stands in his own cloud, which is most of them.
    - id: resonance-stone-aura
      item: Resonance Stone
      slot: other
      note: 'LATE ACT 2, Mind Flayer Colony — this pickup triggers the respec. The 9 m aura makes creatures Psychic-vulnerable, doubling Shadow Blade and Strange Conduit. Asterion carries it within 9 m. ⚠ It also gives ALLIES Psychic vulnerability and mental-save disadvantage, so holster it against Psychic attackers.'
    act3:
    - id: shadow-blade-phalar-act3-default
      item: Shadow Blade
      held: 2
      wiki: Shadow Blade (weapon)
      slot: weapons
      bis: true
      note: 'CARRIED OVER unchanged — a 3d8 Shadow Blade main hand, bound for CHA and Deepened Pact, with a shield in the off-hand. ⚠ Bind the Knife of the Undermountain King against Psychic-immune targets, and confirm the Stone aura still works after Act 2.'
    - id: viconias-walking-fortress
      item: Viconia's Walking Fortress
      tier: S
      tier_note: '5wATdII3wmI (47:46) — +3 AC, upgraded Shield Bash, spell defences and Reflective Shell; the legendary shield earns it'
      slot: off-hand
      bis: true
      note: 'ACT-3 OFF-HAND, from Viconia DeVir in the Cloister of Sombre Embrace under the House of Grief. +3 AC, advantage on saves against spells, and spell attacks against him at disadvantage. ⚠ Do not swap until the Helm of Balduran supplies crit immunity.'
    - id: act3-head-charles
      item: Helm of Balduran
      tier: S
      tier_note: 'Is EVERY Act 3 Helmet Awesome? - BG3 Helmets Tier List and Guide - Act 3 (17:36) — purely defensive, yet any character wanting a defensive option wants this'
      slot: head
      bis: true
      note: 'SELECTED ACT-3 HEAD, from the Wyrmway (Ansur). Attackers cannot land critical hits, +1 AC, +1 to saving throws and Stun immunity. ⚠ It is what frees the off-hand for Viconia''s Walking Fortress; a crit roughly doubles the Hold Person concentration DC.'
    - id: act3-armour-charles
      item: Luminous Armour
      tier: S
      tier_note: 'BG3''S BEST ARMOR - Medium Armor Tier List - Honour Mode Guide - Part 3 (22:22) — a game-winning armour; the list had no S tier until this item was given one'
      rank: '#2'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #2 of 20 — Radiating Shockwave stacks Radiating Orb across an encounter'
      held: 1
      slot: armour
      bis: true
      note: CARRIED OVER — locked for the whole run. Helldusk Armour's AC 21 and −3 damage are the price of the Radiant Shockwave engine; Helm of Balduran, the Walking Fortress, Shield and Mirror Image carry the defence instead.
    - id: act3-hands-charles
      item: Gloves of Battlemage's Power
      tier: A
      tier_note: 'The BEST GLOVES In Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (18:12) — A on the list''s own terms: he says A tier if the Arcane Acuity effect worked, and placed it in D only because it was bugged when he recorded. This run treats the effect as working, so the A stands'
      held: 2
      slot: hands
      bis: true
      note: 'CARRIED OVER, locked. Helldusk Gloves and Craterflesh Gloves are both forgone: Arcane Acuity makes Hold Person land, and Hold Person makes every swing crit.'
    - id: act3-feet-charles
      item: Helldusk Boots
      tier: S
      tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (1:00:13) — the saving throw makes the wearer extremely safe in almost every circumstance'
      slot: feet
      bis: true
      note: 'ACT-3 BOOTS, in a locked Gilded Chest on the top floor of Wyrm''s Rock Fortress, and the default half of the flex. Prone immunity, Steadfast against forced movement, and a bonus-action Hellcrawler teleport. ⚠ Infernal Evasion is once per LONG rest, not per turn.'
      options:
      - id: opt-boots-of-stormy-clamour-charles-a3
        item: Boots of Stormy Clamour
        tier: S
        tier_note: 'The BEST BOOTS in Baldur''s Gate 3 - Complete Tier List and Guide (12:32) — the best way to apply Reverberation, and many builds are based on it'
        rank: '#7'
        rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #7 of 20 — any condition also applies Reverberation; build-defining later'
        held: 1
        note: 'THE FLEX, carried the whole run — take the Reverberation against casters and ranged packs, keep the Helldusk against anything with a Shove or a knockdown. ⚠ Shared with Asterion; whoever inflicts more conditions that fight wears them.'
    - id: amulet-of-greater-health
      item: Amulet of Greater Health
      tier: S
      tier_note: 'The BEST AMULETS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 3 (13:32) — the only real decision left is who to put it on'
      slot: amulets
      bis: true
      note: 'ACT-3 NECK, leftmost pedestal in the House of Hope Archive. Sets Constitution to 23 and grants advantage on Constitution saving throws, which cancels the Risky Ring''s disadvantage on concentration checks. ⚠ Contested with Gale; Charles wins. Steal it on a DC 20 Sleight of Hand.'
    - id: act3-ring1-charles
      item: Strange Conduit Ring
      tier: S
      tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (44:11) — easy to keep active all the time, and it raises damage output dramatically'
      rank: '#5'
      rank_note: 'The 20 BEST ITEMS in Act 1 - Baldur''s Gate 3 Honour Mode Guide, #5 of 20 — 1d4 psychic on every weapon attack while concentrating'
      held: 2
      slot: ring 1
      bis: true
      note: 'CARRIED OVER and still locked — every attack the nova adds multiplies it. ⚠ It is Psychic, so it is the line most exposed to the Resonance Stone failing after Act 2.'
    - id: act3-ring2-charles
      item: Second ring
      slot: ring 2
      wiki: false
      note: 'Same flex slot as Act 2. Run Arcane Synergy for most of Act 3, because Hold Person now lands on essentially every humanoid at DC 27. Keep Risky Ring bagged for bosses that cannot be Held.'
      options:
      - id: opt-arcane-synergy-act3
        item: Ring of Arcane Synergy
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 1 (21:54) — an extremely powerful effect, but a better source of it exists for most builds'
        note: 'THE DEFAULT ONCE HOLD PERSON IS RELIABLE. Booming Blade triggers it, so it is live from the second attack on: +CHA per weapon hit, stacking on the pact weapon''s CHA and doubled by the Stone. ⚠ Not alongside Bonbon''s Diadem.'
      - id: opt-risky-ring-act3
        item: Risky Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (34:21) — too good to leave at home, given a way to cover the saving-throw downside'
        held: 2
        note: 'THE NON-HELD ANSWER — advantage on every attack roll is the largest crit-rate multiplier in the game. ⚠ It does nothing against a Held target, and the save disadvantage taxes the party''s Concentration carrier.'
      - id: opt-killers-sweetheart-act3
        item: Killer's Sweetheart
        tier: A
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (14:36) — very good for builds rolling a lot of damage dice, but only one encounter per day'
        note: 'One guaranteed critical hit after a kill, once per long rest. ⚠ Redundant against a Held target, so bank it only for un-Holdable fights.'
      - id: opt-callous-glow-ring-charles
        item: Callous Glow Ring
        tier: S
        tier_note: 'The BEST RINGS in Baldur''s Gate 3 - Honor Mode Tier List and Guide - Act 2 (4:45) — the number of uses is absurd once the wearer is lit'
        note: '+2 Radiant per hit against ILLUMINATED targets, which would feed another Shockwave. ⚠ It needs light, which fights the darkness plan, and it is currently Gale''s.'
    - id: act3-cloak-charles
      item: Cloak of Protection
      tier: S
      tier_note: 'The COOLEST ITEMS in BG3 - Complete Cloak Tier List and Guide (13:30) — excellent, and someone in the party will almost certainly be wearing it'
      held: 2
      slot: cloaks
      bis: true
      note: 'CARRIED OVER. Flat +1 AC and +1 saves never stops applying, which beats the conditional Act 3 cloaks on a body with save disadvantage. ⚠ Mantle of the Holy Warrior is a trap — Crusader''s Mantle is Concentration.'
    - id: act3-ranged-charles
      item: Vicious Shortbow
      tier: S
      tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (57:48) — +7 on crits works passively, so any melee crit build gets it free'
      slot: ranged weapons
      bis: true
      note: 'ACT-3 RANGED, and he never fires it — Dolor Amarus is a holder passive, so +7 per critical hit rides every melee swing out of a dead slot. ⚠ BHAAL PATH ONLY (Echo of Abazigal, Murder Tribunal); otherwise take the Hellrider Longbow below.'
      options:
      - id: opt-hellriders-longbow-charles
        item: Hellrider Longbow
        tier: S
        tier_note: 'The BEST BOWS in Baldur''s Gate 3 - Honor Mode Tier List and Guide (53:35) — +3 initiative from an unused slot; he would put it in S+ if it existed'
        note: 'THE NON-BHAAL FALLBACK, from Ferg Drogher in Rivington. Passive +3 initiative out of the same dead slot. ⚠ It is Gale''s by default, so take it only on a run where the Vicious Shortbow is unavailable.'
    - id: bhaalist-armour-unlock
      item: Bhaalist Armour
      tier: S
      tier_note: 'ARMOR TIER LIST - Light Armour - Baldur''s Gate 3 Honour Mode Guide - Part 2 (42:20) — piercing vulnerability aura breaks the game; LOCKED BEHIND A STORY EVENT, SOME RUNS ONLY'
      slot: other
      note: 'Sold by the Echo of Abazigal, the same Bhaal-path vendor as the Vicious Shortbow. ⚠ NOT WORN — none of his damage is Piercing and the chest is locked. Beating Orin as Bhaal''s chosen also gives the party A Most Bloody Inheritance at High Hall: crit threshold −2.'
    progression:
    - id: prog-head
      item: 'Head: Haste Helm → Holy Lance Helm → Helm of Balduran'
      slot: head
      note: 'Act 1 Haste Helm (Blighted Village) → Act 2 Holy Lance Helm (Rosymorn Monastery) → Act 3 Helm of Balduran (Ansur). ⚠ The Grymskull Helm is illegal all run — Heavy Armour proficiency.'
    - id: prog-armour
      item: 'Chest: Luminous Armour, all three acts (LOCKED)'
      slot: armour
      note: One chest for the whole run. Radiant Shockwave is the engine, fed by Inquisitor's Might on every hit and by Divine Smite. Forgoes Helldusk Armour; crit immunity comes from the off-hand instead.
    - id: prog-hands
      item: 'Hands: Gloves of the Growling Underdog → Gloves of Battlemage''s Power (LOCKED from Act 2)'
      slot: hands
      note: Act 1 Growling Underdog (Dror Ragzlin) as a stopgap → Gloves of Battlemage's Power (Reithwin Tollhouse) from Act 2, and they never come off.
    - id: prog-feet
      item: 'Boots: Boots of Striding → Helldusk Boots'
      slot: feet
      note: 'A FLEX SLOT ALL RUN. Striding (Minthara) in Acts 1–2 → Helldusk (Wyrm''s Rock) in Act 3; both block Prone, which is what keeps Hold Person up. Stormy Clamour (Omeluum) is the alternative — default to it through Act 1, then to the defensive boot.'
    - id: prog-cloaks
      item: 'Cloak: none available → Cloak of Protection'
      slot: cloaks
      note: Empty through Act 1 — the only Act 1 magical cloak is the Dark Urge Mantle, and that goes to Asterion. Cloak of Protection (Talli) from Act 2 on.
    - id: prog-amulets
      item: 'Amulet: Amulet of Misty Step → Amulet of Greater Health'
      slot: amulets
      note: Acts 1–2 Amulet of Misty Step (Priestess Gut) → Act 3 Amulet of Greater Health (House of Hope Archive), which is what makes the Risky Ring safe on a permanent concentrator.
    - id: prog-ring1
      item: 'Ring 1: Ring of Arcane Synergy → Strange Conduit Ring'
      slot: ring 1
      note: Ring of Arcane Synergy in Act 1 → Strange Conduit Ring locked in from Act 2, because Hold Person makes him a permanent concentrator and the Stone doubles the Psychic rider.
    - id: prog-ring2
      item: 'Ring 2: Strange Conduit Ring → flex (Arcane Synergy / Risky / Killer''s Sweetheart)'
      slot: ring 2
      note: 'Strange Conduit Ring in Act 1 → a real flex from Act 2, decided by whether the target can be Held: Arcane Synergy if it can, Risky Ring if it cannot. The Shadow Blade Ring needs no slot — summon, then unequip.'
    - id: prog-weapons
      item: 'Melee: bound weapon → Phalar Aluve one-handed → 3d8 Shadow Blade'
      slot: weapons
      note: One respec, at the Stone. Phalar Aluve behind a shield carries Act 1 into Act 2; the Stone triggers the swap to a 3d8 Shadow Blade, and Phalar leaves for Bonbon's melee set.
    - id: prog-offhand
      item: 'Off-hand: Shield → Adamantine Shield → Viconia''s Walking Fortress'
      slot: off-hand
      note: A plain Grove shield (the Safeguard Shield is Bonbon's) → the Adamantine Shield from the Forge for crit immunity on the Hold Person carrier → Viconia's Walking Fortress once the Helm of Balduran covers crits.
    - id: prog-ranged
      item: 'Ranged: Dual Hand Crossbows +1 → Vicious Shortbow'
      slot: ranged weapons
      note: 'Acts 1–2 the crossbows exist to launch Darkness Arrows. Act 3 the Vicious Shortbow (Echo of Abazigal, Bhaal path) turns the same dead slot into +7 on every critical hit, and hands the Hellrider Longbow back to Gale.'
    - id: prog-consumables
      item: 'Consumables: Arrows of Darkness, all three acts'
      slot: consumables
      note: 'Arrows of Darkness in all three acts — farmed arrows are the darkness source, because Hold Person owns his Concentration. Auntie Ethel''s Hair takes CHA to 18. Elixirs: Bloodlust on Hold days, Elixir of Heroism when nothing is Holdable.'
  playstyle: |-
    - **The loop:** Inquisitor's Might, Booming Blade to build Acuity, Hold Person on the priority target, then dump smites into a body that auto-crits.
    - **Concentration is Hold Person and nothing else.** Bless, Hex, Divine Favour, Darkness and both smite spells are out. Asterion supplies Bless; darkness comes from farmed arrows. Hunger of Hadar replaces the Hold on non-humanoid fights.
    - **Elixir:** Bloodlust on days with something to Hold, Elixir of Heroism (+1d4 attacks and saves, stacks with Bless) on days without. Skip Armour of Agathys on Heroism days.
    - **Curse the nova target on the set-up turn.** Hexblade's Curse is a bonus action, once per short rest, and it heals Charles for Warlock level + CHA when the target dies.
    - **Act 1 turn order:** pre-cast Shriek from stealth, Inquisitor's Might as the bonus action, Booming Blade, then smite on crits. Hexblade's Curse waits for the next turn; it wants the same bonus action.
    - **One Channel Oath charge per short rest.** Vow of Enmity for a long Act 1 boss fight, Inquisitor's Might otherwise, and always Inquisitor's Might from Act 2.
    - **Divine Sense before Inquisitor's Might against undead and fiends.** Bonus action, short-rest recharge, two turns of advantage — exactly the fights where Hold Person and Command fail.
    - **Cast Aura of Protection once at char 8 and again at char 11.** It is not on by default and the respec removes it. The radius is 3 m, so stay inside it.
    - **Acuity sequencing:** land a Booming Blade or a smite before casting Hold Person, and cast it before the enemy's turn — every hit he takes cuts the duration by 2. Gale Hastes Charles and Bonbon.
    - **Radiant is the debuff engine.** Every point of Radiant fires Luminous Armour's Shockwave, stacking Radiating Orb within 3 m up to -10 to attack rolls. It never orbs allies, but neutrals are fair game.
    - **Darkness placement:** the cloud blocks ranged attacks both ways and Blinds enemies inside it, so stand in it to shut down archers. Devil's Sight lets him keep fighting.
    - **⚠ Darkness is not the accuracy plan.** Advantage needs a target without darkvision and most Act 1-2 enemies have it. Accuracy comes from the Risky Ring in Act 2 and Shadow Blade's own obscured-target advantage.
    - **No fire into Hunger of Hadar.** Gale's Armour of Landfall lays Plant Growth under the zone for a multi-turn no-save lock, and fire burns Plant Growth away. Gale's fire goes at targets outside it.
    - **Shriek is for Gale too:** 1d4 Thunder per damage instance, and Scorching Ray damages 3-7 separate times a cast. From the Stone onward Bonbon activates it before Gale's turn.
    - **Char 9 respec at the Stone:** Warlock 5 / Paladin 4, Alert and Savage Attacker, summon a 3d8 Shadow Blade and keep the Adamantine Shield. Phalar goes to Bonbon. Re-select Oath of Vengeance.
    - **Once per long rest, out of combat:** stand next to Gale for a Twinned Draconic Elemental Weapon off the Drakethroat Glaive. ⚠ Summon the Shadow Blade first — a re-summoned blade comes back unenchanted.
    - **Once per long rest, out of combat:** cast Aid, upcast as high as you can spare. Charles is the party's only source and it costs no Concentration.
    - **Nova:** Hold a humanoid, then spend the largest Divine Smites first. Upcast Hold Person from an L3 pact slot to hold two humanoids, so a mid-turn kill does not waste the rest of the chain.
    - **Defensive reads:** AC 19-20 behind a shield, crit-immune from the Adamantine Shield and later the Helm of Balduran. Pre-cast Mirror Image when he expects to be focused, and keep Shield for the reaction that would break Hold Person.
---
