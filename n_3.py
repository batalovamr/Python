# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

array = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {array}")
new_array = []
[new_array.append(i) for i in array if i not in new_array]
print(f"Список из неповторяющихся элементов: {new_array}")

