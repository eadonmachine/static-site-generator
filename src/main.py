import os, shutil
from textnode import TextNode, TextType
from copystatic import copy_directory
from gencontent import generate_pages_recursive


def main():
    if os.path.exists("public/"):
        shutil.rmtree("public/")
    os.mkdir("public/")
    copy_directory("static/", "public/")
    generate_pages_recursive("content/", "template.html", "public/")

main()