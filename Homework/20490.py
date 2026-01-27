from string import printable as pri


def f(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


ans = []
for x in range(1, 2006):
    num = f(4 ** 163 * 5 + 12 ** 62 - x, 5)
    if num.count('1') < num.count('4'):
        ans.append(x)
print(max(ans))
