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
  ability_targets: CHA 17 → 18 (Hag's Hair) → 20 (Mirror of Loss); CON stays 16.
  feats:
  - at: char 6 (Warlock 4)
    feat: Savage Attacker
    note: Rerolls every damage die incl. Divine Smite; ~+16%.
  - at: char 9 (Paladin 4)
    feat: Great Weapon Master
    note: Bonus-attack-on-crit works with any melee weapon incl. Shadow Blade — the 7th swing. The +2 CHA feat was redundant (Hag+Mirror reach 20).
  invocations:
  - Devil's Sight (take FIRST, at Warlock 2 / char 2 — enables the Shadow Blade + Darkness combo)
  - Thirsting Blade (the 3rd attack)
  - Improved Pact Weapon
  weapon_plan: Self-cast Shadow Blade (2d8 from char 3, 3d8 at W5) + shield, run with Devil's Sight/Darkness for advantage → Heavy piercing Pike once Bhaalist Armour drops.
  creation:
    level1_class: Warlock 1 (Hexblade patron)
    level1_gains: Pact Magic (1 × L1 short-rest slot), Hexblade's Curse (bonus action), Bind Hexed Weapon (attack with CHA). Pact Boon (Pact of the Blade) is not until Warlock 3.
    subclass_choice: Hexblade patron (Warlock 1)
    proficiencies:
      armor_weapons: Medium armour + shields + martial (Hexblade, Warlock 1); heavy armour from Paladin.
      saving_throws: WIS + CHA (Warlock).
      skills: 2 Warlock picks + Haunted One (Medicine, Intimidation).
    starting_cantrips: 2 known at Warlock 1 — recommend Eldritch Blast + one filler.
    starting_spells: 2 known from the Warlock list plus the Hexblade L1 expanded adds (Shield, Wrathful Smite).
    notes: 'Charles''s character-creation class is Warlock 1 (Half-Orc Dark Urge). RUSH Warlock 1→2→3 first (Devil''s Sight at char 2, Pact of the Blade + self-cast Shadow Blade at char 3), THEN multiclass Paladin from character level 4 — so Divine Smite lands at char 5 (two levels later than a Paladin-first order). Worth it: early Act 1''s problem is landing attacks with no party control (Hold Person/Monster) online yet, and the Shadow Blade + Devil''s Sight package is a self-contained advantage/defense source from char 3. Oathbreaker and the auras arrive later; the L6–12 tail is unchanged.'
  spells:
    note: 'Charles is a smite platform, not a spell-slinger — most slots are spent as Divine Smite. Concentration is the bottleneck: hold only ONE of Wrathful Smite / Bless / Divine Favour / Shield of Faith at a time. Mandatory = the nova depends on it; Recommended = strong flex / buffs.'
    mandatory:
    - spell: Divine Smite
      level: Feature (Paladin 2)
      school: Class feature — Radiant
      save: None (melee weapon attack roll)
      when: char 5
      why: 'The build''s core. Expend any slot on a melee hit: 2d8 Radiant at L1, +1d8 per slot level above 1st (cap 5d8 at an L4 slot), +1d8 vs Fiends/Undead; dice DOUBLE on a crit. Not a prepared spell and not stopped by Counterspell — set the Critical-Hit Divine Smite reactions to auto-confirm.'
    - spell: Shadow Blade
      level: '2'
      school: Illusion
      save: None (bonus action to summon)
      when: char 3 (Warlock 3)
      why: 'Core early/mid weapon AND the early-game advantage engine: bonus action, NOT concentration, lasts until long rest; 2d8 psychic → 3d8 once Warlock 5 grants L3 pact slots. Bind Hexed/Pact Weapon onto it to attack with CHA. Grants Advantage on melee attacks vs any Lightly/Heavily Obscured target — so it hits at advantage in the abundant dim-light of Act 1, and with Devil''s Sight you fight inside your own Darkness: enemies in it are Blinded (they attack you at disadvantage), while you see fine and attack them at advantage. Verified: bg3.wiki/wiki/Shadow_Blade.'
    - spell: Wrathful Smite
      level: '1'
      school: Evocation
      save: WIS save (to avoid Frightened)
      when: char 1 (Hexblade) / char 5 (Paladin)
      why: 'The one prepared spell in the nova line: +1d6 psychic (doubles to 2d6 on a crit) and can Frighten. Concentration — cast once and it rides subsequent swings.'
    recommended:
    - spell: Hex
      level: '1'
      school: Enchantment
      save: None (rider on each hit)
      when: char 1 (Warlock 1)
      why: +1d6 Necrotic per hit (~+3d6/turn on a 3-attack nova) + disadvantage on a chosen ability. Concentration — better for sustained fights than the one-shot nova (competes with Wrathful Smite).
    - spell: Shield
      level: '1'
      school: Abjuration
      save: None (reaction, +5 AC)
      when: char 1 (Hexblade L1 expanded)
      why: Reaction +5 AC to dodge an incoming hit; not concentration; strong survival pick for a melee body.
    - spell: Armour of Agathys
      level: '1'
      school: Abjuration
      save: None
      when: char 1–6
      why: Temp HP + Cold retaliation that scales with the pact slot — 15 temp HP / 15 Cold from a Warlock-5 L3 pact slot. Not concentration.
    - spell: Bless
      level: '1'
      school: Enchantment
      save: None (concentration)
      when: char 5 (Paladin 2)
      why: +1d4 to attack rolls and saves for up to 3 allies; best pre-fight buff on turns not riding Wrathful Smite.
    - spell: Command
      level: '1'
      school: Enchantment
      save: WIS save
      when: char 5 (Paladin 2)
      why: Cheap single-target control (Drop / Halt / Approach) to open a nova or peel an enemy caster.
    - spell: Hellish Rebuke
      level: '1'
      school: Evocation
      save: DEX save (half on save)
      when: char 8 (Paladin 3, Oathbreaker oath spell)
      why: Free ALWAYS-PREPARED Oathbreaker oath spell; reaction fire damage when hit, at zero prepared-slot cost.
    - spell: Darkness
      level: '2'
      school: Evocation
      save: None
      when: char 3 (learn as a Warlock spell) / char 10 (free Oathbreaker oath spell)
      why: 'Vision-denial bubble Charles fights inside via Devil''s Sight — enemies in it are Blinded (disadvantage to hit him) while he sees fine and keeps advantage; NOT concentration in BG3 (a placed cloud, ~10 turns). Learn it as a Warlock spell from char 3 to run the combo through Act 1–2; it becomes free + always-prepared as an Oathbreaker oath spell at char 10. Collapses vs enemies with their own Devil''s Sight/truesight.'
    - spell: Spiteful Suffering
      level: Channel Oath (not a spell)
      school: Oathbreaker Channel Oath — Necrotic
      save: CHA save
      when: char 8 (Paladin 3)
      why: 1d4+CHA Necrotic/turn AND grants all attackers Advantage on the target — a self-contained advantage/crit-fishing source when the Risky Ring isn't equipped.
    - spell: Eldritch Blast
      level: Cantrip
      school: Evocation
      save: Ranged spell attack
      when: char 1 (Warlock 1)
      why: Ranged fallback for turns he can't reach melee (2 beams at char 5, 3 at char 10); a real option with Agonising Blast + CHA 20.
  leveling:
  - char_level: 2
    class: Warlock 2
    gains: Invocation (Devil's Sight — see normally in magical Darkness)
  - char_level: 3
    class: Warlock 3
    gains: Pact of the Blade + self-cast Shadow Blade (2d8) → advantage engine online (advantage vs dim-light/obscured targets; fight inside Darkness via Devil's Sight)
  - char_level: 4
    class: Paladin 1
    gains: Lay on Hands
  - char_level: 5
    class: Paladin 2
    gains: Divine Smite (nova online)
  - char_level: 6
    class: Warlock 4
    gains: 'Feat: Savage Attacker'
  - char_level: 7
    class: Warlock 5
    gains: Deepened Pact → 2 attacks; Shadow Blade → 3d8
  - char_level: 8
    class: Paladin 3
    gains: Pick any oath, break it → Oathbreaker
  - char_level: 9
    class: Paladin 4
    gains: 'Feat: Great Weapon Master (bonus-attack-on-crit)'
  - char_level: 10
    class: Paladin 5
    gains: Extra Attack stacks → 3 attacks
  - char_level: 11
    class: Paladin 6
    gains: Aura of Protection
  - char_level: 12
    class: Paladin 7
    gains: Aura of Hate
  itemization:
    act1:
    - id: everburn-blade
      item: Everburn Blade
      note: 'Everburn Blade (Nautiloid — Commander Zhalk): 2d6 + 1d4 fire greatsword, the strongest turn-1 weapon; bind it via Hex Warrior to swing off CHA even at STR 8'
    - id: sword-of-justice
      item: Sword of Justice
      note: 'Sword of Justice (Risen Road — Anders/Karlach questline): +1 heavy-armour greatsword that casts Compelled Duel — a solid aggro option before the pact blade'
    - id: blood-of-lathander
      item: Blood of Lathander
      note: 'Blood of Lathander (Rosymorn Monastery puzzle): +3 legendary mace with Sunbeam and a party revive-at-0-HP aura — an excellent one-hander to pair with a shield if you go sword-and-board early'
    - id: adamantine-splint-scale-mail-adamantine-shield
      item: Adamantine Splint/Scale Mail + Adamantine Shield
      note: 'Adamantine Splint/Scale Mail + Adamantine Shield (Grymforge forge): crit-immunity, −damage, and reels attackers — the Act 1–2 defensive backbone for a frontliner'
    - id: phalar-aluve
      item: Phalar Aluve
      note: 'Phalar Aluve (Underdark, in the stone): Shriek adds thunder to every hit on the target and Sing buffs allies — carry it early or hand off'
    - id: caustic-band
      item: Caustic Band
      note: 'Caustic Band (Underdark — Derryth Bonecloak): +2 acid on weapon hits — cheap flat damage while smite slots are scarce'
    - id: auntie-ethel-s-hair-cha-17-18
      item: Auntie Ethel's Hair → CHA 17 → 18
      note: Auntie Ethel's Hair → CHA 17 → 18 (raises Aura DCs, attack/smite accuracy, and prepared-spell count)
    - id: diadem-of-arcane-synergy
      item: Diadem of Arcane Synergy
      note: 'Diadem of Arcane Synergy (Crèche): reallocated from Gale — inflict a condition (Wrathful Smite/Hexblade''s Curse) → +CHA to weapon damage; Act 1–2 head slot before Sarevok''s Helmet'
    - id: strange-conduit-ring
      item: Strange Conduit Ring
      note: 'Strange Conduit Ring (Crèche): +1d4 psychic on attacks while Concentrating (Wrathful Smite/Bless) — doubled by the Resonance Stone and on a crit; competes with the Shadow Blade Ring for a ring slot'
    - id: note
      item: Note
      note: 'Note: Pact of the Blade + self-cast Shadow Blade come online at Warlock 3 (char 5) — a 2d8 psychic one-hander, so you can drop the greatsword for blade-and-shield'
    act2:
    - id: self-cast-shadow-blade-upcast-to-3d8
      item: Self-cast Shadow Blade upcast to 3d8
      note: Self-cast Shadow Blade upcast to 3d8 (Warlock 5, char 7) as the main weapon + a shield (or keep the Adamantine Shield)
    - id: risky-ring
      item: Risky Ring
      note: 'Risky Ring (Moonrise — Araj Oblodra): advantage on ALL attacks (disadvantage on saves) — the crit-fishing engine; keep it behind Aura of Protection to offset the save penalty'
    - id: ring-slot-2
      item: Ring slot 2
      note: 'Ring slot 2 (flex): Strange Conduit Ring (+1d4 psychic while concentrating — feeds the nova) OR Shadow Blade Ring (bonus-action backup blade). Conduit usually wins on nova turns'
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      note: 'Killer''s Sweetheart (Gauntlet of Shar — Self-Same Trial): your first attack after a kill is a GUARANTEED crit → a free doubled smite every fight'
    - id: head-slot
      item: Head slot
      note: 'Head slot: Covert Cowl (Last Light — −1 crit while Obscured) vs the Diadem (+CHA weapon damage). Cowl for crit-fishing in Darkness; Diadem for raw damage. (A 2nd Covert-Critical head — the Dark Justiciar Helmet — lets Asterion run one too.)'
    - id: amulet-heavy-armour
      item: Amulet/heavy armour
      note: 'Amulet/heavy armour: keep the Adamantine set or buy heavy armour from Moonrise vendors until the Helldusk set (Act 3)'
    - id: fight-beside-the-trickster-to-share-its-resonance-stone-aura
      item: Fight beside the Trickster to share its Resonance Stone aura
      note: Fight beside the Trickster to share its Resonance Stone aura (doubles the psychic Shadow Blade)
    act3:
    - id: bhaalist-armour
      item: Bhaalist Armour
      note: Bhaalist Armour (piercing-vuln aura)
    - id: heavy-piercing-pike
      item: Heavy piercing Pike
      note: Heavy piercing Pike (two-handed → enables GWM's -5/+10)
    - id: sarevok-s-horned-helmet
      item: Sarevok's Horned Helmet
      note: Sarevok's Horned Helmet (crit range)
    - id: killer-s-sweetheart
      item: Killer's Sweetheart
      note: Killer's Sweetheart (guaranteed crit after a kill)
    - id: a-defensive-amulet
      item: A defensive amulet
      note: A defensive amulet
    - id: helldusk-gloves
      item: Helldusk Gloves
      note: Helldusk Gloves
  playstyle: |-
    - **Early Act 1 (char 3+):** self-cast Shadow Blade + shield and fight from advantage — Shadow Blade grants advantage vs obscured/dim-light targets, and casting Darkness lets you fight inside it with Devil's Sight (you see, enemies are Blinded → they miss you, you hit at advantage). This is the fix for "missing attacks" before any party control is online; Divine Smite comes online at char 5.
    - **Pre-apply Hexblade's Curse** the turn before so the bonus action is free.
    - **Nova turn:** attack (3) + Haste (3) + GWM bonus attack (1) = 7 auto-crit swings on a Held target, smiting each; short rest to refuel.
    - Half-Orc adds a die on crits; Curse drops the crit threshold to 19–20; Risky Ring keeps you at advantage.
    - **Dark Urge bonus:** A Most Bloody Inheritance (from the Act-3 Murder questline) reduces Charles's crit threshold by a further −2, stacking with Curse (−1) + Sarevok's Helmet + Covert Cowl — a very wide crit range for non-Held targets.
  late_game_config:
    note: At Act 3 you can run either weapon set.
    shadow_blade_set: 3d8 psychic one-hander + shield; ×2 from the Trickster's Resonance Stone (shared, buggy); GWM bonus attack only.
    piercing_set: Heavy piercing Pike (1d10) two-handed; ×2 from your own Bhaalist Armour (always on); GWM bonus attack + All In (-5/+10); no shield.
  nova:
    assumptions: Held target (every hit auto-crits), full 8-slot dump. Smites double their dice on a crit; Half-Orc adds a die; Savage Attacker rerolls every die (d8→5.81, d10→7.15, d6→4.47). Flat weapon bonuses (CHA 5 + Aura of Hate 5 + Improved Pact Weapon 1 + Curse 4 [+ GWM 10 on the pike]) ride the weapon's type so they double; smites are radiant so neither aura doubles them.
    configs:
    - name: Shadow Blade + Resonance Stone (psychic ×2)
      lines:
      - line: Weapon swing — 7d8 + 15, psychic ×2
        count: 7
        each: 111.4
        total: 780
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
      - line: Wrathful Smite — 2d6 psychic ×2
        count: 1
        each: 17.9
        total: 18
      turn_total: 1070
    - name: Pike + Bhaalist (piercing ×2)
      lines:
      - line: Weapon swing — 3d10 + 25 (incl. GWM +10), piercing ×2
        count: 7
        each: 92.9
        total: 650
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
      - line: Wrathful Smite — 2d6 psychic (undoubled)
        count: 1
        each: 8.9
        total: 9
      turn_total: 930
    caveats: 'Shadow Blade + Resonance Stone has the higher ceiling (~1,070) but rides the Trickster''s shared, buggy stone — without it it falls to ~670, so the Pike is better whenever the stone isn''t up. Both figures assume the Savage-Attacker-rerolls-smite quirk (bg3.wiki: ''unknown if bugged/intended'') and that Hexblade''s Curse''s +4 rides the weapon''s type; if Curse is untyped, shave ~28 off each.'
---

