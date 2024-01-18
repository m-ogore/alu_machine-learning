#!/usr/bin/env python3
import tensorflow as tf
import numpy as np
'''

Write the function def create_layer(prev, n, activation):

prev is the tensor output of the previous layer
n is the number of nodes in the layer to create
activation is the activation function that the layer should use
use tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG") 
to implement He et. al initialization for the layer weights
each layer should be given the name layer
Returns: the tensor output of the layer
'''

def create_layer(prev, n, activation):
    
    weights = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, activation=activation, kernel_initializer=weights, name='layer')

    # Apply the layer to the previous tensor
    output = layer(prev)


    
    