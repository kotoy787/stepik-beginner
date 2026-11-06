# Задание 1
word = input()
for i in range(10):
    print(i, word)

# Задание 2
n = int(input())
for i in range(n + 1):
    if i == 0:
         print("Квадрат числа", i, "равен", i ** 2)
    if i > 0 and n > 0:
         print("Квадрат числа", i, "равен", i ** 2)

# Задание 3
n = int(input())

for i in range(n):              
    for j in range(n - i):      
        print('*', end='')
    print() 

# Задание 4
m = int(input())          
p = int(input())          
n = int(input())          

multiplier = 1 + p / 100  
population = m            

for day in range(1, n + 1):       
    print(day, population)        
    population = population * multiplier 

# С 2-мя параметрами:
for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)      

# Последовать от 100 до 999
for i in range(100, 1000):
    if i % 10 == 7:
        print(i)

# Задача отобразить диапозон от m до n
m = int(input())
n = int(input())
for i in range(m, n+1):
    print(m, i+1)

# Таблица умножения от *1 до * 10  
num = int(input())
for i in range(1, 11):
    print(num, "x", i, "=", num * i) 
     
# Числа в диапозоне от m до n, где (m > n) и только нечетные
m = int(input())
n = int(input())
for i in range(m , n -1, -1):
    if i % 2 != 0:
        print(i)            

# 2 в 1

m = int(input())
n = int(input())
if m <= n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)    
