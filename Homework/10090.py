from string import printable as pri
from itertools import product as pro

cnt = 0
for val in set(pro(pri[:8], repeat=5)):
    val = ''.join(val)
    if val.count('1') == 0 and val[0] != '0' and len(val) == len(set(val)):
        for i in pri[:8:2]:
            val = val.replace(i, '!')
        for i in pri[1:8:2]:
            val = val.replace(i, '+')
        if '!!' not in val and '++' not in val:
            cnt += 1
print(cnt)
