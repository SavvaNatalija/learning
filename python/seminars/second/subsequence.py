# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:* 
# - Для N = 5: 1, -3, 9, -27, 81

array = []
a = 1

number = int(input('Введите целое число '))
for i in range(number):    
    array.append(a)
    a *= -3
print(array, sep=', ')

my_list = []

for i in range(number):
    a = (-3)**i
    my_list.append(a)
print(*my_list, sep=', ')