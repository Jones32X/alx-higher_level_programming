#!/usr/bin/python3
"""Modle creates a class named Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square
    Attributes:
    attr1(size): size of square
    attr2(area): finds the area of it
    """
    def __init__(self, size):
        """Initializes instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns informal string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)

