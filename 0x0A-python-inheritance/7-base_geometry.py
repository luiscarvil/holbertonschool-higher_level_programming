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
