import re
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
        # print(f"node: {node}")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
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


def extract_markdown_images(text):
    image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_matches

def split_nodes_image(old_nodes):
    new_nodes = []
    # print(f"old_nodes: {old_nodes}")
    for node in old_nodes:
        # print(f"node.text: {node.text}")
        split_text = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        print(f"split_text: {split_text}")
        images = extract_markdown_images(node.text)
        print(f"images: {images}")
        # if images == []:
            # continue
        alt_text, url = images[0]
        for node in split_text:
            # print(f"node: {node}, alt_text: {alt_text}, url: {url}")
            if node == url:
                # print(f"making image node")
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                if len(images) > 1:
                    images = images[1:]
                    alt_text, url = images[0]
            elif node == alt_text:
                # print(f"alt_text node")
                continue
            elif node == "":
                # print(f"empty node")
                continue
            else:
                # print(f"text node with: {node}")
                new_nodes.append(TextNode(node, TextType.TEXT))
            
    # print(f"new_nodes: {new_nodes}")
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    # print(f"old_nodes: {old_nodes}")
    for node in old_nodes:
        # print(f"node.text: {node.text}")
        split_text = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        # print(f"split_text: {split_text}")
        links = extract_markdown_links(node.text)
        # print(f"images: {images}")
        alt_text, url = links[0]
        for node in split_text:
            # print(f"node: {node}, alt_text: {alt_text}, url: {url}")
            if node == url:
                # print(f"making image node")
                new_nodes.append(TextNode(alt_text, TextType.LINK, url))
                if len(links) > 1:
                    links = links[1:]
                    alt_text, url = links[0]
            elif node == alt_text:
                # print(f"alt_text node")
                continue
            elif node == "":
                # print(f"empty node")
                continue
            else:
                # print(f"text node with: {node}")
                new_nodes.append(TextNode(node, TextType.TEXT))
            
    # print(f"new_nodes: {new_nodes}")
    return new_nodes



def text_to_textnodes(text):
    new_nodes = []
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_image([node])
    for node in new_nodes:
        print(f"node: {node}")
        if node.text_type == TextType.IMAGE:
            print(f"doing image")
            new_nodes.append(split_nodes_image([node]))
        if node.text_type == TextType.LINK:
            print(f"doing link")
            new_nodes.append(split_nodes_link([node]))
    print(f"new_nodes: {new_nodes}")




