# Charles — build notes

Why Charles is what he is. `content/characters/charles.md` is the cheat sheet: what to
take, where to get it, one gotcha. Everything that explains a choice lives here, keyed by
the entry `id` or field name in the content file, in the same section order.

Sources: the 2026-09-11 Cephalopocalypse review (`docs/cephalopocalypse-build-review-2026-09-11.md`,
"the report"), bg3.wiki through `bg3kb`, and the reasoning that was in the content file
before the 2026-09-11 cheat-sheet pass.

---

## Decisions applied on 2026-09-11, with the report's rationale

**T1-3 — character 12 is Warlock 6, not Paladin 7.** Two reviewers (0CbK5ufVk-g 37:45 and
50:13; 9qa8wa1WEVg 31:32; MuodaDzKp98 27:04 also ends on Warlock 6). The cost is one L2
Paladin slot: half-caster effective spell level drops 4 → 3, so slots go 4×L1 + 3×L2 to
4×L1 + 2×L2. That is one 3d8 smite, worth roughly +40 on a crit swing, plus Relentless
Avenger and one seat-filler prepared spell. The gain is a seventh Warlock spell known and
Accursed Spectre: when Charles or an ally within 18 m kills a creature under Hexblade's
Curse, a reaction raises a 10-turn spectre (Mundane: 31 HP, AC 14, Devour Soul heals
Charles, Pluck Soul pulls 5 m). The nova's Held target is the natural curse target and
dies to the nova, so most fights get a free body. Not raised from constructs, elementals,
oozes, plants or undead. Only the last level changes — no respec, and Aura of Protection
still arrives at Paladin 6 = char 11. Verified: bg3.wiki Accursed Spectre (passive
feature); slot count from bg3.wiki Spells (half-caster ESL rounds up, Warlock levels
ignored).

Relentless Avenger, the thing given up, was already called weak in the file: hit with an
Opportunity Attack, gain 4.5 m movement next turn. The old char-12 row also recorded the
oath cost it was priced against — Oathbreaker's Aura of Hate would have added +CHA to
melee weapon damage, doubled by the Resonance Stone, for roughly +65 on a full nova. That
trade is still accepted for the same reason: Inquisitor's Might is the only
non-concentration per-hit Radiant source that keeps Luminous Armour firing.

**T2-11 — Hold Person from an L3 pact slot.** 2p2QqzNsfec 34:36. Upcasting adds one target
per slot level above 2nd and the DC does not change, and the pact slot returns on a short
rest. Two Held bodies answer the recorded nova caveat, where the Held target dies mid-turn
and the rest of the chain lands on something un-Held at roughly half value. Cost: one
Shield or Counterspell reaction that fight. Verified: bg3.wiki Hold_Person.

**T2-12 — Elixir of Heroism on days with nothing to Hold.** 01A_BHMeLQU 34:53. +1d4 to
every attack roll and saving throw until long rest, and the wiki records it as a distinct
condition, so it stacks with Bless. Against a Held target it adds nothing and Bloodlust
stays the nova elixir. On undead, construct and crit-immune days there is no nova to feed,
and +1d4 on every Risky Ring concentration save beats a kill-gated Action. Skip Armour of
Agathys on those days, because temp-HP sources do not stack and Heroism is not one.

**T3-C1 — Divine Sense.** Bonus action, short-rest recharge, two turns of advantage against
undead and fiends. It was listed as a char-3 gain and never mentioned again, and those are
exactly the fights where Hold Person and Command fail.

**T3-C2 — Aura of Protection must be cast once.** Wiki: it is not on by default and a
respec removes it, so it needs casting at char 8 and again at char 11. Radius 3 m. A
forgotten toggle is −4 or −5 on every party saving throw.

**T3-C4 — Hexblade's Curse application text.** Once per short rest, bonus action, 20% free
proc on a hit with a hexed weapon, and it heals Charles for Warlock level + CHA when the
target dies. None of that was in the file. Curse the nova target on the set-up turn, which
is also what Accursed Spectre needs (T1-3) and what T4-U1 would make mandatory.

**T3-C5 — Shadow Blade's own advantage.** bg3.wiki Shadow_Blade passive: advantage against
Lightly or Heavily Obscured targets. A second advantage route that needs no arrow, and the
replacement for the Darkness advantage T4-V2 removed.

**T3-C6 — Radiant Shockwave never orbs allies.** Wiki: all non-allied creatures, neutrals
included. Asterion can stand on the Held target; watch neutral NPCs.

**T3-C7 — the GWM sentence.** "All In could never apply behind a shield" is true but covers
only half the feat. The wiki confirms the Bonus Attack needs no two-hander and no All In,
so the file now says the bonus attack was weighed and lost to Savage Attacker.

**T3-C8 — A Most Bloody Inheritance.** Bhaal's-chosen party buff at High Hall if Charles
defeated Orin: crit threshold −2, stacking, plus Stunning Gaze. The one Bhaal-path payoff
for the other three party members, recorded on the Bhaalist Armour row alongside the
Vicious Shortbow / Echo of Abazigal unlock.

**T2-28 — Boots of Stormy Clamour shared with Asterion.** 4naQFyHry2M 24:26. Asterion
inflicts more conditions per turn than anyone (Stun, Topple Prone, Bleeding from Flawed
Helldusk, Ability Drain), each adding 2 turns of Reverberation, so the next Stunning Strike
CON save is at −2 to −4. The cost to him that fight is Night Walkers' Misty Step in Acts
1–2 or Kushigo's +WIS per hit in Act 3 (≈ +20). Rule recorded on both of Charles's Stormy
Clamour option rows: whoever inflicts more conditions that fight wears them.

**T2-24 — Plant Growth under Hunger of Hadar, no fire in the zone.** 4KkXqqeKz80 28:02.
Gale's Armour of Landfall grants Plant Growth once per short rest. Under Hunger of Hadar
(Blinded, so they cannot jump, plus quarter speed) it is a multi-turn no-save lock with
Repelling Blast pushing escapers back. Standing rule: no Fireball, Scorching Ray or Heat
into the zone, because fire burns Plant Growth away (bg3.wiki/wiki/Plant_Growth). Gale's
fire goes at targets outside; Charles and Bonbon work the inside.

