from math import ceil, log2

L = 172
for i in range(1, 10 ** 10):
    I = ceil(L * i / 8)
    if I * 356984 > 54 * 2 ** 20:
        print(2 ** (i - 1) + 1)
        break
