#!/usr/bin/env python3
"""Build `content/ratings.md` -- the Ratings tab's data -- from the ratings dataset.

The tab answers "what did the guide corpus say about every item it rated?", so it
reads the whole of `research/item_tiers.json`, not just the party's gear:

    research/slots/*.json  --(merge_slot_tiers.py)-->  research/item_tiers.json
                                                              |
                          this tool ------------------> content/ratings.md
                                                              |
                       apply_item_tiers.py ----> content/characters/*.md (badges)

Output shape, under a single `ratings` key:

    slots[]            one per item type, in the UI's slot order
      acts[]           act1 / act2 / act3 / all -- the list the rating came from
        items[]        already sorted: tier S..F, then top-20 rank, then name

An item carries `tier` (its letter within its slot) and/or `rank` (its placing on
that act's top-20 countdown); the two are independent and many items have both. A
top-20 entry whose slot list has not been read yet still appears, rank-only.

Regenerate after every merge; hand edits to `content/ratings.md` are overwritten.

    python tools/build_ratings_page.py --dry-run
    python tools/build_ratings_page.py
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys

DATA = pathlib.Path("research/item_tiers.json")
VOCAB = pathlib.Path("research/item_vocab.json")
OUT = pathlib.Path("content/ratings.md")

# The slot vocabulary and order `index.html` renders. Anything outside it lands in
# "Other" rather than silently disappearing.
SLOT_ORDER = [
    "Head", "Armour", "Hands", "Boots", "Amulets", "Cloaks", "Rings",
    "Melee Weapons", "Ranged Weapons", "Off-hand & Shields",
    "Elixirs", "Potions & Oils", "Other",
]
SLOT_ALIASES = {
    "ring": "Rings", "rings": "Rings", "amulet": "Amulets", "amulets": "Amulets",
    "helmet": "Head", "helmets": "Head", "head": "Head", "armor": "Armour",
    "armour": "Armour", "gloves": "Hands", "hands": "Hands", "boots": "Boots",
    "feet": "Boots", "cloak": "Cloaks", "cloaks": "Cloaks",
    "melee weapons": "Melee Weapons", "weapons": "Melee Weapons",
    "ranged weapons": "Ranged Weapons",
    "off-hand & shields": "Off-hand & Shields", "shields": "Off-hand & Shields",
    "elixirs": "Elixirs", "potions & oils": "Potions & Oils",
    "consumables": "Potions & Oils", "arrows": "Potions & Oils",
}
ACT_ORDER = ["act1", "act2", "act3", "all"]
ACT_LABELS = {"act1": "Act 1", "act2": "Act 2", "act3": "Act 3", "all": "All acts"}
# A few lists define an S+ (or A+) above their S; keep those ahead of the plain letter.
TIER_ORDER = ["S+", "S", "A+", "A", "B", "C", "D", "F"]


def norm(name):
    """Same normalisation as apply_item_tiers.py, so the two agree on identity."""
    text = (name or "").lower().replace("’", "'")
    text = re.sub(r"\(.*?\)", " ", text)
    text = re.sub(r"^the\s+", "", text.strip())
    text = re.sub(r"[^a-z0-9'+ ]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def canonical_slot(name):
    raw = str(name or "").strip()
    slot = SLOT_ALIASES.get(raw.lower(), raw)
    return slot if slot in SLOT_ORDER else "Other"


# ---------------------------------------------------------------- YAML emitter

SAFE = re.compile(r"^[A-Za-z][A-Za-z0-9 ()&'/.,+-]*$")


def scalar(value):
    if value is True or value is False:
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    # Quote unless the string is plainly safe; ": " and " #" would change the parse.
    if SAFE.match(text) and ": " not in text and " #" not in text:
        return text
    return "'" + text.replace("'", "''") + "'"


def emit(value, indent=0, out=None):
    """Minimal block-style YAML for dicts / lists / scalars. Keys are plain."""
    pad = " " * indent
    if out is None:
        out = []
    if isinstance(value, dict):
        for key, val in value.items():
            if val is None or val == "" or val == [] or val == {}:
                continue
            if isinstance(val, (dict, list)):
                out.append("%s%s:" % (pad, key))
                emit(val, indent + 2, out)
            else:
                out.append("%s%s: %s" % (pad, key, scalar(val)))
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)):
                rows = []
                emit(item, indent + 2, rows)
                if not rows:
                    continue
                # First key sits on the dash line, the rest line up under it.
                out.append("%s- %s" % (pad, rows[0].strip()))
                out.extend(rows[1:])
            else:
                out.append("%s- %s" % (pad, scalar(item)))
    else:
        out.append("%s%s" % (pad, scalar(value)))
    return out


# ---------------------------------------------------------------- assembly


def rank_label(rank):
    return "HM" if str(rank).upper() == "HM" else "#%s" % rank


def tier_key(row):
    tier = row.get("tier")
    return TIER_ORDER.index(tier) if tier in TIER_ORDER else len(TIER_ORDER)


def rank_key(row):
    """Ranked items lead their tier group; HM sits behind every number."""
    raw = str(row.get("rank", "")).lstrip("#")
    if not raw:
        return 999
    return 900 if raw.upper() == "HM" else int(raw)


def build(data):
    sources = data.get("sources") or {}
    vocab_slot = {}
    if VOCAB.is_file():
        for slot, names in json.loads(VOCAB.read_text(encoding="utf-8")).items():
            for name in names:
                vocab_slot.setdefault(norm(name), canonical_slot(slot))

    # (slot, act) -> [row], plus an index so a top-20 rank can find its tier row.
    buckets = collections.defaultdict(list)
    by_item = collections.defaultdict(list)
    for entry in data.get("tiers") or []:
        slot = canonical_slot(entry.get("slot"))
        act = entry.get("rated_in") or "all"
        if act not in ACT_LABELS:
            act = "all"
        row = {
            "item": entry["item"],
            "tier": str(entry.get("tier", "")).upper(),
            "verdict": entry.get("verdict", ""),
            "source": entry.get("source", ""),
            "at": entry.get("at", ""),
        }
        buckets[(slot, act)].append(row)
        by_item[norm(entry["item"])].append((slot, act, row))

    # A rank belongs on the item's own row when the two lists agree on the act (an
    # "all acts" slot list covers every act). Otherwise it stands as its own entry,
    # which is how an item whose slot list is unread still shows up.
    rank_only = 0
    for entry in data.get("ranked") or []:
        key = norm(entry["item"])
        act = entry.get("act") or "all"
        rows = by_item.get(key) or []
        target = next((row for _, a, row in rows if a == act), None)
        if target is None:
            target = next((row for _, a, row in rows if a == "all"), None)
        if target is None:
            slot = vocab_slot.get(key) or (rows[0][0] if rows else "Other")
            target = {"item": entry["item"], "verdict": entry.get("verdict", ""),
                      "source": entry.get("source", ""), "at": entry.get("at", "")}
            buckets[(slot, act)].append(target)
            by_item[key].append((slot, act, target))
            rank_only += 1
        target["rank"] = rank_label(entry["rank"])
        target["of"] = entry.get("of", 20)
        # The countdown is its own list, so name it even when a letter came first.
        target["rank_source"] = entry.get("source", "")

    slots = []
    for slot in SLOT_ORDER:
        acts = []
        for act in ACT_ORDER:
            rows = buckets.get((slot, act))
            if not rows:
                continue
            rows.sort(key=lambda row: (tier_key(row), rank_key(row), norm(row["item"])))
            acts.append({
                "act": act,
                "label": ACT_LABELS[act],
                "count": len(rows),
                "lists": sorted({row["source"] for row in rows if row.get("source")}),
                "items": rows,
            })
        if acts:
            slots.append({
                "slot": slot,
                "count": sum(act["count"] for act in acts),
                "acts": acts,
            })

    all_rows = [row for rows in buckets.values() for row in rows]
    used = sorted({row["source"] for row in all_rows if row.get("source")}
                  | {row["rank_source"] for row in all_rows if row.get("rank_source")})
    source_rows = []
    for vid in used:
        meta = sources.get(vid) or {}
        slot = meta.get("slot")
        source_rows.append({
            "id": vid,
            "title": meta.get("title", vid),
            "slot": canonical_slot(slot) if slot and slot != "any" else "",
            "rated_in": meta.get("rated_in", ""),
            "kind": meta.get("kind", ""),
            "ratings": sum(1 for row in all_rows
                           if vid in (row.get("source"), row.get("rank_source"))),
        })

    return {
        "about": "Every item rating read out of the guide corpus, by item type and by "
                 "the act whose list rated it. A letter is the item's tier inside its "
                 "own slot; a #number is its placing on that act's top-20 countdown.",
        "generated_from": str(DATA).replace("\\", "/"),
        "generated_by": "tools/build_ratings_page.py",
        "channel": data.get("channel", ""),
        "playlist": data.get("playlist", ""),
        "note_on_acts": data.get("note_on_acts", ""),
        "totals": {
            "entries": len(all_rows),
            "items": len({norm(row["item"]) for row in all_rows}),
            "lists": len(source_rows),
            "ranked_only": rank_only,
        },
        "tier_scale": [{"tier": letter, "what": text}
                       for letter, text in (data.get("tier_scale") or {}).items()],
        "sources": source_rows,
        "coverage": {
            "complete_note": (data.get("complete_slots") or {}).get("note", ""),
            "complete_lists": (data.get("complete_slots") or {}).get("lists") or [],
            "not_yet_read": data.get("not_yet_read") or [],
            "unresolved_note": (data.get("unresolved") or {}).get("note", ""),
            "unresolved": (data.get("unresolved") or {}).get("items") or [],
        },
        "slots": slots,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not DATA.is_file():
        sys.exit("no " + str(DATA))
    ratings = build(json.loads(DATA.read_text(encoding="utf-8")))

    lines = ["---",
             "# GENERATED by tools/build_ratings_page.py from research/item_tiers.json.",
             "# Edit the dataset and re-run; hand edits here are overwritten."]
    lines.extend(emit({"ratings": ratings}))
    lines.append("---")
    lines.append("")
    text = "\n".join(lines) + "\n"

    print("%d ratings on %d items across %d item types, %d lists (%d rank-only)"
          % (ratings["totals"]["entries"], ratings["totals"]["items"],
             len(ratings["slots"]), ratings["totals"]["lists"],
             ratings["totals"]["ranked_only"]))
    for slot in ratings["slots"]:
        print("  %-20s %3d  (%s)" % (slot["slot"], slot["count"],
                                     ", ".join("%s %d" % (act["label"], act["count"])
                                               for act in slot["acts"])))
    if args.dry_run:
        print("\n(dry run, nothing written)")
    else:
        OUT.write_text(text, encoding="utf-8", newline="\n")
        print("\nwrote %s (%.1f KB)" % (OUT, len(text) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
