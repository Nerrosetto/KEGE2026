from string import printable as pri


def conv(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1] if a else 0


cnt = 0
num = conv(2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024, 27)
for i in num:
    a = [x for x in pri[:10]]
    if i not in a:
        cnt += 1
print(cnt)
