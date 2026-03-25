import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    last_dim=scores.shape[-1]
    mask_matrix=scores.copy()
    i=np.arange(last_dim)[: , None]
    j=np.arange(last_dim)[None:,]
    mask=j>i
    mask_matrix[...,mask]=mask_value
    return mask_matrix
    
    
    
    