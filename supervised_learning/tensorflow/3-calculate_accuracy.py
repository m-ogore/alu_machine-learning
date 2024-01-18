#!/usr/bin/env python3

import tensorflow as tf
'''
Write the function def calculate_accuracy(y, y_pred): 
that calculates the accuracy of a prediction:

y is a placeholder for the labels of the input data
y_pred is a tensor containing the network’s predictions
Returns: a tensor containing the decimal accuracy of the prediction
hint: accuracy = correct_predictions / all_predictions
'''
def calculate_accuracy(y, y_pred):
    # Compare predicted labels with true labels
    correct_predictions = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))

    # Calculate accuracy as the ratio of correct predictions to total predictions
    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
    #accuracy = tf.nn.softmax_cross_entropy_loss(labels = y, logits = y_pred)


    return accuracy