from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:5], repeat=9):
    i = ''.join(i)
    if i[0] != '0':
        for t in pri[:5:2]:
            i = i.replace(t, '*')
        if i.count('**') == 2 and '***' not in i:
            cnt += 1
print(cnt)
