N = int(input('Введите число меньше 100: '))
n = -2
if N < 100:
    while N:
        print(n)
        n /= -2
        if N < 0:
            N += 1
        else:
            N -= 1
else:
    print('Число больше 100.')
