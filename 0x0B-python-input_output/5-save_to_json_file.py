#!/usr/bin/python3
"""import json"""
import json


def save_to_json_file(my_obj, filename):
    """This function returns the JSON representation of an object (string)"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
