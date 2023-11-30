#!/usr/bin/python3
"""
This function takes matrix(list of lists)
and div(int or float).
"""


def matrix_divided(matrix, div):
    """
    Function to divide elents of a matrix by div.
    """
    new_matrix = []
    x = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for n in range(len(matrix) - 1):
        if len(matrix[n]) != len(matrix[n + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    for el in matrix:
        if type(el) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for y in el:
            if type(y) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = list(map(lambda r: list(map(lambda x: round(x / div, 2) if x != 0 else 0.00, r)), matrix))
    return new_matrix
