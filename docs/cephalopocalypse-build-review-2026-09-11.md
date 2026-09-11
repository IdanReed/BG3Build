# Cephalopocalypse build review — candidate changes for y/n

Reviewed 2026-09-11. Thirty-three Cephalopocalypse videos shortlisted in
`cephalopocalypse-videos.md` were fetched as auto-caption transcripts
(`resources/videos/transcripts/<id>.md`), summarised one file per video in
`resources/videos/summaries/`, and compared by thirteen reviewers against the four
character files, `content/party.md`, `content/loot.md`, the deviation register and the
2026-09-10 / 2026-09-11 changelog entries. Every mechanics claim that decides a
candidate was checked against bg3.wiki through `bg3kb`; the `verify` line says which
survived.

The party under review: Charles (Vengeance Paladin 7 / Hexblade Warlock 5), Asterion
(Open Hand Monk 9 / Thief Rogue 3), Gale (Draconic Red Sorcerer 11 / Fiend Warlock 1),
Bonbon (Swords Bard 11 / Fighter 1). Non-Honour, Patch 8, modded Hag's Hair.

How to read this: each candidate has an ID. Answer y/n per ID. **Rec** is the
reviewer's lean, not a decision. Where several videos raised the same change the
count is given, because convergence across independent guides is the strongest
signal this corpus offers. Tier 5 lists what was considered and not recommended, so
nothing is silently dropped.

---

## Tier 1 — Significant shifts that could be better

Class split, level order, or a core-engine item. Big work, big effect.

### T1-1 · Asterion: take Rogue 2–3 at character 8–9, Monk 7–9 at 10–12 — **Rec: yes**
- Raised by six reviewers (bX5paFDOGDU 36:25, IC1WiOi_nYQ 12:32, 6i-Rpr9ziqs 59:08, uY-RJbv0DhY 17:07, Ni8rrKcrMqs 15:03, bCW4Hrr7Hmw 16:44). Every video with this chassis goes Monk 6 → Rogue tail → Monk 7–9.
- Ours: `asterion.md` `build_order` Rogue 1 → Monk 1–9 → Rogue 2 → Thief 3. Fast Hands arrives at the last level. No reason for that order is recorded anywhere.
- Delta: same final split, no respec. Fast Hands (a permanent second Flurry) moves from char 12 to char 9, so two more Tavern Brawler punches a turn (≈ +38 to +54 with the Stone) for the Resonance Stone stretch and all of early Act 3. Cost: Alert slips char 9 → 11, Evasion 8 → 10, Ki Resonation and the d8 die 10 → 12, Ki pool 6 at char 9. DEX 20 already gives +5 initiative before Alert, so the delay costs less here than in the videos' STR arrays.
- Files: `asterion.md` `build_order`, `leveling` chars 8–12, `feats[Alert].at`, `illithid` note (Black Hole carrier timing); `party.md` power-spike line.

### T1-2 · Bonbon: The Dead Shot in Act 3, Titanstring until then — **Rec: yes**
- Raised by four reviewers (-gnyG9gH-no 29:01, s2TJ7kOaJmA 27:27, 5UFoWD3Uwis 28:28, G_ShgMOS7zg 46:53, 54:08). "We care more about just hitting all of our shots because we have so many broken effects tied to hitting."
- Ours: Titanstring "all game" (`act3-ranged-bonbon`, `prog-ranged`, `act3-elixir-bonbon`; changelog 2026-09-10 §3). That decision compared Titanstring only against hand crossbows; The Dead Shot was never weighed.
- Delta: The Dead Shot is +2 and Keen Attack doubles proficiency on its ranged attacks, so at char 9+ it is +5 to hit over Titanstring, which cancels Sharpshooter's −5 outright, and it crits on 19. Damage per hit drops ~7 (Cloud Giant rider lost). Against AC 18 that is 75% × 27.5 = 20.6 expected per shot vs 50% × 34.5 = 17.3; on a Hasted 8-projectile turn, 6 hits instead of 4, each an Acuity and Band trigger. Titanstring only wins above ~76% base hit chance. Act 3 only: Fytz the Firecracker, Stormshore Armoury. Frees her elixir slot (see T2-2) and ends the second daily Giant Strength drinker.
- Verified: Keen Attack "doubles their Proficiency Bonus when rolling ranged attacks with this weapon, unless they have Disadvantage" (bg3.wiki/wiki/Keen_Attack). Switches off under disadvantage, so not into Charles's Darkness.
- Conflicts: one copy exists. T3-A2 (Asterion) and T3-C3 (Charles) also want it; this use beats both. Changelog 2026-09-10 §3 and D17's Act 3 half need rewording.
- Files: `bonbon.md` act3 ranged, elixir, `prog-ranged`, `prog-consumables`, `at_a_glance.elixir`, `playstyle`; `loot.md` Stormshore row; `party.md` gear line; changelog.

### T1-3 · Charles: character 12 as Warlock 6 (Accursed Spectre) instead of Paladin 7 — **Rec: your call, slight lean yes**
- Raised by two reviewers (0CbK5ufVk-g 37:45, 50:13; 9qa8wa1WEVg 31:32; MuodaDzKp98 27:04 also ends on Warlock 6).
- Ours: `leveling` char 12 "The Paladin 7 trade": Relentless Avenger, which the file itself calls weak.
- Delta: the cost is one L2 Paladin slot (ESL 4 → 3 means 4/3 → 4/2 slots), i.e. one 3d8 smite ≈ +40 on a crit swing, plus Relentless Avenger and one seat-filler prepared spell. The gain is a 7th Warlock spell known and Accursed Spectre: when Charles or an ally within 18 m kills a creature under Hexblade's Curse, a reaction raises a 10-turn spectre (Mundane: 31 HP, AC 14, Devour Soul heals Charles, Pluck Soul pulls 5 m). The nova's Held target is the natural curse target and dies to the nova, so this is a free body most fights. Not on constructs, elementals, oozes, plants, undead. Only the last level changes; no respec.
- Verified: bg3.wiki Accursed Spectre (passive feature); slot count from bg3.wiki Spells (half-caster ESL rounds up; Warlock levels ignored).
- Pairs with T4-U1 (curse per damage roll) and T3-C4 (curse application text).

