#!/usr/bin/python3
"""import json"""
import json


def load_from_json_file(filename):
    """This function returns the JSON representation of an object (string)"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
