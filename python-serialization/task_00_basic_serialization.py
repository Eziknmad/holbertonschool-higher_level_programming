#!/usr/bin/env python3
"""
Basic serialization module.
Provides functions to serialize a Python dictionary to a JSON file
and deserialize it back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized JSON data.
    """
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
