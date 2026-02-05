#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an area method
that is not implemented.
"""


class BaseGeometry:
    """
    A base class for geometry objects.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")
