# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование 
# библиотеки Random для получения случайного int

import random
my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)
res_list = []

for i in range(len(my_list)):
    k = random.randint(i,len(my_list)-1)
    b = my_list[k]
    my_list[k] = my_list[i] 
    my_list[i] = b

print(*my_list,sep=', ')