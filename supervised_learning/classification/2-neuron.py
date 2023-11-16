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