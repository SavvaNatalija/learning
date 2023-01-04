# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import math

my_list = []
result_list = []

for _ in range(9):
    number = random.randint(0,10)
    my_list.append(number)
        
print(f'рандомный десятизначный список {my_list}')


for i in range(math.ceil(len(my_list)/2)):
    number=my_list[i]*my_list[len(my_list)-i-1]
    # print(number)
    result_list.append(number)

print('произведение пар списка (первый - последний, и тд):')
print(*result_list, sep=', ')