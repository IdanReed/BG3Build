"""Hybrid search over the LanceDB table: dense vector + BM25, fused with RRF
(optionally re-ranked by a GPU cross-encoder if config.RERANKER_MODEL is set).

    from bg3kb.search import search
    hits = search("where do I find Bhaalist Armour", k=5)
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import lancedb  # noqa: E402

from bg3kb import config as C  # noqa: E402
from bg3kb.embedder import embed_query  # noqa: E402


@lru_cache(maxsize=1)
def _table():
    return lancedb.connect(C.LANCE_DIR).open_table(C.TABLE_NAME)


@lru_cache(maxsize=1)
def _reranker():
    from lancedb.rerankers import RRFReranker

    if C.RERANKER_MODEL:
        from lancedb.rerankers import CrossEncoderReranker
        return CrossEncoderReranker(model_name=C.RERANKER_MODEL, device="cuda")
    return RRFReranker()


def search(query: str, k: int = 8, category: str | None = None) -> list[dict]:
    """Return up to k ranked chunks. `category` filters to a wiki category."""
    qv = embed_query(query)
    q = (
        _table()
        .search(query_type="hybrid")
        .vector(qv)
        .text(query)
        .rerank(reranker=_reranker())
        .limit(k)
    )
    if category:
        q = q.where(f"array_has(categories, '{category}')", prefilter=True)

    hits = []
    for r in q.to_list():
        hits.append({
            "page_title": r["page_title"],
            "section": r["section"],
            "url": r["url"],
            "categories": r.get("categories", []),
            "score": float(r.get("_relevance_score", r.get("_distance", 0.0))),
            "text": r["text"],
        })
    return hits
