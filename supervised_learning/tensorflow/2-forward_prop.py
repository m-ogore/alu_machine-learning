import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer

def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Create the forward propagation graph for the neural network.

    Parameters:
        x (tf.Tensor): Placeholder for the input data.
        layer_sizes (list): List containing the number of nodes in each layer of the network.
        activations (list): List containing the activation functions for each layer of the network.

    Returns:
        tf.Tensor: The prediction of the network in tensor form.
    """
    # Initialize the input tensor for forward propagation
    prev_layer = x

    # Iterate over each layer size and activation function
    for size, activation in zip(layer_sizes, activations):
        # Create the layer using the create_layer function
        prev_layer = create_layer(prev_layer, size, activation)

    return prev_layer
