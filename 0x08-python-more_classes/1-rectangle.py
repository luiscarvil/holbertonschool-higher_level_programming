#!/usr/bin/python3
"""
define a rectangle

Returns:
    int: value by area and perimeter.
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter with rectangle

        Returns:
            int: retunr private value width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        value pass to setter

        Args:
            value (int): width by rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter height rectangle

        Returns:
            int: retunr private value height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        value pass setter

        Args:
            value (int): value height rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
