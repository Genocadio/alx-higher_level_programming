#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    n = len(keys)

    # Manual sorting
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    # Print dictionary by ordered keys
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
