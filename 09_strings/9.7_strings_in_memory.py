# Найти следующую русскую букву алфавита после введенной
letter = input().upper()

if letter == "Я": # Если буква является последней в алфавите, то 
    print("Дальше букв нет")
else:
    next_char = ord(letter) + 1
    print(chr(next_char))
    

# Вывести символы в диапозоне a до b для каждого кодового значения Unicode
start = int(input())
end = int(input())

for i in range(start, end + 1):
    print(chr(i), end=" ")

# Вывести для каждый буквы в строке свой кодовый номер в Unicode
text = input()

for char in text:
    print(ord(char), end=" ")

# Найти из 4 строк самое тяжелое слово
# Под самым тяжелым подразумевается сумма кодовых слов букв по таблице Unicode
max_weight = 0
heaviest_word = ""

for i in range(4):
    text = input()
    total = 0
    for char in text:
        total += ord(char)  
    
    if total > max_weight:
        max_weight = total
        heaviest_word = text

print(heaviest_word)

#
text = input()
total = 0

for char in text:
    total += ord(char) * 3 # каждый символ в тексте стоит: код в таблице Unicode * 3
    
print(f"Текст сообщения: '{text}'")
print(f"Стоимость сообщения: {total}🐝") # Вывести стоимость сообщения Сэма

# Нужно посчитать сумму кодов символов в таблице Unicode * 3 в eng и rus расскладке
# Старая стоимость: <стоимость старого сообщения>🐝
# Новая стоимость: <стоимость нового сообщения>🐝
text = input()
eng_text = text # Переназначил переменную чтобы в дальнейшем ее использовать для eng расскладки

total_rus = 0
total_eng = 0

eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"

for char in eng_text: 
    total_eng += ord(char) * 3 # Стоимость старого сообщения в eng расскладке
for i in range(0, len(eng)):
    text = text.replace(eng[i], rus[i]) # Заменяем eng буквы на rus
for char in text:
    total_rus += ord(char) * 3 # Стоимость нового сообщения в rus расскладке

print(f"Старая стоимость: {total_eng}🐝")    
print(f"Новая стоимость: {total_rus}🐝")    

# Шифр Цезаря (сдвиг на n символов назад с закольцовкой алфавита)
n = int(input())
text = input()
result = ""

for char in text:
    new_code = ord(char) - n
    if new_code < ord('a'):
        new_code += 26
    result += chr(new_code)

print(result)

# Задача: "Сбой в системе" - расшифровка [u-код] в буквы
text = input()

while "[u-" in text:
    start = text.find("[u-")
    end = text.find("]", start)
    
    number = int(text[start+3 : end])
    letter = chr(number)

    text = text[:start] + letter + text[end+1:]

print(text)