**T2-25 — Phalar Aluve is always Shriek.** 6i-Rpr9ziqs 36:19 argues for Sing in
survival fights (wielder and allies within 6 m get +1d4 to attack rolls and all saving
throws for 5 turns; the "mental" tooltip is wrong). Declined as a per-fight mode: Shriek's
−1d4 to enemy saves and +1d4 Thunder per damage instance is what the nova and Gale's
Scorching Ray run on. Whether Sing stacks with Bless is unverified anyway (distinct stack
ID). Bonbon carries the sword from the Stone and carries Shriek.

**T4-V2 — Darkness grants advantage only against enemies without darkvision.** 5yTLH3BWrW0
8:52 plus wiki darkvision mechanics: Attacking from Shadows needs the target to lack
darkvision, or to be beyond its range. Goblins, gnolls, duergar, drow and Shadow-Cursed
creatures all see him, which is most of Acts 1–2. The cloud's real value is the ranged
block in both directions and the Blinded condition on enemies inside it. Every
"advantage in, disadvantage out" and "Darkness Arrows for advantage" line is gone; the
accuracy plan is the Risky Ring from Act 2 and Shadow Blade's obscured-target advantage
(T3-C5).

**T4-V3 — Counterspell against a higher-level spell rolls INT.** Live wiki bug. Charles's
Counterspell comes off an L3 pact slot and his INT is 8, so it covers spells of level 3 and
below outright and is a 20–30% roll against 4th level and above. Gale can upcast from a
Sorcerer slot to remove the check; Charles cannot.

**T4-V5 — Paralysed auto-crits apply to any attack within 3 m, not only melee.** The Hold
Person `why` said "from melee within 3m". Corrected. It changes nothing for Charles, who
only swings, but it is the rule Gale and Bonbon act on.

**T4-V6 — the Mirror of Loss +2 is not guaranteed.** One DC 25 Religion check per
character, and a failure locks that character out forever, then a 60% roll per attempt.
Religion is INT-based and only Charles is proficient, at INT 8. His CHA 20 end state
assumes it. Plan: Enhance Ability from Bonbon, Guidance, and a quicksave before each
prayer. (s50sTy53DZw 3:08; bg3.wiki/wiki/Mirror_of_Loss.)

**T4-U5 — Helldusk Helmet stays in the crit-immune list.** The report expected the full
wiki page to show no critical-hit immunity and asked for it to be dropped from the
pre-nova check list. It does show it. `bg3kb/.venv/Scripts/python -m bg3kb.cli "Helldusk
Helmet" --k 3 --full` returns, under "The wearer of this item gains": *Attackers can't land
Critical Hits on the wearer.* Alongside Infernal Sight, Magical Durability +2 and
Immolating Gaze. So the item was already recorded correctly and no edit was made. This
check is closed, not open.

---

## Creation and stats

**`class`** — final split Paladin 6 / Hexblade Warlock 6 (was Paladin 7 / Warlock 5). See
T1-3 above. The respec at char 9 is unchanged at Warlock 5 / Paladin 4; only char 12
differs.

**`locked_decisions`** — the five locks, at length:

1. *Gloves of Battlemage's Power from Act 2* — the Arcane Acuity engine, and the reason
   Hold Person and Command land.
2. *Luminous Armour in every act* — the Radiant Shockwave engine. Medium armour, AC 15 +
   DEX (max 2) = 17 for the whole run. Accepted cost: no Helldusk Armour AC 21 in Act 3.
3. *Oath of Vengeance, never broken* — Inquisitor's Might is the per-hit Radiant that feeds
   the Shockwave.
4. *Concentration is Hold Person* — he sets up his own auto-crit nova and holds nothing
   else.
