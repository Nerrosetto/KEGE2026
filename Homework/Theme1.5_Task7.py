flag = 0
inp1 = int(input('Введите первое число: '))
inp2 = int(input('Введите второе число: '))
if inp1 and inp2 != 0:
    while flag == 0:
        if inp1 > inp2 and inp1 % inp2 == 0:
            flag += 1
        elif inp2 > inp1 and inp2 % inp1 == 0:
            flag += 1
        else:
            inp1 /= inp2
            inp2 /= inp1
    if inp1 and inp2 < 0:
        print('Нет НОД.')
    else:
        print('НОД: ', inp1 if inp1 < inp2 else inp2)
else:
    print('Одно из чисел равно 0.')
