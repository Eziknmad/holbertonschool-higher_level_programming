#!/usr/bin/python3
"""
This module defines a class that inherits from list and adds
a method to print the list in sorted order.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list.

    Provides a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order without
        modifying the original list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
