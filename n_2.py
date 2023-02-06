# 45. Найти сумму чисел списка стоящих на нечетной позиции

import random
lst = [random.randint(1, 10) for i in range(10)]
print(lst)
new_lst = [value for index, value in enumerate(lst) if index % 2 == 1]
print(new_lst)
print(sum(new_lst))