#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    while length > 0:
        print("{:d}".format(my_list[length - 1]))
        length = length - 1
