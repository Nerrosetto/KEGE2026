from string import printable as pri


def perev(num, sys):
    a = ''
    while num:
        a += pri[num % sys]
        num //= sys
    return a[::-1]


ans = []
for x in range(1, 11500):
    num = perev(7 ** 270 + 7 ** 170 + 7 ** 70 - x, 7)
    ans.append([num.count('0'), x])
print(int(max(ans)[1]))
