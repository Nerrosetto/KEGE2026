from string import printable as al


def convert(num, sys):
    res = ''
    while num:
        res += al[num % sys]
        num //= sys
    return res[::-1]


res = []
cou = 0
for x in range(0, 3001):
    num = convert(9 * 11 ** 210 + 8 * 11 ** 150 - x, 11)
    if num.count('0') == 60:
        res.append(x)
print(max(res))
