#!/usr/bin/python3
""" add_integer
Function that print 2 numbers

Returns:
    c : add a + b integers
"""


def add_integer(a, b=98):
    """
    Args:
        a (int): First element
        b (int, optional): Second element Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    """
    c = 0
    if type(a) is int or type(a) is float:
        pass
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        pass
    else:
        raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return c
