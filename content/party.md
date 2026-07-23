---
roster:
- slot: 1
  nickname: Charles
  class: Oathbreaker Paladin 7 / Hexblade Warlock 5
  role: Melee crit-smite nova
  character: Dark Urge (Half-Orc)
  played_by: Idan
- slot: 2
  nickname: Asterion
  class: Arcane Trickster 11 / 1-dip (War Cleric or Fighter)
  role: Stealth assassin — melee Shadow-Blade or ranged sniper
  character: Astarion
  played_by: Idan
- slot: 3
  nickname: Gale
  class: Storm Sorcerer 10 / Tempest Cleric 2
  role: Wet+Lightning nuke + Haste engine
  character: Gale
  played_by: Alondra
- slot: 4
  nickname: Bonbon
  class: Swords Bard 11 / Fighter 1
  role: Control + damage + face
  character: Bard
  played_by: Alondra
synergies:
- name: Haste engine
  how: Sorcerer Twinned-Hastes the Paladin (Haste is single-target, so Twinnable) → a 4th attack.
- name: Wet → doubled
  how: Sorcerer's Create Water (+ Trickster Mage-Hand water bottles) makes lightning/cold hit double.
- name: Control → auto-crit
  how: Bard's Hold Monster paralyzes a target → melee auto-crits → doubled crit-smites for the Paladin.
- name: Shared psychic
  how: Trickster carries the Resonance Stone up front — doubling both its own and the Paladin's psychic Shadow Blade strikes (melee config).
- name: Auras
  how: Paladin's Aura of Protection (+CHA saves) + Aura of Hate (+CHA melee damage) buff the melee cluster.
