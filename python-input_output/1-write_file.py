#!/usr/bin/python3
"""Module that defines a function to write a string to a UTF8 text file."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
