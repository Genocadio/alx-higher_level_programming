#!/usr/bin/python3
def roman_to_int(roman_string):
    values = [1, 5, 10, 50, 100, 500, 1000]
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for letter in roman_string:
        if letter not in symbols:
            return 0
    roman = 0
    n = len(roman_string)
    for i in range(n):
        temp = 0
        for j in range(7):
            if symbols[j] == roman_string[i]:
                temp = values[j]
                break
        if i + 1 < n:
            next_val = 0
            for k in range(7):
                if symbols[k] == roman_string[i + 1]:
                    next_val = values[k]
                    break
            if temp < next_val:
                roman -= temp
            else:
                roman += temp
        else:
            roman += temp
    return roman
