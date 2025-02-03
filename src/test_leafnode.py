import unittest

from leafnode import LeafNode

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

    

if __name__ == "__main__":
    unittest.main()