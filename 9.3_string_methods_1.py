# 
text = input()
if text == text.title(): # Если имя и фамилия начинаются с заглавной буквы то
    print("YES")
else:                    # Иначе
    print("NO")

# Заменяем строчные символы на заглавные
text = input()

print(text.swapcase())

# Посчитать кол-во символов в нижнем регистре 
s = input()
count = 0 

for char in s:
    if char == char.lower() and char != char.upper():
        count += 1

print(count)        



   



