"""Warm search daemon: keeps the embedding model + LanceDB handle loaded so
repeat CLI queries are instant, then exits after DAEMON_IDLE_SECONDS idle.

Protocol (newline-delimited JSON over a loopback TCP socket):
  request:  {"query": "...", "k": 8, "category": null}\n
  response: {"hits": [...]} | {"error": "..."}\n

The CLI auto-starts this in the background; you rarely run it by hand. To watch
it live (logs to stderr) run it in the foreground:
    python -m bg3kb.daemon
"""
from __future__ import annotations

import json
import socket
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bg3kb import config as C  # noqa: E402
from bg3kb.search import search  # noqa: E402


def _handle(conn: socket.socket) -> None:
    with conn.makefile("rwb") as f:
        line = f.readline()
        if not line:
            return
        try:
            req = json.loads(line)
            hits = search(req["query"], k=req.get("k", 8), category=req.get("category"))
            resp = {"hits": hits}
        except Exception as e:  # noqa: BLE001 — report to client, keep serving
            resp = {"error": f"{type(e).__name__}: {e}"}
        f.write((json.dumps(resp) + "\n").encode("utf-8"))
        f.flush()


def serve() -> None:
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        srv.bind((C.DAEMON_HOST, C.DAEMON_PORT))
    except OSError:
        # Port already bound -> another daemon is running. Nothing to do.
        print("bg3kb daemon: already running, exiting.", file=sys.stderr)
        return
    srv.listen(8)  # incoming clients queue here while we warm up
    print(f"bg3kb daemon: listening on {C.DAEMON_HOST}:{C.DAEMON_PORT}, "
          f"idle timeout {C.DAEMON_IDLE_SECONDS}s", file=sys.stderr)

    # Warm the model + table before accepting, so the first client's query is
    # already fast. Clients that connect meanwhile wait in the listen backlog.
    try:
        search("warmup", k=1)
        print("bg3kb daemon: model warm, ready.", file=sys.stderr)
    except Exception as e:  # noqa: BLE001 — surface per-request instead
        print(f"bg3kb daemon: warmup skipped ({e}).", file=sys.stderr)

    # accept() times out after the idle window; a timeout means no client has
    # connected in that time -> shut down and free the VRAM.
    srv.settimeout(C.DAEMON_IDLE_SECONDS)
    while True:
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            print("bg3kb daemon: idle timeout, shutting down.", file=sys.stderr)
            break
        with conn:
            _handle(conn)
    srv.close()


if __name__ == "__main__":
    serve()
