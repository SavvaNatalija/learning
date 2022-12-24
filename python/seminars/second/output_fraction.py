# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числ

# variant 1
a = float(input('Введите дробное число: '))
b = a*10 % 10
c = int(b//1)
if c == 0:
    print('нет')
else:
    print(c)

# проверка на "целостность" числа
number1 = 5.00001
number2 = 5.0

if number1 == int(number1):
    print('Целое')
else:
    print('Дробное')
if number2 == int(number2):
    print('Целое')
else:
    print('Дробное')

# variant 2
number = input('Введите дробное число: ')
number = number.split('.')
print(number)
if len(number) > 1:
    print(number[1][0])
else:
    print('Целое число')
