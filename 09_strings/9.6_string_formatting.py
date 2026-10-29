s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(2010, "10k", "Bitcoin")

print(s)

#
s = f'In {2010}, someone paid {"10K"} {"Bitcoin"} for two pizzas.'

print(s)

#
today_date = input()
euro_rate = input()
yuan_rate = input()
print(f"На {today_date}: 1€ = {euro_rate}₽, 1¥ = {yuan_rate}₽") # Вывести дату, курс евро, курс юаня

# Или 
date, euro, china_money = [input() for i in range(3)]
print(f"На {date}: 1€ = {euro}₽, 1¥ = {china_money}₽")

# 
a = int(input())
b = int(input())

sum_cubes = a**3 + b**3
cube_sum = (a + b)**3

print(f"Для чисел {a} и {b}:")
print(f"  Сумма кубов: {a}**3 + {b}**3 = {sum_cubes}") # вывести сумму кубов a и b 
print(f"  Куб суммы: ({a} + {b})**3 = {cube_sum}") # вывести куб суммы a и b

# Читаем входные данные
day = int(input())
current_weight = float(input())

# Вычисляем, на сколько кг нужно худеть в день
# (100 - 88) / 60 = 0.2 кг
daily_loss = (100 - 88) / 60

# Вычисляем целевую массу на текущий день
target_weight = 100 - (daily_loss * day)

# Проверяем, идет ли все по плану (вес меньше или равен цели)
# Используем round или просто сравнение с небольшим допуском из-за особенностей float
if current_weight <= target_weight + 1e-9:
    print("Все идет по плану")
else:
    print("Что-то пошло не так")

# Выводим информацию в нужном формате
# Для текущего веса используем вывод как есть, чтобы сохранить формат (например, 99.9)
# Для цели форматируем до 1 знака после запятой, как в примере
print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight:.1f} кг")  
    
    



