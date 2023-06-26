#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
    except ValueError as ve:
        err_msg = "Exception: Unknown format code 'd' for object of type '{}'"
        print(err_msg.format(type(value).__name__), file=sys.stderr)
        return False
