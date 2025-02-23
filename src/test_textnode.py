import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://localhost")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://localhost")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_leaf_error(self):
        with self.assertRaises(ValueError):
            leafNode = LeafNode('a', None, None)

    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a paragraph test")
        self.assertEqual(node.to_html(), "<p>This is a paragraph test</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a test")
        self.assertEqual(node.to_html(), "This is a test")

if __name__ == "__main__":
    unittest.main()