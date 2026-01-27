from string import printable as pri


def convert(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1] if a else '0'


ans = []
for x in range(0, 9999):
    num = convert(x, 4)
    if x % 2 == 0:
        num = '12' + num + convert(int(num[-1], 4) * 3, 4)
    else:
        num = '13' + num + '21'
    num = int(num, 4)
    if num > 50:
        ans.append(num)
print(min(ans))
