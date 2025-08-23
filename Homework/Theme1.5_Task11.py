inp = int(input('Введите число: '))
flag = 0
while inp:
    if (inp % 10) % 2 == 0:
        flag += 1
    else:
        pass
    inp //= 10
print('Количество чётных цифр: ', flag)
