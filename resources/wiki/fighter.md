# Fighter — BG3 progression & spell reference

> Sources: [bg3.wiki](https://bg3.wiki/wiki/Fighter) + local KB (`party_plan.json`). Patch 8, non-Honour mode. Used as a **1-level dip** by **Batman (Config B)** — Arcane Trickster Rogue 11 / Fighter 1 — and **SimonSays** — Swords Bard 10 / Fighter 1 / Wizard 1. Role: Archery fighting style, martial/armour proficiency, and (for SimonSays only — see below) CON save proficiency.

## Spellcasting

**Fighter is a NON-caster at the dip level.** A Fighter gains no spells, no cantrips, and no spell slots at levels 1 or 2. Spellcasting only appears if you take the **Eldritch Knight** or **Arcane Archer** subclass, and that choice does not happen until **Fighter level 3** — neither build reaches it. So the Fighter dip contributes **zero** to either character's spell list.

- **No spellcasting ability of its own.** The base Fighter class has no defined spellcasting ability. BG3 falls back to a default (Intelligence for custom characters and for the Astarion/Dark Urge/Gale/Karlach/Lae'zel origins) for using scrolls, wands, and other item-based casting. ⚠️ For a multiclassed character whose *most recently taken* class is Fighter (or Rogue), the game instead uses the **next most recent** class's spellcasting ability for item/scroll DCs.
  - **Batman (Config B):** his real casting comes from the Arcane Trickster subclass, which *does* define **Intelligence** as its spellcasting ability — so AT spells (Shield, Disguise Self, Shadow Blade) and stolen scrolls all key off **INT**. The Fighter dip changes none of this; it is only taken for Archery. This is exactly why Config B is "single-stat INT."
  - **SimonSays:** Bard spells key off **Charisma**; the Wizard dip's spells/scribing key off **Intelligence**. The Fighter level provides no casting and no casting stat.
- **Known / prepared / scribe:** not applicable — the Fighter dip grants none of these. (Batman's AT is a *known*-spell caster on the Rogue side; SimonSays's Bard is *known* and the Wizard dip *scribes*. All out of scope for this file.)
- **Level-up spell replacement:** not applicable to the Fighter dip (no spells to learn or replace).

## Level-by-level

Both builds take **only Fighter 1**, so that is the load-bearing row. Deeper rows are included as BG3-accurate context (why you would *not* go further, and where the usual milestones fall) but are **not taken** by either build.

| Class Lvl | Features gained | New spell slots | Spells you may add / replace | Cantrips |
|---|---|---|---|---|
| **1 (the dip)** | **Fighting Style** (pick **Archery** = +2 to attack rolls with ranged weapons); **Second Wind** (bonus action, heal 1d10 + Fighter level, recharge on short rest). Proficiencies — see the two cases below. | None | None | None |
| 2 *(not taken)* | Action Surge (extra Action, 1/short rest) | None | None | None |
| 3 *(not taken)* | **Choose a subclass** (Arcane Archer / Battle Master / Champion / Eldritch Knight) — subclass, and any subclass spellcasting, begins here | None | Eldritch Knight only | Eldritch Knight only |
| 4 *(not taken)* | **Feat** | None | — | — |
| 5 *(not taken)* | **Extra Attack** (a 2nd attack per Attack action) | None | — | — |

Feat levels within the Fighter class are **4, 6, 8, 12** (Fighter uniquely gets a bonus feat at 6). ⚠️ BG3 feats are gated by *class* level, so a 1-level Fighter dip grants **no feat** — both builds get their feats from their Rogue / Bard levels instead.

### Proficiencies granted by the dip — depends on turn order (critical)

BG3 rule (bg3.wiki): **only the first class you take grants saving-throw proficiencies, and multiclassing never grants heavy-armour proficiency or skill proficiencies.** So the same "Fighter 1" gives different things to the two builds:

- **SimonSays — Fighter is the FIRST class after the respec** (`respec at 8 → Fighter 1 → Wizard 1 → Swords Bard 1–10`). As a first class, Fighter 1 grants the full package:
  - **Saving-throw proficiency: Strength + Constitution** ✓ (this is the CON save the build wants — helps concentration on Hold Monster / Confusion / Fear).
  - **Armour:** Light, Medium, **Heavy**, and Shields. **Weapons:** Simple + Martial (longbow proficiency included).
  - **Skills:** choose **2** from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, Survival.
  - ⚠️ **Trade-off:** because Fighter is now the first class, it *replaces* the Bard's normal **Dexterity + Charisma** save proficiencies with **Strength + Constitution**. SimonSays gains CON (concentration) but loses CHA save proficiency. This is the deliberate reason to slot Fighter first.

- **Batman (Config B) — Fighter is a MULTICLASS** taken at character level 2 (`Rogue 1 → Fighter 1 → Rogue 2–11`). As a non-first class, Fighter 1 grants **only**:
  - **Fighting Style (Archery)** and **Second Wind**.
  - **Armour:** Light, **Medium**, Shields. **Weapons:** Simple + Martial. (**No Heavy armour** — multiclassing never grants it.)
  - ⚠️ **NO Constitution save proficiency.** Batman's saves stay **Dexterity + Intelligence** (from Rogue, his first class). The "CON save proficiency" listed for Batman in `party_plan.json` (char-level-2 row) is **incorrect** — multiclassing into Fighter cannot grant it. In practice it doesn't matter much: Batman's Act 3 **Amulet of Greater Health** already grants advantage on CON saves. ⚠️ Also **no skill proficiencies** from this dip (multiclass Fighter grants none), contrary to a first-class Fighter.

## Spell picks for this party

Fighter contributes **no spells or cantrips** to either character, so there is nothing to "pick" on the Fighter side. The mandatory/recommended lists below therefore cover the **non-spell dip choices** the Fighter level actually forces (Fighting Style, and for SimonSays the 2 skills) — the load-bearing decisions of the dip.

### Batman (Config B)

**Mandatory**
- **Fighting Style: Archery** (Fighter Lvl 1 · passive · no save) — +2 to ranged attack rolls; the entire reason for the dip on a hand-crossbow sniper (Ne'er Misser + Hellfire Hand Crossbow). Take at char level 2.
- **Second Wind** (Fighter Lvl 1 · bonus-action self-heal · no save) — comes free with the level; a minor emergency heal (1d10 + 1) for the frail assassin, on a short rest.

**Recommended**
- Nothing further from Fighter — the build intentionally stops at Fighter 1. ⚠️ Do **not** expect a CON save proficiency or heavy armour from this dip (see above); Batman goes armour-light anyway (Bracers of Defence, +2 AC with no armour).

### SimonSays

**Mandatory**
- **Fighting Style: Archery** (Fighter Lvl 1 · passive · no save) — +2 to ranged attack rolls for the ranged Slashing-Flourish acuity engine (Hellrider's Longbow → Gontr Mael).
- **Take Fighter as the FIRST class in the respec** — this is what delivers the **Strength + Constitution saving-throw proficiency** (CON = concentration insurance for the control spells) plus full armour/martial proficiency. If Fighter is not slotted first, the CON save is lost. ⚠️ Accepts the loss of the Bard's default CHA save proficiency.

**Recommended**
- **Fighter skills (choose 2)** (Fighter Lvl 1 · no save) — pick from the Fighter list; **Perception** and **Athletics** (or **Insight** for a face) are the strongest utility picks, and they don't overlap the Bard's Expertise skills.
- **Second Wind** (bonus-action self-heal) — free with the level; a small panic-button heal that scales with Fighter level (only +1 here).

## Uncertainties (⚠️ summary)
- ⚠️ `party_plan.json` lists "CON save proficiency" as a Fighter-dip benefit for **Batman (Config B)**; this is **wrong** because Fighter is multiclassed after Rogue 1 — corrected above.
- ⚠️ SimonSays's CON save proficiency is **contingent on taking Fighter first** in the level-8 respec, which the build order specifies; it also costs the Bard's CHA save proficiency.
- ⚠️ Item/scroll spell DCs for a Fighter-most-recent multiclass fall back to the previous class's stat; for Batman the Arcane Trickster subclass pins this to INT regardless, so no practical issue.
