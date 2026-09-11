# Build notes — Asterion (The Fist in the Dark)

Why the Asterion build is what it is. `content/characters/asterion.md` is the cheat
sheet: what to take, where to get it, when to use it. Everything that explains a
choice lives here, keyed by the entry `id` or field name it came from.

Decision source: `docs/cephalopocalypse-build-review-2026-09-11.md` (the "report").
Applied here: T1-1, T2-26, T2-27, T2-28, T3-A1, T3-A3–A12, T4-V6.
Declined: T2-29, T3-A2, and the Swashbuckler / Monk 8-Thief 4 tails.

---

## Creation

**`race_notes`** — Fey Ancestry is advantage against Charm and immunity to magical
Sleep; Darkvision is what lets him operate in the Underdark and the Shadow-Cursed
Lands without a light source. The cut sentence said Graceful Cloth is Clothing
rather than armour and that Bracers of Defence work while unarmoured and
shieldless; both facts now live on the item entries that need them, which is where
a player looks.

**`stats_note` / `starting_stats`** — point-buy 8/15/15/8/15/8 is exactly 27 points,
because DEX, CON and WIS at 15 cost 9 each. The odd-score rule is the whole reason
the array looks like that: 14 and 15 are both +2, so a +1 landing on an even score
buys nothing. INT is dumped to 8 because nothing in the build touches it, and the 2
points that frees are precisely the cost of CON 14 → 15, which is what turns Tavern
Brawler's +1 into CON 16 and a real +3 instead of a wasted point.

**`ability_targets` / `ability_scores` (T2-26, applied)** — the racial +2 and the
modded Hag's Hair both go to WIS now, not DEX. Report rationale (bX5paFDOGDU 32:45):

- DEX 15 +1 = 16, 18 under the Graceful Cloth. WIS 15 +2 = 17, 18 with the Hair, 20
  with the Mirror of Loss.
- **AC is identical in every act.** The old array ended DEX 20 (+5) / WIS 18 (+4);
  the new one ends DEX 18 (+4) / WIS 20 (+5). Unarmoured Defence sums both
  modifiers, so 10 + 9 + 2 (Bracers) = AC 21 either way.
- Gains: +1 Psychic per unarmed hit from Manifestation of Mind from char 7, doubled
  by the Resonance Stone, and +1 more per hit from the Boots of Uninhibited Kushigo
  in Act 3 — roughly +12 to +16 a turn across 5–6 hits. Plus +1 on WIS saves for
  the Resonance Stone carrier, who is the member the Stone punishes most.
- Costs: −1 initiative, −1 DEX saves, −1 Sleight of Hand and Stealth. The
  initiative loss compounds with T1-1, which pushes Alert to char 11.
- This is a creation-time change, not a respec.

**`pickpocket.success_math` (T2-26 knock-on)** — at char 12 the flat bonus drops
from +13 to +12: DEX 18 (+4) + proficiency 4 doubled by Expertise (+8). The
Graceful Cloth still supplies advantage. There is no Reliable Talent floor at Rogue
3, so a low roll can still fail; most Act 1–2 targets sit well under +12 with
advantage.

**`ability_scores` WIS step / T4-V6 (party-wide, applied)** — the Mirror of Loss +2
is not guaranteed. One DC 25 Religion check per character, and a failure locks that
character out permanently, then a 60% roll per attempt. Religion is INT-based and
only Charles is proficient, at INT 8. Every build's end stats assume the +2. Plan:
Enhance Ability from Bonbon, Guidance, and a quicksave before each prayer. The
report also killed the videos' claim that the Mirror cannot be used on two
characters — the wiki says it is per character. (s50sTy53DZw 3:08;
bg3.wiki/wiki/Mirror_of_Loss)

**`creation.starting_cantrips` / leveling `Racial cantrip`** — the wiki is explicit
that a recruited companion's race-related choices carry over unchanged: "the
selectable aspects of any given race, such as a high elf's choice of cantrip, also
remain fixed" (Withers, Services). The Withers respec does not re-present it, so he
keeps whatever Larian assigned. Bone Chill would be a fine outcome — A tier,
targets AC at range, prevents healing, gives undead disadvantage on attacks — but
nothing in the build depends on the cantrip either way.

