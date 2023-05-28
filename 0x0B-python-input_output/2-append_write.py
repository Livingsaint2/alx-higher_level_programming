#!/usr/bin/python3
"""File manipulation to create or append text to a file"""


def append_write(filename="", text=""):
    """Writes text into a file.
    Args:
        filename: path to the file that wants to be written.
        text: string to be input inside the file
    Returns:
        Nothing.
    """
    with open(filename, "a") as my_file:
        nb_char = my_file.write(str(text))
    my_file.close()
    return (nb_char)
