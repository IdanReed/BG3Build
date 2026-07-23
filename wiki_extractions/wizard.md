# Wizard (1-level dip) — BG3 progression & spell reference

> Sources: bg3.wiki (Wizard, Spells, Transcribing scrolls, Shield, Command, Arcane Recovery pages) + local KB (`party_plan.json`). Patch 8, non-Honour. Used by **SimonSays** (Swords Bard 10 / Fighter 1 / **Wizard 1**) — a pure utility dip taken as the character's **final level (char lvl 9 in the plan's post-respec order, after Fighter 1)**. Its whole job: **scribe scrolls**, get **Shield**, and raise the caster level enough to **unlock the single Level-6 spell slot**.

## Spellcasting

- **Spellcasting ability: Intelligence.** SimonSays runs INT 16 (+3) via the respec (Gloves of Dexterity cover DEX, freed DEX points go to INT). This governs the Wizard spell save DC / attack and the number of Wizard spells preparable. It does **not** touch the build's headline payoff (see below), because that runs on the Bard's CHA.
- **Known-vs-prepared-vs-scribe (Wizard is a hybrid):**
  - Wizards learn spells into a **spellbook** — **6 spells chosen at Wizard level 1**, then +2 each further Wizard level (this dip only ever gets the initial 6).
  - Wizards then **prepare** a subset of the spellbook to cast. **Prepared count = Wizard level + INT modifier (min 1)** → at Wizard 1 / INT 16 that's **4 prepared Wizard spells**. Re-preparable any time out of combat.
  - Wizards **do NOT have the Replacement Spell feature** that Bard/Sorcerer/etc. use to swap a known spell on level-up. Instead, the Wizard grows its spellbook by **transcribing scrolls** — permanently adding a Wizard-list spell for `50 gp × spell level` + consuming the scroll, no known-spell given up.
  - **Level-up replacement rule:** a Wizard cannot replace a known spell on level-up (no Replacement Spell). The Bard levels *do* offer Replacement Spell; the Wizard level does not. Prepared casters (incl. this Wizard slice) otherwise re-pick prepared spells freely out of combat.
