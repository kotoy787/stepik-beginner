# Найти наименьший делитель числа
num = int(input())
n = 2
flag = False

while num != 0:
    if num % n == 0:
        flag = True
        break
    n += 1

if flag and n != 1:
    print(n)
else:
    print(num)

# Напечатать числа кроме  
num = int(input())
i = 0

while i != num:
    i += 1  
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
    