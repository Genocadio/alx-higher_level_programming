#!/usr/bin/python3
def element_at(my_list, idx):
    while idx < (len(my_list) - 1):
        if my_list[idx] > 0:
            return my_list[idx]
        else:
            return None
    else:
        return None
