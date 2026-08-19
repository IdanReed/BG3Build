# Cephalopocalypse Lockadin Video vs Charles — Build Comparison and Change Review

Comparison of the Patch 8 Paladin/Warlock guide against the Charles build, plus the reviewed change batch and open decisions.

- Video: EVEN MORE BROKEN — [Re-Updated] BG3 Minthara / Wyll Paladin / Warlock Honour Build Guide
- Video ID: `XepUM_mU1qY` · Channel: Cephalopocalypse · Duration: 45:10
- Transcript: `video_transcripts/XepUM_mU1qY.md`
- Structured summary: `video_summaries/EVENMOREBROKEN-[Re-Updated]BG3Minthara-WyllPaladin-WarlockHonourBuildGuide.md`
- Build under review: `content/characters/charles.md` (717 lines, post-itemization-rebuild)
- Status: **analysis only — no build changes applied**

> **Revision note.** First written against the pre-pull Charles. Re-reviewed after the 23-commit
> itemization rebuild, which materially changed the Charles side: Inquisitor's Might activated,
> Hunger of Hadar and Repelling Blast added, the Staff of Arcane Blessing routine introduced,
> heavy armour solved via Helldusk, and the full three-act itemization rebuilt.

---

## 1. The framing that governs everything

The video presents two builds, and this playthrough is on the second one's difficulty tier:

- **Video primary:** Paladin 2 / Warlock 10 — built *specifically* because Paladin and Pact-of-the-Blade Extra Attack **do not stack in Honour Mode**.
- **Video Tactician-or-lower variant:** Paladin 5 / Warlock 7 — three attacks per round.
- **Charles:** Paladin 7 / Warlock 5. `meta.md` sets `mode: non-Honour`.

Comparing Charles to the headline Paladin 2 / Warlock 10 is the wrong axis — that build exists to dodge a rule this run isn't using. The real comparison is **Paladin 5 / Warlock 7 vs Paladin 7 / Warlock 5**, and both reach three attacks. Charles has shifted two levels from Warlock to Paladin.

---

## 2. What the itemization rebuild already resolved

Four gaps flagged in the first pass are now closed:

| First-pass finding | Current state |
|---|---|
| No Repelling Blast | **Taken** — third invocation, with a note that invocations can't be swapped, so the respec is the only chance |
| No Hunger of Hadar | **Taken** — one of six Warlock 5 spells, rated S tier, "Charles is the party's only possible carrier" |
| Third invocation unrecorded | **Resolved** — Devil's Sight, Agonising Blast, Repelling Blast, explicitly three not two |
| Locked out of heavy armour | **Moot** — Helldusk Armour carries its own proficiency passive ("You are considered Proficient with this armour while wearing it"), so he wears the best chest in the game at AC 21 anyway |

So the video's signature **Hunger of Hadar + Repelling Blast** loop is now available to Charles. That supersedes the earlier "okay with losing that combo" decision — he has it.

Two first-pass findings survive unchanged: the nova block still says "full 8-slot dump" while listing 7 smites, and Gloves of Battlemage's Power still appears nowhere in `content/`.

---

## 3. Structural differences that remain

### 3.1 The two-level shift

| | Video (Tactician) | Charles |
|---|---|---|
| Split | Paladin 5 / Warlock 7 | Paladin 7 / Warlock 5 |
| Pact slot level | L4 → Divine Smite caps **5d8** | L3 → Divine Smite caps **4d8** |
| Shadow Blade | 3d8 | 3d8 (4d8 needs an L5 slot, i.e. Warlock 9) |
| Auras | **none** | Aura of Protection (Pal 6) + Aura of Hate (Pal 7) |
| Total smite fuel | ~4 slots | **~9 slots** |
| Warlock extras | Accursed Specter, Phantasmal Killer, +2 spells | none of these |

Neither video variant has a single aura. Charles's two extra Paladin levels buy Aura of Protection (+CHA to saves for him *and* the party — now load-bearing, since it is the first listed mitigation for the Risky Ring's save disadvantage) and Aura of Hate.

The smite-fuel row is the bigger story: the 973-damage nova is only possible because of Paladin 7's slot table. The video's Paladin 2 has two L1 slots and cannot dump eight. **The video optimizes sustained per-swing damage; Charles optimizes one enormous crit-nova turn.**

### 3.2 Arcane Acuity is on a different character — deliberately

