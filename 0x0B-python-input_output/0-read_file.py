#!/usr/bin/python3
"""Write to a file"""

#!/usr/bin/python3
"""file manipulation using python"""


def read_file(filename=""):
    """Read file template function.
    Args:
        filename: path to the file that wants to be read.
    Returns:
        Nothing.
    """
    with open(filename, "r") as my_file:
        print(my_file.read(), end="")
    my_file.close()
