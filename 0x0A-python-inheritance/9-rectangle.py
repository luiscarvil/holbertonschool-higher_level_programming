#!/usr/bin/python3
"""
contain class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle():
    """ rectangle representation """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area width * height """
        return self.__width * self.__height

    def __str__(self):
        """ rectangle return """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
