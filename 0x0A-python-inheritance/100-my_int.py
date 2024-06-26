#!/usr/bin/python3
"""Defines the class MyInt that inherits from int."""


class MyInt(int):
    """Inverts the int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
