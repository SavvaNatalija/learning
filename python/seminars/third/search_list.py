# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

my_list = ['sfdasfads', 'hgh5', 'dfgdfhfg5', 'sdgd1']

print(my_list)

search = input('Введите искомое число: ')

for item in my_list:
    if search in item:
        print(f'число {search} входит в заданный список')
        break
else: # для break в for - если существует, то else не отрабатывается
    print(f'число {search} не входит в заданный список')

# False = 1, False, [], (), {}, None