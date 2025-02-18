from textnode import TextNode

def main():
    text_test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(text_test.__repr__())

main()