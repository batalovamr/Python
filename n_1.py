# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_list(n):
    a = []
    for i in range(n):
        a.append(random.randrange(-10, 10))
    return a

n = int(input("Введите размер массива: "))
array = create_list(n)
sum = 0
for i in range (1, len(array) - 1, 2):
    sum += array[i]
print(array)
print(sum)