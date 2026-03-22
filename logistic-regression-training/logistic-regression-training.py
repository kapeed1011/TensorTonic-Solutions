import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    
    N,D=X.shape
    b=0
    w=np.zeros(D)
    

    for i in range(steps):#looping over no of steps
        z=w@X.T+b #calculating y_pred ie logits
        p=_sigmoid(z)#converting those logits to prob
        #loss=y[i]*np.log(prob) + (1-y[i])*(np.log(1-prob)) #using logits and prob to find loss. i don't know where to use this loss
        delta_w=X.T @(p-y)/N# i saw the hint and found delta w 
        delta_b=np.mean(p-y)# i saw the hint and found delta b
        w=w-lr*delta_w #updating w
        b=b-lr*delta_b#updating b
    return (w,b)
        
