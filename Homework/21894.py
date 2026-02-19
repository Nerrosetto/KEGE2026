from string import printable as pri
from itertools import product as pro

cnt = 0
for i in pro(pri[:10], repeat=4):
    i = ''.join(i)
    if i[0] != '0' and len(set(i)) == len(i):
        for t in pri[:10:2]:
            i = i.replace(t, '*')
        for t in pri[1:10:2]:
            i = i.replace(t, '!')
        if '**' not in i and '!!' not in i:
            cnt += 1
print(cnt)
