# Перевести километры в мили
# объявление функции
def convert_to_miles(km):
    miles = km * 0.6214
    return miles

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))

# Обернуть строку в теги <code></code>
# объявление функции
def code_format(text):
    return f"<code>{text}</code>"

# считываем данные
text = input()

# вызываем функцию
print(code_format(text))

# Подается номер месяца
# Нужно вывести количество дней в этом месяце
# Год не високосный
# объявление функции
# объявление функции
def get_days(month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days[month - 1]

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

# Округлить положительное число с плавающей точкой по правилам математики
# объявление функции
def math_round_to_int(num):
    if num - int(num) >= 0.5:
        num = int(num) + 1
    else:
        num = int(num)
                  
    return num 
                  
# считываем данные
num = float(input())

# вызываем функцию
print(math_round_to_int(num))

# Вывести список делителей числа в порядке возрастания
# объявление функции
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))

# Посчитать количество делителей числа
# объявление функции
def number_of_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) # len посчитает количество элементов в списке

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))

# Вывести новый список чисел без повторяющихся значений
# объявление функции
def get_unique(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result        

# считываем данные
numbers = eval(input())

# вызываем функцию
print(get_unique(numbers))

# Программа на вход принимает список data
# Нужно вернуть индекс последнего вхождения value в список data
# Если нету то вывести ERROR!
# объявление функции
def get_last_index(data, value):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            return i    
    return "ERROR!" # Если в списке не нашлось искомое значение value
    
# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))

# Подается строка и символ каждое на отдельной строке
# Посчитать количество вхождений символа в строку и вывести список с индексами вхождений
# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == char]   
# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

# Программе подается два отсортированных списка, состоящий из чисел
# И обьединяет их в один отсортированный список
# Я решил без sort() т.к он хорош только для небольших списков а использовал два указателя
# объявление функции
def merge(list1, list2):
    result = []
    i = 0  # Указатель для певрого списка
    j = 0  # Указатель для второго списка
    
    # Идем пока оба списка не закончатся
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]: 
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Добавляем остаток списка, который еще не закончился
    # Один из срезов гарантировано будет пустым         
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

# Программе подается число n затем n строк, содержащие числа в порядке возрастания
#
def quick_merge(list1, list2):    
    result = []
    p1 = 0 # Указатель первого списка
    p2 = 0 # Указатель второго списка
    
    # Цикл работает пока оба списка не закончатся
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    
    # Добавляем остаток списка, который еще не закончился
    # Один из срезов гарантировано будет пустым
    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]

    return result

n = int(input())
total = []

for _ in range(n):
    current = [int(c) for c in input().split()] # Символы строки сохраняем в список и преобразуем их в числа
    total = quick_merge(total, current) # Присваиваем total результат функции quick_merge то есть список result

print(*total) # Выводим все элементы списков











