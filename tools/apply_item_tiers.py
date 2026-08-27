#!/usr/bin/env python3
"""Write the ratings in `research/item_tiers.json` into `content/characters/*.md`.

Two independent fields, because an item can hold both kinds of rating at once:

    tier / tier_note   a letter tier from that slot's tier list
    rank / rank_note   a place in that act's top-20 countdown

Existing `tier: '#N'` values are migrated to `rank`, which is where a countdown
placing belongs now that letter tiers occupy `tier`.

Idempotent: every managed field is stripped and rewritten on each run, so editing
the dataset and re-running is the way to change a rating.

Scope is gear only. A build's `spells:` block carries the same tier/tier_note pair,
written from a different dataset by `tools/apply_spell_tiers.py`, so those lines are
left alone here instead of being stripped as stale.

    python tools/apply_item_tiers.py --dry-run
    python tools/apply_item_tiers.py
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

DATA = pathlib.Path("research/item_tiers.json")
CHARACTERS = pathlib.Path("content/characters")
MANAGED = ("tier", "tier_note", "rank", "rank_note")


def norm(name):
    text = (name or "").lower().replace("’", "'")
    text = re.sub(r"\(.*?\)", " ", text)
    text = re.sub(r"^the\s+", "", text.strip())
    text = re.sub(r"[^a-z0-9'+ ]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def yq(text):
    return "'" + str(text).replace("'", "''") + "'"


SPELLS_KEY = re.compile(r"^(?P<ind>[ ]*)spells:[ ]*$")


def spell_spans(text):
    """Offset ranges of every `spells:` block — the region this applier does not own.

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


def strip_managed(text, strip_re):
    """Strip the managed fields everywhere except inside a `spells:` block. Each span
    boundary sits at the start of a line, so a match can never straddle one."""
    out, cursor = [], 0
    for start, end in spell_spans(text):
        out.append(strip_re.sub("", text[cursor:start]))
        out.append(text[start:end])
        cursor = end
    out.append(strip_re.sub("", text[cursor:]))
    return "".join(out)


def variants(key):
    """The content and the guides disagree on plurals: the party sheet says "Arrows of
    Darkness" and "Dual Hand Crossbows +1" where the tier lists say "Arrow of Darkness"
    and "Hand Crossbow +1". Try the obvious singular/plural forms before giving up."""
    out = [key]
    words = key.split()
    for i, word in enumerate(words):
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            out.append(" ".join(words[:i] + [word[:-1]] + words[i + 1:]))
        elif len(word) > 3:
            out.append(" ".join(words[:i] + [word + "s"] + words[i + 1:]))
    if words and words[0] in ("dual", "twin"):
        out.extend(variants(" ".join(words[1:])) if len(words) > 1 else [])
    # Possessives drift too: the party sheet says "Hellrider's Longbow", the bow list
    # says "Hellrider Longbow".
    stripped = re.sub(r"'s", "", key).replace("  ", " ").strip()
    if stripped != key:
        out.append(stripped)
    return out


def build_lookup(data):
    tiers, ranks = {}, {}
    for row in data["tiers"]:
        key = norm(row["item"])
        # An item rated by more than one list keeps the first reading; the dataset
        # records one verdict per (item, source) so this only fires for genuine
        # cross-list duplicates such as a staff that also appears as a weapon.
        tiers.setdefault(key, []).append(row)
    for row in data["ranked"]:
        ranks.setdefault(norm(row["item"]), []).append(row)
    return tiers, ranks


def pick(rows, act):
    if not rows:
        return None
    for row in rows:
        if row.get("rated_in") == act or row.get("act") == act:
            return row
    return rows[0]


def tier_note(row, sources):
    src = sources.get(row["source"], {})
    where = src.get("title", row["source"])
    return "%s (%s) — %s" % (where, row.get("at", "?"), row["verdict"])


def rank_note(row, sources):
    src = sources.get(row["source"], {})
    place = row["rank"]
    place = ("honourable mention" if place == "HM" else "#%s of %s" % (place, row.get("of", 20)))
    return "%s, %s — %s" % (src.get("title", row["source"]), place, row["verdict"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.loads(DATA.read_text(encoding="utf-8"))
    tiers, ranks = build_lookup(data)
    sources = data["sources"]

    strip_re = re.compile(
        r"\n[ ]+(?:%s): [^\n]*(?=\n)" % "|".join(MANAGED))
    entry_re = re.compile(r"^(?P<ind>[ ]+)- id: (?P<id>\S+)[ ]*\n(?P<item>(?P=ind)  item: [^\n]*)$",
                          re.M)
    act_re = re.compile(r"^    (?P<act>act[123]|progression):[ ]*$", re.M)

    total_tier = total_rank = 0
    for path in sorted(CHARACTERS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        text = strip_managed(text, strip_re)

        # Which act does each offset fall in, so a rating can prefer that act's list.
        acts = [(m.start(), m.group("act")) for m in act_re.finditer(text)]

        def act_at(pos):
            current = "act1"
            for start, act in acts:
                if start <= pos:
                    current = act
                else:
                    break
            return current

        out = []
        cursor = 0
        for match in entry_re.finditer(text):
            act = act_at(match.start())
            if act == "progression":
                continue
            name = match.group("item").split("item:", 1)[1].strip().strip("'\"")
            key = norm(name)
            tier_row = rank_row = None
            for cand in variants(key):
                tier_row = tier_row or pick(tiers.get(cand), act)
                rank_row = rank_row or pick(ranks.get(cand), act)
            if not tier_row and not rank_row:
                continue
            field = " " * (len(match.group("ind")) + 2)
            lines = []
            if tier_row:
                lines.append("%stier: %s" % (field, tier_row["tier"]))
                lines.append("%stier_note: %s" % (field, yq(tier_note(tier_row, sources))))
                total_tier += 1
            if rank_row:
                place = rank_row["rank"]
                lines.append("%srank: %s" % (field, yq("#%s" % place if place != "HM" else "HM")))
                lines.append("%srank_note: %s" % (field, yq(rank_note(rank_row, sources))))
                total_rank += 1
            out.append((match.end(), "\n" + "\n".join(lines)))

        if out:
            pieces = []
            for pos, insert in out:
                pieces.append(text[cursor:pos])
                pieces.append(insert)
                cursor = pos
            pieces.append(text[cursor:])
            text = "".join(pieces)

        if args.dry_run:
            print("%-14s %d entry insertion(s)" % (path.name, len(out)))
        else:
            path.write_text(text, encoding="utf-8")
            print("%-14s %d entry insertion(s)" % (path.name, len(out)))

    print("letter tiers written: %d   ranks written: %d" % (total_tier, total_rank))
    return 0


if __name__ == "__main__":
    sys.exit(main())
