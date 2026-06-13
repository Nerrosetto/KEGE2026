from string import printable as pri


def perev(N, sys):
    R = ''
    while N:
        R += pri[N % sys]
        N //= sys
    return R[::-1]


ans = []
for N in range(10, 9999):
    R = perev(N, 3)
    if N % 4 == 0:
        R += R[-3:]
    else:
        R = '1' + R + '20'
    R = int(R, 3)
    if R > 423:
        ans.append(R)
print(min(ans))
