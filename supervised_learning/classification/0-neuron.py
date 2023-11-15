#!/usr/bin/env python3

import numpy as np

'''
class constructor: def __init__(self, nx):
nx is the number of input features to the neuron
If nx is not an integer, raise a TypeError with the exception: nx must be an integer
If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer
All exceptions should be raised in the order listed above
Public instance attributes:
W: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
b: The bias for the neuron. Upon instantiation, it should be initialized to 0.
A: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.

'''
class Neuron:
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        
        self.nx = nx
        self.W = np.random.normal(size=(nx,))
        self.b = 0
        self.A = 0
lib_train = np.load('../data/Binary_Train.npz') #/home/seer/alu-machine_learning/supervised_learning/data
X_3D, Y = lib_train['X'], lib_train['Y']
X = X_3D.reshape((X_3D.shape[0], -1)).T

np.random.seed(0)
neuron = Neuron(X.shape[0])
print(neuron.W)
print(neuron.W.shape)
print(neuron.b)
print(neuron.A)
neuron.A = 10
print(neuron.A)

