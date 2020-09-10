#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in matrix:
        for j in i:
            matrix2.append(j*j)
    return(matrix2)