The video's second "broken combination" is Gloves of Battlemage's Power + Band of the Mystic Scoundrel. Charles has neither; both the Band and the Helmet of Arcane Acuity are Bonbon's, who stacks Acuity far faster on hand-crossbow hits. **The video's build is a self-sufficient damage *and* control platform; Charles is a damage platform with control delegated.** Correct for a four-person party, a hole solo — which is what the video optimizes for.

### 3.3 Act 1 is a different game plan

The video self-casts Darkness from Warlock 3 and fights in it continuously. Charles stops Warlock at 2 through Act 1 to rush Paladin, so he has no Shadow Blade and no self-cast Darkness until the char-9 respec. His substitute is more sophisticated than anything in the video: **Arrows of Darkness are concentration-free**, so he gets Devil's Sight advantage *while* holding Bless / Divine Favour / Hex and powering Strange Conduit. The video hits this exact concentration conflict and never finds the workaround.

The rebuild added a refinement the video has no equivalent for: **place the cloud so Charles is inside and the target is not**, because a Darkness cloud blocks ranged attacks *into and out of* itself — an enemy standing inside it is one Gale cannot shoot.

### 3.4 Weapon philosophy

The video: *"you don't need to pick a weapon, so other characters can use whatever weapons you have."* Charles spends a feat on **Dual Wielder** purely to keep Phalar Aluve off-hand for party-wide Shriek — 1d4 Thunder per qualifying damage instance, which on Gale's 3–7 Scorching Ray hits is worth roughly 7d4 per cast. That is a party-value argument the video never makes because it never considers a party.

Feat totals are identical (2 each). Charles reaches CHA 20 via Hag's Hair + Mirror of Loss with no ASI — better than the video's Hair + one ASI, and the video never mentions the Mirror of Loss.

### 3.5 Initiative — still the one place Charles is worse

The video names initiative as the build's **single biggest structural weakness** and prescribes DEX 16 plus the **Hellrider Longbow** for a passive +3 in an otherwise unused slot.

Charles is DEX 14, and the rebuild states plainly he "has the party's worst initiative at **d4+2**." Meanwhile his ranged slot is described twice as effectively dead: *"a Darkness cloud blocks ranged attacks into and out of itself, so on any turn he plays his cloud correctly he cannot shoot out of it."*

**A dead slot and the party's worst initiative is exactly the case the video's Hellrider Longbow answers.** +3 on a d4+2 roll is close to doubling it. See §7.

### 3.6 Spell breadth and summons

Charles still has no **Accursed Specter** (Warlock 6) and no **Minions of Chaos** (Warlock 9) — the video's build has two summons, valued especially for solo play. He also has **no Shield spell**, which the video rates highly; see §8.7 for the inconsistency there.

---

## 4. Where both builds independently agree

Shadow Blade as core weapon · Resonance Stone psychic doubling · Ring of Arcane Synergy off Booming Blade · Killer's Sweetheart · Boots of Striding (concentration → immune to prone/forced movement) · Amulet of Misty Step · Knife of the Undermountain King as an off-hand crit stick · Booming Blade · Defence fighting style · Devil's Sight + Darkness · Savage Attacker · CHA 17 plus a Hair · Counterspell · Command · Hunger of Hadar + Repelling Blast · Bind Hexed Weapon for CHA scaling.

Two builds derived independently landing on that much overlap is a good sign the core is sound.

---

## 5. Where Charles's file is more rigorous than the video

- **Resonance Stone risk handling** — no effect on Undead or Constructs, gives *allies* psychic vulnerability and mental-save disadvantage, 9m/6m positioning rules, holster conditions, and an expectation that it stops working after Act 2.
- **Risky Ring honesty** — "disadvantage on saves roughly squares his concentration-failure rate," with a three-step mitigation chain (Aura of Protection → Cloak of Protection → Amulet of Greater Health cancelling it outright).
- **Feat interaction rigour** — the Duelling/GWM analysis (they can never be active on the same attack) and the Great Weapon Fighting caveat (Phalar is Versatile, not Two-Handed, so it may not apply at all).
- **Prepared-spell counts at every level** — the video never mentions that Paladin prepared count is level + CHA and re-opens on every CHA increase.
- **Booming Blade's one-cast-per-Action limit**, stated in the file, never in the video.
- **Psychic-immunity fallbacks**, which the video has no answer for at all.

---

## 6. Verified BG3 facts (bg3.wiki)

### Channel Oath economy — the hard constraint

