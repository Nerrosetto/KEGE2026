from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:13], repeat=6):
    i = ''.join(i)
    if i[0] != '0' and i.count('0') >= 2:
        for t in pri[10:13]:
            i = i.replace(t, '*')
        if '**' in i and i.count('*') == 2:
            cnt += 1
print(cnt)
