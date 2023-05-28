#!/usr/bin/python3
""" Converts a file into it's json representation """
import json


def to_json_string(my_obj):
    """returns the json representation of an object.
    Args:
        my_obj: object to be json parsed.
    Returns:
        my_obj json representation or error if something happened.
    """
    return (json.dumps(my_obj))
