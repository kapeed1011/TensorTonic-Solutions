import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X=np.array(X)
    y=np.array(y)
    n=len(X)
    index=np.arange(n)
    if rng is not None:
       
        rng.shuffle(index)
    else:
        np.random.shuffle(index)
    for i in range(0,n,batch_size):
        end=i+batch_size
        if end>n and drop_last==True:
            break
        batch_idx=index[i:end]
        yield X[batch_idx], y[batch_idx]