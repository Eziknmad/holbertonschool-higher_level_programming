#!/usr/bin/python3
"""
Module that provides a function to add two integers.
Handles type validation and casting as specified.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.

    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
