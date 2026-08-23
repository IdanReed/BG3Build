# Brief: reading a tier list transcript into ratings

How to turn one Cephalopocalypse tier-list transcript into a complete `(item, tier)`
table. Written after several failed attempts at automating it — the failure modes below
are all real and all cost accuracy.

## The job

For ONE video id, produce a rating for **every item the video rates**, not just items
some party uses. Write the result to `research/slots/<videoid>.json`.

## Step 1 — dump the verdicts

```sh
python tools/dump_tier_verdicts.py --source <VIDEOID> --before 24 --after 13
```

That prints every spoken "`<letter>` tier" in transcript order, with the run-up (`<<<`)
and the tail (`>>>`). Read them **in order**. If you need more context around one, use:

```sh
python tools/lookup_item_tier.py --source <VIDEOID> --item "Some Item" --words 90
```

Treat the letter that tool guesses as a hint only — measured against known answers it
scored 9/9 on one list and 1/5 on another.

## Step 2 — assign each verdict to an item

The narrator uses two phrasings, and telling them apart is the whole task:

1. **Name in the run-up** — "…the Bracing Band, so I'm going to say it is **A tier**."
2. **Name in the tail** — "**D tier** for the Rain Dancer."

### The trap that breaks naive matching

After delivering a verdict the narrator immediately introduces the *next* item, so the
tail often contains two names:

> "**D tier** for the rain dancer. The Staff of Arcane Blessing has no enhancement bonus…"

Here `D` belongs to the Rain Dancer, and the Staff of Arcane Blessing is the next item —
it gets its own verdict later. Rules that work:

- In the tail, only the name within ~5 words and directly after "for the" is the rated item.
- An item's name is **repeated twice** when it is introduced ("the ring of free action the
  ring of free action gives you…"). That marks the START of a discussion, not a verdict.
- Every verdict belongs to exactly one item, and each item usually gets exactly one
  verdict. If two items seem to claim one verdict, one of them is the next item.

### Other things that actually happen

- **Skip the first ~3 minutes.** The opening defines the tier scale ("in S tier I'm
  placing items that…") and produces 5–7 fake verdicts. Ignore them.
- **Lists are roughly alphabetical.** Use that to sanity-check your ordering, and to spot
  an item you have skipped.
- **Deliberation:** "I'm torn between A tier and B tier… on balance I'll give it B."
  Record the final letter only.
- **Revisions:** "I'd move Chira's Amulet down to B tier as well" — that re-rates an item
  from a *different* video. Record it only if it is in this video's slot, and note it.
- **Conditional ratings:** e.g. gloves rated "B for Honour mode" but "busted on Tactician
  or below", or an item rated D *only because its effect is bugged*. Capture the condition
  in the verdict text — it changes the answer for a non-Honour run.
- **Availability limits:** e.g. the Ring of Evasion is obtainable only by an origin Gale.
  If the narrator says so, put it in the verdict text in CAPS.
- **A list may not use every letter, and some add one.** The medium-armour list hands out
  S freely; what it declines to include is an *S+*, which the narrator says Luminous
  Armour would occupy if it existed. The arrows, elixirs and potions lists do run a real
  S+. Follow what the narrator defines for the list in front of you.
- **Captions garble names badly.** Real examples: "Marco HH gear" = Markoheshkir,
  "mel's first staff" = Melf's First Staff, "costic band" = Caustic Band, "rap city" =
  Rhapsody, "F Lou" = Phalar Aluve, "the ciret of" = Circlet of, "bird band" = Spurred
  Band, "ma's friend" = Mage's Friend. Use the item's described effect to identify it, and
  check the name against `research/item_vocab.json`, which lists real item names per slot.

## Step 3 — write the file

`research/slots/<videoid>.json`, exactly this shape:

```json
{
  "source": "<VIDEOID>",
  "label": "Rings tier list, Act 1",
  "slot": "Rings",
  "rated_in": "act1",
  "verdicts_in_transcript": 33,
  "items": [
    { "item": "Caustic Band", "tier": "S", "at": "7:16",
      "verdict": "for almost every party; goes on whoever makes the most attacks in a round" }
  ],
  "unassigned": [
    { "at": "14:01", "tier": "A", "why": "a revision to an amulet from another video" }
  ]
}
```

- `item` — the real name, spelled as `research/item_vocab.json` spells it.
- `tier` — one of `S A B C D F`.
- `verdict` — one clause, your own words, ≤ 20 words. Do not paste transcript text.
- `unassigned` — every verdict you could NOT confidently attribute. Do not guess to
  empty this list; an honest gap is worth more than a wrong rating.
- `verdicts_in_transcript` — the count after dropping the opening scale definition.
  `len(items) + len(unassigned)` should equal it. If it does not, you have missed one.

## Rules

- Never invent a rating. If the narrator never gives an item a letter, leave it out and
  say so in `unassigned`.
- Never convert a rank into a letter, or carry a rating across from another video.
- Do not edit any file other than your own `research/slots/<videoid>.json`.
- Report back only: the video id, the item count, and anything you could not resolve.

## Variant: spell and cantrip lists

Same method, three differences.

1. **Use the [Updated] Patch 8 series only.** The playlist carries two spell series; the
   older one predates Patch 8 and this run is on Patch 8, so the updated videos supersede
   it. The updated cantrip list is `mgqMv2h-0x0`; the updated spell lists are titled
   "ULTIMATE SPELLS GUIDE - [Updated]".
2. **Write to `research/spells/<videoid>.json`**, not `research/slots/`. Same shape, but
   replace `slot` with `spell_level` (0 for cantrips, 1-6 otherwise) and drop `rated_in`.
3. **Names are spells, not gear**, so check spellings against the spell names used in
   `content/characters/*.md` (each build has a `spells` block with `mandatory` and
   `recommended` lists) rather than `item_vocab.json`.

Extra things that happen in the spell lists:

- A spell is often rated **per class** ("A tier generally, but S tier on a Sorcerer") or
  **per use** ("S for the concentration-free version"). Record the headline letter in
  `tier` and put the qualifier in `verdict`.
- **Upcasting** gets discussed at length; it does not change the letter.
- These lists are long and dense, with 40+ verdicts each. Work down them in order.
- Do not rate a spell that appears only as a comparison ("better than Magic Missile").

## The mangling is worse than any table

Later readers found the captions mangle "tier" in at least these ways, beyond the glued
letters: `CTI`, `DTI`, `dier`, `deta`, `detail`, hyphenated `c-tier`, the two-token
`dt tier`, `<letter> here` ("s here for the sacred star"), and — most awkward — the word
being **absent altogether** ("the plus one quarterstaff is D", "B for the corpse
grinder"). The matcher now covers everything except the last case.

So treat the tool as a floor. The reliable cross-checks are structural, and worth doing
every time:

- The list runs alphabetically. A gap in the alphabet is a missed verdict.
- The narrator often states his own totals — "that is 21 of the 42 second level spells",
  "there are 20 act one armours", "five weapons in S tier". Count yours against his.
- An item with a full write-up and no letter is either a genuine omission (record it in
  `unassigned`) or a mangled verdict you have not found yet. Look again before deciding.