### T1-4 · Gale: drop the Fiend level, go Sorcerer 12 — **Rec: no**
- IC1WiOi_nYQ 19:40–37:00 and bGupbGD2Fw0 21:42 both run pure Sorcerer 12: third feat (Alert / War Caster / +2 CHA) and a twelfth spell (Globe of Invulnerability and Chain Lightning both fit).
- Ours: Fiend 1 at char 7 for Command; `party.md` names Command as Gale's non-concentration control lane; Extended Spell was picked for it.
- Why no: Command leaves Gale entirely. Bonbon only gets Command at Bard 10 and Charles's copy costs his Paladin slots, so the party's mass no-concentration disable disappears for Acts 1–2 and shrinks after. A third feat is the only thing the dip costs, and Vigilance already substitutes for Alert. Listed because two ranking videos build it this way.

### T1-5 · Gale: Hexblade instead of Fiend for the dip — **Rec: no**
- iVOxw7TWYa0 9:52–12:32. Hexblade's Curse is +4 per ray (+28 on a 7-ray cast, +56 across a Hasted double) and crits on 19; Shield from the Warlock list.
- Why no: Hexblade's expanded list is Shield / Wrathful Smite, not Command, so the control lane goes (same objection as T1-4), and the curse's bonus action collides with Quickened Scorching Ray every turn. The damage is real; the party role is the cost. Verified lists at bg3.wiki/wiki/Warlock.

