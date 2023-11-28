#!/usr/bin/python3
def uppercase(str):
    for c in str:
        val = ord(c)
        if val >= 97 and val <= 122:
            char = chr(val - 32)
        else:
            char = c
        print("{}".format(char), end="")
    print()
