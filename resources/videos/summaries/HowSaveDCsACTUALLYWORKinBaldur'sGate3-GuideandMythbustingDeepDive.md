# How Save DCs ACTUALLY WORK in Baldur's Gate 3 - Guide and Mythbusting Deep Dive

- Playlist index: 0284
- Video ID: `PTAxrNWT2wE`
- Source: https://www.youtube.com/watch?v=PTAxrNWT2wE
- Transcript: `resources/videos/transcripts/PTAxrNWT2wE.md`
- Channel: Cephalopocalypse · Duration: 31:11
- Reviewed: 2026-09-11
- Scope: mechanics deep dive on the five save-DC formulas in BG3, with the item / scroll / illithid DC rule as the main subject. Not a build guide.

## Build

Not a build guide. No race, class, item, elixir or turn recommendations. The one piece of build advice is at [25:36]: arrange a multiclass so that the class most recently taken at level 1 has the casting stat you want, because that stat governs spells cast from items, scrolls and illithid powers.

## Mechanics claims

- [2:35–3:38] A saving throw is 1d20 + the relevant ability modifier + proficiency bonus if the class is proficient in that save, plus other bonuses. Typical saves are 13–15 at low level and 17–20 at high level. Meeting or beating the DC succeeds.
- [5:12–6:15] There are five DC types: fixed, concentration, maneuver, spell and item. The formulas are reciprocal, the same for the party and for enemies, with a few exceptions. Item DC does not exist in tabletop and is BG3-specific.
- [6:48–7:49] Fixed DC is a set number: traps, story effects, consumables. A thrown grease bottle is DC 12 DEX every time; the Grease spell uses the caster's spell save DC instead. A few spells and items are bugged to use fixed DCs.
- [7:49–9:23] Concentration save is a CON save with DC = half the damage taken, minimum 10. 1 damage is DC 10, 100 damage is DC 50. CON-save bonuses apply. The only lever an attacker has is dealing more damage.
- [9:23–12:32] Maneuver DC = 8 + proficiency bonus + the higher of the STR or DEX modifier. Level 1 with STR 16 is 13; level 12 with STR 20 is 17. It governs Battle Master maneuvers, monk Stunning Strike (a change from tabletop, where Stunning Strike is a spell-style DC), weapon actions, and shield bash, which was recently fixed from spell DC to maneuver DC. Some save-DC items apply to maneuver DC, others only to spell save DC, so maneuver DCs run a little lower.
- [13:03–16:09] Spell save DC = 8 + proficiency bonus + the casting stat of the class that learned the spell, regardless of multiclass order. A Bard/Cleric uses CHA for bard spells and WIS for cleric spells. A spell known from two classes gives two versions, pick the one with the higher stat. Wizard spells, including spells scribed from scrolls, always use INT even at Wizard 1. Class features with saves, such as Glamour Bard's Mantle of Majesty, use that class's spell DC.
- [17:45–19:21] Item DC = 8 + proficiency bonus + a casting stat, where the stat is that of the most recent NEW casting class, the class most recently taken at level 1. It applies to spells cast from items, spells cast from scrolls and illithid powers. For a mono-class character it equals the spell DC.
- [19:52] Item DC is affected by most save-DC-increasing items, like spell save DC. Some spells with repeatable effects are bugged to use item DC on recasts: the first Call Lightning uses spell DC, every recast uses item DC.
- [20:22–22:58] Only classes with a casting ability count. Fighter and Rogue do not change the stat unless Eldritch Knight or Arcane Trickster is taken, which counts from the subclass level (Fighter 3), not from Fighter 1. With no caster class at all the class default applies: Fighter and Rogue INT, Barbarian CHA, Monk WIS. Paladin and Ranger count from level 1, before they know any spells.
- [21:24] A Sorcerer who dips Cleric casts a known Fireball with CHA but a scroll of Fireball with WIS.
- [23:30–25:05] Worked examples. Cleric 1 / Bard 1 / Cleric 10 uses CHA. Cleric 1 / Fighter 1 / Cleric 10 uses WIS. Cleric 1 / Fighter 3 (Eldritch Knight) / Cleric 8 uses INT. Cleric 1 / Paladin 1 / Cleric 10 uses CHA. Warlock, Paladin, Bard, then Cleric uses WIS; swap the last two and it is CHA. Only the level at which the newest class was entered matters.
- [26:41–29:14] Opinion: the rule is most likely an unintended leftover; the presenter's preferred fix would be highest mental stat.

## Verdicts

No tier list. The presenter calls item DC "one of the only things in the entire game that cares about what order you took your classes in" [19:21] and says it "adds unnecessary complexity and unnecessary traps for new players with no benefit" [28:14]. He warns new players to skip the item-DC section [16:42].

## Relevance to our party

Every DC formula the party relies on is one of the five here. Charles (Paladin 7 / Hexblade 5), Gale (Sorcerer 11 / Fiend Warlock 1) and Bonbon (Fighter 1 then Swords Bard 11) all end with CHA as the newest casting stat under this rule, so their scroll casts and illithid powers use the same stat as their class spells; Asterion (Rogue 1, then Monk, then Rogue 2–3) lands on Monk's WIS because Rogue is ignored. `content/tadpole.md` already encodes exactly this rule and the same per-character outcomes. The video's concentration formula matches deviation D5, its maneuver formula matches Asterion's Stunning Strike entry, and its spell formula plus "most save-DC items apply" matches Charles's Hold Person at DC 27 (8 + 4 + 5 + 10 Acuity). The video never names Arcane Acuity, the Gloves of Battlemage's Power, the Helmet of Arcane Acuity or the Band of the Mystic Scoundrel; the only statement that touches them is the general one at [19:52] that item DC takes save-DC item bonuses.
