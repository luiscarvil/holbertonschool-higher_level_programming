#!/usr/bin/python3
"""
square method - print square
"""


class Square:
    """
    class square check conditions
    """
    def __init__(self, size=0):
        """
        conditions and definition
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
