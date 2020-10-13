#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """ inicialization atributes """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update values """
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                setattr(self, i, j)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        define dictionary to Square
        """
        dict_ = {}
        array = ["id", "size", "x", "y"]
        for i in array:
            dict_[i] = getattr(self, i)
        return dict_
