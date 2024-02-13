#!/usr/bin/env python3
import numpy as np

def shuffle_data(X, Y):
    '''
    X is the input data to be shuffled
    Y is the corresponding correct labels to X
    '''
    m = X.shape[0]
    permutation = list(np.random.permutation(m))
    shuffled_X = X[permutation, :]
    shuffled_Y = Y[permutation, :].reshape((m, Y.shape[1]))
    
    return shuffled_X, shuffled_Y