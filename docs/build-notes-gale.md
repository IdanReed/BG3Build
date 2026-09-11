# Build notes — Gale (The Powder Keg)

Why Gale's build is what it is. `content/characters/gale.md` is the cheat sheet:
what to take, where to get it, one gotcha each. Everything cut from it for length
is here, plus the rationale the 2026-09-11 Cephalopocalypse review
(`docs/cephalopocalypse-build-review-2026-09-11.md`) recorded for each decision.
Anchors are the field name or the entry `id` used in the content file.

Final split: Sorcerer 11 (Draconic Bloodline — Red) / Fiend Warlock 1.

---

## Creation and stats

**`race_notes`** — Human in BG3 gives a freely-assigned +2/+1 like every race, so
the race is stat-neutral and costs nothing. Civil Militia already grants LIGHT
ARMOUR, so the Warlock dip is *not* needed to wear Armour of Landfall; the dip is
justified by Command alone. The published guide recommends Halfling for Luck (no
natural 1s on the many Scorching Ray attack rolls and Heat CON saves); Gale is a
fixed origin Human, so that safety net is unavailable and CON-save advantage from
Spidersilk Armour, later Armour of Landfall, is the replacement. Netherese orb:
an EARLY-Act-1 issue only, the 3-item "The Wizard of Waterdeep" quest. Feed him
three magic items and the hunger resolves; Elminster later quells it entirely.
Ignoring it stacks escalating Arcane Hunger debuffs (disadvantage on saves →
attacks → half move) and only the final ignored stage is fatal. It is not an
Act 1–2 resource drain.

**`stats_note`** — point-buy base 8/15/14/8/10/15 spends all 27 points (DEX 15 and
CHA 15 cost 9 each, CON 14 costs 7, WIS 10 costs 2). Human +2 → CHA 17 and +1 →
DEX 16. DEX 16 is load-bearing because Draconic Resilience is unarmoured AC
13 + DEX and both Spidersilk Armour and Armour of Landfall are 13 + DEX light
armour, so DEX is his entire AC. WIS 10 because nothing keys off it.

Rejected: CON 16 / DEX 14 (Tier 5) — +1 concentration save against −1 AC and
−1 initiative, and the chest already grants CON-save advantage.

**`ability_targets` / `ability_scores` (T4-V6)** — the Mirror of Loss +2 is not
guaranteed. One DC 25 Religion check per character; a failure locks that character
out forever. Religion is INT-based and only Charles is proficient, at INT 8. After
the check there is still a 60% roll per attempt. All four builds' end stats assume
the +2. Plan: Bonbon casts Enhance Ability, someone casts Guidance, and quicksave
before every prayer. The videos' claim that the Mirror "cannot be used on both" is
wrong — the wiki says it is per character. (s50sTy53DZw 3:08;
bg3.wiki/wiki/Mirror_of_Loss)

CHA 20 is the target and no ASI is needed to reach it, which is what frees both
feats for Dual Wielder and Elemental Adept. Birthright (+2 CHA → 22) is worn by
nobody: Gale's head belongs permanently to the Hat of Fire Acuity and Bonbon's to
the Helmet of Arcane Acuity, and +2 Charisma is +1 spell save DC against Acuity's
+10.

**`feats` Dual Wielder** — unusual on a caster, but the build wields two staves as
stat sticks and neither pair is Light (Spellsparkler + Melf's in Acts 1–2,
Markoheshkir + Rhapsody in Act 3), so the feat is mandatory to hold both. Cost:
both hands are full for the whole run, so Gale can never carry a shield.

**`feats` Elemental Adept: Fire (T3-G6, T2-20 declined)** — the tier lists rate the
feat only B in general while Alert is one of two S+ picks, so this is knowingly a
B-tier spend. The old rationale in the file was wrong and is corrected: Bonbon
does *not* strip fire resistance "one target at a time" — a ranged Flourish hits
two targets per attack and an Arsonist's Oil coating lasts ten turns. The feat's
case is instead that it needs no set-up turn at all and removes 1s from every fire
die, worth roughly +1.2 per ray on every cast. In BG3 the wiki text is "cannot
roll a 1" on fire damage dice, not the tabletop treat-1s-as-2s. The
resistance-piercing covers "spells you cast AND attacks you make"; only the no-1
clause is spell-only. Act 3 is dense with fire-resistant enemies.

**`feats_note`** — Sorcerer grants feats at Sorc 4 and Sorc 8, which are character
levels 4 and 9. The Warlock level grants none and Sorc 12 is never reached.
Initiative and concentration are therefore gear and consumable problems on this
build, not feat problems.

