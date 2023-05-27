#!/usr/bin/python3
"""
This module checks if an object is instance of some class and subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is instance of a_class
    or subclass, else false
    """
    return (isinstance(obj, a_class))
