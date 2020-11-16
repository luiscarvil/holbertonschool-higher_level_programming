#!/usr/bin/python3
"""
Write a function that returns an object (Python data structure)
"""


import json


def from_json_string(my_str):
    """

    Args:
        my_str (str): [object represented by JSON]

    Returns:
    [object]
    """
    return json.loads(my_str)
