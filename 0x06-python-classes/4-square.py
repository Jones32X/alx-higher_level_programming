#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Defines/Represents a square."""

    def __init__(self, size=0):
        """Initializes  new square.

        Args:
            size (int): New square size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square ara."""
        return (self.__size * self.__size)
