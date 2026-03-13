from string import printable as pri


def pere(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


ans = []
for N in range(1, 1000000):
    R = pere(N, 3)
    if N % 3 != 0:
        R += pere((N % 3) * 5, 3)
    R = int(R, 3)
    if R > 146:
        ans.append(N)

print(min(ans))
