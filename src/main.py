import os, shutil
from textnode import TextNode, TextType
from copystatic import copy_directory
from gencontent import generate_page


def main():
    if os.path.exists("public/"):
        shutil.rmtree("public/")
    os.mkdir("public/")
    copy_directory("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")

main()