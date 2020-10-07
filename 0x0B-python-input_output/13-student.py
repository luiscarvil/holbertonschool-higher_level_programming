#!/usr/bin/python3
"""class student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Public method
    """
    def to_json(self, attrs=None):

        if not attrs:
            return self.__dict__
        else:
            new_dict = {}
            for i in self.__dict__:
                if i in attrs:
                    new_dict[i] = self.__dict__[i]
            return new_dict

    """Public method
    """
    def reload_from_json(self, json):

        for i in self.__dict__:
            if i in json:
                self.__dict__[i] = json[i]
