from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node

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
    print("=======Text to html node test======")
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())
    try:
        text_node_to_html_node(-1)
    except Exception as err:
        print(err)


main()