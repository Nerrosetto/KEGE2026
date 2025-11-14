from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100000):
    count = 0
    R = convert(N, 4)
    b = [*map(str, R)]
    if R[0] == 3:
        for i in range(len(R)):
            if R[i] == 3:
                b[i] = 1
            if R[i] == 1:
                b[i] = 3
        R = b
        R = str(R) + '21'
    else:
        R = '1' + R[1:] + '12'
    if int(R, 4) < 598:
        ans.append(N)
print(max(ans))
