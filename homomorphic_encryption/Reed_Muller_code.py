import itertools
import numpy as np

def eval_z(m : int, z : int, f : list) -> int:
    if f == [0 for _ in range(m)]:
        return 1
    else:
        for index in range(m):
            if f[index] == 1 and int(bin(z)[2:].zfill(m)[index]) == 0:
                return 0
        return 1


def eval(m : int, f : list) -> list:
    eval_vec = []
    for z in reversed(range(pow(2, m))):
        eval_vec.append(eval_z(m, z, f))

    return eval_vec


def make_RM_code_generator_matrix(m : int, r : int) -> list:
    generator_matrix = []
    for deg in range(r + 1):
        for f_deg_list in list(itertools.combinations([i for i in range(m)], deg)):
            f = [0 for _ in range(m)]
            for f_deg_index in f_deg_list:
                f[f_deg_index] = 1
            generator_matrix.append(eval(m, f))
    
    return generator_matrix


def make_RM_code(m : int, r : int) -> list:
    RM_code = []
    generator_matrix = make_RM_code_generator_matrix(m, r)
    RM_code_dim = len(generator_matrix)
    for index in range(pow(2, RM_code_dim)):
        codeword = list(np.dot(np.array([int(b) for b in list(bin(index)[2:].zfill(RM_code_dim))]), np.array(generator_matrix)))
        for index in range(len(codeword)):
            codeword[index] %= 2
        RM_code.append(codeword)
    
    return RM_code