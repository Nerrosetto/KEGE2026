from string import printable as pri


def perev(num, sys):
    a = ''
    while num:
        a += pri[num % sys]
        num //= sys
    return a[::-1]


ans = []
for N in range(166, 9999):
    R = perev(N, 3)
    a = sum(int(i) for i in R)
    if a % 9 == 0:
        R += '2'
    else:
        R += perev(a % 9, 3)
    if N > 166:
        ans.append(int(R, 3))
print(min(ans))
