# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 
# 1, 1, 2, 3, 5, 8, 13, 21]

def Fib(n):
    if n >= 0:
       i = range(n+1)
       list = [0,1]
       for k in i[2:]:
           list.append(list[k-1] + list[k-2]) 
       return list[n]
    else:
       n = -(n-1)
       i = range(n+1)
       list = [1,0]
       for k in i[2:]:
           list.append(list[k-2] - list[k-1]) 
       list.reverse()
    return list[0]

n = int(input("Введите целое число: "))
list = [Fib(i) for i in range(-n, n + 1)]
print(list)