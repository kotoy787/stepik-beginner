# Посчитать количество артиклей a, an, the в тексте
text = input().lower()
words = text.split()

articles = words.count("an") + words.count("a") + words.count("the")

print(f"Общее количество артиклей: {articles}")

#
numbers = [8, 9, 10, 11]
numbers[1] = 17 # Удалить первый элемент списка
numbers.extend([4, 5, 6]) # добавить в конец списка список 
del numbers[0] # Удалить первый элемент
numbers *= 2 # Умножить список на 2
numbers.insert(3, 25) # Добавить элемент 25 по индексу 3

print(numbers)

# Нужно удалить коментарии и символы пустого пространства в сообщениях
n = input() # Подается строка например #12
num = int(n[1:]) # Нужно взять само число

for i in range(num):
    line = input()
       
    index_hash = line.find("#") # Если в тексте есть # 
    
    if index_hash != -1: # Если есть
        clean_line = line[:index_hash] # Все что до символа #
    else: # Если нету
        clean_line = line
        
    print(clean_line.rstrip()) # Нужно убрать лишние пробелы в конце

# Поменять значение min и max местами
text = input().split()
numbers = []

for num in text:
    numbers.append(int(num))
    
max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)

# Отсортировать числа по возрастанию и по убыванию
nums = input().split()
numbers = []

for num  in nums:
    num = int(num)
    numbers.append(num)
    
numbers.sort()
print(*numbers)
numbers.sort(reverse = True)
print(*numbers, end="")

# Отсортировать название песен по алфавиту
n = int(input())
result = []

for i in range(n):
    result.append(input())
    
result.sort()
print(*result, sep="\n")






