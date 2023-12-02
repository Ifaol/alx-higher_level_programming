#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = 0
    leng = len(my_list)
    if leng == 0:
        return None
    else:
        for i in my_list:
            if int(i) > maxi:
                maxi = i
    return maxi
