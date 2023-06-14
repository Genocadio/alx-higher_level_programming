#!/usr/bin/python3
def weight_average(my_list=[]):
    var = 0
    wei = 0
    for tup in my_list:
        var += tup[0] * tup[1]
        wei += tup[1]

    return (var / wei)
