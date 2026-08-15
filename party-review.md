# BG3 Party Build Review — Patch 8 pass

_In-depth review of the four current builds (leveling, spells, itemization, feats, tadpole) against
the expert Patch 8 video tier lists in `video_summaries/`, cross-checked against a local copy of
bg3.wiki (`bg3kb/data/chunks.jsonl`)._

**Party reviewed:** Charles (Oathbreaker Paladin 7 / Hexblade Warlock 5) · Asterion (Open Hand Monk 9 /
Thief Rogue 3) · Gale (Draconic-Red Sorcerer 11 / Fiend Warlock 1) · Bonbon (Swords Bard 11 / Fighter 1).
**Mode:** non-Honour, modded Hag's Hair (one per character), Patch 8 + hotfixes #30–#36.

**Source labels used throughout:**
`[V]` = expert video tier list · `[W]` = verified against local bg3.wiki copy · `[P]` = the plan's own
claim, neither confirmed nor refuted by the sources read.

> ⚠️ **This file replaces an earlier review that described a different party** (a Gloomstalker archer
> and a Wet/Lightning Storm Sorcerer). That version is preserved in git history at `b45e496~`.
> One of its claims was wrong and has been corrected below: Arcane Acuity caps at **10** turns, not 7.

---

## Verdict at a glance

| Build | Verdict | Headline |
|---|---|---|
| **Charles** — Oathbreaker Pal 7 / Hexblade 5 | ✅ **KEEP**, 3 additions | Chassis is well-supported. Missing **Aid**, missing the **Murder Tribunal** item cluster he alone unlocks, and **Luck of the Far Realms is at risk of auto-wasting** on his own crit-range stack. |
| **Asterion** — Open Hand Monk 9 / Thief 3 | ✅ **KEEP**, near-optimal | The single most-endorsed build in the whole source set: Open Hand is the top Monk subclass, a top-5 pure build *and* a "broken build"; Tavern Brawler and Alert are the only two **S+** feats; Monk 8–9 + Rogue 3–4 is named "the defining combination." Two of his Act 3 items are missing from the loot route. |
| **Gale** — Draconic-Red Sorc 11 / Fiend Warlock 1 | 🔧 **TUNE** | The build works, but its two self-declared structural weaknesses — no Alert, no CON-save protection until Act 3 — are **both solvable in Act 1 with items the plan already passes over**. Also carries a **hidden anti-synergy in its own Act 3 loadout** (Markoheshkir Heat vs Callous Glow vs Arcane Acuity), and rests on **one untested assumption** (Spellmight per ray) that could invert a core item. |
| **Bonbon** — Swords Bard 11 / Fighter 1 | 🔧 **TUNE** | Correct chassis and correct engine. Two live questions: **Fighter 1 vs Fighter 2** (Action Surge), and whether **Magical Secrets → Command** duplicates Gale rather than adding to him. |
| **Party** | 🔧 **TUNE** | Strong. The gaps are concentrated in three places: **initiative**, **the Bless economy**, and **a handful of never-routed items**. |

---

## Decisions taken — and now applied to `content/`

These were chosen at the table and are already written into the guide data.

| Decision | Where it landed |
|---|---|
| **Gale drinks Elixir of Vigilance every long rest** (+5 initiative, replaces Alert) | `gale.md`, `party.md`, `loot.md` |
| **Gale wears Spidersilk Armour from Act 1** (CON-save advantage, −1 AC) | `gale.md`, `loot.md`, `party.md` |
| **Charles takes Aid** at Paladin 5 | `charles.md` |
| **Charles keeps concentrating on Bless**, cast while holding the Staff of Arcane Blessing | `charles.md`, `party.md`, `loot.md` |
| **Bonbon wears The Whispering Promise** for the char 1–3 Bless window | `bonbon.md`, `loot.md`, `party.md` |
| **Luminous Armour stays on Charles**; both ores go to Bonbon (Shield + Splint) | `bonbon.md`, `loot.md` |
| **Magical Secrets → Command + Globe of Invulnerability** (Counterspell dropped) | `bonbon.md` |
| **Gale carries both Rhapsody and Staff of Spellpower**, swapping per fight | `gale.md` |
| **Add Ability Drain** (Charles + Asterion, *not* Gale — it would drain his CHA) | `tadpole.md`, `asterion.md` |
| **Charles gets Shield of Thralls**; drops Armour of Agathys | `tadpole.md` |
| **Luck of the Far Realms stays on Charles** *and* is bought for Asterion and Bonbon | `tadpole.md` |
| **Gale's illithid list rewritten** around his real DC 27 and his reactions | `tadpole.md` |
| **Murder Tribunal items documented but gated** — the Bhaal path stays undecided | `loot.md`, `charles.md` |
| Missing loot entries added: Soul Catching, Kushigo Boots, Arcane Blessing, Drakethroat, Grymskull | `loot.md` |

Validated: all nine content files still parse, and `GET /api/plan` returns 200 with every new entry present.

---

# Part 1 — Party-level findings

These matter more than any individual item swap, and three of them are cheap.

## 1. Initiative is rolled on a **d4**, and the plan is priced as if it were a d20

`[W]` **Initiative in BG3 is `d4 + Dexterity modifier`** — not d20. It is explicitly *not* a Dexterity
check, so Jack of All Trades and Enhance Ability do nothing for it.

This single fact reprices a lot of the plan. A flat +2 is worth *half the entire die's range*. It is
also why the feats video rates **Alert as one of only two S+ feats** `[V]` — +5 on a d4 is not a bonus,
it is a guarantee.

**Verified initiative sources** `[W]` (the complete table):

| Bonus | Sources |
|---|---|
| **+5** | Alert (feat) · **Elixir of Vigilance** (consumable) — both also grant immunity to Surprise |
| **+3** | Hellrider Longbow · Sentinel Shield · Feral Instinct · Dread Ambusher |
| **+2** | **Bhaalist Armour** · **Assassin of Bhaal Cowl** · Mask of Soul Perception · Elven Chain · Elegant Studded Leather · Flame Enamelled Armour · Soulbreaker Greatsword |
| **+1** | Bow of Awareness · Fistbreaker Helm · Stalker Gloves · Halberd of Vigilance · Ambusher · +2 armours |

### The fix: Gale's "no feat for Alert" problem is already solved and the plan doesn't notice

