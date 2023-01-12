# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    list = [rnd() for i in range(k+1)]
    return list

def create_str(array):
    list = array[::-1]
    s = ''
    if len(list) < 1:
        s = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                s += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    s += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                s += f'{list[i]}x'
                if list[i+1] != 0:
                    s += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                s += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                s += ' = 0'
    return s

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))