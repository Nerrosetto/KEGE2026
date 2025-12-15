from itertools import product as per
from string import printable as pri

cnt = 0
for val in set(per(pri[:12], repeat=7)):
    val = ''.join(val)
    if val[0] != '0' and val.count('b') == 2:
        for i in pri[:12:2]:
            val = val.replace(i, '*')
        for i in pri[1:12:2]:
            val = val.replace(i, '+')
        for i in ['**', '++']:
            if i not in val:
                cnt += 1
print(cnt)
