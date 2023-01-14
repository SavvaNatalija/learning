# my_string = 'Питон лучший язык в мире'

# # new_string = my_string.split() - может со строкой исполняться только 1 раз
# # new_string = my_string.replace('и', '$').replace(' ', '!')
# # new_string = my_string.strip() очищает от лишних пробелов в начале и конце строки

# if my_string.startswith('Пит'):
#     print('Да, все верно')
# if my_string.endswith('ре'):
#     print('Да, все верно')
# if my_string.lower().startswith('пит'):
#     print('Да, все верно')



# print(my_string)
# print(new_string)

# my_list = ['21', '23', '543', '43', 'gt', '645fsdf']
# add = '-'

# print(add.join(my_list)) # 21-23-543-43-gt-645fsdf

my_dict = {32:'32', 3: 45, 1: 'один', 'ключ': 2142345, 'список': [321, 324, 543, 321]}  #все эелементы парные, словарь, ключи уникальные

print(my_dict.get(2, 'нет такого ключа'))
print(my_dict.get(1, '0'))

print(my_dict.get(2, 0) + my_dict.get(3, 0))

my_dict['new'] = 'value' #если ключ существует, затрется значение на новое
print(my_dict)
my_dict[3] = my_dict.get(3)+1 #увеличить на 1 значение ключа 3

