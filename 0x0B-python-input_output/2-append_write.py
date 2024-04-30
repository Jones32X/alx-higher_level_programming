#!/usr/bin/python3
"""File-appending function."""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file.

    Args:
        filename (str): File name to append to.
        text (str): String to append to the file.
    Returns:
        Num of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
