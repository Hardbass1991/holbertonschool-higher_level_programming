#!/usr/bin/python3
"""Module featuring a function that divides elements in a matrix
"""


def matrix_divided(matrix, div):
    """Function that divides elements in a matrix by input number

    Args:
        matrix: input matrix
        div: input number
    """
    new_mat = []
    TE_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        if type(i) != list:
            raise TypeError(TE_msg)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(TE_msg)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif type(div) == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j] / div, 2))
        new_mat.append(row)
    return new_mat
