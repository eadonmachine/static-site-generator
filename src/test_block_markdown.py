import unittest
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node
)

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
        

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
        md2 = "> \"I am in fact a Hobbit in all but size.\"\n>\n> -- J.R.R. Tolkien"
        node2 = markdown_to_html_node(md2)
        html2 = node2.to_html()
        self.assertEqual(
            html2,
            "<div><blockquote>\"I am in fact a Hobbit in all but size.\" -- J.R.R. Tolkien</blockquote></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()