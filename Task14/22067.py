from string import printable as pri


def f(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


x = f(3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2, 17)
for i in pri[1:17:2]:
    x = x.replace(i, '')
print(len(set(x)))
