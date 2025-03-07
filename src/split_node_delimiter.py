
from textnode import TextNode
from textnode import TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        first_pos = text.find(delimiter)
        if first_pos == -1:
            new_nodes.append(node)
            continue

        second_pos = text.find(delimiter, first_pos + 1)
        if second_pos == -1:
            raise Exception(f"No closing delimiter found {delimiter}")
        
        before_text = text[:first_pos]
        middle_text = text[first_pos + len(delimiter):second_pos]
        after_text = text[second_pos + len(delimiter):]
        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        new_nodes.append(TextNode(middle_text, text_type))
        if after_text:
            after_node = TextNode(after_text, TextType.TEXT)
            new_nodes.extend(split_nodes_delimiter([after_node], delimiter, text_type))

    return new_nodes

#take a node with a delimeter and a text type.
#split the text in the node based on the delimiter. old_node.text.split(delimiter)
#create new nodes based on the text
#return a list of new nodes