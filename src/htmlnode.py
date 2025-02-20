class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = []
        if (children != None):
            self.children = children.copy()
        self.props = {}
        if(props != None):
            self.props = props.copy()

    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        dict_string = ""
        for key,val in self.props:
            dict_string += f"{key}: \"{val}\" "
        return dict_string
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps dict: {self.props}\n"