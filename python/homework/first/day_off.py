print('введите цифру = день недели')
a = int(input())
if (a == 6 or a == 7):
    print('это выходной день')
else:
    print('это рабочий день')


def input_int():
    while True:
        try:
            number = int(input('Введите целое число: '))
            return number
        except:
            print('ошибка')

# print(input_int())
day = input_int()

if 0 < day < 8:
    if day < 6:
        print('будни')
    else:
        print('выходные')