# Swords Bard — BG3 progression & spell reference

> Sources: bg3.wiki (Bard, College of Swords, and per-spell pages) + local party KB (`party_plan.json`). Patch 8, non-Honour. Used by **SimonSays** ("The Commander") — build **Swords Bard 10 / Fighter 1 / Wizard 1**, role: control + damage + party face.

## Spellcasting

- **Spellcasting ability: Charisma.** All Bard spells use CHA for Spell Save DC and spell attack rolls. (The Wizard-dip spells instead use **Intelligence** — they are Wizard-class spells.)
- **Known caster, not a prepared caster.** Bards learn a fixed, growing set of *Spells Known*; those spells are then **Always Prepared** (castable at any time, no daily re-pick). You do **not** re-choose your list each long rest the way a Cleric/Druid/Wizard does. (BG3 note: "Bards know fewer spells at low levels" in exchange for always-prepared.)
- **Level-up replacement:** on **every** Bard level-up you may **replace exactly 1 known Bard spell** with another from the Bard list (optional). This is the only way to swap a Bard spell after learning it. ⚠️ Once learned and not replaced at that level-up, a Bard spell is locked in until a future level-up (or a full respec with Withers).
- **Counts at the levels this build hits:**
  - Bard 1: **2 cantrips**, **4 spells known**.
  - Bard 4: **3 cantrips** (spells known 7).
  - Bard 10: **4 cantrips**, **13 Bard-list spells known** **+ 2 Magical Secrets picks = 15 total known**. ⚠️ Magical Secrets is presented as a separate pick in the level-up UI, on top of the 13 in the class table.
- **Multiclass dips:**
  - **Fighter 1 — NON-casting dip.** Grants a Fighting Style (take **Archery** for the ranged flourishes/bow), Second Wind, CON-save proficiency, and martial-weapon/all-armour/shield proficiency. **No spell slots, no spells.**
  - **Wizard 1 — full-caster dip (INT).** Grants a spellbook; you learn Wizard cantrips + level-1 spells and can **scribe scrolls** into the book. Its spells (e.g. **Shield**) key off Intelligence, and unlike Bards a Wizard **re-prepares** freely each long rest.
- **Spell slots are pooled by combined caster level.** Bard 10 (full) + Wizard 1 (full) = **caster level 11**; Fighter 1 contributes 0. ⚠️ Caster level 11 yields slots **4 / 3 / 3 / 3 / 2 / 1** — the single **6th-level slot** exists only because of the Wizard dip (pure Bard 10 tops out at 5th-level slots). That L6 slot is what lets **Command** hit up to 6 targets.

## Level-by-level

Table is by **Bard class level** (the class this build takes 10 of). "New spell slots" are the *pure-Bard* additions at that level; see the Spellcasting note for the real multiclass total. Dips (Fighter 1, Wizard 1) are listed under the table.

| Class Lvl | Features gained | New spell slots | Spells you may add / replace | Cantrips |
|---|---|---|---|---|
| Bard 1 | Spellcasting (CHA), Bardic Inspiration (d6) | 2× L1 | Pick your initial **4** known spells (all L1) | **2** |
| Bard 2 | Song of Rest, Jack of All Trades | +1× L1 (→3) | +1 known (→5); may replace 1 | 2 |
| Bard 3 | **College of Swords** (Blade Flourish — Defensive/Slashing/Mobile; **Fighting Style**: Duelling *or* Two-Weapon; Medium-armour + Scimitar prof), **Expertise** (2 skills) | +1× L1 (→4), +2× L2 | +1 known (→6); **L2 spells unlock**; may replace 1 | 2 |
| Bard 4 | **Feat #1** (build: Sharpshooter) | +1× L2 (→3) | +1 known (→7); may replace 1 | **3** (+1) |
| Bard 5 | Font of Inspiration, Improved Bardic Inspiration (**d8**) | 2× L3 | +1 known (→8); **L3 spells unlock**; may replace 1 | 3 |
| Bard 6 | **Extra Attack** (subclass), Countercharm | +1× L3 (→3) | +1 known (→9); may replace 1 | 3 |
| Bard 7 | — | 1× L4 | +1 known (→10); **L4 spells unlock**; may replace 1 | 3 |
| Bard 8 | **Feat #2** (build: Dual Wielder / +2 CHA) ⚠️ | +1× L4 (→2) | +1 known (→11); may replace 1 | 3 |
| Bard 9 | — | 1× L5 | +1 known (→12); **L5 spells unlock**; may replace 1 | 3 |
| Bard 10 | **Magical Secrets** (2 non-Bard spells, up to L5), **Expertise** (2 more skills), Improved Bardic Inspiration (**d10**) | +1× L5 (→2) | +1 Bard known (→13) **+ 2 Magical Secrets** = **15 total**; may replace 1 Bard spell | **4** (+1) |

