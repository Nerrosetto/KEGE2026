from itertools import product as pro, permutations as per
from string import printable as pri


def perev(x, i):
    a = ''
    while x:
        a += pri[x % i]
        x //= i
    return a[::-1]


ans = []
for N in range(1, 99999):
    R = perev(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += perev(N % 3 * 5, 3)
    R = int(R, 3)
    if R > 150:
        ans.append(R)
print(min(ans))
