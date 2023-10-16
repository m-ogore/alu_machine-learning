#!/usr/bin/env python3
import numpy as np

#A function  that calculates the mean and covariance of a data set:
def mean_cov(X): #X is a numpy.ndarray of shape (n, d) containing the data set:
    X=np.array(X)
    #n is the number of data points
    #d is the number of dimensions in each data point
    n = len(X)
    d = len(X[0])

    #(n,d)=X.shape

    #If X is not a 2D numpy.ndarray, raise a TypeError with the message X must be a 2D numpy.ndarray
    if X.ndim != 2:
         raise TypeError("X must be a 2D numpy.ndarray")
    #If n is less than 2, raise a ValueError with the message X must contain multiple data points
    if n<2:
         raise ValueError("X must contain multiple data points")
    #Calculate the mean for each dimension:
    mean = np.mean(X, axis=0, keepdims=True)
    #Calculate the covariance matrix:
    cov=(X-mean)/(n-1)
    #for x in enumerate(X):
     #    for mean in means:
      #       cov.append(sum(x-mean)/(n-1))
    return mean,cov
