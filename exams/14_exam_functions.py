# объявление функции
def draw_triangle():
    for i in range(8):
        print(" " * (7 - i) + "*" * (2 * i + 1))
        
# основная программа
draw_triangle()  # вызов функции

# Доставка первого товара стоит 1000 рублей
# Следующих 120 рублей
# Посчитать сумму доставки
# объявление функции
def get_shipping_cost(quantity):
    return 1000 + 120 * (quantity - 1)
# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# Нужно вернуть словесное написание числа num
# объявление функции
def number_to_words(num):
    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
    }
    
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
    }
    
    if num < 20:
        return units[num]
    elif num % 10 == 0:
        return tens[num // 10]
    else:
        return f"{tens[num // 10]} {units[num % 10]}"

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))

# Подается num - номер месяца 
# lan - язык либо русский либо английский
# Нужно вывести название месяца в соотвествии с языком
# объявление функции
def get_month(language, number):
    en_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                 'october', 'november', 'december']
    ru_months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
                 'октябрь', 'ноябрь', 'декабрь']
    
    if language == "ru":
        return ru_months[number - 1]
    else:
        return en_months[number - 1]
               
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

# Магическая дата это когда день * месяц = двух последним цифрам в году
# Если дата им является вывести True, False в противном случае
# объявление функции
def is_magic(date):
    d, m, y = [int(x) for x in date.split(".")]
    return d * m == y % 100 

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

# Проверить что в тексте есть все буквы алфавита
# объявление функции
def is_pangram(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

# Нужно посчитать значение биномального коэфицента
# объявление функции
def compute_binom(n, k):
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))



