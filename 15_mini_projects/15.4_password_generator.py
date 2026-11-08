import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password    
        
count = int(input("Количество паролей для генерации: "))
length = int(input("Длина одного пароля: "))

digits_on = input("Включать ли цифры 0123456789? (д/н): ").strip().lower()
upper_on = input("Включать ли прописные буквы? (д/н): ").strip().lower()
lower_on = input("Включать ли строчные буквы? (д/н): ").strip().lower()
symbols_on = input("Включать ли символы !#$%&*+-=?@^_? (д/н): ").strip().lower()
exceptions_on = (
    input("Исключать ли неоднозначные символы il1Lo0O? (д/н): ").strip().lower()
)

if digits_on in ("д", "да", "y", "yes"):
    chars += digits
if upper_on in ("д", "да", "y", "yes"):
    chars += uppercase_letters
if lower_on in ("д", "да", "y", "yes"):
    chars += lowercase_letters
if symbols_on in ("д", "да", "y", "yes"):
    chars += punctuation

# Если попросили исключить неоднозначные символы
if exceptions_on in ("д", "да", "y", "yes"):
    for c in "il1Lo0O":
        chars = chars.replace(c, "")    
        
for _ in range(count):
    print(generate_password(length, chars))        