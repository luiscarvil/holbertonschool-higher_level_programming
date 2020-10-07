#!/usr/bin/python3
"""
function that return the number of lines of a text
"""


def number_of_lines(filename=""):
    """
    Args:
        filename (str, ""): [text file to open and read].
        Returns: [int]: [numb lines]
    """
    lines_numb = 0
    with open(filename, 'r') as f:
        for i in f:
            lines_numb += 1
    return lines_numb
