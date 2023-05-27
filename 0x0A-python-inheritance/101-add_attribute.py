#!/usr/bin/python3
"""
Module to check if an object can be assigned
with new attributes
"""


def add_attribute(instance, attribute, value):
    """
    Function to add new attributes in a function
    """
    if not hasattr(instance, "__dict__"):
        raise TypeError("can't add new attribute")
    elif hasattr(instance, "__slots__") and not hasattr(instance, attribute):
        raise TypeError("can't add new attribute")
    setattr(instance, attribute, value)
