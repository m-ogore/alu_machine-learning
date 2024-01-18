#!/usr/bin/env python3

import tensorflow as tf
'''
Write the function def calculate_loss(y, y_pred): that calculates the softmax cross-entropy loss of a prediction:

y is a placeholder for the labels of the input data
y_pred is a tensor containing the network’s predictions
Returns: a tensor containing the loss of the prediction
'''

def calculate_loss(y, y_pred):
    loss = tf.losses.softmax_cross_entropy(
        y, y_pred
    )
    return loss
