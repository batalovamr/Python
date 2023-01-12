# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

# запись в файл
def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0, 101)

# создание коэффициентов многочлена
def create_mn(k):
    list = [rnd() for i in range(k+1)]
    return list

# создание многочлена в виде строки
def create_str(array):
    list = array[::-1]
    s = ''
    if len(list) < 1:
        s = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                s += f'{list[i]}x^{len(list) - i - 1}'
                if list[i + 1] != 0 or list[i + 2] != 0:
                    s += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                s += f'{list[i]}x'
                if list[i + 1] != 0 or list[i + 2] != 0:
                    s += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                s += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                s += ' = 0'
    return s

# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
    i = 1  # степень
    ii = l-1  # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


# создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file5_1.txt", create_str(koef1))
write_file("file5_2.txt", create_str(koef2))

# нахождение суммы многочлена
with open('file5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file5_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
list1 = calc_mn(st1)
list2 = calc_mn(st2)
ll = len(list1)
if len(list1) > len(list2):
    ll = len(list2)
lst_new = [list1[i] + list2[i] for i in range(ll)]
if len(list1) > len(list2):
    mm = len(list1)
    for i in range(ll, mm):
        lst_new.append(list1[i])
else:
    mm = len(list2)
    for i in range(ll, mm):
        lst_new.append(list2[i])
write_file("file5_res.txt", create_str(lst_new))
with open('file5_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")