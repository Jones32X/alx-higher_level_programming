#!/usr/bin/python3
"""Defs Python class-to-JSON function."""


def class_to_json(obj):
    """Returns dictionary represntation of a simple data structure."""
    return obj.__dict__
