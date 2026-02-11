import numpy as np

def convert_to_int(hex_string):
    return int(hex_string, 16)

def convert_to_hex(int_value):
    return "{:02x}".format(int_value)

def add_round_key(state_matrix:list, round_key_matrix:list):

    state_matrix = np.array(state_matrix)
    round_key_matrix = np.array(round_key_matrix)

    if state_matrix.shape != (4, 4) or round_key_matrix.shape != (4, 4):
        raise Exception("Invalid input. Input must be 4x4 matrix")
    
    string_hex_to_int_convetor = np.vectorize(convert_to_int)

    state_matrix = string_hex_to_int_convetor(state_matrix)
    round_key_matrix = string_hex_to_int_convetor(round_key_matrix)

    intermediate_result = np.bitwise_xor(state_matrix, round_key_matrix)

    int_to_hex_convertor = np.vectorize(convert_to_hex)
    final_result = int_to_hex_convertor(intermediate_result)

    return final_result