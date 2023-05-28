#!/usr/bin/python3
"""File manipulation to get number of lines"""


def number_of_lines(filename=""):
    """Reads the number of lines.
    Args:
        filename: path to the file that wants to be read.
    Returns:
        counter: number of lines of file.
    """
    counter = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            counter += 1
    my_file.close()
    return (counter)
