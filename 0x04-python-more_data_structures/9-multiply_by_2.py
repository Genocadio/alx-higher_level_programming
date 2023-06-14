#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dct = {}
    for key, value in a_dictionary.items():
        new_dct[key] = value * 2
    return new_dct
