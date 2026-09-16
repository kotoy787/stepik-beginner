# Посчитать кол-во чисел в диапозоне от a, b если a <= b
# И куб которых оканчивается на 4 или 9
a = int(input())
b = int(input())
counter = 0
for i in range(a, b + 1):
    if (i ** 3 % 10 == 4) or (i ** 3 % 10 == 9):
        counter += 1
        
print(counter)

# Вывести n-ое кол-во чисел а затем их сложить
n = int(input())
total = 0
for i in range(n):
    x = int(input())
    total += x

print(total)

#
import math

n = int(input())
total = 0

for i in range(1, n + 1):
    total += 1 / i

result = total - math.log(n)
print(result)

# Посчитать кол-во чисел в диапозоне от a, b
# И квадрат которых оканчивается на 2 или на 5 или на 8
n = int(input())
total = 0
for i in range(1, n + 1):
    if (i ** 2 % 10 == 2) or (i ** 2 % 10 == 5) or (i ** 2 % 10 == 8):
        total += i

print(total)        

# Вычислить произведение отличных от нуля чисел 
count = 1                 
for i in range(10):       
    x = int(input())       
    if x != 0:
        count *= x

print(count)

# Вычислить сумму всех делителей
n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
               
print(total)

# Если в 10 чисел четные вывести YES, в противном случае NO
counter = 0
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        counter += 1
        
if counter == 10:
    print("YES")
else:
    print("NO")

# Посчитать сумму знакочередующейся суммы
n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total -= i
    if i % 2 != 0:
        total += i
            
print(total)      

# Вывести 2 максимальных числа из списка
n = int(input())

max1 = 0
max2 = 0

for i in range(n):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x

print(max1, max2)

# Последовательность Фенобачи 
n = int(input())

a = 1
b = 1

for i in range(n):
    if i == n - 1:
        print(a)
    else:
        print(a, end=' ')
    a, b = b, a + b
    

