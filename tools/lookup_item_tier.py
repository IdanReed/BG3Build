#!/usr/bin/env python3
"""Print the passage where a tier list discusses a named item, up to its verdict.

Companion to `tools/dump_tier_verdicts.py`. That tool walks a whole list verdict by
verdict; this one goes straight to the items the party actually uses.

It leans on a habit the narrator has: the item's name is said twice in a row when it is
introduced ("the ring of free action the ring of free action basically gives you..."),
which locates the start of its discussion far more reliably than a bare mention, since
bare mentions also occur in intros and in comparisons against other items. From that
introduction the passage runs to the first spoken "<letter> tier", which is that item's
verdict.

THE LETTER IS A HINT, NOT AN ANSWER. Measured against hand-read ground truth it scored
9/9 on the Act 1 rings but only 1/5 on the staves, because the narrator's other phrasing
-- "D tier for the rain dancer. The Staff of Arcane Blessing has no enhancement bonus..."
-- puts the NEXT item's name just after the previous item's verdict, so the next item
steals it. Resolving that needs every verdict in the list assigned at once, which is
what `tools/dump_tier_verdicts.py` plus a reader does. Use this tool to find where an
item is discussed; confirm the letter from the printed passage.

    python tools/lookup_item_tier.py --source EoRrJ5kI2yk --slot Rings
    python tools/lookup_item_tier.py --source K--zIJJJotI --item "Boots of Speed"
"""
from __future__ import annotations

import argparse
import difflib
import pathlib
import re
import sys

import yaml

CHARACTERS = pathlib.Path("content/characters")
TRANSCRIPTS = pathlib.Path("resources/videos/transcripts")

LETTERS = ("s", "a", "b", "c", "d", "f")
NOT_GEAR = re.compile(
    r"^(?:head|glove|boot|neck|second|first|empty|no |none|nothing|early |"
    r"resonance stone aura)", re.I)
ALIASES = {
    "head": "Head", "helmet": "Head", "helm": "Head", "circlet": "Head", "hat": "Head",
    "armour": "Armour", "armor": "Armour", "chest": "Armour", "body": "Armour",
    "robes": "Armour",
    "hands": "Hands", "gloves": "Hands", "bracers": "Hands", "gauntlets": "Hands",
    "rings": "Rings", "ring": "Rings", "ring 1": "Rings", "ring 2": "Rings",
    "feet": "Boots", "boots": "Boots", "shoes": "Boots",
    "amulets": "Amulets", "amulet": "Amulets", "neck": "Amulets", "necklace": "Amulets",
    "cloaks": "Cloaks", "cloak": "Cloaks", "back": "Cloaks",
    "weapons": "Melee Weapons", "weapon": "Melee Weapons", "melee": "Melee Weapons",
    "ranged weapons": "Ranged Weapons", "ranged": "Ranged Weapons",
    "off-hand": "Off-hand & Shields", "shields": "Off-hand & Shields",
    "shield": "Off-hand & Shields",
    "elixirs": "Elixirs", "elixir": "Elixirs",
    "consumables": "Potions & Oils", "potions": "Potions & Oils", "oils": "Potions & Oils",
    "coatings": "Potions & Oils", "arrows": "Potions & Oils",
    "other": "Other", "misc": "Other", "party aura": "Other",
}
RANGED_WORDS = ("bow", "crossbow", "sling", "dart", "javelin", "ranged")


def party_items():
    out = []
    for path in sorted(CHARACTERS.glob("*.md")):
        text = path.read_text(encoding="utf-8-sig").lstrip()
        data = yaml.safe_load(text[3:text.index("\n---", 3)])
        builds = data["builds"]
        for build in (builds if isinstance(builds, list) else [builds]):
            if not isinstance(build, dict):
                continue
            for act, entries in (build.get("itemization") or {}).items():
                if act == "progression" or not isinstance(entries, list):
                    continue
                for entry in entries:
                    if not isinstance(entry, dict):
                        continue
                    for item in [entry] + list(entry.get("options") or []):
                        if not isinstance(item, dict):
                            continue
                        raw = item.get("wiki") if isinstance(item.get("wiki"), str) else item.get("item")
                        name = re.sub(r"\(.*?\)", " ", raw or "")
                        name = re.sub(r"\s{2,}", " ", name).strip()
                        if not name or NOT_GEAR.match(name):
                            continue
                        declared = str(entry.get("slot") or "").strip().lower()
                        slot = ALIASES.get(declared, "Other")
                        low = name.lower()
                        if slot == "Melee Weapons" and any(w in low for w in RANGED_WORDS):
                            slot = "Ranged Weapons"
                        if slot == "Potions & Oils" and "elixir" in low:
                            slot = "Elixirs"
                        out.append({"act": act, "slot": slot, "char": data["nickname"],
                                    "name": name})
    return out


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
        for tok in re.findall(r"[a-z0-9']+", text.lower()):
            toks.append(tok)
            stamps.append(stamp)
    return toks, stamps


