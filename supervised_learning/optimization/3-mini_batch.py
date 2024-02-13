

import numpy as np
import tensorflow as tf

shuffle_data = __import__('2-shuffle_data').shuffle_data
#from tensorflow import metaflow, tf, restore_session
def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32, epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):

    m = X_train.shape[0]
    x = tf.placeholder(tf.float32, shape=(m, 784))
    y = tf.placeholder(tf.float32, shape=(m, 10))
    accuracy = tf._metrics.Accuracy()
    loss = tf.losses.softmax_cross_entropy(y, Y_valid)
    train_op = tf.train.AdamOptimizer().minimize(loss) 

    for epoch in range(epochs):
        sess = tf.Session()
        shuffle_data
        for i in range(0, m, batch_size):
            x_batch = X_train[i:i+batch_size]
            y_batch = Y_train[i:i+batch_size]
            sess.run(train_op, feed_dict={x: x_batch, y: y_batch})
            train_cost = sess.run(loss, feed_dict={x: x_batch, y: y_batch})
            train_accuracy = sess.run(accuracy)
            valid_cost = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
            valid_accuracy = sess.run(accuracy)
            print(f'{epoch} epochs:\n'
                f'\tTraining Cost: {train_cost}\n'
                f'\tTraining Accuracy: {train_accuracy}\n'
                f'\tValidation Cost: {valid_cost}\n'
                f'\tValidation Accuracy: {valid_accuracy}')


    
    save_path = tf.train.Saver().save(sess, save_path)

    return save_path