5. *A shield in the off-hand from the Grove onward* — a plain +2 AC Shield from any vendor
   (the Safeguard Shield is Bonbon's), then the Adamantine Shield, then Viconia's Walking
   Fortress. He never two-hands and never dual-wields, which is why neither Great Weapon
   Master nor Dual Wielder is ever taken.

**`stats_note`** — point-buy 8/14/15/8/10/15 spends all 27 points, because CON 15 and CHA
15 cost 9 each. Half-Orc +2 → CHA 17 and +1 → CON 16. Nothing left over.

**`ability_targets`** — CHA 17 → 18 (Hag's Hair, modded so it is available) → 20 (Mirror of
Loss, subject to T4-V6). CHA drives Aura DCs, attack and smite accuracy, Inquisitor's
Might's radiant rider, the Hold Person DC and the prepared-spell count. CON stays 16; the
Amulet of Greater Health sets it to 23 in Act 3 anyway.

**`race_notes`** — Half-Orc Savage Attacks adds an extra weapon die on melee crits, and a
second extra die to Divine Smite on a crit; that second die is disabled in Honour mode
only, and this is a non-Honour run. Relentless Endurance is a free once-per-long-rest
death save. He is the origin character, so the Hag's Hair goes to him.

**`creation.notes`** — Warlock 1 first is deliberate, at creation and again at the respec.
At STR 8 he needs Bind Hexed Weapon from the first fight, and Paladin-first would only buy
heavy armour proficiency, which a build locked to medium Luminous Armour never uses. Act 1
stops Warlock at 2: Hexblade gives CHA weapon binding and Devil's Sight, then Paladin 1–5
gives Inquisitor's Might at char 3, Divine Smite at char 4, Alert at 6 and Extra Attack at
7. Paladin 6 for Aura of Protection if char 8 lands before the Stone. Because the oath is
never broken there is no Oathbreaker Knight to pay and no oath bookkeeping at the respec.

**`creation.proficiencies.armor_weapons`** — Hexblade grants medium armour, shields and
martial weapons. Multiclassing into Paladin does *not* grant heavy armour, which is why the
Grymskull Helm is illegal on him at every point in the run.

---

## Leveling

**char 1 · Spells** — exactly two spells known at Warlock 1, not four. The Hexblade
expanded list (Shield, Wrathful Smite) is folded into the choosable options rather than
granted, so those are two more candidates competing for the same two picks. Hex and Armour
of Agathys win: sustained per-hit damage while arrow darkness keeps Concentration free, and
durable non-concentration temp HP. Wrathful Smite becomes preparable off the Paladin list
at char 4, and Shield is the Warlock-2 pick on the very next level, so paying a pick for
either here would waste it.

**char 1 · Skills** — Deception and Religion, matching `proficiencies.md`. Intimidation is
the trap: Half-Orc Menacing and the Haunted One background both grant it and proficiency
does not stack.

**char 2 · Invocations** — Devil's Sight and Agonising Blast. Devil's Sight was described as
"what makes an arrow cloud into an advantage engine"; T4-V2 killed that reading, so its
value is now fighting unblinded inside the cloud while everyone else is Blinded. Agonising
Blast scales the ranged fallback with CHA.

**char 2 · Warlock spell** — hidden behind the invocation screen. Warlock 2 raises Spells
Known from 2 to 3, so there is a third level-1 pick that is easy to click past. Shield is
it: a reaction, no Concentration, and the cheapest protection for a build that never rises
above AC 17–18 early. The other candidates were Wrathful Smite (preparable off the Paladin
list from char 4 anyway), Hellish Rebuke and Protection from Evil and Good.

**char 3 · Oath** — Vengeance is locked, not a stop on the way to Oathbreaker. It is the
only oath that supplies a non-concentration per-hit Radiant rider, and it hands over Hold
Person and Misty Step free at Paladin 5, which is where the whole nova setup comes from.
Costs accepted knowingly: Oathbreaker's Aura of Hate (≈ +65 on a full nova, Stone-doubled),
and Darkness and Crown of Madness never arriving free. If Divine Smite alone ever proves to
be enough of an Orb source, Oathbreaker becomes worth revisiting; that decision is deferred
past Act 2.

**char 4 · Fighting style** — Duelling. He fights one-handed behind a shield from the Grove
onward, and a shield is not a weapon, so the style's "nothing in the other hand" clause is
satisfied: +2 damage on every Phalar swing and later every Shadow Blade swing. Defence's +1
AC is the alternative if AC is wanted over damage; the shield already supplies +2.

**char 4–12 · Prepared spells** — the count is Paladin level + CHA modifier and the list
re-opens every level and swaps freely out of combat, which is why the rows give a whole
loadout rather than an increment. Bless is deliberately absent throughout: it is
Concentration, and Asterion casts it off the Staff of Arcane Blessing. Divine Favour and
Shield of Faith are listed as on-the-record Concentration options that will never actually
be cast. Left out as bottom tier: Searing Smite, Heroism, Cure Wounds. Branding Smite is
skipped despite being Radiant and feeding the Shockwave, because it is Concentration. Magic
Weapon is skipped because Bind Hexed Weapon makes it redundant. Unused slots become Divine
Smites. With the T1-3 change the count stops at eleven (Paladin 6 + CHA 5) at char 11
instead of reaching twelve at char 12, and the char-12 row now records the seventh Warlock
spell known instead of a prepared-spell increment.

**char 5 · Channel Oath budget** — one short-rest charge buys Inquisitor's Might or Vow of
Enmity, never both. Vow of Enmity is Bonus Action, 3 m, advantage on attacks against one
enemy for 10 turns, and the wiki notes a self-cast bug that extends the advantage to all
targets. Rough guide: Vow of Enmity for a long Act 1 boss fight, where 10 turns of
advantage doubles the crit rate before Hold Person exists. Inquisitor's Might everywhere
else and always from Act 2, because the Risky Ring supplies advantage by then and the
radiant rider becomes the scarcer resource.

**char 6 · Feat: Alert** — +5 Initiative and Surprise immunity, permanently. He is the
party's slowest body at d4+2; Alert makes it d4+7, still behind Gale's d4+11 so his first
turn is already Hasted, but ahead of nearly every enemy, so Hold Person goes up before they
act.

**char 8 · Timing** — the Stone normally arrives late enough that char 8 comes first. Aura
of Protection is the best interim Paladin level: +CHA to the party's saves, and the first
line of defence for the Hold Person concentration he is about to start carrying under the
Risky Ring. Cast it (T3-C2).

**char 9 · respec at the Resonance Stone** — a Withers respec rebuilds from scratch and
re-presents every earlier choice, including patron, skills, oath, fighting style, cantrips
and invocations. Coming back at Paladin 4 he only re-earns the Paladin-3 oath grant, so
Bane and Hunter's Mark are free again but Hold Person and Misty Step are not; those need
Paladin 5 and do not return until char 10. Bridge those two levels with Hunger of Hadar or
Bonbon's Hold Monster rather than spending one of the six Warlock picks on Hold Person.

**char 9 · Invocations** — three, not two: two at Warlock 2 plus one at Warlock 5.
Invocations cannot be swapped on level-up, so the respec is the only chance to set all
three. Repelling Blast turns Eldritch Blast into ledge control and shoves escapers back
into Hunger of Hadar. Avoid Fiendish Vigour: its at-will False Life clashes with Armour of
Agathys, because temp-HP sources never stack.

**char 9 · Warlock spells** — six known at Warlock 5, and the list changed from earlier
plans. Darkness is out because it competes with Hold Person for Concentration and farmed
arrows do the same job for free. Misty Step is out because it now arrives free from the
oath. Those two freed picks go to Shield and Mirror Image, both non-concentration defence,
which is what a chest locked at AC 17 actually needs. Hunger of Hadar stays as the
non-humanoid Concentration alternative. Hex is dropped because Hold Person owns the slot
permanently. A seventh arrives at Warlock 6 (char 12).

**char 9 · Paladin feat** — the usual char-9 respec has levels for both feats. If the Stone
lands at level 8, take Warlock 5 / Paladin 3 for Alert and add Paladin 4 with Savage
Attacker on the next level.

**char 12 · Warlock 6** — see T1-3. The seventh spell known is a spare: Darkness as a
second cloud source, or a Warlock Hold Person if a second Hold off a short-rest slot is
worth more than the spare. Self-cast Darkness still costs Concentration, so the arrows
remain the default either way.

---

## Spells

**`spells.note`** — the whole block exists to record one constraint: his Concentration is
Hold Person and nothing else, so Bless, Divine Favour, Hex, Darkness, Branding Smite and
Wrathful Smite are all out of the rotation despite being available. Darkness comes from
farmed arrows, which cost no Concentration; Bless comes from Asterion. Hunger of Hadar is
the one deliberate exception, swapped in only for fights where nothing is Holdable.

**Hold Person** — the concentration and the reason the nova works. The DC is what matters,
and the Gloves of Battlemage's Power are what raise it: Arcane Acuity is +1 spell save DC
per remaining turn up to +10, which is DC 27 at the cap. Build stacks with the Booming Blade
lead and the smites that follow, then Hold. Holding it excludes every other Concentration
spell he owns, and that is the intended trade. Humanoids only — see Hunger of Hadar for
everything else. T2-11 adds the L3 pact-slot upcast for two targets.

**Inquisitor's Might** — mandatory for three reasons. (1) It is the only per-hit Radiant
source he can run, because Divine Favour, Branding Smite and Crusader's Mantle are all
Concentration or out of level range, and Radiant is what triggers Luminous Armour's Radiant
Shockwave. (2) It needs no Concentration, so it coexists with Hold Person. (3) The Daze
rider has no saving throw at all. At CHA 17 the rider is +3 per weapon hit, rising to +5 at
CHA 20. It reaches 9 m and can target an ally — on Asterion's 4–6 unarmed hits it extracts
far more raw damage than on Charles's swings, but the Shockwave only fires on the *wearer's*
own Radiant damage, so it stays on Charles whenever the Orb stack matters.

**Divine Smite** — 2d8 Radiant at L1, +1d8 per slot level above 1st (cap 5d8 at an L4
slot), +1d8 against Fiends and Undead, and the dice double on a crit. Not a prepared spell
and not stopped by Counterspell. Paladin 6 plus Warlock 6 is eight slots per rest cycle
(4×L1 + 2×L2 Paladin, 2×L3 pact), down from nine before T1-3, which is still the reason
this build novas harder than a shallow Paladin dip.

**Shadow Blade** — level-3 pact slots start it at 3d8 Psychic, lasting until long rest with
no Concentration, which is exactly why it fits a build whose Concentration is spoken for.
The Resonance Stone doubles the Psychic. Its own passive gives advantage against Lightly or
Heavily Obscured targets (T3-C5), which is now the advantage route instead of the arrow
cloud (T4-V2).

**Shield** — locking Luminous Armour caps the chest at AC 17; the off-hand shield lifts him
to 19–20, and the reaction's +5 is still the cheapest way to turn a hit that would break
Hold Person into a miss.

**Mirror Image** — three duplicates, +9 AC, no Concentration: the best non-concentration
defence available to him and the direct answer to a locked AC 17 chest. Each miss removes
one duplicate.

**Armour of Agathys** — 15 temp HP and 15 Cold retaliation from a Warlock-5 L3 slot, no
Concentration. Temp-HP sources never stack, so run this *or* the illithid Shield of Thralls,
and cast Aid after it rather than before. Skipped on Elixir of Heroism days (T2-12).

**Aid** — self-centred 9 m radius, +5 maximum HP per member and +5 more per slot level above
2nd, lasting until long rest with no Concentration, and downed allies come back with an
extra hit point. Aid is Cleric or Paladin only and there is no Cleric, so Charles is the
party's only source. Cast it *after* summoning anything that should be covered.

**Command** — rated the #3 spell in the game and it uses no Concentration, so it coexists
with Hold Person. Run it as a mass disable: one extra target per slot level above 1st, so a
level-2 Paladin slot disables a cluster for the turn he needs to close. Its DC rides Arcane
Acuity, same as Hold Person. Does not work on Undead.

**Counterspell** — no scrolls exist, so it has to be learnt on level-up. See T4-V3 for the
INT check against higher-level spells.

**Hunger of Hadar** — the answer to Hold Person's humanoid-only limit, and warlock-exclusive
in this party. Large difficult-terrain zone that Blinds, deals Cold at the start of enemy
turns and Acid at the end, with the Acid save DC bugged to 12 per the tier note. Pairs with
Repelling Blast to shove escapers back in and with Plant Growth beneath it (T2-24). On
non-humanoid fights Bonbon attempts Hold Monster and Charles takes the zone.

**Booming Blade** — the cheapest way to put the first Arcane Acuity stacks up before casting
Hold Person. Adds Thunder from char 5, fires once per Action even with Extra Attack,
triggers the Ring of Arcane Synergy for 2 turns, and triggers the Gloves of Battlemage's
Power.

**Eldritch Blast** — two beams at char 5, three at char 10. Its attack rolls ride Arcane
Acuity, unlike his weapon swings.

**Wrathful Smite** — kept prepared, never cast. It is Concentration, so casting it drops
Hold Person and the auto-crit nova with it, but it is free off the Paladin list so it costs
nothing to hold for fights where nothing is Holdable and Hunger of Hadar is not worth the
slot.

**Bane / Hunter's Mark** — free and always prepared from the oath at Paladin 3, and neither
is on the general Paladin list, so the oath is his only route to them. Bane is the one with
a use (−1d4 to enemy attacks and saves) but it is Concentration, so it sits idle from char
7. Hunter's Mark duplicates Hex's +1d6 per hit and is out for the same reason. Phalar Shriek
covers the save-debuff role without Concentration.

**Hex (dropped)** — +1d6 Necrotic per hit and disadvantage on an ability, and it powers the
Strange Conduit Ring. Correct in Act 1 while arrow darkness keeps Concentration free, but
Hold Person takes the slot permanently from char 7, so it does not survive the respec.

**Darkness (not picked)** — self-cast Darkness would compete with Hold Person for
Concentration, and farmed Arrows of Darkness produce the same 3 m cloud with none of that
cost. Devil's Sight does not care which source made the cloud. Dropping it freed a Warlock
pick.

**Blink** — a chance to go Ethereal at the end of each turn, untargetable until his next.
The third contender alongside Shield and Mirror Image for pure evasion instead of AC. Rated
C only for solo play; in a party it redirects aggro to allies.

**Protection from Evil and Good** — strong against Aberrations, Celestials, Elementals, Fey,
Fiends and Undead, and its real effect is blanket Frightened immunity rather than the
charm protection the tooltip claims, but it is Concentration, so it sits with Bless and Hex.

**Bone Chill** — ranged anti-healing with no save, plus advantage against Undead. Take it
over Mage Hand when that niche beats exploration utility.

---

## Itemization — Act 1

**`early-hexed-weapon`** — Hexblade can bind anything, and a shield's +2 AC is worth more
than a Versatile weapon's larger die.

**`phalar-aluve-two-handed`** — one-handing it costs one point of average damage (d8 rather
than the Versatile d10) and Duelling gives two back from char 4. The 6 m Shriek aura covers
Charles and Asterion. At the Resonance Stone the sword goes to Bonbon's melee set for good
and she carries Shriek from then on. Always Shriek, never Sing (T2-25).

**`plain-shield-charles`** — one-handing the bound weapon buys +2 AC from level 1 on the
body that will carry Hold Person. It holds the slot until the Adamantine Shield is poured.

**`adamantine-shield`** — the second Mithral ore, poured with the Shield mould rather than
into an Adamantine Scale Mail nobody wears now that Luminous Armour is locked. This is the
crit immunity the guide gave up by locking the chest, put back on the body that needs it
most: a critical hit roughly doubles a concentration save DC, and from char 7 he is
concentrating on Hold Person in every fight. His melee set is the *active* set, so the
shield's crit immunity is live; the inactive-set caveat that stopped Bonbon parking one
behind her bow does not apply to him.

**`haste-helm`** — he keeps it rather than lending it out, because he has the party's worst
initiative at d4+2 and the longest distance to close.

**`luminous-armour`** — Radiating Orb is −1 to attack rolls per remaining turn, stacking
duration on reapplication up to −10. He has exactly two Radiant sources feeding it,
Inquisitor's Might on every weapon hit and Divine Smite, which is precisely why the oath is
Vengeance and not Oathbreaker. The accepted cost is AC 17 all run and no Helldusk Armour AC
21 in Act 3; Shield, Mirror Image, the Adamantine Shield, the Helm of Balduran and Aura of
Protection are the compensation. It hits non-allied creatures only, neutrals included
(T3-C6).

**`act1-hands-charles`** — a placeholder by design: his best-in-slot does not exist until
the Reithwin Tollhouse in Act 2, so nothing here is worth committing to. Growling Underdog
is the default because it is a free advantage source before the Risky Ring and while Vow of
Enmity still competes with Inquisitor's Might for the single Channel Oath charge. Baneful
Striking is better on any turn the party needs a save to land — Asterion's Stun, or his own
Command. Gloves of Power are the weakest of the three but free and early.

**`boots-of-striding`** — Focused Stride grants Momentum on casting a Concentration spell
and blocks Prone and forced movement while it holds, which matters enormously from char 7,
because falling Prone ends Concentration outright with no save. Before char 7 the only thing
it protects is Hex, which is cheap to lose, so Stormy Clamour is the Act 1 default. The same
kill (Minthara) yields Gale's Spidersilk Armour.

**`opt-boots-of-stormy-clamour-charles-a1`** — the engine: Inquisitor's Might puts Radiant on
every weapon hit from char 3, each hit fires a Radiant Shockwave, and each Shockwave applies
Radiating Orb, which is a condition. The boots carry a hidden OncePerAttack limit, but the
Shockwave is a CreateExplosion event, which resets that limit, so every swing procs rather
than only the first. Reverberation is −1 to STR, DEX and CON saves per turn, and at 5 turns
it forces a Prone save at an effective DC 15. One target per trigger: the Shockwave spreads
Radiating Orb to everything within 3 m but only the first creature gets the Reverberation,
so this is single-target pressure, not an AoE lock. Gale gives them up because his
Reverberation payload is empty in Act 1 — Belligerent Skies needs Thunder, Lightning or
Radiant and he casts fire, and Coruscation, Callous Glow and Spineshudder are all Act 2.

**`ring-of-arcane-synergy`** / **`strange-conduit-ring`** — do not also give him Bonbon's
Diadem of Arcane Synergy; it is the same condition and will not stack with itself. Strange
Conduit is rated #5 of the 20 best Act 1 items for exactly this kind of multiattacking
concentrator; it used to depend on him holding Hex or Bless inside an arrow cloud, and now
that Hold Person is permanent it is simply always on. Per the wiki it covers melee, ranged
and Thrown but *not* Unarmed Strike, which is why it can never move to Asterion.

**`arrows-of-darkness`** — the darkness source for the entire run, not just Act 1, because
Hold Person owns his Concentration permanently and the Darkness spell was therefore dropped
from his Warlock picks. Prefer Bonbon placing it; from the Stone she also carries Phalar and
Shriek, and she fires it last in her turn aimed at the ground. See T4-V2 for what it does
and does not buy.

**`dual-hand-crossbows-plus-one`** — mainly a Darkness-Arrow launcher. Once he stands inside
his own cloud it blocks ranged attacks into and out of itself, so the slot is close to dead;
that is exactly why the Act 3 bow is a passive stat stick.

**`act1-cloak-charles`** — deliberately empty, not an oversight. The Deathstalker Mantle is
the only magical cloak obtainable in Act 1 and it goes to Asterion; every other cloak first
appears in Act 2 or Act 3.

---

## Itemization — Act 2

**`gloves-of-battlemage-s-power`** — the confirmed triggers are every Shadow Blade weapon
attack, Booming Blade, and any smite spell. Reaction Divine Smite triggers nothing on its
own: it inherits the attack it rides on, so +0 off a plain weapon swing, +4 when it chains
off an attack that already triggered, and +2 only if Divine Smite is cast straight from the
action bar. That costs him nothing as written, because he always leads with Booming Blade or
a smite and every Shadow Blade swing is itself a trigger, so each attack-plus-reaction-smite
is +4 — the Luminous Armour shockwave is what resets the once-per-attack limit between them.
It breaks the moment he binds the Knife of the Undermountain King main hand against
Psychic-immune targets: plain weapon swings are not spells, so only the Booming Blade lead
and smite spells feed Acuity in those fights. Acuity duration drops by 2 every time he takes
damage, so build stacks and cast Hold Person before the enemy's turn. The accepted cost is
the whole rest of the glove progression: Baneful Striking, Helldusk Gloves and Craterflesh
Gloves (≈ +49 on a full nova, Bhaal path) are all forgone.

**`act2-offhand-charles`** — Ketheric's Shield (+1 spell save DC) drops at the Colony and
goes to Bonbon: crit immunity is worth more to Charles than +1 on a DC that Acuity already
caps.

**`act2-head-charles`** (Holy Lance Helm) — ignore the damage; Smite the Graceless is 1d4 on
a fixed DC 14 Dexterity save and will not matter. Take it for what the Radiant tick plugs
into: it is Radiant, so it fires a Luminous Armour shockwave and spreads Radiating Orb *on
enemy turns*, and it is a confirmed Battlemage's Power trigger, so it also refills Arcane
Acuity between his turns. That is the direct answer to Acuity decaying by 2 every time he is
hit, and it is self-reinforcing, because it only fires when an attack misses and Radiating
Orb at −10 plus Mirror Image makes enemies miss constantly. Requires Medium Armour
proficiency, which Hexblade grants. Act 3 keeps the Helm of Balduran instead: crit immunity
protecting the Hold Person concentration beats an off-turn Acuity trickle.

**`opt-covert-cowl-act2`** — −1 crit threshold while Obscured, and standing inside an arrow
cloud is Heavily Obscured. Same redundancy that demoted Risky Ring and Killer's Sweetheart:
you cannot improve on a guaranteed crit. Illegal on Asterion, whose Unarmoured Defence
breaks on any helmet marked as armour, so there is no contest for it.

**`opt-boots-of-stormy-clamour-charles-a2`** — Act 2 is the peak because the Holy Lance Helm
fires on enemy turns, on whichever creature missed, so this is the one channel that does
spread Reverberation across a pack. On his own turn it is one proc per attack, three or four
with Haste. The cost is exactly what Striding was buying: a single successful knockdown
drops Hold Person and the nova with it, and the Risky Ring gives him disadvantage on that
save. Reverberation feeds nothing this party controls with — Hold Person, Hold Monster,
Command and Fear are all Wisdom saves. It buys the Prone pop and Asterion's Stunning Strike,
which is a Constitution save. Shared with Asterion per fight (T2-28).

**`act2-amulet-charles`** — genuinely open. The Amulet of Misty Step was carrying the slot
and Paladin 5 hands him Misty Step free, so its whole reason for being there is gone.
Nothing in the Act 2 pool is clearly best and the Amulet of Greater Health in Act 3 is the
real answer.

**`opt-spineshudder-amulet-charles`** — recorded as a correction, not a recommendation.
Crackling Resonance fires on the wearer's own *ranged spell attacks*, not when the wearer is
hit; the on-being-hit effect is the Thunderskin Cloak. Charles's only ranged spell attack is
Eldritch Blast, cast only to Repel escapers back into Hunger of Hadar, so on him it does
almost nothing. It is Gale's.

**`act2-ring2-charles`** — against a Held target both Risky Ring and Killer's Sweetheart
contribute exactly zero, because advantage and a guaranteed crit are worth nothing when
attacks already auto-hit and auto-crit. That is why ring 1 became the Strange Conduit Ring
and both crit-fishing rings dropped to the flex slot.

**`risky-ring`** — two costs, not one: disadvantage on saves roughly squares his
concentration-failure rate while he permanently holds Hold Person, and the advantage itself
is dead weight on any turn the target is already Held. Mitigate in order: the Adamantine
Shield's crit immunity, Aura of Protection at Paladin 6, the Cloak of Protection and the
Amulet of Greater Health.

**`ring-of-arcane-synergy-act2`** — worth about +20 on the turn it switches on and +30 on
every turn after, because it stacks on top of the pact weapon's own CHA modifier and the
Stone doubles it.

**`cloak-of-protection`** — the arbitration: exactly one exists and it is the only cloak in
the Act 2 pool that touches saving throws. Charles carries a permanent self-inflicted
disadvantage on every save from the Risky Ring while holding the party's Hold Person, and he
stands in every area attack. Gale can be positioned out of danger and has CON-save advantage
from Spidersilk plus save proficiency; Bonbon has AC 18.

**`resonance-stone-aura`** — no effect on Undead or Constructs, and it also gives *allies*
Psychic Vulnerability plus disadvantage on mental saves, which is a real cost on a party
whose Hold Person concentration matters. Asterion carries it within 9 m of Charles, closing
to 6 m when both need Shriek. Holster it against Psychic attackers and dangerous mental-save
effects, and expect it to stop working once Act 2 ends.

---

## Itemization — Act 3

**`shadow-blade-phalar-act3-default`** — two Shadow Blades is not an option: the wiki's only
route to a second one is a hireling soul-recall exploit, the copies use the spell's base
damage rather than the upcast, and they are called out as not working properly with
Battlemage's Power, which is the locked glove this build is built on.

**`viconias-walking-fortress`** — reachable without Shadowheart by passing the House of Grief
investigation into the cloister and refusing Viconia's demand, which starts the fight. +3
AC, advantage on saving throws against spells, spell attacks against him at disadvantage,
Bulwark Rebuke (2d4 Force and possible Prone when a melee attack hits him), Reflective Shell
once per short rest and Warding Bond once per long rest. It replaces the Adamantine Shield
only once the Helm of Balduran supplies crit immunity.

**`act3-head-charles`** — it beats Sarevok's Horned Helmet, which offers more crits but no
protection for the concentration the whole nova depends on. Also 2 HP per turn.

**`act3-armour-charles`** — this is where the Luminous Armour lock costs most: Helldusk
Armour would have given AC 21 flat and −3 to all incoming damage.

**`act3-hands-charles`** — the other place the lock costs real damage. Helldusk Gloves are
+1d6 Fire per hit, roughly +17 a nova, plus a wiki-confirmed +1 to all attack rolls, and they
now go to Bonbon. Craterflesh Gloves are +2d6 Force on a crit, roughly +49 on a full
auto-crit nova, Bhaal path only.

**`act3-feet-charles`** — Infernal Evasion turns one failed saving throw into a success for a
Reaction, but per the wiki it is once per *long rest*, not once per turn, so it is an
emergency button and not the answer to the Risky Ring; the Amulet of Greater Health is what
actually cancels that disadvantage. Contested with Gale, who cannot wear Boots of Persistence
at all; Charles wins on the Prone immunity.

**`amulet-of-greater-health`** — both halves matter only here: CON 23 is +6 to concentration
checks, and the advantage cancels the Risky Ring's disadvantage so those rolls go back to a
straight d20. On a build whose entire nova rests on keeping Hold Person up, this is the
single most important Act 3 pickup. Contested with Gale; Charles wins because Armour of
Landfall already gives Gale CON-save advantage. Steal tip: DC 20 Sleight of Hand if the
Orphic Hammer, the Soul-Sworn Contract and Hope are left alone — an Asterion job.

**`act3-ring1-charles`** — 37.5 damage across the four-attack standard nova and more than 60
across the Terazul ceiling turn. It is Psychic, so it is the single line most exposed to the
Resonance Stone failing after Act 2.

**`act3-ranged-charles`** (Vicious Shortbow) — Dolor Amarus is listed on *the holder*, not the
main hand, and the wiki states it applies to all weapon attacks while a weapon carrying the
feature is equipped: +7 flat on every critical hit. Every swing against a Held target crits,
so that is +21 on the standard nova and +63 on the Terazul turn, out of a slot that was
otherwise dead, because a Darkness cloud blocks ranged attacks both ways and he could never
shoot from it anyway. Ranged and melee weapon sets are separate, so it does not touch Shadow
Blade or the shield. Taking it also settles the Hellrider Longbow, which Gale and Charles
both used to claim: Gale keeps it, and his Elixir of Vigilance stacks it to +8 initiative.

**`opt-hellriders-longbow-charles`** — the non-Bhaal fallback. Passive +3 initiative from the
same dead slot; even with Alert he is only d4+7.

**`bhaalist-armour-unlock`** — not worn. None of his damage is Piercing (Shadow Blade is
Psychic, Phalar is Slashing, Divine Smite is Radiant), it would buff nobody, and the chest
slot is locked to Luminous Armour anyway. Buy it on the Bhaal path for completeness. Charles
as the Dark Urge is what unlocks the Murder Tribunal stock, and the same decision buys the
Vicious Shortbow and, via Orin, A Most Bloody Inheritance (T3-C8).

---

## Progression

**`prog-armour`** — one chest for the whole run. Helldusk Armour's AC 21 and −3 damage go to
Bonbon instead.

**`prog-feet`** — a flex slot all run, sharing Boots of Stormy Clamour with the defensive
pick. Both Striding and Helldusk grant Prone immunity, and Prone ends Concentration
outright, so they are what keeps Hold Person up. Default to Stormy Clamour through Act 1,
when his Concentration is only Hex, and to the defensive boot from char 7 onward.

**`prog-ring2`** — a genuine flex from Act 2, decided by whether the target can be Held. The
Shadow Blade Ring needs no slot at all: summon, then unequip, then put the rings back on.

**`prog-offhand`** — he never two-hands or dual-wields after the Grove, which is why neither
Great Weapon Master nor Dual Wielder is ever taken.

**`prog-consumables`** — not a stopgap. Because Hold Person owns his Concentration
permanently, the Darkness spell was dropped from his Warlock picks and farmed arrows are the
darkness source for the entire run. Elixir split per T2-12.

---

## Playstyle

**Shriek is for Gale, not just the melee** — it adds 1d4 Thunder every time an affected enemy
takes damage, and Scorching Ray damages 3–7 separate times per cast, so activating it before
Gale's turn is worth roughly 7d4 on a single level-6 cast. From the Stone onward that is
Bonbon's call to make, from 3–6 m of the cluster.

**Drakethroat Glaive, once per long rest** — stand next to Gale so he can Twin Draconic
Elemental Weapon onto Charles and onto Bonbon's Titanstring Bow, dropped on the ground next
to him. Targeting Charles hits his main hand — the one-handed Phalar Aluve behind the shield
until the respec, the 3d8 Shadow Blade after it — for +1 Attack Rolls and +1d4 elemental
until long rest. From the Stone onward, summon the Shadow Blade *first*: a blade re-summoned
after the cast comes back unenchanted, and the glaive's cast is gone until the next long
rest. Gale sets the element to Cold every day.

**Darkness placement, historical note** — the old text read "put the cloud so Charles is
inside it and his target is not. He is an unseen attacker — advantage in, disadvantage out."
The first sentence still stands for the ranged block; the second was wrong (T4-V2).

**Defensive reads** — AC 19–20 behind a shield, crit-immune from the Forge (Adamantine
Shield) and again from the Helm of Balduran. Stay inside Aura of Protection range of the
party rather than running ahead.

---

## Nova

**`nova.assumptions`, moved out of the file:**

- **Resonance Stone** within 9 m makes the target Steeped in Bliss and therefore Vulnerable
  to Psychic, which doubles Shadow Blade, the pact-weapon CHA modifier and the Strange
  Conduit Ring — worth about 156 damage a turn. The wiki notes the Stone often stops working
  once Act 2 ends, and level 12 is Act 3, so confirm it still fires before planning around
  it. Without it the standard nova drops from 547 to 348 on the pre-shield-rework
  simulation.
- **Phalar Aluve: Shriek** is modelled at one proc per attack, which is the conservative
  reading; it may fire again off each smite. It lasts only 5 turns, recharges on short rest,
  costs Bonbon an Action (her Haste action on turn 1) and ends if she unequips the sword.
- **Savage Attacker** rerolls every damage die and the wiki confirms it covers damage
  riders, so Shadow Blade, Booming Blade's Thunder, Strange Conduit and Divine Smite all
  roll twice. **Half-Orc Savage Attacks** adds an extra weapon die and a second extra die to
  Divine Smite on every crit; that second die is disabled in Honour mode only.
- **Divine Smite (reaction) costs no Reaction resource** and can fire on every melee hit,
  limited only by spell slots. Set the L2 Critical Hit entry to auto-confirm and leave L1 and
  L3 on Ask, so auto-confirm cannot quietly eat a pact slot mid-nova.
- **Slot budget after T1-3.** Six Paladin slots, 4×L1 + 2×L2, not seven. Upgrading L2 smites
  to L3 buys only about +23 damage and costs both pact slots, which also carry Counterspell,
  Shield and the two-target Hold Person (T2-11).
- **Luminous Armour is what makes the Gloves work.** Radiant Shockwave uses CreateExplosion,
  which resets the Gloves' once-per-attack limit, and Inquisitor's Might makes every swing
  deal Radiant, so the limit resets on every single hit with none of the Perform or grenade
  tricks other builds need. Arcane Acuity caps at +10 (Hold Person DC 27) and Radiating Orb
  caps at −10 on any full nova.
- **Vicious Shortbow parked in the ranged slot** — Dolor Amarus is a holder passive, not a
  main-hand one, so its +7 per critical hit applies to every melee swing. He never fires the
  bow.
- **Arcane Acuity buys no damage.** It is +1 to spell attack rolls and spell save DC only, it
  never touches weapon swings, and he is already at the cap. A second Acuity source is
  insurance against the −2 duration he loses per hit taken, not throughput.

**Table numbers after T1-3.** The ceiling turn lost one smite: 8 of 9 attacks became 7 of 9,
using the report's ≈ 40 per L2 smite on a crit swing, so the smite line went 291 → 251 and
the turn total 1534 → 1494. The standard nova's 512 was simulated with three L2 smites; with
4×L1 + 2×L2 one of those three is now an L1, so the true figure is roughly 10 lower. It was
not re-simulated and the table still reads 512.

**`nova.caveats`, moved out of the file:**

- **The spread is tight, not swingy.** The standard nova runs 366–429 across the 5th–95th
  percentile, with an absolute floor of 146 and a ceiling of 731. The Terazul build averages
  1,481 (floor 462, ceiling 1,949). With roughly 25 dice all rolled twice, σ is only about
  20, so treat the averages as what actually happens. Those simulations predate the shield
  rework; dropping the off-hand Phalar swing and adding Duelling moves each total by under
  20.
- **Extra actions and Extra Attack.** The wiki's Extra Attack page says plainly that Hastened
  and Elixir of Bloodlust actions do get Extra Attack outside Honour, with a worked Tactician
  example. The Hastened and Terazul Jitters condition pages both carry a flat note saying the
  opposite. If the condition pages win, every extra action is a single attack, the ceiling
  turn collapses to roughly 700, and spending the Haste action on Hold Person costs nothing
  instead of costing a whole attack chain. Nothing else here swings this hard on one unknown.
- **Bloodlust's extra action needs a kill that turn**, and if the thing that dies is the Held
  target then everything after it lands on something un-Held: no auto-crit, roughly half
  value. The clean version is a Held add dying to the first chain while the boss stays Held.
  T2-11's two-target upcast is the structural fix.
- **Wrathful Smite is not a legal lead.** Smite spells cost Action + Bonus Action on hit, and
  Inquisitor's Might already spent the bonus action. It is also Concentration, so casting it
  would drop the Hold that makes every swing a crit. Booming Blade simply hits harder anyway:
  23.2 from a crit-doubled 4d8 Thunder against 17.9 from a Stone-doubled 2d6 Psychic. The same
  reasoning rules out Thunderous Smite.
- **Dolor Amarus may be much larger than modelled.** The wiki adds that it "stacks on multiple
  damage riders, which could potentially lead to massive bonuses from different damage
  sources." If that means +7 per *rider* rather than per attack, a swing carrying weapon
  damage, a smite, Strange Conduit and Inquisitor's Might would collect it several times over.
  The tables use the conservative +7 per attack — worth one combat-log check.
- **Risky Ring and Killer's Sweetheart contribute exactly zero against a Held target.**
  Advantage and a guaranteed crit are worth nothing when attacks already auto-hit and
  auto-crit. That is why ring 1 is the Strange Conduit Ring and both of those dropped to the
  flex slot.

---

## Declined for Charles, with the report's reasons

**T2-13 · Great Weapon Master for its bonus-action attack, replacing Savage Attacker** —
MuodaDzKp98 14:33, 9qa8wa1WEVg 15:59. The wiki confirms the Bonus Attack needs no two-hander
and no All In, and on a Held target every swing crits, so each nova turn would buy a
bonus-action auto-crit swing, about +110 on the 512 standard nova. Declined because Savage
Attacker's reroll is about +50 on the standard nova but +120 to +150 on the nine-swing
ceiling, GWM does nothing on a turn with no crit or kill, and the bonus action already
carries Inquisitor's Might and Hexblade's Curse. The GWM sentence in `feats` was corrected
instead (T3-C7).

**T2-14 · Warlock 3 Shadow Blade in Act 1** — 9qa8wa1WEVg 13:24. 2d8 against Phalar's d8+2 is
+2.5 a swing, but Warlock 3 at char 3 pushes Inquisitor's Might, Divine Smite, Alert and Extra
Attack one level each for all of Act 1, and Phalar's Shriek leaves his hand. The respec at
char 9 erases it anyway.

**T2-15 · Great Old One patron at the Stone respec instead of re-picking Hexblade** —
m2F7dNXEwNc 5:45. Mortal Reminder forces a Wisdom save on the target and nearby enemies on
every critical hit or they are Frightened (bg3.wiki/wiki/Mortal_Reminder), and after the
respec every swing at a Held target crits, and the Resonance Stone already gives nearby
enemies disadvantage on Wisdom saves. Declined because it costs Hexblade's Curse (+36
standard / +72 ceiling by the current tables, far more if T4-U1 is true), the heal on kill,
and the Shield spell, which is not on the base Warlock list. The Held target does not need
frightening and the enemies near it are the ones Asterion is punching. Whether Mortal
Reminder's DC takes Acuity is unverified.

