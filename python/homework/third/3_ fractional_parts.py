# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов,
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math

my_list = []

for _ in range(10):
    amount = random.randint(0,3)
    number = round(random.uniform(0, 10), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)
        
print(f'рандомный десятизначный список {my_list}')


result_list = []
for var in my_list:
    if var != int(var):
        result_list.append(round(var%1, 3)) 

print(f'список дробных частей {result_list}')

min = result_list[0]
max = result_list[0]

for var in result_list:
    if var > max:
        max = var
    if var < min:
        min = var

print(f'минимальная дробная часть = {min}, максимальная дробная часть = {max}')