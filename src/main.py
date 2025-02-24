from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    text_test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(text_test.__repr__())

    htmlTest = HTMLNode("p", "This is the paragraph text", ["anchor", "list", "unordered list"], {"href": "https://localhost", "port": "8888"})
    print(htmlTest.__repr__())

    parent_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
    parent_node.to_html()

main()