#!/usr/bin/python3
def element_at(my_list, idx):
    while idx < (len(my_list) - 1):
        num = my_list[idx]
        if num > 0:
            print("Element at index {:d} is {:d}".format(idx, num))
        else:
            return None
    else:
        return None
