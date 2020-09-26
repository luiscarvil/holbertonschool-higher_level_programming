#!/usr/bin/python3
"""
matrix_divided - function that divide matrix in num (div)
"""


def matrix_divided(matrix, div):
    """Matrix_divided

    Args:
        matrix (list): matrix with numbers
        div (int or float): num divisor

    Raises:
        TypeError: div must be a number
        ZeroDivisionError: division b zero
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats

    Returns:
        matrix (list): new matrix with the result by arguments divided.
    """
    array = []
    matrix2 = []

    if type(div) is int or type(div) is float:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for j in matrix:
        array = []
        if len(j) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
        for i in j:
            if (type(i) is int or type(i) is float) and type(matrix) == list:
                pass
            else:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            array.append(round(i / div, 2))
        matrix2.append(array)

    return matrix2
