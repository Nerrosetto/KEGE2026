from string import printable as pri


def f(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


maxi = -1
for x in range(9430):
    num = f(39 ** 483 + 39 ** 235 - x, 39)
    if num.count('0') > maxi:
        maxi = num.count('0')

print(maxi)
