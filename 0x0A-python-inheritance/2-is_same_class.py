#!/usr/bin/python3
"""
This module checks if an object is instance of some class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is instance of a_class, else false
    """
    return (type(obj) == a_class)
