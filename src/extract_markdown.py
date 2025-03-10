import re
from textnode import TextNode

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
