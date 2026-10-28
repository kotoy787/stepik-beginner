# Посчитать кол-во слов в строке
s = input()
c = s.count(" ")

print(c + 1)

#
s = input().lower()

print("Аденин:", s.count("а")) # Аденин = А, в
print("Гуанин:", s.count("г")) # Гуанин = Г, г
print("Цитозин:", s.count("ц")) # Цитозин = Ц, ц
print("Тимин:", s.count("т")) # Тимин = Т, т

# Считает сколько раз в n-ом кол-ве строк 3 рааз встречается число 11
n = int(input())
count = 0

for i in range(n):
    text = input()
    if text.count("11") >= 3:
        count += 1

print(count)        

# Проверить заканчивается ли строка на .com или .ru
text = input()

if text.endswith(".com") or text.endswith(".ru"):
    print("YES")
else:
    print("NO")

# Посчитать кол-во цифр в строке
text = input()
counter = 0

for digit in "0123456789":
    counter += text.count(digit)

print(counter)    

# 
text = input().lower()

if text.count("f") == 1: # Если буква f входит в строку один раз то 
    print(text.find("f")) # Вывести индекс f
elif text.count("f") > 1: # Если больше одной
    print(text.find("f"), text.rfind("f")) # Вывести первую и последнюю f
else: # Если вообще нету
    print("NO")

# Программа удаляет первое и последнее вхождение в строку h
text = input()

first_h = text.find("h")
last_h = text.rfind("h")

left_part = text[0:first_h]
right_part = text[last_h + 1:]

result = left_part + right_part
print(result)



