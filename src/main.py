from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node
from split_node_delimiter import split_nodes_delimiter
from extract_markdown import *

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

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    print("======Testing Extraction=====")
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    text_node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    split_nodes_image([text_node])
main()