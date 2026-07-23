# BG3 Party Build Review — Power + Fun/Journey (merged)

_Two adversarial multi-agent passes over the four `party_plan.json` builds: **Part A** hunts for strictly-stronger options and audits patch state; **Part B** looks for more-fun / earlier-online / smoother-respec variants. Verdicts reconcile both._

## Executive summary

| Build | Power verdict | Power headline | Most-fun alternative | Earliest-online |
|---|---|---|---|---|
| #1 Paladin (Oathbreaker/Hexblade crit-fish) | ✅ KEEP | Every load-bearing mechanic verified live on bg3.wiki and holds in the current patch: (1) Deepened Pact (Pact of the Blade, Warlock 5) Extra Attack ST… | Vengeance Sorcadin — Paladin 6 / Sorcerer 6 (Draconic or Storm). Best match for a caster-leaning player who wants many d… | Take the Hexblade dip at CHARACTER LEVEL 1, then go Paladin. This is the earliest-online AND smoothest approach for the … |
| #2 Rogue (DEX pickpocket) | 🔧 TUNE | Keep the Gloomstalker archer chassis but retune the multiclass: swap the listed Assassin+Champion for Thief 4 + Battle Master 3. This directly fixes t… | Arcane Trickster (near-pure). For a caster-brained player it wins the fun test on its own terms: it is the single rogue … | On the rogue chassis, Arcane Trickster and Swashbuckler are tied for earliest clean online: both need ZERO multiclass an… |
| #3 Sorcerer (Wet+Lightning) | ✅ KEEP | Keep the chassis. The build's three load-bearing mechanics all verified INTACT in the current patch state (Patch 8 + Hotfixes #30-#36): Wet still doub… | Storm Sorcery (built as Storm 10 / Tempest Cleric 2). For a caster player who likes many decisions per turn, Tempestuous… | Draconic-Blue Sorcerer. It is the earliest-FUNCTIONAL of the options: Draconic Resilience gives base AC 13 (+Dex) and +1… |
| #4 Bard (Acuity Commander) | 🔧 TUNE | The build is sound and every load-bearing claim checks out against the current patch: Arcane Acuity is +1 spell-attack/+1 spell-save-DC per remaining … | Ranged Swords Bard "Commander" (the base target build) is the most-fun pick that actually fits this party. Its flourish … | Lore Bard comes online earliest in raw subclass power: it is the ONLY college that gets Magical Secrets at Bard 6 (every… |

## Patch reality check (the load-bearing conclusions)

- **Patch 8 (v4.1.1, 2025-04-15) was the FINAL major patch.** Only hotfixes **#30–#36** followed through 2026; there is **no Patch 9** (the “Patch 9” pages in search are 2020 Early Access).
- **Your meta staples were untouched.** A full-text search of the official notes returned **zero** balance hits for Divine Smite, Sorcery Points, Metamagic, Bardic Inspiration, Thirsting Blade, Deepened Pact, Pact of the Blade, Risky Ring, Markoheshkir, crit gear, GWM, Sharpshooter, Savage Attacker, or Elixirs.
- **Deepened Pact + Extra Attack stacking was removed in HONOUR MODE ONLY** — it still works in your **non-Honor** party, so `Pal 7 / Hexblade 5` keeps its 3 attacks. Claims that `11 Pal / 1 Hexblade` is “strictly superior post-Patch 8” are Honour-Mode framing and don’t apply here.
- **Small relevant deltas:** Mobile Flourish QoL (Swords Bard); **Shadow Blade Ring no longer needs Concentration** + Knife of the Undermountain King advantage fix (relevant to crit builds); Elemental Weapon buffed (all damage types); Glyph of Warding now works with Spellsparkler/Mourning Frost/Winter’s Clutches; Gloves of Battlemage’s Power correctly grant Arcane Acuity. **Bhaalist Armour** got a **tooltip-only** radius fix (3m) — aggregators hallucinated a 2→3m buff; the aura was not changed.

_Patch sources:_ <https://baldursgate3.game/news/the-final-patch-new-subclasses-photo-mode-and-cross-play_138> · <https://www.gameleap.com/articles/bg3-patch-8-full-notes-new-classes-and-all-changes> · <https://bg3.wiki/wiki/Deepened_Pact> · <https://store.steampowered.com/news/app/1086940/view/3347878489035336762> · <https://bg3.wiki/wiki/Patch_Notes> · <https://gamerant.com/baldurs-gate-3-hotfix-update-30-patch-notes-changelog-whats-new/>

> Actionable changes are collected at the end of **Part A** (“Suggested edits to party_plan.json”). Ask and I’ll apply them.

---

# Part A — Power & Patch Adversarial Review

_Verdicts: is each build still optimal, what beats it, and what the current patch changes._

# Adversarial Build Review

*Party context: NON-Honour mode, party of 4. Priorities = fun, comes-online-early, tolerates moderate late-game difficulty mods. Synergy engine: Sorcerer Twinned-Hastes the Paladin and applies Wet to feed its own + the Bard's lightning; the Bard stacks Arcane Acuity to land Command/Hold (paralysis = melee auto-crit within 3m) to set up the Paladin. You personally pilot Build 1 (Paladin) and Build 2 (Rogue); an ally holds the Sorcerer. Every alternative below is judged in THIS party, not in a vacuum. Patch state assessed = Patch 8 (2025-04-15, the final major patch) + Hotfixes #30–#36 (through 2026-03-26).*

## Executive summary

| Build | Verdict | Headline |
|---|---|---|
| #1 Oathbreaker Paladin 7 / Hexblade Warlock 5, Half-Orc ("Lockadin") | **KEEP** | Near-optimal crit-smite converter for this party; all four load-bearing mechanics verified live. Only clash: comes online late (~L10). |
| #2 Gloomstalker 5 / Assassin (or Thief) 4 / Champion 3 DEX archer | **TUNE** | Keep the S-tier archer chassis; retune to **Thief 4 / Battle Master 3** to fix the decision-light autopilot and add real Paladin setup. |
| #3 Draconic-Blue Sorcerer 10 / Tempest Cleric 2 | **KEEP** | Wet-doubling + Destructive-Wrath maximize + Twinned-Haste engine fully intact; only live knobs are subclass flavor and a friendly-fire plan. |
| #4 Swords Bard 10 / Fighter 1 / Wizard 1 (Arcane Acuity "Commander") | **TUNE** | Right slot, right mechanics; swap **Wizard 1 → Fighter 2 (Action Surge)** to land Command/Hold a full turn earlier. |

## Patch changes that matter

**The two load-bearing questions, answered first:**

- **Does Deepened Pact Extra Attack still stack with Paladin Extra Attack? YES — in non-Honour only.** A Warlock 5 (Pact of the Blade / Deepened Pact) + martial-5 multiclass gets **3 attacks per action in Explorer/Balanced/Tactician**, blocked only in Honour Mode. The Honour block is a Patch 5 (Nov 2023) change, **untouched by Patch 8 and hotfixes #30–#36.** Verified live: <https://bg3.wiki/wiki/Extra_Attack>, <https://bg3.wiki/wiki/Deepened_Pact>. Your party is non-Honour, so Build #1's core works. Terminology note: this comes from **Deepened Pact**, not a separate "Thirsting Blade" invocation.
- **Does Arcane Acuity still work? YES, and it was buffed adjacent to your build.** Arcane Acuity = +1 spell attack AND +1 spell save DC per remaining turn, cap 10 (=+10 DC in non-Honour), −1/turn, **−2 per instance of damage taken** (the real sustain tax, a Patch 5 change, mostly irrelevant to a backline archer). Patch 8 **fixed** Gloves of Battlemage's Power to correctly grant Acuity — a small buff to the Bard's engine. Verified: <https://bg3.wiki/wiki/Arcane_Acuity_(Condition)>.

