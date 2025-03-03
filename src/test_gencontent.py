import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_h1(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_h2(self):
        md = "## Hello"
        with self.assertRaises(ValueError):
            title = extract_title(md)
    
    def test_both(self):
        md = "## Hello\n# Hi"
        title = extract_title(md)
        self.assertEqual(title, "Hi")
    
    def test_whitespace(self):
        md = "#      Hello      "
        title = extract_title(md)
        self.assertEqual(title, "Hello")

if __name__ == "__main__":
    unittest.main()