**`creation.starting_spells` (T3-G7)** — the old plan replaced Magic Missile with
Counterspell at Sorc 6. Two reviewers call Magic Missile a party requirement (no
attack roll, no save) and nobody else in the party has one. With the T2-17 spell
path Counterspell arrives at Sorc 5 off the Cloud of Daggers slot, so the Sorc 6
replacement slot is free and Magic Missile survives without a further swap. Both
Shield and Magic Missile are rated S.

**`creation.proficiencies.skills`** — three picks, not two: Sorcerer grants 2 and
Human Versatility grants 1 more of any kind. Sage already supplies Arcana and
History and proficiency does not stack, so do not re-pick Arcana. Persuasion is
the only Sorcerer-list skill that rides the CHA 20 the build targets and makes
Gale the fallback face when Bonbon is benched. Perception is the one skill worth
duplicating across the party because BG3 rolls passive Perception per member.

---

## Leveling

**T2-17 · Cloud of Daggers for characters 3–4 via the unused replacement slots**
— raised by iVOxw7TWYa0 (14:34, 17:10) with the numbers from IC1WiOi_nYQ (25:01):
4d4 on cast and 4d4 again at the start of the enemy turn, with no attack roll and
no save. The old plan left the Sorc 3 and Sorc 5 replacement slots unused
entirely. Path taken: Sorc 3 pick Scorching Ray and replace Chromatic Orb →
Cloud of Daggers; Sorc 5 pick Haste and replace Cloud of Daggers → Counterspell,
one level earlier than before. Scorching Ray still lands at Sorc 3, which is what
starts the Spellsparkler charges. Cost: no Chromatic Orb from character 3 onward.
The PARTY-1 variant that delays Scorching Ray to Sorc 6 was not recommended and is
not taken.

Chromatic Orb is rated S — "exceptionally highly" — for damage plus a chosen
surface with no concentration, and its other elemental modes cover fire-immune
enemies. Losing it at char 3 is the real cost of this path; Cloud of Daggers'
no-roll damage for two levels is judged the better trade.

**T2-19 · Ice Storm instead of Dimension Door at Sorcerer 8 (char 9)** —
iVOxw7TWYa0 22:20. Ice Storm was already sitting in `spells.recommended` as the
A-tier non-concentration AoE and was never scheduled; Dimension Door is C tier in
the channel's own list, and Misty Step scrolls plus Draconic Fly at char 12 cover
traversal. Ice Storm is A specifically because the 20 ft ice surface costs no
concentration, so it drops while Gale holds Twinned Haste. The darkness-party
video offered Banishment for the same slot as a Charisma-save answer to the
un-Holdable boss, but Banishment is Concentration and would drop Twinned Haste, so
it stays a scroll.

**T3-G5 · Ice Storm melt caveat** — Gale's own fire melts the ice. Fire first, Ice
Storm last in the turn; Ray of Frost re-freezes the surface afterwards.

**T2-18 · Cone of Cold instead of Telekinesis at Sorcerer 10 (char 11)** —
iVOxw7TWYa0 23:52. The file itself said Gale "contributes almost nothing to the
fire-immune fights until Chain Lightning at char 12" and called Telekinesis
bugged, Concentration and niche (the wiki records a first-cast save cancelling
concentration). Cone of Cold is a non-concentration 8d8 cone that works while he
holds Haste, and the Mage Hand water-bottle trick already supplies Wet, which
doubles cold damage.

**Spells-known ledger** — Sorcerer is a known caster: 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12 spells known at Sorc 1–11, with one replacement available per level from
Sorc 2. Burning Hands is granted by Red ancestry and costs no pick. Warlock 1 adds
Command and Hex as separately-known Warlock spells.

| Char | Class | Pick | Replacement | Sorcerer known |
|---|---|---|---|---|
| 1 | Sorcerer 1 | Shield, Magic Missile | — | 2 |
| 2 | Sorcerer 2 | Chromatic Orb: Fire | unused | 3 |
| 3 | Sorcerer 3 | Scorching Ray | Chromatic Orb → Cloud of Daggers | 4 |
| 4 | Sorcerer 4 | Hold Person | unused | 5 |
| 5 | Sorcerer 5 | Haste | Cloud of Daggers → Counterspell | 6 |
| 6 | Sorcerer 6 | Fireball | unused (Magic Missile kept) | 7 |
| 7 | Fiend Warlock 1 | Command, Hex (Warlock) | — | 7 |
| 8 | Sorcerer 7 | Daylight: Enchant Item | unused | 8 |
| 9 | Sorcerer 8 | Ice Storm | unused | 9 |
| 10 | Sorcerer 9 | Hold Monster | unused | 10 |
| 11 | Sorcerer 10 | Cone of Cold | unused | 11 |
| 12 | Sorcerer 11 | Chain Lightning | unused | 12 |

