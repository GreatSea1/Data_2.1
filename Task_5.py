import numpy as np

def super_sort(rows, cols):
    A = np.random.randint(1, 101, size=(rows, cols))
    B = A.copy()
    B[:, ::2] = np.sort(B[:, ::2], axis=0)
    B[:, 1::2] = np.sort(B[:, 1::2], axis=0)[::-1]

    return A, B

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
A, B = super_sort(rows, cols)

print(f"Изначальная матрица:\n{A}")
print(f"\nОтсортированная матрица:\n{B}")