from string import printable as al


def convert(num, sys):
    res = ''
    while num:
        res += al[num % sys]
        num //= sys
    return res[::-1]


res = []
cou = 0
for x in range(0, 2401):
    num = convert(7 * 9 ** 210 + 6 * 9 ** 110 - x, 9)
    if num.count('0') == 100:
        res.append(x)
print(max(res))
