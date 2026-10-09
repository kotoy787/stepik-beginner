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

# Цифровой корень числа
n = int(input())

while n > 9:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total
print(n)    
    
# Численный треугольник 3 
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    
    for j in range(i - 1, 0, -1):
        print(j, end="")
        
    print()    
    
# Нахождение решений уравнения b + 3a + 2d = m для заданных n и m
n = int(input())
m = int(input())

found = False

for b in range(1, n):
    for a in range(1, n):
        for d in range(1, n):
            if b + 3 * a + 2 * d == m:
                print(str(b) + " + 3×" + str(a) + " + 2×" + str(d) + " = " + str(m))
                found = True
                
if not found:
    print("При заданных n и m решений не существует.")  

# 1 Способ Найти "Красивое время" когда h ** n = m
n = int(input())

for h in range(24):
    m = h ** n
    
    if 0 <= m <= 59:
        
        if h < 10:
            h_str = str(0) + h 
        else:
            h_str = h
        
        if m < 10:
            m_str = str(0) + m
        else:
            m_str = m
        
        
        print(h_str + ":" + m_str)

# 2 способ решения этой задачи
n = int(input())

for h in range(24):
    for m in range(60):
        if h ** n == m:

            if h < 10:
                hh = "0" + str(h)
            else:
                hh = str(h)
            if m < 10:
                mm = "0" + str(m)
            else:
                mm = str(m)
            print(hh + ":" + mm)                            