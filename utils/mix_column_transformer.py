import numpy as np

default_mixer = np.array([
                            ['02', '03', '01', '01'],
                            ['01', '02', '03', '01'],
                            ['01', '01', '02', '03'],
                            ['03', '01', '01', '02']
                        ])

def xtime(b):
    if b & 0x80:
        return ((b << 1) & 0xff) ^ 0x1b
    else:
        return (b << 1) & 0xff
    
def gf_multiplication(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a = xtime(a)
        b >>= 1
    return result

def mix_columns(matrix, mixer=default_mixer):

    matrix = np.array(matrix)
    
    if matrix.shape != (4,4):
        raise Exception("Invalid input. Input must be 4x4 matrix.")
    
    result = np.empty((4,4), dtype=object)

    for col in range(4):
        for row in range(4):
            mixed_value = 0

            for k in range(4):
                a = int(matrix[k][col], 16)
                b = int(mixer[row][k], 16)

                mixed_value ^= gf_multiplication(a, b)

            result[row][col] = "{:02x}".format(mixed_value)

    return result