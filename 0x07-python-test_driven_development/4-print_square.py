#!/usr/bin/python3
"""module to print square
prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #
    the size must be an integer
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
