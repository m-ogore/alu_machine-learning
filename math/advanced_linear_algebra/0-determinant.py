#!/usr/bin/env python3

'''
        0. Determinant
        Level: 0
        Auto review
        Write a function def determinant(matrix): that calculates the determinant of a matrix:
        matrix is a list of lists whose determinant should be calculated
        If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
        If matrix is not square, raise a ValueError with the message matrix must be a square matrix
        The list [[]] represents a 0x0 matrix
        Returns: the determinant of matrix

'''

def determinant(matrix):
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')
    #if not (len(matrix) == len(matrix[0])):
     #   raise ValueError('matrix must be a square matrix')
    if len(matrix) == 0 or matrix == [[]]:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2: #2 x 2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(len(matrix)):

        for row in range(len(matrix)):
            submatrix = row[:col] + row[col+1:]
            cofactor = matrix[0][col] * determinant(submatrix)
            if col % 2 == 0:
                det += cofactor
            else:
                det -= cofactor
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        cofactor = matrix[0][col] * determinant(submatrix)
        if col % 2 == 0:
            det += cofactor
        else:
            det -= cofactor
    return det

