#!/usr/bin/python3
"""
Module print_square
Prints a square with the character #.
"""


def print_square(size):
    """Prints a square where size is
    the length and width of the square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for X in range(size):
        for P in range(size):
            print('#', end='')
        print()
