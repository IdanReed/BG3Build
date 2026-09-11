# Bonbon build notes (2026-09-11)

Reasoning cut from `content/characters/bonbon.md` in the cheat-sheet restyle, plus the report's reasoning (`docs/cephalopocalypse-build-review-2026-09-11.md`) for each decision applied. Anchors are the entry `id` or field name. Tier notes stay in the content file.

## Creation

**class / build_order / notes (Fighter 1, not Fighter 2)** — Fighter 2 (Action Surge) is the multiclass guides' near-universal package and the videos' own party runs Swords Bard 6 / Fighter 2. It costs Bard 11 and the L6 slot (six-target Command, Otto's). Outside Honour the Hasted action carries Extra Attack, so Gale gives her the second Action every turn; the Action Surge argument is Honour-only (report Tier 5). Bard-first loses Heavy Armour (Splint, Grymskull), CON save proficiency and Archery through Act 1. Arcane Archer 7 / Bard 5, Swords 6 / Gloom 3 / Assassin 3, Spore Druid 2, Thief 3, Bladesinging 2 each cap her at 3rd-level slots or cost Bard 10–11. A Wizard dip would have added only the Shield reaction and scroll scribing.

**race (T3-B9)** — "Half-Elf or Human (early shield)" was stale: Fighter 1 grants shields. Wood Half-Elf adds +1.5 m movement and Stealth proficiency. Half-Elf grants no free skill in BG3, so the Bard 1 pick must be Deception; on Human, Deception could sit on the racial skill and the Bard pick go to Performance.

**starting_stats / stats_note / ability_scores / build_order (T2-10 respec)** — Three videos (-gnyG9gH-no 4:10, 5UFoWD3Uwis 3:40, JDPCUMrtdZs 6:16) respec DEX to 8 once the Gloves of Dexterity are on, freeing 9 points. The report recommended no (it locks the gloves on all game and costs Helldusk Gloves: +1 DC, +1 attack, 1d6 Fire × 8 in Act 3); accepted anyway, with the Gloves of Dexterity kept all game. Creation array 8/15/14/8/10/15 (+2 CHA, +1 DEX) gives DEX 16 for all of Act 1 until the Crèche; a DEX 8 creation would spend early Act 1 at DEX 8, which the Act 1 item guide itself warns against. Respec array 10/8/15/8/14/15 = 27 points (STR 10 costs 2, CON 15 and CHA 15 cost 9 each, WIS 14 costs 7); +2 CHA → 17, +1 CON → 16. Gains: CON 16 (+1 on the Hold Monster concentration save, +12 HP), WIS 14 (+2 WIS saves, Perception, Insight), STR 10 (no −1 Athletics). Losses: Helldusk Gloves; Armour of Agility becomes AC 21 at DEX 18 (was 20 at DEX 16). Fighter 1 is re-taken first so the Fighter-first grants (Heavy Armour, CON save, two skills) survive. The respec happens at the Crèche, not the Stone, because the gloves arrive there.

**ability_targets / CHA chain (T4-V6)** — Mirror of Loss: one DC 25 Religion check per character (fail = locked out forever), then a 60% roll per attempt. Religion is INT-based; only Charles is proficient, at INT 8. Plan: Enhance Ability (hers), Guidance, quicksave before each prayer. The Warped Headband of Intellect (INT 17, +3 vs −1) helps the Religion check. Birthright +2 CHA stacks with the Mirror for 24 out of combat.

**feats (T2-1 Alert over War Caster)** — Six videos ("controllers need initiative so they can go before enemies and stop them from acting"). Her initiative was d4+4, the slowest in the party by 3–8 (Charles d4+7, Gale d4+11, Asterion ~d4+10). Alert: d4+9, Surprise-immune, Hold Monster lands before the enemy's first turn and she is still Hasted on turn 1 behind Gale. Sentinel Shield adds +3 and Vigilance +5 in Act 3. War Caster protected a +6 CON save (+7 at CON 16) that Splint crit immunity (Acts 1–2), Helldusk −3 (Act 3), the shield and Charles's Aura of Protection mostly prevent; on the hard hits ~85% instead of ~98%. Dual Wielder was never a contender: a shield pairs with Phalar Aluve for no feat. Charles made the same trade on 2026-09-10.

**level1_gains / char 1 skills** — Fighter first grants two skills; a later Fighter dip grants none. Intimidation is on neither Guild Artisan nor the Swords list, and char 11 Expertise requires proficiency, so the Fighter pick is its only source. Perception is the most-rolled skill. Athletics at STR 8–10 is covered by Jack of All Trades. Deception: char 4 Expertise, no other source.

## Leveling

**char 4 Fighting style (Dueling)** — Duelling wants a lone melee weapon, Two-Weapon Fighting an off-hand attack; she makes neither.

**char 5 Invisibility / Enhance Ability** — Enhance Ability is B tier ("significant checks are less frequent than players expect") and she has Expertise ×4 plus Jack of All Trades; the reasons to keep it are the Mirror of Loss Religion check (T4-V6) and the odd theft. Both are exploration spells once Hold Person is online.

**char 6 replacement (T3-B5)** — the old swap dropped Longstrider for Hypnotic Pattern and made +3 m party movement a scroll dependency; she is the party's only Longstrider. Dissonant Whispers goes instead: single-target Frightened is outclassed by Hold Person from char 4.

**char 8 replacement (Greater Invisibility not taken)** — A tier ("anchors an entire party strategy"): the target stays invisible while attacking, permanent advantage, disadvantage against it. Concentration, so it competes directly with Hold Monster; her survivability lane is Helldusk and Wavemother's, not stealth. Dropped; scrolls if ever wanted.

**char 9 Plant Growth (T2-5 / T3-B3)** — the old row re-learned Hold Person (known since char 4), so one spell known was unassigned. Four videos (nrTSroBA4eI 16:02, 5UFoWD3Uwis 17:04, JDPCUMrtdZs 15:40, G_ShgMOS7zg 50:02): non-concentration, no save, quarter movement in 6 m; layers under Charles's Hunger of Hadar (his tier note already says "layer over Plant Growth") and her Glyph. Rule: between the pack and the back line, never on the melee cluster. Fire burns it away (T2-24), so Gale's fire goes at targets outside the zone. The old "more Hold, not more Fear" argument stands; it just did not need a second copy of Hold Person.

**char 10 replacement (T3-B6)** — Dominate Person is D tier ("one unreliable temporary ally for a level 5 slot"); not taken. Tasha's Hideous Laughter stays all game: through the Band it is a bonus-action WIS save at her Acuity DC and the tier note calls it a boss-immunity bypass. The swap slot is left unused; Invisibility stays (scouting, theft setup, escape) because Silence arrives as the regular Bard 10 pick one level later and nothing else on the list is dead weight.

**char 11 Magical Secrets (T2-6, T2-7, T4-V1)** — bg3.wiki: "At level 10, all Bards can learn two spells up to level 5"; Globe of Invulnerability and Heroes' Feast are 6th-level and not selectable, and with no Wizard dip there is no scribing, so Globe is scroll-only. Command first: the Band makes hers a bonus action at the party's highest Acuity DC and the L6 slot upcasts it to six targets, neither of which Gale can replicate. Conjure Elemental second: S tier, "a day-long, concentration-free elemental or myrmidon is comparable to adding another character to the party", and it needs no concentration so she still holds Hold Monster. Myrmidon choice (KaS6zqeSkP8 37:30, 51:01, 59:19): Air Myrmidon's Electrified Flail forces DC 13 CON or 2 turns Stunned on every swing and Raging Vortex is a no-save 10-turn Silence; Earth Myrmidon is the tank that draws the hits that would strip her Acuity. Water and Fire both work against Gale: Wet grants Fire RESISTANCE (Vulnerable to Lightning and Cold), and Healing Vapours stopped applying Wet in Patch 8 (bg3.wiki Wet_(Condition), Healing_Vapours), so the old "Water Myrmidon strips fire resistance for Gale" sentences were wrong and are deleted. T2-7: the summon lasts until long rest, so cast it from the L6 slot before the first fight and refund the slot with Spellcrux's bonus action; the cost is the second mid-fight Command / Hold Monster the amulet used to buy. Counterspell is the runner-up Secret, but Gale and Charles carry it and three carriers is one more than the guides advise (T4-V3: Counterspell against a higher-level spell rolls INT, and hers is 8 too).

**char 11 regular pick (Silence, T3-B12)** — bg3.wiki/wiki/Bard level 10 lists "Magical Secrets: Learn 2 non-Bard Spells" AND "Spells Known: 13 — Choose 1 additional Spell from the Bard Spell List"; level 11 "Spells Known: 14"; level 12 "Spells Known: 15". So in BG3 the two Secrets sit on top of the regular column and Bard 10 has three picks. The level-up UI presents the regular pick as a separate step from the Secrets, and it is the easiest pick on this level to miss. Silence takes it: A tier for caster lockdown, and the Magical Secrets note justifies dropping Counterspell partly by pointing at it.

**Cantrips (T3-B1)** — five videos open with Minor Illusion + Friends. Minor Illusion is S tier ("moves creatures toward a point without a saving throw"): groups enemies for Fireball and relocates NPCs for Asterion's theft routes; both Swords Bard guides name it for the face. Vicious Mockery is C tier ("too little damage to beat firing a bow") and waits until char 5. Mage Hand at char 11 or drop; its Throw can Wet a target (2 m splash) for Gale's Cone of Cold / Chain Lightning, the only Wet use left (T4-V1). Light is not taken: Gale learns Light at char 4 and Daylight at char 8.

### Spells-known ledger

Bard regular spells known 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 at Bard 1–11 (bg3.wiki/wiki/Bard: level 10 "Spells Known: 13 — Choose 1 additional Spell from the Bard Spell List" plus "Magical Secrets: Learn 2 non-Bard Spells"; level 11 "Spells Known: 14"; level 12 "Spells Known: 15"). The two Secrets sit on top of that column. Fighter grants none; one optional swap per level from Bard 2.

| Char | Bard | Regular known | Pick(s) | Swap | Known list after |
|---|---|---|---|---|---|
| 2 | 1 | 4 | Healing Word, Longstrider, Dissonant Whispers, Heroism | — | HW, LS, DW, Her |
| 3 | 2 | 5 | Tasha's Hideous Laughter | — | + THL |
| 4 | 3 | 6 | Hold Person | — | + HP |
| 5 | 4 | 7 | Invisibility | Heroism → Enhance Ability | HW, LS, DW, THL, HP, Inv, EA |
| 6 | 5 | 8 | Glyph of Warding | Dissonant Whispers → Hypnotic Pattern | HW, LS, THL, HP, Inv, EA, Glyph, HypP |
| 7 | 6 | 9 | Slow | — | + Slow |
| 8 | 7 | 10 | Confusion | none | + Confusion |
| 9 | 8 | 11 | Plant Growth | — | + Plant Growth |
| 10 | 9 | 12 | Hold Monster | none | + Hold Monster |
| 11 | 10 | 13 (+2 Secrets = 15) | Silence (regular) + Command, Conjure Elemental (Magical Secrets) | none | + Sil, Cmd, CE |
| 12 | 11 | 14 (+2 Secrets = 16) | Otto's Irresistible Dance | none | + Otto's |

Final 16: Healing Word, Longstrider, Tasha's Hideous Laughter, Hold Person, Invisibility, Enhance Ability, Glyph of Warding, Hypnotic Pattern, Slow, Confusion, Plant Growth, Hold Monster, Silence, Otto's Irresistible Dance (14 Bard) + Command, Conjure Elemental (Secrets). Learned then swapped out: Heroism (char 5), Dissonant Whispers (char 6). Never learned: Faerie Fire (C tier; was the Bard 1 fourth pick, Heroism replaces it per T3-B2 because it fills the concentration lane before Hold Person and covers Frightened), Fear (A tier; shares a role with Hypnotic Pattern; scroll if wanted), Dominate Person (D), Greater Invisibility (A, concentration), Globe of Invulnerability (scroll only), Light. Cantrips: Minor Illusion + Friends (Bard 1), Vicious Mockery (Bard 4), Mage Hand (Bard 10).

## Spells (entry reasoning)

**Hypnotic Pattern** — the tier lists rate it A, not S: short duration and ANY damage wakes the targets, so it does not survive a party already firing into the pack. One clean turn, not a lockdown.

**Slow** — half speed, −2 AC and DEX saves, one action, ~50% chance to fizzle a cast; the undead/construct answer where paralysis fails.

**Globe of Invulnerability** — rated the #9 spell in the game; not learnable, so scrolls for the Act 3 caster gauntlets and the Netherbrain's area attacks. Concentration, so a scroll cast costs Hold Monster that turn.

**Healing Word** — the no-healer party's bonus-action ranged revive; pairs with stocked Revivify scrolls; triggers the Whispering Promise and Broodmother's Revenge in Act 1.

**Silence (T3-B12)** — her Hold lane is idle in exactly the fights with nothing to Hold, so her concentration is free; Misty Step and Dimension Door are verbal and stop working inside it. Over Charles's Hunger of Hadar the pack is blinded, slowed and mute.

**Friends** — counts as a crime on Tactician/Honour; hide or fast-travel afterwards. Approval loss if cast on companions.

## Itemization — Act 1

**titanstring-bow / elixir-of-hill-giant-strength** — Archery + Sharpshooter + ranged Slashing Flourish apply the STR rider to every projectile; the elixir sets STR 21 against the Club of Hill Giant Strength's 19 and leaves both melee hands free for the Knife and a shield, so the Club on the Arcane Tower stool is skipped. Nothing competes for the elixir slot; she never drinks Bloodlust. Titanstring was compared only against hand crossbows (2026-09-10 §3): with Sharpshooter it is 23–28 a hit against 18.5 from a hand crossbow, and Ne'er Misser / Hellfire Hand Crossbow only pulled ahead through the bonus-action off-hand shot, which Healing Word and later the Band own. Titanstring is Acts 1–2 only now (T1-2).

**act1-offhand-bonbon (Safeguard Shield)** — a shield parked in the inactive melee set still gives its AC while she fights from the ranged set (the wiki states it outright), so +2 AC and +1 saves cost nothing on a character whose Arcane Acuity is stripped 2 turns every time she is hit. Fighter 1 supplies shield proficiency; no Dual Wielder needed. The Sentinel Shield, not Ketheric's, follows it (T2-3).

**knife-of-the-undermountain-king-offhand (T3-B11)** — the old note called Organ Rearranger "harmless filler" because this party's crits come from Hold, not threshold. The wiki confirms the crit reduction applies to ranged and spell attacks, so while she holds it, and if inactive-set passives pay out (T4-U3), it is a real −1 (The Dead Shot's 19 → 18). A shield needs no Light partner and no Dual Wielder feat, which two weapons would. Goes to Charles at the Stone as his bagged Psychic-immune fallback.

