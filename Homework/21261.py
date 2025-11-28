from string import printable as al


def convert(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


# res_N = []
# res_R = []
ans = []
min_R = 10 ** 100
for N in range(1, 99999):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R.replace('0', 'a')
        R.replace('2', '0')
        R.replace('a', '2')
        R = '32' + R
    else:
        R += '33'
        R = R[:1] + '1' + '0' + R[3:]
    R = int(R, 4)
    if R == 335:
        ans.append(N)
print(max(ans))
#        res_N.append(N)
#        res_R.append(R)
# min_R = min(res_R)
# for i in range(len(res_R)):
#    if res_R[i] == min_R:
#        ans.append(res_N[i])
# print(max(ans))
