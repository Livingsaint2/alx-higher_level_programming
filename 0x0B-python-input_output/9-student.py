#!/usr/bin/python3
"""
Example of creation of class student
"""


class Student():
    """
    This template represents a student
    """
    def __init__(self, first_name, last_name, age):
        """Constructor for students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict of students"""
        return(self.__dict__)
