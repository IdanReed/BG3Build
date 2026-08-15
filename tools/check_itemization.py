#!/usr/bin/env python3
"""Check that every character's itemization covers every equipment slot in every act.

Mirrors the slot vocabulary in index.html (ITEM_SLOT_ALIASES / ITEM_SLOT_ROWS) so a
content slot value that the UI would silently bucket into "Other" is reported here
instead. Run from the repository root:

    python3 tools/check_itemization.py
"""
from __future__ import annotations

import pathlib
import re
import sys

CHARACTERS = pathlib.Path("content/characters")

# index.html ITEM_SLOT_ALIASES, transcribed.
ALIASES = {
    "head": "Head", "helmet": "Head", "helm": "Head", "circlet": "Head", "hat": "Head",
    "armour": "Armour", "armor": "Armour", "chest": "Armour", "body": "Armour",
    "robes": "Armour",
    "hands": "Hands", "gloves": "Hands", "bracers": "Hands", "gauntlets": "Hands",
    "rings": "Rings", "ring": "Rings",
    "feet": "Boots", "boots": "Boots", "shoes": "Boots",
    "amulets": "Amulets", "amulet": "Amulets", "neck": "Amulets", "necklace": "Amulets",
    "cloaks": "Cloaks", "cloak": "Cloaks", "back": "Cloaks",
    "weapons": "Melee Weapons", "weapon": "Melee Weapons", "melee": "Melee Weapons",
    "melee weapons": "Melee Weapons", "main hand": "Melee Weapons",
    "ranged weapons": "Ranged Weapons", "ranged": "Ranged Weapons",
    "ranged weapon": "Ranged Weapons",
    "off-hand": "Off-hand & Shields", "off hand": "Off-hand & Shields",
    "offhand": "Off-hand & Shields",
    "shields": "Off-hand & Shields", "shield": "Off-hand & Shields",
    "elixirs": "Elixirs", "elixir": "Elixirs",
    "consumables": "Potions & Oils", "consumable": "Potions & Oils",
    "potions": "Potions & Oils", "potion": "Potions & Oils", "oils": "Potions & Oils",
    "coatings": "Potions & Oils", "arrows": "Potions & Oils",
    "other": "Other", "misc": "Other", "party aura": "Other",
}

# The slots a complete loadout must name. "Off-hand & Shields" is excluded because a
# two-handed or unarmed build legitimately leaves it empty; the guide says so in prose.
REQUIRED = [
    "Head", "Armour", "Hands", "Rings", "Boots", "Amulets", "Cloaks",
    "Melee Weapons", "Ranged Weapons",
]

ACTS = ["act1", "act2", "act3"]

RANGED_WORDS = ["bow", "crossbow", "sling", "dart", "javelin", "ranged"]

ITEM_RE = re.compile(r"^    - id: (?P<id>\S+)\s*$")
SLOT_RE = re.compile(r"^      slot: (?P<slot>.+?)\s*$")
NAME_RE = re.compile(r"^      item: (?P<item>.+?)\s*$")
ACT_RE = re.compile(r"^    (?P<act>act[123]|final):\s*$")
ITEMIZATION_RE = re.compile(r"^  itemization:\s*$")
TOP_RE = re.compile(r"^  [a-z_]+:")


def parse(path: pathlib.Path):
    """Return {act: [(id, item, canonical_slot, raw_slot)]} for one character file."""
    acts: dict[str, list] = {}
    in_itemization = False
    act = None
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if ITEMIZATION_RE.match(line):
            in_itemization = True
            continue
        if not in_itemization:
            continue
        if TOP_RE.match(line) and not ITEMIZATION_RE.match(line):
            break
        m = ACT_RE.match(line)
        if m:
            act = m.group("act")
            acts.setdefault(act, [])
            cur = None
            continue
        m = ITEM_RE.match(line)
        if m and act:
            cur = {"id": m.group("id"), "item": "", "slot": ""}
            acts[act].append(cur)
            continue
        if cur is None:
            continue
        m = NAME_RE.match(line)
        if m:
            cur["item"] = m.group("item").strip("'\"")
        m = SLOT_RE.match(line)
        if m:
            cur["slot"] = m.group("slot").strip("'\"")
    return acts


def main() -> int:
    problems = 0
    for path in sorted(CHARACTERS.glob("*.md")):
        acts = parse(path)
        name = path.stem
        print(f"\n=== {name} ===")
        cumulative: dict[str, list[str]] = {}
        for act in ACTS:
            entries = acts.get(act, [])
            filled: dict[str, list[str]] = {}
            for e in entries:
                raw = e["slot"].lower()
                canon = ALIASES.get(raw)
                if canon is None:
                    print(f"  !! {act} {e['id']}: unrecognised slot {e['slot']!r} "
                          f"— the UI will bucket this under 'Other'")
                    problems += 1
                    continue
                # index.html re-buckets a "weapons" entry whose name reads as ranged,
                # and an oils entry whose name reads as an elixir. Mirror both.
                text = (e["item"] or e["id"]).lower()
                if canon == "Melee Weapons" and any(w in text for w in RANGED_WORDS):
                    canon = "Ranged Weapons"
                if canon == "Potions & Oils" and "elixir" in text:
                    canon = "Elixirs"
                filled.setdefault(canon, []).append(e["item"] or e["id"])
                cumulative.setdefault(canon, []).append(f"{act}:{e['item'] or e['id']}")
            missing = [s for s in REQUIRED if s not in cumulative]
            if missing:
                print(f"  {act}: MISSING {', '.join(missing)}")
                problems += len(missing)
            else:
                print(f"  {act}: all {len(REQUIRED)} slots covered "
                      f"({len(entries)} entries, {len(filled)} slots touched)")
        rings = len([x for x in cumulative.get("Rings", [])])
        if rings < 2:
            print(f"  !! only {rings} ring entries across all acts; two ring slots exist")
            problems += 1
        if "final" not in acts:
            print("  !! no 'final' loadout tab")
            problems += 1
    print(f"\n{'OK' if not problems else str(problems) + ' problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
