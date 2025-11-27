res = []
for N in range(1, 99999):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += bin(R.count('1'))[2:]
    else:
        R = '1' + R + '101'
    if int(R, 2) > 350:
        res.append(N)
print(min(res))
