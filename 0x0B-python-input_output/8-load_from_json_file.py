#!/usr/bin/python3
"""
creates an object from JSON
"""


import json


def load_from_json_file(filename):
    """

    Args:
        filename: [name to the text file]

    Returns:
        [creates object]
    """
    with open(filename, 'r') as f:
        return json.load(f)
