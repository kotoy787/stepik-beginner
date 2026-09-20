# Сделал код-ревью программы которая выводила произведение всех цифр числа
n = int(input())
product = 1

while n != 0:
    digit = n % 10
    product *= digit
    n //= 10
    
print(product)

# Код-ревью программы которая находила старшую цифру числа
n = int(input())

while n > 9:
    n //= 10
    
print(n)

# Код-ревью где программа выводит всех четных чисел последовательности
total = 0

for i in range(1, 8):
    num = int(input())
    if num % 2 == 0:
        total += num 
    
if total == 0:
    print(0)    
else:
    print(total)

# Код-ревью программы, которая считает положительные числа
# и выводит их кол-во и произведение 
product = 0
count = 1

for i in range(1, 11):
    x = int(input())
    if x > 0:
        count *= x
        product += 1
    elif x == 0:
        product += 1
        count = 0
    
        
if product > 0:
    print(product)
    print(count)
else:
    print('NO')

# Код-ревью программы, которая выводит на экран цифру числа,
# кратная 3
n = int(input())
max_digit = 0
counter = 0

while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        counter += 1
        if max_digit < digit:
            max_digit = digit       
    n //= 10
  
if counter == 0:
    print("NO")
elif max_digit > 0:
    print(max_digit)
else:
    print(0) 

s = input()

# Программа пока длина строки меньше 10, следует правилу:
# если текущая длина строки кратна 4, прибавляет справа символ x
# иначе, если текущая длина строки кратна 5, прибавляет справа символ y
# в противном случае прибавляет слева символ z
while len(s) < 10:
    if len(s) % 4 == 0:
        s = s + 'x'
    elif len(s) % 5 == 0:
        s = s + 'y'
    else:
        s = 'z' + s

s = "@" + s
print(s) 

# Вывести n/m
# где n – количество сообщений длиннее 7 символов, m – общее количество сообщений.   
cnt = 0
total = 0

while True:
    num = int(input())
    total += 1    
    if len(str(num)) > 7:
        cnt += 1
    if num % 100 == 11:
        break    

print(cnt, '/', total, sep='')

# Вывести сумму всех отрицательных чисел из списка и максимальное отрицательное число 
maximum = 0
total = 0
found = False

for i in range(1, 11):
    x = int(input())
    if x < 0:
        total += x
        if maximum == 0 or x > maximum:
            maximum = x
        found = True

if found:
    print(total)
    print(maximum)
else:
    print("NO")