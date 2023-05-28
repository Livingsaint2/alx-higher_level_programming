#!/usr/bin/python3
"""This shows how easy is to manipulate json in python"""
import json


def from_json_string(my_str):
    """returns the object representation of an json input.
    Args:
        my_str: Json parsed string.
    Returns:
        object: Object representation of json.
    """
    return (json.loads(my_str))
