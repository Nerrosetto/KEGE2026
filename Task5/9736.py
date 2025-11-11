maxi = 0
for N in range(1, 5000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    if int(R, 2) <= 170:
        if maxi < int(R, 2):
            maxi = int(R, 2)
print(maxi)
