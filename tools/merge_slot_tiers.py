#!/usr/bin/env python3
"""Fold the per-video tables in `resources/tiers/slots/*.json` into `resources/tiers/item_tiers.json`.

Each slot file is one tier-list video read end to end, in the shape described by
`docs/extraction-brief.md`. This merges them into the single dataset the content
applier reads, and reports anything that needs a human look:

- a slot file whose item count plus unassigned count does not match the verdicts it saw
  (something was missed),
- the same item rated twice from one video (an attribution slipped),
- an item rated differently by two videos, which is legitimate when the two rate it in
  different acts or categories, but worth eyeballing.

    python tools/merge_slot_tiers.py --dry-run
    python tools/merge_slot_tiers.py
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

DATA = pathlib.Path("resources/tiers/item_tiers.json")
SLOTS = pathlib.Path("resources/tiers/slots")
LETTERS = {"S+", "S", "A+", "A", "B", "C", "D", "F"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not SLOTS.is_dir():
        sys.exit("no " + str(SLOTS))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    by_key = {(row["item"], row["source"]): row for row in data["tiers"]}
    existing = set(by_key)

    problems, notes, overrides, added, complete = [], [], [], 0, []
    for path in sorted(SLOTS.glob("*.json")):
        try:
            block = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as err:
            problems.append("%s: unreadable (%s)" % (path.name, err))
            continue
        vid = block.get("source") or path.stem
        items = block.get("items") or []
        unassigned = block.get("unassigned") or []
        seen = block.get("verdicts_in_transcript")

        if seen is not None and len(items) + len(unassigned) != seen:
            # One spoken verdict can rate several items ("D tier for all four of these"),
            # so a mismatch is only suspicious when the file does not explain itself.
            excuse = block.get("count_note") or block.get("note")
            (notes if excuse else problems).append(
                "%s: %d rated + %d unassigned vs %d verdicts%s"
                % (vid, len(items), len(unassigned), seen,
                   ("  (" + str(excuse)[:80] + ")") if excuse else ""))

        dupes = [k for k, n in collections.Counter(
            row.get("item") for row in items).items() if n > 1]
        if dupes:
            problems.append("%s: rated twice: %s" % (vid, ", ".join(sorted(map(str, dupes)))))

        for row in items:
            name, tier = row.get("item"), str(row.get("tier", "")).upper()
            if not name or tier not in LETTERS:
                problems.append("%s: bad row %r" % (vid, row))
                continue
            prior = by_key.get((name, vid))
            if prior is not None:
                if prior["tier"] != tier:
                    overrides.append("%-34s %s -> %s  [%s]"
                                     % (name, prior["tier"], tier, vid))
                    prior["tier"] = tier
                    prior["verdict"] = row.get("verdict", prior.get("verdict", ""))
                    prior["at"] = row.get("at", prior.get("at", ""))
                continue
            entry = {
                "item": name,
                "slot": row.get("slot") or block.get("slot") or "Other",
                "rated_in": row.get("act") or block.get("rated_in") or "all",
                "tier": tier,
                "source": vid,
                "at": row.get("at", ""),
                "verdict": row.get("verdict", ""),
            }
            data["tiers"].append(entry)
            existing.add((name, vid))
            added += 1

        complete.append("%s (%s) — %d items%s"
                        % (block.get("label", vid), vid, len(items),
                           (", %d unassigned" % len(unassigned)) if unassigned else ""))

    # Cross-source disagreements are informational: the same item can sit in two lists.
    by_item = collections.defaultdict(set)
    for row in data["tiers"]:
        by_item[row["item"]].add(row["tier"])
    split = sorted(k for k, v in by_item.items() if len(v) > 1)

    print("slot files: %d   ratings added: %d   dataset total: %d"
          % (len(list(SLOTS.glob("*.json"))), added, len(data["tiers"])))
    if split:
        print("\nrated differently by more than one list (%d):" % len(split))
        for name in split:
            rows = [r for r in data["tiers"] if r["item"] == name]
            print("  %-34s %s" % (name, ", ".join(
                "%s=%s (%s)" % (r["tier"], r["rated_in"], r["source"]) for r in rows)))
    if overrides:
        print("\ncorrected by a complete read of the list (%d):" % len(overrides))
        for o in overrides:
            print("  " + o)
    if notes:
        print("\ncount differences the file explains (%d):" % len(notes))
        for n in notes:
            print("  " + n)
    if problems:
        print("\nNEEDS A LOOK (%d):" % len(problems))
        for p in problems:
            print("  " + p)

    data["complete_slots"] = {
        "note": "Slot lists read end to end, so every item the video rates is present, "
                "not only the party's. Anything outside these lists is party-scoped.",
        "lists": sorted(complete),
    }
    if not args.dry_run:
        DATA.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
        print("\nwrote " + str(DATA))
    else:
        print("\n(dry run, nothing written)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
