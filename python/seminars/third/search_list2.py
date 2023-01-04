# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
search = "qwe"
k = 0
m = 0

print(f'список {my_list} и строка {search}')

for item in my_list:
    m += 1
    if search == item:
        k += 1
        if k == 2:
            print(f'второе входение строки {search} на позиции {m-1}')
            break
else: # для break в for - если существует, то else не отрабатывается
    print(f'строка {search} не встречается дважды в списке {my_list}')

def check(my_list: list, search: str): # прописываем функцию
    count = 0
    for i in range(len(my_list)):
        if search == my_list[i]:
            count += 1
            if count == 2:
                print(f'второе входение строки {search} на позиции {i}')
                break
    else:
        print('второго вхождения нет')

my_list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
my_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
my_list4 = ["123", "234", 123, "567"]
my_list5 = []

check(my_list1, 'qwe')
check(my_list2, "йцу")
check(my_list3, "йцу")
check(my_list4, "123")
check(my_list5, "123")

print(my_list4.count('qwe')) # количество вхождений
print(my_list1.index('qwe', 2))