# Cephalopocalypse Lockadin Video vs Charles — Build Comparison and Change Review

Comparison of the Patch 8 Paladin/Warlock guide against the repo's current Charles build, plus the reviewed change batch and open decisions.

- Video: EVEN MORE BROKEN — [Re-Updated] BG3 Minthara / Wyll Paladin / Warlock Honour Build Guide
- Video ID: `XepUM_mU1qY` · Channel: Cephalopocalypse · Duration: 45:10
- Transcript: `video_transcripts/XepUM_mU1qY.md`
- Structured summary: `video_summaries/EVENMOREBROKEN-[Re-Updated]BG3Minthara-WyllPaladin-WarlockHonourBuildGuide.md`
- Build under review: `content/characters/charles.md`
- Status: **analysis only — no build changes applied yet**

---

## 1. The framing that governs everything

The video presents two builds, and this playthrough is on the second one's difficulty tier:

- **Video primary:** Paladin 2 / Warlock 10 — built *specifically* because Paladin and Pact-of-the-Blade Extra Attack **do not stack in Honour Mode**.
- **Video Tactician-or-lower variant:** Paladin 5 / Warlock 7 — three attacks per round.
- **Charles:** Paladin 7 / Warlock 5. `meta.md` sets `mode: non-Honour`, and `party.md:253` flags Deepened Pact stacking as non-Honour.

Comparing Charles to the headline Paladin 2 / Warlock 10 is the wrong axis — that build exists to dodge a rule this run isn't using. The real comparison is **Paladin 5 / Warlock 7 vs Paladin 7 / Warlock 5**, and both reach three attacks. Charles has shifted two levels from Warlock to Paladin.

---

## 2. Structural differences

### 2.1 The two-level shift

| | Video (Tactician) | Charles |
|---|---|---|
| Split | Paladin 5 / Warlock 7 | Paladin 7 / Warlock 5 |
| Pact slot level | L4 → Divine Smite caps **5d8** | L3 → Divine Smite caps **4d8** |
| Shadow Blade | 3d8 | 3d8 (4d8 needs an L5 slot, i.e. Warlock 9) |
| Auras | **none** | Aura of Protection (Pal 6) + Aura of Hate (Pal 7) |
| Total smite fuel | 2 pact L4 + 2 paladin L1 ≈ 4 | 2 pact L3 + 3 paladin L2 + 4 paladin L1 ≈ **9** |
| Warlock extras | Accursed Specter, Phantasmal Killer, +2 spells, +1 invocation | none |

The video never notices this trade-off because its Paladin dip is only ever 2 or 5 levels — **neither video variant has a single aura.** Charles's two extra Paladin levels buy:

- **Aura of Protection** — +CHA to saves for Charles *and the party*. His file already uses it to offset Risky Ring's save disadvantage and protect allies inside the Resonance Stone aura. The video's build eats the Stone's mental-save disadvantage with nothing to offset it.
- **Aura of Hate** — +CHA to Charles's own melee weapon damage (and nearby undead/fiends, *not* allies). At ~7 swings that's roughly +35, and as a flat bonus riding the weapon's damage type the Stone **doubles it**. That beats the +1d8 per smite Warlock 7 would have given.

The smite-fuel column is the bigger story: the 973-damage nova is only possible *because* of Paladin 7's slot table. The video's build cannot dump eight slots — Paladin 2 has two L1 slots. **The video optimizes sustained per-swing damage; Charles optimizes one enormous crit-nova turn.**

Charles's Half-Orc Savage Attacks die also partly refunds the lower smite cap. The video's race list never contemplates this — it suggests Drow, Halfling, Duergar, Wood Elf, all Darkness- or d20-economy picks, none crit-focused.

### 2.2 Subclass

The video's headline Patch 8 buff is **Oath of the Crown's Righteous Clarity**. Charles runs Oath of Vengeance temporarily, then breaks to **Oathbreaker** for Aura of Hate and Spiteful Suffering. Righteous Clarity appears nowhere in `content/`. (Superseded — see §7.)

### 2.3 Heavy armour and level-1 class

The video is emphatic: take Paladin at level 1 for heavy armour proficiency, because multiclassing in later never grants it. Charles takes Warlock 1 first; his file correctly documents the consequence — medium armour only, or self-proficient Helldusk.

Consequence: Charles cannot wear **Armour of Persistence**, the video's best-in-slot defensive chest. His Luminous Armour pick is arguably better-reasoned than the video's, since Radiating Shockwave triggers off Divine Smite radiant damage and Charles smites far more. (Resolved — see §7.)

### 2.4 Arcane Acuity engine is on a different character

