# Функция принимает 3 параметра
# Имя человек, фамилия человека, отчество человека
# Вывести ФИО 
# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep="")

# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()

# вызываем функцию
print_fio(name, surname, patronymic)

# Вывести количество букв в верхнем и нижнем регистре
# объявление функции
def print_case_counts(text):
    count_lower = 0
    count_upper = 0
    
    for alpha in text:
        if alpha.islower():
            count_lower += 1
        elif alpha.isupper():
            count_upper += 1
    print(f"Букв в верхнем регистре: {count_upper}")
    print(f"Букв в нижнем регистре: {count_lower}")
    
# считываем данные
text = input()

# вызываем функцию
print_case_counts(text)

# Посчитать сумму цифр в числе
# объявление функции
def print_digit_sum(num):
    print(sum([int(digit) for digit in str(num)]))
    
# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)

# Подается строка слов каждое через -
# Отсортировать слова по лексикографическому значению
# И между каждым словом поставить -
# объявление функции
def print_sorted_hyphen(s):
    s.sort() # Сортируем список 
    print(*s, sep="-")
    

# считываем данные
s = input().split("-")

# вызываем функцию
print_sorted_hyphen(s)

# Напечатать равнобедренный треугольник из символов
# объявление функции
def draw_triangle(fill, base):
    average = (base // 2) + 1
    
    for i in range(1, average + 1):
        print(fill * i)
        
    for i in range(average - 1, 0, - 1):
        print(fill * i)

# считываем данные
fill = input() # Символ которым заполним треугольник
base = int(input()) # Величина основания треугольника

# вызываем функцию
draw_triangle(fill, base)

# Вывести время созвона по Пермскому времени
# Часовой пояс в Перми + 2 часа
# объявление функции
def print_perm_time_call(msc_time):
    parts = msc_time.split(":") # Разделяем минуты и часы на части
    
    hours = int(parts[0]) + 2 # Время в Перми
    minutes = int(parts[1])
    
    if hours < 10: # Если меньше 10 добавлем ноль
        hours_str = "0" + str(hours) 
    else:
        hours_str = str(hours)
        
    if minutes < 10: # Если меньше 10 добавляем ноль
        minutes_str = "0" + str(minutes)
    else:
        minutes_str = str(minutes)
    
    print(f"Созвон будет в {hours_str}:{minutes_str}.")

# считываем данные
msc_time = input() # Время по Москве

# вызываем функцию
print_perm_time_call(msc_time)

# Посчитать для каждой буквы слова в нижнем регистре в лекс. порядке
# Количество в вхождений в формате L: N 
# где L - некоторая буква
# N - количество вхождений буквы в слово s
# объявление функции
def print_symbol_counts(s):
    unique_letters = [] # Создаем пустой список для уникальных букв 
    
    # Проходимся по каждой букве и добавляем ее в список, если ее нету в списке
    for letter in s:
        if letter not in unique_letters:
            unique_letters.append(letter)
            
    unique_letters.sort() # сортируем буквы в лекс. порядке
    
    for letter in unique_letters:
        print(f"{letter}: {s.count(letter)}")
    

# считываем данные
s = input().lower()

# вызываем функцию
print_symbol_counts(s)