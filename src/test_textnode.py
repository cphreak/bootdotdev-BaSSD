import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_NORMAL(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_eq_BOLD(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_ITALIC(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq_CODE(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_LINK(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_eq_IMAGE(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_neq_NORMAL(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_BOLD(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_ITALIC(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_neq_CODE(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_neq_LINK(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_neq_IMAGE(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://ThisFake.com/index.html")
        node2 = TextNode("This is a text node", TextType.NORMAL, "https://ThisFake.com/index.html")
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://ThisIsFake.com/index.html")
        node2 = TextNode("This is a text node", TextType.NORMAL, "https://ThisFake.com/index.html")
        self.assertNotEqual(node, node2)

    def test_neq_url_None(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://ThisFake.com/index.html")
        node2 = TextNode("This is a text node", TextType.NORMAL, )
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
    