from string import printable as pri
from itertools import product as pro

cnt = 0
for val in pro(pri[:14], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if len(set(val)) == 2 and val[-1] in '03':
            cnt += 1
print(cnt)
