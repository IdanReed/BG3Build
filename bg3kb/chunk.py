"""Split a page's Markdown into embed-sized chunks.

Strategy:
  - Break the page into sections by Markdown headings, tracking a breadcrumb
    ("Bhaalist Armour > Properties") so each chunk carries its context.
  - Within a section, greedily pack blank-line-separated blocks into windows of
    ~CHUNK_TOKENS tokens with ~CHUNK_OVERLAP overlap between windows.
  - A block bigger than the window is split on token boundaries. Markdown tables
    are split by rows while repeating their header in each fragment.

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
_TABLE_SEPARATOR = re.compile(
    r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$"
)


def ntokens(text: str) -> int:
    return len(_ENC.encode(text))


def _token_windows(text: str, max_tokens: int) -> list[str]:
    """Hard-limit arbitrary text without splitting a UTF-8 character."""
    if max_tokens < 1:
        raise ValueError("max_tokens must be positive")
    tokens = _ENC.encode(text)
    windows: list[str] = []
    start = 0
    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        while end > start:
            try:
                window = _ENC.decode_bytes(tokens[start:end]).decode(
                    "utf-8", errors="strict"
                )
                break
            except UnicodeDecodeError:
                end -= 1
        else:
            raise ValueError(
                "max_tokens is too small to split text at a UTF-8 boundary"
            )
        windows.append(window)
        start = end
    return windows


def _split_oversized_block(block: str, max_tokens: int) -> list[str]:
    """Split a large block, retaining Markdown table headers where possible."""
    lines = block.splitlines()
    if (
        len(lines) >= 3
        and "|" in lines[0]
        and _TABLE_SEPARATOR.match(lines[1])
    ):
        header = lines[:2]
        fragments: list[str] = []
        current = list(header)
        for row in lines[2:]:
            candidate = "\n".join([*current, row])
            if ntokens(candidate) <= max_tokens:
                current.append(row)
                continue

            if len(current) > len(header):
                fragments.append("\n".join(current))
                current = list(header)

            candidate = "\n".join([*header, row])
            if ntokens(candidate) <= max_tokens:
                current.append(row)
            else:
                # A single pathological row cannot retain the header and remain
                # bounded; split it losslessly as ordinary text.
                fragments.extend(_token_windows(candidate, max_tokens))

        if len(current) > len(header):
            fragments.append("\n".join(current))
        return fragments

    return _token_windows(block, max_tokens)


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
    for block in blocks:
        if ntokens(block) > max_tokens:
            # Flush before emitting independently bounded fragments.
            if cur:
                windows.append("\n\n".join(cur))
                cur = []
            windows.extend(_split_oversized_block(block, max_tokens))
            continue
        if cur and ntokens("\n\n".join([*cur, block])) > max_tokens:
            windows.append("\n\n".join(cur))
            # Carry the tail blocks (up to `overlap` tokens) into the next window.
            carry: list[str] = []
            for pb in reversed(cur):
                candidate = [pb, *carry]
                if ntokens("\n\n".join(candidate)) > overlap:
                    break
                carry = candidate
            while carry and ntokens("\n\n".join([*carry, block])) > max_tokens:
                carry.pop(0)
            cur = carry
        cur.append(block)
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
    """Coalesce fragments while their complete stored text remains bounded."""
    out: list[tuple[str, str]] = []
    for crumb, text in frags:
        if out:
            pc, ptext = out[-1]
            combined = f"{ptext}\n\n{text}"
            combined_crumb = _common_crumb(pc, crumb)
            if ntokens(f"{combined_crumb}\n\n{combined}") <= max_tokens:
                out[-1] = (combined_crumb, combined)
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
        content_budget = C.CHUNK_TOKENS - ntokens(f"{crumb}\n\n")
        if content_budget < 1:
            raise ValueError(f"breadcrumb exceeds chunk limit: {crumb}")
        for window in _pack(blocks, content_budget, C.CHUNK_OVERLAP):
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
