import numpy as np

y = np.array([1, 2, 3, 4, 5])
a = np.array([3, 2, 1, 0, -1])

result = np.sum((y - a) ** 2)

print(f"Сумма квадратов разностей: {result}")