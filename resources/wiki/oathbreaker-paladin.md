# Oathbreaker Paladin — BG3 progression & spell reference

> Source: bg3.wiki (Paladin, Oathbreaker, Divine Smite, individual spell pages) + local KB (`party_plan.json`). Patch 8, non-Honour mode. Used by **Durc** (Oathbreaker Paladin 7 / Hexblade Warlock 5, Half-Orc Dark Urge) — role: prepared CHA caster, Divine Smite platform, aura anchor (Protection + Hate).

This doc covers the **Paladin (Oathbreaker) side only**, class levels 1–7 (the depth Durc takes). Warlock/Pact-Magic mechanics live in the Warlock reference; where they change the numbers they're flagged.

## Spellcasting

- **Spellcasting ability: Charisma.** Spell Save DC and spell attack rolls use the CHA modifier. CHA also powers Aura of Protection, Aura of Hate, and Channel Oath DCs.
- **Prepared caster, NOT a known caster.** A Paladin automatically has access to the *entire* Paladin spell list (up to the spell levels it can cast) the moment a level is taken — you never "learn" a fixed set and there is **no Replacement-Spell mechanic to worry about**. Instead you **prepare** a limited subset, and you may **swap your prepared spells freely at any time out of combat**. (Contrast: Warlock/Bard/Sorcerer are *known* casters that replace one spell per level-up; the Paladin side ignores all of that.)
- **Number prepared = Paladin level + CHA modifier** (minimum 1). This uses the **Paladin class level**, not character level. For Durc: at Paladin 2 with CHA 17 (+3) → 5 prepared; scaling to Paladin 7 with CHA 20 (+5) → **12 prepared**. ⚠️ The exact count moves as CHA climbs 17→18 (Hag's Hair)→20 (Mirror of Loss).
- **Oath spells are "Always Prepared" and do NOT count against that limit** — they're free extras granted by the Oathbreaker subclass.
- **No cantrips.** Paladin is one of the classes that gets **zero cantrips** at every level. Durc's only cantrip-like at-will options come from the Warlock side (e.g. any Warlock cantrip / Eldritch Blast), not the Paladin.
- **No scribing.** Paladins cannot scribe scrolls into a spellbook (that's Wizard-only).
- **Spellcasting starts at Paladin 2**, not Paladin 1 — Paladin 1 is a **non-casting dip** (Divine Sense, Lay on Hands, Channel Oath, oath choice only).
- **Divine Smite is a feature, not a prepared spell.** From Paladin 2 you can dump *any* available spell slot into a melee hit for radiant damage; it does not occupy a prepared-spell slot and is unaffected by anti-spell effects (Counterspell, etc.). It can be set to fire automatically on hit/crit via the Reactions menu.

## Level-by-level

Durc takes **Paladin to 7** (character levels 2, 3, 8, 9, 10, 11, 12 in the interleaved build order). Slot numbers below are the **standalone Paladin** unlocks. ⚠️ In Durc's Paladin 7 / Warlock 5 multiclass the real pool differs — see the note under the table.

| Class Lvl | Features gained | New spell slots | Spells you may add / replace | Cantrips |
|---|---|---|---|---|
| **1** (char 2) | Divine Sense, Lay on Hands (3 charges), Channel Oath (1/short rest), **choose an Oath (subclass)**. Non-casting. | none | none yet (no slots) | 0 |
| **2** (char 3) | **Spellcasting** begins; **Divine Smite**; **Fighting Style** (Defence / Duelling / Great Weapon Fighting / Protection) | 2 × L1 | L1 Paladin list unlocks: Bless, Command, Compelled Duel, Cure Wounds, Divine Favour, Heroism, Protection from Evil and Good, Shield of Faith, Searing Smite, Thunderous Smite, Wrathful Smite. Re-prepare freely (prepared = 2 + CHA mod). | 0 |
| **3** (char 8) | Divine Health; **Oathbreaker subclass features** (this build breaks its oath here → Spiteful Suffering, Control Undead, Dreadful Aspect as Channel Oath actions) | +1 → 3 × L1 | **Oath spells (always prepared, free): Hellish Rebuke, Inflict Wounds.** Prepared count = 3 + CHA. | 0 |
| **4** (char 9) | **Feat** → *Great Weapon Master* (build's one Paladin feat) | none | (re-prepare freely; prepared = 4 + CHA) | 0 |
| **5** (char 10) | **Extra Attack** | +1 L1 & +2 L2 → 4 × L1, 2 × L2 | **L2 Paladin list unlocks:** Aid, Branding Smite, Lesser Restoration, Magic Weapon, Protection from Poison. **Oath spells (always prepared, free): Crown of Madness, Darkness.** Prepared = 5 + CHA. | 0 |
| **6** (char 11) | **Aura of Protection** (allies within 3 m gain +CHA mod to all saving throws) | none | (re-prepare freely; prepared = 6 + CHA) | 0 |
| **7** (char 12) | **Aura of Hate** (Oathbreaker subclass feature — self + nearby fiends/undead gain +CHA mod to **melee weapon** damage) | +1 → 3 × L2 | (re-prepare freely; prepared = 7 + CHA) | 0 |

**Not reached (build stops at Paladin 7):** Aura of Courage would come at Paladin 10, **Improved Divine Smite** (+1d8 radiant on every melee hit) at Paladin 11, the L3 oath spells **Bestow Curse + Animate Dead** at Paladin 9, and the L3 Paladin list (Blinding Smite, Crusader's Mantle, etc.) also at Paladin 9. Durc gets **none** of these — its L3 spell *slots* come only from the Warlock side.

⚠️ **Multiclass slot reality (Paladin 7 / Warlock 5).** BG3 sizes the shared pool by **effective spellcaster level (ESL) = the *summed fractional* level of every spellcasting class, floored *once* at the end** — you do **not** floor each class on its own. A half-caster contributes `level ÷ 2` as a fraction (Paladin 7 → 3.5). Warlock **Pact Magic is excluded from ESL** (it's a separate pool), so Paladin is Durc's only contributor → ESL = `floor(3.5) = 3` → about **4 × L1 + 2 × L2** shared slots (usable for Paladin spells *and* Divine Smite). The per-class-floor shortcut only happens to match here because there's a single contributor; pair two odd-level partial casters and it under-counts. Warlock Pact Magic adds **2 × L3 slots** at Warlock 5 on a short-rest recharge, which can also fuel Divine Smite — this is where the nova's L3 (4d8-base) smites come from. Verify exact totals in-game / in the Warlock reference.

⚠️ **Subclass timing.** Oathbreaker is the one Paladin subclass **not selectable at character creation**. You pick a normal oath at Paladin 1, then *break* it (via an oath-breaking action) to convert; the Oathbreaker Knight appears at camp to induct you. The build does this at **Paladin 3 (char 8)**, so all Paladin-3-level Oathbreaker features arrive together. Restoring the oath costs escalating gold (1000 → 2000 → 10000), and **Withers will not respec an active Oathbreaker** until the oath is restored.

⚠️ **Extra Attack stacking.** Paladin 5 grants Extra Attack; Durc *also* has Warlock's Thirsting Blade (Deepened Pact) for a 2nd attack. The plan's "3 attacks" relies on these stacking, which the party doc flags as a **non-Honour-only** interaction — treat the stack as a build assumption, not a vanilla guarantee. (Detail belongs to the Warlock reference.)

## Spell picks for this party

### Durc — Oathbreaker Paladin 7 / Hexblade Warlock 5

Durc is a **smite platform**, not a spell-slinger: nearly every slot is spent as Divine Smite rather than on a cast spell. Prepared spells matter mainly as (a) the one concentration rider used in the nova and (b) cheap pre-buffs. Concentration is the bottleneck — you can hold only one of Wrathful Smite / Bless / Divine Favour / Shield of Faith at a time.

**Mandatory**

- **Divine Smite** (class feature at Paladin 2 · not a prepared spell · Radiant, no save — melee attack roll only) — the core. Expend a slot on a melee hit: **2d8** radiant at L1, **+1d8 per slot level above 1st (cap 5d8 at an L4 slot)**, plus **+1d8 vs Fiends/Undead**. Dice **double on a crit**, which is the whole nova. Set the *Critical Hit* Divine Smite reactions to auto-confirm so every crit smites. Not blocked by Counterspell.
- **Wrathful Smite** (Lvl 1 · Evocation · attack roll + **WIS save** to avoid Frighten) — the one prepared spell in the nova line: adds **1d6 psychic** (doubles to 2d6 on a crit) and can Frighten. Concentration; cast it once and it rides subsequent swings. Also available from the Hexblade side, so it's covered either way.

**Recommended**

- **Bless** (Lvl 1 · Enchantment · no save · concentration) — +1d4 to attack rolls and saves for up to 3 allies; best pre-fight buff on turns you aren't riding Wrathful Smite.
- **Divine Favour** (Lvl 1 · Evocation · no save · concentration, bonus action) — +1d4 radiant to **every** weapon hit; strong on a multi-swing nova turn, but competes with Wrathful Smite/Bless for concentration.
- **Shield of Faith** (Lvl 1 · Abjuration · no save · concentration) — +2 AC for the frontliner when you don't need an offensive concentration spell.
- **Command** (Lvl 1 · Enchantment · **WIS save**) — cheap single-target control (Drop weapon / Approach / Halt) to open a nova or peel a caster.
- **Hellish Rebuke** (Lvl 1 · Evocation · **DEX save**, half on save · reaction, 2d10 fire) — free **always-prepared** Oathbreaker oath spell; reaction damage when hit. Zero prepared-slot cost.
- **Crown of Madness** (Lvl 2 · Enchantment · **WIS save**) and **Darkness** (Lvl 2 · Evocation · no save) — free **always-prepared** Oathbreaker oath spells from Paladin 5; situational control / vision-denial that cost you nothing to keep. ⚠️ Darkness works against Durc unless paired with Devil's Sight (which Durc has from the Warlock side).
- **Spiteful Suffering** (Channel Oath, not a spell · **CHA save** · 1d4+CHA necrotic/turn, grants **advantage to all attackers** on the target) — Oathbreaker channel action; a self-sufficient advantage source for crit-fishing when the Risky Ring isn't equipped.

⚠️ Uncertainties: schools/saves for Command, Shield of Faith, Divine Favour, Crown of Madness, Darkness, and Hellish Rebuke are stated from the Paladin/oath-spell listing and each spell's known BG3 behavior; Wrathful Smite, Bless, and Divine Smite were confirmed directly on their bg3.wiki pages. Multiclass slot totals and the Extra-Attack stack are build assumptions flagged above.
