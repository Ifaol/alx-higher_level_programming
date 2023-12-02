#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    c = 0
    d = 0
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 >= 2:
        a = int(tuple_a[0])
        b = int(tuple_a[1])
    elif len1 == 1:
        a = int(tuple_a[0])
    if len2 >= 2:
        c = int(tuple_b[0])
        d = int(tuple_b[1])
    elif len2 == 1:
        c = int(tuple_b[0])
    return (a + c, b + d)
