#usr/bin/env python3
'''
    Write a class Neuron that defines a single neuron performing binary classification (Based on 2-neuron.py):

    Add the public method def cost(self, Y, A):
    Calculates the cost of the model using logistic regression
    Y is a numpy.ndarray with shape (1, m) that contains the correct labels for the input data
    A is a numpy.ndarray with shape (1, m) containing the activated output of the neuron for each example
    To avoid division by zero errors, please use 1.0000001 - A instead of 1 - A
    Returns the cost
'''

#!/usr/bin/env python3

import numpy as np

class Neuron:
    """
    Class representing a single neuron performing binary classification.
    """

    def __init__(self, nx):
        """
        Initialize a Neuron instance.

        Args:
        - nx (int): Number of input features.

        Attributes:
        - __W (numpy.ndarray): The weights vector for the neuron.
        - __b (float): The bias for the neuron.
        - __A (float): The activated output of the neuron (prediction).
        """
        self.nx = nx
        self.__W = np.random.randn(1, self.nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter method for weights."""
        return self.__W

    @property
    def b(self):
        """Getter method for bias."""
        return self.__b

    @property
    def A(self):
        """Getter method for activated output."""
        return self.__A

    def forward_prop(self, X):
        """
        Perform forward propagation for the neuron.

        Args:
        - X (numpy.ndarray): Input data (shape: (nx, m)).

        Returns:
        - numpy.ndarray: Activated output of the neuron.
        """
        weighted_sum = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-weighted_sum))
        return self.__A
    def cost(self, Y, A):
        """

        Calculates the cost of the model using logistic regression
        Y is a numpy.ndarray with shape (1, m) that contains the correct labels for the input data
        A is a numpy.ndarray with shape (1, m) containing the activated output of the neuron for each example
        To avoid division by zero errors, please use 1.0000001 - A instead of 1 - A
        Returns the cost
    
        """
        #https://www.analyticsvidhya.com/blog/2020/11/binary-cross-entropy-aka-log-loss-the-cost-function-used-in-logistic-regression/
        return -1 / Y.shape[1]* np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))

