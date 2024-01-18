#!/usr/bin/env python3
#import tensorflow as tf
import tensorflow.compat.v1 as tf

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
'''
def create_placeholders(nx, classes):
    x = tf.placeholder(tf.float32, [nx, None])
    y = tf.placeholder(tf.float32, [classes, None]) 
    return x,y