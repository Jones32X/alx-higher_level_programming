#!/usr/bin/python3

"""Defines a MagicClass matching exactly a bytecode."""

import math


class MagicClass:
    """Representation of circle."""

    def __init__(self, radius=0):
        """MagicClass is Initialized.

        Arg:
            radius (float or int): MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns MagicClass's area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns MagicClass's circumference."""
        return (2 * math.pi * self.__radius)
