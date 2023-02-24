# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv('C:/python/california_housing_test.csv')
# 40
print(df[df['population'] < 500]['median_house_value'].mean())
# 42
print(df[df['population'] < df['population'].median()]['households'].max())