Final twelve: Shield, Magic Missile, Scorching Ray, Hold Person, Haste,
Counterspell, Fireball, Daylight: Enchant Item, Ice Storm, Hold Monster, Cone of
Cold, Chain Lightning. Plus free Burning Hands, plus Warlock Command and Hex.
Dropped along the way: Chromatic Orb: Fire (char 3), Cloud of Daggers (char 5).
Never taken: Dimension Door, Telekinesis, Enhance Ability, Misty Step, Globe of
Invulnerability (scrolls).

**`leveling` char 1 Skills** — the Human free skill is a character-creation choice.
Check at the Withers respec screen whether Perception is still re-selectable on
the origin Gale or already locked.

**`leveling` char 7 Cantrips** — Eldritch Blast is unimpressive here because
Agonizing Blast is a Warlock 2 invocation Gale never reaches; take it as an
occasional ranged option, not a plan. Do NOT take Friends as the second cantrip:
Gale already knows it from Sorcerer 1 and the game will not let you re-pick a
known cantrip. Bone Chill is the right second pick (A tier — "targets AC at range,
prevents healing, and gives undead disadvantage on attacks") because char 7 lands
in Act 2, where Command does not work on the Undead. Toll the Dead is the
equivalent WIS-save alternative.

**`leveling` char 11 Ray of Frost** — the sixth cantrip is easy to miss because
char 11 is the only level after char 4 that grants one. S tier: "the best broadly
available elemental attack — Wet doubles its cold damage, the hit reduces movement
without a save, and water can freeze into ice that knocks enemies prone." 3d8 at
this level. Bone Chill is already taken at char 7, so Ray of Frost is the
non-overlapping pick, and it patches the fire-immune hole for free.

---

## Spells

**`spells` Scorching Ray** — rated only A, precisely because its value is
"multi-hit riders, not efficiency," which is exactly how this build uses it. 3 rays
at level 2, +1 ray per slot level above 2nd, so a level-6 slot fires 7. Each ray is
a separate attack roll AND a separate damage instance, so every flat rider applies
to every ray. Confirmed per-ray by name on the wiki: Elemental Affinity: Damage and
the Callous Glow Ring. Inferred but not individually stated: Rhapsody's and
Markoheshkir's +proficiency, covered only by the general rule that bonus damage
from passives and conditions applies per instance. Spellmight's +1d8 is not
addressed anywhere (see In-game checks). At the ceiling that is +5 CHA, +2 Callous
Glow, +3 Rhapsody, +4 Markoheshkir, +1d8 Spellmight and Phalar Aluve's Shriek 1d4
Thunder, all multiplied by the ray count. It is also the Hat of Fire Acuity engine:
each ray deals Fire damage and grants 2 turns of Arcane Acuity, so one level-4
(5-ray) cast takes Gale from 0 to the 10 cap.

**`spells` Counterspell (T4-V3)** — live wiki bug: Counterspell against a spell of
higher level than the slot used rolls INT, and both party carriers have INT 8.
Charles's L3 pact-slot Counterspell is a 20–30% roll against 4th-level and higher
spells. Gale removes the check by upcasting from a higher Sorcerer slot. This
raises the value of Psionic Dominance. Counterspell has no scrolls, so it must be
learnt on level-up. (5yTLH3BWrW0 26:32)

**`spells` Hold Person (T4-V5)** — Paralysed auto-crits apply to ANY attack within
3 m, not only melee. The old text said "from melee". Gale standing within 3 m of a
Held target fires 5–7 crits with advantage, roughly +55 to +80 per cast.
(iVOxw7TWYa0 21:18)

**`spells` Command (T4-V4)** — the old `traps` entry asked whether Command can be
cast from ordinary Sorcerer slots or only from the single short-rest pact slot,
and named Bonbon as the fallback controller if not. The wiki Resources page
settles it: any slot of the right level casts any known spell regardless of which
class granted it. The trap and its fallback clause are deleted. Extended Spell
doubles the condition to two turns. Command: Approach also groups enemies for
Fireball. No effect on Undead.

**`spells` Chain Lightning / Markoheshkir (T3-G3)** — Markoheshkir's Kereska's
Favour grants free spells per short rest that the file never recorded: Flame of
Wrath grants Fireball and Wall of Fire once each, Bolts of Doom grants Chain
Lightning and Lightning Bolt. The old fire-immune playstyle line read as if Chain
Lightning cost the level-6 slot; it does not, so the single L6 slot stays free for
a 7-ray Scorching Ray. This is also why learning Wall of Fire at Sorc 7 was
rejected — Flame of Wrath gives it free.

**`spells` Mage Hand (T4-V1)** — Wet grants Resistant to Fire and Vulnerable to
Lightning and Cold, so applying Wet before a fire cast HALVES Gale's damage. The
water-bottle trick is scoped to Ray of Frost, Cone of Cold and Chain Lightning
only. Healing Vapours stopped applying Wet in Patch 8.
(bg3.wiki/wiki/Wet_(Condition), Healing_Vapours)

**`spells` Globe of Invulnerability** — S tier and total damage immunity, but
Chain Lightning takes the single level-6 spell known, so buy scrolls for the two or
three fights that want it. Learning Globe instead was rejected: it is
Concentration, so it would drop Twinned Haste.

**`spells` Hex** — a per-ray damage rider in theory, but it uses Concentration and
therefore competes with Haste, which makes it a modded-difficulty option only.
Armour of Agathys is the defensive alternative for the same Warlock pick.

---

## Itemization — Act 1

**`the-spellsparkler`** — rated A on the staves tier list, which names Scorching Ray
specifically: each of the 3–5 separate damage instances grants 2 Lightning Charges,
and charges give +1 to attack rolls and +1 Lightning damage, bursting for 1d8 at
five stacks. It carries no enchantment bonus, so it is a rider stick, not an
accuracy stick — that is Melf's job. It is also "Consumable by Gale": wield it, do
not feed it to the Netherese orb.

**`melf-s-first-staff`** — S tier, "the defining early caster bonus… often best
through Acts 1 and 2." The +1 spell attack applies to every single ray and the
+1 DC carries his Command and Hold Person.

**`act1-feet-gale`** — open, and honestly so. The Boots of Stormy Clamour used to
sit here and now go to Charles, because Gale's Reverberation payload does not exist
yet in Act 1: Gloves of Belligerent Skies need Thunder, Lightning or Radiant damage
and he casts fire, while Coruscation, Callous Glow and Spineshudder are all Act 2
pickups. His only Act 1 condition to convert was Command.

**`opt-night-walkers-gale`** — this is now decided, for Act 3 rather than Act 1
(see T3-G2 below). The relevant half of the item is immunity to being knocked
Prone, because Prone ends Concentration outright and Gale carries Twinned Haste
permanently, while Asterion's Bless is the one Concentration in the party nobody
minds losing. Asterion also already has bonus-action Dash and Disengage from Step
of the Wind, so Misty Step is the smaller half of the item for him. Taking it in
Act 1 would re-cut his kit; taking it in Act 3 costs nothing.

**`spidersilk-armour`** — the answer to the build's worst structural problem. Worn
by Minthara in the Shattered Sanctum, the same kill that yields Charles's Boots of
Striding, so it costs nothing extra to acquire. AC 12 + DEX and +1 Stealth, but the
reason to wear it is advantage on Constitution saving throws: Gale has no War
Caster, no feat left to buy one, and no shield once Dual Wielder fills both hands.
It costs exactly 1 AC versus going unarmoured, since Draconic Resilience is
13 + DEX. Take the trade, because Haste is the concentration the entire party plan
is built on.

**`elixir-of-vigilance`** — rated S+ above the scale: a free Alert feat. BG3 rolls
initiative on a d4 + DEX, not a d20, so +5 is larger than the entire die. Gale is
the only party member with no competing elixir — Asterion needs Giant Strength,
Bonbon needs Hill Giant then Vigilance of her own, Charles wants Bloodlust or
Heroism — so the one-elixir-per-rest slot is free for him.

**`ring-of-protection`** — ranked #20 of 20 in the Act 1 list with the note that it
should "shore up the party's lowest AC." That is Gale: Spidersilk puts him at AC 15
against Asterion's 21 unarmoured. The +1 to all saving throws is concentration
insurance as well. Asterion takes the Bracing Band instead and loses nothing.

**`gloves-of-belligerent-skies`** — Charles has a real claim (Divine Smite is
Radiant, and the wiki notes Phalar Aluve's Shriek Thunder triggers them correctly
in Honour Mode specifically). They stay with Gale because he applies the rider 5–7
times per cast against Charles's two swings.

---

## Itemization — Act 2

**`hat-of-fire-acuity`** — the item that turns the build on. Dealing Fire damage
grants 2 turns of Arcane Acuity, capped at 10, and each remaining turn is +1 spell
attack AND +1 spell save DC. Because each ray deals Fire damage separately, one
level-4 cast (5 rays) takes him from 0 to the cap. If the Strange Ox is missed in
Act 2 it reappears in Rivington, on a hill west of the requisitioned barn, in
Act 3.

**`coruscation-ring` + `callous-glow-ring`** — the chain, in order: light on GALE →
ray 1 applies Radiating Orb (the wiki is explicit that Coruscation keys off the
WEARER being illuminated, not the target) → the target is now Illuminated → rays
2+ each add Callous Glow's +2 radiant, up to +14 on a level-6 cast → which re-procs
Gloves of Belligerent Skies. Radiating Orb is also −1 to the target's attack rolls
per remaining turn, so it is a party-wide accuracy debuff. Charles can stand in his
Darkness cloud throughout; none of this touches him. Callous Glow stays with Gale
rather than Asterion or Bonbon because his ray count is the highest in the party
and his own Coruscation Ring is what illuminates the target in the first place.
Take Callous Glow off against Shar worshippers and Justiciars.

**`spineshudder-amulet`** — applies Reverberation on ranged SPELL-ATTACK hits only,
which is exactly what Gale makes, 3–7 times a cast. Paired with Belligerent Skies
firing on the Callous Glow radiant of every ray, that is roughly 28 turns of
Reverberation from one Scorching Ray against a threshold of 5, so single targets go
Prone repeatedly: five stacks force a Constitution save that the condition's own
penalty makes effectively DC 15. This pair is the whole engine, which is why the
Boots of Stormy Clamour could leave for Charles without costing him anything — the
boots were adding nothing he was not already three times over.

**`cloak-of-protection-gale`** — not his, though he is the obvious candidate. It is
the only Act 2 cloak that touches saving throws and exactly one exists. Charles
gets it because he carries permanent DISADVANTAGE on every save from the Risky Ring
while holding concentration in melee. Gale already has CON-save advantage from
Spidersilk plus save proficiency from level 1, and can be positioned out of danger.

**`thunderskin-cloak`** — the synergy is real rather than incidental: Gale is the
party's largest source of Reverberation (Spineshudder and Belligerent Skies each
fire per ray), so essentially anything that reaches him is already Reverberating,
and the Dazed WIS-save penalty then feeds his own Command. Rated D on the grounds
that the DC 13 save will practically never trigger for a normal build.

