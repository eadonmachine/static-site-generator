import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        md = """



This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items




"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        md = "# This is a heading"
        md2 = "## This is also a heading"
        md3 = "### So is this"
        md4 = "#### And this"
        md5 = "##### This too"
        md6 = "###### And this too"
        md7 = "####### But this is not"
        md8 = " ## This isn't"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md4), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md5), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md6), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md7), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md8), BlockType.PARAGRAPH)

    def test_quote_block(self):
        md = ">This is a quote"
        md2 = ">This is a\n>multi line quote"
        md3 = ">This is not\na quote\n>block"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(md2), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(md3), BlockType.PARAGRAPH)

    def test_code_block(self):
        md = "```This is a code block```"
        md2 = "```This is a\nmulti line code block```"
        md3 = "```This is not a code block``"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)
        self.assertEqual(block_to_block_type(md2), BlockType.CODE)
        self.assertEqual(block_to_block_type(md3), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        md = "- This is an\n- Unordered list"
        md2 = "-- This isn't\n- a ul"
        md3 = "- This is"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(md2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md3), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        md = "1. This is\n2. An ordered\n3. List"
        md2 = "2. This shouldn't\n3. Count"
        md3 = "1. This is\n1. Not right either"
        md4 = "1. This is fine"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(md2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md4), BlockType.ORDERED_LIST)

    def test_misc(self):
        md = "# This is a\n1. Heading block"
        md2 = "1. Not any\n- Type of list"
        md3 = "This is just text"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md3), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()