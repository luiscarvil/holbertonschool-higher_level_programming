#!/usr/bin/python3
"""
function that reads n lines of a text file (UTF8)
"""


def read_lines(filename="", nb_lines=0):
    """
    Args:
        filename (str): [name file to open and read].
        nb_lines (int): [counter number lines].
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            read_data = f.read()
            print(read_data, end='')
        else:
            for i in range(nb_lines):
                read_data = f.readline()
                print(read_data, end="")
