from string import printable as pri

ans = 0
for x in range(1, 9431):
    num = 39 ** 483 + 39 ** 235 - x
    a = ''
    while num:
        a += pri[num % 39]
        num //= 39
    a = a[::-1]
    ans = max(ans, a.count('0'))
print(ans)
