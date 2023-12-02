#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leng = len(my_list)
    if leng != 0:
        if leng == 1:
            print("{:d}".format(my_list[0]))
        else:
            while leng > 0:
                print("{:d}".format(my_list[leng - 1]))
                leng = leng - 1
