#!/usr/bin/python3
"""module to indent text"""


def text_indentation(text):
    """
    function to print new line after each of these characters: .?
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ".:?":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
    print("{}".format(text), end="")
