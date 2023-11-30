#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    c = 0
    for n in sys.argv:
        c = c + 1
        if c == 1:
            continue
        else:
            number = int(n)
            sum = sum + number
    print("{}".format(sum))
