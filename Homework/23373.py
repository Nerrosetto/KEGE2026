from string import printable as al


def convert(num, sys):
    res = ''
    while num:
        res += al[num % sys]
        num //= sys
    return res[::-1]


num = convert(2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 21 - 35, 49)
cou = 0
for i in num:
    if al.index(i) <= 9:
        cou += 1
print(cou)
