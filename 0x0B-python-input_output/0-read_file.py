#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    """print

    Args:
        filename (str, ""): [name file passed to read].
    """
    with open('my_file_0.txt') as f:
        print(f.read(), end="")