- **Cantrips known at Wizard 1: 3** (chosen from the Wizard cantrip list; INT-scaled, separate from the Bard's cantrips).
- **Transcribing scope:** only **one** Wizard level is needed to transcribe *any* Wizard-list scroll up to the level of slot you can cast — and with the multiclass build that's up to **Level 6** (see Level-by-level). ⚠️ The **50% (25 gp/level) school discount requires a Wizard subclass**, which is chosen at Wizard **level 2** — so this 1-level dip pays **full 50 gp/level** with no discount.
- ⚠️ **Prep-slot bottleneck:** transcribed/spellbook spells can only be *prepared* if you have free Wizard prep slots — and the dip only has **4** (1 + INT 3), one of which Shield usually occupies. You can scribe a big library but only field ~4 Wizard spells at a time (re-preppable out of combat). Bard's own "known" spells are a *separate* pool and are unaffected.
- **Shared slots:** all classes pour into one multiclass spell-slot pool; any slot of the right level casts **any** spell you know/prepare regardless of source class. That's why the Wizard-granted Level-6 slot can be spent on the Bard's Command.

## Level-by-level

Only **Wizard 1** is taken. "New spell slots" reflects the multiclass reality (the Wizard's own-class table is shown for reference, but slots actually come from the combined caster-level pool).

| Class Lvl | Features gained | New spell slots | Spells you may add / replace | Cantrips |
|---|---|---|---|---|
| **Wizard 1** (this dip) | Spellcasting (INT); **Arcane Recovery** (1 charge → recover one L1 slot, 1×/day, out of combat, ⚠️ minor on a dip); **Transcribing scrolls** (scribe Wizard scrolls → spellbook) | Own-class table: **2× L1**. In the multiclass build these merge into the shared pool: adding this full-caster level raises **ESL 10 → 11**, so the pool becomes **4 / 3 / 3 / 3 / 2 / 1** — i.e. it **unlocks the single Level-6 slot**. | **Learn 6** spells from the Wizard L1 list (incl. **Shield**). **No Replacement Spell** on level-up; grow the book later via scrolls. Prepared = 1 + INT (4 at INT 16). | **3** (choose from Wizard cantrip list) |
| *(Wizard 2 — not taken)* | *Choose a subclass / school of magic (would enable the 25 gp scribe discount)* | *—* | *+2 spells* | *—* |
| *(Wizard 4 — not taken)* | *Feat (Wizard's first feat is at Wizard 4)* | *—* | *+2 spells* | *—* |

**How the Level-6 slot math works (the reason to dip):** effective spellcaster level (ESL) sums full-caster class levels; base Fighter (not Eldritch Knight) adds **0**. Bard 10 (full) + Wizard 1 (full) + Fighter 1 (0) = **ESL 11**. The multiclass table gives ESL 10 → `4/3/3/3/2` (no L6) but **ESL 11 → `4/3/3/3/2/1`**. So at char lvl 11 (Bard 10 / Fighter 1, ESL 10) SimonSays has *no* 6th slot; the Wizard level "completes" it. (An 11th Bard level would also reach ESL 11 — but Wizard is chosen because it *also* delivers Shield + scroll-scribing.)

**Payoff spell — Command (a Bard spell, powered by the Wizard's slot):** Command (L1 Enchantment, **target rolls a WIS save**; DC = Bard **CHA** + Arcane Acuity) affects **+1 target per slot level above 1st**. Spent through the newly-unlocked **Level-6 slot → up to 6 enemies** at once. Command comes from the Bard's Magical Secrets at Bard 10; the Wizard dip only supplies the 6th-level slot to upcast it.

## Spell picks for this party

### SimonSays — Swords Bard 10 / Fighter 1 / Wizard 1

The dip is not about Wizard *spells* per se — it's Shield + scribing + the L6 slot. The 6 level-up picks + 3 cantrips are a small bonus; pick low-cost utility.

**Mandatory**
- **Shield** (Lvl 1 · Abjuration · Reaction, *no save/attack*) — the marquee reason to dip. Reaction + L1 slot → **+5 AC until your next turn** and **immunity to Magic Missile**. **Must be one of the 6 level-up picks — there is no Shield scroll to transcribe.** ⚠️ Upcasting gives no extra benefit; DC-independent so INT doesn't matter here.

**Recommended** (fill the remaining 5 initial L1 picks + 3 cantrips; all optional, re-preppable, remember only ~4 Wizard prep slots)
- **Magic Missile** (Lvl 1 · Evocation · *auto-hit, force, no save*) — reliable chip and a dependable concentration-breaker; damage is INT-independent, so it stays useful at INT 16.
- **Grease** (Lvl 1 · Conjuration · DEX save) — cheap prone/control if a low slot is idle. ⚠️ save DC keys off INT, so weaker than the Bard's CHA control.
- **Fog Cloud** (Lvl 1 · Conjuration · *no save*) — vision denial / disengage cover; pairs with the party's stealth pieces.
- **Longstrider** (Lvl 1 · Transmutation · *no save*) — permanent +movement out-of-combat buff.
- **Disguise Self** (Lvl 1 · Illusion · *no save*) — extra face/utility beyond the Bard's kit.
- **Cantrips (3):** **Mage Hand**, **Minor Illusion**, **Light** (or **Friends**) — low-impact INT-scaled utility; treat as filler, not a damage source.
- **Later via scribing:** with the L6 slot online you can transcribe Wizard scrolls up to **Level 6** (available to buy from char lvl 9) into the spellbook — a cheap way to bank niche Wizard-list utility the Bard can't learn. ⚠️ Bounded by the 4 prep slots and the full 50 gp/level cost (no school discount without a subclass).