**`act2-feet-gale` / `opt-acrobat-shoes-gale`** — Acrobat Shoes are arguably the
better pick and are rated D only because DEX-save advantage "is available
elsewhere". It is not available elsewhere on this character: Spidersilk and Armour
of Landfall both give Constitution-save advantage and nothing in the kit touches
Dexterity, and Fireballs and breath weapons are what actually take Twinned Haste
off him. The slot is forced either way — Boots of Persistence, Vital Conduit Boots
and The Speedy Lightfeet all require Medium Armour proficiency, which Sorcerer 11 /
Warlock 1 never grants, and Helldusk goes to Charles.

**`drakethroat-glaive` (Drakethroat element = Cold)** — Human Civil Militia gives
Gale the glaive proficiency, and Twinned Spell (3 sorcery points) doubles the cast,
so out of combat he equips the glaive, Twins Draconic Elemental Weapon onto
Bonbon's bow and Charles's main hand, and swaps the staves back. Each target gets
+1 Attack Rolls and +1d4 of one chosen element until long rest, stacking with Magic
Weapon. The element is now COLD every day: Bonbon's Snowburst Ring plan (T2-8)
needs cold on her bow, and Charles's blade takes cold too unless the fight ahead
resists it. Gale's Elemental Adept: Fire does nothing for an ally's weapon, so
there was never a reason to pick fire. The glaive only takes a weapon on the ground
or an ally's MAIN-HAND weapon, both within 1.5 m, so the bow is dropped at his feet
and re-equipped afterwards while Charles is targeted directly. From the Resonance
Stone on, Charles's main hand is the 3d8 Shadow Blade, so he summons it first.

