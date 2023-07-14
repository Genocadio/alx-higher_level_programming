#!/usr/bin/python3
"""module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that appends a line of text to a file"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if search_string in line:
                f.write(line)
            f.write(new_string)
