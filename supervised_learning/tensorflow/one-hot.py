'''
    create one hot labels for the target/Y/ intended output of the network
    
    Tensorflow

    the array of labels is [cat, dog, cat, dog, ...]

'''
import numpy as np
import tensorflow as tf

labels = ['cat', 'dog', 'cat', 'dog']

# Convert labels to numerical indices
label_dict = {'cat': 0, 'dog': 1}
numeric_labels = [label_dict[label] for label in labels]

def one_hot(labels):
    one_hot = tf.one_hot(labels, len(set(labels)))
    return one_hot

print(one_hot(numeric_labels))
