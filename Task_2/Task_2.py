import pandas
import numpy as np
import sys
import pickle

#1
print("#1")
arr_1 = [1, 7, 13, 105]
size_of_arr1 = sys.getsizeof(arr_1)
print(f"Размер массива arr_1 - {size_of_arr1} байт")

with open("binary_arr_1.dat", "wb") as file:
    pickle.dump(arr_1, file)
with open("binary_arr_1.dat", "rb") as file:
    len_of_arr_1 = len(arr_1)
    empty_arr = np.empty(len_of_arr_1)
    binary_arr_1 = pickle.load(file)
    for bin_arr_1 in binary_arr_1:
        #print(bin_arr_1)
        empty_arr = binary_arr_1
    print(f"\nСчитывание массива из бинарного файла: \n{empty_arr}")


with open("file1.txt") as file:
    some_data = file.read()
    print(f"\nСчитывание массива из .txt файла: \n{some_data}")

print("#1")
#1

#2
print("\n#2")
arr_zeros = np.zeros(10)
print(arr_zeros)

arr_ones = np.ones(10)
print(arr_ones)

arr_fives = np.full(10, 5)
print(arr_fives)
print("#2")
#2

#3
print("\n#3")
parity_arr = np.arange(30, 71, 2)
print(parity_arr)
print("#3")
#3

#4
print("\n#4")
arr_5_to_50 = np.linspace(5, 50, 10)
print(arr_5_to_50)
print("#4")
#4

#5
print("\n#5")
random_array_1_to_100 = np.random.randint(1, 101, size=(3, 3, 3))
print(random_array_1_to_100)
print("#5")
#5

#6
print("\n#6")
array_30_to_41 = np.arange(30, 42).reshape(3, 4)
print(array_30_to_41)
print("#6")
#6

#7
print("\n#7")
array_1_and_0 = np.zeros((10, 10), dtype=int)
array_1_and_0[0, :] = 1   
array_1_and_0[-1, :] = 1  
array_1_and_0[:, 0] = 1   
array_1_and_0[:, -1] = 1
print(array_1_and_0)
print("#7")
#7

#8
print("\n#8")
array_diagonal = np.zeros((5, 5), dtype=int)
np.fill_diagonal(array_diagonal, np.arange(1, 6))
print(array_diagonal)
print("8")
#8

#9
print("\n#9")
array_chess = np.zeros((4, 4), dtype=int)
array_chess[1::2, ::2] = 1
array_chess[::2, 1::2] = 1
print(array_chess)
print("9")
#9

#10
print("\n#10")
array_march_2017 = np.arange('2017-03-01', '2017-04-01', dtype='datetime64[D]')
print(array_march_2017)
print("10")
#10