**T3-C3 · The Dead Shot as Charles's non-Bhaal ranged stat stick** — only one copy exists and
T1-2 gives it to Bonbon, whose Keen Attack doubling and +2 turn it into +5 to hit and a 19
crit threshold on a build with eight projectiles a Hasted turn. The idea is removed from
Charles's file entirely. His non-Bhaal fallback stays the Hellrider Longbow, borrowed from
Gale.

**Also considered and left alone** (report Tier 5): Paladin 5 / Warlock 7, Paladin 2 /
Warlock 10, Paladin 9 / Warlock 3, mono-Paladin 11; Crown, Ancients and Devotion oaths; a
Charisma ASI instead of Savage Attacker; self-cast Darkness instead of farmed arrows;
Lockadin initiative gear (Gloves of Dexterity, Soulbreaker, Yuan-ti); Helmet of Arcane
Acuity + Band, Ketheric's Shield, Rhapsody off-hand, Potent Robe, Coruscation, Callous Glow,
Hellrider's Pride, Shar's Spear of Evening, Clown Hammer, the Snowburst ice combo, Cloud of
Daggers, Hex, a DEX 16 / CON 14 spread, Bone Chill over Mage Hand, and the re-bind curse
exploit.

---

## In-game checks

Each of these needs one play session to settle. Nothing in the content file depends on them
being true.

