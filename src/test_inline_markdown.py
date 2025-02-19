import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        target = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, target)

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        target = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, target)

    def test_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        target = [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, target)

    def test__multiple_italic(self):
        node = TextNode("This is *text* with multiple *italic* words", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        target = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.ITALIC),
            TextNode(" with multiple ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" words", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, target)

    def test_none(self):
        node = TextNode("This is just some plain text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        target = [
            TextNode("This is just some plain text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, target)

    def test_odd_delimiters(self):
        node = TextNode("This is text with *one delimiter", TextType.NORMAL)
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_multiple_nodes(self):
        node = TextNode("This is text with an *italic* word", TextType.NORMAL)
        node2 = TextNode("This is more text with an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node, node2], "*", TextType.ITALIC)
        target = [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
            TextNode("This is more text with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, target)

    def test_two_types(self):
        node = TextNode("This is text with a **bold** word and an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        target = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, target)

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        target = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(images, target)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        target = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(links, target)

if __name__ == "__main__":
    unittest.main()