**`creation.level1_gains` (T3-A1, applied)** — the old text called Sneak Attack
"vestigial… it needs a finesse weapon, not fists". That is wrong. Sneak Attack
(Ranged) fires off any ranged weapon attack, so his hand-crossbow fallback carries
2d6 whenever he has advantage or an ally is adjacent to the target. The reaction is
set to **Ask** so it is not spent on the first low-value shot of a turn. Wiki-
confirmed (report T4-V7).

---

## Leveling

**`build_order`, `leveling` rows 8–12, `feats[Alert].at`, `creation.notes` (T1-1,
applied)** — the order is now Rogue 1 (creation) → Monk 1–6 (char 2–7) → Rogue 2
(char 8) → Rogue 3 Thief (char 9) → Monk 7 (char 10) → Monk 8 (char 11) → Monk 9
(char 12). Final split is unchanged at Open Hand Monk 9 / Thief Rogue 3, and there
is no respec.

Report rationale — raised by six reviewers (bX5paFDOGDU 36:25, IC1WiOi_nYQ 12:32,
6i-Rpr9ziqs 59:08, uY-RJbv0DhY 17:07, Ni8rrKcrMqs 15:03, bCW4Hrr7Hmw 16:44); every
video running this chassis goes Monk 6 → Rogue tail → Monk 7–9. The old order put
Fast Hands at the last level and recorded no reason for it anywhere.

- **Gain:** Fast Hands is a permanent second bonus action, so a second Flurry of
  Blows every turn. It moves from char 12 to char 9 — two more Tavern Brawler
  punches a turn (≈ +38 to +54 with the Resonance Stone) for the whole Resonance
  Stone stretch and all of early Act 3.
- **Cost:** Alert slips char 9 → 11. Evasion and Stillness of Mind slip char 8 →
  10. Ki Resonation and the d8 Martial Arts die slip char 10 → 12. Ki pool is 6 at
  char 9 instead of 8.
- **Why the cost is small here:** the videos run STR arrays with low DEX, so Alert
  is their only initiative. Asterion has DEX 16–18 plus the Mask of Soul
  Perception's +2 in Act 3, so two turns without Alert cost less. Under T2-26 the
  DEX is one point lower than it was, which is the one place the two decisions
  work against each other.

**`feats`** — only two feats in the whole build (Monk 4 = char 5, Monk 8 = char 11)
and both are spent. Tavern Brawler and Alert are the two S+ feats in the corpus's
feat tier list and nobody else in the party takes either.

**`feats[Tavern Brawler]`** — two separate effects, and the second is easy to miss:
it adds the STR modifier to unarmed attack rolls *and* damage a second time, and it
raises Strength or Constitution by 1 (base cap 20). Take the CON option, because
the Giant Strength elixir overrides STR anyway — which is why CON is bought at an
odd 15. Once STR exceeds DEX it also drives attack rolls and the Stunning Strike
DC, since BG3 monk DCs use the higher of DEX and STR; Cloud Giant (STR 27, +8) is
the ceiling. Scope note dropped from the sheet: the feat also covers Throw and
Improvised Melee Weapon attacks, neither of which requires empty hands — only the
base Unarmed Strike action needs "no melee weapons equipped", so the hands-empty
rule never blocks a thrown consumable.

**`leveling` char 1 Skills (T3-A4, applied)** — Athletics replaces Insight. Report:
on the daily Giant Strength elixir Asterion is at +9 to +12 Athletics, the party's
best Shove number, and Insight is already covered by Gale and Bonbon (Bonbon has
Expertise in it). Bonbon drinks the same elixir and already has Athletics from
Fighter 1, so this makes a second shove/grapple carrier. `content/proficiencies.md`
updated to match. Cut from the sheet: Investigation is the party's only coverage —
Charles, Gale and Bonbon all lack it. Athletics Expertise was considered and
rejected in the report's Tier 5 (Push is a save, not a contest).

---

## Spells and features

**`Stunning Strike`** — the party contribution. 1 Ki on a hit, CON save or Stunned:
auto-fails STR and DEX saves, is attacked at advantage, loses its turn. It locks
bosses and hands Charles free crits. The Resonance Stone does **not** help — per
the wiki the aura penalises INT, WIS and CHA saves only.