1. **Hexblade's Curse: per damage roll or per swing?** (T4-U1.) Two videos' combat logs show
   +proficiency on every damage instance — weapon, Booming Blade, smite, riders — not once per
   swing. A nova swing carries four or five instances, so the ceiling's 72 would be about 200
   and the standard nova gains about +70 whenever the curse is up. The wiki wording ("damage
   rolls") is consistent but not explicit. Check: one cursed target, one smite, read the
   combat log. (0CbK5ufVk-g 46:37, zIiqb32iN9w 19:37.)
2. **Does a reaction interrupt a multi-projectile spell?** (T4-U4 / T2-23.) zIiqb32iN9w 22:43
   shows a reaction — Hellish Rebuke or an opportunity attack — interrupting the first
   projectile of Magic Missile or Scorching Ray and dropping the remaining projectiles.
   Unverified in the KB. If true, Charles is the natural baiter: step out of melee to draw the
   opportunity attack before Gale casts.
3. **Threatened on ranged spell attacks within 3 m.** (T4-V5 caveat.) Paralysed grants
   advantage to any attack within 3 m, but it is unconfirmed whether a ranged spell attack
   inside an enemy's reach takes Threatened disadvantage, which would cancel it. Decides
   whether Gale should stand inside 3 m of a Held target for Scorching Ray crits.
4. **Helldusk Helmet crit immunity — CLOSED.** Confirmed by the full wiki page: "Attackers
   can't land Critical Hits on the wearer." It stays in the `nova.caveats` pre-nova check
   list. No in-game check needed.
