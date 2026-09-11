#!/usr/bin/env python3
"""Fold the per-video tables in `resources/tiers/spells/*.json` into `resources/tiers/spell_tiers.json`.

Sibling to `tools/merge_slot_tiers.py`, kept separate because spells and gear are
consumed differently: gear ratings badge the itemization tabs, spell ratings badge the
`spells` blocks in each build.

Source is the [Updated] Patch 8 spell series only. The playlist also carries an older
pre-Patch-8 series, which is superseded and deliberately not read.

    python tools/merge_spell_tiers.py --dry-run
    python tools/merge_spell_tiers.py
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

DATA = pathlib.Path("resources/tiers/spell_tiers.json")
SPELLS = pathlib.Path("resources/tiers/spells")
LETTERS = {"S+", "S", "A", "B", "C", "D", "F"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not SPELLS.is_dir():
        sys.exit("no " + str(SPELLS))

    data = {
        "about": "Spell and cantrip tier ratings, read from the [Updated] Patch 8 spell "
                 "series in playlist PLgTVc5Jd2rrLPuc3vE6XqK65QQboFfolP. One row per "
                 "spell per source video. Feeds tier/tier_note on the spells blocks in "
                 "content/characters/*.md.",
        "playlist": "PLgTVc5Jd2rrLPuc3vE6XqK65QQboFfolP",
        "channel": "Cephalopocalypse",
        "method": "tools/dump_tier_verdicts.py lists every spoken verdict; each was read "
                  "and attributed by hand. The lists state their own totals on camera "
                  "(\"26 of the 52 first level spells\"), which is the completeness check.",
        "scale": "S A B C D. This series defines no F tier, so a reported F is a mis-hear.",
        "sources": {},
        "spells": [],
    }

    problems, notes = [], []
    for path in sorted(SPELLS.glob("*.json")):
        try:
            block = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as err:
            problems.append("%s: unreadable (%s)" % (path.name, err))
            continue
        vid = block.get("source") or path.stem
        items = block.get("items") or []
        unassigned = block.get("unassigned") or []
        seen = block.get("verdicts_in_transcript")
        level = block.get("spell_level")

        if seen is not None and len(items) + len(unassigned) != seen:
            excuse = block.get("count_note") or block.get("note")
            (notes if excuse else problems).append(
                "%s: %d rated + %d unassigned vs %d verdicts" % (
                    vid, len(items), len(unassigned), seen))

        dupes = [k for k, n in collections.Counter(
            row.get("item") or row.get("spell") for row in items).items() if n > 1]
        if dupes:
            problems.append("%s: rated twice: %s" % (vid, ", ".join(sorted(map(str, dupes)))))

        data["sources"][vid] = {
            "label": block.get("label", vid),
            "spell_level": level,
            "rated": len(items),
        }
        for row in items:
            name = row.get("item") or row.get("spell")
            tier = str(row.get("tier", "")).upper()
            if not name or tier not in LETTERS:
                problems.append("%s: bad row %r" % (vid, row))
                continue
            data["spells"].append({
                "spell": name,
                "level": row.get("level", level),
                "tier": tier,
                "source": vid,
                "at": row.get("at", ""),
                "verdict": row.get("verdict", ""),
            })

    by_name = collections.defaultdict(set)
    for row in data["spells"]:
        by_name[row["spell"]].add(row["tier"])
    split = sorted(k for k, v in by_name.items() if len(v) > 1)

    print("spell files: %d   spells: %d   distinct: %d"
          % (len(data["sources"]), len(data["spells"]), len(by_name)))
    print("levels: " + ", ".join(
        "L%s=%d" % (lvl, n) for lvl, n in sorted(
            collections.Counter(str(r["level"]) for r in data["spells"]).items())))
    print("tiers:  " + ", ".join(
        "%s=%d" % (t, n) for t, n in sorted(
            collections.Counter(r["tier"] for r in data["spells"]).items())))
    if split:
        print("\nrated differently by more than one video (%d): %s"
              % (len(split), ", ".join(split)))
    if notes:
        print("\ncount differences the file explains (%d):" % len(notes))
        for n in notes:
            print("  " + n)
    if problems:
        print("\nNEEDS A LOOK (%d):" % len(problems))
        for p in problems:
            print("  " + p)

    if not args.dry_run:
        DATA.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
        print("\nwrote " + str(DATA))
    else:
        print("\n(dry run, nothing written)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
