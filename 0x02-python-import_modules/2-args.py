#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument.")
    else:
        print("{} arguments".format(num_arguments), end="")
        print(":")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

    print()
