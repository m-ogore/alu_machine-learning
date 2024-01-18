#!/usr/bin/env python3
import tensorflow as tf

# disabling eager mode 
tf.compat.v1.disable_eager_execution() 

'''
Write the function def create_placeholders(nx, classes): that returns two placeholders, x and y, 
for the neural network:

nx: the number of feature columns in our data
classes: the number of classes in our classifier
Returns: placeholders named x and y, respectively
x is the placeholder for the input data to the neural network
y is the placeholder for the one-hot labels for the input data

def create_placeholders(nx, classes):
    # nx: the number of feature columns in our data
    # classes: the number of classes in our classifier
    # x is the placeholder for the input data to the neural network
    # y is the placeholder for the one-hot labels for the input data

    x = tf.compat.v1.placeholder(tf.float32, shape=(None,nx), name='x')
    y = tf.compat.v1.placeholder(tf.float32, shape = (None,classes), name='y')

    return x,y
    '''
import tensorflow as tf

def create_placeholders(nx, classes):
    """
    Create placeholders for input data (x) and one-hot labels (y).

    Parameters:
        nx (int): Number of feature columns in the data.
        classes (int): Number of classes in the classifier.

    Returns:
        x (tf.Tensor): Placeholder for input data.
        y (tf.Tensor): Placeholder for one-hot labels.
    """
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')

    return x, y
