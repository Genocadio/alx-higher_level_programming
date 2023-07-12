#!/usr/bin/python3
"""module for function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if the object is an inheritance of class, else False"""
    return issubclass(type(obj), a_class)
