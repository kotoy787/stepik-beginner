# Длина строки s
s = 'Python rocks!'
print(len(s))

# Вывести 4-ый символ строки s
s = 'Python rocks!'
print(s[3])

# Вывести символы s от 2 до 5 (включительно)
s = 'Python rocks!'
print(s[1:5])

# Убрать ведущие символы #
s = '###Python rocks!####'
print(s.strip("#"))

# Вывести строку s в верхнем регистре
s = 'Python rocks!'
print(s.upper())

# Заменить символ o в строке s на @
s = 'Python rocks!'
print(s.replace("o", "@"))

# Вывести символ из текста не кратные трем
text = input()
result = ""

for i in range(len(text)):
    if i % 3 != 0:
        result += text[i]
    
print(result)

# Заменить 1 на one
text = input()
result = text.replace("1", "one")
print(result)

# Убрать из текста символ @
text = input()
result = text.replace("@", "")
print(result)

# Вывести второе вхождение буквы f в строку
# Если f встречается один раз то ввывести -1 
# Если вообще f не встречается вывести -2
text = input()

if text.find("f") == -1:
    print(-2)
elif text.count("f") == 1:
    print(-1)
else:
    new_text = text.replace("f", "#", 1)
    
    print(new_text.find("f"))
    
# Взять часть от первого вхождения h до последнего h и перевернуть текст наоборот
text = input()

first = text.find("h")
last = text.rfind("h")

print(text[:first + 1] + text[first+1:last][::-1] + text[last:])






