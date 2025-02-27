import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    for i in range(len(blocks) -1, -1, -1):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            del blocks[i]

    return blocks

def block_to_block_type(markdown):
    lines = markdown.split("\n")

    if re.match(r"^#{1,6} .", markdown):
        return BlockType.HEADING

    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE

    isquote = True
    for line in lines:
        if not line.startswith(">"):
            isquote = False
            break
    if isquote:
        return BlockType.QUOTE

    isul = True
    for line in lines:
        if not line.startswith("- "):
            isul = False
            break
    if isul:
        return BlockType.UNORDERED_LIST

    isol = True
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            isol = False
            break
    if isol:
        return BlockType.ORDERED_LIST


    return BlockType.PARAGRAPH