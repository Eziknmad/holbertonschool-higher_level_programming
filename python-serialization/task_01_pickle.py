#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom object using pickle.
"""

import pickle


class CustomObject:
    """
    Custom object class that supports serialization with pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): File to save the serialized object.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.

        Args:
            filename (str): File containing the serialized object.

        Returns:
            CustomObject or None: Deserialized object or None on failure.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (OSError, pickle.PickleError, EOFError):
            return None
        return None