**`Manifestation of Mind`** — +1d4 + WIS Psychic per unarmed strike. At 4–6 hits a
turn all of it doubles under the Resonance Stone, which is how the Monk joins the
psychic engine without a Shadow Blade. Toggle to Soul or Body for radiant or
necrotic against psychic-resistant foes.

**`Celestial Haste` / `act3-ranged-asterion`** — the Action it costs to cast is paid
back by the Hasted extra Action the same turn, so casting it on turn 1 is free. It
was previously filed under Bonbon, where it did nothing: she is already Hasted by
Gale and concentrating on Hold Monster.

**`Minor Illusion`** — it would be the ideal racial cantrip (S tier: pulls creatures
toward a distraction with no save, redirects sightlines for stealth and theft, and
does not touch his INT 8), which is why it is listed. It is not a pick to make.

**`Vampire Bite` (T3-A3, applied)** — the file called the Bite "minor". Happy is +1
to all attack rolls, saves and most ability checks
(bg3.wiki/wiki/Happy_(Condition)), which is a party-wide-quality buff on a free
bonus action. Not obtainable from Gale, from corpses, or from pre-upgrade Karlach.
**Duration is unverified** — see In-game checks.

**`Ascendant Bite` / `ascension-asterion` (T2-27, applied — ASCEND)** — raised by
four reviewers (bX5paFDOGDU 4:10, SZYnp9AppYk 3:38, uY-RJbv0DhY 3:09, Ni8rrKcrMqs
2:36). Vampire Ascendant adds 1d10 Necrotic to every weapon *and unarmed* attack
(bg3.wiki/wiki/Vampire_Ascendant): at 5–6 unarmed hits a turn that is ≈ +27 to +44
in Act 3, the same order as the Gloves of Soul Catching rider, which is the
build's single biggest gear upgrade. It also grants Ascendant Bite (6d6 healing,
6d6 Necrotic, grants Happy) and Misty Escape. It is **not** doubled by the
Resonance Stone, because it is Necrotic and not Psychic.

The file previously never mentioned Ascension at all and `loot.md` marked the event
MAJOR with no number. This is a story choice; the price of refusing it is the ≈ +27
to +44 a turn above, and that is now stated in the build.

---

## Itemization — Act 1

**`staff-of-arcane-blessing`** — the staff *grants* Bless as a level 1 spell once
per long rest, so Asterion needs no Paladin dip and no class access to cast it.
That is the reason he stays a clean Open Hand Monk 9 / Thief Rogue 3. Every Bless
its wielder casts also applies **Mystra's Blessing**, a second +1d4 that lands only
on spell attack rolls — worth +1d4 accuracy on each of Gale's 3–7 Scorching Ray
rays, which is the real reason the staff sits on Asterion rather than anyone else.
Concentration then sits on the one party member with nothing else to concentrate
on. Bless at level 1 hits only three creatures: pick Charles, Gale and Bonbon and
leave Asterion out, since he benefits least from +1d4 and the other three all key
off attack rolls. Losing concentration drops the regular Bless, but the wiki notes
Mystra's Blessing persists on its own, so Gale keeps his spell-attack bonus even if
Asterion is hit. The Arcane Tower elevator buttons only appear if someone in the
party carries Bernard's Guiding Light ring.

**`corellon-s-grace`** — the staves tier list rates it S and says in the same breath
that Tavern Brawler monks replace it, so retiring it at char 5 is the intended arc,
not a downgrade.

**`dual-hand-crossbows-plus-one` (T3-A7, applied)** — the ranged set does not touch
the melee hands, so Tavern Brawler stays live while the crossbows are equipped.
Report: leave the **dual-wield toggle off**, or a single crossbow shot
automatically spends a Flurry on an off-hand shot.

**`graceful-cloth`** — Cat's Grace is +2 DEX, which under T2-26 carries him 16 → 18
rather than 18 → 20. The reason to keep it once DEX has stopped mattering is
advantage on Dexterity checks, which is advantage on every Sleight of Hand roll he
makes as party thief.

