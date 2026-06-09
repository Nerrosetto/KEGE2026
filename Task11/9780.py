from math import *

L = 25
i = int(log2(26)) + 1  # 26- мощность алфавита
I = L * i  # длина строки * вес символа
print(int(I / 8 * 35) + 1)