`gale.md` lists this under **traps**: _"There is no Alert and no War Caster — initiative and
concentration are gear problems on this build,"_ and answers it with **Bow of Awareness (+1)**, with
Elixir of Vigilance mentioned only as a situational fallback "for the fights where he must go first."

But `[W]` **Elixir of Vigilance grants +5 initiative and immunity to Surprise, lasts until long rest,
costs 25 gp, and is sold by many merchants** (Danthelon's, Kith in Grymforge, Popper at the Circus).
Its only cost is the one-elixir-per-rest slot — **and Gale is the one party member with no competing
elixir.** Asterion needs Giant Strength (load-bearing for attack, damage *and* his Stun DC); Bonbon
wants Bloodlust or Hill Giant.

> **Recommendation:** make **Elixir of Vigilance Gale's standing daily elixir**, exactly as Giant
> Strength is Asterion's. It converts a +1 item into a +5 permanent effect, replicates the Alert feat
> he cannot afford, and frees **Bow of Awareness** and the Hellrider's Longbow contest entirely.
> This is the cheapest high-impact change in the review.

### Resulting party initiative order

| | Roll | Range |
|---|---|---|
| Asterion | d4 + 5 (DEX 20) + 5 (Alert) | **11–14** |
| Gale | d4 + 3 (DEX 16) + 5 (Vigilance) | **9–12** |
| Bonbon | d4 + 4 (DEX 18) + 3 (Hellrider's Longbow) | **8–11** |
| Charles | d4 + 2 (DEX 14) | **3–6** |

Charles going last is **correct and should be stated as deliberate** rather than left as an accident:
his entire job is to swing at a target the others have already Held, Stunned, or Commanded. The plan's
`opening_rotation` already sequences him fourth — it just never says that the initiative build supports it.

---

## 2. The Bless economy — the plan's tightest bottleneck, with three unused fixes

The plan flags this twice itself: Charles is **the only Bless source**, Bless **costs him his
concentration**, and **character levels 1–3 have no Bless at all**. Meanwhile `[V]` rates
**Bless S-tier** and the Paladin's default early concentration spell.

Three items the plan never assigns break this open:

**a) The Whispering Promise** `[V]` **#10 of 20 best Act 1 items** — `[W]` _"When you heal a creature,
it gains a **+1d4 bonus to Attack rolls and Saving throws** for 2 turns."_ That is Bless, **without
concentration**, from a 40 gp ring sold by Grat at the Goblin Camp and by Volo.

**b) Hellrider's Pride** `[V]` **#6 of 20** — `[W]` _"When you heal another creature, it gains
Resistance to Bludgeoning, Piercing, and Slashing damage dealt by weapon attacks for 2 turns."_
The video names these two as a deliberate package: *the same heal* produces Bless and Blade Ward.

> ⚠️ **CORRECTION — the ring does NOT free Charles's concentration.** An earlier draft of this review
> claimed it did. `[W]` Blessed Mercy _"applies the same condition as the standard Bless spell, and
> therefore **cannot stack with it**"_ — and `[W]` _"Despite also being called Bless, this buff is
> **not** enhanced by the Staff of Arcane Blessing."_ Bless the spell also covers **3 creatures**
> (4 upcast to L2) for **10 turns**, versus the ring's **one creature per heal for 2 turns**.
>
> So **someone still burns concentration on Bless** — Charles, as before. The ring's real jobs are:
> **(1)** character levels **1–3**, before Charles has Bless at all, which is exactly the hole the plan
> admits to; **(2)** any fight where Charles concentrates on Hex, Divine Favour or Darkness instead.
> `[W]` also confirms useful triggers: a **thrown Potion of Healing blesses every creature it splashes**,
> drinking one self-triggers it, it fires **even on a target at full HP**, and a **Short Rest counts as
> self-healing**.

> ⚠️ **Correction to the video's framing:** the pitch assumes a bonus-action heal. `[W]` **Paladin
> Lay on Hands costs a full Action**, not a bonus action, at 1.5 m range. So Charles is *not* the
> cheap trigger the guide imagines.
>
> **The right carrier is Bonbon.** She has **Healing Word — a bonus-action ranged heal** — and she is
> already planned to carry **Broodmother's Revenge**, which triggers on *any* healing. One bonus-action
> Healing Word would then fire **three** item procs at once: poison coating on her own projectiles,
> +1d4 attack/saves on the target, and Blade Ward on the target. `[V]` also confirms **thrown healing
> potion splashes** trigger these, which lets any character apply it to several allies at once.
>
> **Cost:** Whispering Promise displaces **Caustic Band**; Hellrider's Pride displaces
> **Gloves of Dexterity**, which `[V]` calls _"the most impactful equipable item in Act 1 and arguably
> the entire game."_ So take the ring, **not** the gloves. Best window is **Acts 1–2**, before the Band
> of the Mystic Scoundrel claims her bonus action.

**c) Staff of Arcane Blessing** `[V]` **A-tier**, and the fit is nearly exact — `[W]` _"Creatures you
Bless also gain Mystra's Blessing for an additional **1d4 bonus to spell attack rolls**."_

Gale's entire loop is 3–7 spell attack rolls per cast, so +1d4 (avg 2.5) per ray beats Melf's flat +1.

> ⚠️ **But the obvious version doesn't work.** Mystra's Blessing only applies to creatures blessed by
> *the staff's wielder*, and Bless is Concentration — so Gale cannot cast it himself without dropping
> Twinned Haste.
>
> **The version that does work:** **Charles** holds the staff, casts Bless (his existing default
> concentration) on Gale and the party, then swaps to Phalar Aluve. Charles keeps concentration, and
> Gale gets +1d4 on every single ray. This costs Charles nothing he wasn't already doing.

---

## 3. Aid is missing, and Charles is the party's only possible source

`[V]` rates **Aid S-tier** and specifically names it _"the only Aid source in this party pool."_
`[W]` confirms: **Paladin class level 5**, level-2 slot, self-centred **9 m radius**, **+5 maximum HP**
(+5 more per slot level above 2nd), **duration Until Long Rest, no concentration**. Downed allies
return with an extra hit point.

Charles hits Paladin 5 at character level 7 and again at 10 post-respec, and the plan lists "Level 2
Paladin spells" at both — but **Aid appears nowhere in his sheet.** For a party with one healer, no
Cleric, and no Bless below level 4, a permanent party-wide +5 to +15 max HP for one L2 slot per long
rest is close to free.

