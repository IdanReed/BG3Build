import unittest

from bg3kb import config as C
from bg3kb.chunk import _pack, _split_oversized_block, _token_windows, chunk_page, ntokens


class ChunkBoundsTests(unittest.TestCase):
    def test_complete_chunks_include_breadcrumbs_in_limit(self):
        doc = {
            "title": "A Detailed Page",
            "url": "https://example.test/page",
            "categories": [],
            "markdown": (
                "# A deliberately descriptive section heading\n"
                + "\n\n".join(
                    f"Paragraph {index}: " + "lightning damage and battlefield control. " * 35
                    for index in range(8)
                )
            ),
        }

        chunks = chunk_page(doc)

        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(ntokens(chunk["text"]) <= C.CHUNK_TOKENS for chunk in chunks))

    def test_pack_counts_blank_line_separators(self):
        blocks = ["alpha " * 12, "beta " * 12, "gamma " * 12]
        windows = _pack(blocks, max_tokens=25, overlap=5)

        self.assertTrue(all(ntokens(window) <= 25 for window in windows))

    def test_table_fragments_repeat_header_when_rows_fit(self):
        table = "\n".join(
            [
                "| Name | Effect |",
                "| --- | --- |",
                *[f"| Item {index} | Damage and control effect {index} |" for index in range(12)],
            ]
        )

        fragments = _split_oversized_block(table, max_tokens=45)

        self.assertGreater(len(fragments), 1)
        self.assertTrue(all(fragment.startswith("| Name | Effect |\n| --- | --- |") for fragment in fragments))
        self.assertTrue(all(ntokens(fragment) <= 45 for fragment in fragments))

    def test_token_windows_preserve_unicode(self):
        text = "Psychic damage 🙂 and Crèche exploration. " * 20

        windows = _token_windows(text, max_tokens=7)

        self.assertEqual("".join(windows), text)
        self.assertTrue(all(ntokens(window) <= 7 for window in windows))


if __name__ == "__main__":
    unittest.main()
