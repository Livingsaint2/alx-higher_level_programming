#!/usr/bin/python3
"""
This module checks if an object inherits from a class
"""


def inherits_from(obj, a_class):
    """function to detect if an object inherits_from.
    Args:
        obj (obj): the first object.
        a_class (str): class to know if the object inherits from it.
    Returns:
        bool: True for success, False otherwise.
    """
    if (type(obj) is not a_class):
        return (issubclass(type(obj), a_class))
    else:
        return (False)
