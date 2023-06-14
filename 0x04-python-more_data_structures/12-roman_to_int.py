#!/usr/bin/python3
def roman_to_int(roman_string):
    values = [1, 5, 10, 50, 100, 500, 1000]
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for letter in roman_string:
        if letter not in symbols:
            return 0
    result = 0
    n = len(roman_string)
    for i in range(n):
        current = values[symbols.index(roman_string[i])]
        if i + 1 < n:
            next_val = values[symbols.index(roman_string[i + 1])]
            if current < next_val:
                result -= current
            else:
                result += current
        else:
            result += current

    return result
