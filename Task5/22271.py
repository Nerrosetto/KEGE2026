from string import printable as pri


def f(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


ans = []

for N in range(1, 10000):
    R = oct(N)[2:]
    if R[0] == '5':
        R = R.replace('2', '!').replace('1', '2').replace('!', '1')
        R = '11' + R
    else:
        R = '2' + R[1:] + '10'
    if int(R, 8) < 1354:
        ans.append([R, N])
print(max(ans)[1])
