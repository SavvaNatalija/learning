# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
# степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

from random import randint

k = int(input('Введите максимальную степень: '))

def RandomPolynomy(my_dict):
    for i in range (k, -1, -1):
        my_dict[i] = randint(-100,101)
    return my_dict

def PrintPolynomy(my_dict, file_name):
    dict_str = ''
    for k, v in my_dict.items():
        if v == -1:
            dict_str = dict_str[:-2]
            if k == 1:
                dict_str += f'- x + '
            elif k == 0:
                dict_str += f'- 1 + '
            else:
                dict_str += f'- x**{k} + '
        elif v < 0: 
            dict_str = dict_str[:-2]
            if k == 1:
                dict_str += f'- {-1*v}*x + '
            elif k == 0:
                dict_str += f'- {-1*v} + '
            else:
                dict_str += f'- {-1*v}*x**{k} + '
        if v == 1:
            if k == 1:
                dict_str += f' x + '
            elif k == 0:
                dict_str += f'+ 1 + '
            else:
                dict_str += f'x**{k} + '
        elif v > 0: 
            if k == 1:
                dict_str += f'{v}*x + '
            elif k == 0:
                dict_str += f'{v} + '
            else:
                dict_str += f'{v}*x**{k} + '
        else:
            dict_str = dict_str    
    else:
        dict_str = dict_str[:-3] + ' = 0'        
    print(dict_str)
    fname = f'python/homework/fourth/{file_name}.txt'
    # print(fname)
    my_file = open(fname, "w") 
    my_file.write(dict_str)
    my_file.close()


education = {}
print(f'первый рандомный словарь {RandomPolynomy(education)}')
print('первый многочлен из рандомного словаря: ')
PrintPolynomy(education, 'education')
print()

education2 = {}
print(f'второй рандомный словарь {RandomPolynomy(education2)}')
print('второй многочлен: ')
PrintPolynomy(education2, 'education2')
print()

sum_education = {}
for k, v in education.items():
    sum_education[k] = education[k]+education2[k]
print(f'словарь суммы двух словарей {sum_education}')
print('суммарный многочлен: ')
PrintPolynomy(sum_education, 'sum_education')
print()

my_file = open('python/homework/fourth/first_polynomy.txt')
first_str_polynomy = ''
first_str_polynomy = my_file.read()
print(f'читаем из первого файла first_polynomy.txt многочлен {first_str_polynomy}')
first = first_str_polynomy.replace(' - ',' -').replace('- ',' -').replace(' -x', ' -1x').replace(' + ', ' ').lstrip().rstrip().replace(' = 0', '').replace('*', '').replace('x', ':').replace(' :',' 1:').replace(': ',':1 ').replace(' ',',').split(',')

my_file = open('python/homework/fourth/second_polynomy.txt')
second_str_polynomy = ''
second_str_polynomy = my_file.read()
print(f'читаем из второго файла second_polynomy.txt многочлен {second_str_polynomy}')
second = second_str_polynomy.replace(' - ',' -').replace('- ',' -').replace(' -x', ' -1x').replace(' + ', ' ').lstrip().rstrip().replace(' = 0', '').replace('*', '').replace('x', ':').replace(' :',' 1:').replace(': ',':1 ').replace(' ',',').split(',')

for i in range(len(first)):
    if first[i].find(':') == -1:
        first[i] += ':0'

first_dict = {} 

for item in first:
    a, b = item.split(':')
    first_dict[int(b)] = int(a)
print(f'первый словарь из файла: {first_dict}')

for i in range(len(second)):
    if second[i].find(':') == -1:
        second[i] += ':0'


second_dict = {}
for item in second:
    a, b = item.split(':')
    second_dict[int(b)] = int(a)
print(f'второй словарь из файла: {second_dict}')

sum_dict = {}

if (list(second_dict.keys())[0] > list(first_dict.keys())[0]):
    for i in range(list(second_dict.keys())[0], -1, -1):
        sum_dict[i] = first_dict.get(i, 0) + second_dict.get(i, 0)
        
else:
    for i in range(list(first_dict.keys())[0], -1, -1):
        sum_dict[i] = first_dict.get(i, 0) + second_dict.get(i, 0)        
print(f'сумма: {sum_dict}')
print('и записываем в файл summa.txt получившийся многочлен')
PrintPolynomy(sum_dict, 'summa')



