"""MCP server exposing the BG3 wiki KB to Claude Code as a `bg3_search` tool.

Register:
    claude mcp add bg3-wiki -- python -m bg3kb.mcp_server

The server loads the embedding model lazily on the first query.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from bg3kb.search import search as _search  # noqa: E402

mcp = FastMCP("bg3-wiki")


@mcp.tool()
def bg3_search(query: str, k: int = 8, category: str | None = None) -> list[dict]:
    """Search the Baldur's Gate 3 wiki (bg3.wiki) knowledge base.

    Returns up to `k` ranked chunks, each with the page title, section
    breadcrumb, source URL, and text. Use `category` to restrict to a wiki
    category (e.g. "Spells", "Heavy armour"). Good for item stats/locations,
    spell details, class/build mechanics, and quest facts.
    """
    return _search(query, k=k, category=category)


if __name__ == "__main__":
    mcp.run()