### T1-6 · Gale: Sorcerer 9 / Fiend 3 — **Rec: no**
- bCW4Hrr7Hmw 29:11 calls Sorcerer 9 "another reasonable breakpoint". Fiend 3 gives two short-rest L2 pact slots with Scorching Ray on the Fiend list (two extra 3-ray casts per short rest) and Pact of the Tome Guidance (the party's missing second Guidance).
- Why no: costs Careful Spell (Fireball into the melee cluster), the L6 slot (7-ray Scorching Ray or Chain Lightning), one L5 slot, two Sorcerer spells known and 2 sorcery points. The video's own argument (L6 spells are weak) does not apply because our L6 use is an upcast. Whether pact slots feed Create Sorcery Points is unverified.

### T1-7 · Gale: take the Warlock level at character 2, not 7 — **Rec: no, unless Act 1 control is what you want**
- iVOxw7TWYa0 9:22. Command from early Act 1 (Extended Command at char 3), five levels earlier.
- Cost: Scorching Ray, Dual Wielder, Twinned Haste and Elemental Affinity each slip one level (Haste char 5 → 6), landing on the Grymforge and Crèche fights. Identical from char 8. `party.md` "Twinned Haste online at char 5" would change.

---

## Tier 2 — Noticeable behaviour changes

How a turn is played, loadout swaps, positioning, elixir choice. Medium work.

### Bonbon

#### T2-1 · Alert instead of War Caster at Bard 8 (char 9) — **Rec: yes**
- Raised by six reviewers (-gnyG9gH-no 22:46, bGupbGD2Fw0 58:07, G_ShgMOS7zg 50:33, s50sTy53DZw 1:03:10, JDPCUMrtdZs 25:34, Jk0KrLcfeCA 33:17). "Controllers need initiative so they can go before enemies and stop them from acting."
- Ours: War Caster for advantage on the Hold Monster concentration save. Her initiative is d4+4 (Acts 1–2), d4+3 in Act 3 under Helldusk Gloves, the slowest in the party by 3–8 (Charles d4+7, Gale d4+11, Asterion ~d4+10).
- Delta: Alert makes her d4+9 / d4+8 and Surprise-immune, so Hold Monster lands before the enemy's first turn and she is still Hasted on turn 1 behind Gale. What War Caster protected: a +6 CON save that Adamantine Splint crit immunity (Acts 1–2), Helldusk's −3 (Act 3), Ketheric's Shield and Charles's Aura of Protection already mostly prevent; on the hard hits, ~85% instead of ~98%. Charles made the same trade on 2026-09-10 §2.
- Files: `bonbon.md` `feats`, `leveling` char 9; `amulet-of-greater-health` note ("she already has War Caster's advantage") and the 2026-08-15 conflict-table sentence.

#### T2-2 · With The Dead Shot, drink Elixir of Vigilance in Act 3 — **Rec: yes if T1-2**
- 5UFoWD3Uwis 21:45, JDPCUMrtdZs 26:36. Once Titanstring's Strength rider is gone the Giant Strength elixir buys nothing; Vigilance is +5 initiative and Surprise immunity on a d4 roll. With T2-1 as well she is d4+13, which is more than needed; take T2-1 for Acts 1–2 and this for the elixir slot, or one of the two.
- Files: `bonbon.md` `at_a_glance.elixir`, `act3-elixir-bonbon`, `prog-consumables`; `loot.md` Cloud Giant row ("Bonbon + Asterion" → Asterion).

#### T2-3 · Sentinel Shield as the default off-hand from Moonrise — **Rec: no if T2-1**
- s50sTy53DZw 5:43, 23:21. The party rule: initiative items to the one character without Alert. +3 initiative for Ketheric's +1 DC and DEX-save advantage. Whether any non-AC shield passive applies from the inactive melee set is unverified (the file already flags this). Alert answers the same gap without the doubt. Keep as the recorded option.

#### T2-4 · Sharpshooter toggle rule for Titanstring — **Rec: yes**
- -gnyG9gH-no 13:55 gives "off below 30% displayed". With Titanstring's flat rider that threshold is too low: the −5 is worth taking only above ~65% base hit chance in Act 1 (displayed ≥ 40% with it on) and ~85% in Act 3 with Cloud Giant (displayed ≥ 60%); ~10 points lower under advantage. Moot in Act 3 if T1-2. One playstyle sentence.

#### T2-5 · Plant Growth as a known spell — **Rec: yes**
- Raised by four reviewers (nrTSroBA4eI 16:02, 5UFoWD3Uwis 17:04, JDPCUMrtdZs 15:40, G_ShgMOS7zg 50:02). Non-concentration, no save, quarter movement in 6 m; layers under Charles's Hunger of Hadar (his own tier note already says "layer over Plant Growth") and her Glyph. Fills the empty char 9 pick (T3-B3). Rule: cast between the pack and the back line, never on the melee cluster.

#### T2-6 · Summon the Air or Earth Myrmidon, never Water — **Rec: yes**
- KaS6zqeSkP8 37:30, 51:01, 59:19. Depends on T4-V1 (Wet grants fire resistance). Air Myrmidon: Electrified Flail forces DC 13 CON or 2 turns Stunned on every swing, Raging Vortex is a no-save 10-turn Silence; Earth Myrmidon is the tank that draws the hits that strip her Acuity. Water and Fire both work against Gale's fire.
- Files: `bonbon.md` Conjure Elemental `why`, char 11 Magical Secrets note.

#### T2-7 · Open the day with the L6 Myrmidon, then refund the slot with Spellcrux — **Rec: yes**
- KaS6zqeSkP8 17:13, 1:01:56. Summon lasts until long rest; Spellcrux's bonus action returns the L6 slot for the six-target Command in the fight that needs it. Cost: the second Command / Hold Monster the amulet currently buys. One playstyle sentence.

#### T2-8 · Snowburst Ring in the open Act 2 ring 2, Drakethroat set to Cold — **Rec: your call**
- Raised by five reviewers (s2TJ7kOaJmA 31:33, nrTSroBA4eI 30:04, 5UFoWD3Uwis 31:05, JDPCUMrtdZs 35:25, Jk0KrLcfeCA 1:14:12). Every Cold-damage hit drops a 4.5 m ice circle (2 turns; DEX save vs her spell DC or Prone). Four to eight circles a turn with no slot or concentration, and it works on the undead and constructs that ignore Hold and Command.
- Cost: ice under the melee cluster is difficult terrain for Charles and Asterion, and Prone ends Charles's Hold Person with no save, so his Prone-immune boot stops being a flex (T2-28 interacts). Gale's fire melts it. Last Light Inn, loose plank in the bedroom north of the bar (DC 10 Perception). Act 2 only; Caustic Band takes ring 2 in Act 3.
- Verified: bg3.wiki Snowburst_Ring. Whether Acuity raises the ice DC is unverified.

#### T2-9 · Bhaalist Armour as a bagged nova swap — **Rec: no**
- s2TJ7kOaJmA 28:30. Inside 3 m of a Held target every projectile crits and piercing is doubled: ≈ 600 vs ≈ 275 on a Hasted 8-projectile turn.
- Why no: AC 17 instead of Helldusk's 21 and 3 DR, every hit she takes strips Acuity and forces a save, the aura helps nobody else (Charles Psychic/Radiant, Asterion Bludgeoning, Gale Fire), she must stand in the melee cluster, and the Bhaal path is the price. Recorded so the number is visible; a one-boss-fight swap if you ever want it. Verified: Aura of Murder 3 m, Paralysed auto-crit within 3 m, in-3 m disadvantage cancels the Paralysed advantage.

#### T2-10 · Respec to DEX 8 once the Gloves of Dexterity are in hand — **Rec: no**
- -gnyG9gH-no 4:10, 5UFoWD3Uwis 3:40, JDPCUMrtdZs 6:16. Frees 9 points for CON 16 / WIS 14.
- Why no: locks the Gloves of Dexterity on all game, so Helldusk Gloves (2026-09-10 §5: +1 DC, +1 attack, 1d6 fire × 8) are lost and Act 3 DEX falls to 8. Breaks `build_order` "no respec".

#### T2-30 · Amulet of the Devout instead of Spellcrux in Act 3 — **Rec: your call, lean yes**
- Jk0KrLcfeCA 57:36. +2 spell save DC on every Hold Monster, Command, Confusion and Glyph, live from turn 1 and additive to the Acuity cap; the only +DC neck in the game (bg3.wiki/wiki/Amulet_of_the_Devout: the Channel Divinity charge is the only cleric-gated half). Against Spellcrux's one refunded level-6 slot per long rest (which T2-7 would spend on the Myrmidon refund).
- `loot.md` currently says "nobody — sell it" for a wrong reason (T4-V8); the curse constraint it records still stands (Jaheira with Khalid's Gift loots the offering chest cleanly).

### Charles

#### T2-11 · Cast Hold Person from an L3 pact slot to Hold two humanoids — **Rec: yes**
- 2p2QqzNsfec 34:36. Upcast adds a target per slot level; the pact slot returns on a short rest. Two Held bodies answer the recorded nova caveat (the Held target dies mid-turn and the rest lands on something un-Held). Cost: one Shield or Counterspell reaction that fight. Verified: bg3.wiki Hold_Person.
- Files: `charles.md` Hold Person entry, `nova.assumptions`, `nova.caveats`.

#### T2-12 · Elixir of Heroism instead of Bloodlust on days with nothing to Hold — **Rec: yes**
- 01A_BHMeLQU 34:53. +1d4 to every attack roll and saving throw until long rest, stacks with Bless (wiki: a distinct condition). Against a Held target it adds nothing and Bloodlust stays the nova elixir; on undead/construct/crit-immune days there is no nova to feed and +1d4 on every Risky Ring concentration save is worth more than a kill-gated Action. Skip Armour of Agathys those days (one temp-HP source). One sentence in `at_a_glance.elixir` and `playstyle`.

#### T2-13 · Great Weapon Master for its bonus-action attack, replacing Savage Attacker — **Rec: no**
- MuodaDzKp98 14:33, 9qa8wa1WEVg 15:59. The recorded rejection ("All In could never apply behind a shield") covers only half the feat: wiki confirms the Bonus Attack needs no two-hander and no All In. On a Held target every swing crits, so each nova turn buys a bonus-action auto-crit swing (~+110 on the 512 standard nova).
- Why no: Savage Attacker's reroll is ~+50 on the standard nova but +120–150 on the nine-swing ceiling, GWM does nothing on a turn with no crit or kill, and the bonus action already carries Inquisitor's Might and Hexblade's Curse. You confirmed Alert + Savage Attacker today. The GWM sentence in `feats` should still be corrected (T3-C7).

#### T2-14 · Warlock 3 Shadow Blade in Act 1 — **Rec: no**
- 9qa8wa1WEVg 13:24. 2d8 vs Phalar's d8+2 is +2.5 a swing, but Warlock 3 at char 3 pushes Inquisitor's Might, Smite, Alert and Extra Attack one level each for all of Act 1, and Phalar's Shriek leaves his hand. The respec at char 9 erases it anyway.

#### T2-15 · Great Old One patron at the Stone respec instead of re-picking Hexblade — **Rec: no**
- m2F7dNXEwNc 5:45. Mortal Reminder: every critical hit forces a Wisdom save on the target and nearby enemies or they are Frightened (bg3.wiki/wiki/Mortal_Reminder). After the respec every swing at a Held target crits, and the Stone already gives nearby enemies disadvantage on Wisdom saves. Act 1 is untouched (Hexblade 1–2 stays until char 9; Pact of the Blade covers the CHA binding).
- Why no: costs Hexblade's Curse (+36 standard / +72 ceiling by the current tables, far more if T4-U1 is true), the heal on kill, and the Shield spell (not on the base Warlock list). The Held target does not need frightening and the enemies near it are the ones Asterion is punching. Whether Mortal Reminder's DC takes Acuity is unverified.

### Gale

#### T2-16 · Boots of Arcane Bolstering in Acts 2–3 — **Rec: your call, lean yes**
- iVOxw7TWYa0 35:16. Dash grants Arcane Charge for 2 turns: +2 spell damage per independent damage instance against any Threatened enemy (wiki: the enemy must be Threatened, not the wearer, so any target Charles or Asterion stands next to). +10 on a 5-ray cast, +14 on 7, for the two turns after a pre-combat Dash, which are the turns that decide most fights. Araj Oblodra, Moonrise, 190 gp, no proficiency tag. Costs Evasive Shoes' +1 AC. Same slot as T3-G2 (Night Walkers): pick one for Act 3.

#### T2-17 · Cloud of Daggers for chars 3–4 via the unused replacement slots — **Rec: yes**
- iVOxw7TWYa0 14:34, 17:10; IC1WiOi_nYQ 25:01 gives the numbers (4d4 on cast and again at the start of the enemy turn, no roll). Ours leaves the Sorc 3 and Sorc 5 replacement slots unused.
- Path: Sorc 3 pick Scorching Ray, replace Chromatic Orb → Cloud of Daggers; Sorc 5 pick Haste, replace Cloud of Daggers → Counterspell (one level earlier than now). Keeps Scorching Ray at 3 (Spellsparkler charges). Cost: no Chromatic Orb for chars 3–5. The PARTY-1 variant (delay Scorching Ray to Sorc 6) is not recommended.

#### T2-18 · Cone of Cold instead of Telekinesis at Sorcerer 10 (char 11) — **Rec: yes**
- iVOxw7TWYa0 23:52. Our own file says Gale "contributes almost nothing to the fire-immune fights until Chain Lightning at char 12" and calls Telekinesis bugged, concentration and niche. Cone of Cold is a non-concentration 8d8 cone that works while he holds Haste; the Mage Hand water bottle already supplies Wet for double damage.

#### T2-19 · Ice Storm instead of Dimension Door at Sorcerer 8 (char 9) — **Rec: yes**
- iVOxw7TWYa0 22:20. Ice Storm is already in `spells.recommended` as the A-tier non-concentration AoE and is never scheduled; Dimension Door is C tier in the channel's own list. Misty Step scrolls and Fly at char 12 cover traversal. Add the T3-G5 melt caveat. The darkness-party video offers Banishment for the same slot (a Charisma-save answer for the un-Holdable boss), but it is Concentration and drops Twinned Haste, so Ice Storm takes the pick; Banishment stays a scroll.

#### T2-20 · Alert instead of Elemental Adept: Fire at Sorcerer 8 — **Rec: no**
- IC1WiOi_nYQ 30:13. The video's Arsonist's Oil argument weakens ours ("she strips fire resistance one target at a time" — a ranged Flourish hits two targets per attack and the oil lasts ten turns), but Alert on Gale duplicates the Vigilance elixir's +5, so the gain is retiring a 25 gp daily consumable. Elemental Adept's no-1s on fire dice is ~+1.2 per ray every cast. Modest either way; keep as is. Reword the Elemental Adept note (T3-G6).

#### T2-21 · Arsonist's Oil fire-vulnerability setup — **Rec: your call**
- iVOxw7TWYa0 40:25. Make the target fire-resistant (thrown Elixir of Fire Resistance), hit it with an Arsonist's-Oil weapon, then overwrite the resistance with another thrown elixir: the target ends Vulnerable to fire, doubling every ray (~175 → ~350 on a 7-ray cast). Wiki-confirmed (bg3.wiki/wiki/Arsonist's_Oil). Two elixirs and a Bonbon bonus action per target; an exploit, and this is a non-Honour run.

#### T2-22 · Pyroquickness Hat as a boss-turn head swap — **Rec: your call, lean yes**
- IC1WiOi_nYQ 37:30. Action Scorching Ray grants an extra bonus action: 7+5+5 rays instead of 7+5 (~+100 for 6 sorcery points) on a turn that does not need Acuity for Command. Wet (a thrown water bottle) or Helldusk Armour negates the self-Burning that would otherwise force a Haste save each turn. Sorcerous Vault, 160 gp. Bag item, not a slot change. Verified: bg3.wiki Pyroquickness_Hat.

#### T2-23 · Bait enemy reactions before Scorching Ray — **Rec: yes (one sentence)**
- zIiqb32iN9w 22:43. A reaction (Hellish Rebuke, opportunity attack) interrupting the first projectile of Magic Missile or Scorching Ray drops the remaining projectiles, shown on a combat log. Unverified in the KB. Charles is the natural baiter: step out of melee to draw the opportunity attack before Gale casts. Cheap to write, cheap to be wrong about.

### Party

#### T2-24 · Plant Growth (Armour of Landfall) under Hunger of Hadar, no fire in the zone — **Rec: yes**
- 4KkXqqeKz80 28:02. Gale's Armour of Landfall grants Plant Growth once per short rest; under Charles's Hunger of Hadar (blinded so they cannot jump, quarter speed) it is a multi-turn no-save lock with Repelling Blast pushing escapers back. Nothing in our text connects the two. Standing rule: no Fireball, Scorching Ray or Heat into the zone, because fire burns Plant Growth away (bg3.wiki/wiki/Plant_Growth). Gale's fire goes at targets outside; Charles and Bonbon work the inside.

#### T2-25 · Phalar Aluve: Sing in fights about surviving, Shriek in fights about damage — **Rec: yes**
- 6i-Rpr9ziqs 36:19. Sing gives the wielder and allies within 6 m +1d4 to attack rolls and ALL saving throws for 5 turns (wiki: the "mental" tooltip is wrong); Shriek is −1d4 to enemy saves and +1d4 Thunder per damage instance. Same Action, one mode per activation. Sing is +1d4 on Charles's Risky Ring concentration saves. Per-fight call; one line in `bonbon.md` `phalar-aluve-bonbon` and `party.md`. Whether Sing stacks with Bless is unverified (distinct stack ID).

### Asterion

#### T2-26 · Racial +2 and Hag's Hair on WIS instead of DEX — **Rec: your call, lean yes**
- bX5paFDOGDU 32:45. DEX 16 (18 under the Cloth) / WIS 17 → 18 → 20. AC identical in every act (the modifiers sum the same). Gains +1 Psychic per hit from Manifestation of Mind from char 7 (doubled by the Stone) and +1 more per hit from the Kushigo boots in Act 3 (≈ +12–16 a turn), +1 WIS saves on the Stone carrier. Costs −1 initiative, −1 DEX saves, −1 Sleight of Hand / Stealth. Creation-time change, not a respec. Interacts with T1-1 (Alert later, so the −1 initiative bites a little more).

#### T2-27 · Record the Ascension decision and its number — **Rec: decide; record either way**
- Raised by four reviewers (bX5paFDOGDU 4:10, SZYnp9AppYk 3:38, uY-RJbv0DhY 3:09, Ni8rrKcrMqs 2:36). Vampire Ascendant adds 1d10 Necrotic to every weapon and unarmed attack (bg3.wiki/wiki/Vampire_Ascendant): ≈ +27 to +44 a turn in Act 3, the size of the Gloves of Soul Catching rider. Also Ascendant Bite (6d6 heal, 6d6 Necrotic, grants Happy). Not doubled by the Stone. `asterion.md` never mentions it; `loot.md` marks the event MAJOR with no number. Story choice; the file should state the price of refusing it.

#### T2-28 · Boots of Stormy Clamour on Asterion in fights where Charles wears Striding or Helldusk — **Rec: yes (per-fight option text)**
- 4naQFyHry2M 24:26. Asterion inflicts more conditions per turn than anyone (Stun, Topple Prone, Bleeding from Flawed Helldusk, Ability Drain), each adding 2 turns of Reverberation, so the next Stunning Strike CON save is at −2 to −4. Cost that fight: Night Walkers' Misty Step (Acts 1–2) or Kushigo's +WIS per hit (Act 3, ≈ +20). Depends on 2026-09-11 §3 (boots are Charles's flex).

#### T2-29 · Luminous Gloves as a boss-fight bag swap (Manifestation of Soul + Radiating Orb) — **Rec: no**
- bX5paFDOGDU 32:13. 6–8 Radiant hits a turn stack Orb on one boss. Costs Soul Catching's 1d10 per hit and the Stone doubling on Manifestation of Mind. The narrator himself calls it "not a primary strategy for monks". Luminous Gloves' armour tag is unconfirmed.

---

## Tier 3 — No-question improvements

Missed items, free upgrades, stale sentences. Low risk. Suggest accepting as a batch and naming any exceptions.

### Bonbon
- **T3-B1 Minor Illusion at char 2, Vicious Mockery deferred** — five videos open with Minor Illusion + Friends. Ours takes the S-tier grouping cantrip at char 11 and a C-tier damage cantrip at char 2 while she has a bow.
- **T3-B2 Bard 1 fourth spell: Heroism (or Disguise Self) instead of Faerie Fire** — Faerie Fire is C tier in our own table and dropped at char 5; Heroism fills her empty concentration lane before Hold Person and covers Frightened.
- **T3-B3 char 9 spell pick re-learns Hold Person** — already known from char 4, so one spell known is unassigned. Fill with Plant Growth (T2-5). Found by two reviewers.
- **T3-B4 Stock Arrows of Many Targets** — one attack roll on up to four targets, riders not halved (bg3.wiki/wiki/Arrow_of_Many_Targets); two arrows cap Acuity unhasted on turn 1. Rated S+ in `ratings.md`, in no Bonbon row. Two reviewers.
- **T3-B5 Keep Longstrider; drop Dissonant Whispers at char 6** — she is the party's only Longstrider; the current swap makes +3 m party movement a scroll dependency. Two reviewers.
- **T3-B6 Keep Tasha's Hideous Laughter into Act 3 for the Band** — bonus-action WIS save at her Acuity DC; our own tier note calls it a boss-immunity bypass. Spend the char 10 swap elsewhere or skip Dominate Person (D tier).
- **T3-B7 Ring of Feywild Sparks over Caustic Band in Act 3 ring 2** — hidden +1 spell save DC (bg3.wiki/wiki/Ring_of_Feywild_Sparks; `ratings.md` already rates it S), Auntie Ethel at the Blushing Mermaid. +1 DC on Hold Monster vs 8–12 Acid a turn. Your call between the two; the reviewer leans ring.
- **T3-B8 Flourish costs the Inspiration only on hit** — wiki lists "Cost on hit", so a Sharpshooter miss refunds the die. Flourish on every attack; the Boots of Brilliance "Inspiration-starved" rationale is weaker than written.
- **T3-B9 Race line: Wood Half-Elf** — "(early shield)" is stale, Fighter 1 grants shields; Wood Half-Elf adds +1.5 m movement and Stealth.
- **T3-B10 Warped Headband of Intellect as the dialogue swap** — INT 17 for Arcana/History/Investigation/Religion checks; nobody wants it in combat. Same pattern as the Birthright swap.
- **T3-B12 Silence over Charles's Hunger of Hadar on non-Holdable fights** — her Hold lane is idle in exactly those fights, so her Concentration is free; Misty Step and Dimension Door are verbal and stop working inside it. One sentence.
- **T3-B13 Fire the Arrow of Darkness as the last attack of her turn** — she has no blind immunity, so anything under the cloud is untargetable for the rest of her turn; Flourishes first, arrow last, aimed at the ground so the cloud edge sits between Charles and the target.
- **T3-B14 Boots of Striding as her Act 3 per-fight alternative** — free once Charles moves to Helldusk Boots; Striding covers Prone and forced movement while concentrating, Persistence covers Paralysed and Restrained. Fighter 1 supplies the proficiency.
- **T3-B11 Knife of the Undermountain King wording** — wiki confirms Organ Rearranger applies to ranged and spell attacks, so "harmless filler" is wrong while she holds it; the inactive-set question stays open.

### Charles
- **T3-C1 Divine Sense against undead and fiends** — bonus action, short-rest recharge, two turns of advantage. Listed as a gain at char 3 and never mentioned again; exactly the fights where Hold Person and Command fail.
- **T3-C2 Aura of Protection must be cast once** — wiki: not on by default, removed on respec (so char 8 and again char 11), 3 m radius. A forgotten toggle is −4/−5 on every party save.
- **T3-C3 The Dead Shot as the non-Bhaal ranged stat stick** — holder-scoped Improved Critical; only if T1-2 is declined (one copy).
- **T3-C4 Hexblade's Curse application text** — once per short rest, 20% free proc on a hexed-weapon hit, heals Warlock level + CHA on the kill. None of this is in the file.
- **T3-C5 Shadow Blade has its own advantage against obscured targets** — bg3.wiki Shadow_Blade passive: advantage vs Lightly or Heavily Obscured targets. A second advantage route that needs no arrow, and the fallback if T4-V2 lands.
- **T3-C6 Radiant Shockwave never orbs allies** — wiki: all non-allied creatures, neutrals included. Asterion can stand on the Held target; watch neutral NPCs.
- **T3-C7 Correct the GWM sentence** — "All In could never apply" is true; "never taken" should say the bonus attack was weighed and lost to Savage Attacker (T2-13).
- **T3-C8 A Most Bloody Inheritance** — Bhaal's-chosen party buff at High Hall (crit threshold −2, stacking, plus Stunning Gaze) if Charles defeated Orin. The one Bhaal-path payoff for the other three; one line in the Bhaal-path notes.
- **T3-C9 tadpole.md Charles DC line** — names Helldusk Gloves (now Bonbon's) and ignores Battlemage's Power Acuity; his illithid DC is 17 → 27, same ceiling as the others.

### Gale
- **T3-G1 Pre-cast Twinned Haste before initiative** — Hastened lasts 10 turns; casting just before engaging frees Gale's turn 1 Action for a second Scorching Ray. Ambushes keep the current line.
- **T3-G2 Disintegrating Night Walkers to Gale in Act 3** — free once Asterion moves to Kushigo boots. Correction after applying: the wiki gives them a short-rest Misty Step, immunity to Web / Entangle / Ensnare and no slipping on grease or ice, NOT Prone immunity as the reviewer wrote. Still taken: the ice-footing matters once Snowburst and Ice Storm are in the plan, and the Misty Step is concentration insurance of a different kind. Against Evasive Shoes' +1 AC. Same slot as T2-16.
- **T3-G3 Record Markoheshkir's free spells** — Flame of Wrath: Fireball and Wall of Fire once each per short rest; Bolts of Doom: Chain Lightning and Lightning Bolt. The fire-immune playstyle line reads as if Chain Lightning costs the L6 slot.
- **T3-G4 Heat Convergence into Fireball, never Scorching Ray** — wiki: multi-hit spells consume Heat on the first hit only; area spells add it to every target. Use the free Flame of Wrath Fireball.
- **T3-G5 Ice Storm note: his own fire melts the ice** — fire first, Ice Storm last; Ray of Frost re-freezes.
- **T3-G7 Keep Magic Missile at Sorc 6** — two videos call it a party requirement (no roll, no save) and nobody else has one; with T2-17's path the Sorc 6 replacement slot is free, so Magic Missile survives without a further swap.
- **T3-G8 Spend the idle pact slot as a sorcery point** — the darkness video converts Warlock slots to sorcery points; if so the level-1 pact slot is +1 SP per short rest whenever Command is not needed. Unverified in the KB; the first attempt settles it.
- **T3-G6 Reword the Elemental Adept note** — "one target at a time" is wrong (two per Flourish, ten-turn coating); the feat's case is the no-1s and no set-up, not Bonbon's coverage.

### Asterion
- **T3-A1 Sneak Attack wording** — "needs a finesse weapon" is wrong; Sneak Attack (Ranged) fires off any ranged weapon attack, so his hand-crossbow fallback carries 2d6. Set the reaction to Ask.
- **T3-A2 The Dead Shot swapped in after Celestial Haste** — only if T1-2 is declined (one copy). Improved Critical is holder-scoped (wiki), so it lowers his punch crit threshold from the ranged slot.
- **T3-A3 Bite something every day for Happy** — +1 to all attack rolls, saves and most checks (bg3.wiki/wiki/Happy_(Condition)); the file calls the Bite "minor". Not from Gale, corpses, or pre-upgrade Karlach. Duration unverified.
- **T3-A4 Athletics instead of Insight at Rogue 1** — +9 to +12 on the elixir, the party's best Shove number; Insight is covered by Gale and Bonbon. `proficiencies.md` too.
- **T3-A5 Topple, not Stagger, on a concentrating caster** — Prone ends concentration with no save (our own changelog says so); Stagger only for a caster with a dangerous reaction.
- **T3-A6 Potion of Speed on nova turns in Acts 1–2** — a potion, not an elixir, so it stacks with Giant Strength; rated S+ in `ratings.md`. Costs a Flurry before Thief 3.
- **T3-A7 Dual-wield toggle off** — otherwise a crossbow shot auto-spends a Flurry on an off-hand shot.
- **T3-A8 Hide outside vision cones without a roll; release Shift** — Shift+Hide hides the whole party and drags Charles's Stealth into a check.
- **T3-A9 The no-elixir fallback sentence** — punch on DEX (+4/+4 instead of +10/+10); Stun DC unchanged in Acts 1–2; do not pick up a weapon (Tavern Brawler always adds the STR modifier, wiki).
- **T3-A10 The out-ranging rule** — end the turn 50 ft from melee enemies; Dash 90+ ft to stay outside ranged range. The answer to a failed Stun is to leave, not stand.
- **T3-A12 Eversight Ring wording** — "see through magical darkness" is sourced, but no one can make ranged attacks into or out of a Darkness cloud regardless of sight (bg3.wiki/wiki/Darkness_(cloud)); tighten so it reads "fights unblinded inside the cloud", not "shoots into it".
- **T3-A11 Stillness of Mind auto-casts and costs the Action** — wiki: no toggle, no reaction prompt. Nothing in this party grants fear immunity; keep him inside Charles's aura when fear is expected.

### Party
- **T3-P1 State the stealth opener** — start fights from Stealth so enemies are Surprised: a free skipped enemy turn and a Hold window before anything moves. `party.md` has no opener rule.

---

## Tier 4 — Mechanics corrections

Our text states a rule the corpus contradicts. **Verified** ones are wiki-confirmed and should be fixed regardless of the tiers above. **Unverified** ones need one in-game check before anything is built on them.

### Verified — fix the text
- **T4-V1 Wet grants fire resistance; the Water Myrmidon no longer applies it.** `bonbon.md` says the Water Myrmidon's Wet is "the party's only reliable way to strip enemy fire resistance ahead of Gale." Wet: Resistant to Fire, Vulnerable to Lightning and Cold; Healing Vapours stopped applying Wet in Patch 8. Applying it before Scorching Ray halves Gale's damage. Found by three reviewers. Delete both sentences, scope the Mage Hand water-bottle note to Ray of Frost / Cone of Cold / Chain Lightning. (bg3.wiki/wiki/Wet_(Condition), Healing_Vapours)
- **T4-V2 Darkness advantage only against enemies without darkvision.** `charles.md` "advantage in, disadvantage out", `weapon_plan` "Darkness Arrows for advantage", Devil's Sight and Shadow Blade notes, `loot.md` Phalar note. Wiki Darkvision mechanics: Attacking from Shadows needs the target to lack darkvision (or be beyond its range). Goblins, gnolls, duergar, drow and Shadow-Cursed creatures all see him. The cloud's real value is the ranged block, Blinded enemies inside it, and advantage vs the darkvision-less minority; from Act 2 the Risky Ring supplies advantage anyway. Act 1 accuracy plan should not lean on it. (5yTLH3BWrW0 8:52)
- **T4-V3 Counterspell against a higher-level spell rolls INT.** Live wiki bug; both carriers have INT 8. Charles's L3 pact-slot Counterspell is a 20–30% roll against 4th+ level spells; Gale must upcast from a Sorcerer slot to remove the check. Raises the value of Psionic Dominance. (5yTLH3BWrW0 26:32)
- **T4-V4 Command casts from Sorcerer slots.** Wiki Resources: any slot of the right level casts any known spell regardless of source. Delete `gale.md` `traps[6]` and its Bonbon fallback clause.
- **T4-V5 Paralysed auto-crits apply to any attack within 3 m, not only melee.** `gale.md` and `party.md` say "from melee". Gale within 3 m of a Held target fires 5–7 crits with advantage (~+55 to +80 per cast). Caveat to check in play: whether ranged spell attacks inside an enemy's reach take Threatened disadvantage (advantage from Paralysed would cancel it). (iVOxw7TWYa0 21:18)
- **T4-V6 The Mirror of Loss +2 is not guaranteed.** One DC 25 Religion check per character (fail = locked out forever), then a 60% roll per attempt. Religion is INT-based; only Charles is proficient, at INT 8. All four builds' end stats assume it. Plan: Enhance Ability (Bonbon), Guidance, and a quicksave before each prayer. (s50sTy53DZw 3:08; bg3.wiki/wiki/Mirror_of_Loss)
- **T4-V8 loot.md's reason for skipping the Amulet of the Devout is wrong.** It says the amulet "only works with Channel Divinity"; only the extra charge does. The +2 spell save DC applies to anyone (bg3.wiki/wiki/Amulet_of_the_Devout). The skip may still be right (T2-30); the sentence is not. Also in the 2026-08-15 conflicts table.
- **T4-V7 Sneak Attack works on ranged attacks** (T3-A1), **Knife crit passive covers ranged and spell attacks** (T3-B11), **Aura of Protection must be cast** (T3-C2), **Radiant Shockwave spares allies** (T3-C6), **Stillness of Mind costs the Action** (T3-A11), **Booming Blade once per Action and final upgrade at 11**, **Arcane Acuity caps at 10**, **Bloodlust's action carries Extra Attack outside Honour**, **Mirror of Loss is per character**, **no ranged attacks into or out of a Darkness cloud even with Devil's Sight** (m2F7dNXEwNc plays Eldritch Blast from inside clouds; bg3.wiki/wiki/Darkness_(cloud) says no, so Charles's dead-ranged-slot reasoning stands) — the last five contradicted the videos and the wiki backed our text; no change.

### Unverified — one in-game check each
- **T4-U1 Hexblade's Curse per damage roll.** Two videos' combat logs show +proficiency on every damage instance (weapon, Booming Blade, smite, riders), not once per swing. A Charles nova swing carries four or five instances, so the ceiling's "72" would be ~200 and the standard nova gains ~+70 whenever the curse is up, which makes cursing the nova target on the set-up turn a standing rule. Wiki wording ("damage rolls") is consistent but not explicit. Check: one cursed target, one smite, read the log. (0CbK5ufVk-g 46:37, zIiqb32iN9w 19:37)
- **T4-U2 Spellmight Gloves per ray.** iVOxw7TWYa0 30:37 asserts +1d8 on every ray from a build that has played it; wiki silent. Moves our "untested" flag to "probably, confirm".
- **T4-U3 Inactive melee-set passives.** Four videos assert the Knife's crit reduction fires while the bow is out (nrTSroBA4eI 26:56, G_ShgMOS7zg 54:39, 5UFoWD3Uwis 29:32, JDPCUMrtdZs 34:23); wiki confirms only the shield AC carry-over. Decides Ketheric's +1 DC, Sentinel's +3 initiative and the Knife. Check the character sheet with the bow drawn.
- **T4-U4 Reaction-interrupted multi-projectile spells** (T2-23).
- **T4-U5 Helldusk Helmet as crit-immune gear — resolved, our text stands.** `charles.md` `nova.caveats` lists it beside the Adamantine armours, Grymskull and Balduran as cancelling Hold Person's guaranteed crits. The reviewer's wiki summary showed no such line, but the full page reads "Attackers can't land Critical Hits on the wearer" (bg3.wiki/wiki/Helldusk_Helmet). It stays on the pre-nova check list.

---

## Tier 5 — Considered, not recommended

Listed so you can see they were looked at. Each was weighed against the recorded reasoning; none adds an argument that overturns it.

**Class and level**
- Charles Paladin 5 / Warlock 7 (both ranking videos) — compared in ceph-video-comparison §3.1; Paladin 7 buys Aura of Protection and the smite slots the nova runs on. Paladin 2 / Warlock 10 and Paladin 9 / Warlock 3 (breakpoints video) — the first is the Honour design already compared, the second loses Deepened Pact's third attack.
- Charles Great Old One patron (pre-Patch 8 videos) — no Bind Hexed Weapon at STR 8, no Shadow Blade, and Frightened adds nothing on a Held target. Crown (Divine Allegiance) and Ancients (Aura of Warding) — both lose Inquisitor's Might, the only non-concentration per-hit Radiant that keeps Luminous Armour firing; §8.1 stands. Devotion for Sanctuary — ends when Gale casts. Mono-Paladin 11 — costs Bind Hexed Weapon, Shadow Blade, Extra Attack from Deepened Pact.
- Charles Charisma ASI instead of Savage Attacker — decided today; +1 to hit is worth nothing on a Held target and the DC is Acuity-capped.
- Asterion Monk 8 / Thief 4 for a third feat (four videos) — already in `traps`; the third feat's best use (+2 WIS) loses to Ki Resonation and the d8 die. Swashbuckler tail — Flick o' the Wrist needs a main-hand finesse weapon and CHA; Sand Toss spends the Flurry bonus action. Light Cleric 6 / Open Hand 6 — costs Fast Hands, Ki Resonation, Alert and Evasion for engines the party already runs elsewhere.
- Bonbon Fighter 2 / Bard 10 for Action Surge (four videos) — the argument is Honour-only; outside Honour the Hasted action carries Extra Attack, so Gale gives her the second Action every turn. Bard-first — loses Heavy Armour (Splint, Grymskull), CON save proficiency and Archery through Act 1. Arcane Archer Fighter 7 / Bard 5, Swords 6 / Gloom 3 / Assassin 3, Spore Druid 2, Thief 3, Bladesinging 2 — each caps her at 3rd-level slots or costs Bard 10–11 (Hold Monster, Magical Secrets Command and Conjure Elemental, the six-target Command).
- Gale Wizard 1 dip (three videos, one for scroll-scribing) — INT 8 prepares one Wizard spell and it costs Command or Sorcerer 11. Sorcerer 10 / Fiend 2 for Devil's Sight — costs the L6 slot and the payoff (shooting out of a cloud) is denied by the wiki. Storm Sorcerer 4 / Warlock 8 control Sorlock — a different character. CON 16 / DEX 14 on Gale — +1 concentration save against −1 AC and −1 initiative; the chest already gives advantage.
- Charles self-cast Darkness instead of farmed arrows — evicts Hold Person; Bonbon's 18 m bow places the cloud. Lockadin initiative gear (Gloves of Dexterity, Soulbreaker, Yuan-ti) — Alert alone beats all three and each displaces a locked slot. Sorcerer concentrating on Wall of Fire instead of Haste — Charles's and Bonbon's turns both run on the Haste action.

**Items already adjudicated**
- Charles: Helmet of Arcane Acuity + Band, Ketheric's Shield, Rhapsody off-hand, Potent Robe, Coruscation / Callous Glow, Hellrider's Pride, Risky-Ring-class crit gear against a Held target, Shar's Spear of Evening (Last Light falls), Clown Hammer, Snowburst ice combo, Cloud of Daggers / self-cast Darkness / Hex (all concentration), DEX 16 / CON 14 spread, Bone Chill over Mage Hand, the re-bind curse exploit.
- Bonbon: Gloves of Dexterity respec at creation (D1), Bloodlust or Battlemage elixir (the slot is her Strength), hand-crossbow pair (§3), Martial Exertion Gloves, Strange Conduit Ring, Callous Glow + Luminous Gloves, Rhapsody stat stick, Marksmanship Hat (Act 2 only, same stop as the Helmet), Misty Step item (D4), Two-Weapon Fighting style, Cloud of Daggers at Bard 3, Counterspell as a Magical Secret, Graceful Cloth to DEX 20, Bhaalist as the standing chest.
- Gale: Alert + shield instead of Dual Wielder (Rhapsody out-values Ketheric's), Heightened over Careful, Globe of Invulnerability learned (concentration), Wall of Fire at Sorc 7 (Flame of Wrath gives it free), Risky Ring, Amulet of Greater Health (Landfall already gives CON advantage; Charles needs it), Robe of the Weave, self-Haste, Spellcrux swap, The Dead Shot over Hellrider (initiative decides), Gold ancestry.
- Asterion: Gloves of Dexterity trick (D1), Callous Glow with self-cast Light (lights him inside Charles's Darkness), Cloak of Protection (Charles's claim), Helmet of Grit (armour tag), Amulet of Greater Health with CON 8, Manifestation of Soul route, Devotee's Mace / Duellist's Prerogative / Sharpshooter (all need a held weapon), Athletics Expertise (Push is a save, not a contest), baiting the Vest counter (Gale is the easier target).
- Party: flat +1 DC pieces (Hood of the Weave, Robe of the Weave) lose to items that protect the concentration the DC is cast through; the Devout's +2 is the one worth a decision (T2-30). The companions video's Astarion as an Assassin archer with STR 12 — ours is the "specific build" that video exempts.
- Party: one Strength-elixir drinker (D17 accepts two; T1-2 removes the second in Act 3 anyway), three save-DC item carriers (adjudicated), Guidance / Resistance / Create Water utility (no Cleric level to spare; Wet is now known to be wrong for Gale), the surface-combo package (spell picks nobody has), Life of the Party AC exploit, the video's "Mirror of Loss cannot be used on both" claim (wiki: per character).

---

## Where the videos agree with us

About 200 agreement lines across the thirteen findings files. The ones that confirm recorded decisions under review: Titanstring over hand crossbows on a Flourish build (three archer videos, including the hand-crossbow original); Fighter 1 first for Bonbon; Thief 3 for the second bonus action; Alert on every non-DEX character (Bonbon is the gap, T2-1); Tavern Brawler on a daily Giant Strength elixir with STR 8; Hexblade first, Pact of the Blade, Shadow Blade bound daily and one-handed behind a shield; Vengeance for Inquisitor's Might; Draconic Red with Twinned + Quickened + Extended; Fiend 1 for Command as the endorsed Sorcerer dip; every engine item's home (Luminous Armour on Charles, Belligerent Skies / Callous Glow / Coruscation on Gale, Acuity helmet + Band on Bonbon, Stormy Clamour on the condition-inflicter); a shield in the inactive melee set gives its AC while shooting; Hellrider Longbow as an initiative stick; Deepened Pact stacking with Extra Attack outside Honour.

---

## If accepted — follow-through

- Every accepted item edits the named character file plus `party.md` and `loot.md` where an owner or route changes; T1-2 also rewrites changelog 2026-09-10 §3 and D17's Act 3 clause.
- T4 verified corrections are text fixes and can go in regardless of the y/n on the tiers above.
- Re-run `tools/apply_item_tiers.py` and `tools/apply_spell_tiers.py` after any itemization or spell edit; `tools/check_itemization.py` for slot coverage.
- Bump `content/meta.md` (minor: this is a content sweep) and add a dated changelog entry naming what was taken and what was declined, with the T5 list folded into the deviation register where a video rates the item.
- Open in-game checks to schedule: T4-U1 (curse per roll), T4-U2 (Spellmight per ray), T4-U3 (inactive-set passives), T4-V5 caveat (Threatened on ranged spell attacks inside 3 m).
