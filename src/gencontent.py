import os
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line
            return title[2:].strip()
    raise ValueError("No h1 header in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    newpage = template.replace("{{ Title }}", title)
    newpage = newpage.replace("{{ Content }}", html)

    dest_directory = os.path.dirname(dest_path)
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    with open(dest_path, "w") as f:
        f.write(newpage)
