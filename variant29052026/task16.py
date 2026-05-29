F = [0] * 20000
G = [0] * 20000

for n in range(1, 16000):
    if n < 10:
        G[n] = 2 * n
    else:
        G[n] = G[n - 2] + 1
for n in range(1, 16000):
    F[n] = 2 * (G[n - 3] + 8)
print(F[15548])
