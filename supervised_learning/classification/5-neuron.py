#!/usr/bin/python3
'''
Write a class Neuron that defines a single neuron performing binary classification (Based on 4-neuron.py):

Add the public method def gradient_descent(self, X, Y, A, alpha=0.05):
Calculates one pass of gradient descent on the neuron
X is a numpy.ndarray with shape (nx, m) that contains the input data
nx is the number of input features to the neuron
m is the number of examples
Y is a numpy.ndarray with shape (1, m) that contains the correct labels for the input data
A is a numpy.ndarray with shape (1, m) containing the activated output of the neuron for each example
alpha is the learning rate
Updates the private attributes __W and __b
'''
import numpy as np
class Neuron:

    def gradient_descent(self, X, Y, A, alpha = 0.05):
        nx, m = X.shape

        Y.shape = (1,m)
        A.shape = (1,m)

        w = w - alpha(da/dz*d(np.matmul(w,x)+b)/dw) 

        b = b - alpha(da/dz*dz/db) 