#!/usr/bin/python3
"""
module to divide matrix
"""


def matrix_divided(matrix, div):
    """returns matrix divided by div
        assumes matrix is a list of lists
    """
    erro = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(erro)
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(erro)
        if len(matrix[i]) != len(matrix[0]):
            err = "Each row of the matrix must have the same size"
            raise TypeError(err)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError(erro)
            if type(div) != int and type(div) != float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            matrix[i][j] = round(matrix[i][j] / div, 2)
    return matrix
