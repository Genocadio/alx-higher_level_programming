#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = list(map(lambda x: x ** 2, row))
        result.append(new_row)
    return result
