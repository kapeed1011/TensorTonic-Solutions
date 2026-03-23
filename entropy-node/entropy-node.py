import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y=np.array(y)
    total_samples=len(y)
    unique_samples=np.unique(y,return_counts=True)
    value=unique_samples[1]/total_samples
    final_ans= -(np.sum(value*np.log2(value)))
    
    
    return final_ans
    