from random import randint as RA

num = int(input('Введите трёхзначное число: '))
if 99 < num < 1000:
    num_random = RA(100, 999)
    print(num, num_random)
    print('Введённое число больше.' if num > num_random else 'Введённое число меньше.')
