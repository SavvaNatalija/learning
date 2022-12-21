a = 123
b = 1.23
value = None
print(a)
print(b)
print(type(b))
print(type(a))
print(value)
print(type(value))
s = "hello ' world" # 'hello "world'  'hello \'world'
# \n переход на новую строку
print(a, b, s)
print('{a} - {b} - {s}')
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

# списки
list = []
list1 = [1, 2, 3]
list2 = ['1', '2', '3', 'hello'] #список строк
print(list)
print(list1)
print(list2)

#считывание
print('Введите а');
a = input()
# b = int(input())
# c = float(input())

#операции
a=123
b=234
c=a+b
print(c)
#a/b (для вещественных) a//b - целая часть 
# a%b - остаток от деления  a**b - возведение в степень

# 

a = 1 < 4 and 5 > 2
print(a)

a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)