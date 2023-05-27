#!/usr/bin/python3
"""
Starting module to define a rectangle with basegeometry
attributes and methods
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Template for a rectangle with rules of basegeometry"""

    def __init__(self, width, height):
        """ Prints width vs height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
