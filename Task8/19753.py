from itertools import permutations as per
from string import printable as pri

cnt = 0
for val in per(pri[:10], r=6):
    val = ''.join(val)
    res = []
    num = 0
    if val[0] != '0' and int(val) % 4 == 0:
        for i in '02468':
            val = val.replace(i, '*')
        if '**' not in val:
            cnt += 1
print(cnt)
