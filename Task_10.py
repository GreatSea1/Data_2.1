import numpy as np

n = int(input("Введите n: "))  
m = int(input("Введите m: "))

A = np.random.rand(n, m)
B = np.random.rand(m)
C = np.random.rand(m, n)
D = np.random.rand(m)

result = 5 * A @ B + C.T @ D

print(f"Матрица A:\n{A}")
print(f"\nМатрица B:\n{B}")
print(f"\nМатрица C:\n{C}")
print(f"\nМатрица D:\n{D}")
print(f"\nРезультат выражения:\n{result}")