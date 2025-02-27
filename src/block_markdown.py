def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    for i in range(len(blocks) -1, -1, -1):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            del blocks[i]

    return blocks