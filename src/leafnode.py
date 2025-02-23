from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag, value,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node requires a value")
        if self.tag == None:
            return self.value
        properties = ""
        if (self.props):
            for key,val in self.props.items():
                properties += f" {key}=\"{val}\""
        return f"<{self.tag}{properties}>{self.value}</{self.tag}>"