The video's second "broken combination" is **Gloves of Battlemage's Power + Band of the Mystic Scoundrel**: because the weapon *is* a spell, every attack grants Arcane Acuity, converting the bonus action into unresistable Hold Monster / Hypnotic Pattern / Command.

Charles has neither item. The Band and the Helmet of Arcane Acuity are deliberately assigned to Bonbon (`bonbon.md:435,447`), who stacks Acuity faster with dual hand crossbows plus Flourish and has a deeper enchantment/illusion list.

Structural consequence: **the video's build is a self-sufficient damage *and* control platform; Charles is a damage platform with control outsourced to Bonbon and Gale.** Fine for a four-person party, a real hole solo — which is what the video optimizes for.

### 2.5 Act 1 is a completely different game plan

The video self-casts Darkness from Warlock 3 and fights in it continuously. Charles **deliberately stops Warlock at 2 for all of Act 1** to rush Paladin (Divine Smite at char 4, GWM at 6, Extra Attack at 7), so he has no Shadow Blade and no self-cast Darkness until the char-9 respec.

His substitute is more sophisticated than anything in the video: **Arrows of Darkness are concentration-free**, so he fights with Devil's Sight advantage *while* holding Bless / Divine Favour / Hex and powering Strange Conduit Ring. The video repeatedly hits this exact concentration conflict — it drops Hex at Warlock 5 because concentration is contested — and never finds the arrow workaround.

Also absent from the video entirely: Charles's two-handed **Phalar Aluve + Great Weapon Master** phase. The video never uses a two-handed weapon or GWM at any point.

### 2.6 Weapon philosophy and the Dual Wielder feat

The video: *"you don't need to pick a weapon, so other characters can use whatever weapons you have."* Shadow Blade is a Light shortsword, so its off-hand suggestions (Knife of the Undermountain King, Bloodthirst) pair with it **without Dual Wielder**.

Charles spends a feat on **Dual Wielder** purely to keep Phalar Aluve (Versatile longsword) in the off-hand for party-wide Shriek. His file documents the Light alternatives that would free the feat and correctly concludes Shriek's party value wins in a multi-hit party. Defensible, but the one place Charles pays a resource the video doesn't.

Feat totals are identical (2 each). Charles reaches CHA 20 via **Hag's Hair + Mirror of Loss** with no ASI — strictly better than the video's Hair + one ASI. The video never mentions the Mirror of Loss.

### 2.7 Initiative — the one place Charles is worse

The video names initiative as the build's **single biggest structural weakness** (no room for Alert) and prescribes DEX 16 plus the **Hellrider Longbow** for a passive +3 in an otherwise unused slot.

Charles takes **DEX 14 / CON 16** — the exact swap the video calls acceptable — but takes neither fix. His ranged slot holds Dual Hand Crossbows as a Darkness-Arrow launcher, Haste Helm gives Momentum rather than initiative, and Sentinel Shield's +3 is only a defensive alternative. Hellrider's Longbow sits on Bonbon as an "initiative alternative" (`bonbon.md:451`).

### 2.8 Spell breadth and summons

Warlock 5 vs Warlock 7/10 is a large gap. Charles has none of: **Accursed Specter**, **Minions of Chaos**, **Repelling Blast**, **Hunger of Hadar**, **Hypnotic Pattern**, **Confusion**, **Banishing Smite**, **Phantasmal Killer**. Hold Person and Hunger of Hadar sit in his file only as alternatives.

He therefore cannot run the video's signature **Hunger of Hadar + Repelling Blast** loop, and has **zero summons** where the video's build has two.

---

## 3. Where both builds independently agree

Shadow Blade as core weapon · Resonance Stone psychic doubling · Ring of Arcane Synergy triggered by Booming Blade · Killer's Sweetheart · Boots of Striding (concentration → immune to prone/forced movement) · Amulet of Misty Step · Knife of the Undermountain King as off-hand crit stick · Booming Blade · Defence fighting style · Devil's Sight + Darkness · Savage Attacker · CHA 17 start plus a Hair · Counterspell · Command · Bind Hexed Weapon for CHA scaling.

Two builds derived independently landing on that much overlap is a good sign the core is sound.

---

## 4. Where Charles's file is more rigorous than the video

- **Resonance Stone risk handling.** The video treats it as pure upside. Charles's file notes it doesn't affect Undead or Constructs, gives *allies* psychic vulnerability and mental-save disadvantage, sets 9m/6m positioning with Asterion carrying it, and defines holster conditions.
- **Psychic-immunity fallbacks** (Charge-Bound Warhammer, Nyrulna), with the correct note that vulnerability and resistance cancel. The video has no answer for a psychic-immune target.
- **Booming Blade's one-cast-per-Action limit** — stated in Charles's file, never in the video.
- Oath-break sequencing to avoid paying the Oathbreaker Knight before Withers will respec.

