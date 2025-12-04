def convert(num, sys):
    a = ''
    while num:
        a += str(num % sys)
        num //= sys
    return a[::-1]


res = []
ans = []
maxi = -1
for N in range(1, 9999):
    R = convert(N, 5)
    if R[-1] == '0':
        R = R.replace('1', 'a').replace('4', '1').replace('a', '4')
        R = '33' + R
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R < 1922:
        res.append([R, N])
        if maxi < R:
            maxi = R
for i in res:
    if i[0] == maxi:
        ans.append(i[1])
print(min(ans))
