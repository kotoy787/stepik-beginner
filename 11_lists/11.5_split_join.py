# Вывести каждое слово строки на отдельной строке
text = input()
words = text.split()

for word in words:
    print(word)

# Вывести инициалы Ф.И.О.
text = input()
words = text.split()
symbol = ""

for word in words:
    symbol += word[0]
    
s = ".".join(symbol)
print(s, end=".")

# Путь файловой системы Windows
path = input()
files = path.split("\\") # Двойное \\ так как символ \ используется для спец.последовательностей

print(*files, sep="\n") # Каждый файл или папку на отдельной строке

# Правильный ip адрес
ip_adress = input().split(".") # сразу введя ip адрес разделителем . добавляем элементы в список
flag = True

for digit in ip_adress:
    if int(digit) < 0 or int(digit) > 255 : # числа в ip адресе в диапозоне от 0 до 255 включительно
        flag = False

if flag:
    print("ДА")
else:
    print("НЕТ")
                  
# 
text = input()
separator = input()

print(separator.join(text)) # Вставляет указанный разделитель между всеми символами

# Посчитать кол-во пар элементов в списке 
digits = input().split()
counter = 0 

for i in range(len(digits)): #
    for j in range(i + 1, len(digits)): # Проверяем числа с индексами больше предущего 
        if digits[i] == digits[j]: # если значение предыдущего элемента совпадает с нынешним
            counter += 1

print(counter)








