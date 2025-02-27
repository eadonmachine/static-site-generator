import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
        else:
            section_nodes = []
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise ValueError(f"Invalid Markdown: missing {delimiter} delimiter")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    section_nodes.append(TextNode(sections[i], TextType.NORMAL))
                else:
                    section_nodes.append(TextNode(sections[i], text_type))
            new_nodes.extend(section_nodes)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if (old_node.text_type != TextType.NORMAL) or (images == []):
            new_nodes.append(old_node)
        else:
            for i in range(len(images)):
                image_alt = images[i][0]
                image_link = images[i][1]
                sections = old_node.text.split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                if i + 1 == len(images) and sections[1] != "":
                    new_nodes.append(TextNode(sections[1], TextType.NORMAL))
                else:
                    old_node.text = sections[1]
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if (old_node.text_type != TextType.NORMAL) or (links == []):
            new_nodes.append(old_node)
        else:
            for i in range(len(links)):
                link_text = links[i][0]
                link_url = links[i][1]
                sections = old_node.text.split(f"[{link_text}]({link_url})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                if i + 1 == len(links) and sections[1] != "":
                    new_nodes.append(TextNode(sections[1], TextType.NORMAL))
                else:
                    old_node.text = sections[1]
    return new_nodes
