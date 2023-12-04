#!/usr/bin/env python3

'''
Write a function def from_numpy(array): that creates a pd.DataFrame from a np.ndarray:

array is the np.ndarray from which you should create the pd.DataFrame
The columns of the pd.DataFrame should be labeled in alphabetical order and capitalized. There will not be more than 26 columns.
Returns: the newly created pd.DataFrame
'''
def from_numpy(array):
    return pd.DataFrame(array)