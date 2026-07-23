"""Scrape bg3.wiki via the MediaWiki API into a resumable on-disk cache.

Two phases:
  1. Enumerate page titles with action=query&list=allpages (skips redirects).
  2. For each title, fetch rendered HTML with action=parse (prop=text|categories)
     so the stat tables/infoboxes survive, and cache one JSON file per page.

Runs are resumable: a page already present in data/raw/ is skipped, so you can
Ctrl-C and re-run freely. Requests are throttled and send maxlag + a descriptive
User-Agent per MediaWiki API etiquette.

Usage:
    python -m bg3kb.scrape                         # full run
    python -m bg3kb.scrape --limit 50              # first 50 titles only
    python -m bg3kb.scrape --titles "Astarion" "Bhaalist Armour"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

# Allow both `python -m bg3kb.scrape` and `python bg3kb/scrape.py`.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests  # noqa: E402

from bg3kb import config as C  # noqa: E402


def _slug(title: str) -> str:
    """Stable, filesystem-safe filename for a page title (titles have / : etc.)."""
    return hashlib.sha1(title.encode("utf-8")).hexdigest()[:16] + ".json"


def raw_path(title: str) -> Path:
    return C.RAW / _slug(title)


class Client:
    """Thin throttled MediaWiki API client with maxlag + retry handling."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers["User-Agent"] = C.USER_AGENT
        self._min_interval = 1.0 / max(C.REQUESTS_PER_SEC, 0.1)
        self._last = 0.0

    def _throttle(self) -> None:
        wait = self._min_interval - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.monotonic()

    def get(self, **params) -> dict:
        params.setdefault("format", "json")
        params.setdefault("formatversion", 2)
        params.setdefault("maxlag", C.MAXLAG)
        for attempt in range(C.MAX_RETRIES):
            self._throttle()
            try:
                r = self.session.get(C.API_URL, params=params, timeout=60)
            except requests.RequestException as e:
                self._backoff(attempt, f"network error: {e}")
                continue
            if r.status_code == 429:
                self._backoff(attempt, "HTTP 429", retry_after=r.headers.get("Retry-After"))
                continue
            r.raise_for_status()
            data = r.json()
            # maxlag: the server is busy and asks us to wait.
            if isinstance(data, dict) and data.get("error", {}).get("code") == "maxlag":
                self._backoff(attempt, "maxlag", retry_after=r.headers.get("Retry-After"))
                continue
            return data
        raise RuntimeError(f"Gave up after {C.MAX_RETRIES} retries for params={params}")

    @staticmethod
    def _backoff(attempt: int, why: str, retry_after: str | None = None) -> None:
        delay = float(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt
        print(f"  … {why}; sleeping {delay:.0f}s (attempt {attempt + 1})", file=sys.stderr)
        time.sleep(delay)


def enumerate_titles(client: Client, namespaces=C.NAMESPACES) -> list[str]:
    """All non-redirect page titles in the given namespaces."""
    titles: list[str] = []
    for ns in namespaces:
        cont: dict = {}
        while True:
            data = client.get(
                action="query", list="allpages", apnamespace=ns,
                aplimit="max", apfilterredir="nonredirects", **cont,
            )
            titles.extend(p["title"] for p in data["query"]["allpages"])
            print(f"  enumerated {len(titles)} titles (ns={ns})…", file=sys.stderr)
            if "continue" in data:
                cont = data["continue"]
            else:
                break
    return titles


def fetch_page(client: Client, title: str) -> dict:
    """Rendered HTML + categories for one page, as a cache record."""
    data = client.get(
        action="parse", page=title, prop="text|categories",
        redirects=1, disableeditsection=1, disabletoc=1,
    )
    parse = data["parse"]
    categories = [
        c["category"].replace("_", " ")
        for c in parse.get("categories", [])
        if "hidden" not in c  # skip maintenance/tracking categories
    ]
    return {
        "title": parse["title"],
        "pageid": parse.get("pageid"),
        "url": C.ARTICLE_URL.format(title=parse["title"].replace(" ", "_")),
        "categories": categories,
        "html": parse["text"],
    }


def scrape(titles: list[str] | None = None, limit: int | None = None) -> None:
    C.RAW.mkdir(parents=True, exist_ok=True)
    client = Client()

    if titles is None:
        print("Enumerating titles…", file=sys.stderr)
        titles = enumerate_titles(client)
    if limit:
        titles = titles[:limit]

    total = len(titles)
    fetched = skipped = failed = 0
    print(f"Scraping {total} pages -> {C.RAW}", file=sys.stderr)
    for i, title in enumerate(titles, 1):
        dest = raw_path(title)
        if dest.exists():
            skipped += 1
            continue
        try:
            record = fetch_page(client, title)
            dest.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
            fetched += 1
        except Exception as e:  # noqa: BLE001 — keep going; the run is resumable
            failed += 1
            print(f"!! [{i}/{total}] {title}: {e}", file=sys.stderr)
            continue
        if fetched % 100 == 0:
            print(f"  [{i}/{total}] fetched={fetched} skipped={skipped} failed={failed}",
                  file=sys.stderr)

    print(f"\nDone: fetched={fetched}, skipped(cached)={skipped}, failed={failed}, "
          f"cache={len(list(C.RAW.glob('*.json')))} files", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description="Scrape bg3.wiki content pages.")
    ap.add_argument("--titles", nargs="+", help="Scrape only these exact page titles.")
    ap.add_argument("--limit", type=int, help="Cap the number of pages (for dry runs).")
    args = ap.parse_args()
    scrape(titles=args.titles, limit=args.limit)


if __name__ == "__main__":
    main()
