import numpy as np
import timeit

def mult(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def el_mult(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] * B[i][j]
    return C

def np_mult(A, B):
    return np.dot(A, B)

def np_el_mult(A, B):
    return A * B

def benchmark(func, *args, iterations=1):
    time = timeit.timeit(lambda: func(*args), number=iterations)
    return time

n = 1000
#Я попробовал взять n = 100000, и у меня IDE съела 20гб оперативной памяти, а потом ещё и ошибка памяти вылетела
#На значении n = 10000 уже всего лишь 4гб съедается, но обработка идёт всё ещё очень долго

A = np.random.randint(1, 10, size=(n, n)).tolist()
B = np.random.randint(1, 10, size=(n, n)).tolist()
A_np = np.array(A)
B_np = np.array(B)

mult_time = benchmark(mult, A, B)
el_mult_time = benchmark(el_mult, A, B)
np_mult_time = benchmark(np_mult, A_np, B_np)
np_el_mult_time = benchmark(np_el_mult, A_np, B_np)

print(f"mult (без numpy): {mult_time:.6f} сек")
print(f"el_mult (без numpy): {el_mult_time:.6f} сек")
print(f"np_mult (с numpy): {np_mult_time:.6f} сек")
print(f"np_el_mult (с numpy): {np_el_mult_time:.6f} сек")

print(f"Numpy матричное перемножение быстрее в: {mult_time / np_mult_time:.2f} раз")
print(f"Numpy поэлементное перемножение быстрее в: {el_mult_time / np_el_mult_time:.2f} раз")