#!/usr/bin/python3
def uppercase(str):
    for c in str:
        val = ord(c)
        if val >= 97 and val <= 122:
            print("{}".format(chr(val - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
