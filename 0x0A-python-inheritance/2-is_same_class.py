#!/usr/bin/python3
"""module for is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of class, else False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
