from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


res = []
for x in range(3, 999):
    num = 3 * 7 ** (x + 1) + 13 * 7 ** (x + 2) + 31 * 7 ** (3 * x) + 1 * 7 ** (2 * x)
    num = convert(num, 7)
    if sum(map(int, num)) == 18:
        res.append(x)
print(min(res))
