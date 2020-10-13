#!/usr/bin/python3
"""
module Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    defines contructor and instance attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init attributes constructor """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        self.validations("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter width """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter width """
        self.validations("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter width """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter width """
        self.validations("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter width """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter width """
        self.validations("y", value)
        self.__y = value

    def validations(self, name, value):
        """ validation inputs """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """ Getter Area
        """
        return self.__width * self.__height

    def display(self):
        """ print rectangle """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """ print values """
        return ("[Rectangle] ({:d})) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ update values """
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                setattr(self, i, j)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """ define dictionary to rectangle """
        dict_ = {}
        array = ["id", "width", "height", "x", "y"]
        for i in array:
            dict_[i] = getattr(self, i)
        return dict_
