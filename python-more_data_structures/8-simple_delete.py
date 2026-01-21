#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete key from a_dictionary if it exists, then return the dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