`[W]` also settles a related question: **Aid stacks with a single source of temporary HP, but temp HP
sources never stack with each other** — so Charles's **Armour of Agathys** and the illithid **Shield of
Thralls** compete, and he should carry only one.

---

## 4. Three Murder Tribunal items are missing — and Charles is the Dark Urge

`loot.md` already routes the Act 3 Murder questline (Sarevok's Horned Helmet, Bloodthirst, Crimson
Mischief, Ring of Murderous Opportunity). But the **Echo of Abazigal**, unlocked by the same
*Impress the Murder Tribunal* quest, sells three items that appear in **no** file in the repo:

| Item | Effect `[W]` | Fit |
|---|---|---|
| **Craterflesh Gloves** | _"Whenever you score a Critical Hit, deal an additional 1d6 Force"_ — and `[W]` notes it **actually deals 2d6, because the damage is itself doubled by the crit** | **Charles, strong.** On a Held target every swing auto-crits: 7 attacks × 2d6 ≈ **49 extra damage per nova turn**, versus ~17 from the currently-planned Helldusk Gloves (1d4 fire per hit). |
| **Bhaalist Armour** | Light armour, AC 14 + DEX, **+2 Initiative**, and **Aura of Murder: enemies within 3 m become Vulnerable to Piercing** (radius raised 2 m → 3 m in Patch 8) | **Situational.** Charles's own Shadow Blade is Psychic, so it does nothing for him — but Bonbon's hand crossbows and Titanstring are **Piercing**, so enemies engaged with Charles take double from her. Costs Luminous Armour's Radiating Shockwaves and 1 AC. |
| **Assassin of Bhaal Cowl** | **+2 Initiative** | Minor, but on a d4 die a +2 head item is real — and Charles has the party's worst initiative. |

> **Recommendation:** add all three to `loot.md` under the Murder Tribunal. **Craterflesh Gloves are a
> straight upgrade** over Helldusk Gloves for a crit-fisher and should be the Act 3 default. The other
> two are worth recording as options.

---

## 5. Two Adamantine armours are crafted and neither is ever worn

`[V]` ranks **Adamantine Splint #15** and **Adamantine Scale Mail #16**, with the explicit rationale
that _"Adamantine equipment removes random critical-hit spikes"_ and the advice to
_"distribute Adamantine crafts to maximise critical immunity across the party."_

The plan spends **both** Mithral ores on those two armours — then equips **Luminous Armour** on Charles
and **The Protecty Sparkswall** on Bonbon, listing both Adamantine pieces only as "defensive
alternative." As written, two limited crafting resources buy **zero equipped crit immunity**.

`[V]` also ranks **Adamantine Shield #13**, but the plan is right to skip it — Asterion must stay
shieldless, Gale took Dual Wielder, Charles two-hands then dual-wields, and Bonbon is ranged. No legal
wielder.

### ✅ RESOLVED — both ores go to Bonbon, and the Shield was wrongly written off

Follow-up research settled this. **Bonbon is the party's only legal wearer of anything from the forge:**
`[W]` multiclassing into Paladin grants no heavy armour (Charles has Hexblade's *medium + shields*
only), and Charles can never free an off-hand — GWM: All In needs an empty one, and he later
dual-wields. Asterion must stay unarmoured and shieldless; Gale is light-armour-only with two staves.

**The Adamantine Shield is the find the plan dismissed.** `[W]`: _"a character **need not to be actively
holding the equipped shield to get the AC bonus**… a character with a sword and shield in its melee
weapon slots and a longbow in its ranged weapon slots benefits from the shield's AC bonus **even while
using the bow**."_ So Bonbon puts it in her **melee off-hand** (replacing the Knife) and keeps shooting
hand crossbows — **+2 AC and crit immunity from a slot she was barely using**, with no cost to Protecty
Sparkswall's +1 Spell Save DC.

**Why crit immunity belongs on her specifically:** `[W]` a concentration save is _"a Constitution save
against a **DC equal to half the damage taken, or 10, whichever is higher**"_ — so a crit roughly
doubles that DC. She is the one holding **Hold Monster**, the party's auto-crit engine. `[W]` it also
stops Hold Person and Sleeping from granting attackers automatic crits against her.

> **Applied:** craft **Shield + Splint**, both for Bonbon; **Adamantine Scale Mail is dropped** (its only
> home was Charles, and Luminous is decided).
>
> ⚠️ **Verify in play:** the wiki confirms only the **AC bonus** carries from the inactive melee set — it
> never says whether **crit immunity** does. Check her sheet with crossbows drawn. If it doesn't carry,
> fall back to Splint plus the free **Grymskull Helm** (dropped by Grym, whom you kill for the forge
> anyway; grants crit immunity for zero ore, but is evicted by the Helmet of Arcane Acuity in Act 2).
>
> **Charles gets nothing from the forge.** His crit-immunity answer is Act 3 **Helm of Balduran**
> (medium armour, which he has) — and its **+1 to saving throws** partly offsets the Risky Ring's
> permanent disadvantage on saves, which matters because he holds concentration on Darkness while
> wearing it. That is the most fragile concentration in the party and no ore can fix it.

---

## 6. Drakethroat Glaive — a free party-wide weapon buff, and Gale can Twin it

Absent from every file in the repo. `[W]` **Drakethroat Glaive** (rare +2 glaive, **sold by Roah
Moonglow at Moonrise Towers — Act 2**) grants **Draconic Elemental Weapon**, cast as a level-3 spell,
recharging on long rest.

The mechanics that matter `[W]`:
- The effect gives **+1 to Attack Rolls and +1d4 elemental damage**, **duration until long rest**.
- _"This spell can target weapons and non-enemy creatures with a weapon in their main hand."_
- _"A Sorcerer of level 3 and higher can target **two** weapons using Metamagic: Twinned Spell."_
- It **stacks with Magic Weapon**, and does not stack with other Elemental Weapon variants.

Gale is a Sorcerer with Twinned Spell, and is **proficient with glaives** via Human Civil Militia. So
once per long rest, out of combat, he can hold the glaive, Twin the enchant onto **two** party
main-hand weapons, and swap back to his staves. That is +1 attack and +1d4 damage on two characters,
all day, for one Act 2 purchase.

