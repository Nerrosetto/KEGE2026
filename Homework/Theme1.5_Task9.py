inp1 = int(input('Введите число: '))
inp2 = int(input('Введите число: '))
n = 1
while n != 10:
    n += 1
    if inp1 % n == 0 or inp2 % n == 0:
        break
if n == 10:
    print('Числа взаимно простые.')
else:
    print('Числа не взаимно простые.')