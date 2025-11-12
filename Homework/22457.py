from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 20000):
    R = convert(N, 7)
    if sum(map(lambda x: int(x, 7), R)) % 2 == 0:
        R += '555'
    else:
        R = '33' + R + '6'
    if int(R,7) < 12717:
        ans.append(N)
print(max(ans))