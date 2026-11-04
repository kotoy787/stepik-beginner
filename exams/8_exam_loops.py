# Посчитать сумму четных цифр в числе    
n = int(input())
total = 0

while n > 0:
    last_digit = n % 10
    if last_digit % 2 == 0:
        total += last_digit
    n //= 10
    
print(total)

# Из 8 чисел последовательности найти кол-во чисел, делящихся на 4
# И максимально делящееся число на 4
n = 8
count = 0
maximum = - 10 ** 6 - 1

for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if maximum < x:
             maximum = x
                            
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')                                  

# Вывести кол-во нечетных чисел и максимальное нечетное число 
n = 4
count = 0
maximum = - 10 ** 8 - 1

for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if maximum < x:
            maximum = x
            
            
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

#   
num = int(input())

counter = 0
counts = 0
count = 1
total = 0
count_zero_five = 0
count_last = 0

last_num_digit = num % 10

Flag = False

while num != 0:
    last_digit = num % 10
    if last_digit > 7:
        count *= last_digit
        Flag = True
    if last_digit > 5:
        total += last_digit
    if last_digit % 2 == 0:
        counts += 1
    if last_digit == 3:
        counter += 1
    if last_digit == 0 or last_digit == 5:
        count_zero_five += 1
    if last_digit == last_num_digit:
        count_last += 1
    num //= 10

print(counter)
print(count_last)
print(counts)
print(total)
if Flag:
    print(count)
else:
    print(1)
print(count_zero_five)
    
# Вывести 3-ю цифру с начала в числе
num = int(input())

temp_num = num
total_digits = 0

while temp_num > 0:
    total_digits += 1
    temp_num //= 10
    
steps = total_digits - 3

for _ in range(steps):
    num //= 10

print(num % 10)   

# Или 
num = int(input())

while num >= 1000:
    num //= 10

print(num % 10)

# Вывести прямоугольник с 19 звездочками 
num = int(input())

print("*" * 19)

for _ in range(num - 2):
    print("*" + " " * 17 + "*")

print("*" * 19)