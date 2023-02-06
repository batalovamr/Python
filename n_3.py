# 46. Найти произведение пар чисел списка(парой считаем первый и последний, 
# второй предпоследний и тд)

import random
lst = [random.randint(1, 10) for i in range(7)]
print(lst)
new_lst = [lst[i] * lst[-i - 1] for i in range(len(lst) // 2 + len(lst) % 2)]
print(new_lst)