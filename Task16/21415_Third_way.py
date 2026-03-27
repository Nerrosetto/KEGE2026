F = [0] * 2200

for n in range(2200):
    if n <= 5:
        F[n] = 1
    else:
        F[n] = n + F[n - 2]

print(F[2126] - F[2122])
