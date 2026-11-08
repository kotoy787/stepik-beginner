# Шифр Цезаря
ru_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
en_alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Добро пожаловать в программу «Шифр Цезаря»!")

# 1. Запрос параметров
direction = (
    input("Выберите направление (шифрование / дешифрование): ").strip().lower()
)
language = input("Выберите язык (русский / английский): ").strip().lower()
shift = int(input("Введите шаг сдвига (целое число): "))
text = input("Введите текст: ")

# 2. Выбор алфавита
if language in ("русский", "ru", "rus"):
    alphabet = ru_alphabet
else:
    alphabet = en_alphabet

# Если дешифрование — просто делаем шаг в противоположную сторону
if direction in ("дешифрование", "дешифровать", "decode"):
    shift = -shift

result = []
n = len(alphabet)

# 3. Обработка строки
for char in text:
    if char.lower() in alphabet:
        # Находим индекс в алфавите
        idx = alphabet.index(char.lower())
        # Считаем новый индекс по модулю длины алфавита
        new_idx = (idx + shift) % n
        new_char = alphabet[new_idx]

        # Сохраняем регистр
        if char.isupper():
            result.append(new_char.upper())
        else:
            result.append(new_char)
    else:
        # Неалфавитные символы оставляем нетронутыми
        result.append(char)

print("Результат:")
print("".join(result))

# Шифр Цезаря на английском языке
# Сдвиг равен длине слова
text = input()
words = text.split(" ")
result_words = []

for word in words:
    # 1. Считаем длину слова ТОЛЬКО по буквам (без знаков препинания)
    shift = 0
    for char in word:
        if char.isalpha():
            shift += 1

    # 2. Шифруем символы слова
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            if char.isupper():
                # Сдвиг для заглавных 'A'..'Z'
                # ord('A') дает код первой буквы, чтобы сместиться в диапазон 0..25
                new_code = (ord(char) - ord("A") + shift) % 26 + ord("A")
                encrypted_word += chr(new_code)
            else:
                # Сдвиг для строчных 'a'..'z'
                new_code = (ord(char) - ord("a") + shift) % 26 + ord("a")
                encrypted_word += chr(new_code)
        else:
            # Знаки препинания и кавычки не меняем
            encrypted_word += char

    result_words.append(encrypted_word)

# 3. Выводим результат
print(" ".join(result_words))