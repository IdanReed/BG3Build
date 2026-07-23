"""GPU embedding model loader shared by the indexer and the search side.

The model is loaded once (lru_cache) so search calls and MCP requests reuse it.
bge models embed passages raw and queries with a fixed instruction prefix.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bg3kb import config as C  # noqa: E402


@lru_cache(maxsize=1)
def get_model():
    import torch
    from sentence_transformers import SentenceTransformer

    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: CUDA not available — embedding on CPU (slow). Install the "
              "CUDA torch build to use your 3080.", file=sys.stderr)
    model = SentenceTransformer(C.EMBED_MODEL, device=device)
    if C.USE_FP16 and device == "cuda":
        model = model.half()
    print(f"Loaded {C.EMBED_MODEL} on {device}"
          f"{' (fp16)' if C.USE_FP16 and device == 'cuda' else ''}", file=sys.stderr)
    return model


def embed_passages(texts: list[str], show_progress: bool = True):
    """Embed document chunks -> float32 numpy array (n, EMBED_DIM)."""
    model = get_model()
    embs = model.encode(
        texts, batch_size=C.BATCH_SIZE, normalize_embeddings=True,
        convert_to_numpy=True, show_progress_bar=show_progress,
    )
    return embs.astype("float32")


def embed_query(text: str):
    """Embed a search query -> float32 numpy array (EMBED_DIM,)."""
    model = get_model()
    emb = model.encode(
        C.QUERY_PREFIX + text, normalize_embeddings=True, convert_to_numpy=True,
    )
    return emb.astype("float32")
