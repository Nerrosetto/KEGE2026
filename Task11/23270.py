from math import ceil, log2

i = ceil(log2(10 + 27))
for L in range(1, 10 ** 10):
    I = ceil(L * i / 8)
    if I * 3548 > 12 * 2 ** 10:
        print(L)
        break