---

## Itemization — Act 3

**`markoheshkir`** — rated S and called the universal caster best-in-slot. Flame of
Wrath gives fire resistance, +proficiency bonus to Fire spell damage applied per
ray, and Heat generation. Attuning also starts unavoidable Heat self-damage each
turn, which threatens Twinned Haste, so do not attune until Armour of Landfall is
equipped. Staff of Spellpower is the per-fight swap when a second Arcane Battery
matters more than Rhapsody's +3.

**`rhapsody`** — Scarlet Remittance stacks +1 attack, damage AND spell save DC per
kill, up to 3, and the build uses all three with the damage applying per ray. As of
Patch 5 stacks build only on killing living hostile targets and are lost when the
dagger is unequipped, so once he is at +3 it stays in his hand. Staff of Spellpower
covers the off hand until then, and on any day that opens against undead or
constructs where no stack can be built.

**`spellmight-gloves` (T4-U2)** — the whole case for promoting them to core is that
the −5 spell attack / +1d8 damage applies to EACH ray. On a 7-ray cast the two
readings are +7d8 (~31, best in slot) versus +1d8 (~4.5 for a −5 penalty on all
seven rolls, actively harmful). The wiki never addresses it and Spellmight is
absent from the per-instance notes that DO name Elemental Affinity and the Callous
Glow Ring. iVOxw7TWYa0 30:37 asserts +1d8 on every ray from a build that has played
it, which moves the flag from "untested" to "probably, confirm on the first cast".