combat_gameplan:
  note: |-
    Run **two kill zones**.
    - **Zone 1 (frontline)** — the Bard-Held priority/boss target that Charles and Asterion auto-crit into oblivion (psychic/piercing — keep water OUT of it).
    - **Zone 2 (backline adds)** — the cluster Gale Wets and detonates with maximized, doubled lightning/cold plus Asterion's disadvantaged cold scrolls — physically separated so Electrified Water never touches the melee.

    **Two sequencing linchpins:**
    - **Initiative** — the R1 chain assumes Bard acts before Sorcerer before Charles, and BG3 has NO delay-turn, so on bad rolls the nova simply slips to R2.
    - **Bonus-action conflict** — Charles's R1 Hexblade's Curse vs GWM attack forces the true 7-swing turn to R2.

    In **Act 3** treat the Resonance-Stone psychic-×2 as unreliable (known post-Act-2 bug) and default Charles to the self-contained Pike + Bhaalist set.
  per_character:
  - character: Bonbon (Bard) — the initiator
    role: 'Arcane-Acuity control engine: locks the priority target with Hold Monster so the melee auto-crits, then escalates to mass Command.'
    priority_actions: |-
      Wants to act **FIRST** (Hellrider's Longbow initiative).
      - R1: ranged Slashing Flourish (2 hits) on the priority target → ~+4 Arcane Acuity (raises spell save DC THAT turn) and arms the Band of the Mystic Scoundrel → bonus-action Hold Monster at the boosted DC → Paralyzed (hold concentration).
      - R2: Flourish again (Acuity climbs) → Hold Monster/Command on the next target.
      - R3: Acuity near +10 → Command 'Drop'/'Prone' on up to 6 via the Bard-11 L6 slot, or Fear/Confusion; Counterspell the enemy caster; hand out Bardic Inspiration.
    avoid: |-
      - **Never** fire the control spell BEFORE a weapon hit lands that turn (both the Band bonus-cast AND the fresh Acuity need the Flourish to resolve first).
      - Stay ranged/unhit: Acuity decays −2 per hit taken, and losing Bard concentration (or letting the Held target die early) drops the melee's auto-crit.
  - character: Gale (Sorcerer) — the engine + AoE
    role: Party Haste engine plus a Wet + maximized-Lightning AoE aimed at the SECONDARY cluster (kept off the frontline).
    priority_actions: |-
      - R1: action = Twinned Haste on Charles + Asterion (the extra Action fuels Charles's 6–7 swings, plus +2 AC and DEX-save advantage on both); bonus = Quickened Create Water on a separate add cluster (or let Asterion's Mage Hand do the Wet). Now locked concentrating on Haste.
      - R2+: Haste persists for free → detonate: Destructive Wrath (maximize) + Markoheshkir-empowered Lightning Bolt/Chain Lightning (or Cone of Cold) on the Wet cluster — Wet doubles it and already negates any lightning resistance, lightning-on-water Shocks them. Save the 2nd Destructive Wrath (Amulet of the Devout) for a second cluster; hold Counterspell.
    avoid: |-
      - **Electrified-water friendly fire** — never Wet the ground Charles/Asterion stand on and never arc lightning into the melee's water (recurring lightning + prone; a Wet ally takes DOUBLE enemy lightning/cold).
      - Keep the water/lightning cluster physically separate, and guard Haste concentration (War Caster) — if it breaks, Charles and Asterion go Lethargic and lose their next turn.
  - character: Charles (Paladin) — the finisher
    role: Melee crit-smite nova — the single-target finisher that deletes the Bard-Held priority target.
    priority_actions: |-
      - Pre-fight: bind Shadow Blade/Pike and short-rest to refund the pact slot; position so Aura of Protection (+CHA saves) and Aura of Hate (+CHA melee damage) blanket the melee cluster and the Resonance-Stone carrier.
      - R1: bonus = Hexblade's Curse on the Paralyzed target; action (3) + Haste action (3) = 6 auto-crit strikes, Divine Smite the biggest slots first (doubled on the crit; psychic doubled again by the stone), Half-Orc extra die, Savage Attacker rerolls → ~800–1000 on a Held target.
      - R2+ (Curse up, bonus free): full 7 swings incl. the GWM bonus-attack-on-crit; use Killer's Sweetheart's guaranteed crit after a kill; when smites dry up, plain Hasted swings.
    avoid: |-
      - Do not stand in the Sorcerer's water (electrify + Wet doubles enemy lightning/cold on you).
      - On R1 do **NOT** spend the bonus action on the GWM attack instead of Hexblade's Curse — Curse can't be pre-cast before initiative, and its +damage rider is what the doubled-nova math depends on (the GWM swing only comes online R2 once Curse is already up).
  - character: Asterion (Rogue, Config A) — the assassin
    role: 'Stealth assassin / DEX-save nuker: one massive ambush strike on the Held target, plus ownership of the Wet-and-cold AoE lane and the free water-bottle setup.'
    priority_actions: |-
      - Pre-fight: pre-cast 3d8 Shadow Blade (Superior Elixir, no concentration); place the Resonance Stone by the melee cluster inside Charles's Aura; start Hidden; invisible Mage Hand throws water bottles to pre-Wet the enemy cluster.
      - Each turn: bonus = Hide (Reliable Talent → near-automatic; arms Magical Ambush AND Sneak-Attack advantage), action = Booming Blade + Shadow Blade + Sneak Attack 6d6 as ONE strike — auto-crit on the Held target, whole strike doubled psychic by the stone.
      - On a kill, Deathstalker Mantle turns him Invisible → reposition + re-ambush.
      - When Charles already covers the melee target, crouch-cast a stolen cold scroll (Ice Storm / Cone of Cold) into the Wet cluster at disadvantage (Magical Ambush).
    avoid: |-
      - Don't linger in melee after the alpha strike — he's squishy (lean on Cunning Action Disengage/Hide, Misty Step, Uncanny Dodge + Evasion + Shield).
      - He sits INSIDE his own Resonance Stone aura with no Gnome Cunning: vs psychic/mind enemies the stone gives HIM psychic vulnerability + disadvantage on mental saves, so keep him in Charles's Aura of Protection — or don't deploy the stone that fight.
  opening_rotation:
  - step: 1
    who: All — pre-combat setup
    action: 'Long-rest buffs: Charles and Asterion each pre-cast 3d8 Shadow Blade via a Superior Elixir of Arcane Cultivation (no concentration); Charles binds his Pact weapon and short-rests to refund the slot. Asterion goes Hidden and places the Resonance Stone where the melee will cluster (inside Charles''s planned Aura, away from psychic-save-fragile allies); his invisible Mage Hand throws water bottles to pre-Wet the add cluster. Open from stealth for a surprise round.'
  - step: 2
    who: Bonbon (Bard) — R1, first
    action: Ranged Slashing Flourish (2 hits) on the boss → ~+4 Arcane Acuity (raises spell save DC this turn) and arms the Band of the Mystic Scoundrel → bonus-action Hold Monster → boss fails its WIS save → Paralyzed. Hold concentration on the lock.
  - step: 3
    who: Gale (Sorcerer) — R1
    action: Action = Twinned Haste on Charles + Asterion (extra Action + +2 AC / DEX-save advantage). Bonus = Quickened Create Water on a SEPARATE add cluster, not under the melee. Sorcerer now locked concentrating on Haste; boss Held, adds Wet for next round.
  - step: 4
    who: Charles (Paladin) — R1
    action: Bonus = Hexblade's Curse on the Paralyzed boss. Action (3) + Haste action (3) = 6 auto-crit Shadow Blade strikes; Divine Smite the top slots first (doubled on the crit, psychic doubled again by the stone), Half-Orc die, Savage Attacker rerolls. Boss deleted or near-dead (~800–1000). No GWM bonus attack this round — the bonus was spent on Curse.
  - step: 5
    who: Asterion (Rogue) — R1
    action: Bonus = Hide (near-automatic). Action = Booming Blade + Shadow Blade + Sneak Attack 6d6 as one strike on the boss (auto-crit while Held, doubled psychic by the stone) → finishes it. The kill triggers the Deathstalker Mantle → Asterion turns Invisible.
  - step: 6
    who: Enemies — R1
    action: 'If you surprised them, they skip this round. Otherwise they act with the alpha target already dead/locked: Asterion is Invisible, Charles soaks behind +2 AC from Haste, everyone in the aura has +CHA to saves.'
  - step: 7
    who: Bonbon (Bard) — R2
    action: Slashing Flourish on the next priority target (Acuity now ~+6 to +8, control near-unresistable) → bonus-action Hold Monster on it; drop concentration on the dead boss. New target Paralyzed.
  - step: 8
    who: Gale (Sorcerer) — R2
    action: 'Haste persists for free → action open to nuke: Destructive Wrath (maximize) + Markoheshkir Lightning Bolt/Chain Lightning (or Cone of Cold) on the Wet add cluster — doubled by Wet (which also negates any lightning resist), lightning-on-water Shocks them. Keep the blast clear of the melee.'
  - step: 9
    who: Charles (Paladin) — R2
    action: Move to the new Held target. Full 7 swings now — Curse already up, so the bonus is free for the GWM bonus-attack-on-crit. Smite with remaining slots; once dry, plain Hasted swings. Killer's Sweetheart guarantees a crit on the first hit after a kill.
  - step: 10
    who: Asterion (Rogue) — R2
    action: Still Invisible from the R1 kill → open with the big Booming-Blade/Shadow-Blade/Sneak strike on the new Held target (auto-crit), OR crouch-cast a stolen Ice Storm/Cone of Cold into the Wet cluster at disadvantage (Magical Ambush). Mage Hand re-Wets a fresh target or flanks to guarantee Sneak Attack. Then Hide/Disengage out.
  - step: 11
    who: Bonbon (Bard) — R3
    action: Acuity at/near +10 → Command ('Drop'/'Prone') on up to 6 enemies via the Bard-11 L6 slot, or Fear/Confusion to mass-lock the rest. Counterspell the enemy caster; hand out Bardic Inspiration.
  - step: 12
    who: Gale (Sorcerer) — R3
    action: Second Destructive Wrath (Amulet of the Devout) on the next Wet cluster, or Counterspell / Quickened Lightning Bolt on stragglers. Haste stays concentrated on the melee pair.
  - step: 13
    who: Charles + Asterion — R3
    action: Clean up the controlled/prone enemies (advantage everywhere, guaranteed crits on any still Held). Charles falls back to plain swings / Lay on Hands once out of smites; Asterion hit-and-runs — kill a low target to re-proc Deathstalker invisibility, reposition, ambush again. Short-rest after the fight to refuel Charles's spell + pact slots.
item_allocation:
- item: Risky Ring (always-advantage)
  to: Paladin
  why: Oathbreaker has no advantage source; crit-fishing needs it.
- item: Shadow Blade Ring
  to: Paladin
  why: Backup blade (the Trickster self-casts its own 3d8).
- item: Resonance Stone (AoE psychic ×2)
  to: Trickster (melee config) or Paladin (if Trickster goes ranged)
  why: Doubles psychic for the carrier and nearby psychic Shadow Blades; a backline ranged Trickster can't keep the aura on the frontline, so hand it off.
- item: Amulet of Greater Health
  to: Bard (Bonbon)
  why: 'REALLOCATED from the Trickster to the Bard: CON 23 + CON-save advantage armours Hold Monster concentration (the melee auto-crit engine) with NO neck conflict (the Bard''s neck was free), while Gale keeps the Amulet of the Devout for the 2nd Destructive Wrath. Stacks with the Bard''s new War Caster feat. Asterion keeps Uncanny Dodge + Evasion + Shield, so CON isn''t his bottleneck.'
- item: Knife of the Undermountain King
  to: Trickster
  why: Crit 19–20; early main-hand until Shadow Blade.
- item: Deathstalker Mantle
  to: Trickster
  why: Invisible on kill — the assassin's reposition/re-ambush cloak; stands in for a Duergar/Deep-Gnome innate invisibility since the char is Astarion.
- item: Helmet of Arcane Acuity
  to: Bard
  why: Its whole control engine.
- item: Hellrider's Longbow
  to: Bard
  why: '+initiative bow option; Bonbon otherwise runs Titanstring (Act 1) → dual hand crossbows (Act 2+, the Acuity engine).'
- item: Markoheshkir
  to: Sorcerer
  why: Lightning empower (Kereska's Favour).
- item: Amulet of the Devout
  to: Sorcerer
  why: Spell DC + extra Destructive Wrath charge.
progression:
- act: 1
  paladin: Shadow Blade + Devil's Sight (char 3) → Divine Smite (char 5)
  trickster: Expertise, Mage Hand, Shield, Disguise; Knife main-hand; steals
  sorcerer: Straight Storm Sorcery
  bard: Face + Song of Rest + inspiration
- act: 2
  paladin: W5 → 2 attacks + 3d8 blade; Risky Ring
  trickster: Shadow Blade + Magical Ambush + Evasion; Deathstalker Mantle; Eversight 'Asterion' combo
  sorcerer: 'Tempest dip: Wet + maximize'
  bard: Helmet of Arcane Acuity → control online
- act: 3
  paladin: Bhaalist → piercing Pike + crit gear; 3 attacks (7 on a nova)
  trickster: Reliable Talent; carries Resonance Stone; scroll arsenal + Ne'er Misser backup
  sorcerer: Markoheshkir
  bard: Band of the Mystic Scoundrel → full control loop
watch_outs:
- watch_out: Charisma overload
  detail: Paladin/Warlock/Sorc/Bard are all CHA; lean on the Trickster (Expertise + Perception/Investigation) for the DEX/INT/WIS skills.
- watch_out: Resonance Stone debuff
  detail: Its aura makes the whole party (incl. its Astarion carrier — no Gnome Cunning) psychic-vulnerable + disadvantage on mental saves; cluster it near the Paladin's Aura of Protection and keep it off save-fragile allies vs psychic/mind enemies.
- watch_out: Deepened Pact (non-Honour)
  detail: The 3-attack stack works only outside Honour mode; don't drop Warlock below 5.
- watch_out: Undead / crit-immune bosses break the nova (no respec needed)
  detail: |-
    Hold Monster & Command have NO effect on undead, the Resonance Stone excludes undead + constructs, and crit-immunity gear cancels auto-crits — so **both melee multipliers die** vs Ketheric (Act 2), Cazador, the Steel Watchers, and the Netherbrain.

    Fallback (all tactical, no respec):
    - **Bonbon** swaps to Hypnotic Pattern / Slow (work on undead) instead of Hold Monster, and keeps Healing Word for emergencies.
    - **Charles** drops the Resonance Stone and leans on Risky-Ring advantage + Spiteful Suffering for crit-fishing — his Divine Smite already deals +1d8 vs Undead/Fiends, so radiant smites are actually STRONG here.
    - **Gale/Asterion** are unaffected (lightning/force work on undead).

    Treat the Hold→auto-crit→Stone nova as an **anti-LIVING-boss package**.
skills_face:
- duty: Face (Persuasion / Deception / Intimidation)
  who: Bard (Expertise + Friends)
- duty: Sleight of Hand / Stealth
  who: Trickster (Expertise)
- duty: Investigation / Arcana
  who: Trickster (Expertise + Perception)
- duty: Athletics (chasm throws)
  who: Trickster (Expertise)
- duty: Perception / Medicine
  who: Split across the party
---

