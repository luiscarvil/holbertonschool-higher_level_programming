#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        c = 0
        for j in i:
            c = c + 1
            if len(i) == c:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print()
