from string import printable as al


def convert(num, sys):
    a = ''
    while num:
        a += al[num % sys]
        num //= sys
    return a[::-1]


for x in range(1, 100):
    num1 = 7 * 100 ** 6 + 10 * 100 ** 5 + x * 100 ** 4 + 0 * 100 ** 3 + 1 * 100 ** 2 + 2 * 100 ** 1 + 3 * 100 ** 0
    num2 = 1 * 100 ** 5 + 11 * 100 ** 4 + 10 * 100 ** 3 + 6 * 100 ** 2 + 4 * 100 ** 1 + x * 100 ** 0
    num3 = x * 100 ** 6 + 9 * 100 ** 5 + 8 * 100 ** 4 + 0 * 100 ** 3 + 1 * 100 ** 2 + 2 * 100 ** 1 + 13 * 100 ** 0
    num = num1 - num2 + num3
    if num % 21 == 0:
        print(convert(x, 6), num // 21)
# 224
