# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

number = int(input("Введите целое число: "))

# for i in range(-number, number + 1, 1):
#     print(i, end=', ')

my_list = []

for i in range(-number, number + 1):
    my_list.append(i)

print(my_list)
print(*my_list, sep=', ')

