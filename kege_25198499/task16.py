F = [0] * 10000
for n in range(7500):
    if n < 10:
        F[n] = n
    else:
        F[n] = 3 * n + F[n - 3]
print((F[6250] + 2 * F[6244]) / F[6238])
