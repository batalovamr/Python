# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def create_list(n):
    a = []
    for i in range(n):
        a.append(random.randrange(-10, 10))
    return a

n = int(input("Введите размер массива: "))
arr = create_list(n)

if len(arr) % 2 == 0:
    new_arr = []
    for i in range(len(arr) // 2):
        new_arr.append(arr[i] * arr[len(arr) - 1 - i])
    print(arr)
    print(new_arr)

else:
    new_arr = []
    for i in range(len(arr) // 2 + 1):
        new_arr.append(arr[i] * arr[len(arr) - 1 - i])  
    print(arr)
    print(new_arr)

