# if max < b:
#     max = b
# if max < c:
#     max = c
# if max < d:
#     max = d
# if max < e:
#     max = e
# print(f"максимальное число {max}")

# list = [a, b, c, d, e]
# for i in list:
#     if i > max:
#         max = i
# print(f"максимальное число {max}")

# my_max = -1000000
# my_list = []
# for item in range(5):
#     number = int(input(f'введите {item} число: '))
#     my_list.append(number)
#     if number > my_max:
#         me_max = number
# print(f"максимальное число {me_max}")        

# my_list = [4, 8, 2, 0, 9, 5]

# for i in range(len(my_list)):    # есть возможность изменения списка
#     print(my_list[i])
#     my_list[i] = 6
# print(my_list)

# print()

# my_list = [4, 8, 2, 0, 9, 5]
# for i in my_list: # нет возможности изменения списка
#     i = 6
# print(my_list)

my_list = []

for i in range(5):
    number = int(input(f'Введите {i+1} число '))
    my_list.append(number)

print(my_list)
