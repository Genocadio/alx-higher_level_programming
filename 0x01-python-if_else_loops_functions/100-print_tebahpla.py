#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c)), end="")
    print("{}".format(chr(c - 32)), end="")
