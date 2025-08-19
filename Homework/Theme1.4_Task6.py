import math

print('Введите 1 или 2')
print('1 - Вычисление площади круга')
print('2 - Вычисление  площади эллипса')
inp = int(input())
if inp == 1 or inp == 2:
    print('Введите радиус окружности: ' if inp == 1 else 'Введите длину большей и малой полуоси эллипса: ')
    if inp == 1:
        num = int(input())
        print('Площадь круга равна: ', num * math.pi ** 2)
    else:
        num1 = int(input())
        num2 = int(input())
        print('Площадь эллипса равна: ', math.pi * num1 * num2)
else:
    print('Попробуйте снова.')
