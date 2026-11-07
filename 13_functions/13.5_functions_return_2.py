# Подается 3 натуральных числа
# Нужно вернуть значение True если соблюдается неравенство треугольника
# объявление функции
def is_valid_triangle(side1, side2, side3):
    return (
            side1 + side2 > side3 
            and side1 + side3 > side2
            and side2 + side3 > side1
    )
                
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

# Если текст является Палиндромом то вернуть значение True
# объявление функции
def is_palindrome(text):
    clean = [c.lower() for c in text if c.isalpha()] # Убираем лишние символы в списке и оставляем только буквы
    return clean == clean[::-1] 
    
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# По условию слова должны быть одинаковой длины
# Если слова отличаются одной буквой
# Вывести True в противном случае False
# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            
    return count == 1        
# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

# Валидный пароль
# Пароль состоит не менее чем из восьми символов
# В пароле есть хотя бы одна строчная и одна заглавная буква
# В пароле есть хотя бы одна цифра
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for c in password:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True
            
    return has_upper and has_lower and has_digit

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

#
# объявление функции
def is_prime(num):
    
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            
    return count == 2        

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# Подается пароль в формате a:b:c
# a должно быть Палиндромом
# b должно быть простым
# c должно быть четным
# объявление функции
def is_prime(num):
    
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            
    return count == 2        

# объявление функции
def is_valid_password(password):
    parts = password.split(":")   
    
    if len(parts) != 3:
        return False
    
    a, b, c = parts 
    
    return a == a[::-1] and is_prime(int(b)) and int(c) % 2 == 0
               
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

#
# объявление функции
def is_correct_bracket(text):
    
    balance = 0
    for char in text:
        if char == "(":
            balance += 1
        else:
            balance -= 1
        
        # Если прямо сейчас закрывающих стало больше, чем открытых:    
        if balance < 0:
            return False
    
    # В конце все открытые скобки должны найти свою пару (баланс ровно 0):
    return balance == 0
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))