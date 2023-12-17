# циклы

# первая задача
'''
a = int(input())
c = 0
d = 0
for x in range (0, a):
    b = int(input())
    if b == 10:
        c += 1
    if b < 5:
        d += 1
if c > 0:
    c = "YES"
else:
    c = "NO"
print(d, c, sep = "\n")'''

# вторая задача
'''
a = 1
b = 0
while a != 0:
    a = int(input())
    if a % 10 == 0 and a != 0:
        b += 1
print(b)'''

# ветвление

# наименьшее из двух чисел
'''
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)'''

# только
'''
a = int(input())
b = int(input())
c = int(input())
d = 0
if a >= 0:
    d += a
if b >= 0:
    d += b
if c >= 0:
    d += c
print(d)'''

# принадлежность 1
'''
a = int(input())
if a > -1 and a < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")'''

# принадлежность 3
'''
a = int(input())
if (a > -30 and a <= -2) or (a > 7 and a <= 25):
    print("Принадлежит")
else:
    print("Не принадлежит")'''

# ход ладьи
'''
a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
s = 0
if a != a1:
    s += 1
if b != b1:
    s += 1
if s >= 2:
    print("NO")
else:
    print("YES")'''

# количество дней
'''
a = int(input())
if a >= 10:
    if a % 2 == 0:
        print(31)
    else:
        print(30)
elif a >= 3 and a <= 9:
    if a % 2 == 1:
        print(31)
    else:
        print(30)
elif a == 1:
    print(31)
else:
    print(28)'''

# цикл for

# последовательность символов
'''
for i in range(0, 6):
    print("AAA")
for i in range(0, 5):
    print("BBBB")
print("E")
for i in range(0, 9):
    print("TTTTT")
print("G")'''

# звёздный прямоугольник
'''
a = int(input())
for i in range(0, a):
    print("*"*19)'''

# квадрат числа
'''
a = int(input())
for i in range(0, a+1):
    print("Квадрат числа", i, "равен", i**2)'''

# последовательность чисел 3
'''
a = int(input())
b = int(input())
for i in range(a, b - 1, -1):
    if i % 2 == 1:
        print(i)'''

# таблица умножения
'''
a = int(input())
for i in range(1, 11):
    print(a, "x", i, "=", a*i)'''


# циклы while

# количество членов
'''
a = "what"
b = -1
while a != "стоп" and a != "хватит" and a != "достаточно":
    b += 1
    a = input()
print(b)'''

# пока делимся
'''
a = 0
b = []
while a % 7 == 0:
    a = int(input())
    if a % 7 == 0:
        b.append(a)

for x in b:
    print(x)'''

# ведьмаку заплатите чеканной монетой
'''
a = int(input())
b = 0
while a >= 25:
        b += 1
        a -= 25
while a >= 10:
        b += 1
        a -= 10
while a >= 5:
        b += 1
        a -= 5
while a >= 1:
        b += 1
        a -= 1
print(b)'''

# max и min
'''
a = int(input())
max1 = 0
min1 = 10
while a > 0:
    b = a % 10
    a = a//10
    if b > max1:
        max1 = b
    if b < min1:
        min1 = b
print("Максимальная цифра равна ", max1, sep = '')
print("Минимальная цифра равна ", min1, sep = '')'''

# одинаковые числа
'''
a = int(input())
b = a % 10
d = 0
f = 0
while a > 0:
    c = a % 10
    a = a // 10
    if b != c:
        f = 1
    else:
        d = 1
if f == 1:
    print("NO")
elif d == 1:
    print("YES")'''
    
