#!/usr/bin/env python3
'''import numpy as np
#A function to calculate `determinant`
def determinant(matrix):

    matrix = np.array(matrix)
    #if not isinstance(matrix, list) or 
    if matrix.shape == (0,):
        raise ValueError('matrix must be a list of lists')
    #hat takes a square matrix as input and returns the determinant of the matrix. The function first checks if the matrix is a square matrix and if it is a 2x2 matrix. If it is, the function calculates the determinant directly. If the matrix is larger, the function 
    if len(matrix.shape) != 2 and matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix is not square")
                          
    if len(matrix[0]) == 0:
        return 1
    if len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix) == 2 :
        #calculate directly
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    
    
    
    determinant = np.linalg.det(matrix)
    return determinant
   '''            
def minor(matrix, row, col):
    # Helper function to obtain the minor matrix after removing the specified row and column
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

def determinant(matrix):
    # Check if the input matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError('matrix must be a list of lists')

    # Check if the matrix is square
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if num_rows != num_cols:
        raise ValueError('Matrix is not square')

    # Base case: If the matrix is 1x1, return the single element
    if num_rows == 1:
        return matrix[0][0]

    # Base case: If the matrix is 2x2, return the determinant using the cross-product method
    if num_rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(num_cols):
        det += matrix[0][col] * determinant(minor(matrix, 0, col)) * (-1) ** col

    return det

