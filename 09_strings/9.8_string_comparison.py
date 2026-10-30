# Выбрать самое минимальное и самое максимальное слово по таблице Unicode 
# Перемножить последние символы и возвести полученное числов квадрат
w1 = input()
w2 = input()
w3 = input()
w4 = input()

smallest = min(w1, w2, w3, w4)
largest = max(w1, w2, w3, w4)

char_min = smallest[-1]
char_max = largest[-1]

code_min = ord(char_min)
code_max = ord(char_max)

result = (code_min * code_max) ** 2
print(result)

# Найти минимальную и максимальную строки по длине в таблице Unicode
minimum = ""
maximum = ""

while True:
    text = input()
    if text == "КОНЕЦ": # Цикл продолжается до слова КОНЕЦ
        break
 
    if minimum == "": # Прогоняя первое значение у нас text < minimum == True и тогда значения min и max не менялись бы
        minimum = text
        maximum = text
    else:
        if text < minimum:
            minimum = text
        if text > maximum:
            maximum = text

print(f"Минимальная строка ⬇️: {minimum}")
print(f"Максимальная строка ⬆️: {maximum}")

# Найти минимальное, среднее и максимальное по длине строки из 3 
w1 = input()
w2 = input()
w3 = input()

smallest = min(w1, w2, w3)
largest = max(w1, w2, w3)
# Находим среднее (медиану) из трех значений.
# Самое большое число выигрывает в двух парах max(), самое маленькое — ни в одной.
# Остается среднее, которое и выбирает внешний min().
average = min(max(w1,w2), max(w1,w3), max(w2,w3)) #

print(f"{smallest} {average} {largest}")

# Номер класса должен быть в диапозоне от 0 до 9 (включительно)
# И буква должна быть от А до П (включительно)
n = int(input())

allowed_letters = "АБВГДЕЖЗИЙКЛМНОП"

for i in range(n):
    s = input().upper()
    if len(s) == 2 and s[0].isdigit() and s[1] in allowed_letters: # Если 
        print("YES")
    else:
        print("NO")
        
# Сортировка авторов книг и произведений по алфавиту
n = int(input())
is_sorted = True
prev_author = ""
prev_title = ""

for i in range(n):
    book = input()
    
    space_index = book.find(" ") # Найти первый пробел 
    author = book[:space_index] # Автор это все что до первого пробела
    
    start_quote = book.find("«") # Где начинается название произведения
    end_quote = book.find("»") # Где заканчивается произведение
    title = book[start_quote + 1 : end_quote] # Название произведения
    
    if i > 0: # Если поставили бы == то условие было бы всегда True и значение prev_title и prev_author не менялись
        if author < prev_author:
            is_sorted = False
        if author == prev_author and title < prev_title:
            is_sorted = False
        
    prev_author = author
    prev_title = title

if is_sorted: # Эквивалентно is_sorted == True
    print("YES")
else:
    print("NO")          




