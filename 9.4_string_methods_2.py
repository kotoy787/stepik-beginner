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








