#!/usr/bin/python3
""" module comparitions """


class MyInt(int):
    """ swapped == and =! """
    def __eq__(self, value):
        """ return opposite """
        return (int(self) != int(value))

    def __ne__(self, value):
        """ return opposite """
        return(int(self) == int(value))
