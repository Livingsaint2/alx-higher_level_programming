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

    def to_json(self, attr=None):
        """Returns dict of students"""
        if type(attr) is not list:
            return(self.__dict__)
        if (not all(isinstance(items, str) for items in attr)):
            return(self.__dict__)
        result = {}
        return({key: self.__dict__[key] for
                key in self.__dict__.keys() & attr})

    def reload_from_json(self, json):
        """Loads attributes in this instance"""
        if json:
            self.__dict__ = json
