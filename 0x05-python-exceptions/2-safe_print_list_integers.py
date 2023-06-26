#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        iterator = iter(my_list)
        for _ in range(x):
            try:
                value = next(iterator)
                if isinstance(value, int):
                    print("{:d}".format(value), end=" ")
                    count += 1
            except StopIteration:
                break
        print()
    except TypeError:
        pass
    return count
