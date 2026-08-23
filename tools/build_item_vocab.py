#!/usr/bin/env python3
"""Build `research/item_vocab.json`: every bg3.wiki equipment page, grouped by slot.

The tier-list scanner needs to know about ALL items in a slot, not just the party's.
The narrator walks a slot's items in order and delivers a verdict after each one, so a
verdict can only be attributed correctly if the scanner can see where the *next* item
starts -- including items nobody in the party uses.

Source is the bg3kb scrape (`bg3kb/data/chunks.jsonl`), read once and cached.

    python tools/build_item_vocab.py
"""
from __future__ import annotations

import json
import io
import pathlib
import sys

CHUNKS = pathlib.Path("bg3kb/data/chunks.jsonl")
OUT = pathlib.Path("research/item_vocab.json")

# Canonical slot -> the bg3.wiki categories that populate it.
SLOT_CATEGORIES = {
    "Head": ["Helmets"],
    "Rings": ["Rings"],
    "Hands": ["Gloves"],
    "Amulets": ["Amulets"],
    "Boots": ["Boots"],
    "Off-hand & Shields": ["Shields"],
    "Cloaks": ["Cloaks"],
    "Armour": ["Light Armour", "Medium Armour", "Heavy Armour", "Clothing", "Camp Clothing"],
    "Melee Weapons": ["Melee weapons", "Quarterstaves", "Simple weapons", "Martial weapons"],
    "Ranged Weapons": ["Ranged weapons"],
    "Elixirs": ["Elixirs"],
    "Potions & Oils": ["Potions", "Coatings", "Grenades", "Arrows"],
}

# Wiki pages in those categories that are mechanics or lists, not individual items.
SKIP_EXACT = {
    "Equipment", "Weapons", "Armour", "Shields", "Rings", "Amulets", "Cloaks", "Gloves",
    "Boots", "Helmets", "Potions", "Elixirs", "Arrows", "Coatings", "Grenades",
    "Clothing", "Camp Clothing", "Light Armour", "Medium Armour", "Heavy Armour",
    "Melee weapons", "Ranged weapons", "Simple weapons", "Martial weapons",
    "Quarterstaves", "Weapon types", "Lists of equipment", "Lists of weapons",
}


def main() -> int:
    if not CHUNKS.exists():
        sys.exit("missing " + str(CHUNKS) + " - run the bg3kb pipeline first")
    wanted = {}
    for slot, cats in SLOT_CATEGORIES.items():
        for cat in cats:
            wanted[cat] = slot

    by_slot: dict[str, set] = {slot: set() for slot in SLOT_CATEGORIES}
    seen = set()
    with io.open(CHUNKS, encoding="utf-8") as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            title = row.get("page_title")
            if not title or title in seen:
                continue
            seen.add(title)
            if title in SKIP_EXACT or title.startswith("List of"):
                continue
            for cat in row.get("categories") or []:
                slot = wanted.get(cat)
                if slot:
                    by_slot[slot].add(title)

    out = {slot: sorted(names) for slot, names in by_slot.items()}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8", newline="\n")
    total = sum(len(v) for v in out.values())
    print("wrote %s: %d item names across %d slots" % (OUT, total, len(out)))
    for slot in sorted(out):
        print("  %-20s %4d" % (slot, len(out[slot])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
