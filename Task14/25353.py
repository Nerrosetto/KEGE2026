from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


for x in range(1, 27000):
    num = convert(3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x, 27)
    if num.count('0') == 6:
        print(x)
        break
