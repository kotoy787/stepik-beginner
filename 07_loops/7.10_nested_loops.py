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