import numpy as np
def generate_hex_matrix(plaintext):
    hex_encoded_bits = plaintext.encode().hex()
    hex_matrix = np.array([])

    number_of_blocks = (len(hex_encoded_bits) + 31) // 32

    iterator_upper_limit = number_of_blocks * 32 # number of characters

    for i in range(0, iterator_upper_limit, 2):
        if i < len(hex_encoded_bits):
            hex_matrix = np.append(hex_matrix, hex_encoded_bits[i:i+2])
        else:
            hex_matrix = np.append(hex_matrix, "00")

    hex_matrix = hex_matrix.reshape(number_of_blocks, 4, 4)

    for index, block in enumerate(hex_matrix):
        hex_matrix[index] = block.T
    
    return hex_matrix