**Other confirmed changes relevant to these four builds:**

- **Patch 8 (2025-04-15) was the FINAL major patch** — it added 12 subclasses (incl. **Hexblade Warlock**, making Build #1's crit-fish core native, not modded), Photo Mode, cross-play. There is **no Patch 9**; everything after is a hotfix. Source: <https://baldursgate3.game/news/the-final-patch-new-subclasses-photo-mode-and-cross-play_138>.
- **Hotfix #30 (2025-04-30):** Hexblade chance-to-inflict-Curse no longer stacks per Bind re-use (edge case, does NOT touch the −1 crit-threshold); Paladin auras no longer lost after Long Rest; Rogue **Magical Ambush / Skilled Skullduggery / Lethal Concealment no longer vanish while sneaking** (fixes Arcane Trickster's core loop); Uncanny Dodge fixed. Source: <https://gamerant.com/baldurs-gate-3-hotfix-update-30-patch-notes-changelog-whats-new/>.
- **Hotfix #31 (2025-05-14):** Hexblade can replace a spell at L2; Swashbuckler Fancy Footwork works even on a miss.
- **Hotfixes #32–#36 (through 2026-03-26):** platform/stability, crash, and minor tooltip/UI only — **no load-bearing balance changes.** #36 (2026-03-26) is the latest release. Source: <https://bg3.wiki/wiki/Patch_Notes>, <https://larian.com/news/hotfix-36-now-live_149>.
- **NOT nerfed (full-text search of official notes returned zero hits):** Divine Smite (no per-turn cap; dice still double on crit), Sorcery Points, Metamagic (Twinned/Quicken), Wet+Lightning/Cold doubling, Risky Ring, Markoheshkir, Killer's Sweetheart, Sarevok's Horned Helmet, Half-Orc Savage Attacks, Sharpshooter, GWM. Source: <https://bg3.wiki/wiki/Guide:Undocumented_Patch_5_updates>, <https://bg3.wiki/wiki/Wet_(Condition)>.
- **DRS caveat (Patch 5, pre-existing, NOT new):** flat per-hit riders do **not** double on crit — only weapon dice, smite dice, and the Half-Orc Savage die double. This corrects any "everything doubles on crit" framing.
- **Debunked aggregator hallucination:** the "Bhaalist Armour 2m→3m aura radius buff" is a **tooltip-display correction only** in the official Patch 8 notes; no radius increase shipped. Source: <https://comicbook.com/gaming/news/baldurs-gate-3-patch-8-patch-notes/>.

## Build #1 — Oathbreaker Paladin 7 / Hexblade Warlock 5, Half-Orc ("Lockadin")

**Verdict: KEEP (near-optimal for this party). Confidence: high.**

### Why
This is the single best converter of the party's manufactured paralysis auto-crits into damage. All four load-bearing claims verified live:

| Claim | Status | Source |
|---|---|---|
| Deepened Pact + Paladin Extra Attack = 3 attacks (non-Honour only) | CONFIRMED | <https://bg3.wiki/wiki/Extra_Attack> |
| Hexblade's Curse: −1 crit threshold, +prof damage, heal on kill | CONFIRMED | <https://bg3.wiki/wiki/The_Hexblade> |
| Aura of Hate: +CHA melee weapon damage at class level 7 | CONFIRMED | <https://bg3.wiki/wiki/Aura_of_Hate> |
| Half-Orc Savage Attacks: extra weapon die on crit | CONFIRMED | <https://bg3.wiki/wiki/Half-Orc> |

In-context: the Bard's Command/Hold paralysis = auto-crit for melee within 3m, and this build turns each into **doubled weapon dice + doubled Divine Smite dice + doubled Half-Orc Savage die**. The Sorcerer's Twinned Haste doubles the 3-attack action to 6 attacks/turn — attack COUNT is exactly the axis this party multiplies. Short-rest Pact Magic slots mean it smites at full power every fight (unlike a Sorcadin nova that runs dry).

### Strongest alternatives
- **Hexadin 6/6 (Oathbreaker Paladin 6 / Hexblade Warlock 6)** — *viable preference fork, NOT strictly better.* Trades Aura of Hate for a 6th Warlock invocation + marginally better saves (helps offset Risky Ring's save disadvantage). Both keep Aura of Protection. 2026 guides recommend 7/5 for Oathbreaker because +CHA across 3 attacks out-damages the 6th Warlock level. Stay 7/5 for damage; go 6/6 only if you value save-survivability over nova. Source: <https://hacktheminotaur.com/baldurs-gate-3/best-bg3-lockadin-build-multiclass-guide/>.
- **Champion Fighter 11–12 GWM crit-fisher** — *conditional; only better IF the group switches to Honour Mode.* 3 native attacks + Action Surge, works identically in Honour. But for THIS non-Honour smite party it is WORSE: no Divine Smite means paralysis auto-crits only double weapon dice, wasting the party's biggest payoff. File as the Honour-Mode escape hatch, not an upgrade.

**Debunked as "strictly better here":** Sorcadin (self-Haste is redundant with the party Sorcerer, only 2 base attacks, no short-rest slot recovery); Swords Bardadin (role overlap — you already run a Swords Bard).

### Patch impacts
Nothing load-bearing was nerfed. Patch 8 made Hexblade native; hotfixes #30/#31 only touched Hexblade edge cases (Curse-stacking, L2 spell swap), not the crit-threshold reduction. Risky Ring / Sarevok's Helmet / Killer's Sweetheart / Savage Attacks / Aura of Hate all verified untouched.

### Recommended changes / expectations
1. **Stay 7/5** (Oathbreaker Paladin 7 / Hexblade Warlock 5). Half-Orc + Hexblade (Bind Hexed Weapon puts everything on CHA, no STR tax) all check out.
2. **Set the expectation: comes online LATE (~character level 10).** Before then it's an ordinary 2-attack smiter; the 3-attack nova is an Act 3 thing. This is the one genuine clash with the party's "comes-online-early" priority.
3. **Gear:** Risky Ring (permanent advantage — but permanent *disadvantage on saves*, a real fragility tax; partly offset by Aura of Protection), Killer's Sweetheart, Sarevok's Horned Helmet (stacking −1 crit threshold), Balduran's Giant Slayer or Helldusk, Amulet of Greater Health, Birthright. If late-game mods lean on Hold/Feeblemind, budget a Freedom of Movement source or consider 6/6.
4. **Zero migration to Honour Mode** — the stacked 3rd attack is disabled there. Non-issue for this party, but know the build loses its identity if you ever switch modes.

## Build #2 — DEX pickpocket archer (currently Gloomstalker 5 / Assassin (or Thief) 4 / Champion 3)

**Verdict: TUNE (keep the Gloomstalker archer chassis, retune the multiclass). Confidence: high.**

### Why
The listed brief has two false premises to drop: (1) pickpocket is **not** slot-locked — it's gated by Sleight-of-Hand total + gear + a Darkness-arrow's advantage, not subclass; and (2) **"MAX pickpocket" is impossible on any 5/4/3 archer** because Reliable Talent requires **Rogue 11** (verified: <https://bg3.wiki/wiki/Reliable_Talent>). The real complaint — decision-light autopilot — is fixable at zero cost to the party's priorities.

### Primary recommendation: Gloomstalker Ranger 5 / **Thief Rogue 4 / Battle Master Fighter 3** (DEX bow)
A strictly-better-for-you retune, not a new class:
- **Level order:** Ranger 1–5 first (Dread Ambusher + Extra Attack at 5) → Thief 4 (Cunning Action, Sneak Attack, **Fast Hands = 2nd bonus action**, **Sleight-of-Hand Expertise**) → Battle Master 3 (Action Surge + 4 maneuvers).
- **Stats/race:** DEX 17→20, CON 14, WIS 12. Halfling (Luck rerolls) or Wood Elf. Feats: Sharpshooter (L4), then DEX 20 or Alert.
- **Combat gear:** Titanstring Bow (Act 1) → The Dead Shot (Act 3); Gloves of Archery, Risky Ring, Killer's Sweetheart, Deathstalker Mantle + Elixir of Bloodlust; Bhaalist Armour later.
- **Pickpocket kit (swap out of combat):** Graceful Cloth + Gloves of Thievery/Smuggler's Ring + a Darkness arrow for guaranteed advantage. Farm the rare DC-30 checks with a one-off respec or a hireling.

**Why it beats the listed build for you:** same S-tier power and earliest-online curve (Gloomstalker still S-tier: <https://hacktheminotaur.com/baldurs-gate-3/best-bg3-ranger-builds/>); Battle Master maneuvers give a caster-like per-turn menu (Trip, Menacing, Precision, Riposte) that fixes the decision-light fear — Champion adds *zero* choices, and Assassin's auto-crit needs a Surprise opener normal fights rarely grant. Crucially, **Trip Attack (Ranged) exists** (<https://bg3.wiki/wiki/Trip_Attack_(Ranged)>) — you knock a target Prone at range to give your **Paladin** melee advantage. (Caveat: don't shoot the prone target yourself — Prone gives *ranged* attacks disadvantage.)

### The honest SWITCH option (only if caster-fantasy > early-online): Arcane Trickster
- **Split:** Rogue 11 / Fighter 1 (or Wizard/Trickery Cleric 1), hand-crossbow + scrolls.
- **Uniquely delivers both** the caster-itch AND literal **max pickpocket**: **Reliable Talent at Rogue 11** (min roll 10, crit-fail immune — VERIFIED) and **Magical Ambush at Rogue 9** (enemies get disadvantage on saves vs your spells while Hidden — a second controller for the Paladin's setups: <https://bg3.wiki/wiki/Magical_Ambush>).
- **Honest cost:** C-tier damage, no Extra Attack, peaks LATEST (L9/L11) — direct tension with "comes-online-early," weakest exactly when late-game mods bite, and partly redundant with two existing controllers. Its loop is now reliable post-Hotfix #30.

**Debunked for this party:** Swashbuckler (melee, crowds the Paladin, no caster itch — refuted despite the Hotfix #31 buff), Way-of-Shadow Monk (MAD melee, can't use bow gear, online mid), Swarmkeeper (C/B-tier, micro-heavy). **Also honest:** a ranged slot only gets *advantage* from Hold, not the 3m auto-crit double-dip a melee ally would — a genuine limit of any archer here, but the melee alternatives fail on other axes.

### Patch impacts
No load-bearing nerf. Reliable Talent still Rogue 11. Rogue options got net buffs (Hotfix #30 fixed AT stealth-cast; Patch 8 fixed Uncanny Dodge). Gloomstalker still S-tier, so the retune costs nothing on power. Sources: <https://bg3.wiki/wiki/Fast_Hands>, <https://gamestegy.com/post/bg3/1590/pickpocket-build>.

### Recommended changes
Swap **Assassin + Champion → Thief 4 + Battle Master 3**. Treat pickpocket as a ride-along (gear + Darkness arrow), not a build tax. Choose Arcane Trickster only if, on reflection, "I miss casting" genuinely outranks "comes online early."

## Build #3 — Draconic-Blue Sorcerer 10 / Tempest Cleric 2 (Wet + Lightning + Twinned Haste engine)

**Verdict: KEEP the chassis (two tuning knobs). Confidence: high.**

### Why
All three load-bearing mechanics verified INTACT: **Wet still doubles Lightning/Cold** in all modes (<https://bg3.wiki/wiki/Wet_(Condition)>, page updated 2026-06-15), **Destructive Wrath** still maximizes lightning/thunder dice once per short rest, and **Metamagic/Sorcery Points** (Twinned-Haste-the-Paladin) were never touched. The 10/2 split is the correct backbone because it's the only version that keeps the sorcery-point pool large enough to run the Twinned-Haste + Quickened engine the party is built around. **Comes online at char level 7** (Sorc 5 / Cleric 2 = Lightning Bolt + Destructive Wrath + Create/Destroy Water) — meets "comes-online-early."

### Strongest alternatives (all sidegrades, none strictly better)
- **Storm Sorcery 10 / Tempest 2** — *viable fun/AoE sidegrade.* Heart of the Storm splashes ~5 lightning/thunder to all enemies in 6m per qualifying spell, and that splash **is doubled by Wet** — out-scales Draconic's single-target +CHA on the crowds the Bard's Command/Hold creates; plus bonus-action flight. Correction: it does **not** grant innate Call Lightning — CL is merely added to the learnable list at Sorc 6. Best as an Act-3 respec via the Magic Mirror. Source: <https://bg3.wiki/wiki/Storm_Sorcery>.
- **Pure Sorcerer 12** — *consistency sidegrade.* Gains native Chain Lightning + a 6th-level slot + most sorcery points + a 3rd feat, removes Markoheshkir reliance — but **gives up Destructive Wrath** (the biggest damage lever) and heavy armor. Not strictly better.
- **Sorcerer 10 / Wizard 2 (Evocation)** — *party-relevant safety option.* Sculpt Spells makes allies immune to your AoE (directly addresses the friendly-fire problem), but costs Destructive Wrath and only comes online at char level 12. Take only if friendly fire dominates your fights.

**Debunked for this party:** 6 Sorc / 6 Tempest and Tempest-as-main (both gut sorcery points → no Twinned Haste, deleting this seat's whole reason to exist); Shadow Magic Sorcerer (control/survivability, no lightning multiplier — off-thesis).

### Patch impacts
Wet-doubling, Destructive Wrath, and Metamagic all untouched by Patch 8 / #30–#36. The only Wet-adjacent Patch 8 nerf (Water Myrmidon's Healing Vapours) is irrelevant. Long-standing caveat (not a patch change): Wet only *negates* resistance on already-lightning-resistant enemies (Steel Watchers) to 1x — carry a cold/force backup (Chromatic Orb). Chain Lightning still reachable via Markoheshkir's Bolt of Doom (1x/long rest) + scrolls.

### Recommended changes
1. Keep **Sorc 10 / Tempest 2**, take the Cleric dip early (levels 2–3) for Wet-on-demand + heavy armor.
2. **War Caster** (or Resilient: CON) is close to mandatory — you concentrate on Twinned Haste for the Paladin; second feat CHA 20 or Alert.
3. **Knob #1 (fun, not power):** Blue Draconic default; respec to Storm ~L9 for Act 3 if you value AoE + mobility.
4. **Knob #2 (real party gap):** friendly-fire plan for Paladin + Bard in the wet — prefer single-line Lightning Bolt geometry over pooled-water AoE when allies are adjacent, use Storm's flight to reposition. BG3 gives Sorcerers no Sculpt/Careful tool; only take the Wizard dip if friendly fire genuinely dominates.

## Build #4 — Swords Bard 10 / Fighter 1 / Wizard 1 (Arcane Acuity "Commander", ranged longbow)

**Verdict: TUNE (keep the build, change the split). Confidence: high.**

### Why
Every load-bearing mechanic checks out current: Arcane Acuity (+1 spell attack/+1 DC per turn, cap 10 = +10 DC; −2 per damage instance); Helmet of Arcane Acuity grants +2 turns per weapon hit; **Band of the Mystic Scoundrel** casts Enchantment/Illusion (Command/Hold Monster) as a bonus action after a weapon hit with **no spell-level cap**; Ranged Slashing Flourish's two projectiles each stack Acuity. This is the correct safe-backline controller that hard-locks targets for the Paladin's auto-crits, and it doesn't duplicate the Sorcerer's role (different, gear-driven, near-100% DC delivery). Sources: <https://bg3.wiki/wiki/Band_of_the_Mystic_Scoundrel>, <https://bg3.wiki/wiki/Slashing_Flourish_(Ranged)>.

### Strongest alternatives
- **10 Swords Bard / 2 Fighter (Action Surge)** — *the recommended tune, not a switch.* A second Attack action saturates Acuity to +10 and fires Command/Hold on **turn 1** instead of turn 2 — directly serving "comes-online-early" and "set up the Paladin." Mainstream 2025-2026 consensus. Cost: loses Wizard 1's Shield reaction (+5 AC, which also protects the Acuity stack) and scroll versatility. Sources: <https://gamestegy.com/post/bg3/1543/swords-bard-build>, <https://gamerant.com/baldurs-gate-3-bg3-best-swords-bard-archer-build-guide/>.
- **Hand-crossbow (dual-wield) variant** — *early-game weapon choice only.* Fastest turn-1 Acuity before you have STR for Titanstring, but once the loop is online the off-hand bonus-action shot **competes with the Band's bonus-action control cast** — longbow is correct in Act 3.

**Debunked for this slot:** Melee Smite SSB (sits in threat range where Acuity bleeds −2/hit taken, crowds the Paladin); Lore Bard (no weapon-attack engine → can't pump the Helmet → *lower* DC ceiling, and can't nuke-and-lock in one turn); Glamour Bard (soft charm control, doesn't scale with Acuity, no guaranteed paralysis); a second dedicated Sorcerer (role overlap).

### Patch impacts
No load-bearing nerf. Patch 8 only **buffed/fixed** relevant pieces: Mobile Flourish teleport now works on killed targets; Gloves of Battlemage's Power now correctly grant Acuity. Hotfixes #30–#36 don't touch Acuity, the Helmet, the Band, or Slashing Flourish. Sources: <https://bg3.wiki/wiki/Arcane_Acuity_(Condition)>, <https://baldursgate3.game/news/the-final-patch-new-subclasses-photo-mode-and-cross-play_138>.

### Recommended changes
1. **Wizard 1 → Fighter 2 (Action Surge).** This is your level-12 pick either way, so it doesn't change the early-game power curve (the loop is gear-gated to the Helmet in Act 2 and the Band in early Act 3 regardless). Keep Wizard 1 only if you specifically want the Shield reaction as a defensive/panic button + scroll utility — a legitimate sidegrade toward defense.
2. **Loop discipline:** weapon-attack FIRST, then the Band's bonus-action cast — once the bonus cast fires, the Quickening Incantation condition blocks casting Enchantment/Illusion as a full action that same turn.
3. Longbow once the loop is online; Sharpshooter first feat then DEX.

## New sources worth reading

*(Deduped; all post-2023, i.e. reflect Patch 8 / 2025–2026 state — unlikely in a 2023 research set.)*

- <https://bg3.wiki/wiki/The_Hexblade> — Hexblade subclass (added Patch 8, 2025); crit-fish core mechanics.
- <https://bg3.wiki/wiki/Extra_Attack> — current confirmation that Deepened Pact stacks outside Honour only.
- <https://bg3.wiki/wiki/Guide:Patch_8_preview> — Patch 8 mechanic/DRS summary (2025).
- <https://baldursgate3.game/news/the-final-patch-new-subclasses-photo-mode-and-cross-play_138> — official "final patch" announcement (2025-04-15).
- <https://bg3.wiki/wiki/Patch_Notes> — hotfix index through #36 (2026-03-26).
- <https://larian.com/news/hotfix-36-now-live_149> — latest release, Hotfix #36 (2026-03-26).
- <https://hacktheminotaur.com/baldurs-gate-3/best-bg3-lockadin-build-multiclass-guide/> — 2026 Lockadin guide (7/5 vs 6/6 rationale).
- <https://hacktheminotaur.com/baldurs-gate-3/best-bg3-ranger-builds/> — 2026 Ranger tiers (Gloomstalker S / Swarmkeeper C).
- <https://gamestegy.com/post/bg3/1543/swords-bard-build> — Swords Bard split, updated 2025-11-06 (recommends 10/2 Fighter).
- <https://gamerant.com/baldurs-gate-3-bg3-best-swords-bard-archer-build-guide/> — Swords Bard archer, 2025-04-25.
- <https://bg3.wiki/wiki/Trip_Attack_(Ranged)> — confirms ranged Prone setup for the Paladin.
- <https://bg3.wiki/wiki/Wet_(Condition)> — Wet-doubling page, updated 2026-06-15.
- <https://bg3.wiki/wiki/Guide:Book%27s_Guide_to_Crits> — current crit-item reference (Risky Ring / Sarevok's / Killer's Sweetheart).

## Suggested edits to party_plan.json

- **Build #1 (Paladin):** Keep as **Oathbreaker Paladin 7 / Hexblade Warlock 5, Half-Orc**. Add a note: "3-attack nova is Act 3 (~char L10); plays as a 2-attack smiter before then." Add a caveat that Risky Ring gives permanent *disadvantage on saves* — budget Freedom of Movement or consider 6/6 if late-game mods lean on Hold/Feeblemind. Correct any "everything doubles on crit" wording: only weapon + smite + Savage die double (DRS).
- **Build #2 (Rogue):** Change the split from **Gloomstalker 5 / Assassin 4 / Champion 3** to **Gloomstalker 5 / Thief 4 / Battle Master 3**. Remove the false premise that pickpocket needs a dedicated slot or that a 5/4/3 archer reaches "MAX" pickpocket (Reliable Talent = Rogue 11). Note Arcane Trickster (Rogue 11 / 1-dip) as the *conditional switch* if caster-fantasy outranks early-online. Add: "Trip Attack (Ranged) sets up Prone → melee advantage for the Paladin; don't shoot the prone target yourself."
- **Build #3 (Sorcerer):** Keep **Sorc 10 / Tempest 2**. Add two knobs: (a) optional Storm Sorcery Act-3 respec for AoE/fun; (b) an explicit friendly-fire plan (Paladin + Bard stand in the wet — favor single-line Lightning Bolt geometry, no Sculpt Spells available without a Wizard dip). Correct the note that Storm grants innate Call Lightning — it only adds CL to the learnable list at Sorc 6.
- **Build #4 (Bard):** Change split from **10/1/1 (Fighter/Wizard)** to **10 Swords Bard / 2 Fighter (Action Surge)** to land Command/Hold a turn earlier; note Wizard 1 (Shield) as the defensive sidegrade. Add loop rule: weapon-attack before the Band's bonus-action cast (Quickening Incantation).
- **Global:** Add a "Patch state" line — assessed against Patch 8 (final major patch, 2025-04-15) + Hotfixes #30–#36 (latest 2026-03-26); no load-bearing mechanic for any build was nerfed. Flag the debunked "Bhaalist Armour radius buff" rumor as a tooltip fix only. Note the whole plan is non-Honour-mode dependent (Deepened Pact 3rd attack disabled in Honour).

---

# Part B — Fun / Early-Online / Respec-Path Review

_Sidegrades and journey: more fun to pilot, faster to come online, smoother leveling/respec._

# Fun / Early-Online / Respec-Path Review

*NON-Honor · 4 players · priorities: FUN FIRST, come-online-early, tolerates moderate late-game difficulty mods. You play #1 Paladin and #2 Rogue and lean caster (lots of decisions per turn). This pass ranks builds by fun / earliness / smoothness, NOT raw power — sidegrades and slight downgrades are fair game if they play better.*

## At a glance

| Slot | Most-fun pick | Earliest-online pick | Respecs to endgame |
|---|---|---|---|
| #1 Paladin | Vengeance Sorcadin (Pal 6 / Sorc 6) | Hexblade dip at char level 1, then Paladin | 0 (Hexblade-first) |
| #2 Rogue | Arcane Trickster (near-pure Rogue 12) | Arcane Trickster or Swashbuckler at L3 | 0 (single-class) |
| #3 Caster | Storm Sorcery 10 / Tempest 2 | Draconic-Blue 10 / Tempest 2 | 0 (or 1 optional Draconic->Storm) |
| #4 Support | Ranged Swords "Commander" (Bard 10 / Ftr 1 / Wiz 1) | Lore Bard (Magical Secrets at Bard 6) | 1 (at char level 8) |

---

## #1 Paladin slot (current endpoint: Oathbreaker Pal 7 / Hexblade 5)

**Reality check that reframes this whole slot:** the "post-Patch-8 the 3-attack Deepened-Pact combo is gone, so 11 Pal / 1 Hexblade is strictly superior" claim is TRUE ONLY IN HONOUR MODE. Your party is NON-Honor, so Deepened Pact (Warlock 5) still stacks with Paladin's Extra Attack = 3 attacks/turn. The deep 7/5 Hexblade split is a valid top-end melee nova here, not obsolete. So this pass is genuinely a fun/smoothness choice, not a forced downgrade.

**Most fun: Vengeance Sorcadin — Paladin 6 / Sorcerer 6 (Draconic or Storm).**
Best fit for a caster-brained player who wants many decisions per turn. Concrete fun, de-hyped:
- Metamagic adds real per-turn choices. Quickened Spell lets you cast a leveled spell (Hold Person to guarantee smite-crits, Command, Fireball) AND weapon-attack in the SAME turn — BG3 does not enforce tabletop's one-leveled-spell-per-turn rule.
- Twinned Haste buffs you plus an ally (feeds the party's existing haste engine).
- Vow of Enmity (Pal 3) hands you Advantage on demand — crit-fishing without needing the Risky Ring.
- 6/6 keeps Aura of Protection, a 4th-level slot, extra Metamagic, and has NO Oathbreaker respec tax.

Honest tradeoff: modestly lower single-target DPR than the crit-fish Hexblade nova; long-rest (not short-rest) slots, so you nova then run dry; Concentration juggling on Haste. It changes the fantasy from Half-Orc Oathbreaker to a Vengeance caster-smiter — which is exactly the "lots of decisions" you like.

**Earliest online (also the smoothest): take the Hexblade dip at CHARACTER LEVEL 1, then go Paladin.**
At level 1 you already attack with CHA (dump STR permanently — no STR elixirs, no respec ever), have Hexblade's Curse (crit range 19-20 + on-kill heal), and wear medium armor + shield. The only cost vs a Paladin-first order: Divine Smite lands one character level later (char 3 vs 2) and Paladin's Extra Attack one level later (char 6 vs 5) — trivial next to zero respecs. Paladin-first reaches raw Divine Smite at char 2 but forces a STR phase and a later STR->CHA respec, which for Oathbreaker triggers the ~1000g oath-reclaim tax.

**Recommended leveling + respec path (7 Pal / 5 Hexblade, ZERO respecs):**
- Char 1: Warlock 1 (Hexblade) — Bind Hexed Weapon (CHA attacks), Hexblade's Curse, medium armor/shield/martial. STR 8, max CHA.
- Char 2: Paladin 1 — Lay on Hands, heavy-armor prof.
- Char 3: Paladin 2 — Divine Smite (nova online).
- Char 4: Paladin 3 — pick Oath. **Vengeance recommended** (Vow of Enmity = Advantage on demand, no oath-break tax).
- Char 5: Paladin 4 — Feat (Savage Attacker pairs with Half-Orc Savage Attacks, or +2 CHA).
- Char 6: Paladin 5 — Extra Attack.
- Char 7: Paladin 6 — Aura of Protection.
- Char 8-11: Warlock 2->5 — invocations (Agonizing Blast / Devil's Sight), Pact of the Blade at W3, Deepened Pact at W5 = 3 attacks/turn at char 11.
- Char 12: Paladin 7 — final aura.

**Oathbreaker-specific warning:** you cannot respec while your oath is broken — you must pay the Oathbreaker Knight ~1000g to reclaim, respec, then re-break. (The "cost escalates each time" claim is unverified — treat as unconfirmed.) Two clean fixes: (1) this Hexblade-first path needs no respec, so just don't respec while broken; (2) staying Vengeance instead of Oathbreaker avoids the mechanic entirely and is arguably more fun. Only Oathbreaker's Aura of Hate (+CHA weapon damage at Pal 7) is the reason to break at all.

*Alternative if you want Extra Attack one level sooner:* Paladin 1-5 first, then Warlock 1-5, then Pal 6-7 — but you run STR (or a Giant Strength elixir) until you rebuild, plus one planned respec around char 8. Only worth it if that single earlier Extra-Attack level matters to you.

**Other fun options and their tradeoffs:**
- **11 Pal / 1 Hexblade (earliest & smoothest melee):** CHA smiter from char 1, Vow of Enmity char 4, Improved Divine Smite char 12, no respec. Punchy but fewer caster decisions. In non-Honor this is a *sidegrade*, not an upgrade.
- **Bardadin (Swords Bard 10 / Pal 2):** max decisions — Flourishes, Bardic Inspiration, Magical Secrets at Bard 10 (Haste/Counterspell/Spirit Guardians). Funky curve: Bard to 6 first (Extra Attack ~char 8), then Pal 2, then Bard to 10. Loses Aura of Protection.
- **Ancients Lockadin (7 Ancients / 5 Hexblade):** same loop plus Aura of Warding (halves spell damage for allies). No oath-break mechanic, smoother than Oathbreaker; lower personal DPR.
- **Oath of the Crown Hexblade (11/1 novelty tank):** role-flip taunt + Spirit Guardians controller. Strict tenets make accidental oath-break easy.
- **Pure Paladin 12:** smoothest possible ride, 3 feats, Improved Divine Smite at 11 — but the fewest decisions per turn.

*Verified breakpoints (bg3.wiki): Divine Smite Pal 2 · Extra Attack Pal 5 · Aura of Protection Pal 6 · 2nd oath aura Pal 7 · Improved Divine Smite Pal 11 · Vow of Enmity Pal 3 · CHA attacks + Hexblade's Curse (Bind Hexed Weapon) Warlock 1 · Pact of the Blade W3 · Deepened Pact W5 · Swords Bard Extra Attack Bard 6 · Magical Secrets Bard 10. Hexblade is base-game Patch 8 (Apr 15, 2025) content, not a mod.*

---

## #2 Rogue slot (DEX pickpocket)

**Most fun + top pick: Arcane Trickster (near-pure Rogue 12).**
It is the one Rogue subclass that adds a real spell/scroll decision layer on top of Sneak Attack, so it scratches the caster itch while being the best pickpocket in the game (Sleight of Hand + Perception Expertise -> Reliable Talent at L11 = minimum-10 on every steal). Fun landmarks (all mechanically confirmed):
- L3: invisible, permanent Mage Hand Legerdemain + first spells (Disguise Self, Fog Cloud, Tasha's Hideous Laughter, Shield). Build "becomes itself" here.
- L7: 2nd-level slots — Misty Step, Invisibility, Hold Person, Mirror Image.
- L9: Magical Ambush — cast while Hiding and the target rolls Disadvantage on the save (applies to pickpocketed SCROLLS too).
- L11: Reliable Talent.

Honest de-hype: L1-3 plays as a plain ranged rogue, so the caster payoff is gradual; and it is genuinely low raw single-target DPS (no Extra Attack, once-per-turn Sneak Attack). Fine here — the party already has Sorc + Paladin for damage.

**Earliest online:** Arcane Trickster and Swashbuckler tie — both need zero multiclass and become themselves at L3 (AT: Mage Hand + spells; Swashbuckler: Rakish Audacity 1v1 Sneak Attack + near-auto first turn, Dirty Tricks control at L4). The absolute earliest is the CHA Bard-based gish (spells + Bardic Inspiration from L1-2), but it duplicates the party Bard and sequences awkwardly. **Recommended earliest-that-fits: Arcane Trickster at L3.** Avoid the Gloomstalker/Assassin burst if earliness matters — its nova needs Ranger 5 + Fighter 2 (~char 6-7), and Shadow Monk's signature Shadow Strike is L11.

**Recommended leveling + respec path (default pure Rogue 12).** Stats: DEX primary (16 -> 20), INT 14 (spell DC / Mage Hand), CON 14.
- L1: Expertise Sleight of Hand + Perception; Thieves' Tools.
- L2: Cunning Action (feeds Magical Ambush later).
- L3 -> Arcane Trickster: spellcasting + invisible Mage Hand; learn Mage Hand, cantrips, Disguise Self / Fog Cloud / Tasha's / Shield.
- L4: Feat #1 — ASI DEX 16->18.
- L5: Uncanny Dodge; Sneak Attack 3d6.
- L6: Expertise on 2 more skills (Arcana + Investigation, or Stealth).
- L7: Evasion; 2nd-level slots — add Misty Step / Invisibility / Hold Person / Mirror Image.
- L8: Feat #2 — ASI DEX 18->20.
- L9: Magical Ambush — Cunning Action Hide -> Hold Person / stolen Hypnotic Pattern / Confusion at Disadvantage.
- L10: 3rd cantrip; Feat #3 (Alert, or ASI INT for DC).
- L11: Reliable Talent — you essentially never fail a pickpocket/lockpick again.
- L12: Feat #4 (ASI / Lucky / Resilient CON).

**Respec notes:** single-class = no mid-run Withers juggling; the only real choice is the L3 subclass, so respeccing INTO Arcane Trickster from any other rogue is trivial. If you want rock-solid Concentration for control spells plus a +2 ranged attack, run **Rogue 11 / Fighter 1** — but the Fighter level MUST be taken at character creation (level 1); multiclassing into Fighter later gives armor/weapon profs but NOT the CON saving-throw proficiency. Cost: Reliable Talent one level later (L12) and you give up the 4th Rogue feat. Spice: Rogue 11 / Wizard 1 (Abjuration) as your LAST level adds an Arcane Ward retribution-tank layer without disrupting the curve.

*Note on slots: AT caps at 2nd-level spell slots at level 12 (no 3rd-level slots), so Chain Lightning / Cone of Cold etc. are castable only from pickpocketed scrolls — and Magical Ambush's Disadvantage does apply to those scrolls when cast while Hiding.*

**Other fun options and their tradeoffs:**
- **CHA Bard/Rogue gish (e.g. 6 Bard / 4 Rogue / 2 Wizard):** most total spellcasting + party Face; earliest online. Fiddly multiclass order, ~1 planned respec near Act 2/3. Redundant with the team's existing Bard.
- **Swashbuckler (pure 12):** bonus-action Dirty Tricks (disarm/blind/Vicious Mockery) partly scratches the choices-per-turn itch; melee duelist + Face; tied-cleanest single-class. No Extra Attack, C-tier DPS, very smooth ride. (Rakish Audacity's initiative bonus is a flat +2 in BG3, not CHA-scaled.)
- **Gloomstalker / Assassin burst (Ranger 5 / Fighter 3 / Rogue 4):** highest burst, but spectacle over decisions; strict order, 1 planned Act-3 respec; scripted Act 2-3 fights block Surprise.
- **Shadow Monk (pure 12, +1 Rogue for pickpocket):** stylish mobility/stun, Ki not spells (least caster-flavored); Cloak of Shadows at L5, Shadow Step L6, spike at L11. Correction: Cloak of Shadows invisibility DOES end the moment you attack/cast/take damage — it's a reposition tool, not attack-from-stealth. MAD (DEX+WIS); wrong fantasy for this player.
- **Thrown-weapon DEX Rogue:** weakest fit; real throw builds are STR Barbarian/Thief. Skip unless the throw fantasy itself is the whole appeal.

*Verified breakpoints (bg3.wiki): AT spells L3, 2nd-lvl slots L7, Magical Ambush L9, Reliable Talent L11; Swashbuckler Rakish Audacity L3 / Dirty Tricks L4 / Panache L9; Gloom Stalker Dread Ambusher L3, Extra Attack (Ranger) L5; Way of Shadow Cloak of Shadows L5 / Shadow Step L6 / Shadow Strike L11; Rogue feats at 4/8/10/12; throwing scales off STR.*

---

## #3 Caster slot (Wet + Lightning storm-mage)

**Most fun: Storm Sorcery 10 / Tempest Cleric 2.**
Mechanically identical in power to the baseline Draconic-Blue 10/Tempest 2 (self-Wet via Create/Destroy Water at Storm 6, Destructive Wrath maximize at Cleric 2, Twinned Haste intact for the Paladin) but adds **Tempestuous Magic**: a bonus-action 9m fly with no opportunity attacks after every leveled spell, from character level 1. That layers a kite/reposition/AoE-angle decision onto your metamagic choices every turn, at zero power cost. De-hyped: the "fun" is concretely the positioning micro-decision and the damage you avoid by never being pinned — not a damage increase. (Runner-up novelty is Wild Magic, but it's the latest bloomer and weakest damage — pure fun pick.)

**Earliest online: Draconic-Blue Sorcerer.** Draconic Resilience gives base AC 13 (+Dex) and +1 HP per Sorcerer level from L1, so Act 1 is survivable; Elemental Affinity adds CHA to every lightning hit at Sorcerer 6. The wet+lightning nuke identity is live for ALL variants at Sorcerer 5 (Lightning Bolt). Early-power order: Draconic (L1 survivability, L6 always-on +CHA) > Storm (L6 Heart of the Storm) > pure Chain-Lightning / Wild Magic (both L11). **Best-of-both:** start Draconic-Blue for Act 1, free-respec to Storm around L6+.

**Recommended leveling + respec path — level PURE Sorcerer 1-10, then Tempest Cleric at char 11-12.** (Dipping Cleric early only delays your higher Sorcerer slots; Destructive Wrath is a multiplier you bolt on last.) Stats ~16 CHA / 14-16 CON / 14 DEX.
- L1 Sorcerer (choose subclass NOW — Storm for fun, Draconic-Blue for a safer Act 1). **Always take Sorcerer at level 1:** the Sorcerer's own saving-throw proficiencies are CON + CHA, so Sorcerer-first gives BOTH CHA scaling AND CON-save proficiency for concentration. Cantrips: Shocking Grasp, Ray of Frost, Firebolt. Spells: Shield, Chromatic Orb (Lightning), Mage Armor (skip if Draconic).
- L2 Metamagic: Twinned + Careful (or Distant). Early twin nuke = Twinned Chromatic Orb.
- L3 Metamagic: Quickened.
- L4 Feat: War Caster (protects Twinned Haste on the Paladin).
- L5 **Identity online:** Lightning Bolt. Wet a target -> Lightning Bolt doubled. (Line AoE — hits multiple naturally, not via Twinned.)
- L6 Subclass spike: Storm = Heart of the Storm free AoE + Create/Destroy Water (self-Wet) + resistance; Draconic = Elemental Affinity (+CHA per lightning hit).
- L7: 4th-level spells (Ice Storm, Dimension Door).
- L8 Feat: +2 CHA (or Elemental Adept: Lightning to pierce resistance).
- L9: 5th-level spells (Cone of Cold).
- L10: 4th Metamagic (Heightened/Distant); biggest sorcery-point pool for Quickened.
- L11-12: Tempest Cleric 1 -> 2 — heavy armor + Wrath of the Storm, then Destructive Wrath maximize. Signature turn: (Quickened) Create Water -> Lightning Bolt / Cone of Cold + Destructive Wrath = Wet-doubled AND maximized.

**Respec rules:** Withers respecs are free/unlimited. On every respec take Sorcerer at level 1 first, then append the 2 Cleric levels. Subclass is a level-1 choice, so Draconic<->Storm<->Wild is a cheap full-respec test. Amulet of Greater Health (Act 2) frees your CON stat. Dip Cleric LAST (L11-12) for the smoothest climb; if you want Destructive Wrath earlier, the 6 Sorc / 6 Tempest split gets it ~char 6-7 (and Call Lightning at Cleric 5) at the cost of 5th/6th-level slots and metamagic depth.

**Important corrections baked in (both original finders had these backwards):**
- CON saves: Sorcerer-first is CORRECT for concentration — the Sorcerer's own saves are CON + CHA. Taking Cleric first would instead give WIS + CHA and LOSE the CON proficiency. No CHA-vs-CON tradeoff exists.
- Twinned Spell CANNOT hit Lightning Bolt (line AoE) or Chain Lightning (multi-target). Valid twins: Chromatic Orb, Haste (the Paladin synergy), Hold Person. Nuance: the Markoheshkir-GRANTED Chain Lightning can still be twinned; the learned class spell cannot (disabled Patch 6).
- Call Lightning is a Tempest spell at CLERIC level 5 — the 2-level dip does NOT grant it. Only the 6/6 split and the Cleric-9 Thunder Apostle get it.
- Storm Sorcery grants only Create/Destroy Water (L6) and Fly (L11) off-list — NOT Sleet Storm / Call Lightning / Thunderwave.
- Draconic-Blue's lightning RESISTANCE is the Elemental Affinity option at Sorc 6 (costs a sorcery point), not innate at L1; Blue ancestry's L1 grant is Witch Bolt.

**Other fun options and their tradeoffs:**
- **Pure Sorcerer 12 (Chain Lightning):** most decisions/turn, no multiclass to fumble, native Chain Lightning + 6th-level slots; most respec-proof. Loses Destructive Wrath maximize + self-Wet (lateral).
- **Cold / Draconic-White (ice control):** Ray of Frost as slot-free primary; ice surfaces prone-lock rooms. Gear-gated (Mourning Frost, late Act 1); a few more enemies resist cold. Lateral.
- **6 Sorc / 6 Tempest "Talos Dragonling":** Thunderbolt Strike knockback pinball, two maximized casts/short rest, tankier; loses 5th/6th Sorc slots + metamagic depth (fewer decisions). Power-competitive.
- **Thunder Apostle (Cleric 9 / Sorc 3):** frontline storm-priest with Spirit Guardians + healing; durability/utility sidegrade, fewest metamagic decisions, biggest stat re-tune (WIS matters).
- **Wild Magic 12:** chaos surges make every fight different; truly online only at L11 (Controlled Chaos), weakest damage (B-tier). Pure fun pick, fully respec-friendly.

*Verified breakpoints (bg3.wiki): subclass/domain at L1; Destructive Wrath Cleric 2; Draconic AC13+Dex and +1 HP/level from L1; Elemental Affinity + Heart of the Storm at Sorc 6; Tempestuous Magic 9m fly from L1; metamagic 2/1/1 at L2/3/10; feats 4/8/12; spell slots 3rd@5 / 4th@7 / 5th@9 / 6th@11; native Chain Lightning Sorc 11; Sorcerer saves CON+CHA.*

---

## #4 Support slot (Swords Bard control)

**Most fun that actually fits this party: Ranged Swords Bard "Arcane Acuity Commander" (Bard 10 / Fighter 1 / Wizard 1).**
Its flourish -> stack Arcane Acuity -> bonus-action Command/Hold/Hypnotic Pattern loop is the most decision-dense turn engine of the options, it stays at range so it does NOT crowd your own melee Paladin (slot #1), and Fighter 1 gives the CON-save proficiency that protects concentration on your control spells. Core loop: ranged Slashing Flourish (two shots per Bardic die) or Arrow of Many Targets stacks Arcane Acuity (Helmet of Arcane Acuity, Act 2), turning a sky-high Spell Save DC into bonus-action Enchantment/Illusion casts via Band of the Mystic Scoundrel (Act 3). Fighter 1 = CON saves + heavy armor/shield + Archery style (cancels Sharpshooter's -5); Wizard 1 = scroll-scribing + completes the 6th spell slot.

Two runner-ups by taste: **Melee Smite "Bardadin" (Bard 10 / Pal 2)** is the highest-dopamine pick — banking fat Bard slots into crit Divine Smites on forced-crit Command targets is the biggest-number fantasy in the game — but it's a distinct melee chassis that overlaps your Paladin frontline and drops the Fighter CON-save. **Lore Bard** is the pick for the most decisions per turn (reactive Cutting Words + double Magical Secrets), de-hyped below.

**Earliest online: Lore Bard.** It's the only college that gets Magical Secrets at Bard 6 (all others wait until Bard 10), poaching Counterspell / Command / Hunger of Hadar ~4 levels early, with Cutting Words already live at Bard 3. Caveat: every college is strong from L1 (Expertise + Jack of All Trades face, real spells + Bardic Inspiration) and martial colleges get Extra Attack at Bard 6. For the TARGET ranged Swords build specifically, the martial core is online by Bard 6 but the control engine is gear-gated: partial in Act 2 (Acuity helm), full loop only in Act 3 (Band of the Mystic Scoundrel).

**Recommended leveling + respec path (10/1/1 — ONE respec, at char level 8):**
- Levels 1-7: level PURE Swords Bard (no early dip — Bard has no multiclass tax). L1: CHA 16+ / DEX 16 / CON 14; Vicious Mockery + a damage cantrip; play ranged (Faerie Fire, Dissonant Whispers, Cloud of Daggers). L3: College of Swords, Two-Weapon Fighting (or Dueling+shield for early AC); start using ranged Slashing Flourish. L4: Feat — ASI CHA 18 (or Sharpshooter). L5: Bardic Inspiration -> d8 and short-rest recharge (Font of Inspiration) — the real power jump. L6: Extra Attack. L7: capstone slots.
- **Level 8 = the single respec.** Rebuild in EXACT class order: **Fighter 1 -> Wizard 1 -> Bard 6** (then Bard to 10 as you level to 12). Fighter FIRST = never lose CON-save concentration protection, plus heavy armor/shield and Archery style. Wizard SECOND = scribe scrolls + completes the 6th slot. Because Fighter+Wizard are first, your two Bard ASIs land at CHARACTER levels 6 (Bard 4) and 10 (Bard 8): take Sharpshooter and +2 CHA (or Dual Wielder).

**Item timeline:** Helmet of Arcane Acuity (Act 2) turns each flourish hit into +Spell Save DC -> control comes online; Band of the Mystic Scoundrel (Act 3) enables bonus-action Command/Hold after a weapon hit -> full loop. Weapons: dual hand crossbows early (more attacks = faster Acuity stacking) -> Titanstring Bow + Club/Elixir of Hill Giant Strength late.

**Corrections baked in (finders missed these):**
- **Arcane Acuity caps at 7 stacks (+7 Spell Save DC)** — NOT the "8-10" / "snap to 8" claimed. One big hit can add several stacks/turn, but +7 is the ceiling.
- **The 10/1/1 build has only 2 feats** (Bard 4 and Bard 8) vs 3 for a pure Bard 12 — a real cost the finders didn't flag, because Fighter 1 / Wizard 1 grant no feats.
- **Rogue 11 / Fighter 1 rule applies here too:** the Fighter CON-save only comes if Fighter is taken at char creation OR (as here) as the first class in the respec rebuild — multiclassing into it later gives no saving-throw proficiency.
- If you run **Bardadin instead:** Paladin **Oath is chosen at Paladin level 1**, not level 2; Fighting Style AND Divine Smite both arrive at Paladin level 2. Level order: Bard 6 FIRST (lock Extra Attack — never dip Paladin before Bard 6), then Pal 1 (Oath + Lay on Hands), then Pal 2 (Fighting Style Defense + Divine Smite + slots), then Bard to 10. No Fighter CON-save on this chassis = more fragile in melee.

**Other fun options and their tradeoffs:**
- **Melee Smite "Bardadin" (10 Bard / 2 Pal):** highest burst ceiling, big novas; more fragile, no Fighter CON-save, DC ramp slightly slower. Overlaps your Paladin frontline.
- **Lore (pure, or same 1/1 dip):** most decisions/turn (reactive Cutting Words + double Magical Secrets), earliest online. Lower weapon damage, squishy early. De-hype: **Cutting Words is bugged to a flat -1d6 vs all non-bard enemies** (it reads the attacker's bard level), so its reactive nerf never scales past d6.
- **Valour (pure):** lowest complexity, proactive Combat Inspiration die, only bard with shield prof; stable, lower ceiling, Magical Secrets only at L10.
- **Glamour (Patch 8 novelty buffer):** Mantle of Inspiration = group temp HP, no concentration, lasts to long rest — genuine set-and-forget team buff. But **Mantle of Majesty (the repeatable-Command feature) is a CONCENTRATION action**, so it competes with holding Hold Person / Hypnotic Pattern — you can't stack both. Weakest per optimizers; not a natural 1/1/10 fit.

*Verified breakpoints (bg3.wiki): subclass at Bard 3; Font of Inspiration / short-rest d8 at Bard 5; Extra Attack at Bard 6; Lore Magical Secrets at Bard 6 and 10; Arcane Acuity 7-stack cap; Paladin Oath at level 1, Divine Smite/Fighting Style at level 2; Cutting Words attacker-level bug; Glamour Mantle of Majesty is concentration.*

---

## New sources worth reading

- **bg3.wiki — Deepened Pact** — confirms Warlock Extra Attack stacks with Paladin/Fighter Extra Attack in all non-Honour modes (removed only in Honour). Load-bearing for slot #1.
- **bg3.wiki — The Hexblade** — Bind Hexed Weapon (CHA attacks at Warlock 1) + Hexblade's Curse; base-game Patch 8 (Apr 15, 2025) content, not a mod.
- **bg3.wiki — Metamagic: Twinned Spell** — eligibility (single-target only); rules out Twinned Lightning Bolt / Chain Lightning.
- **bg3.wiki — Storm Sorcery / Draconic Bloodline / Tempest Domain** — Tempestuous Magic, Heart of the Storm, Elemental Affinity, Destructive Wrath (Cleric 2), Call Lightning (Cleric 5).
- **bg3.wiki — Arcane Trickster** — L3/L7/L9/L11 breakpoints and 2nd-level slot cap.
- **bg3.wiki — Cloak of Shadows** — invisibility ends on attack/cast/damage (corrects the Shadow Monk pitch).
- **bg3.wiki — Arcane Acuity (Condition) / Helmet of Arcane Acuity** — 7-stack (+7 DC) cap.
- **bg3.wiki — Cutting Words** — attacker-bard-level scaling bug (flat -1d6 vs non-bards).
- **bg3.wiki — College of Glamour / Mantle of Majesty** — Mantle of Majesty is a concentration action; Mantle of Inspiration is not.
- **gamestegy.com — Bardadin, Arcane Trickster, Swashbuckler, Talos Dragonling, Storm/Cold Sorcerer guides** — dated community leveling orders for the runner-up variants.
- **hacktheminotaur.com — Sorcadin build** and **gamestegy.com — Oath of Vengeance Paladin** — reference paths for the slot #1 most-fun pick.
