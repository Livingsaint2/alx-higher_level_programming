#!/usr/bin/python3
"""
Starting module to define a rectangle with basegeometry
attributes and methods
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Square class to represent a rect with width and height equal """

    def __init__(self, size):
        """ Instantiate square """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """ Calcs the rect area """
        return (self.__size * self.__size)

    def __str__(self):
        """ Prints width vs height """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
