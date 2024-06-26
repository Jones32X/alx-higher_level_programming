#!/usr/bin/python3
"""Defines file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        Filename (str): File name to write.
        text (str): Text to write to file.
    Returns:
        Num of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
