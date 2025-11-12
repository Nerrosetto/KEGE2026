a = []
for N in range(1,100000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11'
    if int(R,2) > 225:
        a.append(int(R,2))
print(min(a))