"""bg3kb — a local hybrid-search knowledge base built from bg3.wiki.

Pipeline: scrape (MediaWiki API) -> clean (HTML->Markdown) -> chunk ->
embed (GPU) -> LanceDB (vector + BM25) -> search (CLI + MCP).
"""

__version__ = "0.1.0"


def _enable_hf_offline_if_cached() -> None:
    """If the embedding model is already downloaded, switch HuggingFace to
    offline mode so subsequent loads don't hit the network to re-validate the
    model revision (that round-trip is what prints the "unauthenticated
    requests" warning and adds a startup delay). Runs at package import — before
    any huggingface_hub import — so the env vars take effect. The first run,
    before the model is cached, stays online so it can download once.
    """
    import os
    from pathlib import Path

    from bg3kb import config as C

    if not getattr(C, "HF_OFFLINE_WHEN_CACHED", True):
        return
    home = os.environ.get("HF_HOME")
    hub = Path(home) / "hub" if home else Path.home() / ".cache" / "huggingface" / "hub"
    model_dir = hub / ("models--" + C.EMBED_MODEL.replace("/", "--"))
    if model_dir.is_dir() and any(model_dir.glob("snapshots/*")):
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")


_enable_hf_offline_if_cached()
