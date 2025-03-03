import os
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line
            return title[2:].strip()
    raise ValueError("No h1 header in markdown")

def generate_page(base_path, from_path, template_path, dest_path):
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
    newpage = newpage.replace("href=\"/", f"href=\"{base_path}")
    newpage = newpage.replace("src=\"/", f"src=\"{base_path}")

    dest_directory = os.path.dirname(dest_path)
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    with open(dest_path, "w") as f:
        f.write(newpage)

def generate_pages_recursive(base_path, dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise FileNotFoundError(f"Source path {dir_path_content} doesn't exist")

    dirlist = os.listdir(dir_path_content)

    if not os.path.exists(dest_dir_path):
        print(f"Destination path {dest_dir_path} does not exist, creating...")
        os.mkdir(dest_dir_path)

    for filename in dirlist:
        from_path = os.path.join(dir_path_content, filename)
        to_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if filename.split(".")[-1] == "md":
                generate_page(base_path, from_path, template_path, to_path[:-2] + "html")
        else:
            generate_pages_recursive(base_path, from_path, template_path, to_path)