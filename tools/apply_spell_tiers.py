#!/usr/bin/env python3
"""Write the ratings in `resources/tiers/spell_tiers.json` into `content/characters/*.md`.

One managed pair, because the spell series runs no ranked countdown:

    tier / tier_note   the letter tier from that spell level's tier list

Sibling of `tools/apply_item_tiers.py` with the same contract: every managed field is
stripped and rewritten on each run, so editing the dataset and re-running is the way to
change a rating. The two appliers stay out of each other's way by region — this one
only touches lines inside a build's `spells:` block, that one only touches lines
outside it.

Class features share the `- spell:` shape (Extra Attack, Flurry of Blows, Fighting
Style) and the spell series does not rate them, so they go unmatched by design. Only an
entry whose `level` is a real spell level is reported as missing a rating.

    python tools/apply_spell_tiers.py --dry-run
    python tools/apply_spell_tiers.py
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys

DATA = pathlib.Path("resources/tiers/spell_tiers.json")
CHARACTERS = pathlib.Path("content/characters")
MANAGED = ("tier", "tier_note")

SPELLS_KEY = re.compile(r"^(?P<ind>[ ]*)spells:[ ]*$")
SPELL_ENTRY = re.compile(r"^(?P<ind>[ ]+)- spell: (?P<name>[^\n]*)$", re.M)
LEVEL_FIELD = re.compile(r"^[ ]+level: (?P<level>[^\n]*)$", re.M)


def norm(name):
    """The content names the variant a build actually casts — "Chromatic Orb: Fire",
    "Daylight: Enchant Item" — where the lists rate the base spell, so drop anything
    after a colon along with parentheticals. Two rated spells carry a colon of their
    own ("Curriculum of Strategy: Artistry of War"); both sides are normalised the same
    way, so those still match on the part in front of it."""
    text = (name or "").lower().replace("’", "'")
    text = text.split(":", 1)[0]
    text = re.sub(r"\(.*?\)", " ", text)
    text = re.sub(r"[^a-z0-9' ]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def yq(text):
    return "'" + str(text).replace("'", "''") + "'"


def unquote(value):
    """A `- spell:` value is either bare or single-quoted with doubled quotes inside."""
    text = value.strip()
    if len(text) > 1 and text[0] == text[-1] and text[0] in "'\"":
        text = text[1:-1]
        if value.strip()[0] == "'":
            text = text.replace("''", "'")
    return text


def spell_level(value):
    """The content's `level` as the dataset writes it: 0 for a cantrip, an int for a
    spell level, None for a class feature."""
    text = unquote(value).lower()
    if "cantrip" in text:
        return 0
    return int(text) if re.fullmatch(r"[1-9]", text) else None


def spell_spans(text):
    """Offset ranges of every `spells:` block — the only region this applier owns.

    A block runs from its `spells:` line to the next non-blank line indented no deeper
    than that key, which is either a sibling field of the build or the next build."""
    spans, pos, open_at, open_ind = [], 0, None, 0
    for line in text.split("\n"):
        if open_at is not None and line.strip():
            if len(line) - len(line.lstrip(" ")) <= open_ind:
                spans.append((open_at, pos))
                open_at = None
        if open_at is None:
            key = SPELLS_KEY.match(line)
            if key:
                open_at, open_ind = pos, len(key.group("ind"))
        pos += len(line) + 1
    if open_at is not None:
        spans.append((open_at, len(text)))
    return spans


def build_lookup(data, problems):
    rows = {}
    for row in data["spells"]:
        key = norm(row["spell"])
        prior = rows.get(key)
        if prior is not None and prior["tier"] != row["tier"]:
            problems.append("%r and %r both normalise to %r with different tiers"
                            % (prior["spell"], row["spell"], key))
            continue
        rows.setdefault(key, row)
    return rows


def tier_note(row, sources):
    src = sources.get(row["source"], {})
    where = src.get("label", row["source"])
    return "%s (%s) — %s" % (where, row.get("at", "?"), row["verdict"])


def apply_block(block, rows, sources, strip_re, report):
    """Strip and rewrite the managed fields on every `- spell:` entry in one block."""
    block = strip_re.sub("", block)
    pieces, cursor, written = [], 0, 0
    entries = list(SPELL_ENTRY.finditer(block))
    for i, match in enumerate(entries):
        name = unquote(match.group("name"))
        row = rows.get(norm(name))
        tail = block[match.end():entries[i + 1].start() if i + 1 < len(entries) else len(block)]
        level_field = LEVEL_FIELD.search(tail)
        level = spell_level(level_field.group("level")) if level_field else None
        if not row:
            if level is not None:
                report["unrated"].append("%s (level %s)" % (name, level))
            continue
        if level is not None and level != row.get("level"):
            report["level_differs"].append(
                "%s: content level %s, rated as level %s" % (name, level, row.get("level")))
        field = " " * (len(match.group("ind")) + 2)
        pieces.append(block[cursor:match.end()])
        pieces.append("\n%stier: %s\n%stier_note: %s"
                      % (field, row["tier"], field, yq(tier_note(row, sources))))
        cursor = match.end()
        written += 1
    pieces.append(block[cursor:])
    return "".join(pieces), written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.loads(DATA.read_text(encoding="utf-8"))
    problems = []
    rows = build_lookup(data, problems)
    sources = data["sources"]
    strip_re = re.compile(r"\n[ ]+(?:%s): [^\n]*(?=\n)" % "|".join(MANAGED))

    total = 0
    report = collections.defaultdict(list)
    for path in sorted(CHARACTERS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        out, cursor, written = [], 0, 0
        for start, end in spell_spans(text):
            out.append(text[cursor:start])
            block, count = apply_block(text[start:end], rows, sources, strip_re, report)
            out.append(block)
            written += count
            cursor = end
        out.append(text[cursor:])
        text = "".join(out)
        total += written

        if not args.dry_run:
            path.write_text(text, encoding="utf-8")
        print("%-14s %d rating(s)" % (path.name, written))

    print("spell ratings written: %d of %d in the dataset" % (total, len(data["spells"])))
    if report["level_differs"]:
        print("\nrated at a different spell level than the content lists (%d):"
              % len(report["level_differs"]))
        for line in report["level_differs"]:
            print("  " + line)
    if report["unrated"]:
        print("\nspell entries the corpus does not rate (%d):" % len(report["unrated"]))
        for line in report["unrated"]:
            print("  " + line)
    if problems:
        print("\nNEEDS A LOOK (%d):" % len(problems))
        for line in problems:
            print("  " + line)
    if args.dry_run:
        print("\n(dry run, nothing written)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
