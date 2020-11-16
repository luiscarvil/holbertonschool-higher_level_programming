#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    """print

    Args:
        filename (str, ""): [name file passed to read].
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
