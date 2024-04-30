#!/usr/bin/python3
"""Defines the class Student."""


class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): Student Fisrt name.
            last_name (str): Student Last name.
            age (int): Student Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, then represents only the attributes
        included in the list.

        Args:
            attrs (list):  (not Mandtory) attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
