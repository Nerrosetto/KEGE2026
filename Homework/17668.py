a = []
for N in range(1,100000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    if N > 27:
        a.append(int(R,2))
print(min(a))