**gloves-of-archery** — +2 damage on every ranged hit; the longbow proficiency is redundant.

**gloves-of-dexterity** — #1 of the Act 1 top 20 ("the most impactful equipable item in Act 1, and in the narrator's view the entire game"). DEX 18 plus +1 attack rolls is a net +2 ranged accuracy over natural 16, plus initiative, AC, DEX saves and skills; the +1 applies to every Flourish projectile and to spell attacks. Sold by A'jak'nir Jeera, Crèche Y'llek. Worn all game (T2-10).

**wondrous-gloves** — +1 AC and one Bardic Inspiration; a nova-cycle swap.

**the-protecty-sparkswall** — #8 of 20, "the caster default through much of Act 2". +1 DC improves Hold Person, Hypnotic Pattern, Slow and Glyph. The Lightning Charge rider (+1 AC and saves) is dead: The Spellsparkler is Gale's. Low clothing AC is the price of DC until the Forge.

**adamantine-scale-mail (Splint)** — #15 of 20. AC 18 flat, attackers cannot crit, all incoming damage −2, melee attackers Reeling. A concentration save is DC = max(10, half damage), so a crit roughly doubles that DC; crit immunity is what protects Hold Monster. Fighter-first makes her the party's only legal Heavy wearer. Swap off Protecty once poured: −1 DC for +6 AC and crit immunity. The id keeps an older name so checkoffs survive.

