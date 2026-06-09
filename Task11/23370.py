from math import ceil, log2

# решается правильно только с помощью кода.
N = 10 + 17
i = ceil(log2(N))
for L in range(1, 10 ** 10):
    I = ceil(L * i / 8)
    if I * 7564230 > 31 * 2 ** 20:
        print(L)
        break
