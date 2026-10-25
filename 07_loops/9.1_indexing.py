# Вывести символ запятой из списка
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[7])

# Вывести символ w из списка
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[-10])

# Вывести символы с четными индексами
s = input()

for i in range(0, len(s), 2):
    print(s[i])

# Вывести символы в слове наоборот
s = input()

for i in range(-1, -len(s) - 1, -1):
    print(s[i])
    
# Вывести ФИО
first_name = input()
last_name = input()
patronymic = input()

print(last_name[0] + first_name[0] + patronymic[0])

# Вывести эмодзи в порядке <номер животного в очереди>) <эмодзи животного>
emoji = input()

for i in range(len(emoji)):
     print(str(i + 1) + ")", emoji[i])

# Считает сумму цифр числа
n = input()
total = 0

for i in range(0, len(n)):
    total += int(n[i])

print(total)

# Проверить есть в ли в тексте цифра
text = input()
has_digit = False

for char in text:
    if char in "0123456789":
        has_digit = True
        break

if has_digit:
    print("Цифра")
else:
    print("Цифр нету")   

# Посчитать кол-во * и + d в строке
text = input()

counter_plus = 0
counter_asterisk = 0

for i in text:
    if i == "+":
        counter_plus += 1
    if i == "*":
        counter_asterisk += 1
        
print("Символ + встречается", counter_plus, "раз")
print("Символ * встречается", counter_asterisk, "раз")

# Посчтитать количетсво пар одинаковых чисел
text = input()
counter = 0

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        counter += 1
        
print(counter)

# Посчитать кол-во гласных и согласных букв
text = input().lower()

vowels = "ауоыиэяюе"
consonants = "бвгджзйклмнпрстфхцчшщ"

vowels_count = 0
consonants_count = 0

for char in text:
    if char in vowels:
        vowels_count += 1
    elif char in consonants:
        consonants_count += 1

print("Количество гласных букв равно", vowels_count)
print("Количество согласных букв равно", consonants_count)

# Перевести число из десятичной в двоичную систему
num = int(input())
total = ""

while num > 0:
    ostatok = num % 2
    total += str(ostatok)
    num //= 2    

result = total[::-1]
print(result)







