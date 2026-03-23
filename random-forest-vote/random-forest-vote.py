import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions=np.array(predictions)
    t,n=predictions.shape
    result=np.zeros(n)
    for i in range(n):
        col=predictions[:,i]
        val,freq=np.unique(col,return_counts=True)
        result[i]=val[np.argmax(freq)]
    return list(result)
        
        
        