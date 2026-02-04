#!/usr/bin/python3
"""
This module defines a function that checks if an object is
an instance of a class or an instance of a class that
inherits from a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or an instance
    of a class that inherited from, the specified class.
    Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses,
        otherwise False.
    """
    return isinstance(obj, a_class)
