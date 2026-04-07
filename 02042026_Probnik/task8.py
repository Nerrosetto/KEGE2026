from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:7], repeat=7):
    i = ''.join(i)
    if i[0] not in '035':
        if sum(i.count(t) >= 1 for t in ['22', '44']) < 2:
            cnt += 1
print(cnt)
