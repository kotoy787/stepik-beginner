# Подается число n (n >= 2), вывести список четных чисел
squares = [i for i in range(2, int(input()) + 1, 2)]
print(squares)

#

# Подаются строкеа, содержащая натуральные числа
# Нужно между каждым числом знак + а затем сумму чисел
n = [int(i) for i in input().split()]
print(*n, sep="+", end="=")
print(sum(n))

# Взять из списка у каждого слова первый символ поставить его в конец и добавить слог ки
text = [word[1:] + word[0] + str("ки") for word in input().split()]
print(*text)
        
# Вывести длину самого длинного слова в списке
text = [len(word) for word in input().split()]
print(max(text))

# Номер должен быть в формате 7-abc-def-hijk
# Или abc-def-hijk где a, b, c, d, e, f, h, i, j, k цирфы от 0 до 9 (включительно)
phone = input().split("-")

# 1. Проверяем, что все части — цифры
all_digits = False not in [p.isdigit() for p in phone]

# 2. Проверяем длины частей
lengths = [len(p) for p in phone]

# 3. Проверяем формат (количество частей + шаблон)
if len(phone) == 3:
    # Если 3 части, первая должна быть 3 цифры
    format_ok = (lengths == [3, 3, 4])
elif len(phone) == 4:
    # Если 4 части, первая должна быть ровно "7"
    format_ok = (lengths == [1, 3, 3, 4] and phone[0] == "7")
else:
    format_ok = False

# 4. Выводим результат
print("YES" if all_digits and format_ok else "NO")





        












