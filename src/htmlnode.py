class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        dict_string = ""
        for prop in self.props:
            dict_string += f' {prop}="{self.props[prop]}"'
        return dict_string
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps dict: {self.props}\n"