#!/usr/bin/python3
"""
function that returns the JSON repres object(str)
"""


import json


def to_json_string(my_obj):
    """
    use json.dumps
    """
    data_read = json.dumps(my_obj)
    return data_read