**act1-ring2-bonbon** — the Whispering Promise is the only Bless before the Underdark; it comes off when Asterion has the Staff of Arcane Blessing because Bless is one non-stacking condition. Volo or Grat, ~40 gp; her bonus-action Healing Word triggers it. Crusher's Ring: +3 m, stacks with Longstrider. Ring of Protection (#20 of 20): +1 AC and all saves; the guides say the lowest-AC body. Bracing Band: +1 AC after a Shove.

**caustic-band** — #12 of 20, "for characters making several attacks per turn". +2 Acid per weapon hit covers melee, ranged and Thrown but NOT Unarmed Strike (wiki), so it never moves to Asterion. Ring 1 through Acts 1–2; the Act 3 option (T3-B7).

**act1-head-bonbon** — a coin-flip: Diadem (Arcane Synergy adds CHA to every ranged hit after a condition lands) vs Grymskull (crit immunity + Fire resistance; Heavy, so only she can wear it). Both replaced by the Helmet of Arcane Acuity in Act 2. **opt-warped-headband-of-intellect-bonbon (T3-B10)**: INT 17 for Arcana/History/Investigation/Religion and the Mirror of Loss Religion check; nobody wants it in combat; the Birthright pattern. Lump the Enlightened carries it in his gut (loot him, or call and loot him later if hired).

