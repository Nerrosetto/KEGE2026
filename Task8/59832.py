from string import printable as pri
from itertools import product as pro

cnt = 0
for i in pro(pri[:9], repeat=5):
    i = ''.join(i)
    if i[0] != '0' and i.count('3') == 2:
        for t in pri[1:9:2]:
            i = i.replace(t, '*')
        if '*2' not in i and '2*' not in i:
            cnt += 1
print(cnt)
