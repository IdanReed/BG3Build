#!/usr/bin/env python3
"""Dump every spoken tier verdict from the tier-list transcripts, in order, with context.

Why this shape: automatic attribution of a verdict to an item does not work reliably.
The transcripts are YouTube auto-captions, so names arrive garbled, and the wiki
vocabulary contains generic base names ("Staff", "Glaive", "Club") that match every
ordinary use of the word and swallow nearby verdicts. Measured against the 29 known
staff ratings, fuzzy attribution scored 7 right, 0 wrong, 22 missed -- precise but
useless recall, and unverifiable on the transcripts with no known answers.

So this tool does only the part a machine does well: find each "<letter> tier" verdict
and print the run-up to it. Naming the item is left to a reader, which is reliable
because the narrator states the item immediately before or after the verdict.

    python tools/dump_tier_verdicts.py --source seZJlJ9tvag
    python tools/dump_tier_verdicts.py --slot Rings --out research/verdicts-rings.txt
    python tools/dump_tier_verdicts.py --list

Pair it with `tools/scan_item_tiers.py --party-only` for a hint of which of the party's
items each passage is likely about; treat that as a pointer, never as the answer.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

TRANSCRIPTS = pathlib.Path("video_transcripts")

ALL = ("act1", "act2", "act3")

# Same source table as tools/scan_item_tiers.py: which video rates which slot.
SOURCES = [
    ("9BcQXb37Bik", ("Elixirs",),                  ALL, "Elixirs tier list"),
    ("HygsHA55jNU", ("Potions & Oils",),           ALL, "Potions tier list"),
    ("VL49XCJgYno", ("Potions & Oils",),           ALL, "Grenades tier list"),
    ("ZMCimWeIxCk", ("Potions & Oils",),           ALL, "Arrows tier list"),
    ("6TdhnnPbupo", ("Potions & Oils",),           ALL, "Poisons, oils and coatings tier list"),
    ("kxTZtj7SY84", ("Potions & Oils",),           ALL, "Barrels, satchels and fireworks tier list"),
    ("Ke2Kbtd-8Do", ("Elixirs", "Potions & Oils"), ALL, "Complete consumables tier list"),
    ("TwFGCc8OOfw", ("Armour",),                   ALL, "Armour tier list: robes, clothes and cloth"),
    ("YsQlQcxhnFQ", ("Armour",),                   ALL, "Armour tier list: light armour"),
    ("5Sbj8DDA04o", ("Armour",),                   ALL, "Armour tier list: medium armour"),
    ("VjmWkRCoDWE", ("Armour",),                   ALL, "Armour tier list: heavy armour"),
    ("7-K743ByJug", ("Armour",),                   ALL, "Complete armour guide"),
    ("5wATdII3wmI", ("Off-hand & Shields",),       ALL, "Shields tier list"),
    ("MbZ0r-Tfixg", ("Cloaks",),                   ALL, "Cloaks tier list"),
    ("nnmJWxi_IzA", ("Hands",),          ("act1",), "Gloves tier list, Act 1"),
    ("e4bPma5G_dQ", ("Hands",),          ("act2",), "Gloves tier list, Act 2"),
    ("_yHOS55NOjY", ("Hands",),          ("act3",), "Gloves tier list, Act 3"),
    ("K--zIJJJotI", ("Boots",),                    ALL, "Boots tier list"),
    ("Epsdb6XtHkI", ("Head",),           ("act1",), "Helmets tier list, Act 1"),
    ("CFRVuQvGsn8", ("Head",),           ("act2",), "Helmets tier list, Act 2"),
    ("MSlweFy-RmI", ("Head",),           ("act3",), "Helmets tier list, Act 3"),
    ("PyWb31wejBA", ("Amulets",),        ("act1",), "Amulets tier list, Act 1"),
    ("uomKPpHjEUo", ("Amulets",),        ("act2",), "Amulets tier list, Act 2"),
    ("23SPY6-dFfw", ("Amulets",),        ("act3",), "Amulets tier list, Act 3"),
    ("EoRrJ5kI2yk", ("Rings",),          ("act1",), "Rings tier list, Act 1"),
    ("xWeMvBJ6tl4", ("Rings",),          ("act2",), "Rings tier list, Act 2"),
    ("FqDSlLv9HkQ", ("Rings",),          ("act3",), "Rings tier list, Act 3"),
    ("otTGzNc4xXw", ("Ranged Weapons",),           ALL, "Bows tier list"),
    ("jeSeVkmqmuc", ("Melee Weapons",),            ALL, "Stabbing weapons tier list, part 1"),
    ("OVl0tHbmwK0", ("Melee Weapons",),            ALL, "Rogue weapons tier list, part 2"),
    ("seZJlJ9tvag", ("Melee Weapons",),            ALL, "Staves tier list"),
    ("nmFK4uJQfC8", ("Melee Weapons",),            ALL, "Simple weapons tier list"),
    ("GunWjIpdxb0", ("Melee Weapons",),            ALL, "Polearms tier list"),
    ("jwuRyGKRxXk", ("Melee Weapons",),            ALL, "Two-handed weapons tier list"),
    ("xt7Eq1-Bzd8", ("Melee Weapons",),            ALL, "One-handed weapons tier list"),
    ("6bdWlo4PgeA", ("Melee Weapons",),  ("act1",), "Versatile weapons tier list, Act 1"),
    ("hhbxLbwDenw", ("Melee Weapons",),  ("act2", "act3"), "Versatile weapons tier list, Acts 2-3"),
]

RANKED = [
    ("X2xy8yw6ZlM", "act1", "items",   "The 20 best items in Act 1"),
    ("yQLYmv9AQPg", "act2", "items",   "The 20 best items in Act 2"),
    ("JnWkqR-N0vM", "act3", "items",   "The 20 best items in Act 3"),
    ("FxGM0vWRtNY", "act1", "weapons", "The 20 best weapons in Act 1"),
    ("3R0lRrJwZjk", "act2", "weapons", "The 20 best weapons in Act 2"),
    ("NQ3Vt7hPBJU", "act3", "weapons", "The 20 best weapons in Act 3"),
]

LETTERS = ("s", "a", "b", "c", "d", "f")
# "as tier"/"at tier" are auto-caption slips for "a tier"; keep them but mark them.
# "dt tier" and "<letter> here" are two-token manglings of the same thing.
SLIPS = {"as": "A", "at": "A", "es": "A", "ay": "A", "be": "B", "see": "C", "sea": "C",
         "dt": "D", "bt": "B", "ct": "C", "st": "S"}
# The word "tier" also gets glued onto the letter, or mangled into something else
# entirely, which a letter-then-"tier" matcher cannot see at all. Real forms observed
# across these transcripts: dtier, ctier, btier, stier, deter, dier, deta, detail,
# CTI, DTI, and hyphenated c-tier / d-tier (the tokeniser keeps hyphens, so those
# never matched a table of un-hyphenated keys). Around 80 verdicts hide in here,
# concentrated in the spell lists. Several forms are also ordinary English words, so
# every match below is reported as uncertain and must be confirmed from the context.
GLUE_RE = re.compile(r"^([sabcdf])-?(?:tier|teer|tie|ti|ier|er|eer|eta|etail)$")
GLUE_EXTRA = {"deter": "D", "dier": "D", "deta": "D", "detail": "D", "detier": "D",
              "cer": "C", "ser": "C", "beer": "B", "deer": "D"}


def glued_letter(tok):
    """The tier letter hiding in a mangled single token, or None."""
    flat = tok.replace("-", "")
    if flat in GLUE_EXTRA:
        return GLUE_EXTRA[flat]
    match = GLUE_RE.match(tok)
    if match and len(tok) > 2:      # a bare "d" or "s" is not a verdict
        return match.group(1).upper()
    return None
# Number words the countdown lists use ("number 14", "at number three").
NUMBER_RE = re.compile(
    r"\bnumber\s+(twenty|nineteen|eighteen|seventeen|sixteen|fifteen|fourteen|thirteen|"
    r"twelve|eleven|ten|nine|eight|seven|six|five|four|three|two|one|\d{1,2})\b", re.I)


def read(vid):
    path = TRANSCRIPTS / (vid + ".md")
    if not path.exists():
        return None
    body = path.read_text(encoding="utf-8").split("## Transcript", 1)[-1]
    toks, stamps = [], []
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"^\[([0-9:]+)\]\s*(.*)$", line)
        stamp, text = (match.group(1), match.group(2)) if match else ("", line)
        for tok in re.findall(r"[a-z0-9'+\-]+", text.lower()):
            toks.append(tok)
            stamps.append(stamp)
    return toks, stamps


def verdicts(toks, stamps, before, after):
    """Every '<letter> tier' with the run-up and the tail, in transcript order."""
    out = []
    for i in range(len(toks) - 1):
        tok = toks[i]
        nxt = toks[i + 1]
        if nxt == "tier" and tok in LETTERS:
            letter, sure = tok.upper(), True
        elif nxt in ("tier", "here", "her") and tok in LETTERS:
            letter, sure = tok.upper(), nxt == "tier"
        elif nxt == "tier" and tok in SLIPS:
            letter, sure = SLIPS[tok], False
        elif glued_letter(tok):
            letter, sure = glued_letter(tok), False
        else:
            continue
        out.append({
            "tier": letter,
            "certain": sure,
            "at": stamps[i] if i < len(stamps) else "",
            "before": " ".join(toks[max(0, i - before):i]),
            "after": " ".join(toks[i + 2:i + 2 + after]),
        })
    return out


def countdowns(toks, stamps, before, after):
    """Every 'number N' announcement in a ranked countdown list."""
    text_positions = []
    joined = []
    for i, tok in enumerate(toks):
        joined.append(tok)
        text_positions.append(i)
    flat = " ".join(joined)
    out = []
    for match in NUMBER_RE.finditer(flat):
        # map char offset back to a token index
        idx = flat.count(" ", 0, match.start())
        out.append({
            "rank": match.group(1).lower(),
            "at": stamps[idx] if idx < len(stamps) else "",
            "before": " ".join(toks[max(0, idx - before // 3):idx]),
            "after": " ".join(toks[idx:idx + after]),
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="one video id")
    ap.add_argument("--slot", help="one canonical slot, e.g. Rings")
    ap.add_argument("--ranked", action="store_true", help="dump the top-20 countdowns instead")
    ap.add_argument("--before", type=int, default=55, help="words of run-up to show")
    ap.add_argument("--after", type=int, default=25, help="words after the verdict to show")
    ap.add_argument("--list", action="store_true", help="list the sources and stop")
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    table = RANKED if args.ranked else SOURCES
    # --source must work for any transcript, not just the gear lists catalogued above:
    # the spell and cantrip lists are not in either table, and silently printing nothing
    # for them reads exactly like "this video has no verdicts".
    if args.source and not any(row[0] == args.source for row in table):
        if not (TRANSCRIPTS / (args.source + ".md")).exists():
            sys.exit("no transcript for " + args.source)
        table = [(args.source, ("Any",), ALL, "Tier list " + args.source)]
    if args.list:
        for row in table:
            present = "*" if (TRANSCRIPTS / (row[0] + ".md")).exists() else " "
            print("%s %-11s %s" % (present, row[0], row[-1]))
        return 0

    lines = []
    total = 0
    for row in table:
        vid, label = row[0], row[-1]
        if args.source and vid != args.source:
            continue
        if not args.ranked and args.slot and args.slot not in row[1]:
            continue
        data = read(vid)
        if not data:
            print("  !! no transcript for " + vid, file=sys.stderr)
            continue
        toks, stamps = data
        found = (countdowns(toks, stamps, args.before, args.after) if args.ranked
                 else verdicts(toks, stamps, args.before, args.after))
        total += len(found)
        lines.append("")
        lines.append("=" * 78)
        lines.append("%s  [%s]  %d passage(s)" % (label, vid, len(found)))
        lines.append("=" * 78)
        for hit in found:
            head = ("#" + hit["rank"]) if args.ranked else (
                hit["tier"] + ("" if hit["certain"] else "?"))
            lines.append("")
            lines.append("--- %-4s @%s" % (head, hit["at"]))
            lines.append("    <<< " + hit["before"])
            lines.append("    >>> " + hit["after"])

    text = "\n".join(lines)
    if args.out == "-":
        sys.stdout.write(text + "\n")
    else:
        pathlib.Path(args.out).write_text(text + "\n", encoding="utf-8", newline="\n")
        print("wrote %s (%d passages)" % (args.out, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
