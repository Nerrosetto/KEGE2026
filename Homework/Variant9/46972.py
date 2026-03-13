from string import printable as pri


def pere(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


num = pere(5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98, 7)
ans = []
for i in num:
    ans.append([num.count(i), i])
print(max(ans))
