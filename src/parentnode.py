from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        if tag == None:
            raise ValueError("Tag requires a value in parent node constructor")
        if children == None:
            raise ValueError("Children requires a value in parent node constructor")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node requires a tag")
        if self.children == None:
            raise ValueError("Parent node found children = None")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}>" + html_string + f"</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"