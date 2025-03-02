from textnode import TextNode, TextType
from copystatic import copy_directory


def main():
    tn = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    print(tn)

    copy_directory("static/", "public/")

main()