---

## 5. Mechanical details from the video worth adding

1. **You cannot chain Booming Blade + a smite spell + Divine Smite in one turn** — the reactions menu blocks it. Charles has all three, so this constrains his rotation and isn't recorded.
2. **Darkness stops ranged attacks but not thrown weapons.** Charles's whole Act 1 is darkness-based; the exception isn't noted.
3. **Hexblade's Curse has a 20% chance to apply on any hit**, not just via the bonus action.
4. The video's **untested question** — whether Booming Blade with Shadow Blade grants four Acuity stacks instead of two below Honour — is directly testable in this non-Honour run.

---

## 6. Verified BG3 facts (bg3.wiki)

Checked because the change batch depends on them.

### Gloves of Battlemage's Power

- **Location: Reithwin Tollhouse (Act 2)** — locked opulent chest, second floor, room with two locked doors. Available *before* the late-Act-2 Resonance Stone respec.
- Effect: gain Arcane Acuity when you hit with a spell or cantrip that uses a weapon. Also Strength Saving Throws +1.
- **Confirmed triggers include:** any smite spell **and** Divine Smite; **Booming Blade**; weapon attacks with **Shadow Blade**. Casting a smite spell then reacting with Divine Smite **triggers it twice**.
- Arcane Acuity: +1 to **spell attack rolls and spell save DC** per remaining turn, max 10 turns. Duration is **reduced by 2 each time the wearer takes damage**.
- Not present anywhere in `content/` — needs a `loot.md` entry.

### Oath of the Crown (Patch 8)

| Level | Feature |
|---|---|
| Pal 1 | **Righteous Clarity** — Channel Oath, bonus action, **self or ally, 18m range**, 10 turns, grants target's proficiency bonus to Attack Rolls |
| Pal 1 | **Champion Challenge** — compels nearby enemies to attack only you; attacks on others have Disadvantage (BG3 change: does not stop them moving away) |
| Pal 1 | **Turn the Tide** — heals all nearby non-enemy creatures; BG3 adds Paladin class level to the heal and removes the below-50%-HP restriction |
| Pal 3 | Oath spells: **Command, Compelled Duel** (always prepared) |
| Pal 5 | Oath spells: **Warding Bond, Spiritual Weapon** (always prepared) |
| Pal 7 | **Divine Allegiance** — reaction; when an ally within 1.5m takes damage, heal them 2×Paladin level HP and take 2×Paladin level Radiant yourself (14/14 at Pal 7) |
| Pal 9 | Oath spells: Spirit Guardians, Crusader's Mantle (out of reach at Pal 7) |

Oath-breaking triggers: breaking promises, siding against legitimate rulers, following through on criminal plots, evading arrest, refusing interrogation.

Paladin level-7 oath features by subclass, for reference: Devotion → Aura of Devotion · Ancients → Aura of Warding · **Crown → Divine Allegiance** · Vengeance → Relentless Avenger · **Oathbreaker → Aura of Hate**.

### Wrathful Smite

- Level 1 evocation. Action to cast, or Bonus Action + L1 slot on hit.
- Normal weapon damage + 1d6 Psychic; WIS save or Frightened 2 turns (full damage on save).
- **Is Concentration.** Hexblade class level 1; Paladin 2.

### Concentration conflicts (confirmed list)

Charles has one concentration slot contested by: **Bless, Divine Favour, Hex, Wrathful Smite, Compelled Duel** (all concentration), and **Darkness** (concentration).

**Warding Bond is not concentration.** Spiritual Weapon acts as its own creature with its own initiative turn and needs no bonus action to activate.

### Other

- Inquisitor's Might is **Oath of Vengeance's** Channel Oath (+CHA radiant, can Daze) — the thing being given up from the Act-1 temporary oath, not from Oathbreaker.
- Aura of Protection is **base Paladin 6**, not an oath feature — kept under any oath.

---

## 7. Reviewed change batch

### Accepted as consistent, no conflicts found

- Keep Phalar Aluve off-hand (and therefore Dual Wielder).
- Keep Wrathful Smite, leading with it over Booming Blade on a Luck of the Far Realms or otherwise important swing.
- Band of the Mystic Scoundrel stays on Bonbon.
- Accept losing the Hunger of Hadar / Repelling Blast combo.
- Give Charles the Hellrider Longbow.
- Use Gloves of Battlemage's Power.

