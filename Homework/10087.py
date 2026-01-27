ans = []
for N in range(1, 20000):
    R = bin(N)[2:]
    if len(R) >= 3:
        if N % 3 == 0:
            R += R[-3]
        else:
            R += bin((N % 3) * 3)[2:]
    R = int(R, 2)
    if R > 151:
        print(R)
        break
