#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        leng = len(i)
        if leng == 0:
            print()
            break
        c = 1
        for j in i:
            if leng != c:
                print("{:d}".format(j),  end=" ")
                c = c + 1
            else:
                print("{:d}".format(j))