**One Channel Oath charge, recharging on a short rest.** Every oath's actions draw on this single charge, so each short rest buys exactly one of them. The file already applies this to Inquisitor's Might vs Vow of Enmity; it applies identically to any alternative oath.

### Oath of the Crown (Patch 8)

| Level | Feature |
|---|---|
| Pal 1 | **Righteous Clarity** — Channel Oath, bonus action, **self or ally, 18m**, 10 turns, grants target's proficiency bonus to Attack Rolls |
| Pal 1 | **Champion Challenge** — nearby enemies compelled to attack only you; attacks on others at Disadvantage (BG3: does not stop them moving away) |
| Pal 1 | **Turn the Tide** — heals all nearby non-enemies; BG3 adds Paladin class level and removes the below-50%-HP restriction |
| Pal 3 | Free: **Command, Compelled Duel** |
| Pal 5 | Free: **Warding Bond, Spiritual Weapon** |
| Pal 7 | **Divine Allegiance** — reaction; ally within 1.5m takes damage → heal them 2×Paladin level, take 2×Paladin level Radiant yourself (14/14 at Pal 7) |

### Oath of the Ancients

| Level | Feature |
|---|---|
| Pal 1 | **Healing Radiance** — Channel Oath, bonus action, 3m radius: heal self and all nearby allies for prof + Paladin level + CHA, **then the same amount again next turn**. No effect on undead/constructs |
| Pal 1 | **Nature's Wrath** (restrain; BG3 makes it STR-save only), **Turn the Faithless** |
| Pal 3 | Free: Speak with Animals, Ensnaring Strike |
| Pal 7 | **Aura of Warding** — you and allies within 3m have **Resistance to all spell damage**, permanent. Does not stack with other resistances |

### Paladin level-7 oath features, side by side

Devotion → Aura of Devotion · **Ancients → Aura of Warding** · **Crown → Divine Allegiance** · Vengeance → Relentless Avenger · **Oathbreaker → Aura of Hate**

### Gloves of Battlemage's Power

- **Reithwin Tollhouse, Act 2** — locked opulent chest, second floor. Also Strength saves +1.
- **Confirmed triggers:** any smite spell **and** Divine Smite; **Booming Blade**; weapon attacks with **Shadow Blade**. Casting a smite spell then reacting with Divine Smite **triggers twice**.
- Arcane Acuity: +1 to **spell attack rolls and spell save DC only** per remaining turn, max 10. **Duration drops by 2 every time the wearer takes damage.**

### Bless delivery mechanics

- **Wrathful Smite is Concentration** (WIS save, 1d6 psychic, Frightened 2 turns).
- Charles's one concentration slot is contested by Bless, Divine Favour, Hex, Wrathful Smite, Compelled Duel, and Darkness — all Concentration.
- **Warding Bond is not Concentration.** Spiritual Weapon acts as its own creature with its own initiative turn.
- **The Whispering Promise's Bless lasts 2 turns**; the spell lasts the fight. Not a like-for-like replacement.
- Per the repo's own Broodmother's Revenge note, **any healing triggers these on-heal rings — "even a potion at full HP."**

---

## 7. Reviewed change batch

### Endorsed

**Hellrider Longbow → Charles.** Strongest change in the batch. The file itself establishes both halves of the case: worst initiative in the party at d4+2, and a ranged slot that is "a formality" because his own Darkness blocks shooting out of it. Free +3 in a dead slot.

**Keep Phalar off-hand (and Dual Wielder).** Shriek's party value is well argued and unchanged.

**Keep Wrathful Smite and lead with it on a Luck of the Far Realms swing.** Consistent — but note it is Concentration, so on that turn he is not holding Bless, Hex, or Darkness. Use an Arrow of Darkness for the cloud instead. See §7 Bless answer.

**Band of the Mystic Scoundrel stays on Bonbon.** Correct; she stacks Acuity far faster.

### Q: Paladin or Warlock first, if never switching from Luminous Armour?

**Answer: Warlock first — unchanged, and now for a stronger reason.**

| First-class effect | Paladin 1 | Warlock 1 | Verdict |
|---|---|---|---|
| Saving throws | WIS + CHA | WIS + CHA | **Identical** |
| Heavy armour | Yes | No | **Never needed** — Helldusk is self-proficient |
| Level-1 HP die | d10 | d8 | +2 HP to Paladin |
| Skills | Athletics, Insight, Intimidation, Medicine, Persuasion, Religion | Arcana, Deception, History, Intimidation, Investigation, Nature, Religion | File takes Deception + Religion; Bonbon is the face |
| Shields + martial | Yes | Yes | Same |

