
from textnode import TextType, TextNode
from htmlnode import ParentNode, LeafNode




def text_node_to_html_node(text_node):
    match text_node.get_text_type():
        case TextType.TEXT:
            return LeafNode(None, text_node.text)

        case TextType.BOLD:
            return LeafNode("b", text_node.text)


        case TextType.ITALIC:
            return LeafNode("i", text_node.text)


        case TextType.CODE:
            return LeafNode("code", text_node.text)


        case TextType.LINK:
            return LeafNode("a", text_node.text)


        case TextType.IMAGE:
            return LeafNode("img", text_node.text)


        case _:
            raise Exception("not a valid html node type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_node = node.text.split(delimiter)
        pre_node = split_node[0]
        post_node = split_node[2]
        h_node = split_node[1]
        new_nodes.append(TextNode(pre_node, node.text_type))

        if delimiter == "`":
            new_nodes.append(TextNode(h_node, TextType.CODE))
        elif delimiter == "**":
            new_nodes.append(TextNode(h_node, TextType.BOLD))
        elif delimiter == "_":
            new_nodes.append(TextNode(h_node, TextType.ITALIC))
        else:
            raise Exception("invalid delimiter in split_nodes_delimiter")

        new_nodes.append(TextNode(post_node, node.text_type))

    # print(f"new_nodes: {new_nodes}")
    return new_nodes






