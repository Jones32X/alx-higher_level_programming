#!/usr/bin/python3
""" Text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing given string in a file.

    Args:
        filename (str): File Name.
        search_string (str): String to search for in file.
        new_string (str): String to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
