#!/usr/bin/env python3
"""Extract spoken tier verdicts for gear from the tier-list transcripts.

The transcripts are YouTube auto-captions, so item names arrive garbled ("Marco HH
gear" for Markoheshkir, "Mel's first staff" for Melf's First Staff) and verdicts are
spoken rather than tabulated. The narrator's structure is consistent, though: discuss
one item, deliver its tier, move to the next. So this scanner:

1. loads the full slot vocabulary from `research/item_vocab.json` (every bg3.wiki item
   in the slot, not just the party's -- otherwise a verdict lands on the wrong item
   whenever an unowned item is discussed in between),
2. fuzzy-locates every vocabulary name in the transcript,
3. splits the transcript at each spoken tier verdict, and attributes each verdict to
   the item that dominates the segment leading up to it.

Output is CANDIDATES. Attribution is a heuristic and it cannot tell "I'd rate this A"
from "this is worse than the A tier items", so ratings must be confirmed against the
quoted context before they land in `research/item_tiers.json`.

    python tools/scan_item_tiers.py --source seZJlJ9tvag
    python tools/scan_item_tiers.py --party-only --out research/tier_candidates.txt
    python tools/scan_item_tiers.py --json --out research/tier_candidates.json
"""
from __future__ import annotations

import argparse
import difflib
import json
import pathlib
import re
import sys

import yaml

CHARACTERS = pathlib.Path("content/characters")
TRANSCRIPTS = pathlib.Path("video_transcripts")
VOCAB = pathlib.Path("research/item_vocab.json")

ALL = ("act1", "act2", "act3")

# Which playlist video rates which slot, and which acts it covers. Transcribed from
# the video titles in playlist PLgTVc5Jd2rrLPuc3vE6XqK65QQboFfolP.
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

# The ranked "top 20" lists publish a rank, not a letter tier, so they are scanned
# for countdown positions instead. Slot is unrestricted: they mix every slot.
RANKED = [
    ("X2xy8yw6ZlM", "act1", "items",   "The 20 best items in Act 1"),
    ("yQLYmv9AQPg", "act2", "items",   "The 20 best items in Act 2"),
    ("JnWkqR-N0vM", "act3", "items",   "The 20 best items in Act 3"),
    ("FxGM0vWRtNY", "act1", "weapons", "The 20 best weapons in Act 1"),
    ("3R0lRrJwZjk", "act2", "weapons", "The 20 best weapons in Act 2"),
    ("NQ3Vt7hPBJU", "act3", "weapons", "The 20 best weapons in Act 3"),
]

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

TIER_RE = re.compile(r"\b([sabcdf])[\s\-]?tier\b", re.I)
NOT_GEAR = re.compile(
    r"^(?:head|glove|boot|neck|second|first|empty|no |none|nothing|early |"
    r"resonance stone aura)", re.I)
STOP = {"of", "the", "a", "an", "and", "s", "in", "to", "for"}


def words_of(text):
    return re.findall(r"[a-z0-9'+]+", text.lower())


def load_party():
    """Every itemization entry with its canonical slot; progression rows excluded."""
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
                        out.append({"char": data["nickname"], "act": act, "slot": slot,
                                    "id": item.get("id"), "name": name})
    return out


def read_transcript(vid):
    """(tokens, token->timestamp, plain text) or None when the file is absent."""
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
        for tok in words_of(text):
            toks.append(tok)
            stamps.append(stamp)
    return toks, stamps


def build_index(toks):
    """token position lookup keyed by first letter, to keep fuzzy search cheap."""
    index = {}
    for i, tok in enumerate(toks):
        index.setdefault(tok[0], []).append(i)
    return index


