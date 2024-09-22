import numpy as np

#1
print("#1")
array1 = np.random.randint(0, 20, size=10)
array2 = np.random.randint(0, 20, size=10)
print("Первый массив:", array1)
print("Второй массив:", array2)
common_elements = np.intersect1d(array1, array2)
print(f"Общие элементы:{common_elements}")
print("#1")
#1

#2
print("\n#2")
array = np.random.randint(0, 20, size=15)
print("Исходный массив:", array)
unique_elements = np.unique(array)
print("Уникальные элементы:", unique_elements)
print("#2")
#2

#3
print("\n#3")
array = np.random.randint(0, 20, size=15)
print("Исходный массив:", array)
unique_elements, counts = np.unique(array, return_counts=True)
print("Уникальные элементы:", unique_elements)
print("Частоты:", counts)
print("#3")
#3

#4
print("\n#4")
array = np.random.randint(0, 10, size=4)
for i in range(1, 4):
    repeated_array = np.tile(array, i)
    print(f"Количество повторов: {i} \n{repeated_array}\n")
print("И так далее")
print("#4")
#4

#5
print("\n#5")
array = np.random.choice([np.nan, 1, 2, 3], size=10)
print("Исходный массив:", array)
clean_array = array[~np.isnan(array)]
print("Массив без nan:", clean_array)
print("#5")
#5

#6
print("\n#6")
array = np.random.randint(0, 100, size=10)
print("Исходный массив:", array)
k = np.random.randint(1, len(array)+1)
print("Значение k:", k)
k_smallest = np.partition(array, k - 1)[:k]
k_smallest_sorted = np.sort(k_smallest)
print(f"{k} наименьших значений:", k_smallest_sorted)
print("#6")
#6

#7
print("\n#7")
array = np.random.uniform(0, 100, size=10)
print("Исходный массив:", array)
some_number = np.random.uniform(0, 100)
print("Некоторое число:", some_number)
differences = np.abs(array - some_number)
nearest_index = np.argmin(differences)
nearest_value = array[nearest_index]
print("Ближайший элемент:", nearest_value)
print("#7")
#7

#8
print("\n#8")
array1 = np.array(['a', 'b', 'c'])
array2 = np.array(['1', '2', '3'])
print("Первый массив:", array1)
print("Второй массив:", array2)
combined_array = np.char.add(array1, array2)
print("Результат объединения:", combined_array)
print("#8")
#8

#9
print("\n#9")
array = np.array(['Python', 'Perl', 'JavaScript', 'PHP', 'Java', 'C++'])
print("Исходный массив строк:", array)
frequency_of_P = np.char.count(array, 'P')
print("Частота буквы 'P':", frequency_of_P)
print("#9")
#9

#10
print("\n#10")
coefficients_a = [1, -4, 7]  # Для x^2 - 4x + 7
coefficients_b = [1, -11, 9, 11, -10]  # Для x^4 - 11x^3 + 9x^2 + 11x - 10
roots_a = np.roots(coefficients_a)
roots_b = np.roots(coefficients_b)
print("Корни первого полинома: ", roots_a)
print("Корни второго полинома: ", roots_b)
print("#10")
#10