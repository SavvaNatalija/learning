# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да 
# - 8,9 -> нет


a = int(input('введите первое число: '))
b = int(input('Введите второе число: '))

if a == b**2 or b == a**2:
    print('одно число является квадратом второго')
else:
    print('одно число не является квадратом второго')