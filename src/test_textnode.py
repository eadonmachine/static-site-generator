import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("Hello", TextType.ITALIC)
        node2 = TextNode("Goodbye", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Hello", TextType.NORMAL, "http://url")
        node2 = TextNode("Hello", TextType.ITALIC, "http://url")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("Hello", TextType.NORMAL, "http://url.com")
        node2 = TextNode("Hello", TextType.NORMAL, "http://url.gov")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = TextNode("Hello", TextType.NORMAL, "http://url.com")
        node2 = TextNode("Hello", TextType.NORMAL)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()