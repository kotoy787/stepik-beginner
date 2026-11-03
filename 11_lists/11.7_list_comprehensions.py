# Удалить первыый символ каждой строки и вывести новый список
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [word[1:] for word in keywords]

print(new_keywords)

# Вывести длину каждой строки в новом списке
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(word) for word in keywords] 

print(lengths)

# Получить новый список где только элементы длиной не менее 5 символов (включительно)
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [word for word in keywords if len(word) > 4]

print(new_keywords)

# Получить список всех целых чисел палиндромов от 100 до 1000 (включительно)
palindromes = [digit for digit in range(100, 1001) if str(digit) == str(digit)[::-1]]

print(palindromes)

# Вывести каждое слово из текста на отдельной строке
print(*input().split(), sep="\n")

# Вывести квадрат чисел от до n (включительно) каждое на отдельной строке
squares = [i ** 2 for i in range(1, int(input()) + 1)]
print(*squares, sep="\n")

# Вывести кубы указанных чисел на одной строке
cubes = [int(digit) ** 3 for digit in input().split()]
print(*cubes)

# Вывести все цифровые символы строки
text = [c for c in input() if c.isdigit()]

print(*text, sep="")

# Вывести квадраты четных чисел кроме тех квадратов, которые оканчиваются на 4
squares = [int(i) ** 2 for i in input().split() if int(i) ** 2 % 2 == 0 and int(i) ** 2 % 10 != 4]
print(*squares)





