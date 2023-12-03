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
