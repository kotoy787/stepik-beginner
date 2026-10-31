# Вывести список до буквы z:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
digit = ['a']

for i in range(98, 123):
    letter = chr(i) # Допустим chr(98) это b
    temp = "" # Строка чтобы накапливать буквы, после смены буквы она сбрасывается
    for j in range(1, i - 96 + 1):
        temp += letter
        
    digit.append(temp) # Добавляем букву в список
    
print(digit)   

# Программа создает из указанных строк список
# А затем выводит его
n = int(input())
result = []

for i in range(n):
    lang = input()
    result.append(lang)
    
print(result)

# Программам создает из указанных чисел список их кубов и выводит его
n = int(input())
result = [] # создаем список

for i in range(n):
    digit = int(input())
    digit **= 3 # Находим куб числа
    result.append(digit) # сохраняем результат в список

print(result)    

# Вывести кол-во элементов в списке
# Последний элемент списка
# Вывести список в обратоном порядке
# Содержится ли 5 и 17 в списке. Если да то вывести YES, если нет то NO
# Вывести список кроме первого и последнего элемента
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])

if 5 in numbers and 17 in numbers:
    print("YES")
else:
    print("NO")
      
print(numbers[1:-1])      

# Программа создает список из делителей числа n
n = int(input())
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print(divisors)        

# Создать список состоящий из сумм соседних чисел
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

result = []

for i in range(n - 1):
    sum_digit = numbers[i] + numbers[i + 1]
    result.append(sum_digit)

print(result)    

# Удалить символы с нечентными идексами
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for i in range(n - 1, -1, -1):
    if i % 2 != 0:
        del numbers[i]

# Подается n кол-во строк и каждый символ в строке как отдельный элемент добавляется в список        
print(numbers)   
n = int(input())
result = []

for i in range(n):
    text = input()
    result.extend(text)

print(result)

# Подается натуральное число n  и затем n строк и в конце число k
# Нужно вывести k-ю букву из всех введенных строк
n = int(input())
words = []

for i in range(n):
    words.append(input()) 

k = int(input())
result = ""

for word in words:
    if len(word) >= k:
        result += word[k - 1]

print(result)        

     

