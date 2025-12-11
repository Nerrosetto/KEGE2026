from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:16], repeat=4):
    val = ''.join(val)
    if val.count('3') == 1 and val[0] != '0':
        res = []
        for i in [str(i) * 2 for i in range(0, 10)]:
            if i not in val:
                res.append(True)
            else:
                res.append(False)
        if res.count(False) == 0:
            cnt += 1
print(cnt)
