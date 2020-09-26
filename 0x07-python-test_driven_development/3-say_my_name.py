#!/usr/bin/python3
"""Funtion that prints two strings
"""


def say_my_name(first_name, last_name=""):
    """

    Args:
        first_name (str): First string to add
        last_name (str, str): second string to add. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is str:
        pass
    else:
        raise TypeError("first_name must be a string")
    if type(last_name) is str:
        pass
    else:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
