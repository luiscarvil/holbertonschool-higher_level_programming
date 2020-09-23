#!/usr/bin/python3
"""
method square - defines a square.
"""


class Square:
    """
    class square init size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        else:
            self.__size = value

    @property
    def position(self):
        """
        return the value position tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or\
           value[0] < 0 or value[1] < 0:
            """
            raise error TypeError and push menssage
            """
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        return pow area size
        """
        return(self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        elif self.__position[1] >= 0:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
