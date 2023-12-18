#!/usr/bin/python3
def safe_print_integer(value):
    bol = True
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        bol = False
    return bol
