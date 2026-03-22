import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N=len(seqs)
    if not max_len:
       
        max_len=0
        for i in range(N):
            l=len(seqs[i])
            if l>=max_len:
                max_len=l
        for j in range(N):
            if len(seqs[j])<max_len:
                seqs[j]=seqs[j]+[pad_value]* (max_len-len(seqs[j]))
    else:
        for j in range(N):
            if len(seqs[j])>=max_len:
                seqs[j]=seqs[j][:max_len]
            else:
                seqs[j]=seqs[j]+[pad_value]* (max_len-len(seqs[j]))
    return seqs
    