**broodmother-s-revenge** — #17 of 20. Any healing, even a potion at full HP, coats the bow for +1d6 Poison per projectile for 2 turns; Healing Word is the trigger. Skip poison-immune enemies. Replaced by Spellcrux in Act 2 because the per-turn heal competes with the Acuity loop's bonus action.

**boots-of-speed** — #14 of 20; bonus-action Dash for "the character most likely to waste a turn out of position". Not Asterion's: Step of the Wind gives him bonus-action Dash and Disengage from Monk 2, and the boots would displace the Night Walkers. The Click Heels disadvantage rider is bugged (it applies to the caster's own reactions).

**act1-cloak-bonbon** — the Deathstalker Mantle is the only Act 1 magical cloak and it is a Dark Urge reward that goes to Asterion; every other cloak first appears in Act 2.

**arrows-of-many-targets-bonbon-a1 (T3-B4)** — one attack roll on up to four targets (wiki: "an additional half of that damage to three other targets"; riders not halved); rated S+ in ratings.md ("near quadruple damage, four attack rolls, fastest Arcane Acuity stacking, plus a crit bug"). Two arrows cap Acuity unhasted on turn 1 (Act 2 on). Whether the Titanstring / Cold rider reaches the secondary targets is an in-game check.

## Itemization — Act 2

**helmet-of-arcane-acuity** — Mason's Guild, Reithwin (Act 2, not Act 3). Each weapon hit = 2 turns of Acuity; each turn = +1 spell attack and +1 DC, cap 10. Titanstring stays because a ranged Flourish fires two projectiles and each damaging one is a separate trigger: two Flourishes are four hits, +8 in one Action; a Hasted turn caps at +10. Dual hand crossbows' only edge was a fifth hit from the bonus-action off-hand shot, and the bonus action belongs to Healing Word / the Band. Damage taken strips 2 turns, which is why her defensive gear matters.

