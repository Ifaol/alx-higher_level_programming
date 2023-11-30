#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    i = 0
    if n == 1:
        print("{} arguments.".format(n - 1))
    elif n == 2:
        print("{} argument:".format(n - 1))
        print("{}: {}".format(i + 1, sys.argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        for s in sys.argv:
            i = i + 1
            if i == 1:
                continue
            else:
                print("{}: {}".format(i - 1, s))
