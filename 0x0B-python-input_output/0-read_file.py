#!/usr/bin/python3
"""a script that write to a file"""


def write_file(filename="", text=""):
    """Write to a UTF8 text file.
    Args:
        filename (str): The file name.
        text (str): The text to write to the file.
    Returns:
         characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
