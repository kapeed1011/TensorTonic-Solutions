import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A=np.array(A)
    n,m=A.shape
    new_arr=np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            new_arr[j][i]=A[i][j]
    return new_arr
