import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
        pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(pattern, text)
        return matches

def extract_markdown_links(text):
    # Pattern for Markdown links: [anchor text](url)
    # The (?<!!) ensures we don't match image tags
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if (len(images) == 0):
            new_nodes.append(node)
            continue
        current_text = node.text
        for img_alt, img_url in images:
            image_markdown = f"![{img_alt}]({img_url})"
            parts = current_text.split(image_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_url))
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_links(node.text)
        if (len(images) == 0):
            new_nodes.append(node)
            continue
        current_text = node.text
        for link_txt, link_url in images:
            image_markdown = f"![{link_txt}]({link_url})"
            parts = current_text.split(image_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link_txt, TextType.IMAGE, link_url))
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes