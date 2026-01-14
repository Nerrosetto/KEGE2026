from string import printable as pri
from itertools import product as pro

cnt = 0
for val in pro(pri[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('9') == 1:
            for i in pri[:16:2]:
                val = val.replace(i, '!')
            for i in pri[1:16:2]:
                val = val.replace(i, '-')
            if '!!' not in val and '--' not in val:
                cnt += 1
print(cnt)
