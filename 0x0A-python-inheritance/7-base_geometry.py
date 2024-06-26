#!/usr/bin/python3
"""Defines base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsents base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): Name of the parameter.
            value (int): Parameter to validate.
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