def find_mentions(toks, index, names, threshold=0.78):
    """[(position, canonical name, score)] for every fuzzy mention of any name."""
    mentions = []
    for name in names:
        name_toks = [t for t in words_of(name)]
        if not name_toks:
            continue
        keys = [t for t in name_toks if t not in STOP and len(t) >= 4] or name_toks
        key = max(keys, key=len)
        target = " ".join(name_toks)
        width = len(name_toks)
        candidates = set()
        for start in index.get(key[0], ()):
            tok = toks[start]
            if abs(len(tok) - len(key)) > max(3, len(key) // 2):
                continue
            if difflib.SequenceMatcher(None, tok, key).ratio() < 0.74:
                continue
            offset = name_toks.index(key) if key in name_toks else 0
            candidates.add(max(0, start - offset))
        for start in candidates:
            best = 0.0
            for w in (max(1, width - 1), width, width + 1):
                cand = " ".join(toks[start:start + w])
                score = difflib.SequenceMatcher(None, cand, target).ratio()
                best = max(best, score)
            if best >= threshold:
                mentions.append((start, name, round(best, 2)))
    mentions.sort()
    return mentions


def attribute(toks, stamps, mentions, lookback=260):
    """Tie each spoken verdict to the item that dominates the run-up to it.

    The narrator repeats an item's name while discussing it, so the item with the
    most mentions closest to the verdict is the one being rated. Weighting by
    proximity keeps a passing reference to some other item from winning.
    """
    text = " ".join(toks)
    # Verdict positions in token space: walk tokens looking for "<letter> tier".
    verdicts = []
    for i in range(len(toks) - 1):
        if toks[i + 1] == "tier" and toks[i] in ("s", "a", "b", "c", "d", "f"):
            verdicts.append((i, toks[i].upper()))
        elif toks[i + 1] == "tier" and toks[i] in ("as", "at", "es"):
            # auto-caption slips: "as tier"/"at tier" are almost always "a tier"
            verdicts.append((i, "A"))
    out = []
    prev = 0
    for pos, letter in verdicts:
        window_start = max(prev, pos - lookback)
        scored = {}
        for mpos, name, score in mentions:
            if window_start <= mpos <= pos:
                weight = score * (1.0 + 3.0 * (mpos - window_start) / max(1, pos - window_start))
                scored[name] = scored.get(name, 0.0) + weight
        if scored:
            winner = max(scored.items(), key=lambda kv: kv[1])
            runner = sorted(scored.items(), key=lambda kv: -kv[1])[1:2]
            quote = " ".join(toks[max(0, pos - 70):pos + 12])
            out.append({
                "item": winner[0],
                "tier": letter,
                "confidence": round(winner[1] / (winner[1] + (runner[0][1] if runner else 0.0)), 2),
                "runner_up": runner[0][0] if runner else None,
                "at": stamps[pos] if pos < len(stamps) else "",
                "quote": quote,
            })
        prev = pos
    return out


def dedupe(rows):
    """One verdict per item: the highest-confidence mention wins."""
    best = {}
    for row in rows:
        key = row["item"]
        if key not in best or row["confidence"] > best[key]["confidence"]:
            best[key] = row
    return sorted(best.values(), key=lambda r: r["item"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="limit to one video id")
    ap.add_argument("--party-only", action="store_true",
                    help="report only items the party's itemization names")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    if not VOCAB.exists():
        sys.exit("missing " + str(VOCAB) + " - run tools/build_item_vocab.py first")
    vocab = json.loads(VOCAB.read_text(encoding="utf-8"))
    party = load_party()
    party_names = {p["name"].lower() for p in party}
    party_names |= {re.sub(r"^the\s+", "", n) for n in list(party_names)}

    report = []
    for vid, slots, acts, label in SOURCES:
        if args.source and vid != args.source:
            continue
        read = read_transcript(vid)
        if not read:
            print("  !! no transcript for " + vid, file=sys.stderr)
            continue
        toks, stamps = read
        names = sorted({n for slot in slots for n in vocab.get(slot, [])})
        index = build_index(toks)
        mentions = find_mentions(toks, index, names)
        rows = dedupe(attribute(toks, stamps, mentions))
        if args.party_only:
            rows = [r for r in rows
                    if r["item"].lower() in party_names
                    or re.sub(r"^the\s+", "", r["item"].lower()) in party_names]
        report.append({"source": vid, "label": label, "slots": list(slots),
                       "acts": list(acts), "vocab": len(names),
                       "mentions": len(mentions), "ratings": rows})

    if args.json:
        text = json.dumps(report, indent=1, ensure_ascii=False)
    else:
        lines = []
        for block in report:
            lines.append("")
            lines.append("=" * 78)
            lines.append("%s  [%s]  vocab=%d mentions=%d rated=%d"
                         % (block["label"], block["source"], block["vocab"],
                            block["mentions"], len(block["ratings"])))
            lines.append("=" * 78)
            for row in block["ratings"]:
                flag = " " if row["confidence"] >= 0.75 else "?"
                lines.append("%s %-2s %-34s conf=%.2f @%s%s"
                             % (flag, row["tier"], row["item"], row["confidence"],
                                row["at"],
                                ("  (vs " + row["runner_up"] + ")") if row["runner_up"] else ""))
                lines.append("      ..." + row["quote"])
        text = "\n".join(lines)

    if args.out == "-":
        sys.stdout.write(text + "\n")
    else:
        pathlib.Path(args.out).write_text(text + "\n", encoding="utf-8", newline="\n")
        print("wrote " + args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
