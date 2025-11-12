from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 20000):
    count = 0
    R = convert(N, 8)
    for i in range(len(R)):
        if int(R[i]) % 2 == 0:
            count += 1
    if count % 2 == 0:
        R = convert(N % 8 * 5, 8) + R
    else:
        R = R[:-3] + '46' + R[-3:]
    if N >= 80:
        ans.append(int(R,8))
print(min(ans))