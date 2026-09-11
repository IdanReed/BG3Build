# Draconic Bloodline (Blue) Sorcerer — BG3 progression & spell reference

> Sources: bg3.wiki (Sorcerer, Draconic Bloodline, Tempest Domain, and per-spell pages) + local KB (`party_plan.json`). Scope: **Patch 8, non-Honour**. Party member using it: **Toaster** — "The Shock Bottle", Draconic-Blue **Sorcerer 10 / Tempest Cleric 2**, the party's Wet+Lightning AoE nuke and Twinned-Haste engine.

## Spellcasting

- **Ability:** Charisma. Spell Save DC and Spell Attack both use CHA (target 17 → 20 via Hag's Hair + Mirror of Loss).
- **Known, not prepared (Sorcerer side).** Sorcerer spells are *learned* on level-up and cannot be freely re-picked afterward. **On each level-up you may replace exactly 1 known spell** with another Sorcerer spell ("Replacement Spell (Optional)"). Cantrips, once chosen, are permanent (no replacement).
- **The Tempest Cleric dip is a *prepared* caster.** Cleric spells key off **Wisdom** (Toaster's WIS is only ~12), and prepared Cleric spells can be re-chosen freely out of combat. The dip is taken for no-save utility/reactions (Create Water, Destructive Wrath, Wrath of the Storm), not for WIS-save spells. ⚠️
- **Subclass is chosen at Sorcerer level 1** (character creation), not later. Blue ancestry → **Lightning** and grants **Witch Bolt** as a free bonus known spell (does not cost a "spell known" pick).
- **Counts (single-class Sorcerer):**
  - **Cantrips known:** 4 at level 1 → 5 at Sorc 4 → 6 at Sorc 10.
  - **Spells known:** 2 at level 1, +1 every Sorcerer level → **11 known at Sorc 10** (Witch Bolt is extra, on top of this).
- **Metamagic:** choose **2** at Sorc 2, **+1** at Sorc 3, **+1** at Sorc 10 (4 total by Sorc 10). At Sorc 2 only Careful / Distant / Extended / Twinned are available; **Heightened, Quickened, Subtle unlock at Sorc 3**. Build picks Twinned + Extended (Sorc 2), Quickened (Sorc 3); the Sorc-10 pick is free (Heightened or Careful recommended).
- **Sorcery Points** (recharge on long rest) = Sorcerer level from level 2 on; convertible to/from spell slots (Create Spell Slot / Create Sorcery Points).

## Level-by-level

Slots below are the **Sorcerer single-class** progression (this build takes all 10 Sorcerer levels first). "New spell slots" = slots gained *that* level. Feats land at Sorcerer levels **4 and 8** (BG3 grants feats at character level 4/8/12 but gated per class; since Sorcerer is taken first, char 4 = Sorc 4 and char 8 = Sorc 8). This 10/2 split gets **only 2 feats total** — the Tempest Cleric 2 dip grants no feat.

| Class Lvl | Features gained | New spell slots | Spells you may add / replace | Cantrips |
|---|---|---|---|---|
| Sorc 1 | Spellcasting (CHA); **choose subclass → Draconic Bloodline (Blue/Lightning)**; Draconic Resilience (unarmored AC = 13 + DEX, no stack with Mage Armour) + **+1 HP per Sorcerer level**; free **Witch Bolt** | 2× L1 | Pick 2 known spells (+ free Witch Bolt) | Pick 4 |
| Sorc 2 | **Metamagic: choose 2** (→ Twinned, Extended); Create Spell Slot; Create Sorcery Points | +1 L1 (→3) | +1 (→3 known); may replace 1 | 4 |
| Sorc 3 | **Metamagic: choose 1** (→ Quickened) | +1 L1 (→4), +2 L2 | +1 (→4); may replace 1 | 4 |
| Sorc 4 | **Feat → War Caster** (advantage on Concentration saves; Shocking Grasp as opportunity reaction) | +1 L2 (→3) | +1 (→5); may replace 1 | +1 (→5) |
| Sorc 5 | 3rd-level spells unlock (Haste, Lightning Bolt, Counterspell, Fireball, Slow, Hypnotic Pattern…) | +2 L3 | +1 (→6); may replace 1 | 5 |
| Sorc 6 | **Subclass: Elemental Affinity** — Damage (add CHA mod to Lightning spell damage) + Resistance (spend 1 Sorcery Point → Lightning resistance until long rest) | +1 L3 (→3) | +1 (→7); may replace 1 | 5 |
| Sorc 7 | — | +1 L4 | +1 (→8); may replace 1 | 5 |
| Sorc 8 | **Feat → Elemental Adept: Lightning** (spells ignore Lightning resistance; can't roll a 1 on Lightning damage). ⚠️ Redundant +2 CHA is the alt only if CHA isn't already capped by Hag's Hair + Mirror | +1 L4 (→2) | +1 (→9); may replace 1 | 5 |
| Sorc 9 | 5th-level spells unlock (Cone of Cold, Hold Monster, Cloudkill…) | +1 L4 (→3), +1 L5 | +1 (→10); may replace 1 | 5 |
| Sorc 10 | **Metamagic: choose 1** (4th total; e.g. Heightened / Careful) | +1 L5 (→2) | +1 (→11); may replace 1 | +1 (→6) |
| — Tempest Cleric 1 (char 11) | *Different class.* Heavy armour + martial weapons + shields; **Wrath of the Storm** (2d8 reaction retaliation); Cleric spellcasting (**WIS**); domain spells always prepared; **Create Water** now preparable | Reaching caster level 11 adds **1× L6** slot | Prepared Cleric spells (WIS) — re-pick freely | — |
| — Tempest Cleric 2 (char 12) | **Channel Divinity: Destructive Wrath** (maximize a Thunder/Lightning damage roll for 1 charge); Amulet of the Devout adds a 2nd charge | No new slots (caster level 12 = same L1–L6 as 11: **4/3/3/3/2/1**) | Prepared Cleric spells (WIS) | — |

**Final slot line (Sorc 10 / Tempest 2 = caster level 12):** L1×4, L2×3, L3×3, L4×3, L5×2, **L6×1**. The lone L6 slot has no known 6th-level Sorcerer spell at Sorc 10, so it is used to **upcast** (e.g. Lightning Bolt) — Chain Lightning is delivered by Markoheshkir instead (see below). ⚠️
The **Sorc-11 Draconic subclass feature** is never reached (build caps Sorcerer at 10); its exact BG3 identity is not verified here. ⚠️

## Spell picks for this party

### Toaster — Draconic-Blue Sorcerer 10 / Tempest Cleric 2

**Mandatory**
- **Witch Bolt** (Lvl 1 · Evocation · attack roll, 1d12 Lightning, Concentration) — *auto-granted free by Blue ancestry at Sorc 1.* Early lightning + builds Lightning Charges on The Spellsparkler; re-activate each turn (guaranteed, no roll). Works with Destructive Wrath.
- **Chromatic Orb: Lightning** (Lvl 1 · Evocation · attack roll, 2d8 Lightning) — learn early. Creates an **Electrified Water** surface, upcasts +1d8/level, and triggers Destructive Wrath; a cheap single-target lightning hit that also sets up the Wet/electrify combo.
- **Lightning Bolt** (Lvl 3 · Evocation · **DEX save**, 8d6 Lightning line) — learnable at **Sorc 5**. The main AoE nuke: doubled vs **Wet** targets, maximized by **Destructive Wrath**, and boosted by Elemental Affinity + Elemental Adept.
- **Haste** (Lvl 3 · Transmutation · no save, Concentration, single-target) — learnable at **Sorc 5**. Single-target so it is **Twinnable**; Twinned Haste (3 Sorcery Points) on the Paladin is the party's "Haste engine". Never cast a second Concentration spell after it (drops Haste → Lethargic).
- **Counterspell** (Lvl 3 · Abjuration · Reaction) — learnable at **Sorc 5**. Shuts down enemy casters; upcast to beat higher-level spells without a check.
- **Create Water** (Lvl 1 · Transmutation · no save, applies **Wet** = Lightning/Cold vulnerability) — **NOT on the Sorcerer list**; obtained via the **Tempest Cleric dip** (Cleric level 1, prepared). The Wet setup that doubles the whole lightning package. ⚠️ Do not expect to "know" it as a Sorcerer.

**Recommended**
- **Shocking Grasp** (Cantrip · Evocation · melee spell attack, 1d8→2d8 at char 5→3d8 at char 10, Lightning) — best lightning cantrip: strips the target's Reactions, advantage vs metal armour, and scales with Potent Robe (+CHA to cantrip damage), Elemental Affinity, Spellmight Gloves, Markoheshkir. Also the payload for War Caster's opportunity spell.
- **Cone of Cold** (Lvl 5 · Evocation · DEX save, 5d8 Cold) — the Sorc-9/10 fifth-level nuke. Off-element for Elemental Adept: Lightning, but **Wet gives Cold vulnerability too**, so it still doubles; strong when you want AoE that isn't the lightning line.
- **Fireball** (Lvl 3 · Evocation · DEX save, 8d6 Fire) — flexible AoE for fire-vulnerable / non-Wet packs; off-type (no Elemental Affinity/Adept synergy), so a situational pick, not the core.
- **Misty Step** (Lvl 2 · Conjuration · Bonus Action) and/or **Fly** — mobility/repositioning out of your own electrified water.
- **Enhance Ability / Hypnotic Pattern** (Lvl 2 / Lvl 3 · Illusion · WIS save) — optional control if you want more than damage; the Bard is the primary controller, so low priority.
- **Chain Lightning** (Lvl 6 · Evocation · DEX save, 10d8 Lightning) — **not learnable at Sorc 10** (Sorcerer gets it at class level 11). Toaster accesses it through **Markoheshkir** (Kereska's Favour → Bolts of Doom: cast Chain Lightning + Lightning Bolt once each per short rest) or from scrolls. ⚠️
- **Metamagic use:** Twinned → Haste; Extended → double surface/Witch Bolt/Slow duration; Quickened → bonus-action nuke (cast a leveled spell + a cantrip same turn); Sorc-10 pick → Heightened (disadvantage on the target's save) or Careful (spare allies from your AoE).
- **Glyph of Warding** (Lvl 3 · Abjuration · DEX save, 5d8 of chosen element) — the plan lists this for Toaster, but it is **NOT a Sorcerer spell** (Bard/Cleric/Wizard only, at class level 5) and the Cleric dip only reaches level 2, so **this build can only cast it from scrolls**, not learn it. ⚠️
