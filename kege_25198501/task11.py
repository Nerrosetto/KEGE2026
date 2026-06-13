from math import ceil, log2

L = 377
I = ceil(5536 * 2 ** 13 / 23155)
print(2 ** (ceil(I / L) - 1) + 1)
