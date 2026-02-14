#!/usr/bin/python3
"""Defines a Student class with JSON serialization and deserialization"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the instance
        If attrs is a list of strings, only return those attributes
        """
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance using a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
