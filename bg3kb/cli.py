"""Command-line search over the BG3 wiki KB.

    python -m bg3kb.cli "where do I find Bhaalist Armour"
    python -m bg3kb.cli "haste engine sorcerer" --k 5 --category "Spells"
    python -m bg3kb.cli            # interactive REPL — loads the model once,
                                   # then answers many queries with no reload

One-shot queries go through a background daemon (bg3kb.daemon) that keeps the
model warm for 5 minutes, so repeat calls are instant. Use --no-daemon to run
fully in-process instead.
"""
from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bg3kb import config as C  # noqa: E402

# Note: bg3kb.search (which pulls in lancedb) is imported lazily inside the REPL
# and --no-daemon paths only, so daemon-client calls stay lightweight and fast.


def _print_hits(hits: list[dict], full: bool) -> None:
    if not hits:
        print("No results.")
        return
    for i, h in enumerate(hits, 1):
        print(f"{i}. {h['page_title']} — {h['section']}   (score {h['score']:.3f})")
        print(f"   {h['url']}")
        if full:
            print("\n" + h["text"] + "\n")
        else:
            snippet = " ".join(h["text"].split())[:300]
            print(f"   {snippet}…\n")


def _start_daemon() -> None:
    # Detach so the daemon outlives this CLI process and isn't killed by a
    # Ctrl-C aimed at the shell: a new process group on Windows (also hiding the
    # console window), a new session on POSIX.
    extra: dict = {}
    if os.name == "nt":
        extra["creationflags"] = (
            subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        )
    else:
        extra["start_new_session"] = True
    subprocess.Popen(
        [sys.executable, "-m", "bg3kb.daemon"],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        cwd=str(Path(__file__).resolve().parent.parent),
        close_fds=True, **extra,
    )


def _ask_daemon(payload: dict) -> dict:
    """Send one query to the daemon, starting + waiting for it if needed."""
    addr = (C.DAEMON_HOST, C.DAEMON_PORT)

    def _once() -> dict:
        with socket.create_connection(addr, timeout=5) as s:
            s.settimeout(180)  # generous: covers a cold daemon's model warmup
            f = s.makefile("rwb")
            f.write((json.dumps(payload) + "\n").encode("utf-8"))
            f.flush()
            line = f.readline()
        return json.loads(line)

    try:
        return _once()
    except (ConnectionRefusedError, socket.timeout, OSError):
        pass  # no daemon yet — start one and wait for it to come up

    print("bg3kb: starting warm daemon (first query loads the model)…", file=sys.stderr)
    _start_daemon()
    deadline = time.monotonic() + 90
    while time.monotonic() < deadline:
        try:
            return _once()
        except (ConnectionRefusedError, OSError):
            time.sleep(0.3)
    raise RuntimeError("bg3kb daemon did not become ready in time")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")  # BG3 text has non-cp1252 chars
    sys.stderr.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Search the BG3 wiki knowledge base.")
    ap.add_argument("query", nargs="?",
                    help="Query. Omit to enter an interactive REPL (model loads once).")
    ap.add_argument("--k", type=int, default=8, help="Number of results (default 8).")
    ap.add_argument("--category", help="Restrict to a wiki category.")
    ap.add_argument("--full", action="store_true", help="Print full chunk text.")
    ap.add_argument("--no-daemon", action="store_true",
                    help="Run in-process instead of via the warm daemon.")
    args = ap.parse_args()

    # REPL: stays warm within this process, so it never needs the daemon.
    if not args.query:
        from bg3kb.search import search
        print("bg3kb search — enter a query (blank line or Ctrl-C to quit).")
        try:
            while True:
                query = input("\nquery> ").strip()
                if not query:
                    break
                _print_hits(search(query, k=args.k, category=args.category), args.full)
        except (EOFError, KeyboardInterrupt):
            print()
        return

    # One-shot query.
    if args.no_daemon:
        from bg3kb.search import search
        _print_hits(search(args.query, k=args.k, category=args.category), args.full)
        return

    resp = _ask_daemon({"query": args.query, "k": args.k, "category": args.category})
    if "error" in resp:
        print(f"error: {resp['error']}", file=sys.stderr)
        raise SystemExit(1)
    _print_hits(resp["hits"], args.full)


if __name__ == "__main__":
    main()
