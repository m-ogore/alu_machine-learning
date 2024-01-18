#!/usr/bin/env python3
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
