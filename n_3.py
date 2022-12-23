# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите 
# на экран их сумму.
# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
import math

n = int(input('Введите целое число: '))
list = []
m = 0
for i in range(1, n + 1):
    m = (1 + 1 / i) ** i
    list.append(round(m, 2))
print(list)
print(sum(list))
