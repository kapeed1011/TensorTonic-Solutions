import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X=np.array(X,dtype=float)
    
    
    if X.ndim==1:
        mask=np.isnan(X)
        valid=~mask
        if np.any(valid):
            if strategy=='mean':
                to_fill=np.mean(X[valid])
            else:
                to_fill=np.median(X[valid])
        else:
            to_fill=0.0
        X[mask]=to_fill
    else:
        N,D=X.shape
        for i in range(D):
            col=X[:,i]
            mask=np.isnan(col)
            valid=~mask
            if np.any(valid):
                if strategy=='mean':
                    to_fill=np.mean(col[valid])
                else:
                    to_fill=np.median(col[valid])
            else:
                to_fill=0.0
            col[mask]=to_fill
            X[:,i]=col
    return X
        
        
