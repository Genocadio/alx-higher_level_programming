#!/usr/bin/python3
"""this module appends a text file (UTF8)"""


def append_write(filename="", text=""):
    """This function appends a text file (UTF8)"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
