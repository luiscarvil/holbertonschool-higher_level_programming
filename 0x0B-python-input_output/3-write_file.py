#!/usr/bin/python3
"""
function that writes a string to a text file (utf-8) & return N char
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): [file to open and read or create].
        text (str): [text to write].

    Returns:
        [int]: [number of characters]
    """
    lines = 0
    with open(filename, 'w') as f:
        lines = f.write(text)
    return lines
