# Вывести все слова до слова КОНЕЦ
word = input()
while word != "КОНЕЦ":
    print(word)
    word = input()

# Примечание: так как чтобы while остановил цикл нам нужно:
# 1. Чтобы все условия были false поэтому в цикле while
# 2. В данном случае мы используем оператор and а не or
word = input()
while word != "КОНЕЦ" and word != "конец":
    print(word)
    word = input()

# Посчитать кол-во слов до слова остановки
word = input()
counter = 0
while word != "стоп" and word != "хватит" and word != "достаточно":
    counter += 1
    word = input()
    
print(counter)

# Выводить до тех пор пока числа делятся на 7 без остатка
num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())

# Посчитать сумму n-ого количества положительных чисел
num = int(input())
total = 0
while num >= 0:
    total += num
    num = int(input())
    
print(total)

# Колво пятерок в последовательности 5 
num = int(input())
counter = 0

while 1 <= num <= 5:
    if num == 5:
        counter += 1
    num = int(input())

print(counter)
   
# Вывести почту без символа "_"
nickname = input()

while "_" in nickname:
    nickname = input()

print(nickname)

# Посчитать кол-во людей в очереди между Александрой и Левоном
name = input()
while name != "Александра":
    name = input()

counter = 0
name = input()    
    
while name != "Левон":
        counter += 1
        name = input()

print(counter)        

# Посчитать кол-во монет которые надо заплатить ведьмаку
n = int(input())
counter = 0

while n >= 25:
    counter += 1
    n = n - 25

while n >= 10:
    counter += 1
    n = n - 10

while n >= 5:
    counter += 1
    n = n - 5

while n >= 1:
    counter += 1
    n = n - 1

print(counter)  
