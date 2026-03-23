import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    
    """
    x=np.array(x)
    if rng:
        rand = rng.random(x.shape)
    else:
        rand=np.random.random(x.shape)
    mask= rand>p
    scale=1/(1-p)
    dropout_pattern=mask.astype(float)*scale
    x=x*dropout_pattern
    return (x,dropout_pattern)