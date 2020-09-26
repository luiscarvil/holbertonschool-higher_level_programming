#!/usr/bin/python3
"""text identation
"""


def text_indentation(text):
    """

    Args:
        text (string): contain text str string

    Raises:
        TypeError: text must be a string
    """
    text2 = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join(i.strip() for i in text.split("\n")), end="")
