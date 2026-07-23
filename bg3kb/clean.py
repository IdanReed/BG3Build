"""Convert cached MediaWiki-rendered HTML into clean Markdown.

Strips MediaWiki chrome (edit links, navboxes, TOC, category footer, scripts)
but KEEPS tables, because BG3 item/spell stats live in tables and infoboxes.

Standalone preview:
    python -m bg3kb.clean "Bhaalist Armour"
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bs4 import BeautifulSoup  # noqa: E402
from markdownify import markdownify as md  # noqa: E402

from bg3kb import config as C  # noqa: E402
from bg3kb.scrape import raw_path  # noqa: E402

# Selectors for elements that are pure UI chrome, not content.
_DROP_SELECTORS = [
    "style", "script", "link", "meta",
    ".mw-editsection", ".mw-jump-link", ".noprint", ".navbox",
    ".toc", "#toc", ".mw-references-wrap", ".reference", ".mw-empty-elt",
    ".mw-cite-backlink", ".printfooter", ".catlinks", "#catlinks",
]


def html_to_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # MediaWiki wraps real content in .mw-parser-output; narrow to it if present.
    root = soup.select_one(".mw-parser-output") or soup

    for sel in _DROP_SELECTORS:
        for el in root.select(sel):
            el.decompose()
    # Images add noise to a text KB; keep captions, drop the <img> tags.
    for img in root.find_all("img"):
        img.decompose()

    text = md(
        str(root),
        heading_style="ATX",   # "## Heading"
        bullets="-",
        strip=["a"],           # keep link text, drop the URLs
    )
    # Collapse the blank-line noise markdownify tends to leave behind.
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_markdown(title: str) -> dict:
    """Return {title, url, categories, markdown} for a cached page."""
    record = json.loads(raw_path(title).read_text(encoding="utf-8"))
    return {
        "title": record["title"],
        "url": record["url"],
        "categories": record.get("categories", []),
        "markdown": html_to_markdown(record["html"]),
    }


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # BG3 text has non-cp1252 chars
    if len(sys.argv) < 2:
        print("usage: python -m bg3kb.clean \"<page title>\"", file=sys.stderr)
        raise SystemExit(2)
    doc = load_markdown(sys.argv[1])
    print(f"# {doc['title']}\n<{doc['url']}>\ncategories: {', '.join(doc['categories'])}\n")
    print(doc["markdown"])
