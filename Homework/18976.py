from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:20], repeat=5):
    res = []
    val_2 = val
    val = ''.join(val)
    if val[0] != '0':
        for i in pri[:20:2]:
            val = val.replace(i, '*')
        for i in pri[1:20:2]:
            val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            if int(val_2[0], 20) + int(val_2[-1], 20) == 26:
                cnt += 1
print(cnt)
