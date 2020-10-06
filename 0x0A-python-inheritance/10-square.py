#!/usr/bin/python3
"""
subclass Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """ intantiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area """
        return self.__size * self.__size
