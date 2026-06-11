from string import printable as pri


def perev(num, sys):
    a = ''
    while num:
        a += pri[num % sys]
        num //= sys
    return a[::-1]


ans = []
for x in range(1, 3000):
    num = perev(12 * 19 ** 12 + 9 * 19 ** 9 + 5 * 19 ** 5 - x, 19)
    if num.count('0') % 2 == 0:
        ans.append(x)
print(sum(ans))

# ИЛИ:
ans = []
for x in range(1, 3000):
    num = 12 * 19 ** 12 + 9 * 19 ** 9 + 5 * 19 ** 5 - x
    cnt_0 = 0
    while num:
        if num % 19 == 0:
            cnt_0 += 1
        num //= 19
    if cnt_0 % 2 == 0:
        ans.append(x)
print(sum(ans))
