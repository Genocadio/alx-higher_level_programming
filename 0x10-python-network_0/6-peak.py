#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """"finds a peak in a list of unsorted integers."""
    li = list_of_integers
    length = len(li)
    if length == 0:
        return
    mid = length // 2
    if (mid == length - 1 or li[mid] >= li[mid + 1]) and\
       (mid == 0 or li[mid] >= li[mid - 1]):
        return li[mid]
    elif mid != length - 1 and li[mid + 1] > li[mid]:
        return find_peak(li[mid + 1:])
    return find_peak(li[:mid])
