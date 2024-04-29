#!/usr/bin/python3
"""Defines the function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds new attribute to an object if possible.

    Args:
        obj (any): Object to add an attribute to.
        att (str): Attribute name to add to obj.
        value (any): Attribute value.
    Raises:
        TypeError: When the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
