# Вывести список [1, 2, 3, ..., n]
n = int(input())
digit = list(range(1, n + 1, 1))
print(digit)

# Выводит список, состоящий из n букв нижнего регистра английского алфавита
n = int(input())
alpha = [] # Создаем пустой список

for i in range(97, 97 + n): # Перебираем символы по кодовым номерам букв по таблице Unicode
    alpha += [chr(i)] # Добавляем буквы в список

print(alpha)    

# Вывести список нечетных чисел от 1 до n
n = int(input())
digit_env = list(range(1, n + 1, 2)) # Список от 1 до n + 1 с шагом в 2

print(digit_env)

# Вывести четные символы списка
text = input()

print(list(text[0:len(text) + 1:2]))





