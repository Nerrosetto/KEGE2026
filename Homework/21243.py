from string import printable as pri
def f(N, sys):
    a = ''
    while N:
        a += pri[int(N)%sys]
        N //= sys
    return a[::-1]

ans = []
for N in range(1,99999):
    R = f(N,5)
    if sum(map(int, R)) % 5 == 0:
        R = R.replace('0', '!').replace('1','0').replace('!','1')
        R += '14'
    else:
        R += '33'
        R = '44' + R[1:]
    R = int(R,5)
    if R >= 370:
        ans.append([R, N])
print(min(ans)[1])