> ⚠️ Two caveats to verify in play: the spell details list **Concentration** even though the condition
> is "until long rest" (the same pattern as `Daylight: Enchant Item`, which the plan already relies on);
> and Charles's **Shadow Blade is summoned fresh each rest**, so enchant **Phalar Aluve** or Bonbon's
> crossbows instead. Note `[V]` records that Patch 8 changed Elemental Weapon from a +1 *enchantment*
> (attack **and** damage) to +1 **attack rolls only**.

---

## 7. What the party structurally cannot have — and where the plan is right

`[V]`'s single strongest structural recommendation is _"at least one reliable source of **Guidance**,
**Longstrider**, **Create Water**, and **Counterspell**."_ Against a Sorcerer / Swords Bard / Paladin /
Warlock lineup:

- **Guidance** `[V]` **#2 spell overall** — Cleric/Druid only. **Unavailable.** The plan's insistence
  that the **Silver Pendant is MANDATORY from level 1** is fully vindicated; if anything it is
  understated. It is the party's only access to the second-best spell in the game.
- **Create or Destroy Water** `[V]` **S** — Cleric/Druid only. **Unavailable.** The plan correctly
  demotes Wet to "a niche tool… not a party engine." Nothing to fix.
- **Longstrider** `[V]` **#1 spell overall** — Bonbon has it as a ritual. ✅ Correctly prioritised.
- **Counterspell** `[V]` **#4 overall**, and **no scrolls exist — it must be learned.** The party ends
  with three carriers (Gale, Bonbon via Magical Secrets, Charles post-respec) against a recommendation
  of two. Mild over-investment; see Bonbon's Magical Secrets question below.

---

# Part 2 — The four builds

## Charles — Oathbreaker Paladin 7 / Hexblade Warlock 5

### ✅ Verdict: KEEP the chassis. Three additions, one hazard.

