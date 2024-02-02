#!/usr/bin/env python3
'''
    Write the function def normalization_constants(X):
      that calculates the normalization (standardization) constants of a matrix:

    X is the numpy.ndarray of shape (m, nx) to normalize
    m is the number of data points
    nx is the number of features
    Returns: the mean and standard deviation of each feature, respectively

'''
import numpy as np
def normalization_constants(X):
    '''
    X is the numpy.ndarray of shape (m, nx) to normalize
    m is the number of data points
    nx is the number of features
    Returns: the mean and standard deviation of each feature, respectively
    '''
    '''
    m = X.shape[0]
    nx = X.shape[1]
    X = np.array(X, shape =(m, nx))
    '''
    mean = np.mean(X, axis=0) 
    std = np.std(X, axis=0)

    return mean,std
    