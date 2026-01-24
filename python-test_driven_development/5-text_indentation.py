#!/usr/bin/python3
"""
Module for text indentation.

This module provides a function to print text with 2 new lines
after each of these characters: . ? :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? and :.

    Args:
        text: The text to print (must be a string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
