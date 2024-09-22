import numpy as np

array = np.linspace(-2 * np.pi, 2 * np.pi, 100)
print(f"Изначальная матрица:\n{array}")

sin_squared = np.sin(array) ** 2
cos_squared = np.cos(array) ** 2
sum_of_squares = sin_squared + cos_squared

print(f"\nСумма квадратов синуса и косинуса для каждого элемента:\n{sum_of_squares}")