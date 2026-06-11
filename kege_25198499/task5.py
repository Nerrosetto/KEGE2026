from string import printable as pri


def perev(num, sys):
    a = ''
    while num:
        a += pri[num % sys]
        num //= sys
    return a[::-1]


ans = []
for N in range(1, 999999):
    R = perev(N, 3)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += perev(N % 3 * 4, 3)
    R = int(R, 3)
    if R < 100:
        ans.append(N)
print(max(ans))
