from itertools import product as per
from string import printable as pri

cnt = 0
for val in per(pri[:2], repeat = 16):
    val = ''.join(val)
    if val[0] != '0' and sum(map(int, val)) % 3 == 0:
        cnt += 1
print(cnt)
