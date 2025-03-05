from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


#takes a text_node argument and handles the conversion to HTML
#check text_node class for arguments and swap type for text_node
def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    if text_node.text_type == TextType.TEXT:
        new_leaf = LeafNode(None, text_node.text)
        return new_leaf
    elif text_node.text_type == TextType.BOLD:
        new_leaf = LeafNode("b", text_node.text)
        return new_leaf
    elif text_node.text_type == TextType.ITALIC:
        new_leaf = LeafNode("i", text_node.text)
        return new_leaf
    elif text_node.text_type == TextType.CODE:
        new_leaf = LeafNode("code", text_node.text)
        return new_leaf
    elif text_node.text_type == TextType.LINK:
        new_leaf = LeafNode("a", text_node.text, {"href":text_node.url})
        return new_leaf
    elif text_node.text_type == TextType.IMAGE:
        new_leaf = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        return new_leaf
    else:
        raise Exception("Type not defined as Enum in text_to_html() arg.")
