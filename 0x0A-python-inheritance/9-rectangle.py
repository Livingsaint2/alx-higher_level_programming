#!/usr/bin/python3
"""
Starting module to define a rectangle with basegeometry
attributes and methods
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Template for a rectangle with rules of basegeometry"""

    def __init__(self, width, height):
        """ Instantiate rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calcs the rect area """
        return (self.__width * self.__height)

    def __str__(self):
        """ Prints width vs height """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
