from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:9], repeat=5):
    if i[0] != '0':
        i = ''.join(i)
        for t in pri[1:9:2]:
            i = i.replace(t, '*')
        if i.count('0') == 1:
            if '*0' not in i and '0*' not in i:
                cnt += 1
print(cnt)
