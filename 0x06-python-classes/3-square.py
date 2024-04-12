#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent/Define a square."""

    def __init__(self, size=0):
        """Initializes  new square.

        Args:
            size (int): New square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square's current area"""
        return (self.__size * self.__size)
