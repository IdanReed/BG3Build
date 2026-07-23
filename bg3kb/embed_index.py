"""Build the LanceDB table: clean + chunk every cached page, embed on GPU,
store vectors, and create the BM25 full-text index.

    python -m bg3kb.embed_index
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import lancedb  # noqa: E402
from tqdm import tqdm  # noqa: E402

from bg3kb import config as C  # noqa: E402
from bg3kb.chunk import chunk_page  # noqa: E402
from bg3kb.clean import html_to_markdown  # noqa: E402
from bg3kb.embedder import embed_passages  # noqa: E402


def load_chunks(use_cache: bool = True) -> list[dict]:
    # The clean+chunk pass over 13k pages takes ~15-20 min, so cache it: re-runs
    # (e.g. after installing the GPU torch, or changing the embed model) skip
    # straight to embedding. Pass --rechunk to rebuild from raw pages.
    if use_cache and C.CHUNKS_CACHE.exists():
        with C.CHUNKS_CACHE.open(encoding="utf-8") as fh:
            chunks = [json.loads(line) for line in fh if line.strip()]
        print(f"Loaded {len(chunks)} cached chunks from {C.CHUNKS_CACHE} "
              f"(pass --rechunk to rebuild).", file=sys.stderr)
        return chunks

    files = sorted(C.RAW.glob("*.json"))
    if not files:
        print(f"No cached pages in {C.RAW}. Run `python -m bg3kb.scrape` first.",
              file=sys.stderr)
        raise SystemExit(1)
    chunks: list[dict] = []
    for f in tqdm(files, desc="clean+chunk"):
        rec = json.loads(f.read_text(encoding="utf-8"))
        doc = {
            "title": rec["title"],
            "url": rec["url"],
            "categories": rec.get("categories", []),
            "markdown": html_to_markdown(rec["html"]),
        }
        chunks.extend(chunk_page(doc))
    print(f"{len(chunks)} chunks from {len(files)} pages", file=sys.stderr)

    C.CHUNKS_CACHE.parent.mkdir(parents=True, exist_ok=True)
    with C.CHUNKS_CACHE.open("w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"Cached chunks -> {C.CHUNKS_CACHE}", file=sys.stderr)
    return chunks


def build(rechunk: bool = False) -> None:
    chunks = load_chunks(use_cache=not rechunk)

    texts = [c["text"] for c in chunks]
    t0 = time.monotonic()
    vectors = embed_passages(texts)
    dt = time.monotonic() - t0
    rate = len(texts) / dt if dt else float("inf")
    print(f"Embedded {len(texts)} chunks in {dt:.1f}s = {rate:.0f} chunks/s",
          file=sys.stderr)

    for c, v in zip(chunks, vectors):
        c["vector"] = v

    db = lancedb.connect(C.LANCE_DIR)
    table = db.create_table(C.TABLE_NAME, data=chunks, mode="overwrite")
    table.create_fts_index("text", replace=True)
    print(f"Built table '{C.TABLE_NAME}' with {table.count_rows()} rows "
          f"+ BM25 index at {C.LANCE_DIR}", file=sys.stderr)


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Embed chunks and build the LanceDB index.")
    ap.add_argument("--rechunk", action="store_true",
                    help="Re-run clean+chunk from raw pages, ignoring chunks.jsonl.")
    args = ap.parse_args()
    build(rechunk=args.rechunk)
