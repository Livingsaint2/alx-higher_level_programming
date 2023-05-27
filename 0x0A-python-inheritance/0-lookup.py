#!/usr/bin/python3
"""
This function return a list of available attributes and methods
of an object
"""


def lookup(obj):
    """lookup description.
    This module demonstrates a way to get attributes from an object.
    Attributes:
        obj: object that we want to return the propertys from.
    """
    return (dir(obj))
