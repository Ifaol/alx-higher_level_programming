#!/usr/bin/python3
for i in range(122, 96, -1):
    val = i % 2
    if val != 0:
        char = chr(i - 32)
    else:
        char = chr(i)
    print("{}".format(char), end="")
