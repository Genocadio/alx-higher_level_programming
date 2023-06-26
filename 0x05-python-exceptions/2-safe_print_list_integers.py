#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            try:
                print("{:d}".format(int(value)), end=" ")
                count += 1
            except ValueError:
                continue
        print()
    except IndexError:
        pass
    return count
