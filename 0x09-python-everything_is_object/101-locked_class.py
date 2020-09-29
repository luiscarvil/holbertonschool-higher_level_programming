#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass:
    """
    New class with no ibject attribute
    """
    def __setattr__(self, attribute, value):
        if attribute != "first_name":
            raise AttributeError("'LockedClass' object has \
no attribute 'last_name'")
        else:
            self.__dict__[attribute] = ValueError