**`armour-of-landfall`** — AC 13 + DEX, +1 Spell Save DC and advantage on
Constitution saving throws, which is what replaces the Halfling Luck and War Caster
this build cannot have and what makes Markoheshkir's Heat safe to carry while
concentrating. Robe of the Weave is the pure-damage alternative (+2 AC and +1 spell
attack/DC) but has no CON-save advantage, so it loses for a Haste-concentration
build. Landfall also grants Plant Growth once per short rest (see Playstyle,
T2-24).

**`hellriders-longbow`** — the contest with Bonbon is settled by the item itself.
Her ranged slot belongs to a bow for the whole game and a bow cannot share it, so
she has no free ranged slot and Gale has one he never otherwise uses. He holds it
purely as a stat stick; on top of the standing Elixir of Vigilance that is +8
initiative without a feat. The Dead Shot over Hellrider was considered and rejected
for Gale: initiative decides this slot, and Bonbon has the claim on The Dead Shot
(T1-2).

**`act3-feet-gale` (T3-G2 · Disintegrating Night Walkers as the default)** — free
once Asterion moves to the Boots of Uninhibited Kushigo. Prone immunity on the
party's most important concentration plus a short-rest Misty Step, against Evasive
Shoes' +1 AC. Evasive Shoes become the per-fight option for fights with no Prone
threat. Night Walkers do not cover Paralysed or Restrained; the Ring of Free Action
is the answer to those. This is the same slot T2-16 (Boots of Arcane Bolstering)
wanted, and Night Walkers win it — see Declined.

**`helldusk-boots-gale`** — less close than it used to read. Infernal Evasion, a
Reaction to turn a failed save into a success, is ONCE PER LONG REST per the wiki,
not once per turn, so it is an emergency button rather than standing concentration
insurance. What decides the slot is the Prone immunity, and Charles is the
frontliner who gets knocked down. Gale has no Prone cover; the Night Walkers give
ice-footing and a short-rest Misty Step instead.

**`act3-amulet-gale`** — Amulet of Greater Health goes to Charles: its CON-save
advantage is redundant on Gale, who already has that from Armour of Landfall,
whereas Charles has the Risky Ring's disadvantage for it to cancel. On the Amulet
of the Devout (T4-V8): the old note here said its Channel Divinity charge is dead
on a Paladin, which is beside the point — the wiki's +2 spell save DC applies to
anyone. It is skipped for other reasons, recorded in `docs/build-notes-party.md`.

**`birthright`** — +2 Charisma to a maximum of 22, but the head slot belongs
permanently to the Hat of Fire Acuity and without Acuity the build stops working.
It does not go to Bonbon either, for the same reason. Bagged as an out-of-combat
Charisma swap for dialogue checks.

---

## Progression

**`prog-feet`** — empty through Act 1 because the Reverberation payload does not
come online until Act 2 and the Boots of Stormy Clamour therefore go to Charles →
Evasive Shoes (Mattis, Last Light) from Act 2 → Disintegrating Night Walkers in
Act 3. A modest slot forced by a hard rule: every strong boot in the pool requires
Medium Armour proficiency that Sorcerer/Warlock never grants.

**`prog-hands`** — Spellmight's −5 to hit needs Arcane Acuity to cover it, which is
why the first Scorching Ray of a fight is cast with the gloves off.

**`prog-consumables`** — Elixir of Vigilance every long rest, all game, and the
substitute for the Alert feat this build cannot afford.

---

## Playstyle

**T3-G1 · Pre-cast Twinned Haste before initiative** — Hastened lasts 10 turns, so
casting just before engaging frees Gale's turn 1 Action for a second Scorching Ray.
Ambushes keep the old line, where Haste is the turn 1 Action.

**T3-G4 · Heat Convergence into Fireball, never Scorching Ray** — the wiki is
explicit that multi-hit spells consume the stored Heat on the first hit only, while
area spells add it to every target. Use the free Flame of Wrath Fireball as the
discharge.

**T2-24 · Plant Growth under Hunger of Hadar, and no fire in the zone** —
4KkXqqeKz80 28:02. Armour of Landfall grants Plant Growth once per short rest;
under Charles's Hunger of Hadar (blinded so they cannot jump, quarter speed) it is
a multi-turn no-save lock with Repelling Blast pushing escapers back. Standing
rule: no Fireball, Scorching Ray or Heat into the zone, because fire burns Plant
Growth away (bg3.wiki/wiki/Plant_Growth). Gale's fire goes at targets outside the
zone; Charles and Bonbon work the inside.

