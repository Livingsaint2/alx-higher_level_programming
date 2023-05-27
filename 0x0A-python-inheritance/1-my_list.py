#!/usr/bin/python3
"""
Here we use python inheritance with a list object
"""


class MyList(list):
    """
    This class mimics the list behavior with
    a new component
    """

    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        print(sorted(self))
