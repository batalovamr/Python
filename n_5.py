# Реализуйте алгоритм перемешивания списка.

import random
list = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {list}")
random.shuffle(list)
print(f"список после перемешивания:\n{list}")