### Q: Paladin or Warlock first, if never switching from Luminous Armour?

**Answer: Warlock first — keep it as it is.**

Heavy armour was the only strong argument for Paladin-first, and committing to Luminous Armour kills it. Full list of what first-class controls in BG3:

| First-class effect | Paladin 1 | Warlock 1 | Verdict |
|---|---|---|---|
| Saving throw proficiencies | WIS + CHA | WIS + CHA | **Identical** |
| Heavy armour | Yes | No | Irrelevant now |
| Level-1 HP die | d10 | d8 | +2 HP to Paladin |
| Skill list | Athletics, Insight, Intimidation, Medicine, Persuasion, Religion | Arcana, Deception, History, Intimidation, Investigation, Nature, Religion | Bonbon is the face (`bonbon.md:6,272`), so Persuasion is low value |
| Shields + martial weapons | Yes | Yes | Same |

+2 max HP doesn't justify anything. And for the **initial 1–8 progression Warlock must be first** regardless: Charles is STR 8, so a Paladin-1 opening swings at −1 with no Charisma scaling until Bind Hexed Weapon arrives.

This reverses the earlier "take Paladin first at the respec" suggestion, which was entirely contingent on wanting heavy armour. Helldusk Armour is self-proficient, so even it wouldn't require Paladin-first.

### Q: Bless vs Darkness concentration at char 9? And how does the party get Bless?

**Answer: neither — switching to Crown dissolves the problem.**

- **Accuracy no longer needs Bless.** Righteous Clarity is a bonus action + Channel Oath charge, 10 turns, **not concentration**, granting +proficiency — **+4** at character 9–12 versus Bless's +1d4 (avg +2.5). Strictly better. Bless was only ever a workaround for the accuracy problem Crown solves directly.
- **Darkness doesn't need to be self-cast.** Arrows of Darkness are concentration-free and do the same tactical job. Self-cast Darkness buys a bigger radius and longer duration for the price of the whole concentration slot. Keep arrows as default; treat the spell as backup for when a large or long-lived cloud is needed.
- **Spend concentration on Wrathful Smite.** Bonus synergy: **Strange Conduit Ring only pays out while concentrating**, so Wrathful Smite switches it on and the Resonance Stone doubles its 1d4 psychic. Hex is the fallback if the rider is wanted without the WIS save.

**Party Bless — nobody else can cast it.** Asterion is a Monk, Bonbon's Bard list doesn't include it, Gale is a Storm Sorcerer. Charles is the only source. Two non-concentration answers:

1. **Turn the Tide + The Whispering Promise** — Turn the Tide heals all nearby non-enemies; Whispering Promise Blesses anything healed. **Party-wide Bless from one Channel Oath charge, no concentration.** `loot.md:46-52` already has the Whispering Promise + Hellrider's Pride pair unassigned, described as a Bless-on-heal combo. Only available *because* of the Crown switch. **Verify in-game** that Whispering Promise fires off a group heal, not just single-target.
2. **Lay on Hands + The Whispering Promise** as single-target fallback (5 charges at Pal 6+), or Righteous Clarity targeting an ally at 18m.

Caveat: Righteous Clarity and Turn the Tide draw on the **same Channel Oath charge pool** — confirm how many charges Paladin 7 has, since that decides whether both fit in one short-rest window.

---

## 8. Open decisions

### 8.1 Aura of Hate → Divine Allegiance is the biggest cost, and it isn't an accuracy trade

Crown's Paladin-7 feature is **Divine Allegiance**: a *reaction* healing an adjacent ally 14 HP while dealing Charles 14 Radiant. Near-dead weight for a striker, and his reaction is already contested by Divine Smite crit-confirmation, Shield, and Counterspell.

Given up: Aura of Hate's +CHA (+5) to melee weapon damage, **doubled to +10 per swing by the Resonance Stone** — roughly +60–70 across a 7-swing nova. Righteous Clarity's +4 accuracy doesn't come close. Still defensible (Crown adds Warding Bond, Spiritual Weapon, Command free), but should be decided knowingly. Aura of Protection is kept either way.

### 8.2 Crown removes every on-demand advantage source

