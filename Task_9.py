import numpy as np

array1 = np.random.rand(4, 1, 3)
array2 = np.random.rand(12, 1)

result = array1 * array2
print("Размер результирующего массива: ", result.shape)