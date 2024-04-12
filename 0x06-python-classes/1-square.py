#!/usr/bin/python3
"""Represents a class Square"""


class Square:
    """
    Defines properties of square by: (based on 0-square.py).

    Attributes:
        size: square size (ONE side).
    """
    def __init__(self, size):
        """Makes instances of square (ONE side).

        Args:
            size: square size.
        """
        self.__size = size
