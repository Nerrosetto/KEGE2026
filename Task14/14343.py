from string import printable as pri


def conve(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


num = conve(5 * 343 ** 2031 + 4 * 49 ** 2142 - 3 * 7 ** 111 + 7 ** 222, 7)
print(sum(map(int, num)))
