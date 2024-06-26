#!/usr/bin/python3
"""Defines the Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size):
        """Initializes new square.

        Args:
            size (int): New square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
