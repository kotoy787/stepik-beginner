# Вывести сумму квадратов элементов списка
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0
for num in numbers:
    total += num ** 2

print(total)

# Нужно вывести вначале отрицательные числа, затем нули и после положительные, каждое на отдельной строке
n = int(input())
plus_digit = []
null_digit = []
minus_digit = []

for i in range(n):
    num = int(input())
    if num < 0:
        minus_digit.append(num) 
    elif num == 0:
        null_digit.append(num)
    else:
        plus_digit.append(num)

result = minus_digit + null_digit + plus_digit
print(*result, sep="\n")

# Вывести уникальные слова каждое на отдельной строке
# Уникальные, те что не повторялись
n = int(input())
result = []

for i in range(n):
    word = input().lower()    
    if word not in result:
        result.append(word)

print(*result, sep="\n")

# Вывести значение функции для каждого x f(x) = x ** 2 + 2 * x + 1 каждое на отдельной строке
n = int(input())
result = []

for i in range(n):
    x = int(input())
    result.append(x)

for i in range(n):
    f_x = (result[i] ** 2) + (2 * result[i]) + 1
    result.append(f_x)

print(*result[:n], sep="\n")   
print()        
print(*result[n:], sep="\n")



# Убрать из списка минимальный элемент и максимальный и вывести в таком же порядке
n = int(input())
result = []

for i in range(n):
    num = int(input())
    result.append(num)

minimum = min(result)
maximum = max(result)

for x in result:
    if x != minimum and x != maximum:
        print(x)

#
n = int(input())
result = []

for i in range(n):
    text = input()  # Вначале подается текст запроса
    result.append(text)

search = input() # Сам поисковой запрос
for text in result:
    if search.lower() in text.lower():
        print(text) # Вывести строки где содержится поисковой запрос

# Вывести текст в котором встречаются одновременно все поисковые запросы 
# Каждый на отдельной строке
n = int(input())
result = []

for i in range(n): # Весь текст запросов сохранить в список
    text = input()
    result.append(text)

k = int(input()) # Кол-во запросов
searches = [] # Запросы

for i in range(k):
    searches.append(input().lower())

for text in result:
    flag = True # Изначально подразумевыаем что все запросы присутствуют
    
    for search in searches:
        if search not in text.lower(): # Если хотя бы одного запроса нету в строке
            flag = False
            break
            
    if flag: # Если все заросы есть
        print(text)