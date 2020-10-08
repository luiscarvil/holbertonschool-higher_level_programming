#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        new_str = ""
        for i in f:
            if search_string in i:
                new_str += new_string
            else:
                new_str += i
    with open(filename, 'w') as f:
        f.write(new_str)