+2 max HP justifies nothing, and heavy armour proficiency turns out to be unnecessary at every point in the plan. More decisively: **for levels 1–8 Warlock must be first regardless** — at STR 8, a Paladin-1 opening swings at −1 with no Charisma scaling until Bind Hexed Weapon arrives.

⚠ The premise needs checking though: the current file **does not** stay on Luminous Armour. It runs Luminous (Act 1) → **Adamantine Scale Mail** (Act 2) → **Helldusk Armour** (Act 3), and the Adamantine step is specifically justified as crit immunity to protect concentration under the Risky Ring. All three are legal without heavy proficiency. See §8.5.

### Q: Bless vs Darkness concentration at char 9? And how does the party get Bless?

**Answer: the party already has a working non-concentration Bless engine, and it needs no oath change.**

Bonbon wears **The Whispering Promise** and has bonus-action **Healing Word**. Her heal Blesses the target, costs no concentration, and per the repo's own note fires *even at full HP*. The file already frames the ring as covering "char 1–3 and any fight where Charles concentrates on Hex or Darkness instead."

Post-respec the file's own nova assumptions say Darkness holds concentration and *"Wrathful Smite/Hex/Bless are out."* So **Charles already isn't the Bless source after char 9** — that is the existing plan, not a gap.

What Charles's concentration Bless uniquely buys is the **Staff of Arcane Blessing** rider: Bless cast while wielding the staff also applies **Mystra's Blessing** (+1d4 spell attack rolls), worth +1d4 accuracy on each of Gale's 3–7 rays. The ring's version does **not** get this. So the real trade is:

| | Charles concentrates on Bless + staff | Whispering Promise delivers Bless |
|---|---|---|
| Bless on party | Yes, whole fight | Yes, **2 turns only** |
| Mystra's Blessing for Gale | **Yes** | No |
| Charles's concentration | Consumed | **Free for Hex / Darkness / Wrathful Smite** |
| Strange Conduit + Boots of Striding | Live (any concentration works) | Live only if he holds something else |

**For this build, the ring wins on nova turns.** Two turns of Bless covers the entire nova, and freeing the slot for Hex is roughly +1d6 per hit across ~7 hits. Keep the staff routine for long fights where Gale is casting repeatedly.

**On your Hellrider's Pride idea — the mechanic works, the slot does not.** Thrown healing potions splash and heal multiple targets, so one throw from someone wearing both Whispering Promise and Hellrider's Pride would Bless *and* grant Bludgeoning/Piercing/Slashing resistance party-wide, no concentration, no Channel Oath charge. That is the best version of the idea.

The obstacle is that Hellrider's Pride is **gloves**, and `loot.md:53` says exactly why it is unassigned: *"the glove slot is spoken for on every member — Bonbon wears Gloves of Dexterity (the #1 item), Charles Gloves of Baneful Striking, Asterion Bracers of Defence, Gale Gloves of Belligerent Skies."* Adding it means dropping one of those. On Charles the glove slot is now **quadruple**-contested (Baneful Striking / Helldusk / Craterflesh / your Battlemage's Power request), so he is the worst candidate.

**On Oath of the Ancients — you intuited the right subclass.** Healing Radiance is a *better* Whispering Promise trigger than Crown's Turn the Tide, because it heals the whole group **twice** (this turn and next), refreshing the 2-turn Bless. And **Aura of Warding beats Divine Allegiance at Paladin 7 by a wide margin** — party-wide resistance to all spell damage, which also halves Gale's own fire splash on allies. If an oath change is happening, Ancients is the stronger target. It still costs Aura of Hate and both advantage sources; see §8.1.

Two caveats on any Channel-Oath-based Bless plan: **one charge per short rest**, so Healing Radiance or Turn the Tide *replaces* Righteous Clarity / Inquisitor's Might that rest; and Healing Radiance's radius is only 3m, so the party must be clustered.

---

## 8. Open decisions

### 8.1 The oath decision is now a three-way, and the cost of leaving Vengeance→Oathbreaker went up

The rebuild **activated Inquisitor's Might** as "THE ACT 1 DAMAGE BUTTON, live from character level 3," with three arguments the old file didn't have:

