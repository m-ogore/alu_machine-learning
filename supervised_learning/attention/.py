'''Create a class RNNEncoder that inherits from tensorflow.keras.layers.Layer to encode for machine translation:

    Class constructor def __init__(self, vocab, embedding, units, batch):
        vocab is an integer representing the size of the input vocabulary
        embedding is an integer representing the dimensionality of the embedding vector
        units is an integer representing the number of hidden units in the RNN cell
        batch is an integer representing the batch size
        Sets the following public instance attributes:
            batch - the batch size
            units - the number of hidden units in the RNN cell
            embedding - a keras Embedding layer that converts words from the vocabulary into an embedding vector
            gru - a keras GRU layer with units units
                Should return both the full sequence of outputs as well as the last hidden state
                Recurrent weights should be initialized with glorot_uniform
    Public instance method def initialize_hidden_state(self):
        Initializes the hidden states for the RNN cell to a tensor of zeros
        Returns: a tensor of shape (batch, units)containing the initialized hidden states
    Public instance method def call(self, x, initial):
        x is a tensor of shape (batch, input_seq_len) containing the input to the encoder layer as word indices within the vocabulary
        initial is a tensor of shape (batch, units) containing the initial hidden state
        Returns: outputs, hidden
            outputs is a tensor of shape (batch, input_seq_len, units)containing the outputs of the encoder
            hidden is a tensor of shape (batch, units) containing the last hidden state of the encoder
'''
#!/usr/bin/python3

import tensorflow
import numpy as np

class RNNEncoder(tensorflow.keras.layers.Layer):
    def __init__(self, vocab, embedding, units, batch):

        super(RNNEncoder, self).__init__()
        self.vocab = int(vocab)
        self.embedding = int(embedding)
        self.units = int(units)
        self.batch = int(batch)
        self.embedding_layer = tensorflow.keras.layers.Embedding(self.vocab, self.embedding)

        self.gru = tensorflow.keras.layers.GRU(self.units, 
                                          return_sequences = True,
                                          return_state = True)

    def initialize_hidden_state(self):

        return tensorflow.zeros(shape=(self.batch, self.units))
    def call(self,x,initial):

        x = self.embedding_layer(x)

        outputs, hidden_state = self.gru(x, initial_state=initial)
        

        return outputs, hidden_state
        

encoder = RNNEncoder(1024, 128, 256, 32)
print(encoder.batch)
print(encoder.units)
print(type(encoder.embedding))
print(type(encoder.gru))

initial = encoder.initialize_hidden_state()
print(initial)
x = tf.convert_to_tensor(np.random.choice(1024, 320).reshape((32, 10)))
outputs, hidden = encoder(x, initial)
print(outputs)
print(hidden)

