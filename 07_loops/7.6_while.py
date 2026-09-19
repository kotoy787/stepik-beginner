# Вывести все числа наоборот, каждое на отдельной строке 
num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num //= 10

# Вывести все числа наоборот в одной строке
num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit, end="")
    num //= 10

# Найти минимальное и максимальное число
num = int(input())
maximum = num % 10
minimum = 9

while num != 0:
    last_digit = num % 10
    if maximum < last_digit:
        maximum = last_digit
    
    if minimum > last_digit:
        minimum = last_digit
        
    num //= 10
    
print("Максимальная цифра равна", maximum)
print("Минимальная цифра равна", minimum)

# Вычислить для числа:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
num = int(input())
length = len(str(num))

total = 0
product = 1
x = num

while x != 0:
    last = x % 10
    total += last
    product *= last
    x //= 10

first = num 
while first >= 10:
    first //= 10
    
average = total / length
last = num % 10

print(total) 
print(length)
print(product)    
print(average)
print(first)
print(first + last)

# Найти вторую цифру числа 
n = int(input())

while n > 99:
    n = n // 10

print(n % 10)  

# Проверяем есть ли лишняя цифра в числе
num = int(input())
last = num % 10
flag = True   

num //= 10    

while num != 0:
    second = num % 10
    if last != second:   
        flag = False     
    
    num //= 10

if flag == True:
    print("YES")
else:
    print("NO")

# Проверить является ли последовательность чисел упорядоченной по неубыванию
num = int(input())

prev = num % 10
num //= 10
flag = True

while num != 0:
    curr = num % 10
    
    if curr < prev:
        flag = False
    
    prev = curr
    num //= 10

if flag == True:
    print("YES")
else:
    print("NO")
    
# Посчитать количество четных чисел и вывести их в порядке слева направо 
num = int(input())
n = len(str(num))
delitel = 10 ** (n - 1)

counter = 0
found = False

while delitel > 0:
    digit = num // delitel % 10
    if digit % 2 == 0:
        counter += 1
        print(counter, "-я четная цифра равна ", digit, sep='')
        found = True
    delitel //= 10

if not found:
    print("Четных цифр в числе нет")