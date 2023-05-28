#!/usr/bin/python3
"""This file saves an obj in json format"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object in json representation.
    Args:
        my_obj: object to be json parsed.
        filename: file to store json parsed info.
    Returns:
        Nothing.
    """
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(my_obj))
    json_file.close()
