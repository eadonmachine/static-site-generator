import os, shutil, sys
from textnode import TextNode, TextType
from copystatic import copy_directory
from gencontent import generate_pages_recursive


def main():
    dir_path_static = "./static"
    dir_path_public = "./docs"
    dir_path_content = "./content"
    template_path = "./template.html"

    try:
        basepath = sys.argv[1]
    except:
        basepath = "/"
    print(f"Using base path {basepath}")
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    os.mkdir(dir_path_public)
    print("Copying static files to public directory...")
    copy_directory(dir_path_static, dir_path_public)
    print("Generating site...")
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_public)
    print("Done.")

main()