#!/usr/bin/python3
"""
Here we use python inheritance with a int object
"""


class MyInt(int):
    """
    This class mimics the int behavior with
    but operators are reversed
    """

    def __init__(self, value):
        """
        Init Mylist with int params
        """
        int.__init__(self)
        self.value = value

    def __eq__(self, other):
        """
        Reverse equal operation
        """
        if (self.value == other):
            return False
        else:
            return True

    def __ne__(self, other):
        """
        Reverse not equal operation
        """
        if (self.value != other):
            return False
        else:
            return True
