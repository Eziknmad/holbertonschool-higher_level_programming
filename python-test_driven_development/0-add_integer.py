#!/usr/bin/python3
"""
Module that provides a function to add two integers.
Handles type validation and casting as specified.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.

    a and b must be integers or floats; otherwise, raise a TypeError.
    Floats are cast to integers before addition.

    Raises:
        TypeError: if a or b is not an integer or float, or
                   if a or b is NaN or infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN or Infinity for 'a'
    if isinstance(a, float):
        if a != a or a == float('inf') or a == float('-inf'):
            raise TypeError("a must be an integer")

    # Check for NaN or Infinity for 'b'
    if isinstance(b, float):
        if b != b or b == float('inf') or b == float('-inf'):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
