#!/usr/bin/python3
""" module MyList """


class MyList(list):
    """
    function print version list sorted
    """
    def print_sorted(self):
        print(sorted(self))
