import numpy as np
from utils.s_box_table import s_box_table

def substitute_bytes(matrix : list):
    matrix = np.array(matrix)
    if matrix.shape != (4, 4):
        raise Exception("Invalid matrix. The shape of the matrix should be 4x4.")
    
    for i in range(4):
        for j in range(4):
            element = matrix[i][j]
            row = element[0]
            col = element[1]
            if not row.isnumeric():
                row = 10 + ord(row) - ord('a')
            else:
                row = int(row)
            if not col.isnumeric():
                col = 10 + ord(col) - ord('a')
            else:
                col = int(col)
            matrix[i][j] = s_box_table[row][col]

    return matrix
            