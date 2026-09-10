#!/usr/bin/env python3
"""Write the ratings in `research/spell_tiers.json` into `content/characters/*.md`.

Sibling to `tools/apply_item_tiers.py`, and the step `tools/merge_spell_tiers.py`
was built to feed: the merged dataset badges the `spells` blocks in each build the
same way item ratings badge the itemization tabs.

    tier / tier_note   the letter tier the [Updated] Patch 8 spell series gave it

Only the `spells` lists are touched. Item entries carry their own `tier` from the
item pipeline, so the managed fields are stripped per spell entry rather than
across the whole file.

Entries the series never rated — class features such as Stunning Strike, and
racial actions — are left alone; the series rates spells and cantrips only.

Idempotent: every managed field is stripped and rewritten on each run, so editing
the dataset and re-running is the way to change a rating.

    python tools/apply_spell_tiers.py --dry-run
    python tools/apply_spell_tiers.py
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

DATA = pathlib.Path("research/spell_tiers.json")
CHARACTERS = pathlib.Path("content/characters")
MANAGED = ("tier", "tier_note")

# `- spell: NAME` followed by that entry's more-indented field lines.
ENTRY_RE = re.compile(
    r"^(?P<ind>[ ]+)- spell: (?P<name>[^\n]*)\n"
    r"(?P<body>(?:(?P=ind)  [^\n]*\n)*)",
    re.M,
)
STRIP_RE = re.compile(r"^[ ]+(?:%s):[^\n]*\n" % "|".join(MANAGED), re.M)


def norm(name):
    text = (name or "").lower().replace("’", "'")
    text = re.sub(r"\(.*?\)", " ", text)
    text = re.sub(r"[^a-z0-9' ]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def yq(text):
    return "'" + str(text).replace("'", "''") + "'"


def unyq(text):
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "'\"":
        inner = text[1:-1]
        return inner.replace("''", "'") if text[0] == "'" else inner
    return text


def variants(name):
    """The content names a chosen mode where the tier list names the spell: the
    build sheet says "Chromatic Orb: Fire" and "Daylight: Enchant Item" for what the
    series rated as "Chromatic Orb" and "Daylight"."""
    out = [norm(name)]
    if ":" in name:
        out.append(norm(name.split(":", 1)[0]))
    return [key for key in out if key]


def content_level(body):
    """The spell level as the content states it, or None for a class feature."""
    match = re.search(r"^[ ]+level:[ ]*(.*)$", body, re.M)
    if not match:
        return None
    raw = unyq(match.group(1))
    if re.search(r"cantrip", raw, re.I):
        return 0
    return int(raw) if re.fullmatch(r"[1-6]", raw.strip()) else None


def tier_note(row, sources):
    src = sources.get(row["source"], {})
    where = src.get("label", row["source"])
    return "%s (%s) — %s" % (where, row.get("at", "?"), row["verdict"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.loads(DATA.read_text(encoding="utf-8"))
    sources = data["sources"]
    lookup = {}
    for row in data["spells"]:
        lookup.setdefault(norm(row["spell"]), []).append(row)

    total_written = total_unrated = 0
    conflicts = []
    for path in sorted(CHARACTERS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        written = unrated = 0
        pieces = []
        cursor = 0

        for match in ENTRY_RE.finditer(text):
            name = unyq(match.group("name"))
            body = STRIP_RE.sub("", match.group("body"))
            level = content_level(body)

            row = None
            for key in variants(name):
                rows = lookup.get(key)
                if rows:
                    row = rows[0]
                    break

            # A level disagreement means the name matched the wrong spell, so leave
            # the entry unrated rather than stamp a rating from another level.
            if row and level is not None and row["level"] != level:
                conflicts.append((path.name, name, level, row["level"]))
                row = None

            if row:
                field = " " * (len(match.group("ind")) + 2)
                body = "%stier: %s\n%stier_note: %s\n%s" % (
                    field, row["tier"], field, yq(tier_note(row, sources)), body)
                written += 1
            elif level is not None:
                unrated += 1

            pieces.append(text[cursor:match.start()])
            pieces.append("%s- spell: %s\n%s" % (match.group("ind"), match.group("name"), body))
            cursor = match.end()

        pieces.append(text[cursor:])
        text = "".join(pieces)

        if not args.dry_run:
            path.write_text(text, encoding="utf-8")
        print("%-14s %d rated, %d spell entries left unrated" % (path.name, written, unrated))
        total_written += written
        total_unrated += unrated

    for name, spell, mine, theirs in conflicts:
        print("  ! %s: %s is level %s here, level %s in the dataset — skipped"
              % (name, spell, mine, theirs), file=sys.stderr)
    print("spell tiers written: %d   unrated spells/cantrips: %d" % (total_written, total_unrated))
    return 0


if __name__ == "__main__":
    sys.exit(main())
