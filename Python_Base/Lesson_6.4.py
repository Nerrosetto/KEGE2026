from math import pi

Height = float(input('Введите высоту: '))
Rad = float(input('Введите радиус: '))
S_side = 2 * pi * Rad * Height
S_base = pi * Rad**2
print('Площадь поверхности цилиндра: ', S_side + S_base * 2)
