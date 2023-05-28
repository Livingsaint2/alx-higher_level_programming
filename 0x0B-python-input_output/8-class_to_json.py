#!/usr/bin/python3
"""this file receives the standard input"""


def class_to_json(obj):
    """this shows the attributes and methods of a class
    in json
    """
    return(obj.__dict__)
