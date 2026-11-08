# Игра числовая угадайка
from random import randint


def is_valid(value, max_val):
    return value.isdigit() and 1 <= int(value) <= max_val

print('Добро пожаловать в числовую угадайку!')

while True:
    
    while True:
        limit = input(
            "Введите правую границу диапозона (число n от 2 и больше): "
        )
        if limit.isdigit() and int(limit) > 1:
            limit = int(limit)
            break
        print("Пожалуйста введите число больше 1.")
        
    num = randint(1, limit)
    attemps = 0
    
    while True:
        digit = input(f"Введите число от 1 до {limit}:")
    
        if not is_valid(digit, limit):
            print(f'А может быть все-таки введем целое число от 1 до {limit}?')
            continue 
    
        digit = int(digit) 
        attemps += 1       
        if digit > num:
            print('Слишком много, попробуйте еще раз')
        elif digit < num:
            print('Слишком мало, попробуйте еще раз')
        elif digit == num:
            print(f"Вы угадали за {attemps} попыток, поздравляем!")
            break
    
    again = input("Хотите сыграть еще раз? (д/н или yes/no): ").strip().lower()
    if again not in ("д", "да", "y", "yes"):
        print("Спасибо за игру! До встречи.")
        break
    print("-" * 30)

