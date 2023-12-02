#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return None
    else:
        new_list = my_list.copy()
        j = -1
        for i in my_list:
            j = j + 1
            if int(i) % 2 == 0:
                new_list[j] = True
            else:
                new_list[j] = False
    return new_list
