#!./.intranet/bin/python

import numpy as np

class Poisson:

    def __init__(self, data=None, lambtha=1.):
        self.data = data

        self.lambtha = float(lambtha)

        if data is None:
            self.lambtha = float(lambtha)

            if self.lambtha <= 0:
                 raise ValueError('lambtha must be a positive value')
        else:
            if not isinstance(data,list):
                raise TypeError('data must be a list')
            if len(self.data) < 2:
                raise ValueError('data must contain multiple values')
            #Calculate the lambtha of data

            self.lambtha = np.sum(data)/len(data)

    def pmf(self, k): 
        self.k = int(k)       
        if self.k < 0:
             
            return 0
        else:
            
            #k is out of range
    
            return (np.exp(-self.lambtha)*self.lambtha**self.k)/np.math.factorial(self.k)
np.random.seed(0)
data = np.random.poisson(5., 100).tolist()
p1 = Poisson(data)
print('P(9):', p1.pmf(9))

p2 = Poisson(lambtha=5)
print('P(9):', p2.pmf(9))


