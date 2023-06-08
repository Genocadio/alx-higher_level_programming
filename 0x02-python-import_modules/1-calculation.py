#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    result = add(a, b)
    diff = sub(a, b)
    prod = mul(a, b)
    divid = div(a, b)
    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, prod))
    print("{} / {} = {}".format(a, b, divid))
