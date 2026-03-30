from string import printable as pri


def f(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


ans = []
for x, y in zip(range(100), range(99)):
    num = f(5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x, 5)
    if int(num) > 0 and num.count('0') == 10:
        ans.append(x * y)
print(max(ans))
