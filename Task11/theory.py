from math import log2, ceil

# I = L * i, где I- вес одного идентификатора, L- длина идентификатора, i- вес символа.

# 1855

L = 101
N = 10 + 4090
i = ceil(log2(N))  # bit (бит)
I = L * i
I = ceil(I / 8)  # Переводим в byte (байт).
print(int(2048 * I / 1024))  # 1024- Перевод из байт к килобайт.

# 23270
N = 10 + 27
i = ceil(log2(N))
for L in range(1, 10 ** 9):
    I = L * i
    I = ceil(I / 8)
    if 3548 * I > 12 * 2 ** 10:
        print(L)
        break

print('_' * 40)

# 23195
L = 172
for i in range(1, 10 ** 9):
    I = L * i
    I = ceil(I / 8)
    if 356984 * I >= 54 * 2 ** 20:
        print(2 ** (i - 1) + 1)
        break
# ЛИБО:
for N in range(1, 10 ** 10):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 356984 * I >= 54 * 2 ** 20:
        print(N)
        break
