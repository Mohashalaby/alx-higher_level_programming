#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda New_Matrix: list(map(lambda x: x**2, New_Matrix)), matrix))