**Dips (character-level detour, per the build's respec order Fighter 1 → Wizard 1 → Bard 1–10):**
- **Fighter 1:** Archery Fighting Style, Second Wind, CON-save prof, martial/heavy-armour/shield prof. Non-casting.
- **Wizard 1:** Wizard spellbook + scroll-scribing (INT); pick up **Shield** (and optional utility). Bumps combined caster level to 11 → unlocks the **L6 slot**.

⚠️ **Feat-level correction:** Bard feats/ASIs land at **Bard class levels 4, 8, 12**. This build reaches Bard 10, so it gets exactly **two** Bard feats — at **Bard 4** and **Bard 8**. `party_plan.json` labels the second feat "Bard 10," which is incorrect; it triggers at **Bard 8**. (Fighter 1 and Wizard 1 grant no feats — those are at Fighter 4 / Wizard 4.)

⚠️ **Extra Attack:** granted by College of Swords at **Bard 6** (confirmed). It does not stack with any other Extra Attack, but there's only Fighter 1 here (no Fighter Extra Attack), so the Bard makes **2 weapon attacks** per Attack action. With **Slashing Flourish (Ranged)** each attack can hit up to 2 enemies, which is how the build stacks Arcane Acuity fast (each *hit* = +2 acuity → +spell save DC). ⚠️ Firing two flourishes in one turn relies on Extra Attack treating the flourish as one of your attacks; each flourish costs a Bardic Inspiration on hit.

## Spell picks for this party

### SimonSays — Swords Bard 10 / Fighter 1 / Wizard 1 ("The Commander")

All the WIS-save enchantment/illusion controls below scale with **CHA + the Helmet of Arcane Acuity** stacking spell save DC, so they land near-unresistably once acuity is up; **Command** is then delivered as a **bonus action** via the Band of the Mystic Scoundrel after a weapon hit.

**Mandatory** (the build's named picks)

- **Glyph of Warding** (Lvl 3 · Abjuration · **DEX save**) — pre-placed AoE burst (5d8, pick an element); add at **Bard 5** when L3 slots open. Best set before a fight since it's a ground trap.
- **Fear** (Lvl 3 · Illusion · **WIS save**) — 9m cone; frightened enemies drop weapons and can't act/approach. Add at **Bard 5+**. Concentration.
- **Confusion** (Lvl 4 · Enchantment · **WIS save**) — 6m-radius scramble; enemies attack randomly/skip turns. Add at **Bard 7**. Concentration.
- **Hold Monster** (Lvl 5 · Enchantment · **WIS save**) — paralyse; attacks from within 3m are **auto-crits** (this is the party's melee auto-crit engine for Durc's smites). Add at **Bard 9**; upcast adds +1 target per slot above 5th. Concentration.
- **Command** (Lvl 1 · Enchantment · **WIS save**) — **Magical Secrets pick at Bard 10** (not a base Bard spell). Drop/Halt/Grovel/Flee; upcast affects +1 target per slot above 1st, so the **L6 slot from the Wizard dip = up to 6 targets**. The core bonus-action control loop.
- **Counterspell** (Lvl 3 · Abjuration · Reaction) — **Magical Secrets pick at Bard 10** (not a base Bard spell). Shuts off enemy casters; contested by slot level (no flat save).
- **Shield** (Lvl 1 · Abjuration · Reaction, **INT** via Wizard dip) — +5 AC reaction and negates Magic Missile; the survivability payoff of the Wizard 1 dip.

**Recommended** (strong flex / earlier-game controllers; use the level-up replacement to rotate in)

- **Vicious Mockery** (Cantrip · Enchantment · **WIS save**) — free psychic + disadvantage on the target's next attack, and stacks acuity-friendly control at range. Grab at Bard 1.
- **Friends** (Cantrip · Enchantment · Concentration) — **advantage on Charisma checks vs a non-hostile creature**; the face's dialogue enabler. ⚠️ Never cast on companions (they lose approval when it ends), and on higher difficulties NPCs may notice.
- **Hypnotic Pattern** (Lvl 3 · Illusion · **WIS save**) — arguably the best AoE lockdown (9m radius incapacitate); superb acuity payoff and a strong companion/alternative to Fear. Available at **Bard 5**. Concentration; breaks on damage.
- **Hold Person** (Lvl 2 · Enchantment · **WIS save**) — cheaper single-target paralyse (auto-crits within 3m) available all the way back at **Bard 3**; the early-game stand-in for Hold Monster.
- **Dominate Person** (Lvl 5 · Enchantment · **WIS save**) — turn a humanoid against its allies; available at **Bard 9** if you'd rather flex a 5th-level pick alongside Hold Monster.

⚠️ Concentration clash: Fear, Confusion, Hold Monster, Hypnotic Pattern, Hold Person, Dominate Person, and Friends are all Concentration — only one at a time. Glyph, Command, Counterspell, and Shield are not.
