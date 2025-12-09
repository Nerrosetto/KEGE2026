def convert(num, sys):
    a = ''
    while num:
        a += str(num % sys)
        num //= sys
    return a[::-1]


ans = []
for N in range(1, 999999):
    R = convert(N, 9)
    if R[0] == '7':
        R = R.replace('6', '*').replace('3', '6').replace('*', '3')
        R = '34' + R
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R < 2876:
        ans.append([R, N])
a = max(ans)
res = []
for i in range(len(ans)):
    if ans[i][0] == a[0]:
        res.append(ans[i][1])
print(max(res))
