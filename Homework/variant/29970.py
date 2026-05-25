F = [0] * 38000
G = [0] * 38000
for n in range(1, 37900):
    if n <= 20:
        G[n] = n + 2
    else:
        G[n] = G[n - 3] + 1
for n in range(3, 37900):
    F[n] = 3 * G[n - 3] + 7
print(F[37811])
