#!/usr/bin/python3
"""Defs a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student.

        Args:
            first_name (str): First student name.
            last_name (str): Student last name.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obtains Student dictionary representation."""
        return self.__dict__
