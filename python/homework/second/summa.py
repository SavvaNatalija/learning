# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

my_string = input('введите вещественное число ')
print(type(my_string))
a = 0
res_str = my_string.replace('.','')

for i in range(len(res_str)):
    a += int(res_str[i])

print(a)



