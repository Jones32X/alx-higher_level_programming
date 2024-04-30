#!/usr/bin/python3
""" function reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """Prints contents of a UTF8 text file to stdout."""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