**act2-ranged-bonbon (Titanstring)** — carried over; STR rider on every projectile, Flourish and special-arrow riders included; Drakethroat set to Cold so every projectile drops Snowburst ice (T2-8). Replaced by The Dead Shot in Act 3 (T1-2).

**act2-melee-bonbon / act2-safeguard-bonbon** — the melee set is a rack of holder passives, never swung. Safeguard leaves at Moonrise (Sentinel), the Knife at the Stone (Phalar).

**phalar-aluve-bonbon (T2-25)** — Charles hands it over at his respec. Versatile, not Light, so without Dual Wielder only a shield can share her hands with it. Shriek: 6 m aura on the wielder, ends if unequipped, costs an Action; spend the Haste action on turn 1 or pre-cast from stealth; play 3–6 m from the targets (outside the 3 m ranged-disadvantage band, inside the aura): −1d4 to their saves and attack rolls, +1d4 Thunder per damage instance. Sing (+1d4 to allies' attacks and ALL saves for 5 turns; 6i-Rpr9ziqs 36:19) was proposed for survival fights; decision: ALWAYS Shriek, Sing is not added. Whether Sing stacks with Bless is unverified anyway.

**act2-offhand-bonbon / opt-sentinel-shield-bonbon (T2-3)** — roles swapped. Sentinel Shield (Lann Tarv, Moonrise main floor, ~580 gp: +2 AC, +3 initiative, advantage on Perception) is the default from Act 2 to the end; Ketheric's Shield (+2 AC, advantage on DEX saves, +1 spell save DC and +1 spell attack; Colony second fight, or pickpocket after disarming him) is the option for fights where +1 DC matters. The report recommended no if Alert was taken ("initiative items to the one character without Alert"); accepted anyway, so she rolls d4+9 (Alert) +3 (Sentinel) +5 (Vigilance, Act 3). Only one Sentinel Shield exists. Verification caveat, once: the wiki confirms only that a shield's AC in the inactive melee set carries over while the ranged set is live; it says nothing about other shield passives, so Sentinel's +3 initiative and Ketheric's +1 DC are in-game checks (T4-U3). Not the Adamantine Shield: its crit immunity is exactly the unconfirmed passive, the second Mithral ore is Charles's, and the Splint gives her crit immunity outright. The `opt-sentinel-shield-bonbon` id now holds Ketheric's Shield (ids are frozen).

**act2-chest-bonbon / act2-hands-bonbon** — carried over; nothing in Act 2 beats either.

**act2-elixir-bonbon** — Hill Giant through Act 2; Cloud Giant no longer follows (T2-2). Giant Strength vendors: Araj, Talli, Mattis, Roah.

**spellcrux-amulet** — Warden, Moonrise prison. Bonus action, restore any one slot, once per long rest. On a Bard 11 with one L6 slot that was "a second six-target Command"; from Act 3 it is the Myrmidon refund (T2-7). Replaces Broodmother's.

**act2-ring2-bonbon (T2-8 Snowburst Ring)** — five videos (s2TJ7kOaJmA 31:33, nrTSroBA4eI 30:04, 5UFoWD3Uwis 31:05, JDPCUMrtdZs 35:25, Jk0KrLcfeCA 1:14:12). Every Cold-damage hit drops a 4.5 m ice circle (2 turns; DEX save vs her spell DC or Prone): four to eight circles a turn with no slot or concentration, and it works on the undead and constructs that ignore Hold and Command. Needs Gale's Drakethroat set to Cold every day (Gale's file updated to match). Costs: ice under the melee cluster is difficult terrain for Charles and Asterion, and Prone ends Charles's Hold Person with no save (his Prone-immune boots stop being a flex); Gale's fire melts it. Rule: shoot the back line first. Last Light Inn, loose plank in the bedroom north of the bar, DC 10 Perception. Snowburst does not work with thrown weapons or with after-cast Cold (Hunger of Hadar, Agathys). Whether Acuity raises the ice DC is unverified. Old note: the slot was "genuinely open until Act 3" and the Risky Ring is NOT a candidate (disadvantage on the CON saves protecting Hold Monster). Options kept: Whispering Promise (off once Asterion casts Bless), Ring of Mental Inhibition (Mental Fatigue compounds with her Acuity DC), Callous Glow Ring (+2 Radiant vs illuminated targets per projectile; Gale's, and it fights Charles's Darkness).

**cloak-of-cunning-brume** — Mattis, ~70 gp; the Act 2 cloak pool is built for melee (Fleshmelter, Thunderskin trigger on being hit) and Cloak of Protection goes to Charles.

