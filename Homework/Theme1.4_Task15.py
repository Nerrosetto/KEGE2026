from math import sqrt
a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))
if a != 0:
    D = sqrt(b**2 - 4*a*c)
    x1 = (-b-D)/a*2
    x2 = (-b+D)/a*2
    print(x1, x2)
    print(sqrt(x1), sqrt(x2))
