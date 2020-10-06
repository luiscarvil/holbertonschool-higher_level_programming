#!/usr/bin/python3
""" contains inherits_from funtion """


def inherits_from(obj, a_class):
    """
    return true  if the object is an isintance class inherited othr False
    """
    return isinstance(obj, a_class) if type(obj) != a_class else False
