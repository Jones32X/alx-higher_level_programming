#!/usr/bin/python3
"""Def the class Student."""


class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student.

        Args:
            first_name (str): Student First name.
            last_name (str): Student last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get Student dictionary representation.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Not mandtory) Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces  attributes of the Student.

        Args:
            json (dict): key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
