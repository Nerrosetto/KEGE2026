from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 5000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert(N % 3 * 5, 3)
    if int(R, 3) > 133:
        ans.append(int(R, 3))
print(min(ans))
