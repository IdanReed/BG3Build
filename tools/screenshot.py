#!/usr/bin/env python3
"""Screenshot a view of the running guide with headless Chrome.

The UI has no URL routing — every view is reached by clicking the sidebar — so
this writes a temporary `_shot.html` beside `index.html` (same origin, so it can
still fetch `/api/plan`), appends a small harness that clicks the requested view
and optionally isolates one section card, shoots it, and deletes the copy again.

The server must already be running.

    python tools/screenshot.py --view Gale --section Spells
    python tools/screenshot.py --view Bonbon --section Spells --theme light
    python tools/screenshot.py --view __overview__ -o /tmp/overview.png
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import urllib.parse

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INDEX = pathlib.Path("index.html")
SHOT = pathlib.Path("_shot.html")

HARNESS = """
<script>
/* Injected by tools/screenshot.py. Not part of the application. */
(function () {
  const cfg = %s;
  if (cfg.theme) {
    try { localStorage.setItem("bg3-theme", cfg.theme); } catch (e) {}
    document.documentElement.setAttribute("data-theme", cfg.theme);
  }
  const tick = setInterval(function () {
    const btn = Array.from(document.querySelectorAll("[data-key]"))
      .find((b) => b.getAttribute("data-key") === cfg.view);
    if (!btn) return;
    clearInterval(tick);
    btn.click();
    setTimeout(function () {
      const host = document.getElementById("main-content");
      if (cfg.section) {
        const sec = Array.from(host.querySelectorAll("section.card")).find((s) => {
          const head = s.querySelector(".section-title");
          return head && head.textContent.trim().toLowerCase() === cfg.section.toLowerCase();
        });
        if (sec) host.replaceChildren(sec);
      }
      document.body.classList.add("shot-ready");
    }, 500);
  }, 60);
})();
</script>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--view", default="Gale",
                    help="sidebar key: a character nickname, or __overview__ / __tad__ / __loot1__")
    ap.add_argument("--section", default=None, help="isolate one section card, e.g. Spells")
    ap.add_argument("--theme", choices=("light", "dark"), default=None)
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--size", default="1400x1400", help="viewport, WxH")
    ap.add_argument("-o", "--out", default="shot.png")
    args = ap.parse_args()

    if not pathlib.Path(CHROME).exists():
        print("Chrome not found at %s" % CHROME, file=sys.stderr)
        return 1

    cfg = {"view": args.view, "section": args.section, "theme": args.theme}
    html = INDEX.read_text(encoding="utf-8")
    SHOT.write_text(html.replace("</body>", HARNESS % json.dumps(cfg) + "</body>"), encoding="utf-8")
    width, _, height = args.size.partition("x")
    url = "http://127.0.0.1:%d/%s?%s" % (
        args.port, SHOT.name, urllib.parse.urlencode({"v": args.view}))
    try:
        proc = subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--virtual-time-budget=12000",
            "--window-size=%s,%s" % (width, height or "1400"),
            "--screenshot=" + str(pathlib.Path(args.out).resolve()), url,
        ], capture_output=True, text=True)
    finally:
        SHOT.unlink(missing_ok=True)

    if not pathlib.Path(args.out).exists():
        sys.stderr.write(proc.stderr)
        print("no screenshot written — is the server running on port %d?" % args.port, file=sys.stderr)
        return 1
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