**`circlet-of-psionic-revenge`** — the constraint that picks this item: per the wiki,
"Helmets and Gloves marked as Light, Medium or Heavy Armour count as armour, and
prevent Unarmoured Defence from working". That permanently rules out Covert Cowl
(Light), the Dark Justiciar Helmet (Medium) and Shadow of Menzoberranzan. The
circlet carries no proficiency requirement, so it is legal. The +1 mental saves
printed on it are Githyanki-only and he does not get them; it is taken purely for
the retaliation, which the Resonance Stone doubles from Act 2.

**`act1-hands-asterion` options** — Bracers of Defence give +2 AC while unarmoured
and shieldless, reaching AC 21, the highest no-armour AC in the party. The Sparkle
Hands' Lightning Charges are best when he is landing 4–6 hits a turn. Gloves of
Cinder and Sizzle lose to the Sparkle Hands against metal armour or fire
resistance. Gloves of Thievery are worth less than AC or damage in a fight, so they
stay bagged — and unlike Guidance, their advantage actually shows in the pickpocket
window.

**`bracing-band`** — the wiki notes the trigger "is not just Shove", with **Flurry of
Blows: Push** named explicitly on the list. Asterion already throws Push as one of
his three Open Hand variants, so on any turn he pushes something the +1 AC is
simply always up, on the character with no armour to fall back on. Sergeant Thrinn
gives one of two rewards; this beats the Armour of Uninhibited Kushigo because
Graceful Cloth is the standing chest anyway. The Ring of Protection stays with
Gale, the party's lowest-AC body, since Asterion is already at 21.

**`deathstalker-mantle`** — the only magical cloak obtainable in Act 1 by anyone;
every other cloak in the game is Act 2 or later, which is why three of the four
cloak slots in the party stay empty until Act 2.

**`disintegrating-night-walkers`** — free Misty Step once per short rest plus
immunity to Prone and to difficult terrain from surfaces, Enwebbed and Entangled.
They do not cover Paralysed or Restrained, which the Ring of Free Action closes in
Act 3. These boots move to Gale in Act 3 once Asterion takes the Kushigo boots
(report T3-G2) — cross-file fact.

---

## Itemization — Act 2

**`resonance-stone`** — he places and carries it. Manifestation of Mind Psychic,
Psionic Overload and the Circlet's retaliation are all doubled across 4–6 hits a
turn. The aura also gives enemies disadvantage on mental saving throws, and
Command and both Hold spells are WIS saves, so anything standing near Asterion is
close to unable to resist Gale's control. It does **not** help Stunning Strike (CON
save). The aura also makes the party — and him — psychic-vulnerable and
disadvantaged on mental saves, which is what the Amulet of the Harpers answers, and
it stops working once Act 2 ends.

**`flawed-helldusk-gloves`** — across five strikes a turn the 1d4 Necrotic is roughly
+12 damage against the +2 AC the Bracers were giving, which is the right trade
while Act 2 enemies are still soft. The Bleeding it can inflict is one of the
conditions that feeds the Stormy Clamour option below. Budget the Infernal Iron
deliberately; the same pieces upgrade Karlach's engine.

**`shadow-cloaked-ring`** — the wiki names weapon **and unarmed** attacks explicitly,
which most riders do not. Nearly everything in the Shadow-Cursed Lands counts as
Lightly or Heavily Obscured or is made of shadow, so it is roughly +12 across a
full Flurry turn.

**`eversight-ring` (T3-A12, applied)** — the old text implied he could shoot out of a
Darkness cloud. He cannot, and neither can anyone else: per
bg3.wiki/wiki/Darkness_(cloud) no ranged attack crosses the cloud boundary in
either direction regardless of sight, and the report confirmed our position against
a video (m2F7dNXEwNc) that plays Eldritch Blast from inside one. What the ring
actually buys is that he is not Blinded inside the cloud, so he can melee in there
at all — the wiki's blind immunity "also allows the wearer to see through magical
darkness". Wording tightened to "fights unblinded inside the cloud".

**`opt-boots-of-stormy-clamour-asterion-a2` / `-a3` (T2-28, applied)** — new per-fight
option entries on both feet slots. Report rationale (4naQFyHry2M 24:26): Asterion
inflicts more conditions per turn than anyone in the party — Stun, Topple's Prone,
Bleeding from the Flawed Helldusk Gloves, Ability Drain from the illithid passive —
and each one adds 2 turns of Reverberation, so the next Stunning Strike CON save
lands at −2 to −4. The cost that fight is the Night Walkers' Misty Step in Acts
1–2, or the Kushigo boots' +WIS per hit in Act 3 (≈ +20 with WIS 20).

