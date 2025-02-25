from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType

def text_to_html(type):
    if type == TextType.TEXT:
        print("Text")
    elif type == TextType.BOLD:
        print("Bold")
    elif type == TextType.ITALIC:
        print("Italicized")
    elif type == TextType.CODE:
        print("Coded")
    elif type == TextType.LINK:
        print("Aaaaaaaa")
    elif type == TextType.IMAGE:
        print("Imagine")
    else:
        raise Exception("Type not defined as Enum in text_to_html() arg.")
