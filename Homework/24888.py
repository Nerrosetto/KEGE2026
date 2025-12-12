from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1:
        res = []
        if val[0] != val[1] != val[2] != val[3]:
            cnt += 1
print(cnt)
