import numpy as np

def shift_rows(matrix : list):
    matrix = np.array(matrix)
    if matrix.shape != (4, 4):
        raise Exception("Invalid input. Input must be 4x4 matrix.")
    for i in range(4):
        matrix[i] = np.roll(matrix[i], -i)
    return matrix