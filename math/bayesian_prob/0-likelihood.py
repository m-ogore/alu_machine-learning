#!/usr/bin/env python3

'''
You are conducting a study on a revolutionary cancer drug and are looking to find the probability that a patient who takes this drug will develop severe side effects. During your trials, n patients take the drug and x patients develop severe side effects. You can assume that x follows a binomial distribution.

Write a function def likelihood(x, n, P): that calculates the likelihood of obtaining this data given various hypothetical probabilities of developing severe side effects:

x is the number of patients that develop severe side effects
n is the total number of patients observed
P is a 1D numpy.ndarray containing the various hypothetical probabilities of developing severe side effects
If n is not a positive integer, raise a ValueError with the message n must be a positive integer
If x is not an integer that is greater than or equal to 0, raise a ValueError with the message x must be an integer that is greater than or equal to 0
If x is greater than n, raise a ValueError with the message x cannot be greater than n
If P is not a 1D numpy.ndarray, raise a TypeError with the message P must be a 1D numpy.ndarray
If any value in P is not in the range [0, 1], raise a ValueError with the message All values in P must be in the range [0, 1]
Returns: a 1D numpy.ndarray containing the likelihood of obtaining the data, x and n, for each probability in P, respectively


'''

import numpy as np

def likelihood(x, n, P):
    # n must be a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')

    # x must be an integer that is greater than or equal to 0
    if not isinstance(x, int) or x < 0:
        raise ValueError('x must be an integer that is greater than or equal to 0')

    # x must be less than n
    if x > n:
        raise ValueError('x cannot be greater than n')

    # Check if P is a 1D numpy.ndarray
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    # Check if values in P are in the range [0, 1]
    if not all(0 <= val <= 1 for val in P):
        raise ValueError('All values in P must be in the range [0, 1]')

    # Initialize an empty array to store the likelihoods
    likelihoods = np.zeros(P.shape)

    for i, p in enumerate(P):
        if p < 0 or p > 1:
            raise ValueError('All values in P must be in the range [0, 1]')

        # Calculate the binomial coefficient using NumPy
        binomial_coefficient = np.math.factorial(n) / (np.math.factorial(x) * np.math.factorial(n - x))

        # Calculate the binomial probability using the binomial coefficient
        likelihoods[i] = binomial_coefficient * p**x * (1 - p)**(n - x)

    return likelihoods
