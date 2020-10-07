#!/usr/bin/python3
"""
funct that appends a string at the end of a text file & return # char
"""


def append_write(filename="", text=""):
    """

    Args:
        filename (str): [file to open and read or create].
        text (str): [text to write].

    Returns:
        [int]: [number of characters]
    """
    with open(filename, 'a') as f:
        read_data = f.write(text)
    return read_data
