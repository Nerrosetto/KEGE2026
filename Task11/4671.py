from math import *

L = 32
i = int(log2(10 + 63)) + 1
I = L * i
print(int(I * 3840 / 2 ** 13))