1. +CHA radiant on every weapon hit for 2 turns, which **triggers Luminous Armour's Radiating Shockwaves**.
2. **9m range, can target an ally** — on Asterion's 4–6 unarmed hits per turn it extracts roughly three times what it does on Charles's 1–2 swings.
3. The **Daze has no saving throw at all**.

Vengeance also hands over free **Hold Person** at Pal 5 — S tier, and the file notes it lets Charles "set up his OWN auto-crit nova instead of waiting on Bonbon to supply the Hold." That is the setup his entire nova depends on.

| | Vengeance → Oathbreaker (current) | Crown | Ancients |
|---|---|---|---|
| Channel Oath (1/short rest) | Inquisitor's Might / Vow of Enmity → Spiteful Suffering | Righteous Clarity / Champion Challenge / Turn the Tide | Healing Radiance / Nature's Wrath |
| Pal 7 | **Aura of Hate** — +CHA melee damage, doubled by the Stone | Divine Allegiance — reaction heal-swap, self-damaging | **Aura of Warding** — party halves all spell damage |
| Free oath spells | Bane, Hunter's Mark, Hold Person, Misty Step → Hellish Rebuke, Inflict Wounds, Crown of Madness, **Darkness** | Command, Compelled Duel, Warding Bond, Spiritual Weapon | Speak with Animals, Ensnaring Strike |
| Advantage on demand | **Vow of Enmity** + **Spiteful Suffering** | none | none |
| Oath break needed | Yes | No | No |

**The damage cost of dropping Aura of Hate:** +5 melee weapon damage, and because flat bonuses ride the weapon's damage type, the Resonance Stone **doubles it to +10 per swing** — roughly +65 across a 7-swing nova. Righteous Clarity's +4 to attack rolls does not come close, and it is **largely redundant** — the Risky Ring already grants advantage on *all* attacks from Act 2 onward, which is what actually drives the crit nova.

**Hidden knock-on:** the char-9 efficiency flag says don't spend a Warlock pick on Darkness, because Oathbreaker grants it free at char 10 — take Hex instead. **Under Crown or Ancients, Darkness is not a free oath spell**, so that pick must go back to Darkness and Hex is lost. Invocations and Warlock spells can't be swapped later, so this is a one-shot decision at the respec.

My read: **keep Vengeance → Oathbreaker.** The accuracy itch is already answered by Risky Ring, Darkness Arrows, Bless, and Vow of Enmity in Act 1. If you still want to switch, switch to **Ancients**, not Crown — Aura of Warding is a real party-wide defensive aura, where Divine Allegiance is a self-damaging reaction competing with Divine Smite confirmation, Shield, and Counterspell.

### 8.2 Gloves of Battlemage's Power — I'd now argue against it