Vow of Enmity (Vengeance, Act 1, `charles.md:288`) and Spiteful Suffering (Oathbreaker, explicitly the "advantage/crit-fishing source when the Risky Ring isn't equipped") both vanish. Crown grants no advantage. For a build stacking crit range (Covert Cowl, Sarevok's Helmet, Knife of the Undermountain King), **advantage beats flat accuracy** — it manufactures crits, which double smite dice. Post-switch: Darkness Arrows, Risky Ring (Act 2+), Gloves of the Growling Underdog. **Act 1 before Risky Ring is the weak window.**

### 8.3 "Keep boots of stormy" — which item?

Charles has **Boots of Striding** (`charles.md:383`). **Boots of Stormy Clamour is Gale's** (`gale.md:641`). If Striding was meant, nothing changes. If Stormy Clamour was genuinely meant, that strips Gale and loses Striding's prone/forced-movement immunity, which the file ties to concentration.

### 8.4 Gloves of Battlemage's Power — what does it displace?

It's an **Act 2** item, so it displaces Gloves of Baneful Striking from Act 2 onward and competes with Helldusk Gloves in Act 3. Baneful Striking's −1d4 to target saves feeds Asterion's Stun and the casters' control; Helldusk adds fire on every hit plus spell attack/DC. Which loses?

### 8.5 Be explicit about what the Acuity is *for*

With the Band staying on Bonbon, Arcane Acuity buffs **spell attack rolls and spell save DC only** — nothing for Shadow Blade swings. Real targets: Command and Compelled Duel (free from Crown), Wrathful Smite, Champion Challenge, Eldritch Blast, and **illithid powers** — `tadpole.md:10` records "Save DC = NEWEST class's casting stat + Arcane Acuity". A genuine payoff, but a different one from the video's Band-enabled bonus-action control. The file should carry the real justification, not reasoning that no longer applies.

### 8.6 Removing psychic-immunity fallbacks leaves a live hole

Shadow Blade is pure psychic — against a psychic-immune enemy the main hand does nothing. Suggested compromise: collapse two item entries into one line, "vs psychic-immune, bind Phalar main-hand instead." Concise, no hole. Separately the **Resonance Stone holstering guidance should stay** — it protects the whole party from psychic vulnerability and mental-save disadvantage, and is not a fallback-weapon concern.

---

## 9. Follow-through the changes force

1. **Recompute the nova block.** `7d8 + 15` almost certainly folds in Aura of Hate's +5, which the Stone was doubling. The 973 figure drops materially; `assumptions` is written in Oathbreaker terms.
2. **Crown deletes the oath-break apparatus** — a concision win. Remove: "keep the oath intact until the Stone respec to avoid paying the Oathbreaker Knight," the char-3 and char-5 keep-oath-intact notes, and the char-9 break-the-oath step.
3. **Remove or rehome Oathbreaker-dependent entries:** Spiteful Suffering, Crown of Madness, and Hellish Rebuke's note that it returns as a free always-prepared Oathbreaker spell.
4. **Record Crown's free always-prepared spells:** Command (currently a Paladin prepared pick — now free, freeing a slot), Compelled Duel, plus **Warding Bond** and **Spiritual Weapon** at Pal 5. Both are free value the file lacks.
5. **Hellrider Longbow can replace the Dual Hand Crossbows outright** — special arrows fire from bows in BG3, and melee/ranged are separate slots so there's no conflict with Phalar. One slot gets +3 initiative *and* the Darkness-Arrow launcher. Confirm dropping the crossbows.
6. **Metadata and cross-file propagation:** `class:` line, `role:`, and the char-3/5/9 oath entries; `party.md:193,196,235` carry Charles's loadouts and the oath-break description; `loot.md` needs a Gloves of Battlemage's Power entry with the Tollhouse location.
7. **Third invocation pick at Warlock 5 is still unrecorded.** With Hunger of Hadar and Repelling Blast off the table it's a free pick worth naming.
8. **Minor:** the nova block says "full 8-slot dump" but lists 7 smites, while Paladin 7 / Warlock 5 has ~9 slots available. Worth reconciling.

---

## 10. Bottom line

Charles is not a worse version of the video's build; it's the same chassis tuned for a different objective. The video builds a **self-sufficient solo Honour Mode generalist** — deep Warlock for spell breadth, self-contained bonus-action control via Arcane Acuity, Righteous Clarity for accuracy, no auras, modest smite fuel. Charles is a **party-embedded nova striker** — deep Paladin for two auras and nine smite slots, control delegated to Bonbon, Phalar Shriek buffing the party, crit-fishing via Risky Ring and Half-Orc.

Given the party context, Paladin 7 / Warlock 5 is likely **stronger** than the video's Paladin 5 / Warlock 7: Aura of Hate doubled by the Stone plus Aura of Protection outweighs a 5d8 smite cap and a specter.

The two changes worth pushing back on are **§8.1 and §8.2** — Crown costs a doubled +5 damage aura and both advantage sources, in exchange for accuracy that Risky Ring may already cover.