**act2-feet-bonbon (T3-B8)** — Boots of Brilliance restore one Inspiration per long rest. The old rationale ("Inspiration-starved rather than AC-starved") is weaker than written: the wiki lists Flourish as "Cost on hit", so a Sharpshooter miss refunds the die. Flourish on every attack. Still the best Act 2 boot for her; Boots of Speed stay bagged.

**arrows-of-many-targets-bonbon-a2** — two arrows cap Acuity on turn 1 unhasted; each secondary target gets a Snowburst circle if the Cold rider carries (check).

## Itemization — Act 3

**band-of-the-mystic-scoundrel** — Chult backpack via Akabi's wheel at the Circus, one party member only. After a weapon hit, Enchantment and Illusion spells become bonus actions: Acuity with the action, Hold Monster or six-target Command in the same turn. Wiki caveat: once Quickening Incantation is active she cannot cast those spells as an ACTION that turn. Any weapon attack triggers it, even a barrel before combat.

**act3-ranged-bonbon (T1-2 The Dead Shot)** — four videos (-gnyG9gH-no 29:01, s2TJ7kOaJmA 27:27, 5UFoWD3Uwis 28:28, G_ShgMOS7zg 46:53, 54:08): "we care more about just hitting all of our shots because we have so many broken effects tied to hitting." The Titanstring "all game" decision compared it only against hand crossbows. The Dead Shot is +2 and Keen Attack doubles proficiency on its ranged attacks, so at char 9+ it is +5 to hit over Titanstring, cancelling Sharpshooter's −5, and Improved Critical crits on 19. Damage per hit drops ~7 (Cloud Giant rider lost). Against AC 18: 75% × 27.5 = 20.6 expected per shot vs 50% × 34.5 = 17.3; on a Hasted 8-projectile turn, 6 hits instead of 4, each an Acuity and Band trigger. Titanstring only wins above ~76% base hit chance, hence the option ("when hit chance is already ≥ 75%: Bless, Held target"), and it then needs a Giant Strength elixir that day. Keen Attack: "doubles their Proficiency Bonus when rolling ranged attacks with this weapon, unless they have Disadvantage" (bg3.wiki Keen_Attack), so never into Charles's Darkness. One copy exists: Asterion (T3-A2) and Charles (T3-C3) both wanted it; this use beats both and both files drop the idea. Fytz the Firecracker, Stormshore Armoury. Frees the elixir slot (T2-2) and ends the second daily Giant Strength drinker. Gontr Mael stays Asterion's (Celestial Haste is self-only concentration; she is Hasted by Gale and concentrating); Hellrider's Longbow is Gale's.

**act3-elixir-bonbon (T2-2 Vigilance)** — with the STR rider gone the Giant Strength elixir buys nothing; Vigilance is +5 initiative and Surprise immunity on a d4 roll, ~25 gp (Danthelon, Kith, Popper). With Alert and Sentinel she is d4+17, more than needed, but the slot has no better use. Cloud Giant (STR 27) is Asterion-only now.

**act3-melee-bonbon / act3-offhand-bonbon / opt-ketherics-shield-bonbon-a3** — as Act 2. Viconia's Walking Fortress goes to Charles. Ketheric's +1 DC on a single-boss Hold Monster is the case for the swap.

**act3-ring2-bonbon (T3-B7 Ring of Feywild Sparks)** — hidden +1 spell save DC not on the tooltip (bg3.wiki; ratings.md already S), Auntie Ethel at the Blushing Mermaid. +1 DC on every Hold Monster / Command vs Caustic Band's 8–12 Acid a turn; the reviewer leaned ring, accepted. Caustic Band is the option for trash packs. The old note's Ring of Free Action swap is gone: Boots of Persistence already grant Freedom of Movement and the ring is Asterion's.

**opt-bhaalist-armour-bonbon (T2-9)** — s2TJ7kOaJmA 28:30. Inside 3 m of a Held target every projectile crits and Piercing is doubled: ≈ 600 vs ≈ 275 on a Hasted 8-projectile turn. The report recommended no: AC 17 instead of Helldusk's 21 and 3 DR, every hit strips Acuity and forces a save, the aura helps nobody else (Charles Psychic/Radiant, Asterion Bludgeoning, Gale Fire), she must stand in the melee cluster, and the Bhaal path (Echo of Abazigal after the Murder Tribunal) is the price. Accepted only as a bagged option for a single-boss Hold fight. Verified: Aura of Murder 3 m; Paralysed auto-crit within 3 m; the in-3 m ranged disadvantage cancels the Paralysed advantage (the auto-crit still applies).

