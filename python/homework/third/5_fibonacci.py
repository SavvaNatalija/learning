# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)  


k = int(input('введите количество k для чисел Фибоначчи: '))

F = []
for x in range(-k,k+1):
    if x < 0:
        F.append(-1*(fibonacci(-1*x)))
    else:
        F.append(fibonacci(x))

print(F)