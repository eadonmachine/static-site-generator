from htmlnode import HTMLNode

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