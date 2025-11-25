from string import printable as al


def convert(num, sys):
    res = ''
    while num:
        res += al[num % sys]
        num //= sys
    return res[::-1]

res = []
for x in range(1, 2031):
    num = convert(3 ** 100 - x,3)
    if num.count('0') == 1:
        res.append(x)
print(max(res))