**What the sources confirm.** `[V]` ranks **Darkness S-tier** and says its ceiling is _"far higher in
a party that can see through magical darkness"_ — Devil's Sight makes Charles exactly that character,
so the Darkness-Arrow plan is not a workaround, it is the endorsed use. **Savage Attacker** and
**Great Weapon Master** are both **S-tier feats**; **Dual Wielder is A**. **Bless (S)**, **Command (S,
#3 overall)**, **Hex (S)**, **Shield (S)**, **Booming Blade (S, #6 overall and new in Patch 8)** and
**Armour of Agathys (A)** are all already on his sheet. The Shadow-Blade-plus-Resonance-Stone package
appears in `[V]` as one of the seven "broken builds."

**Where the sources push back.** The class video ranks Paladin oaths **Vengeance > Oathbreaker**, and
the plan keeps Vengeance through Acts 1–2 anyway before breaking for Aura of Hate — which is the right
reading. Note honestly: **no video in this set gives a Paladin/Warlock split at all** — no 7/5, no 6/6.
The split is unendorsed rather than contradicted.

### Changes, ranked

1. **Take Aid** at Paladin 5 (see Part 1 §3). Free party-wide +5–15 max HP, no concentration.
2. **Craterflesh Gloves over Helldusk Gloves** in Act 3 (see Part 1 §4) — roughly +30 damage on a nova turn.
3. **Hold the Staff of Arcane Blessing to cast Bless**, then swap to Phalar (see Part 1 §2c). Free +1d4
   to every one of Gale's rays.
4. **Upcast Command as a mass disable.** `[V]` notes Command _"upcasts to add targets"_ and rates it #3
   overall; the plan only ever treats it as single-target.
5. **Consider Hunger of Hadar.** `[V]` rates it **S** and calls it warlock-exclusive and one of the
   game's best layered-control spells. It is currently filed as an "alternative" on his sheet. It costs
   the Darkness concentration slot, so it is a per-fight choice, not a replacement.

### ⚠️ Hazard: Luck of the Far Realms will auto-waste itself on Charles

`[W]` _"Due to the way this passive's reaction is coded, it triggers on attacks that are **not natural
20 rolls but are already critical hits due to Critical Hit Threshold Reductions**."_

Charles is the party's crit-threshold stacker — Hexblade's Curse, Knife of the Undermountain King,
Sarevok's Horned Helmet, Covert Cowl. `tadpole.md` warns "never on a Held target or an already-critical
attack," but does not say **the reaction fires on its own**. On Charles specifically, Luck is likely to
be consumed automatically by a crit he was going to get anyway. Either treat it as unreliable on him,
or move it to Asterion.

### Minor notes
- **Death Ward is D-tier** `[V]`, **Banishment B**, **Searing Smite** explicitly _"worse than simply
  spending the slot on Divine Smite."_ None are in the plan — correctly.
- `[W]` **Aid stacks with one temp-HP source; temp-HP sources never stack.** Pick either Armour of
  Agathys or Shield of Thralls, not both.
- `[W]` **Killer's Sweetheart only applies to *weapon* attack rolls**, despite a tooltip implying
  otherwise. Harmless here — Charles is a weapon attacker — but it rules out ever moving it to Gale.

---

## Asterion — Open Hand Monk 9 / Thief Rogue 3

### ✅ Verdict: KEEP. This is the most heavily endorsed build in the entire source set.

Every load-bearing choice is independently top-ranked `[V]`:

- **Tavern Brawler and Alert are the only two S+ feats in the tier list.** Asterion takes both. Nobody
  else in the party takes either.
- **Open Hand is the best Monk subclass**, a **top-5 pure build to 12**, *and* one of the seven
  **"broken builds."**
- **Thief is the 2nd-best Rogue subclass**, and the multiclass video names **Monk 8–9 + Rogue 3–4**
  _"the defining combination"_ — an exact match for Monk 9 / Thief 3.
- **Minor Illusion is S-tier** (_no-save forced movement_) — his racial cantrip pick.
- **Graceful Cloth is #3**, **Disintegrating Night Walkers #11**, **Ring of Protection #20** — all his.

### Changes, ranked

1. **Two of his Act 3 items are missing from the loot route.** `asterion.md` assigns **Gloves of Soul
   Catching** and **Boots of Uninhibited Kushigo**, but neither appears in `content/loot.md`, so neither
   will ever show on the loot checklist. Both verified `[W]`:
   - *Gloves of Soul Catching* — **+1d10 Force per unarmed hit**, +2 CON, House of Hope (Hope's reward).
   - *Boots of Uninhibited Kushigo* — **adds WIS modifier to unarmed strike damage**, carried by
     Prelate Lir'i'c in the Astral Plane at the start of Act 3.
   At 4–6 unarmed hits per turn these are among his largest damage sources; they need routing.
2. **Give him Luck of the Far Realms instead of Charles** (see the hazard above). He stacks no
   crit-threshold reduction, so the reaction won't fire early.
3. **Add Ability Drain.** `[V]` rates it **A-tier** and nobody in the party takes it. `[W]` confirms:
   passive, **once per turn on an attack roll, reduces the target's corresponding ability by 1**
   (Strength for melee) — free, and it counts as applying a condition, which his and Gale's gear cares
   about. One middle-ring tadpole.

### Notes and corrections
- `[W]` **Cull the Weak is mutually exclusive with Non-Lethal Attacks** — enabling one disables the
  other. Worth recording alongside the existing Deathstalker warning, and relevant to any non-lethal
  knockout (e.g. Kagha for Broodmother's Revenge).
- `[W]` Cull the Weak's splash damage _"only applies to enemies"_ despite the tooltip saying "all
  nearby creatures." The plan can drop that worry.
- `[V]` names **Karlach's Soul Coins** as part of the broken Open Hand Monk build. This party has no
  Karlach — a real but unavoidable gap, worth noting so it isn't mistaken for an oversight.
- **Tavern Brawler is slightly broader than the plan states** `[W]`: the feat also covers **Throw** and
  **Improvised Melee Weapon** attacks, neither of which needs empty hands. Only the base **Unarmed
  Strike** action requires "no melee weapons equipped." Asterion's build is unarmed, so the
  hands-empty rule still applies to him exactly as written — but the feat's Throw coverage is why
  `[V]` also builds a Tavern Brawler *thrower*, and it means a thrown consumable is never blocked by
  the rule.
- `[W]` **Titanstring's +STR stacks per damage instance** and **ranged Slashing Flourish fires two
  separate projectiles** — both confirmed individually, though the wiki never states the interaction
  together. Also flagged as "mostly changed in Honour mode," which does not affect this party.
- `[W]` **Club of Hill Giant Strength (STR 19) and the Elixir (STR 21) do not stack** — both are
  "set to X" effects, so the elixir simply overrides. The plan already assumes this correctly.
- The **Monk 8 / Thief 4** third-feat variant is already noted in his traps; given Alert and Tavern
  Brawler are the two S+ feats and he already has both, staying Monk 9 for Ki Resonation is right.

---

## Gale — Draconic-Red Sorcerer 11 / Fiend Warlock 1

### 🔧 Verdict: TUNE. The build is sound; both of its self-declared weaknesses are fixable in Act 1.

**What the sources confirm.** `[V]` rates **Dual Wielder A-tier** with the reasoning
_"chiefly because dual-staff spellcasters can combine two powerful passive items"_ — an unusually exact
endorsement of Gale's most unorthodox pick. **Haste (S)**, **Counterspell (S, #4)**, **Command (S, #3)**,
**Shield (S)**, **Hold Person (S)**, **Misty Step (S)**, **Globe of Invulnerability (S)** are all
correctly identified. Taking **Sorcerer at level 1** for CON+CHA saves matches the multiclass video's
"universal package" advice. **Melf's + Spellsparkler** is endorsed by name for _"a fire Sorcerer who
generates many hits."_ **Markoheshkir → Gale** is confirmed.

### The two structural fixes

1. **Elixir of Vigilance as his standing daily elixir** (Part 1 §1) — replaces the Alert feat he cannot
   afford, +5 initiative instead of +1.
2. **Spidersilk Armour in Act 1.** The plan treats CON-save protection as an Act 3 problem solved only
   by Armour of Landfall, and calls losing the Safeguard Shield _"the main defensive regression of the
   Fire Sorlock switch."_ But `[W]` **Spidersilk Armour** is **light armour, AC 12 + DEX, +1 Stealth,
   and grants ADVANTAGE ON CONSTITUTION SAVING THROWS** — worn by **Minthara in the Shattered Sanctum**,
   the same Act 1 kill the plan already makes for Charles's Boots of Striding. Gale has light armour
   proficiency from Civil Militia and currently has **no chest item assigned at all**.
   **Trade:** AC 12+3 = 15 versus Draconic Resilience's 13+3 = 16, so it costs exactly 1 AC to protect
   Twinned Haste — the concentration the entire party plan is built around — from Act 1 rather than Act 3.
   It is already in `loot.md`, marked `core: false`.

### Spell-list notes `[V]`

- **Fireball is only B-tier** — _"do not cast it solely because it is iconic."_ The plan leans on it as
  the primary AoE. Not wrong (it is on-element for Elemental Affinity, Flame of Wrath and Elemental
  Adept), but it should not be prioritised over more Scorching Ray.
- **Scorching Ray is A, not S** — and the stated reason is precisely that it is _"valued for multi-hit
  riders, not efficiency."_ That is exactly what this build does with it. Strong validation of the
  approach rather than the spell.
- **Magic Missile is S-tier.** The plan calls it _"a deliberate placeholder"_ to be replaced by
  Counterspell at Sorc 6. Worth re-examining — it is one of the few reliable answers to a missed
  attack-roll turn on a build made entirely of attack rolls.
- **Chromatic Orb is S** (currently a "replacement candidate"); **Ice Storm A** and non-concentration,
  so it layers on top of Haste; **Cloud of Daggers S**; **Enhanced Leap S**.
- **Elemental Adept is only B-tier** generally `[V]`, and it consumes one of Gale's two feats. The plan's
  justification (fire is the most-resisted type in Act 3; no bow archer to mass-apply Arsonist's Oil;
  removes 1s from many dice) is party-specific and holds — but it is worth stating that this is a
  B-tier feat bought at the cost of never having an S+ one, and that **the Elixir of Vigilance fix above
  is what makes that acceptable.**
  Two wording corrections `[W]`: BG3's text is **"you cannot roll a 1"**, not the tabletop "treat 1s as
  2s"; and the resistance-piercing is **broader than the plan states** — it covers _"spells you cast
  **and attacks you make**,"_ not spells alone. The no-1 clause is spell-only.
- **Per-ray riders are confirmed for some, inferred for others** `[W]`. The Scorching Ray page
  explicitly names **Elemental Affinity: Damage** and the **Callous Glow Ring** as applying to *each*
  ray. **Rhapsody** and **Markoheshkir's +proficiency** are covered only by the general rule that bonus
  damage from passives and conditions applies per ray — very likely true, but not individually stated.
- The Ice Sorcerer video is a direct comparison point: the CHA riders (Elemental Affinity, Potent Robe,
  Necklace of Elemental Augmentation) are **element-agnostic**; what a fire build gives up is the
  **cold vulnerability layer** (Chilled + Wet) and the ice control terrain. This party cannot produce
  Wet reliably anyway (no Cleric/Druid), so **choosing fire is correct here** — the cold build's
  advantage is unreachable for us.

### ⚠️ Trap the plan misses: Markoheshkir's Heat fights the rest of his own Act 3 kit

The planned Act 3 loadout is **Markoheshkir (Flame of Wrath) + Callous Glow Ring + Coruscation Ring +
Hat of Fire Acuity**, with Gale deliberately kept **Illuminated** so Coruscation fires. Three verified
interactions turn that combination against itself `[W]`:

1. **Heat's self-damage is not stopped by Elemental Adept: Fire.** The feat pierces *enemy* resistance;
   it does not protect Gale.
2. **Callous Glow adds +2 radiant to Gale's own Heat tick while he is Illuminated** — and the build
   keeps him Illuminated on purpose. His own damage ring makes his own self-damage worse.
3. **Any damage taken strips 2 turns of Arcane Acuity.** So every Heat tick chips the very stat the
   whole build exists to stack, *and* forces a CON save against Twinned Haste.

The plan already warns "do not attune Flame of Wrath until Armour of Landfall is equipped" — that
addresses the Haste concentration, but **not** the Acuity bleed or the Callous Glow amplification.
Treat Flame of Wrath as a per-fight toggle rather than a permanent attunement, and consider dropping
Coruscation (and therefore the illumination) in the fights where Acuity uptime matters more than the
radiant riders.

### ⚠️ Two unresolved questions that gate his build

**a) Does Spellmight's +1d8 apply per ray, or once per spell?** — **the highest-stakes open question in
the whole plan.** `gale.md` promotes Spellmight Gloves to CORE precisely because
_"Scorching Ray is an attack roll fired 3–7 times per cast."_ The fact-check found the −5/+1d8 wording
confirmed but **the per-ray question never addressed anywhere in the wiki**, and Spellmight is absent
from the per-instance notes that *do* explicitly name Elemental Affinity and Callous Glow.

The two outcomes are wildly different on a 7-ray cast:
- **Per ray:** −5 on each roll for **+7d8 ≈ +31** damage. Best-in-slot, as the plan says.
- **Once per spell:** −5 on *all seven* rolls for **+1d8 ≈ +4.5**. Actively harmful.

Do not treat "+1d8 per ray" as established. Test it on a single cast the moment the gloves are acquired.

**b) Can Gale cast Command from ordinary Sorcerer slots?** `gale.md` already flags this. The fact-check
leans **yes** — Command is confirmed on the Fiend's level-1 list, and warlock spell access is described
elsewhere as usable with non-pact slots — but found **no direct multiclass citation**. If it turns out
to be pact-slot-only, his control lane is **once per short rest**, not every turn, and the Warlock dip
loses most of its value. Confirm at character level 7.

---

## Bonbon — Swords Bard 11 / Fighter 1

### 🔧 Verdict: TUNE. Right chassis, right engine, two open questions.

**What the sources confirm.** `[V]` ranks **Swords the 2nd-best Bard college**; **Sharpshooter S-tier**;
**War Caster A**; **Gloves of Dexterity #1 overall** (_"the most impactful equipable item in Act 1 and
arguably the entire game"_) with the advice to dump DEX and reclaim the points — which the plan does;
**Protecty Sparkswall #8**; **Caustic Band #12**; **Broodmother's Revenge #17**. **Glyph of Warding (S)**,
**Hold Person (S)**, **Healing Word (S)**, **Dissonant Whispers (S)** and **Longstrider (S, #1 overall)**
are all already on her sheet. `[V]` also settles a `loot.md` alternative: **Wondrous Gloves should stay
benched**, since trading the #1-ranked item for +1 AC and one Bardic Inspiration is a downgrade.

### Open question 1: Fighter 1 vs Fighter 2 (Action Surge)

The multiclass video lists **Fighter (Action Surge)** as a universal package and its own party build
uses a **Swords Bard 6 / Fighter 2** core `[V]`. Bonbon takes only Fighter 1.

- **Keeping Fighter 1** buys Archery (+2 ranged, offsets Sharpshooter), CON saves (protects Hold
  Monster) and heavy armour — and preserves **Bard 11**, which is what gives her the **level 6 slot that
  upcasts Command to six targets** and Otto's Irresistible Dance.
- **Going Fighter 2** adds a second Attack action to saturate Arcane Acuity and fire control a full turn
  earlier — at the cost of dropping to Bard 10, losing the L6 slot and the 6-target Command.

Given the L6 slot is explicitly the plan's payoff (_"Bard 11 = caster level 11 → one L6 slot, so Command
still hits up to 6 targets"_), **Fighter 1 is defensible and probably correct here** — but the plan should
record *why* it rejects Action Surge rather than leaving it unaddressed.

### Open question 2: does Magical Secrets → Command duplicate Gale?

`[V]` calls **Magical Secrets at Bard 10 the single biggest lever** in this party for reaching otherwise
unavailable S-tier spells: **Spirit Guardians (S, #10 overall)**, **Globe of Invulnerability (S, #9)**,
**Heroes' Feast (S)**, **Haste (S)**, **Hunger of Hadar (S)**.

The plan spends both picks on **Command + Counterspell**. But **Gale already spams Command** as his
non-concentration lane, and the party already has **three** Counterspell carriers against a recommended
two. Meanwhile:

- **Globe of Invulnerability** is currently planned to be covered by **buying scrolls** — a Magical
  Secret would make it repeatable, and it is the #9 spell in the game.
- **Heroes' Feast** is a party-wide permanent buff otherwise unreachable by any of the four.
- **Spirit Guardians** is #10 overall but is a melee aura, and Bonbon is deliberately backline — a poor
  fit despite the ranking.

**Bonbon's Command is not fully redundant** — hers is a *bonus action* via the Band of the Mystic
Scoundrel at the party's highest DC, which Gale cannot replicate. But **Counterspell is** the weaker of
her two picks. Worth considering **Counterspell → Globe of Invulnerability or Heroes' Feast**.

### Other notes
- **Take The Whispering Promise** (Part 1 §2) — she is the correct carrier.
- `[V]` **Hypnotic Pattern is A, not S** — _damage wakes the targets and the duration is short._ The
  plan calls it "best-in-class AoE lockdown"; that should be tempered.
- `[V]` **Enhance Ability is only B** — _"significant checks are less frequent than players expect."_
  The plan trades Faerie Fire for it at char 5; low stakes either way.
- `[V]` **Greater Invisibility (A)** _"anchors an entire party strategy"_ and **Silence (A)** are both
  absent from her list. **Cloud of Daggers is S** and also absent.
- Her background is listed as "Entertainer **or** Guild Artisan" while `proficiencies.md` assumes Guild
  Artisan. Pick one so the skill table is accurate.

---

# Part 3 — The tadpole plan

**Verdict: ✅ in good shape, and more accurate than the video sources.** Several claims the videos could
not corroborate were verified directly:

| Plan claim | Status |
|---|---|
| Zaith'isk chain is INT 12 → WIS 15 → CON 18; failed save = −2 to that stat, cured by consuming a parasite; Ghustil must be left alive | ✅ **CONFIRMED** `[W]`, exactly as written |
| Awakened makes all illithid powers cost a Bonus Action | ✅ **CONFIRMED** `[W]` — and note the wiki's warning that use is **_not optional_** and _"could prove disadvantageous"_ for characters that use bonus actions heavily. Bonbon is exactly such a character (Band loop + off-hand crossbow), so this is a real, permanent tradeoff and deserves stronger wording than the plan gives it. |
| Black Hole: 6 m pull with **no save**, 9 m radius, 18 m range, INT save only for Slow, 5 recasts, short-rest recharge | ✅ **CONFIRMED** `[W]` |
| Favourable Beginnings: proficiency bonus to the first attack/check; only the first attacker benefits on a shared target | ✅ **CONFIRMED** `[W]` — and `[W]` adds that _"only Deception and Persuasion receive ability check bonuses,"_ which matches the plan's Bonbon note |
| Freecast waives slot **and** metamagic cost | ✅ **CONFIRMED** `[W]` — _"If an action takes more than one type of resource… both costs are removed"_ |
| Cull the Weak threshold = number of evolved powers | ✅ **CONFIRMED** `[W]` |

### Corrections and additions

1. **Perilous Stakes is fine — the Honour-mode worry does not apply.** `[W]` _"Outside of Honour mode,
   this can target any creature including enemies; in Honour mode it can only target allies."_ This
   party is explicitly **non-Honour**, so casting it on an enemy boss is correct as written. (Flagged
   because the video source presents the Honour restriction without that qualifier.)

2. **Shield of Thralls is undersold.** The plan describes it as _"10 temp HP to self/ally, and the
   gateway to Freecast."_ `[W]` confirms the 10 temp HP but adds: _"If these temporary hit points are
   lost due to incoming damage, the shield **bursts, possibly Stunning nearby foes**"_ — a **3 m**
   explosion, **recharging on a SHORT rest**, lasting until long rest. That makes it a repeatable
   precast area-stun, best on a frontliner. **Charles never gets it**, and he is the frontliner.
   ⚠️ But note `[W]`: _"Can only have temporary hit points from one source"_ — it competes with his
   Armour of Agathys.

3. **Ability Drain (A-tier) is taken by nobody** — see Asterion above. `[W]` it drains **the ability used
   for the attack roll**, so it belongs on **Charles and Asterion** (melee → enemy Strength) and is
   worthless on **Gale**, whose spell attacks would drain Charisma.

4. **Gale's power list was written against an obsolete assumption, and is now rewritten.** `[W]` confirms
   _"All bonuses to spell save DC such as Arcane Acuity or Arcane Enchantment will also apply to illithid
   powers"_ — so his **DC 27 is real**, and the old "no save-based powers, his DC is ~13" rule (a relic of
   the dropped Tempest dip) is void. The rewrite is also built around his action economy: his Action and
   Bonus Action are both committed to Scorching Ray and he is not taking Awakened, so **reactions and
   toggles are worth far more to him than Actions**:
   - **Psionic Dominance** — the best pick in the tree for him, above Freecast. A **Reaction** that
     nullifies an enemy spell of level ≤ his proficiency bonus, **no roll and no save either side**.
   - **Freecast** stays core. `[W]` both its caveats confirmed: disabled by equipping/unequipping a
     **ranged** weapon, and reset by another character applying a condition such as Guidance.
   - **Black Hole** — the 6 m pull needs no save; the Slow rides his DC 27. Clusters a pack into one Fireball.
   - **Stage Fright** — WIS save, **enemies only, no friendly fire**: disadvantage on all their attacks.
   - ⚠️ **Never press Concentrated Blast** — `[W]` it _"ends the caster's active Concentration spell when
     cast,"_ and it sits free in his bar right next to Twinned Haste.

5. **Two false alarms, checked and cleared:**
   - **Mind Sanctuary is safe for this party.** The alarming clause — that it grants Hastened instead and
     _"removes and prevents other sources of Slowed or Hastened,"_ making an already-hasted creature
     immediately Lethargic — is `[W]` explicitly marked **"(Honour Mode only)"**. This guide is
     non-Honour, so Bonbon can keep it. It would be a party-breaker in Honour.
   - `[W]` **Shield of Thralls' burst stun is a flat DC 15 INT save**, *not* scaled by Arcane Acuity — so
     it is a bonus on Charles, not a plan.
   - `[W]` **Mind Blast's cone targets all creatures**, friendly fire included, unlike Stage Fright.

4. **Luck of the Far Realms auto-triggers on threshold crits** — see the Charles hazard above. This is
   the most important correction in the tadpole section.

### Unverified in either source set
The refund-on-commune structure, the commune-vs-eat mechanic, all tadpole **costs**, and the
"newest level-1 class casting stat" DC rule are `[P]` — asserted by the plan and confirmed by neither
the videos (which cover only the inner and middle rings, with no costs at all) nor the wiki pages read.
They may well be right; they are simply unconfirmed here.

---

# Part 4 — Repo / content fixes

Independent of build decisions, these are content-integrity issues:

1. **Missing loot entries for assigned items.** `Gloves of Soul Catching` and `Boots of Uninhibited
   Kushigo` are assigned in `asterion.md` but absent from `content/loot.md`, so they never appear on
   the loot checklist. Add both (locations verified above).
2. **Add the Echo of Abazigal stock** to the Murder Tribunal area: Craterflesh Gloves, Bhaalist Armour,
   Assassin of Bhaal Cowl.
3. **Add Drakethroat Glaive** to Act 2 (Roah Moonglow, Moonrise Towers).
4. **Promote `Spidersilk Armour`** from `core: false` and assign it to Gale.
5. **Promote `The Whispering Promise`** from `core: false` and assign it to Bonbon.
6. **Record a location for Boots of Speed**, or note deliberately that it is skipped — `[V]` ranks it
   #14 and it is absent from `loot.md` entirely. Note `[V]` also flags it as **bugged** (the
   opportunity-attack rider reportedly applies to the wearer), so this is a "record it" item, not a
   "swap to it" item.
7. **Bonbon's background** — resolve "Entertainer or Guild Artisan" to match `proficiencies.md`.
8. **This file replaced a stale review** describing an entirely different party. Its Arcane Acuity
   "7-stack cap" claim was wrong: `[W]` _"Arcane Acuity has a maximum Duration: 10 turns"_ — the
   current content's cap of 10 is correct.

---

# Part 5 — Where the sources disagree, and what they don't cover

**Honest limits of this review:**

- **No video in the set gives a Paladin/Warlock, Sorcadin, or Sorlock numeric split.** No "7/5", no
  "6/6". Charles's and Gale's splits are *unendorsed*, not contradicted.
- **The Hat of Fire Acuity — called "THE build-defining item" twice in our own files — appears in none
  of the six item/party videos**, nor does the Arcane Acuity mechanic or the Strange Ox. This is not
  evidence against it (the items guide is Act 1 only), but the plan's central pillar has zero
  corroboration from this source set. The mechanic itself is confirmed `[W]`.
- **The class ranking video is explicitly a personal-favourites list** (_"how cool and fun is it?"_),
  not a balance claim. It ranks Draconic 2nd-worst of four Sorcerer subclasses and Fiend worst of four
  Warlock patrons — both relevant to Gale, and both to be weighted accordingly. Gale's Fiend pick is
  for the **Command spell list**, not for the patron's power.
- **The videos contradict each other** on: Bard college (Valor for fun vs Swords for mechanics),
  Paladin oath (Vengeance vs Devotion), Elemental Adept (B-tier generally, near-mandatory in the Ice
  build), and Arcane Archer (last in the class video, a "broken build" in another).
- **Honour-mode framing** runs through most sources. This party is non-Honour, which is why Deepened
  Pact + Extra Attack stacking, Perilous Stakes on enemies, and save-scumming the Zaith'isk all remain
  valid here.
- **28 load-bearing mechanics were fact-checked against the wiki; 21 came back fully confirmed.** The
  seven that did not are listed in their character sections above. The most consequential are
  **Spellmight per ray** (never addressed anywhere) and **Command's spell slots** (implied, uncited) —
  both flagged in Part 6 as confirm-in-play rather than presented as settled.

---

# Part 6 — Ranked action list

**Do these first — cheap, high impact:**

1. **Gale drinks Elixir of Vigilance every long rest.** +5 initiative, replaces the Alert feat he
   cannot afford. 25 gp. *(§1)*
2. **Charles takes Aid** at Paladin 5. Party-wide +5–15 max HP, no concentration, one L2 slot. *(§3)*
3. **Bonbon wears The Whispering Promise** and uses Healing Word to trigger it — concentration-free
   Bless for the party, and it frees Charles's concentration lane. *(§2)*
4. **Gale wears Spidersilk Armour from Act 1** — CON-save advantage protects Twinned Haste 2 acts
   earlier, for 1 AC. *(Gale)*
5. **Fix the four missing loot entries** so the checklist is complete. *(§4)*

**Then decide these explicitly:**

6. **Craterflesh Gloves replace Helldusk Gloves** on Charles in Act 3 (~+30 damage per nova turn). *(§4)*
7. **Move Luck of the Far Realms from Charles to Asterion** — it auto-wastes on crit-threshold builds. *(§3)*
8. **Add Ability Drain** (A-tier, free passive, taken by nobody). *(Asterion)*
9. **Charles carries the Staff of Arcane Blessing to cast Bless**, giving Gale +1d4 per ray. *(§2c)*
10. **Buy the Drakethroat Glaive** in Act 2; Gale Twins the enchant onto two weapons per long rest. *(§6)*
11. **Reconsider Bonbon's second Magical Secret** — Counterspell is the party's third; Globe of
    Invulnerability or Heroes' Feast are otherwise unreachable. *(Bonbon)*
12. **Give Charles Shield of Thralls** for the repeatable short-rest area stun — but drop Armour of
    Agathys, since temp HP sources do not stack. *(§3)*
13. **Decide the Adamantine question** — two ores currently buy two benched armours. *(§5)*

14. **Treat Markoheshkir's Flame of Wrath as a per-fight toggle, not a permanent attunement** — its
    Heat tick is amplified by Gale's own Callous Glow Ring and strips 2 Arcane Acuity turns per hit. *(Gale)*

**Confirm in play — in priority order:**

15. **Does Spellmight Gloves' +1d8 apply per ray or once per spell?** The difference is roughly +31
    damage versus +4.5 on a 7-ray cast, and decides whether the gloves are best-in-slot or a trap. Test
    on the first cast after acquiring them.
16. **Can Gale cast Command from Sorcerer slots, or only the pact slot?** Gates his entire control lane
    and the value of the Warlock dip. Evidence leans yes, but it is uncited. Check at character level 7.
17. Whether Drakethroat's Elemental Weapon actually holds concentration (its details say Concentration;
    its condition says "until long rest").
18. Whether a `Light`-lit character registers as Illuminated for the Coruscation Ring (already flagged
    in `gale.md`).
