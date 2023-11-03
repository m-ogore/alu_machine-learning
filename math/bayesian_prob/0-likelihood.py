
#!/usr/bin/env python3

import numpy as np
import math
def likelihood(x, n, P):
    #n must be a positive integer
    if n < 1:
        raise ValueError('n must be a positive integer') 
    #x must be an integer that is greater than or equal to 0
    if not isinstance(x,int) > 0:
        raise ValueError('x must be an integer that is greater than or equal to 0')
    
    #xmust be less than n
    if x > n: 
        raise ValueError('x cannot be greater than n')
    
    #if P is not a 1D numpy.ndarray, raise a TypeError with the message P must be a 1D numpy.ndarray
    if P.ndim != 1:
        raise TypeError('P must be a 1D numpy.ndarray')
    
    # Initialize an empty array to store the likelihoods
    likelihoods = np.zeros(P.shape)
    
    for i, p in enumerate(P):
        if p < 0 or p > 1:
            raise ValueError('All values in P must be in the range [0, 1]')
        #Returns: a 1D numpy.ndarray containing the likelihood of obtaining the data, x and n, for each probability in P, respectively
        #for i, p in enumerate(P):
        # Calculate the binomial probability using the formula
        likelihoods[i] = np.math.comb(n, x) * p**x * (1-p)**(n-x)
        #likelihoods[i] = (math.factorial(n)/(math.factorial(n)*math.factorial(n-x))) * p**x * (1-p)**(n-x)
    
    
    return likelihoods