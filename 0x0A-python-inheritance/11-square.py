#!/usr/bin/python3
"""
basegeometry method
"""


class BaseGeometry:
    """ area with raise Exception """
    def area(self):
        """ not implemented """
        raise Exception("area() is not implemented")
    """ integer_validator """

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ rectangle representation """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ string of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """ represent square """
    def __init__(self, size):
        """ instantiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" square area"""
        return self.__size ** 2

    def __str__(self):
        """ string of the square """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
