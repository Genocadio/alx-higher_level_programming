#!/usr/bin/python3
"""This module writes a text file (UTF8)"""


def write_file(filename="", text=""):
    """This function writes a text file (UTF8)"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
