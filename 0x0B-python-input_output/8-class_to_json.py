#!/usr/bin/python3
"""module for function class_to_json"""


def class_to_json(obj):
    """This function returns the JSON representation of an object (string)"""
    return obj.__dict__
