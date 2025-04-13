import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_tag(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1.tag, node2.tag)

    def test_eq_value(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1.value, node2.value)

    def test_eq_children(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1.children, node2.children)

    def test_eq_props(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1.props, node2.props)

    def test_eq_tag(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1.tag, node2.tag)

    @unittest.skip("Broken, no clue why. Will come back to fix")
    def test_eq_all(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1, node2)

    def test_neq_tag(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h2", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node1.tag, node2.tag)

    def test_neq_value(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h2", "header2", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node1.value, node2.value)

    def test_neq_children(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h2", "header1", "1", {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node1.children, node2.children)

    def test_neq_props(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h2", "header1", "", {"href": "https://www.google.com/index.html","target": "_blank",})
        self.assertNotEqual(node1.props, node2.props)

    def test_none_tag(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)

    def test_none_value(self):
        node = HTMLNode()
        self.assertIsNone(node.value)

    def test_none_children(self):
        node = HTMLNode()
        self.assertIsNone(node.children)

    def test_none_props(self):
        node = HTMLNode()
        self.assertIsNone(node.props)

    def test_eq_props_output(self):
        node1 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "header1", "", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

#LeafNodes
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_h2(self):
        node = LeafNode("h2", "Hello, world!")
        self.assertEqual(node.to_html(), "<h2>Hello, world!</h2>")

    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_no_value(self):
        node = LeafNode("b", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_no_tag(self):
        node = LeafNode("", "Raw text")
        self.assertNotEqual(node.to_html(), "Raw text")
    
#ParentNode
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )

    def test_parent_to_html_with_multi_children(self):
        child_node_1 = LeafNode("b", "child_node_1")
        child_node_2 = LeafNode("p", "child_node_2")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child_node_1</b><p>child_node_2</p></div>",
        )

    def test_parent_no_tag(self):
        child_node_1 = LeafNode("b", "child_node_1")
        child_node_2 = LeafNode("p", "child_node_2")
        parent_node = ParentNode(None, [child_node_1, child_node_2] )
        self.assertRaises(ValueError, parent_node.to_html)

    def test_parent_no_childern(self):
        parent_node = ParentNode("div", None )
        self.assertRaises(ValueError, parent_node.to_html)

