import numpy as np

def make_field(size):
    matrix = np.ones((size, size), dtype=np.int8)
    matrix[1::2, ::2] = 0
    matrix[::2, 1::2] = 0
    return matrix

size = int(input("Введите размер матрицы: "))
checkerboard_matrix = make_field(size)
print(checkerboard_matrix)