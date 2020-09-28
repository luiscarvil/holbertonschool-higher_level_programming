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
        self.__width = width
        self.__height = height

    def __str__(self):
        """ print string """
        if self.width == 0 or self.height == 0:
            return("")
        else:
            return(("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """ string convertion """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ destructor object rectangle """
        print("Bye rectangle...")

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