**T2-21 · Arsonist's Oil fire-vulnerability setup** — iVOxw7TWYa0 40:25. Make the
target fire-resistant with a thrown Elixir of Fire Resistance, hit it with an
Arsonist's-Oil weapon, then overwrite the resistance with another thrown elixir:
the target ends Vulnerable to fire, which doubles every ray, roughly 175 → 350 on a
7-ray cast. Wiki-confirmed (bg3.wiki/wiki/Arsonist's_Oil). Costs two elixirs and a
Bonbon bonus action per target, and it is an exploit — acceptable because this is a
non-Honour run.

**T4-V5 · Stand within 3 m of a Held target** — see the Hold Person note above.
The caveat to watch in play is whether a ranged spell attack made inside an enemy's
reach takes Threatened disadvantage; advantage from Paralysed would cancel it if
so.

**Fire-immune fights** — Gale's damage drops sharply against House of Hope,
Raphael, the red dragon and Yurgir. The plan is Markoheshkir on Bolts of Doom for
free Chain Lightning and Lightning Bolt each short rest, Cone of Cold and Ice Storm
from the spell list, Ray of Frost for slot-free chip, and Twinned Haste, Command
and Counterspell for everything else.

**`traps` Heat** — three interactions compound Markoheshkir's Heat self-damage:
Elemental Adept: Fire does NOT protect Gale (it pierces enemy resistance, it does
not reduce damage he takes); the Callous Glow Ring adds +2 radiant to Gale's own
Heat tick whenever he is Illuminated, and the Coruscation chain keeps him
Illuminated on purpose; and any damage taken strips 2 turns of Arcane Acuity, so
every tick chips the exact stat the build exists to stack, on top of forcing a CON
save against Twinned Haste. Gale is Human, so there is no Halfling Luck. Consider
dropping Coruscation in fights where Acuity uptime matters more than the radiant
riders.

---

## Declined

**T1-4 · Drop the Fiend level, go Sorcerer 12 — no.** IC1WiOi_nYQ 19:40–37:00 and
bGupbGD2Fw0 21:42 both run pure Sorcerer 12: a third feat (Alert / War Caster /
+2 CHA) and a twelfth spell known, with Globe of Invulnerability and Chain
Lightning both fitting. Declined because Command leaves Gale entirely. Bonbon only
gets Command at Bard 10 and Charles's copy costs his Paladin slots, so the party's
mass no-concentration disable would disappear for Acts 1–2 and shrink after. A
third feat is the only thing the dip costs, and the Vigilance elixir already
substitutes for Alert. `party.md` names Command as Gale's non-concentration control
lane and Extended Spell was picked for it.

**T1-5 · Hexblade instead of Fiend for the dip — no.** iVOxw7TWYa0 9:52–12:32.
Hexblade's Curse is +4 per ray (+28 on a 7-ray cast, +56 across a Hasted double)
and crits on 19. Declined for two reasons: Hexblade's expanded list is Shield and
Wrathful Smite, not Command, so the control lane goes (the same objection as T1-4),
and the curse's bonus action collides with Quickened Scorching Ray every turn. The
damage is real; the party role is the cost. Lists verified at bg3.wiki/wiki/Warlock.

*"Any way to get Command and go Hexblade?"* — not on Gale. Command is not on the
Hexblade expanded list at Warlock 1, and Gale has no other route to it: Sorcerer
does not have it, and a second dip is unaffordable. The party's other copies are
Charles's Paladin list in Acts 1–2 (Command is an oath/Paladin-list spell he can
prepare) and Bonbon's Magical Secrets at Bard 10. Both are worse than Gale's: Charles's
copy spends the Paladin slots the nova smites run on, and Bonbon's does not exist
until char 10 or 11. So the dip stays Fiend.

**T1-6 · Sorcerer 9 / Fiend 3 — no.** bCW4Hrr7Hmw 29:11 calls Sorcerer 9 "another
reasonable breakpoint". Fiend 3 gives two short-rest L2 pact slots with Scorching
Ray on the Fiend list (two extra 3-ray casts per short rest) and Pact of the Tome
Guidance, the party's missing second Guidance. Declined because it costs Careful
Spell (Fireball into the melee cluster), the L6 slot (a 7-ray Scorching Ray or
Chain Lightning), one L5 slot, two Sorcerer spells known and 2 sorcery points. The
video's own argument, that L6 spells are weak, does not apply because our L6 use is
an upcast. Whether pact slots feed Create Sorcery Points is unverified.

**T1-7 · Take the Warlock level at character 2 — no, unless Act 1 control is what
you want.** iVOxw7TWYa0 9:22. Command from early Act 1, with Extended Command at
char 3, five levels earlier. Cost: Scorching Ray, Dual Wielder, Twinned Haste and
Elemental Affinity each slip one level (Haste char 5 → 6), landing on the Grymforge
and Crèche fights, and `party.md`'s "Twinned Haste online at char 5" would change.
Identical from char 8 onward.

