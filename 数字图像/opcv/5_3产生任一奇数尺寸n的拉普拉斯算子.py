# 5-3
import numpy as np
def genlaplacian(n):
    matrix = np.ones((n, n), dtype=np.int)
    matrix[n//2][n//2] = 1-n*n
    return matrix
