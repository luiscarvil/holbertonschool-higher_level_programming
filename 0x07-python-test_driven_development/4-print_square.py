#!/usr/bin/python3
"""print square with '#'
"""


def print_square(size):
    """

    Args:
        size (int): size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
