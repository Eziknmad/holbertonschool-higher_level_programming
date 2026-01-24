#!/usr/bin/python3
"""
Module for adding two integers.

This module provides a function to add two numbers after
ensuring they are integers or can be converted to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        int: The addition of a and b as integers

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a:
            raise ValueError("cannot convert float NaN to integer")
        if a == float('inf') or a == float('-inf'):
            raise OverflowError(
                "cannot convert float infinity to integer"
            )

    if isinstance(b, float):
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        if b == float('inf') or b == float('-inf'):
            raise OverflowError(
                "cannot convert float infinity to integer"
            )

    return int(a) + int(b)
