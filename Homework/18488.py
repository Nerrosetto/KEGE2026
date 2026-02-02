from string import printable as pri


def conv(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1] if a else 0


for x in range(1, 1000):
    num = conv(7 ** 666 + 7 ** 333 + 49 ** x - 343, 7)
    if num.count('6') == 49:
        print(x)
        break
