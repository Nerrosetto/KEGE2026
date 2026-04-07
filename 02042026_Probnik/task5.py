from string import printable as pri


def f(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


ans = []
for N in range(1, 99999):
    R = f(N, 4)
    if N % 4 == 0:
        R += R[:2]
    else:
        R += f(N % 4 * 4, 4)
    R = int(R, 4)
    if R > 291:
        ans.append(R)
print(min(ans))
