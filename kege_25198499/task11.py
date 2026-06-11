from math import ceil, log2

i = ceil(log2(10 + 52 + 500))
for L in range(1, 10000):
    if L * i * 45877 >= 49 * 2 ** 23:
        print(L)
        break
