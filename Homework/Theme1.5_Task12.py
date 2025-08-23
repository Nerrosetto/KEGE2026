num1 = 0
num2 = 0
num3 = 0
inp = int(input('Введите трёхзначное число: '))
if 99 < inp < 1000:
    num1 = inp % 10
    num2 = inp // 10 % 10
    num3 = inp // 100
    if num1 != 0 and num2 != 0 and num3 != 0:
        print(num1 * num2 * num3)
    else:
        print(num1 + num2 + num3)
else:
    print('Введите другое число.')
