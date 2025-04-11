
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"\n\
tag: {self.tag} \n\
value: {self.value} \n\
children: {self.children} \n\
props: {self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return None
        my_props = ""
        for prop in self.props:
            # print(f"prop: {prop}")
            my_props = my_props + ' ' + prop + '="' + self.props[prop] + '"'
        return my_props


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must be defined")
        if self.children == None:
            raise ValueError("children must be defined")

        my_string = ""
        for node in self.children:
            my_string = my_string + node.to_html()
        return f'<{self.tag}>{my_string}</{self.tag}>'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value must be defined.")
        if self.tag == None:
            return self.value

        if self.tag == "a":
            if self.props["href"] == None:
                raise ValueError("anchor tag must have a url")
            return f'<a href={self.props["href"]}>{self.value}</a>'

        return f'<{self.tag}>{self.value}</{self.tag}>'



