# Illithid / Zaith'isk rework plan — 2026-09-14 (for review)

Status: proposal. Nothing in `content/` has been changed. Approve, amend, or reject per
section; §9 lists the edits that implement it.

Basis: `docs/zaithisk-awakened-review-2026-09-14.md` (placement decision and the
power-by-power audit), the Cephalopocalypse illithid tier lists Part 1 (`9af1gYSpXK4`)
and Part 2 (`rpVrXn3Rl7k`, summary in `resources/videos/summaries/`), and bg3.wiki.
Non-Honour, Patch 8. Ratings quoted are the corpus's and assume Awakened.

## 1. What changes

| | Today (`content/tadpole.md`) | Proposed |
|---|---|---|
| Awakened (Zaith'isk) | Bonbon | **Gale** |
| Every-turn bonus-action power | none (Bonbon's three are once per long rest and fight the Band) | Gale: Black Hole ×6 per short rest, Stage Fright, Force Tunnel, Shield of Thralls recast; Stakes, Mind Sanctuary per long rest |
| Perilous Stakes | Bonbon, bonus action | Gale, bonus action at DC 27 |
| Mind Blast | Bonbon, bonus action | Bonbon, Action cast (one Flourish) |
| Mind Sanctuary | Bonbon | Gale (Freecast is its gate), after an in-game test |
| Ability Drain | Charles, Asterion | + Bonbon |
| Cull the Weak | Asterion, Gale optional | Asterion, Bonbon, Gale; Charles optional |
| Psionic Backlash | nobody | Bonbon, Asterion |
| Luck of the Far Realms | Charles; Asterion and Bonbon optional | all three, core |
| Psionic Overload | Charles and Asterion pre-cast | Asterion only; Charles never presses it; Bonbon situational |
| Stage Fright | Gale, Act 3, Action | Gale, Act 2, bonus action |
| Specimen estimate | "roughly two dozen" | ~40 on a Grove-saving run (§6) |

Unchanged: all four commune, never eat. Gale's Freecast and Psionic Dominance. The
Resonance Stone on Asterion. Charles's Shield of Thralls. Skips of Fracture Psyche,
Repulsor, Absorb Intellect, Survival Instinct.

## 2. Principles

1. **Passives, toggles and reactions cost nothing.** Every S/A one goes to every
   character who can trigger it: Favourable Beginnings, Ability Drain, Luck, Cull the
   Weak, Psionic Backlash, Freecast, Psionic Dominance.
2. **Action-cost powers go to the one character whose bonus action is empty and whose
   Action is expensive.** That is Gale (§3 of the review: about one Quickened ray per
   fight, never Hasted). Awakened is mandatory, so it must sit where nothing else wants
   the bonus action.
3. **Save-based powers ride Arcane Acuity.** Gale and Bonbon reach DC 27; Charles ~19–21;
   Asterion 17. Save powers belong to the first two.
4. **Self-damage never touches a concentration lane.** Psionic Overload, Transfuse
   Health and Concentrated Blast are gates, not buttons, on Charles, Gale and Bonbon.
5. **Inner-ring spends are loans.** Communing refunds them, so pre-transform buys are
   limited to what helps in Acts 1–2 plus the gates for middle-ring powers.

## 3. The Zaith'isk: procedure for Gale

- When: Crèche Y'llek, Act 1, before the Inquisitor. Talk to Ghustil Stornugoss, then
  keep her alive until the machine has been used. One use per game; it is destroyed
  afterwards.
- Party: Lae'zel out. If she is present and becomes the speaker she sits and
  auto-fails. Charles and Bonbon stand well back so Gale is the active speaker when the
  dialogue opens (a companion sits only when the avatars are out of range).
- Gear: Helmet of Autonomy (skeleton at the Festering Cove entrance, Underdark) for
  WIS save proficiency (verified, bg3.wiki). Ring of Protection, already his in Act 1,
  is +1 to every save. Elixir of Heroism is +1d4 to saves for the sitting. Bonbon's
  Safeguard Shield is another +1 if handed over for the dialogue; proficiency does not
  matter for a saving throw.
- Saves: DC 12 INT (Gale INT 8, ~40%), DC 15 WIS (WIS 10, proficiency from the helmet,
  ~45%), DC 18 third save whose stat depends on class (Sorcerer has CON proficiency;
  ~40% if it is CON). Quicksave before sitting and reload on any failure: Awakened
  needs all three. A failed save is only −2 to that stat and any specimen spent
  afterwards removes it, so a slip is cheap, but the passive is the point.
- Loot the three specimens next to the machine.
- Confirm in the character sheet that Gale's illithid powers show Bonus Action.

## 4. Power sets (maps to `tadpole.md` `characters[].powers`)

Tier is the corpus letter. Cost is permanent specimens (inner ring = refunded, 0).

### Gale — Awakened, DC 27 from the Hat of Fire Acuity (Act 2)

| Power | Ring | Gate | When | Cost | Use |
|---|---|---|---|---|---|
| Transfuse Health | inner | — | Act 1 | 0 | gate only, never press |
| Perilous Stakes | middle | Transfuse | Act 1, first two specimens | 1 | bonus action, long rest. Boss on turn 2 after Scorching Ray caps Acuity. INT save. "Instantly win any boss fight" below Honour. |
| Psionic Overload | inner | — | Act 2 | 0 | gate only, never press |
| Stage Fright | middle | Overload | Act 2, with the Hat | 1 | bonus action, short rest. Enemies-only disadvantage on attacks for 3 turns, 2d6 psychic per miss. Haste insurance. |
| Shield of Thralls | middle | Transfuse | Act 2 | 1 | pre-cast on himself out of combat; in combat a bonus action recast on Charles once per short rest (Agathys must be down). Freecast gate. |
| Force Tunnel | inner | — | free on communing | 0 | bonus action, short rest. No-save 4 m push line, allies unaffected. |
| Charm | middle | Favourable Beginnings (free) | Act 3 | 1 | gate for Dominance; reaction with an unreliable save |
| Psionic Dominance | elite | Charm | Act 3 | 1 | reaction, long rest. Free Counterspell for spells of level ≤ 4. |
| Black Hole | elite | Dominance | Act 3 | 1 | bonus action, short rest + 5 recasts. Every turn. Pull to the Held target or the Shriek aura; DC 27 Slow. |
| Freecast | elite | Shield of Thralls | Act 3 | 1 | toggle, long rest. Free Twinned Haste turn 1 of the hardest fight. No ranged-weapon swap; an ally's Guidance or Aura resets it. |
| Cull the Weak | middle | Concentrated Blast (free) | Act 3 | 1 | toggle. Rays execute anything under his power count. |
| Mind Sanctuary | elite | Freecast | Act 3, optional | 1 | bonus action, long rest. Test first (§8). Non-Honour: allies within 3 m swap Action and bonus action once per turn for 3 turns; stacks with Haste. |
| Displacer Beast Shape | elite | Stage Fright | Act 3, optional | 1 | bonus action, long rest. 85 HP body for after Haste is already lost; loses spells while shaped. |

Never press: Concentrated Blast (ends his concentration), Psionic Overload, Transfuse
Health (self-damage: Haste save and −2 Acuity). Never buy: Ability Drain (drains his own
CHA-based spell attacks), Mind Blast (cone hits allies; he has the AoE already),
Fracture Psyche, Absorb Intellect.

Bonus-action priority each turn (Act 3): T1 Black Hole (Twinned Haste is the Action).
T2 Perilous Stakes on the boss, or Stage Fright when many attackers threaten Haste.
T3+ Black Hole recast; Force Tunnel when melee reaches him or the Held target; Shield of
Thralls on Charles when his Agathys is gone. Quickened Scorching Ray only when SP
exceed the next fight's Haste cost.

### Bonbon — Band of the Mystic Scoundrel, DC 27 from the Helmet of Arcane Acuity

| Power | Ring | Gate | When | Cost | Use |
|---|---|---|---|---|---|
| Favourable Beginnings | inner | — | Act 1 | 0 | passive. First check per NPC, first arrow per enemy; Flourish applies it to both arrows. |
| Psionic Overload | inner | — | Act 1–2 | 0 | Ability Drain gate. Press only in fights where she holds no Hold (Action cost = one Flourish; +1d4 on 4–8 arrows a turn). |
| Ability Drain | middle | Overload | Act 1–2 | 1 | passive. Every turn her first hit drains DEX: enemy AC drops for the whole party. Counts as a condition. |
| Luck of the Far Realms | middle | Favourable Beginnings | Act 1–2 | 1 | reaction, long rest. Turn a Flourish hit into a crit. No crit-range gear, so it never fires early. |
| Concentrated Blast | inner | — | Act 2 | 0 | gate only, never press |
| Cull the Weak | middle | Concentrated Blast | Act 2 | 1 | toggle. The most execution checks in the party; nothing of hers keys off kills. |
| Psionic Backlash | middle | Concentrated Blast | Act 2 | 1 | reaction. Psychic damage to a nearby caster when it casts; she has no other reaction. |
| Mind Blast | elite | — | Act 3, first buy | 1 | **Action** cast, long rest. 14 m cone, 4d8 + CHA psychic, INT save or Stunned at DC 27. Costs one Flourish; take it when the cone beats two arrows. Check the line of fire: it hits allies. |
| Shield of Thralls | middle | Transfuse (free) | Act 3 | 1 | Freecast gate; 10 temp HP pre-cast on herself |
| Freecast | elite | Shield of Thralls | Act 3 | 1 | toggle, long rest. Free L6 Command or Hold Monster. No Titanstring / Dead Shot swap that turn. |
| Illithid Expertise | elite | Luck | Act 3, optional | 1 | passive. Redundant as a face upgrade; Part 2 notes a respec then refunds the Bard Expertise on those skills, so her four picks could move to Sleight of Hand, Perception, Insight, Athletics. |

Dropped from her list: Perilous Stakes (Gale), Mind Sanctuary (Gale). Rule that stays:
Flourish then Band every turn; an illithid Action only when it wins the fight.

### Asterion — Resonance Stone, DC 17 (WIS)

| Power | Ring | Gate | When | Cost | Use |
|---|---|---|---|---|---|
| Psionic Overload | inner | — | Act 1, first | 0 | MARQUEE. +1d4 psychic on every punch, doubled by the Stone. Cast in combat: the Action (two attacks) or, if it proves castable, out of combat (§8). |
| Favourable Beginnings | inner | — | Act 1 | 0 | passive; Luck gate |
| Ability Drain | middle | Overload | Act 1–2 | 1 | passive. He attacks first and most; drains STR/DEX once a turn. |
| Luck of the Far Realms | middle | Favourable Beginnings | Act 1–2 | 1 | reaction, long rest. "S tier on rogues" (Part 1 @ 29:03); no crit-range gear so it fires when chosen. Cannot rescue a missed Stunning Strike. |
| Concentrated Blast | inner | — | Act 2 | 0 | gate only |
| Cull the Weak | middle | Concentrated Blast | Act 2 | 1 | toggle. 4–6 strikes a turn = the most checks after Bonbon. Mutually exclusive with Non-Lethal Attacks. |
| Psionic Backlash | middle | Concentrated Blast | Act 2 | 1 | reaction. Deflect Missiles is his only other reaction. |
| Displace | middle | Force Tunnel (free) | Act 3 | 1 | Black Hole gate |
| Black Hole | elite | Displace | Act 3 | 1 | **Action** on turn 1 (Alert): the no-save pull before anyone moves, both bonus actions kept for Flurries. Keep while specimens allow; Gale's recasts cover later turns. |

Not Awakened. The Stone makes him psychic-vulnerable too (Amulet of the Harpers rule
stands).

### Charles — DC 17 + Battlemage Acuity

| Power | Ring | Gate | When | Cost | Use |
|---|---|---|---|---|---|
| Favourable Beginnings | inner | — | Act 1 | 0 | passive; Luck gate |
| Luck of the Far Realms | middle | Favourable Beginnings | Act 1, first buy | 1 | reaction, long rest. The emergency crit when Hold fails. Not on a Held target; his crit-range gear can make it fire early. |
| Psionic Overload | inner | — | Act 1–2 | 0 | **gate only, never press.** 1d4 a turn forces Hold Person saves at Risky Ring disadvantage and strips 2 Acuity a tick. |
| Ability Drain | middle | Overload | Act 1–2 | 1 | passive. STR drain from every first hit. |
| Shield of Thralls | middle | Transfuse (free) | Act 3 | 1 | Action out of combat, pre-cast on himself. Bursts into a DC 15 INT stun in 3 m when the temp HP break. Replaces Armour of Agathys. |
| Cull the Weak | middle | Concentrated Blast (free) | Act 3, optional | 1 | toggle. OFF when the Deathstalker Mantle needs the killing blow. |

Skips stand: Mind Blast, Black Hole, Psionic Backlash (Counterspell and Luck already
use his reaction).

## 5. Where every strong power lands

| Corpus tier | Power | Carrier(s) |
|---|---|---|
| S | Favourable Beginnings | all four |
| S | Psionic Overload | Asterion; Bonbon when not concentrating |
| S | Cull the Weak | Asterion, Bonbon, Gale; Charles optional |
| S | Shield of Thralls | Charles (self), Gale (bonus-action recast), Bonbon (gate) |
| S | Black Hole | Gale every turn; Asterion turn 1 |
| S | Illithid Expertise | Bonbon optional (skill re-spend) |
| S | Fly | all four |
| A | Ability Drain | Charles, Asterion, Bonbon |
| A | Luck of the Far Realms | Charles, Asterion, Bonbon |
| A | Psionic Backlash | Bonbon, Asterion |
| A | Mind Blast | Bonbon |
| A | Freecast | Gale, Bonbon |
| A | Psionic Dominance | Gale |
| non-Honour standout | Perilous Stakes | Gale |

Nothing rated S or A is unused except Illithid Expertise, which duplicates Bonbon's Bard
Expertise. Every Action-cost power in play sits on the one Awakened character except
Mind Blast (Bonbon, one Flourish) and Asterion's turn-1 Black Hole.

## 6. Specimen schedule

Supply on a Grove-saving run, from the wiki's locations list (bg3.wiki/wiki/Illithid_powers):

| Act | Fixed pickups | Looted from infected NPCs | Approx. total |
|---|---|---|---|
| 1 | Enclave Library 1, Crèche infirmary 3 | Edowin, Gut, Dror Ragzlin, Minthara, Flind, Nere | ~10 |
| 2 | Zhentarim crate at Moonrise docks 2, Colony brine pool 1 (DC 16 Perception) | Marcus, Z'rell, Linsella, Malik, Krizt, Merim, windmill mind flayer, Moonrise cultists | ~10–14 |
| 3 | Rivington barrel 1, ship storage 2, Wyrm's Rock chest 1, Sorcerous Sundries 1, Blushing Mermaid 1, Iron Throne 1, Lodge 1, Crimson Draughts 1, Counting House vault 6 1, Foundry lab 1, cargo ship east of the Foundry 6, Feed the Mind Flayer 1 | — | 18–19 |

Plus ~10 inner-ring refunds on communing. `tadpole.md:25`'s "roughly two dozen" is
low by about fifteen.

Buy order (running total is the demand, supply in brackets):

| Step | Act | Who | Buys | Running demand |
|---|---|---|---|---|
| 1 | 1, after the Dream Visitor | Charles | Favourable Beginnings → Luck | 2 |
| 2 | 1 | Asterion | Psionic Overload | 3 |
| 3 | 1 | Bonbon | Favourable Beginnings | 4 |
| 4 | 1, Crèche | Gale | Transfuse Health → Perilous Stakes | 6 [~9 obtainable before the Crèche: library, infirmary, Edowin, Gut, Ragzlin, Minthara, Flind] |
| 5 | 1, late | Gale sits in the Zaith'isk; Asterion Favourable Beginnings; Bonbon Overload → Ability Drain | 9 |
| 6 | 1 late / 2 early | Asterion Ability Drain, Luck; Charles Overload (gate) → Ability Drain | 13 [Act 1 ends ~10] |
| 7 | 2, Hat on | Gale Psionic Overload (gate) → Stage Fright; Shield of Thralls | 16 |
| 8 | 2 | Bonbon Luck; Concentrated Blast → Cull, Backlash | 20 |
| 9 | 2 | Asterion Concentrated Blast → Cull, Backlash | 23 [Acts 1–2 supply ~20–24; defer Cull/Backlash pairs to Act 3 if short, their gates refund anyway] |
| 10 | 3 start | all four commune; ~10 refunds | 13 net |
| 11 | 3 | Gale Charm → Dominance → Black Hole; Freecast | 17 |
| 12 | 3 | Bonbon Mind Blast; Shield of Thralls → Freecast | 20 |
| 13 | 3 | Asterion Displace → Black Hole; Charles Shield of Thralls | 23 |
| 14 | 3 | Gale Cull, Mind Sanctuary (after test), Displacer; Bonbon Illithid Expertise; Charles Cull | 28 [Act 3 supply 18–19 + refunds] |

Running demand counts gates, which refund at step 10. Permanent demand is 23 through
step 13 and 28 with step 14. Fixed pickups (25) plus refunds (~10) cover everything
through step 13 without a single looted specimen; step 14 comes out of the loots.

## 7. Combat scripts (what changes at the table)

- **Gale**: T1 Twinned Haste + Black Hole. T2 Scorching Ray + Stakes (boss) or Stage
  Fright (mob). T3+ Ray/Fireball + Black Hole recast. Dominance is his Counterspell
  when a big spell targets him. Freecast toggled on before the first Haste of the
  hardest fight of the day.
- **Bonbon**: unchanged loop. Mind Blast replaces one Flourish when a DC 27 cone stun
  beats two arrows (turn 1 into a pack, from the back line). Press Overload in
  no-concentration fights. Luck on the biggest Flourish projectile. Cull and Ability
  Drain run themselves.
- **Asterion**: turn 1 Action Black Hole when the pack is scattered, else Overload; then
  Flurry, Flurry. Luck when a Stunning Strike hit needs to be a crit.
- **Charles**: pre-cast Shield of Thralls instead of Agathys. Luck when Hold fails and a
  hit lands. Nothing else changes; his bonus actions stay Curse and Might.
- **Party**: the Stakes target is the Hold target. Gale's Black Hole point is the Held
  target's feet so Shriek, Radiant Shockwave and Fireball share a cluster. Mind
  Sanctuary, if it passes the test, goes down on Charles and Asterion the turn before
  the nova (Charles's idle bonus action becomes a second Attack action).

## 8. Verify in game before finalising

1. Gale, a companion, can be the Zaith'isk speaker with both avatars parked away.
2. After Awakened, Black Hole's recasts show as bonus actions.
3. Psionic Overload out of combat: Part 1 @ 5:40 says it cannot be cast; the wiki says
   the buff lasts "10 turns or until the end of combat". Decides Asterion's row.
4. Mind Sanctuary non-Honour: does the Action/bonus swap work, and does Charles get a
   full second Attack action from it? Decides Gale's optional row.
5. The third Zaith'isk save's stat for a Sorcerer.
6. Cull the Weak's kills do not trigger the Deathstalker Mantle (Charles's optional row).

## 9. Content edits that implement this

- `content/tadpole.md`
  - `mechanics`: rewrite "Awakened (Zaith'isk, Act 1) → give to BONBON" to Gale, with
    §3's logistics; rewrite "Parasite economy" with §6's counts; fix "Bonbon's
    crossbows" in Watch-outs; fix Asterion's DC to 17.
  - `order`: step 2 `who: Gale`; step 3 drop Charles from Psionic Overload (Asterion
    only, cast in combat); step 5 becomes Gale's Transfuse → Stakes; add Act 1–2 steps
    for Ability Drain / Luck on all three attackers and Cull + Backlash on Bonbon and
    Asterion; step 7 (Bonbon) becomes Mind Blast + Freecast path, Action cast; step 10
    (Gale) adds Stakes PRE, Stage Fright PRE, Mind Sanctuary optional.
  - `characters[]`: replace each `powers` list with §4's tables; Gale's `short`, `dc`
    and `note` to the Awakened controller; Bonbon's `short`/`note` to the Band
    controller with Action Mind Blast; add Bonbon and Asterion Psionic Backlash rows;
    add Bonbon Cull and Ability Drain rows; Charles's Psionic Overload row becomes gate
    only; Gale's `avoid` gains "never buy Ability Drain / Mind Blast" (already there)
    and loses "he is NOT taking Awakened".
  - Pronouns: Bonbon is "her" throughout.
- `content/party.md`: Gale's per_character "Each round" line gains the bonus-action
  Black Hole / Stage Fright / Stakes cast; gear line notes Awakened.
- `content/characters/gale.md:820`: delete "The party skips illithid powers".
- `docs/act2-route.md:63`: add the sitter and the Lae'zel / avatar-distance rule.
  Another session is editing this file; coordinate before touching it.
- `content/loot.md:359-360`: optional, name the sitter.
- `content/meta.md`: minor version bump (content sweep).
- `docs/build-notes-party.md`: one paragraph on why Awakened is Gale's, pointing at the
  review.

## 10. If Awakened stays on Bonbon instead

Apply §4's Bonbon, Asterion and Charles additions (Ability Drain, Cull, Backlash, Luck
core; Charles never presses Overload). Bonbon keeps Stakes, Mind Blast and Mind
Sanctuary as bonus actions under the existing "Band or the power that wins the fight"
rule. Gale buys Stage Fright only as an Action power and skips Stakes. Do not buy Black
Hole, Stage Fright or Force Tunnel for Bonbon; each fights the Band every turn. Awakened
then fires about three times per long rest, which is the cost of this option.
