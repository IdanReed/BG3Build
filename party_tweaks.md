# Party Tweaks — staging

_A scratchpad of proposed build changes to fold into `content/` once the Rust migration settles. Nothing here is wired into the `content/` pipeline yet — treat it as the changelog to apply (and as the rationale for each change). Same assumptions as the main plan: **non-Honour, Patch 8 (+ hotfixes #30–#36)**. Load-bearing claims are sourced to bg3.wiki._

> When applying: the nickname changes below also rename the character files (`content/characters/durc.md → charles.md`, etc.) and every `nickname:`/cross-reference in `meta`, `party`, `loot`, and the other character docs.

---

## 0. Renames

| Old nickname | New nickname | Character (unchanged) |
|---|---|---|
| Durc | **Charles** | Dark Urge (Half-Orc) |
| Batman | **Asterion** | Astarion (High Elf / Vampire Spawn) — in-game the companion is spelled *Astarion*; keeping your spelling as the party nickname |
| Toaster | **Gale** | Gale (Human) |
| SimonSays | **Bonbon** | the Bard (hireling/custom) |

---

## 1. Charles — rush Shadow Blade + Devil's Sight for an early advantage engine

**Problem:** early Act 1 feels weak — missing a lot of attacks, and none of the party's control (Hold Person / Hold Monster) is online yet to manufacture crits, so Charles has no advantage source of his own.

**Fix:** rush the first three character levels as **Hexblade Warlock 1 → 2 → 3** to bring **Shadow Blade + Devil's Sight** online at char level 3. This is a self-contained "defense + advantage" package that doesn't depend on the rest of the party coming online.

### Why it works (sourced)

- **Shadow Blade** (L2 illusion): bonus action, **not concentration**, lasts until long rest; 2d8 psychic (→3d8 on an L3 slot at Warlock 5). Crucially, **you attack with Advantage against any target in dim light or darkness**. Warlock learns it at **class level 3**. → <https://bg3.wiki/wiki/Shadow_Blade>
- **Devil's Sight** (Warlock invocation, **class level 2**): see normally in natural *and magical* darkness to 24 m, and **immunity to the Blinded from the Darkness spell**. → <https://bg3.wiki/wiki/Devil's_Sight>
- **The combo:** stand in **Darkness** (a placed cloud, **not concentration** in BG3 — lasts ~10 turns). You see fine (Devil's Sight); enemies inside are **Blinded** → they attack at **disadvantage** (your *defense*) and your attacks against them have **advantage**, which Shadow Blade *also* grants for the dim/dark condition (your *offense*). Ranged enemies outside can't see or shoot into the cloud. → Blinded interaction: <https://bg3.wiki/wiki/Fog>
- Even without casting Darkness, huge swaths of Act 1 (Underdark, caves, night camps, dungeons) are naturally dim, so Shadow Blade is often at advantage for free. Darkness is the on-demand + defensive-bubble version.
- Bonus defense already baked in: Hexblade grants **medium armour + shields at Warlock 1**, so Shadow Blade (a one-handed shortsword) **+ shield** is a real AC body from level 1.

### Revised leveling (endpoint unchanged: Oathbreaker Paladin 7 / Hexblade Warlock 5)

Only the first five levels reorder — the L6–12 tail is identical to the current `durc.md`.

| Char | Current plan | **New (rush)** |
|---|---|---|
| 1 | Warlock 1 | **Warlock 1** — Hexblade's Curse, Bind Hexed Weapon (CHA attacks), medium armour + shield |
| 2 | Paladin 1 | **Warlock 2** — invocation: **Devil's Sight** |
| 3 | Paladin 2 (**Divine Smite**) | **Warlock 3** — Pact of the Blade + **Shadow Blade (2d8)** → *advantage engine online* |
| 4 | Warlock 2 (Devil's Sight) | **Paladin 1** — Lay on Hands |
| 5 | Warlock 3 (Shadow Blade) | **Paladin 2** — **Divine Smite** *(nova online)* |
| 6 | Warlock 4 — Feat: Savage Attacker | Warlock 4 — Feat: Savage Attacker |
| 7 | Warlock 5 — Deepened Pact (2 atk), SB 3d8 | Warlock 5 — Deepened Pact (2 atk), SB 3d8 |
| 8 | Paladin 3 — Oathbreaker | Paladin 3 — Oathbreaker |
| 9 | Paladin 4 — Feat: GWM | Paladin 4 — Feat: GWM |
| 10 | Paladin 5 — Extra Attack (3 atk) | Paladin 5 — Extra Attack (3 atk) |
| 11 | Paladin 6 — Aura of Protection | Paladin 6 — Aura of Protection |
| 12 | Paladin 7 — Aura of Hate | Paladin 7 — Aura of Hate |

**The one tradeoff:** Divine Smite slips from char 3 → char 5. Worth it — early on you have only a single short-rest pact slot to smite with anyway, so the scarce smites matter far less than *landing* attacks. Advantage roughly doubles your effective hit-and-crit rate, which is exactly the "missing a lot of attacks" complaint. By char 5 you're smiting again, now connecting far more often.

### Notes / caveats

- **Learn Darkness as a known Warlock spell** once you have L2 pact slots (Warlock 3). Warlock's known-spell count is tight, so budget it against Shield / Hex / Wrathful Smite. (Oathbreaker also gets Darkness free as an oath spell at Paladin 5 / char ~10, but that's much later.)
- Shadow Blade's advantage is **melee-only** since Patch 8 Hotfix 1 (fine — Charles is melee) and applies to both main- and off-hand. → <https://bg3.wiki/wiki/Shadow_Blade_(passive_feature)>
- The Darkness bubble **collapses vs enemies that also have Devil's Sight / truesight** (imps, some devils, Raphael) — same caveat already noted on Asterion's Eversight combo.
- This dovetails with the existing item plan: the **Shadow Blade Ring** can now go to Charles as a backup summon, and **Covert Cowl** (−1 crit while Obscured) is extra-live since he'll spend Act 1–2 fighting in the dark.

---

## 2. Bonbon — Titanstring + Giant-Strength elixirs early, dual hand crossbows once the Acuity helmet is online

**Rationale:** dual hand crossbows exist to throw *more hits per turn* to stack **Arcane Acuity fast** — but that only pays off once the **Helmet of Arcane Acuity** (Act 2, Mason's Guild) is generating stacks. In Act 1 there's no helmet, so the extra low-damage shots are wasted; a few **big Titanstring hits** are stronger.

### Early kit (Act 1)

- **Fighter 1 at character creation** for the **Archery** fighting style (+2 to ranged attack) — this offsets **Sharpshooter**'s −5 and lands the big Titanstring shots. (Taking Fighter *first* still gives the CON-save proficiency the current plan wants, with **no respec needed**.)
- **Titanstring Bow** — rare +1 **two-handed Longbow** that adds your **STR modifier to damage** (in addition to DEX, min +1, and it even boosts special-arrow riders and Sneak Attack). Zhentarim Basement, sold by Brem after *Find the Missing Shipment*. → <https://bg3.wiki/wiki/Titanstring_Bow>
- **Elixir of Giant Strength** sets STR, feeding Titanstring's bonus: **Hill Giant (STR 21, +5) → … → Cloud Giant (STR 27, +8)** per hit. (Sets STR, so Bonbon's own STR 8 is irrelevant while active; costs the one-elixir-per-rest slot.)
- Because Titanstring is two-handed you **can't dual-wield** it — but **Ranged Slashing Flourish** still fires **two projectiles**, each carrying the full Titan (+STR) and Sharpshooter (+10) bonus. With Extra Attack (Bard 6) that's a serious Act-1 burst from a single turn.

### Late pivot (Act 2 →)

Once the **Helmet of Arcane Acuity** is equipped, switch to **two hand crossbows** so every attack (main + off-hand + flourish projectiles) stacks Acuity → sky-high spell-save DC → bonus-action **Hold Monster / Command** via the **Band of the Mystic Scoundrel** (Act 3). This is the existing endgame loop in `simonsays.md`; the only change is that it's now the **Act-2+** configuration, not the Act-1 one.

### Leveling / ordering change

The current `simonsays.md` plays **pure Swords Bard 1–7, then respecs at char 8** to insert Fighter 1 / Wizard 1. The tweak: **take Fighter 1 at creation** and go Bard from there (endpoint class composition **Swords Bard 10 / Fighter 1 / Wizard 1 unchanged**). This makes the Titanstring archer real from Act 1 and removes the respec.

Suggested order: **Fighter 1 (char 1) → Wizard 1 (char 2) → Swords Bard 1–10 (char 3–12).** Breakpoints land at: College of Swords char 5, Extra Attack char 8, Hold Monster char 11, Magical Secrets + the L6 slot char 12 — the same tail the level-8 respec produced.

> ⚠ **Open decision (see bottom):** taking Fighter+Wizard first delays every Bard breakpoint ~1–2 char levels vs. playing pure Bard early. Alternative: keep Fighter at creation but **defer the Wizard 1 dip** to the very end (or drop it) so Bard breakpoints come sooner. Titanstring + Archery is the priority either way.

---

## 3. Gale — Storm Sorcery: yes to the wet-combo, and here's the fuller toolkit

You went **Storm Sorcery** (over the plan's Draconic-Blue) because the flight is fun — **Tempestuous Magic** = a bonus-action 9m fly with no opportunity attacks after *any* leveled spell, from level 1. Confirmed and validated. → <https://bg3.wiki/wiki/Tempestuous_Magic>

### Is "water + Chromatic Orb / frost cantrip" the bread and butter?

Yes — that's the correct core. **Wet** makes a target **Vulnerable to both Lightning and Cold (double damage)**; if they were already resistant, Wet cancels the resistance instead. → <https://bg3.wiki/wiki/Wet_(Condition)>
- **Chromatic Orb: Lightning** on a Wet target = doubled, and it lays down an **Electrified Water** surface for follow-up Shocked.
- **Ray of Frost** (cantrip) is your free, spammable doubled-cold option and slows the target.

### The better options a Storm Sorc unlocks (this is the real answer)

At **Sorcerer 6**, Storm's *Storm Spells* feature hands you a themed spell package for **free** — and **Heart of the Storm** turns every lightning/thunder cast into an AoE. → <https://bg3.wiki/wiki/Storm_Sorcery>

- **Create or Destroy Water** (free at Sorc 6): **you apply your own Wet** — no Tempest dip, no thrown water bottles needed. Cast Water, then blast. → <https://bg3.wiki/wiki/Create_or_Destroy_Water>
- **Call Lightning** (free at Sorc 6): concentration storm cloud — cast once, then **re-fire a bolt as an action each turn with no further slot**. Doubled by Wet, and each cast also triggers Heart of the Storm. Best sustained-AoE lightning a storm sorc gets.
- **Sleet Storm** (free at Sorc 6): control — ice surface + blinds + knocks prone (breaks enemy concentration). Off-element but excellent utility.
- **Heart of the Storm** (Sorc 6): whenever you cast a L1+ lightning/thunder spell, **all enemies within 6m take (Sorc level ÷ 2) lightning/thunder** — and that splash is **also doubled by Wet**. So every Chromatic Orb: Lightning quietly becomes a small AoE nuke. (Enemies-only — no friendly fire from this part.) → <https://bg3.wiki/wiki/Heart_of_the_Storm>
- **Lightning Bolt** (Sorc 5, L3): the main **line** AoE nuke — doubled on Wet, clustered targets.
- **Witch Bolt**: sustained single-target lightning; re-trigger each turn with no roll, and it stacks Lightning Charges on **The Spellsparkler**.
- **Cold branch** (all doubled on Wet): Ray of Frost → **Ice Storm** (L4, DEX save, ice surface) → **Cone of Cold** (L5).

### Metamagic that fits

- **Twinned** Chromatic Orb (two doubled orbs) or Twinned Haste (the party Haste engine — keep this).
- **Quickened** a nuke so you can cast Create Water *and* blast in the same turn (or blast + Tempestuous fly out).
- **Heightened** on your save-based control (Sleet Storm, etc.).

### Storm vs. the old Draconic-Blue chassis

You trade Draconic Resilience (base AC 13 + DEX, +1 HP/level → squishier now) and Elemental Affinity (+CHA per lightning hit) for **flight + Heart of the Storm AoE + the Storm Spells list (self-Wet / Call Lightning / Sleet Storm)**. For a fun-first, mobile playstyle that's a great trade — you lose some single-target lightning and durability, gain mobility, AoE, and self-sufficiency on Wet.

**Keep the Tempest Cleric 2 dip** at the end anyway: **Destructive Wrath** (maximize any lightning/thunder roll) is still your biggest single multiplier, and heavy armour + shields help the squishier Storm body. Its Create Water just becomes redundant with the Sorc-6 version (fine — more Wet on demand).

### Early gear (Act 1)

- **The Spellsparkler** — quarterstaff, builds **Lightning Charges** (+1 attack, +1 lightning; 5 charges → 1d8 burst). Reward from **Counsellor Florrick** for *Rescue the Grand Duke* at **Waukeen's Rest**. ⚠ It's flagged "Consumable by Gale" — **wield it, don't feed it to the orb.** → <https://bg3.wiki/wiki/The_Spellsparkler>
- **Gloves of Belligerent Skies** (Crèche) — lightning/thunder hits stack Reverberation → soft CC.
- Standard friendly-fire discipline still applies: Electrified Water and Lightning Bolt lines hit allies, and a **Wet ally takes double** enemy lightning/cold — keep the wet cluster off the melee.

---

## Open decisions to confirm

1. **Bonbon ordering** — Fighter 1 + Wizard 1 both at the front (char 1–2, recommended for the cleanest Titanstring Act 1), **or** Fighter 1 at creation but defer/drop the Wizard 1 dip so Bard breakpoints arrive sooner?
2. **Gale split** — keep the **Sorc 10 / Tempest 2** chassis (Destructive Wrath + armour), or go **pure Storm Sorc 12** for Storm's Fury (L11), native Chain Lightning, a 6th-level slot, and a 3rd feat (losing Destructive Wrath)?
