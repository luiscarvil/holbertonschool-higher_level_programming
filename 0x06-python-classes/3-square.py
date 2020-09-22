#!/usr/bin/python3
"""
method square - defines a square.
"""


class Square:
    """
    class square check conditions
    """
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
