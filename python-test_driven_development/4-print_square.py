#!/usr/bin/python3
"""
Module for printing a square with the character #.

This module provides a function to print a square of a given size
with proper validation and error handling.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square (must be an integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