**T2-16 · Boots of Arcane Bolstering in Acts 2–3 — no.** iVOxw7TWYa0 35:16. Dash
grants Arcane Charge for 2 turns: +2 spell damage per independent damage instance
against any Threatened enemy, and the wiki says the ENEMY must be Threatened, not
the wearer, so any target Charles or Asterion stands next to qualifies. That is +10
on a 5-ray cast and +14 on 7, for the two turns after a pre-combat Dash, which are
the turns that decide most fights. Araj Oblodra at Moonrise, 190 gp, no proficiency
tag. Declined because it is the same slot as T3-G2; the Night Walkers (no slipping on
Snowburst or Ice Storm ice, short-rest Misty Step) win, with Evasive Shoes' +1 AC as
the fallback option. Correction: the wiki lists no Prone immunity on the Night Walkers.

**T2-20 · Alert instead of Elemental Adept: Fire at Sorcerer 8 — no.**
IC1WiOi_nYQ 30:13. Alert on Gale duplicates the Vigilance elixir's +5 initiative,
so the whole gain is retiring a 25 gp daily consumable. Elemental Adept's no-1s on
fire dice is about +1.2 per ray on every cast. Modest either way; kept as is. The
video's Arsonist's Oil argument did weaken the old rationale and that sentence was
corrected (T3-G6).

**T2-22 · Pyroquickness Hat as a boss-turn head swap — no.** IC1WiOi_nYQ 37:30. An
Action Scorching Ray grants an extra bonus action, so 7+5+5 rays instead of 7+5,
roughly +100 for 6 sorcery points on a turn that does not need Acuity for Command.
Wet (a thrown water bottle) or Helldusk Armour negates the self-Burning that would
otherwise force a Haste save each turn. Sorcerous Vault, 160 gp, a bag item rather
than a slot change. Verified at bg3.wiki Pyroquickness_Hat. Declined: it competes
with the Hat of Fire Acuity, which is the build, and the Wet workaround halves his
fire damage.

**T2-23 · Bait enemy reactions before Scorching Ray — no.** zIiqb32iN9w 22:43
shows a combat log where a reaction (Hellish Rebuke, opportunity attack)
interrupting the first projectile of Magic Missile or Scorching Ray drops the
remaining projectiles. Unverified in the KB. Charles would be the natural baiter,
stepping out of melee to draw the opportunity attack before Gale casts. Declined as
a written rule; it stays an in-game check (T4-U4).

**Banishment at Sorcerer 8** (the darkness-party video's pick for the same slot) —
a Charisma-save answer for the un-Holdable boss, but Concentration, so it drops
Twinned Haste. Ice Storm takes the pick and Banishment stays a scroll.

**Already adjudicated and unchanged (Tier 5):** Alert + shield instead of Dual
Wielder (Rhapsody out-values Ketheric's Shield); Heightened over Careful; Wall of
Fire at Sorc 7 (Flame of Wrath gives it free); Risky Ring; Amulet of Greater Health
(Landfall already gives CON advantage and Charles needs it); Robe of the Weave;
self-Haste; a Spellcrux swap; The Dead Shot over Hellrider (initiative decides);
Gold ancestry; a Wizard 1 dip (INT 8 prepares one Wizard spell and it costs Command
or Sorcerer 11); Sorcerer 10 / Fiend 2 for Devil's Sight (costs the L6 slot and the
payoff of shooting out of a cloud is denied by the wiki); Storm Sorcerer 4 /
Warlock 8 Sorlock (a different character); concentrating on Wall of Fire instead of
Haste (Charles's and Bonbon's turns both run on the Haste action).

---

## In-game checks

- **Spellmight Gloves per ray (T4-U2).** Cast one Scorching Ray with the gloves on
  and read the damage breakdown. Per ray is best in slot; once per spell is a −5
  penalty on every roll for ~4.5 damage. Decides whether Spellmight stays the Act 3
  hands.
- **Pact slot → sorcery point (T3-G8).** At a short rest on a day Command is not
  needed, try converting the level-1 pact slot with Create Sorcery Points. If it
  works that is +1 sorcery point per short rest for free. Try it once and record
  the answer.
- **Threatened on ranged spell attacks within 3 m (T4-V5 caveat).** Standing inside
  3 m of a Held target is the plan for auto-crit rays. Check whether a ranged spell
  attack made inside an enemy's reach takes Threatened disadvantage; if it does,
  the Paralysed advantage should cancel it, so confirm the net roll.
- **Light-lit characters and Coruscation.** Confirm a character lit by the Light
  cantrip registers as Illuminated for the Coruscation Ring. If not, use a torch or
  wait for Daylight at char 8.
- **Rhapsody stacks across a long rest.** The wiki says stacks are lost on
  unequipping; verify whether they also reset on a long rest.
- **Hexblade's Curse per damage roll (T4-U1)** and **reaction-interrupted
  multi-projectile spells (T4-U4)** are Charles's and the party's checks, recorded
  in `docs/build-notes-party.md`, but both change Gale's turn if they land: U4 in
  particular would make reaction-baiting worth writing down after all.
