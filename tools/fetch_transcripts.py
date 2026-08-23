#!/usr/bin/env python3
"""Fetch YouTube auto-caption transcripts for a playlist into `video_transcripts/`.

One Markdown file per video, named `<videoId>.md`, skipped if it already exists.
Text comes from yt-dlp's json3 auto-captions. json3 repeats each caption line as a
rollup event flagged `aAppend`; those are dropped, which is why output here is not
tripled the way some older hand-fetched transcripts in this repo are.

Run from the repository root:

    python tools/fetch_transcripts.py PLgTVc5Jd2rrLPuc3vE6XqK65QQboFfolP
    python tools/fetch_transcripts.py <playlist> --only EoRrJ5kI2yk,xWeMvBJ6tl4
    python tools/fetch_transcripts.py <playlist> --list      # manifest only, no fetch

Requires `yt-dlp` on PATH.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

OUT = pathlib.Path("video_transcripts")
BLOCK_SECONDS = 30
FIELDS = ["playlist_index", "id", "duration", "channel", "title"]
SEP = "\t"


def yt_dlp(args: list[str]) -> str:
    exe = shutil.which("yt-dlp")
    if not exe:
        sys.exit("yt-dlp not found on PATH")
    done = subprocess.run([exe] + args, capture_output=True, text=True, encoding="utf-8")
    if done.returncode:
        sys.exit("yt-dlp failed: " + (done.stderr or "").strip()[:2000])
    return done.stdout


def manifest(playlist: str) -> list[dict]:
    """The playlist as a list of dicts, in playlist order."""
    template = SEP.join("%(" + f + ")s" for f in FIELDS)
    raw = yt_dlp(["--flat-playlist", "--no-warnings", "--print", template, playlist])
    rows = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split(SEP)
        if len(parts) < len(FIELDS):
            continue
        row = dict(zip(FIELDS, parts[: len(FIELDS) - 1] + [SEP.join(parts[len(FIELDS) - 1 :])]))
        rows.append(row)
    return rows


def stamp(seconds: float) -> str:
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return "%d:%02d:%02d" % (h, m, s) if h else "%d:%02d" % (m, s)


def caption_lines(path: pathlib.Path) -> list[tuple[float, str]]:
    """(start seconds, text) per real caption line, rollup duplicates dropped."""
    data = json.loads(path.read_text(encoding="utf-8"))
    lines = []
    for event in data.get("events", []):
        if event.get("aAppend"):
            continue
        text = "".join(seg.get("utf8", "") for seg in event.get("segs", []))
        text = " ".join(text.split())
        if not text:
            continue
        lines.append((event.get("tStartMs", 0) / 1000.0, text))
    return lines


def blocks(lines: list[tuple[float, str]]) -> list[tuple[float, str]]:
    """Group caption lines into ~30s paragraphs so the file stays readable."""
    out = []
    start = None
    buf: list[str] = []
    for at, text in lines:
        if start is None:
            start = at
        elif at - start >= BLOCK_SECONDS:
            out.append((start, " ".join(buf)))
            start, buf = at, []
        buf.append(text)
    if buf and start is not None:
        out.append((start, " ".join(buf)))
    return out


def fetch_one(row: dict, playlist_id: str, workdir: pathlib.Path) -> pathlib.Path | None:
    vid = row["id"]
    url = "https://www.youtube.com/watch?v=" + vid
    yt_dlp([
        "--skip-download", "--write-auto-subs", "--sub-langs", "en-orig,en",
        "--sub-format", "json3", "--no-warnings", "-q",
        "-o", str(workdir / "%(id)s.%(ext)s"), url,
    ])
    # en-orig is the untranslated track when both are offered.
    found = sorted(workdir.glob(vid + "*.json3"))
    preferred = [p for p in found if ".en-orig." in p.name] or found
    if not preferred:
        print("  !! no auto-captions for " + vid)
        return None

    lines = caption_lines(preferred[0])
    if not lines:
        print("  !! empty caption track for " + vid)
        return None
    words = sum(len(text.split()) for _, text in lines)
    duration = row.get("duration") or ""
    try:
        duration = stamp(float(duration))
    except ValueError:
        duration = "unknown"

    head = [
        "# " + row["title"],
        "",
        "- Video: " + url,
        "- Video ID: `" + vid + "`",
        "- Channel: " + (row.get("channel") or "unknown"),
        "- Playlist: `" + playlist_id + "` (index " + (row.get("playlist_index") or "?") + ")",
        "- Transcript language: English (auto-generated)",
        "- Duration: " + duration + " · Words: " + str(words),
        "- Retrieved via: yt-dlp auto-captions (json3), grouped into ~"
        + str(BLOCK_SECONDS) + "s blocks",
        "",
        "## Transcript",
        "",
    ]
    body = ["[" + stamp(at) + "] " + text for at, text in blocks(lines)]
    path = OUT / (vid + ".md")
    path.write_text("\n".join(head + body) + "\n", encoding="utf-8", newline="\n")
    for p in found:
        p.unlink()
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("playlist", help="playlist URL or bare list id")
    ap.add_argument("--only", help="comma-separated video ids to limit the fetch to")
    ap.add_argument("--force", action="store_true", help="refetch even if the file exists")
    ap.add_argument("--list", action="store_true", help="print the manifest and stop")
    args = ap.parse_args()

    playlist = args.playlist
    playlist_id = playlist.rsplit("list=", 1)[-1] if "list=" in playlist else playlist
    if "://" not in playlist:
        playlist = "https://www.youtube.com/playlist?list=" + playlist_id

    rows = manifest(playlist)
    print("playlist %s: %d videos" % (playlist_id, len(rows)))
    if args.list:
        for row in rows:
            local = "*" if (OUT / (row["id"] + ".md")).exists() else " "
            print("%4s %s %-11s %s" % (row["playlist_index"], local, row["id"], row["title"]))
        return 0

    only = set(filter(None, (args.only or "").split(","))) or None
    todo = [
        row for row in rows
        if (only is None or row["id"] in only)
        and (args.force or not (OUT / (row["id"] + ".md")).exists())
    ]
    print("fetching %d" % len(todo))
    OUT.mkdir(exist_ok=True)
    written = 0
    with tempfile.TemporaryDirectory() as tmp:
        workdir = pathlib.Path(tmp)
        for i, row in enumerate(todo, 1):
            print("[%d/%d] %s %s" % (i, len(todo), row["id"], row["title"][:70]), flush=True)
            if fetch_one(row, playlist_id, workdir):
                written += 1
    print("wrote %d transcript(s) to %s" % (written, OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
