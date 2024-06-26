#!/usr/bin/python3

"""Represents a class Square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes Square.

        Args:
            size (int): new square size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
