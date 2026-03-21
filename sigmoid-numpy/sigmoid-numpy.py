import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x=np.asarray(x)
    sigmoid_fun=1/(1+np.exp(-x))
    return sigmoid_fun