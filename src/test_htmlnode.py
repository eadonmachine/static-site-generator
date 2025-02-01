import unittest

from htmlnode import HTMLNode

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
        print(node1)

    

if __name__ == "__main__":
    unittest.main()