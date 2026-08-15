# bg3kb — local hybrid-search KB from bg3.wiki

Scrapes every content page on [bg3.wiki](https://bg3.wiki) (MediaWiki 1.43.9),
converts each to Markdown (keeping the stat tables), chunks it, embeds the
chunks (on the GPU if you have one), and stores them in an embedded **LanceDB**
table with both a vector index and a BM25 full-text index. Query it from a CLI
or from Claude Code via an MCP server.

## Setup (uv)

Run everything from the repo root in a **uv**-managed venv. The venv lives at
`bg3kb/.venv` and is git-ignored, so each machine builds its own.

**Windows (git bash):**

```bash
cd /c/EpicSource/Personal/bg3
uv venv bg3kb/.venv
source bg3kb/.venv/Scripts/activate
uv pip install -r bg3kb/requirements.txt
# Install the CUDA torch build for the 3080 (otherwise embedding runs on CPU):
uv pip install torch --index-url https://download.pytorch.org/whl/cu124
```

**macOS:**

```bash
cd ~/local/BG3Build
uv venv bg3kb/.venv
source bg3kb/.venv/bin/activate
uv pip install -r bg3kb/requirements.txt   # the default torch wheel is correct here
```

No extra torch step on macOS. `embedder.py` picks the best device available —
CUDA, else Apple-Silicon MPS, else CPU — and prints which one it used. Note that
recent torch wheels require **macOS 14+** for MPS; on older systems torch
reports MPS unavailable and embedding falls back to CPU. That is fine for
search (a query is one short string: ~0.2 s warm) but slow for a full
`embed_index` rebuild.

If you only want to query the existing index, that is all the setup needed —
`bg3kb/data/` already holds the scraped pages and the built LanceDB table, and
the embedding model downloads itself on the first query.

Then set a real contact string in `bg3kb/config.py` (`USER_AGENT`) — needed only
if you are going to **scrape**.

Re-activate in a new shell with `source bg3kb/.venv/bin/activate`
(`bg3kb/.venv/Scripts/activate` on Windows), or prefix commands with `uv run` to
skip activation.

## Run order

```bash
# 1. Scrape (resumable, ~1.5h at the default polite rate). Dry run first:
python -m bg3kb.scrape --titles "Astarion" "Bhaalist Armour" "Divine Smite" "Resonance Stone"
python -m bg3kb.scrape                 # full run (all namespace-0 pages)

# 2. Build the index (embeds on GPU, prints chunks/sec):
python -m bg3kb.embed_index

# 3. Query:
python -m bg3kb.cli "where do I find Bhaalist Armour"
python -m bg3kb.cli "best weapon type for a crit-smite paladin" --k 5
python -m bg3kb.cli            # no query -> interactive REPL (model loads once)
```

The model downloads once (during step 2) into the HuggingFace cache. After
that, bg3kb switches HuggingFace to **offline mode** automatically, so each run
loads from cache with no Hub network check (config: `HF_OFFLINE_WHEN_CACHED`).

### Warm daemon (fast repeat queries)

A one-shot `cli` call would normally reload the model each time (~15-20 s of
CUDA init). Instead, the first query auto-starts a background **daemon**
(`bg3kb.daemon`) that holds the model in VRAM and serves queries over a loopback
socket; it shuts down after 5 min idle (`DAEMON_IDLE_SECONDS`). So:

- 1st query: ~17 s (spawns + warms the daemon)
- subsequent queries: ~0.4 s

Flags/knobs: `--no-daemon` runs fully in-process; port/idle timeout are in
`config.py`. The REPL and MCP server stay warm on their own and don't use the
daemon. To watch the daemon live: `python -m bg3kb.daemon`.

## Preview without a GPU

`clean.py` and `chunk.py` run standalone against cached raw pages, so you can
confirm fidelity before installing torch (only the lightweight deps are needed:
`uv pip install requests beautifulsoup4 markdownify tiktoken tqdm`):

```bash
python -m bg3kb.clean "Bhaalist Armour"     # prints the Markdown (tables kept)
python -m bg3kb.chunk "Bhaalist Armour"     # prints the chunk breakdown
```

## MCP server (query from Claude Code)

```bash
# Windows
claude mcp add bg3-wiki -- \
  C:/EpicSource/Personal/bg3/bg3kb/.venv/Scripts/python.exe \
  C:/EpicSource/Personal/bg3/bg3kb/mcp_server.py

# macOS
claude mcp add bg3-wiki -- \
  /Users/idanreed/local/BG3Build/bg3kb/.venv/bin/python \
  /Users/idanreed/local/BG3Build/bg3kb/mcp_server.py
```

Use the venv's Python (so the server has torch/lancedb/mcp) and the script's
absolute path — `mcp_server.py` self-bootstraps `sys.path`, so it works no
matter which directory Claude Code launches it from. The server exposes one
tool, `bg3_search(query, k=8, category=None)`.

The registration is per-machine (`claude mcp add` writes to the local config,
not the repo), so run it once on each. Check it with `claude mcp list`.

## Notes

- Content is CC BY-SA 4.0; every chunk stores its source `url` for attribution.
- `mcp_server.py` supports both mcp 1.x (`FastMCP`) and mcp 2.x, which renamed
  that class to `MCPServer`. The decorator API is the same either way.
- `robots.txt` disallows `/w/api.php` for crawlers — this tool is a one-time,
  low-rate personal archive that caches to disk and never re-fetches. Keep the
  rate modest and the `USER_AGENT` honest.
