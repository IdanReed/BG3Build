"""Embedding model loader shared by the indexer and the search side.

The model is loaded once (lru_cache) so search calls and MCP requests reuse it.
bge models embed passages raw and queries with a fixed instruction prefix.

The device is picked automatically: CUDA (NVIDIA), else MPS (Apple Silicon),
else CPU. CPU is slow for a full `embed_index` run but fine for query-time
embedding, which is one short string per search.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bg3kb import config as C  # noqa: E402


def _pick_device() -> str:
    """Best available accelerator: CUDA -> MPS -> CPU."""
    import torch

    if torch.cuda.is_available():
        return "cuda"
    # is_available() is False on macOS below the torch build's minimum (recent
    # wheels require macOS 14+), so this falls through to CPU on older systems.
    if torch.backends.mps.is_available():
        return "mps"
    if torch.backends.mps.is_built():
        print("NOTE: this macOS is too old for the installed torch's MPS backend — "
              "embedding on CPU. Fine for search; slow for `embed_index`.",
              file=sys.stderr)
    else:
        print("NOTE: no GPU backend available — embedding on CPU. Fine for search; "
              "slow for `embed_index`.", file=sys.stderr)
    return "cpu"


@lru_cache(maxsize=1)
def get_model():
    import torch
    from sentence_transformers import SentenceTransformer

    device = _pick_device()
    # Load CUDA weights directly in fp16. Loading fp32 and converting afterward
    # briefly doubles host/virtual-memory pressure for large embedding models.
    # fp16 is CUDA-only here: CPU fp16 matmul is slow, and MPS keeps fp32 to
    # avoid the accuracy drift that would desync queries from the fp32 index.
    fp16 = C.USE_FP16 and device == "cuda"
    model = SentenceTransformer(
        C.EMBED_MODEL,
        device=device,
        model_kwargs={"torch_dtype": torch.float16} if fp16 else None,
    )
    print(f"Loaded {C.EMBED_MODEL} on {device}{' (fp16)' if fp16 else ''}",
          file=sys.stderr)
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
