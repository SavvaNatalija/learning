# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
def a(x1, y1, x2, y2):    
    return round(((x2-x1)**2+(y2-y1)**2)**0.5, 2)
print('введите координату x первой точки')
x1 = float(input())
print('введите координату y первой точки')
y1 = float(input())
print('введите координату x второй точки')
x2 = float(input())
print('введите координату y второй точки')
y2 = float(input())
print(f"расстояние между этими точками составляет {a(x1, y1, x2, y2)}")