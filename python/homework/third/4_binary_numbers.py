# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def translator(x):
    my_list = []
    number = int(x)
    while number > 0:
        a = number % 2
        my_list.append(a)
        number = number // 2
    for i in range(len(my_list)//2):
        b = my_list[i]
        my_list[i] = my_list[len(my_list)-1-i]
        my_list[len(my_list)-1-i] = b
    x = int(''.join(map(str, my_list)))
    return(x)


x = int(input('Введите десятичное число, необходимое для преобразования в двоичное: '))
y = translator(x)
print(f'двоичным числом к десятичному числу {x} является {y}')

