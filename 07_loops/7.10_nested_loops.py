# Перебирает все числа от 1 до n
# и печатает к числу столько плюсов сколько у него делителей
n = int(input())

for i in range(1, n + 1):
    print(i, end="")
    for j in range(1, i + 1):
        if i % j == 0:
            print("+", end="")

    print()   
    
# Вывести сумму факторалов от 1 до n 
n = int(input())
total = 0
count = 1

for i in range(1, n + 1):
    count *= i
    total += count
print(total)

# Печатает треугольник Флойда
n = int(input())
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()    

# Проверяет числа из диапозона a и b и выводит только простые числа
a = int(input())
b = int(input())

for x in range(a, b + 1):
    total = 0  

    for i in range(1, x + 1):
        if x % i == 0:
            total += 1

    if total == 2:
        print(x)
        
# Считает число у которого больше всего сумма всех делителей и сумму делителей самого числа
a = int(input())
b = int(input())
maximum = 0
best_x = 0

for x in range(a, b + 1):
    current_sum = 0
    for i in range(1, x + 1):
        if x % i == 0:
            current_sum += i

    if current_sum >= maximum:
        maximum = current_sum
        best_x = x
        
print(best_x, maximum, end=" ")        

