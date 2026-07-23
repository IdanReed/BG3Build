# Arcane Trickster Rogue — BG3 progression & spell reference

> Sources: bg3.wiki (Rogue, Arcane Trickster, Mage Hand Legerdemain, Magical Ambush, Reliable Talent, Uncanny Dodge, Scrolls, individual spell pages) + local KB (`party_plan.json`, `research/trickster_*.txt`). Patch 8, non-Honour. Used by **Batman** (Astarion) — Arcane Trickster Rogue 11 / 1-level dip (War Cleric = Config A melee, or Fighter = Config B ranged).

## Spellcasting

- **Spellcasting ability for Arcane Trickster (AT) *class* spells = Intelligence.** This never changes — AT class spells (Shield, Disguise Self, Shadow Blade, etc.) and the AT spell-save DC / spell attack always key off INT, even when multiclassed.
- **Known vs prepared vs scribe:** AT is a **known-spell** caster. All Arcane Trickster spells are **Always Prepared** (you don't re-pick a prepared list each rest the way a Cleric/Wizard does). It does **not** scribe scrolls into a spellbook (that is Wizard-only). Cantrips + spells come from the **Wizard** spell list, restricted to **Enchantment or Illusion** school — with a few "any-school" exceptions (below).
- **Counts (by Rogue *class* level, from the AT spellcasting chart):**
  - Cantrips known: **Mage Hand (free) + 2 chosen** at Rogue 3, rising to **Mage Hand + 3** at Rogue 10.
  - Spells known: **3** at Rogue 3 → 4 (R4) → 5 (R7) → 6 (R8) → 7 (R10) → **8 at Rogue 11**.
  - At Rogue 3 you learn **2 Enchantment/Illusion spells + 1 "any-school" spell**; at Rogue 8 the spell learned may again be **any school**. All other picks must be Enchantment/Illusion.
- **Replace on level-up? Yes.** AT has a **Replacement Spell** feature: on level-up you may swap **one** known spell for another spell from the **full Wizard list** (of a level you have slots for). This — plus the two "any-school" picks — is how off-list spells such as **Shield** (Abjuration) and **Shadow Blade** (Illusion, but not on the AT auto-list ⚠️) enter your known list. ⚠️ The exact levels at which the replace option is offered aren't fully pinned here, but it is broadly available on AT level-ups from Rogue 4 on.
- **Astarion racial cantrip:** as a High Elf, Astarion knows one extra Wizard cantrip (incl. **Booming Blade**, which High Elves get at character level 1) on top of the AT counts above.
- **The dip is a spellcasting dip too:**
  - **Config A — War Cleric 1:** grants **Wisdom** casting, 3 Cleric cantrips (e.g. Guidance, Resistance) + prepared Cleric spells (Create Water, Command, etc.), medium/heavy armour, shields, martial weapons, and War Priest.
  - **Config B — Fighter 1:** grants **no** casting stat of its own, Archery fighting style, CON-save proficiency, armour/shields/martial weapons.
- **Scroll casting stat (a real, split mechanic — verified):** scrolls are a *non-class* feature, so their DC uses your **most-recently-reached-level-1 class that has a casting stat** (Rogue only "counts," at INT, once Arcane Trickster is taken; Fighter never counts).
  - **Config A:** Rogue 1 (char 1) → **War Cleric 1 (char 2)** → Rogue 2–11. The Cleric was reached at level 1 *more recently* than Rogue, so **scrolls key off WIS** while **AT class spells still key off INT**. (Plan's WIS outcome is correct; the reason is "Cleric is the newer level-1 class," not simply "Rogue first." ⚠️)
  - **Config B:** Fighter is ignored (no casting stat), so the only counting class is AT-Rogue → **everything (AT spells *and* scrolls) keys off INT.** ✅
- The class is **not** non-casting at the dip level for spell purposes, but note **AT spellcasting itself doesn't come online until Rogue 3** (character level 4 in this build). At character levels 1–3 you have no AT spells yet (only the dip's casting, if Config A).

## Level-by-level

Table is by **Rogue class level** (the levels this build actually takes: Rogue 1–11). The single dip level is a *different* class and is noted below the table. "New spell slots" = the delta gained that level (AT is a 1/3 caster). ⚠️ In BG3 multiclassed casters **pool** their slots, so Config A's War Cleric dip adds full-caster slot levels to the shared pool — your real L1/L2 slot totals run a little above the pure-AT numbers here; Config B's Fighter adds none.

| Class Lvl | Features gained | New spell slots | Spells you may add / replace | Cantrips |
|---|---|---|---|---|
| Rogue 1 | Expertise (2 skills — Sleight of Hand + Stealth), Sneak Attack (melee & ranged) **1d6**. *Take Rogue first so scrolls/Sneak lock in correctly.* | — (no AT casting yet) | — | — (Astarion's High Elf racial cantrip is chosen here, separate from AT) |
| Rogue 2 | Cunning Action: **Dash / Disengage / Hide** (bonus-action Hide arms Sneak Attack + later Magical Ambush) | — | — | — |
| Rogue 3 | **Arcane Trickster** subclass: **Mage Hand Legerdemain** (Mage Hand becomes invisible + permanent) + spellcasting begins. Sneak **2d6** | **2 × L1** | **Learn 3:** 2 Enchantment/Illusion (e.g. **Disguise Self**, Sleep/Colour Spray) + **1 any-school** (take **Shield**) | **Mage Hand (free) + pick 2** (e.g. **Booming Blade**, Minor Illusion) |
| Rogue 4 | **Feat** (Config A: **Savage Attacker**; Config B: **Sharpshooter**) | +1 L1 (→ **3 × L1**) | +1 (Ench/Illusion); may **replace 1** | — |
| Rogue 5 | **Uncanny Dodge** (reaction: halve a hit's damage). Sneak **3d6** | — (3 × L1) | may replace 1 | — (Booming Blade's thunder rider upgrades at **character** lvl 5) |
| Rogue 6 | **Expertise** (2 more skills — Perception + Investigation) | — | may replace 1 | — |
| Rogue 7 | **Evasion** (DEX-save spells → 0 dmg on success). Sneak **4d6**. **L2 slots unlock** | +1 L1 (→ **4 × L1**) + **2 × L2** | +1 (now up to L2 — **replace into Shadow Blade** here) | — |
| Rogue 8 | **Feat** (Config A: **+2 WIS → 17**; Config B: **Alert**) | — | +1 — **this pick may be any school** | — |
| Rogue 9 | **Magical Ambush** (while **Hiding**, targets have **Disadvantage on saves vs your spells**). Sneak **5d6** | — | may replace 1 | — |
| Rogue 10 | **Feat** (Config A: **Dual Wielder** or Alert; Config B: flex, e.g. +2 INT) + **3rd cantrip** | **+2 L1** (→ **6 × L1**) | +1 | **+1 chosen (→ 3 chosen)** |
| Rogue 11 | **Reliable Talent** (proficient checks can't roll under 10). Sneak **6d6** | — | +1 (→ **8 known**) | — (Booming Blade's *final* upgrade is at **character** lvl 11) |

**The dip (character level 2 in the plan):** taken *after* Rogue 1.
- **Config A — War Cleric 1:** WIS casting; 2 × L1 Cleric slots into the shared pool; 3 cantrips (Guidance, etc.) + prepared Cleric spells (Create Water, Command, Shield of Faith, …); medium/heavy armour + shields + martial weapons; **War Priest** (bonus-action weapon attacks). No feat, **no Extra Attack.**
- **Config B — Fighter 1:** **Archery** fighting style (+2 ranged attack); CON-save proficiency; armour/shield/martial proficiency. No casting stat, no feat, **no Extra Attack.**

**Things this build never gets:** **Extra Attack** (neither Rogue/AT nor a 1-level Fighter/Cleric dip grants it — single weapon action per turn, plus off-hand and Booming Blade), and **no L3+ spell slots from levels** (max native slot is L2; the L3 slot for the 3d8 Shadow Blade comes from a **Superior Elixir of Arcane Cultivation**, not from leveling). ⚠️

## Spell picks for this party

### Batman (Astarion) — Arcane Trickster 11 / 1-dip

Config A (melee Shadow-Blade, War Cleric dip) is primary; Config B (ranged sniper, Fighter dip) deltas are noted. Only the AT/dip *known* spells + the key stolen *scrolls* are listed. Save types below are verified against bg3.wiki.

**Mandatory**
- **Mage Hand** (Cantrip · Conjuration · no save) — free from Mage Hand Legerdemain at Rogue 3; invisible + permanent. Scouts, flanks to enable **Sneak Attack** out in the open, and throws water bottles to set up Wet for the Sorcerer/your cold. Core to the build both configs.
- **Booming Blade** (Cantrip · Evocation · **melee weapon attack roll**, uses DEX) — pick at Rogue 3 (Astarion also has it free as a High Elf). The once-per-turn Sneak-Attack delivery vehicle in melee; adds thunder when the target moves and scales at character level 5 & 11. Melee-relevant for Config A; Config B keeps it only as a melee backup.
- **Shield** (Lvl 1 · Abjuration · Reaction, no save) — take with the Rogue-3 **any-school** pick. +5 AC and immunity to Magic Missile; the squishy assassin's main survival button. Both configs.
- **Disguise Self** (Lvl 1 · Illusion · no save) — Rogue 3. Infiltration/skip-fights, and a fresh disguise after a botched steal. Both configs.
- **Shadow Blade** (Lvl 2 · Illusion · Bonus Action, no save) — added at Rogue 7 via **spell replacement** (⚠️ it isn't on the AT auto-list despite being Illusion, but is learnable at Rogue 7). Psychic shortsword, 2d8 (→ **3d8** upcast at L3 via the Superior Elixir), **Advantage vs targets in dim light/darkness (melee attacks)**, lasts until long rest, no concentration. Config A's main weapon (psychic → doubled by the Resonance Stone, auto-crit vs Held); Config B keeps it as a darkness/adjacency backup.

**Recommended**
- **Fog Cloud** (Lvl 1 · Conjuration · no save) — any-school/replacement pick. Self-made obscurement to Hide (arms Magical Ambush) and to feed the Eversight-Ring "Batman" darkness combo. Both configs.
- **Minor Illusion** (Cantrip · Illusion · no save) — Rogue-3 cantrip option; clusters enemies for AoE scrolls and pulls patrols. Both configs.
- **Misty Step** (Lvl 2 · Conjuration · no save) — via replacement at Rogue 7+; escape/reposition if you'd rather not lean entirely on the Night Walkers/Amulet-of-Misty-Step item copies. Both configs.
- **Hold Person** (Lvl 2 · Enchantment · **WIS save**) — control that pairs with **Magical Ambush** (disadvantage applies to the *initial* save only). Optional since the Bard owns hard control; a WIS-save spell, so best on Config A (WIS scrolls) than Config B.
- **Config A dip spells (WIS):** **Create Water** (Lvl 1 · Transmutation · no save — applies **Wet** → cold/lightning vulnerability), **Command** (Lvl 1 · Enchantment · **WIS save**), **Guidance** (Cantrip · +1d4 to ability checks — stacks with Expertise/Reliable Talent for skills). Config B loses all of these.
- **Stolen offensive scrolls (the AoE "nuker" lane; DC uses WIS in Config A / INT in Config B):**
  - **Chain Lightning** (Lvl 6 · Evocation · **DEX save** · Lightning) — true DEX-save AoE; works fully with Magical Ambush.
  - **Ice Storm** (Lvl 4 · Evocation · **DEX save** · Cold+Bludgeoning) and **Lightning Bolt** (Lvl 3 · Evocation · **DEX save** · Lightning) — the genuine **DEX-save cold/lightning** options; these, not the two below, fill the "DEX-save cold lane" the plan wants. ⚠️
  - ⚠️ **Correction:** the plan's flagship "cold-first, DEX-save" scrolls are mis-saved — **Cone of Cold** (Lvl 5 · Evocation · **CON save**, not DEX) and **Otiluke's Freezing Sphere** (Lvl 6 · Evocation · **CON save**, not DEX) are both **Constitution** saves. They're still great cold nukes and Magical Ambush still gives disadvantage on any save type, but they are **not** DEX-save scrolls, and **Evasion** (your DEX-save defense) has nothing to do with them offensively. If you specifically want DEX-save cold, use **Ice Storm / Wall of Ice** instead.
- **Config B feat/weapon note (not spells):** dual hand crossbows — **Ne'er Misser** turns your Sneak Attack into **Force** (bypasses resistances) — plus **Sharpshooter** and **Alert**; drop **Savage Attacker** (melee-only, useless on crossbows).

## Uncertainties (⚠️ recap)
- Exact AT level-ups that offer the **Replacement Spell** option (broadly available on level-up; not level-by-level verified here).
- **Shadow Blade** is obtained at Rogue 7 **via spell replacement** (not the normal AT auto-list) despite being an Illusion spell — confirmed by the spell page, but a quirk.
- Multiclass **spell-slot pooling** exact totals with the Cleric dip (Config A) — higher than the pure-AT chart, but the precise pooled numbers depend on BG3's multiclass caster table.
- Config A scroll stat = **WIS** because the War Cleric is the more-recently-reached level-1 casting class (the plan's outcome is right; its stated reason "Rogue first" is imprecise).
- **Cone of Cold** and **Otiluke's Freezing Sphere** are **CON** saves, contradicting the plan's "DEX-save cold scrolls" label.
