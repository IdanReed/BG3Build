"""Split a page's Markdown into embed-sized chunks.

Strategy:
  - Break the page into sections by Markdown headings, tracking a breadcrumb
    ("Bhaalist Armour > Properties") so each chunk carries its context.
  - Within a section, greedily pack blank-line-separated blocks into windows of
    ~CHUNK_TOKENS tokens with ~CHUNK_OVERLAP overlap between windows.
  - A block bigger than the window (typically a stat table) is emitted whole —
    tables are never split.

Token counting uses tiktoken (cl100k_base) as a fast, model-agnostic proxy; the
exact tokenizer doesn't matter for sizing.

Standalone preview:
    python -m bg3kb.chunk "Bhaalist Armour"
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tiktoken  # noqa: E402

from bg3kb import config as C  # noqa: E402
from bg3kb.clean import load_markdown  # noqa: E402

_ENC = tiktoken.get_encoding("cl100k_base")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


def ntokens(text: str) -> int:
    return len(_ENC.encode(text))


def iter_sections(markdown: str, page_title: str):
    """Yield (breadcrumb, section_text) with heading hierarchy tracked."""
    stack: list[tuple[int, str]] = []  # (heading level, title)
    buf: list[str] = []

    def crumb() -> str:
        return " > ".join([page_title, *[t for _, t in stack]])

    for line in markdown.split("\n"):
        m = _HEADING.match(line)
        if m:
            if buf:
                yield crumb(), "\n".join(buf).strip()
                buf = []
            level = len(m.group(1))
            title = m.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
        else:
            buf.append(line)
    if buf:
        yield crumb(), "\n".join(buf).strip()


def _pack(blocks: list[str], max_tokens: int, overlap: int) -> list[str]:
    """Greedily pack blocks into token-bounded windows, with token overlap."""
    windows: list[str] = []
    cur: list[str] = []
    cur_tok = 0
    for block in blocks:
        bt = ntokens(block)
        if bt > max_tokens:
            # Oversized block (e.g. a big stat table): flush, then keep it whole.
            if cur:
                windows.append("\n\n".join(cur))
                cur, cur_tok = [], 0
            windows.append(block)
            continue
        if cur_tok + bt > max_tokens and cur:
            windows.append("\n\n".join(cur))
            # Carry the tail blocks (up to `overlap` tokens) into the next window.
            carry: list[str] = []
            ct = 0
            for pb in reversed(cur):
                pt = ntokens(pb)
                if ct + pt > overlap:
                    break
                carry.insert(0, pb)
                ct += pt
            cur, cur_tok = list(carry), ct
        cur.append(block)
        cur_tok += bt
    if cur:
        windows.append("\n\n".join(cur))
    return windows


def _common_crumb(a: str, b: str) -> str:
    """Longest shared breadcrumb prefix (falls back to the page title)."""
    pa, pb = a.split(" > "), b.split(" > ")
    common = []
    for x, y in zip(pa, pb):
        if x != y:
            break
        common.append(x)
    return " > ".join(common) if common else pa[0]


def _merge_small(frags: list[tuple[str, str]], max_tokens: int) -> list[tuple[str, str]]:
    """Coalesce consecutive fragments while the combined text stays under the
    window cap. Collapses infobox micro-sections into coherent chunks."""
    out: list[tuple[str, str]] = []
    for crumb, text in frags:
        if out:
            pc, ptext = out[-1]
            combined = f"{ptext}\n\n{text}"
            if ntokens(combined) <= max_tokens:
                out[-1] = (_common_crumb(pc, crumb), combined)
                continue
        out.append((crumb, text))
    return out


def chunk_page(doc: dict) -> list[dict]:
    """Turn a {title,url,categories,markdown} doc into chunk records."""
    frags: list[tuple[str, str]] = []
    for crumb, section in iter_sections(doc["markdown"], doc["title"]):
        if not section:
            continue
        blocks = [b.strip() for b in re.split(r"\n{2,}", section) if b.strip()]
        for window in _pack(blocks, C.CHUNK_TOKENS, C.CHUNK_OVERLAP):
            frags.append((crumb, window))

    chunks: list[dict] = []
    for idx, (crumb, window) in enumerate(_merge_small(frags, C.CHUNK_TOKENS)):
        chunks.append({
            "id": f"{doc['title']}#{idx}",
            "page_title": doc["title"],
            "section": crumb,
            "url": doc["url"],
            "categories": doc["categories"],
            "chunk_index": idx,
            # Prepend the breadcrumb so the chunk is self-contained for both
            # the embedder and BM25.
            "text": f"{crumb}\n\n{window}",
        })
    return chunks


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # BG3 text has non-cp1252 chars
    if len(sys.argv) < 2:
        print("usage: python -m bg3kb.chunk \"<page title>\"", file=sys.stderr)
        raise SystemExit(2)
    doc = load_markdown(sys.argv[1])
    cs = chunk_page(doc)
    print(f"{doc['title']}: {len(cs)} chunks\n", file=sys.stderr)
    for c in cs:
        print(f"--- [{c['chunk_index']}] {c['section']} ({ntokens(c['text'])} tok) ---")
        print(c["text"])
        print()
