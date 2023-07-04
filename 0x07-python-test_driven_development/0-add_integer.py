#!/usr/bin/python3
"""
module to add two integers
adds to integers a and b

"""


def add_integer(a, b=98):
    """returns sum of a and b both integers
    raises a TypeError if either a or b is not an integer or not a float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    if type(b) == float:
        b = int(b)
    if type(a) == float:
        a = int(a)
    return a + b
