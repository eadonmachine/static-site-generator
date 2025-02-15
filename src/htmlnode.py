from textnode import TextNode, TextType

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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode - Tag: {self.tag}, Value: {self.value}, Props: {self.props}"

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"HTMLNode - Tag: {self.tag}, Children: {self.children}, Props: {self.props}"

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")

        if self.children == None:
            raise ValueError("ParentNode must have children")

        html = ""
        for child in self.children:
            html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("TextNode has an invalid TextType")