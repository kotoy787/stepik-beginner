# Найти координату середины отрезка
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# Вывести длину окружности и площадь круга
# объявление функции
def get_circle(radius):
    from math import pi
    length = 2 * pi * radius
    square = pi * radius ** 2
    
    return length, square
# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)

# Квадратное уравнение
# объявление функции
def solve(a, b, c):
    d = (b**2 - 4 * a * c) ** 0.5
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    return min(x1, x2), max(x1, x2) 

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)