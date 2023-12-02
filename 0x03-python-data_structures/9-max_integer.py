#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return None
    else:
        maxi = int(my_list[0])
        for i in my_list:
            if int(i) > maxi:
                maxi = i
    return maxi
