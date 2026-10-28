#
n = int(input())

for i in range(1, n + 1):
    text = input()
    if text.isspace() or text == "": # Если в строке пустая строка и пробел то
        print(str(i) + ":", "COMMENT SHOULD BE DELETED")
    else:
        print(str(i) + ":", text)

# Проверить никнейм пользователя
nickname_user = input()

if nickname_user.startswith("@"): # Никнейм начинается на @
    name = nickname_user[1:]
    if 5 <= len(nickname_user) <= 15: # Длина никнейма от 5 до 15 (включительно)
        if name.isalnum() and name == name.lower(): # Никнейм состоит только из букв или цифр и только строчные буквы
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")
else:
    print("Incorrect")

# Является ли строча Российским номерным знаком
car_number = input()
is_valid = True

if len(car_number) == 10 or len(car_number) == 9:
    if car_number[6] != "_":
        is_valid = False
        
    for i in range(len(car_number)):
        if i == 6:
            continue
            
        if i in [0, 4, 5]:
            if car_number[i] not in "АВЕКМНОРСТУХABEKMHOPCTYX":
                is_valid = False
        else:
            if not car_number[i].isdigit():
                is_valid = False
else:
    is_valid = False

if is_valid:
    print("YES")
else:
    print("NO")


