#!/usr/bin/python3
"""
This module defines a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods available for an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of the object's attributes and methods.
    """
    return dir(obj)
