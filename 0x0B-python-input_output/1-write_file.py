#!/usr/bin/python3
"""File manipulation to create or write a file"""


def write_file(filename="", text=""):
    """Writes text into a file.
    Args:
        filename: path to the file that wants to be written.
        text: string to be input inside the file
    Returns:
        Nothing.
    """
    with open(filename, "w") as my_file:
        nb_char = my_file.write(len(text))
    my_file.close()
    return (nb_char))
