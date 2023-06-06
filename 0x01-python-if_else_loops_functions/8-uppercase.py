#!/usr/bin/python3
def uppercase(string):
    result = ""
    for char in string:
        uppercase_char = chr(ord(char) & ~32) if 'a' <= char <= 'z' else char
        result += "{}".format(uppercase_char)
    print(result)
