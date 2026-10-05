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

# Сколько коров, быков, телят можно купить на 100 рублей
total = 0
for k in range(1, 100):
    for b in range(1, 100):
        for t in range(1, 100):
            if (k * 5 + b * 10 + t * 0.5 == 100) and (k + b + t == 100):
                total += 1
                print("k =", k, "b =", b,"t =", t)
print("Общее количество решений =", total)

# Найти 5 натуральный чисел удовлетворяющие условию:
# a ** 5 + b ** 5 + c ** 5 + d ** 5 = e ** 5
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                total = a**5 + b**5 + c**5 + d**5
                
                for e in range(d, 151):
                    # Если перевалили за сумму, дальше проверять нет смысла
                    if e**5 > total:
                        break
                    
                    if e**5 == total:
                        print(a + b + c + d + e)
                    