import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x=np.array(x)
    n=len(x)
    output=[]
    for per in q:
        value=np.percentile(x,per,method='linear')
        output.append(value)
    return np.array(output)