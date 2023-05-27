#!/usr/bin/python3
"""
Starting module to define base geometry class
"""


class BaseGeometry():
    """"
    Template for a base geometry object
    """
    def __init__(self):
        """ Initial constructor space """
        pass

    def area(self):
        """ Space to calculate the area (in progress) """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer number """
        if (type(value) is not int):
            raise TypeError(str(name) + " must be an integer")
        if (value <= 0):
            raise ValueError(str(name) + " must be greater than 0")
