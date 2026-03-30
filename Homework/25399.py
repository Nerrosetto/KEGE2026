F = [0] * 400000
G = [0] * 400000

for i in range(15, 303728 + 15)[::-1]:
    if i > 303728:
        G[i] = i - 15
    else:
        G[i] = G[i + 8] / 2 - 109

for i in range(7, 140):
    if i < 128:
        F[i] = 5 * G[i - 7] + 29
    else:
        F[i] = F[i - 5] + 1092

print(F[2049])
