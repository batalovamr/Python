# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите целое число: '))
list = [1]
m = 1
for i in range(2, n + 1):
    m *= i
    list.append(m)
print(list)