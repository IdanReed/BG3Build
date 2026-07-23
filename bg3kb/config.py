"""Central configuration for the bg3kb pipeline.

Everything tweakable lives here so the scraper, indexer, and search share one
source of truth. Paths are absolute (derived from this file's location) so the
tools work regardless of the current working directory.
"""
from __future__ import annotations

from pathlib import Path

# --- Site / API -------------------------------------------------------------
BASE_URL = "https://bg3.wiki"
API_URL = f"{BASE_URL}/w/api.php"          # MediaWiki 1.43.9, scriptpath = /w
ARTICLE_URL = BASE_URL + "/wiki/{title}"    # canonical page URL

# Namespaces to scrape. 0 = main/content (the ~13k article pages). Add more
# (e.g. specific guide namespaces) only if you decide you want them.
NAMESPACES = [0]

# --- Politeness (MediaWiki API etiquette) -----------------------------------
# Set a REAL contact string below — it is the polite thing to do and lets the
# wiki admins reach you instead of just blocking. This is a one-time, low-rate,
# personal archive.
USER_AGENT = "bg3kb/0.1 (personal BG3 wiki archive; contact: your-email@example.com)"
REQUESTS_PER_SEC = 2.5    # self-imposed throttle; ~1.5h for the full 13k pages
MAXLAG = 5                # ask the server to defer us if it's under load
MAX_RETRIES = 5           # for maxlag / 429 / transient network errors

# --- Paths ------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RAW = DATA / "raw"                 # cached per-page JSON (resumable)
LANCE_DIR = str(DATA / "bg3.lance")  # LanceDB dataset dir
TABLE_NAME = "bg3"
CHUNKS_CACHE = DATA / "chunks.jsonl"  # cached clean+chunk output (skip re-cleaning)

# --- Embedding --------------------------------------------------------------
# Default: strong English retrieval model that fits the 3080 at fp16.
# Lighter/faster:      "BAAI/bge-base-en-v1.5"          (768-dim)
# Modern alternatives: "Alibaba-NLP/gte-large-en-v1.5", "Qwen/Qwen3-Embedding-0.6B"
EMBED_MODEL = "BAAI/bge-large-en-v1.5"
EMBED_DIM = 1024
# bge models want passages embedded raw, but queries prefixed with this string.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
BATCH_SIZE = 64
USE_FP16 = True
# Once the model is in the local HF cache, run fully offline so every CLI/search/
# MCP call skips the HF Hub network round-trip (no revision re-check, no
# "unauthenticated requests" warning). The first run downloads it while online.
HF_OFFLINE_WHEN_CACHED = True

# --- Warm search daemon -----------------------------------------------------
# The one-shot CLI reloads the model per invocation. To make repeat queries
# instant, the CLI auto-starts a background daemon that holds the model in VRAM
# and serves queries over a loopback socket, shutting itself down after
# DAEMON_IDLE_SECONDS with no requests.
DAEMON_HOST = "127.0.0.1"
DAEMON_PORT = 8765
DAEMON_IDLE_SECONDS = 300  # 5 min

# Optional cross-encoder reranker for the top-k hybrid hits. Default None uses
# fast RRF rank-fusion (already good). Set to a model name, e.g.
# "BAAI/bge-reranker-v2-m3", to swap in a GPU cross-encoder for higher quality.
RERANKER_MODEL = None

# --- Chunking ---------------------------------------------------------------
# Counted with tiktoken (cl100k_base). Kept below 512 so that after the
# breadcrumb prefix and bge's WordPiece expansion (~1.1-1.3x) chunks still fit
# the model's 512-token limit without truncation. ~400 also sharpens retrieval.
CHUNK_TOKENS = 400     # target window size
CHUNK_OVERLAP = 64     # token overlap carried between adjacent windows
