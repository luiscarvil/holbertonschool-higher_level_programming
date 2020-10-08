#!/usr/bin/python3
"""append after open and write
"""


def append_after(filename="", search_string="", new_string=""):
    """append method
    """
    new_str = ""
    with open(filename, encoding="utf-8") as f:
        for i in f:
            if search_string in i:
                new_str += new_string
            else:
                new_str += i
    with open(filename, 'w') as f:
        f.write(new_str)
