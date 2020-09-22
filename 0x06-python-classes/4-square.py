#!/usr/bin/python3
"""
method square - defines a square.
"""


class Square:
    """
    class square init size
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        return the value size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            """
            raise error TypeError and push menssage
            """
            raise TypeError("size must be an integer")
        if value < 0:
            """
            raise error ValueError and push menssage
            """
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