def mentions_of(toks, name, threshold=0.80):
    want = re.findall(r"[a-z0-9']+", name.lower())
    if not want:
        return []
    target = " ".join(want)
    width = len(want)
    hits = []
    for i in range(len(toks) - width + 1):
        for w in (max(1, width - 1), width, width + 1):
            score = difflib.SequenceMatcher(None, " ".join(toks[i:i + w]), target).ratio()
            if score >= threshold:
                hits.append((i, round(score, 2)))
                break
    return hits


def introduction(hits, gap=14):
    """The mention said twice in quick succession, i.e. where discussion starts."""
    for j in range(len(hits) - 1):
        if 0 < hits[j + 1][0] - hits[j][0] <= gap:
            return hits[j][0]
    return hits[0][0] if hits else None


def all_verdicts(toks):
    return [(i, toks[i].upper()) for i in range(len(toks) - 1)
            if toks[i + 1] == "tier" and toks[i] in LETTERS]


def verdict_for(toks, hits, name, lead=80, trail=26, strict=0.86):
    """The verdict this item's own name sits next to.

    Both phrasings the narrator uses put the name adjacent to the letter: "<item> ...
    so I'll give it B tier", and "D tier for the <item>". Requiring adjacency is what
    stops an item that is merely referenced in passing -- an Act 3 ring named while
    an Act 1 ring is being rated -- from stealing that verdict.
    """
    # A loose match is fine for locating an item's discussion, but not for claiming a
    # verdict: "ring of free action" scores well enough against "ring of protection" to
    # steal its rating. Adjacency therefore demands a near-exact mention.
    width = len(re.findall(r"[a-z0-9']+", name.lower()))
    positions = [h[0] for h in hits if h[1] >= strict]
    best = None
    for pos, letter in all_verdicts(toks):
        for mention in positions:
            if pos - lead <= mention <= pos + trail:
                distance = abs(pos - mention)
                if best is None or distance < best[2]:
                    heard = " ".join(toks[mention:mention + width])
                    best = (pos, letter, distance, mention, heard)
    # An item actually being rated gets talked about repeatedly. A couple of passing
    # references far from the letter means the verdict belongs to whatever is being
    # rated, and this item was only named in comparison to it.
    if best and len(hits) < 5 and best[2] > 25:
        return None
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--slot", help="pull every party item in this canonical slot")
    ap.add_argument("--act", help="restrict to one act key")
    ap.add_argument("--item", action="append", default=[], help="an explicit item name")
    ap.add_argument("--words", type=int, default=95, help="words of passage to print")
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    data = read(args.source)
    if not data:
        sys.exit("no transcript for " + args.source)
    toks, stamps = data

    names = list(dict.fromkeys(args.item))
    if args.slot:
        for row in party_items():
            if row["slot"] == args.slot and (not args.act or row["act"] == args.act):
                if row["name"] not in names:
                    names.append(row["name"])
    if not names:
        sys.exit("nothing to look up: pass --slot or --item")

    lines = []
    for name in sorted(names):
        hits = mentions_of(toks, name)
        if not hits:
            lines.append("")
            lines.append("## %s -- NOT MENTIONED" % name)
            continue
        found = verdict_for(toks, hits, name)
        if not found:
            lines.append("")
            lines.append("## %s   mentions=%d  -- NO VERDICT BESIDE A MENTION "
                         "(probably discussed but not rated in this list)" % (name, len(hits)))
            start = introduction(hits)
            lines.append("   " + " ".join(toks[start:start + 40]))
            continue
        pos, letter, distance, mention, heard = found
        lines.append("")
        lines.append("## %s   mentions=%d  %s @%s  (heard %r, %d words away)"
                     % (name, len(hits), letter, stamps[pos] if pos < len(stamps) else "?",
                        heard, distance))
        lo = max(0, min(mention, pos) - 18)
        hi = min(len(toks), max(mention, pos) + 22)
        lines.append("   " + " ".join(toks[lo:hi]))

    text = "\n".join(lines)
    if args.out == "-":
        sys.stdout.write(text + "\n")
    else:
        pathlib.Path(args.out).write_text(text + "\n", encoding="utf-8", newline="\n")
        print("wrote " + args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