The item is better than I first assumed (it triggers on Shadow Blade swings, Booming Blade, *and* every smite, twice when a smite spell chains into Divine Smite). But with the Band on Bonbon, Arcane Acuity buffs **spell attack rolls and spell save DC only — nothing for Shadow Blade swings**. His save-DC uses are Command as a mass disable, Wrathful Smite, and illithid powers (`tadpole.md:10`: DC = newest class's casting stat + Arcane Acuity).

Against that, the competition is stiff:

| Glove | Act | Value |
|---|---|---|
| **Baneful Striking** | 1–2 | −1d4 to the target's saves — lowers enemy saves for **Asterion's Stun and both casters**, not just Charles |
| **Helldusk** | 3 | +1d6 Fire per hit ≈ +17/nova, plus wiki-confirmed +1 to **all** attack rolls |
| **Craterflesh** | 3 (Bhaal) | ≈ +49/nova on a full auto-crit turn |
| **Battlemage's Power** | 2 | +DC on spells that are mostly someone else's job; **decays 2 turns per hit taken**, and he is the frontliner |

Baneful Striking arguably delivers more *party* control than Battlemage's Power delivers Charles-only control, and the decay clause is worst on exactly this character. Recommend against unless he becomes the primary Command / illithid controller — in which case it displaces Baneful Striking in Act 2 only.

Either way, the item still needs a `loot.md` entry with the Tollhouse location.

### 8.3 "Keep boots of stormy" — still needs disambiguating

Charles has **Boots of Striding** (Act 1–2) → **Helldusk Boots** (Act 3). **Boots of Stormy Clamour is Gale's.** If you meant Striding, nothing changes — though note the file already replaces it in Act 3 with Helldusk Boots, which do the same anti-prone job *plus* turn one failed save per turn into a success, the direct answer to the Risky Ring.

### 8.4 Removing psychic-immunity fallbacks

Dropping Charge-Bound Warhammer and Nyrulna is fine for concision, but Shadow Blade is pure psychic — against a psychic-immune enemy his main hand does nothing. Suggested one-liner: *"vs psychic-immune, bind Phalar main-hand instead"* — trivially available since Phalar is already in the off-hand and is Slashing. Keep the Resonance Stone holstering guidance; that protects the whole party and is a separate concern.

### 8.5 The Luminous Armour premise

Your question assumed never switching, but the file switches twice, and the middle step is load-bearing: **Adamantine Scale Mail's crit immunity** exists because "a critical hit roughly doubles the concentration-save DC, and he is holding Bless, Hex or Darkness in every fight while wearing a ring that gives him disadvantage on that save." Staying on Luminous forfeits that and 1–4 AC. Confirm whether you actually want to freeze the chest slot, or only meant that heavy armour is off the table.

### 8.6 Hunger of Hadar is now in, which reopens a concentration question

Charles now carries the video's S-tier crowd-control spell, but it takes the same slot as Darkness. The file frames it as a per-fight choice. Worth noting he cannot run Hunger of Hadar *and* the Devil's Sight advantage lane from self-cast Darkness — unless he uses an **Arrow of Darkness** for the cloud, which is the same trick that solves the Bless and Wrathful Smite conflicts. That makes arrows worth carrying well past Act 1, which the current `prog-consumables` row does not say (it has them "stop mattering" after the respec).

### 8.7 Shield may have fallen out of the build by accident

The `spells.recommended` list still has **Shield** at "char 1 (Hexblade L1 expanded)", but the char-1 leveling row corrects that Hexblade's expanded list is **not free** — "you still spend a spell known pick" — and picks Hex + Armour of Agathys instead. Shield then appears in no leveling row and not in the six Warlock 5 respec picks. So Charles likely has **no Shield spell at all**, while the file still recommends it. Either the spells entry is stale or a pick is missing.

---

## 9. Follow-through if the batch is applied

1. **Recompute the nova** if Aura of Hate goes — the `7d8 + 15` flat almost certainly includes its +5, doubled by the Stone.
2. **An oath change deletes the oath-break apparatus** (concision win): the char-3/char-5 keep-intact notes, the "⚠ Keep the oath intact until the Stone respec" line in `creation.notes`, and the char-9 break step.
3. **Oathbreaker-dependent entries** would need removing: Spiteful Suffering, Crown of Madness, and Hellish Rebuke's "returns free as an always-prepared Oathbreaker spell."
4. **Re-point the char-9 Warlock pick** back to Darkness under Crown/Ancients, losing the Hex option the efficiency flag recommends.
5. **Hellrider Longbow** replaces the Dual Hand Crossbows outright — special arrows fire from bows, melee and ranged are separate slots, and the file already calls the crossbow slot a formality. Update `prog-ranged` too.
6. **Cross-file propagation:** `class:` and `role:` lines, the char-3/5/9 oath rows, `party.md` loadout and respec rows, and a new `loot.md` entry for Gloves of Battlemage's Power. `tools/check_itemization.py` exists now — run it after edits.
7. **Minor:** reconcile "full 8-slot dump" with the 7 smite lines (Paladin 7 + Warlock 5 has ~9 slots).

---

## 10. Bottom line

Charles is not a worse version of the video's build; it's the same chassis tuned for a different objective. The video builds a **self-sufficient solo Honour Mode generalist**. Charles is a **party-embedded nova striker** — deep Paladin for two auras and nine smite slots, control delegated to Bonbon, Phalar Shriek and the Staff of Arcane Blessing feeding Gale, crit-fishing via Risky Ring and Half-Orc.

Given the party context, Paladin 7 / Warlock 5 is likely **stronger** than the video's Paladin 5 / Warlock 7. The itemization rebuild also closed the gaps the first pass found, so the remaining honest deltas are **initiative** (fix with the Hellrider Longbow) and **no summons**.

Of the requested changes: the Hellrider Longbow is a clear win, the Bless fix needs no oath change at all, and the two I'd push back on are **the oath switch** (§8.1 — costs ~+65/nova and both advantage sources for accuracy Risky Ring already provides) and **Gloves of Battlemage's Power** (§8.2 — a control-DC glove on a character whose control is someone else's job).
