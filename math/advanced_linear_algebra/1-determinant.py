#!/usr/bin/env python3
       
def determinant(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return TypeError('matrix must be a list of lists')

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        return TypeError('matrix must be a square matrix')

    if num_rows == 0:  # Special case for a 0x0 matrix
        return 1

    if num_rows == 1:  # Special case for a 1x1 matrix
        return matrix[0][0]

    if num_rows == 2:  # Special case for a 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(num_cols):
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        cofactor = matrix[0][col] * determinant(submatrix)
        if col % 2 == 0:  # Add for even columns, subtract for odd columns
            det += cofactor
        else:
            det -= cofactor

    return det
