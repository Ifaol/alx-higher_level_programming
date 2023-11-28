#!/usr/bin/python3
def remove_char_at(str, n):
    leng =  len(str)
    if n < 0 or n > leng:
        return str
    else:
        return str[:n] + str[n + 1:]
