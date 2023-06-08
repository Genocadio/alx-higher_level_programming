import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("{} arguments".format(num_arguments), end="")
    if num_arguments == 0:
        print(".", end="")
    else:
        print(":")
        for i, arg in enumerate(arguments):
            print("{}: {}".format(i + 1, arg))

    print()
