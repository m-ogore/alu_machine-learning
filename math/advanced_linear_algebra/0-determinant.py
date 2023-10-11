#!/usr/bin/env python3
import numpy as np
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
               
