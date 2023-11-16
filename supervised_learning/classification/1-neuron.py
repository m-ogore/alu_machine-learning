'''Write a class Neuron that defines a single neuron performing binary classification (Based on 0-neuron.py):

class constructor: def __init__(self, nx):
nx is the number of input features to the neuron
If nx is not an integer, raise a TypeError with the exception: nx must be a integer
If nx is less than 1, raise a ValueError with the exception: nx must be positive
All exceptions should be raised in the order listed above
Private instance attributes:
__W: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
__b: The bias for the neuron. Upon instantiation, it should be initialized to 0.
__A: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.
Each private attribute should have a corresponding getter function (no setter function).
'''
class Neuron:
    def __init__(self, nx):
        """
        Initializes the object with the given nx value.

        Parameters:
            nx (int): The value to initialize nx with.

        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        
        self.nx = nx
        self.__W = np.random.normal(size=(nx,))
        self.__b = 0
        self.__A = 0

        #Each private attribute should have a corresponding getter function (no setter function).
        @property
        def W(self):
            return self.__W

        @property
        def b(self):
            return self.__b

        def A(self):
            return self.__A

        def forward_prop(self, X):
            z = np.matmul(X, self.__W) + self.__b
            self.__A = 1 / (1 + np.exp(-z))
            return self.__A
        

