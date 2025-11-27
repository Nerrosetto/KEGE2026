from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


res = []
res1 = []
a = 10**100
for N in range(3, 99999):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R.replace('0', 'a')
        R.replace('2', '0')
        R.replace('a', '2')
        R = '32' + R
    else:
        R += '33'
        R.replace(R[2], '1')
        R.replace(R[3], '0')
    R = int(R, 4)
    if R > 320:
        res.append(N)
