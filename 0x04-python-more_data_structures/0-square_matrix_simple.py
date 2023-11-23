#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    fresh_matrix = matrix.copy()

    for n in range(len(matrix)):
        fresh_matrix[n] = list(map(lambda x: x**2, matrix[n]))

    return fresh_matrix
~

