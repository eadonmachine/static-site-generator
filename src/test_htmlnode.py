import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node1 = HTMLNode("a", "Link to Google", [],{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a paragraph", [],)
        node3 = HTMLNode("h1", "Header", [],)
        self.assertEqual(node1.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_empty_prop(self):
        node1 = HTMLNode("a", "Link to Google", [],{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a paragraph", [],)
        node3 = HTMLNode("h1", "Header", [],)
        self.assertEqual(node2.props_to_html(), "")

    def test_repr(self):
        node1 = HTMLNode("a", "Link to Google", [],{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a paragraph", [],)
        node3 = HTMLNode("h1", "Header", [],)
        self.assertEqual(node1.__repr__(), "HTMLNode - Tag: a, Value: Link to Google, Children: [], Props: {'href': 'https://www.google.com', 'target': '_blank'}")

class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")

    def test_no_tag(self):
        node1 = LeafNode(None, "Link to Google", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.to_html(), "Link to Google")

    def test_props(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

class TestParentNode(unittest.TestCase):
    def test_1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>")

    def test_no_children(self):
        node = ParentNode(
            "p",
            []
        )
        self.assertEqual(node.to_html(), "<p></p>")
    
class TestTextNodeToHTMLNode(unittest.TestCase):
        def test_text_to_html_normal(self):
            node1 = TextNode("This is some plain text", TextType.NORMAL)
            node2 = text_node_to_html_node(node1)
            self.assertEqual(node2.to_html(), "This is some plain text")

        def test_text_to_html_bold(self):
            node1 = TextNode("This is some bold text", TextType.BOLD)
            node2 = text_node_to_html_node(node1)
            self.assertEqual(node2.to_html(), "<b>This is some bold text</b>")

        def test_text_to_html_italic(self):
            node1 = TextNode("This is some italic text", TextType.ITALIC)
            node2 = text_node_to_html_node(node1)
            self.assertEqual(node2.to_html(), "<i>This is some italic text</i>")

        def test_text_to_html_code(self):
            node1 = TextNode("This is some code", TextType.CODE)
            node2 = text_node_to_html_node(node1)
            self.assertEqual(node2.to_html(), "<code>This is some code</code>")

        def test_text_to_html_link(self):
            node1 = TextNode("This is a link", TextType.LINK, "http://www.google.com")
            node2 = text_node_to_html_node(node1)
            self.assertEqual(node2.to_html(), "<a href=\"http://www.google.com\">This is a link</a>")

        def test_text_to_html_image(self):
            node1 = TextNode("This is an image", TextType.IMAGE, "http://link.to.image")
            node2 = text_node_to_html_node(node1)
            self.assertEqual(node2.to_html(), "<img src=\"http://link.to.image\" alt=\"This is an image\"></img>")
            
if __name__ == "__main__":
    unittest.main()