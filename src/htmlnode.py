class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode - Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        str = ""
        if(self.props != None):
            for prop in self.props:
                str += f" {prop}=\"{self.props[prop]}\""
        return str

