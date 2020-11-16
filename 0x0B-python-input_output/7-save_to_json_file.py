#!/usr/bin/python3
"""
function that writes an object to text file
"""


import json


def save_to_json_file(my_obj, filename):
    """

    Args:
        my_obj: [objecto to writes]
        filename: [text file]
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
