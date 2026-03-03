from math import *

L = 261
I = ceil(31 * 2 ** 23 / 252500)
i = ceil(I / L)
print(2 ** (i - 1) + 1)
