#!/usr/bin/python3
"""This module reads a text file (UTF8)"""


def read_file(filename=""):
    """This function reads a text file (UTF8)"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
