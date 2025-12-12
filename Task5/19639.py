res = []
for N in range(1, 99999):
    R = bin(N)[2:]
    for i in R:
        if R[0] == '0':
            R = R[1:]
    if R.count('0') % 2 == 0:
        R = '1' + R + '1'
    else:
        R = '10' + R
    R = int(R, 2)
    if R < 100:
        res.append(R)
print(max(res))
