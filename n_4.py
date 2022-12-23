# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся 
# в файле file.txt в одной строке одно число.

import random

def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2  *number)}\n")

def read_file():
    with open('file.txt', 'r') as data:
        index = list(map(int, data.readlines()))
    return index
    
n = int(input("Введите число N: "))
list_number = [i for i in range(- n, n + 1)]
print(list_number)
write_file(n)
list_index = read_file()
prod = 1
for i in range(len(list_index)):
    prod *= list_number[list_index[i]]
print(f"Результат равен = {prod}")