The boots are **Charles's** (2026-09-11 §3 makes them his flex pair). The standing
rule recorded in both files: whoever inflicts more conditions that fight wears
them, and Asterion only takes them when Charles is in Striding or Helldusk Boots.
Cross-file fact for `charles.md`, `loot.md` and `party.md`.

---

## Itemization — Act 3

**`boots-of-uninhibited-kushigo`** — adds his WIS modifier to every unarmed strike,
so under T2-26 that is +5 on each of 5–6 hits instead of +4. Boots are not on the
Monk armour-exclusion list, so an armour tag on late boots is never a problem for
him — the exclusion is helmets and gloves only.

**`vest-of-soul-rejuvenation`** — completes the Soul set beside the Gloves of Soul
Catching and the Mask of Soul Perception. Greater Kushigo Counter is a reaction
unarmed strike against any attacker that misses, and it carries every one of his
riders. Losing the Graceful Cloth costs advantage on Sleight of Hand, which is why
the Cloth stays bagged for theft.

**`cloak-of-displacement`** — worth more on Asterion than on Charles in Helldusk
plate, because Asterion is the only party member with neither armour nor damage
reduction. Useful wiki quirk: Displaced is not stripped by anything the game does
not count as a hit, including a successful save against a damage-dealing spell.

**`act3-rings-asterion`** — the Callous Glow Ring is deliberately not his. It needs
illuminated targets, which fights both the Shadow-Cursed Lands and Charles's
Darkness, and Gale's Coruscation chain already lights targets for his own copy.

**`act3-ranged-asterion`** — Celestial Haste is a "holder gains" action, so it needs
no bow proficiency and he never fires the bow. Gontr Mael does not drop if the
Steel Watcher Titan dies to Atrophied.

---

## Progression

**`prog-head`** — only two entries in the whole run because the Light/Medium/Heavy
armour tag rule disqualifies almost every good helmet in the game for an
Unarmoured Defence build.

**`prog-feet`** — Night Walkers through Acts 1–2, Kushigo boots in Act 3, with
Charles's Boots of Stormy Clamour borrowed per fight (T2-28). The Night Walkers
then go to Gale for Act 3 (T3-G2), which is why the hand-off timing matters.

**`prog-elixirs` (T3-A6, applied)** — Potion of Speed is a **potion**, not an elixir,
so it does not collide with the one-elixir-per-long-rest slot and stacks with Giant
Strength. It is rated S+ in `ratings.md`. Cost: before Thief 3 the potion drinks a
Flurry's bonus action, which is exactly why taking Thief 3 at char 9 (T1-1) makes
it cheap.

**`prog-ranged`** — the ranged slot was otherwise a pure fallback, which is why
spending it on a bow he never fires costs nothing.

---

## Playstyle

**Prep (T3-A3)** — the Bite is a free bonus action out of combat and Happy is +1 to
attack rolls, saves and most checks for the whole fight, so it should be habitual
rather than occasional.

**Opener (T3-A8)** — hiding outside an enemy's vision cone needs no Stealth roll at
all; the roll only happens inside a cone. Hiding while **Shift** is held hides the
whole party, which drags Charles's non-proficient Stealth into a check and usually
fails it. Release Shift.

**Turn (T3-A5)** — Topple, not Stagger, against a concentrating caster. Prone ends
concentration outright with no save (recorded in our own changelog). Stagger blocks
Reactions, which is only worth the Flurry against a caster with a dangerous
reaction such as Hellish Rebuke or Counterspell.

**If Stun fails (T3-A10)** — the answer to a failed Stun is to leave, not to stand
there. End the turn 50 ft from melee enemies; Dash 90+ ft to get outside ranged
range as well. He has Step of the Wind, Cunning Action: Dash from char 8 and the
Night Walkers' Misty Step, so the mobility is already paid for.

**`traps` Stillness of Mind (T3-A11)** — the wiki confirms there is no toggle and no
reaction prompt: it auto-casts and spends his Action. Nothing in this party grants
fear immunity, so the mitigation is standing inside Charles's Aura of Protection
when fear is expected.