**amulet-of-greater-health** — CON 23 and advantage on CON saves; on her the advantage half duplicates what Helldusk AC 21 and the refreshing cloak already prevent, while Charles has a permanent Risky Ring disadvantage it cancels. A free L6 slot per long rest is worth more to a controller. (The old wording cited War Caster's advantage; Alert replaced it, T2-1.)

**act3-amulet-bonbon (Spellcrux; T2-30 Amulet of the Devout declined)** — Jk0KrLcfeCA 57:36 proposed the Devout: +2 spell save DC on every Hold Monster, Command, Confusion and Glyph, live from turn 1 and additive to the Acuity cap; the only +DC neck in the game, and the +2 works on anyone (only the Channel Divinity charge is cleric-gated; loot.md's old reason was wrong, T4-V8). Declined: Spellcrux stays. Does the Devout replace something we want? No. Spellcrux is already her Act 3 neck and nothing else is displaced; with T2-7 the refunded L6 slot is what re-arms the six-target Command after the morning Myrmidon, and the curse constraint on the offering chest (Jaheira with Khalid's Gift loots it cleanly) still stands. Revisit if the Myrmidon opener is abandoned.

**helldusk-armour-bonbon** — Raphael, House of Hope. AC 21, all incoming damage −3, Fire resistance, Burning immunity, Infernal Retribution (a caster whose spell she saves against starts Burning), non-concentration Fly once per long rest; grants its own proficiency. The DR is the point for a concentrator: chip damage becomes zero, so no concentration save and no Acuity stripped. Heavy: Stealth at disadvantage; Asterion sneaks. **opt-armour-of-agility**: Medium, AC 17 + full DEX (wiki Exotic Material), so 21 at DEX 18 now that the Gloves of Dexterity stay on (the old note said 20 at DEX 16 under Helldusk Gloves); +2 to all saves, no Stealth penalty; Medium Armour Master or Magic Initiate: Cleric breaks the passive. Take it when +2 saves beat −3 DR.

**wavemother-s-cloak** — once per turn in combat, Water Layer Protection until she takes damage: +2 AC, +2 saves, Fire resistance, Burning immunity. On a backline controller rarely hit it never falls off; strictly better than a Cloak of Protection's flat +1/+1 for her, and it leaves Cloak of Displacement free for Asterion.

**act3-hands-bonbon (T2-10)** — Gloves of Dexterity all game. Helldusk Gloves (Haarlep, House of Hope: Infernal Acuity +1 DC and +1 to all attack rolls, Infernal Touch 1d6 Fire per weapon hit; ≈ +10 damage a turn and +1 Hold Monster DC) were her Act 3 hands; with base DEX 8 they would cost DEX 18 → 8 (−5 attack, −5 damage, −5 AC, −5 initiative, DEX saves and skills), so they are out of her file and go to nobody. Craterflesh Gloves want a crit build she is not.

**act3-head-bonbon** — Helmet of Arcane Acuity: three or four hits a turn reach +10 DC. Birthright rejected for the slot: +2 CHA is +1 DC, ten against one; bagged as the Persuasion / Deception / Intimidation swap (stacks with the Mirror of Loss for CHA 24).

**act3-feet-bonbon / opt-boots-of-striding-bonbon (T3-B14)** — Boots of Persistence (Dammon, Forge of the Nine): permanent Freedom of Movement and Longstrider; Medium proficiency required (Fighter 1). Helldusk Boots are Charles's (save disadvantage to undo); Gale cannot wear Persistence, so this allocation leaves nobody stranded. Boots of Striding are free once Charles moves to Helldusk Boots: Focused Stride on casting a Concentration spell blocks Prone and forced movement while it holds; Persistence covers Paralysed and Restrained; Striding covers knockdowns and Shoves. Per-fight choice.

**arrows-of-many-targets-bonbon-a3** — the turn-1 Acuity filler before the bonus-action Hold Monster / Command.

## Progression

**prog-ranged (T1-2)** — "Titanstring Bow, all game" → "Titanstring Bow → The Dead Shot (Act 3)". The hand-crossbow pivot was never needed: two Flourishes an Action are four Acuity triggers and a Hasted turn caps Acuity alone.

**prog-consumables (T2-2)** — "Giant Strength every long rest, all game (Hill 21 → Cloud 27)" → Hill Giant (Acts 1–2) → Vigilance (Act 3). Never Bloodlust.

**prog-hands (T2-10)** — Helldusk Gloves removed from the chain.

**prog-ring2 (T2-8, T3-B7)** — flex → Snowburst (Act 2); Caustic Band → Feywild Sparks (Act 3).

**prog-weapons (T2-3)** — Sentinel Shield replaces Ketheric's as the default off hand; Ketheric's is the option. Sentinel arrives at Moonrise (before the Stone), Phalar at the Stone.

**prog-head (T3-B10)** — Warped Headband and Birthright as dialogue swaps.

## Playstyle

**Sharpshooter toggle (T2-4)** — -gnyG9gH-no 13:55 gives "off below 30% displayed". With Titanstring's flat rider the threshold is higher: the −5 is worth taking only above ~65% base hit chance in Act 1 (displayed ≥ 40% with it on) and would have been ~85% in Act 3 with Cloud Giant (displayed ≥ 60%); ~10 points lower under advantage. Moot in Act 3 with The Dead Shot (+5 cancels the −5).

**Flourish cost on hit (T3-B8)** — the wiki lists "Cost on hit"; a miss refunds the Inspiration, so Flourish on every attack.

**Drakethroat (Gale's Twinned Draconic Elemental Weapon)** — the spell reaches only a weapon on the ground or a MAIN-HAND weapon, and her melee main hand holds the Daylight-enchanted Knife / Phalar Aluve, so the bow goes on the ground beside Charles for one Twinned cast. +1 attack and +1d4 elemental per projectile, until long rest. Element is Cold every day (Snowburst); Charles's blade gets Cold too unless the fight resists it. Titanstring in Act 2, The Dead Shot in Act 3.

**Daylight carrier** — Gale's Daylight (Enchant Item) on her main-hand weapon lasts until the next long rest (bugged) and travels with her, keeping Gale lit for Coruscation → Callous Glow; it requires a main-hand weapon (rules out Asterion's empty hands) and her mid-range position keeps the 15 m radius over the fight. Cast it before any Darkness Arrow; never swap the main hand afterwards.

**Melee set rack** — two weapons would need Dual Wielder; a weapon plus a shield needs nothing. Shield AC from the inactive set is wiki-confirmed; the rest is T4-U3.

**Arrow of Darkness last (T3-B13)** — she has no blind immunity, so anything under the cloud is untargetable for the rest of her turn; Flourishes first, arrow last, aimed at the ground so the cloud edge sits between Charles and the target. The cloud blocks ranged attacks both ways (T4-V2).

**Plant Growth under Hunger of Hadar (T2-24)** — blinded enemies cannot jump, quarter speed, Repelling Blast pushes escapers back; fire (Fireball, Scorching Ray, Heat) burns Plant Growth away, so no fire into the zone. Gale's Armour of Landfall gives him his own Plant Growth once per short rest.

**Arsonist's Oil (T2-21, party)** — thrown Elixir of Fire Resistance, Arsonist's-Oil hit, second thrown elixir overwrites → Vulnerable to fire; her ranged Flourish coats two targets per attack and the oil lasts ten turns. Recorded on Gale / party; her part is the coated arrow.

**Lanes with Gale** — Bonbon Concentration (Hold), Gale non-concentration (Extended Command). T4-V4: Command casts from any Sorcerer slot, so Gale never needed her as a Command fallback.

**Mirror of Loss (T4-V6)** — see Creation.

## Declined (with reasons)

- **Amulet of the Devout (T2-30)** — Spellcrux stays; nothing displaced (see act3-amulet-bonbon).
- **Sing (T2-25)** — always Shriek.
- **Fighter 2 / Bard 10 (Action Surge)** — Honour-only argument; loses the L6 slot; the Hasted action carries Extra Attack outside Honour.
- **Bard-first** — loses Heavy Armour, CON saves and Archery for Act 1.
- **Other dips** (Arcane Archer 7 / Bard 5, Swords 6 / Gloom 3 / Assassin 3, Spore Druid 2, Thief 3, Bladesinging 2, Wizard 1) — cap slots at 3rd or cost Bard 10–11 (Hold Monster, Secrets, six-target Command).
- **Items already adjudicated (report Tier 5)** — Gloves of Dexterity respec at creation (early Act 1 at DEX 8), Bloodlust or Battlemage elixir, hand-crossbow pair, Martial Exertion Gloves, Strange Conduit Ring, Callous Glow + Luminous Gloves, Rhapsody, Marksmanship Hat (Act 2 only, same stop as the Helmet), Misty Step item, Two-Weapon Fighting, Cloud of Daggers at Bard 3, Counterspell as a Secret, Graceful Cloth to DEX 20, Bhaalist as the standing chest, Risky Ring (disadvantage on her CON saves), Adamantine Shield, Gontr Mael, Hellrider's Longbow, Helldusk Boots, Cloak of Protection.

## In-game checks

- **T4-U3 inactive-set passives** — with the bow drawn, read the character sheet: Sentinel Shield +3 initiative; Ketheric's Shield +1 spell save DC / spell attack; Knife of the Undermountain King crit threshold (The Dead Shot's 19 → 18). Four videos assert the Knife's crit reduction fires from the inactive set; the wiki confirms only shield AC.
- **Snowburst DC and Acuity** — whether Arcane Acuity raises the ice circle's DEX save DC.
- **Titan Weapon rider on Arrow of Many Targets secondary targets** — whether the Titanstring STR rider and the Drakethroat Cold rider reach the three secondary targets (and so drop Snowburst ice under each).
- **T4-V5 caveat (party)** — whether ranged spell attacks inside an enemy's reach take Threatened disadvantage.
- **Mirror of Loss** — quicksave before the prayer; one Religion attempt per character.
