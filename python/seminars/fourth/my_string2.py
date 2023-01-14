# my_dict = {}

# num_list = '324235463213546835413654686463541'

# for dig in num_list:
#     my_dict[dig] = my_dict.get(dig, 0) + 1

# print(my_dict)

my_str = 'a*x**2 + b*x + c = 0'

def conv(my_str):
    my_str=my_str.replace('*', '').replace('2 + ', '').replace(' + ', '').replace(' = 0', '').replace(' ', '')
    new_str=my_str.split('x')
    print(new_str) 
    return new_str

def create_koef(equation: str) -> tuple:
    new_koef = []
    nq = equation.replace(' ', '').replace('=0', '').\
        replace('+', ' ').replace('-', ' -').split()
    for item in nq:
        if item.startswith('x'):
            new_koef.append(1)
        if item.startswith('-x'):
            new_koef.append(-1)
        new_koef.append(int(item.split('*x')[0]))
    print(new_koef)


conv(my_str)
str_1 = '-3*x**2 + 78 * x -9 = 0'
str_new = conv(str_1)
for i in str_new:    
    i = int(i)
    print(type(i))
print(str_new)    

str_new2 = create_koef(str_1)