**`traps` no-elixir fallback (T3-A9)** — with no Giant Strength in the pack, punch on
DEX: +4/+4 instead of +10/+10. The Stunning Strike DC is unchanged in Acts 1–2
because it takes the higher of DEX and STR. Do **not** pick up a weapon to
compensate — Tavern Brawler always adds the STR modifier, which is 8, so a held
weapon is worse than a fist (wiki).

---

## Declined

**T2-29 Luminous Gloves boss-fight bag swap — declined.** bX5paFDOGDU 32:13 wants
6–8 Radiant hits a turn stacking Radiating Orb on one boss via Manifestation of
Soul. Cost: the Gloves of Soul Catching's 1d10 Force per hit, and the Resonance
Stone doubling on Manifestation of Mind (Radiant is not doubled). The narrator
himself calls it "not a primary strategy for monks". The gloves' armour tag is also
unconfirmed, and an armour tag would break Unarmoured Defence outright — see
In-game checks.

**T3-A2 The Dead Shot swapped in after Celestial Haste — declined.** Only one copy
exists (Fytz the Firecracker, Stormshore Armoury) and **Bonbon takes it** under
T1-2. Improved Critical is holder-scoped per the wiki, so it would have lowered his
punch crit threshold from the ranged slot, which is a real effect — it just loses
to giving Bonbon +5 to hit on 8 projectiles a turn. Gontr Mael stays his Act 3
ranged slot unchanged. Cross-file: Charles's equivalent idea (T3-C3) is also
dropped, so nothing else in the party competes for the copy.

**Monk 8 / Thief 4 for a third feat — declined.** Raised by four videos and already
recorded in `traps`. The third feat's best use is +2 WIS, which loses to Ki
Resonation and the d8 Martial Arts die that Monk 9 buys instead.

**Swashbuckler Rogue tail — declined.** Flick o' the Wrist needs a main-hand finesse
weapon and CHA, both of which this build refuses, and Sand Toss spends the Flurry
bonus action.

**Light Cleric 6 / Open Hand 6 — declined.** Costs Fast Hands, Ki Resonation, Alert
and Evasion for engines the party already runs elsewhere.

**Also weighed and left alone** (report Tier 5): the Gloves of Dexterity trick
(settled as D1); Callous Glow with self-cast Light, which lights him up inside
Charles's Darkness; the Cloak of Protection, which is Charles's claim; the Helmet
of Grit (armour tag); the Amulet of Greater Health at CON 8; the Manifestation of
Soul route; Devotee's Mace, Duellist's Prerogative and Sharpshooter, all of which
need a held weapon; Athletics Expertise, because Push is a save and not a contest;
and baiting the Vest's counter, for which Gale is the easier target.

---

## In-game checks

Open questions the build now touches. Each needs one look in play.

1. **Happy duration (T3-A3).** The wiki does not state how long Happy lasts from a
   Vampire Bite. If it is turn-limited rather than until-long-rest, the pre-fight
   bite has to happen immediately before initiative rather than at camp. Check the
   condition tooltip on his portrait after biting.
2. **Luminous Gloves armour tag (T2-29).** Unconfirmed. If they are tagged Light,
   Medium or Heavy they break Unarmoured Defence and the declined swap is not just
   weak but illegal. Read the item tooltip when the gloves drop.
3. **Unarmed strikes as weapon attacks for Battle Acuity / Arcane Acuity-class
   riders.** Several party items and passives trigger on "weapon attacks". Whether
   BG3 counts an Unarmed Strike as one decides how much of that pool Asterion can
   use at all. Check the character sheet and combat log on one unarmed hit with a
   weapon-attack rider equipped.
4. **T4-U1 Hexblade's Curse per damage roll** (Charles's, but it sets whether
   cursing the nova target is a standing rule Asterion should play around). Two
   videos' combat logs show +proficiency on every damage instance rather than once
   per swing. One cursed target, one smite, read the log.
5. **T4-U4 Reaction-interrupted multi-projectile spells.** A reaction interrupting
   the first projectile of Magic Missile or Scorching Ray reportedly drops the
   rest. If true, Asterion stepping out of melee is one way to bait the reaction
   before Gale casts.
