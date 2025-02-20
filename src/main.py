from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(text_test.__repr__())

    htmlTest = HTMLNode("p", "This is the paragraph text", ["anchor", "list", "unordered list"], {"href": "https://localhost", "port": "8888"})
    print(htmlTest.__repr__())

main()