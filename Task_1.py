import pandas
import numpy as np

# Задание 1

arr_1 = np.empty((3, 4))
arr_1.fill(3)
print(arr_1)

arr_2 = np.random.randint(1, 10, (2, 4))
print(f'\n\n{arr_2}')

print (f'\n\nКоличество элементов в массивах arr_1 и arr_2: {arr_1.size + arr_2.size}')

concatinated_arrs = np.concatenate((arr_1, arr_2), axis=0)
print(f'\n\nconcatinated_arrs: \n{concatinated_arrs}')

arr_3 = np.array([1, 8, 6, 5, 8, 3])
arr_4 = ((arr_3 * 3) + 1)
print (f'\n\n{arr_3}\n{arr_4}')

arr_5 = arr_3.reshape(2, 3)
print (f'\n\n {arr_5}')

min_from_arr_5 = np.min(arr_5, axis = 1)
print(f'\n\n{min_from_arr_5}')

mean_of_arr_5 = np.mean(arr_5)
print(f'\n\n{mean_of_arr_5}')

arr_6 = (np.arange(0, 11, 1)) **2
print(f'\n\n{arr_6}')

print(f'\n\n{arr_6[1:-1:2]}')

print(f'\n\n{arr_6[::-1]}')

arr_6[1:-1:2] = 2
print(f'\n\n{arr_6}')

print(f'\n\n{(arr_6 == 49)}') #Каждый элемент, который равен 49, отмечается как True, остальные - как False
#Либо
print(f'{np.count_nonzero(arr_6 == 49)}') #Считается количество элементов, равных 49

A = np.random.randint(-11, 11, (5, 5))
B = A[A < 0]
print(f'\n\n{A}\n\n{B}')

#Задание 2
