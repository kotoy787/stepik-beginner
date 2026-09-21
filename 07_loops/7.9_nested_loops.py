# Вывести три n-числа через пробел и повторить чикл n-кол-во числа
num = int(input())

for i in range(num):
    for i in range(1):
        print(num, num, num)

# Вывести числа от 1 до n пять раз и n-ое кол-во раз
num = int(input())
for i in range(1, num + 1):
    print(i, i, i, i ,i) 

# Вывести таблицу сложение от 1 до n и n-ое кол-во раз
num = int(input())

for i in range(1, num + 1):  
    for j in range(1, 10):    
        print(i, "+", j, "=", i + j)
    print() 

# Печатает численный треугольник
num = int(input())

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()     

