from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0' and val.count(val[0]) == 1 and val.count(val[1]) == 1 and val.count(val[2]) == 1 and len(
            set(val)) == 3:
        for i in pri[:16:2]:
            val = val.replace(i, '*')
        for i in pri[1:16:2]:
            val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            cnt += 1
print(cnt)
