

'''review
Update the class MultiNormal:

public instance method def pdf(self, x): that calculates the PDF at a data point:
x is a numpy.ndarray of shape (d, 1) containing the data point whose PDF should be calculated
d is the number of dimensions of the Multinomial instance
If x is not a numpy.ndarray, raise a TypeError with the message x must be a numpy.ndarray
If x is not of shape (d, 1), raise a ValueError with the message x must have the shape ({d}, 1)
Returns the value of the PDF
You are not allowed to use the function numpy.cov
'''

import numpy as np

class MultiNormal:
    def __init__(self, data):
        if type(data) is not np.ndarray or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] <= 1:
            raise ValueError("data must contain multiple values")
        self.mean = np.mean(data, axis=0)
        self.cov = np.cov(data.T, ddof=0)

    def pdf(self, x):
        if type(x) is not np.ndarray or len(x.shape) != 2 or x.shape[1] != 1:
            raise TypeError("x must be a 2D numpy.ndarray")

        d = x - self.mean
        return (1. / (2 * np.pi * np.sqrt(np.linalg.det(self.cov)))) * np.exp(-0.5 * np.matmul(np.matmul(d.T, np.linalg.inv(self.cov)), d))
