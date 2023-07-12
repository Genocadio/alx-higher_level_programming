#!/usr/bin/python3
"""module for add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    """adds an attribute to an object"""
    if not hasattr(obj, '__dict__'):
        """if can't add attribute"""
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
