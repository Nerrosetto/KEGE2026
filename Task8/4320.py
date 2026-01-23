from string import printable as pri
from itertools import product as pro

cnt = 0
for x in pro(pri[:8], repeat=6):
    x = ''.join(x)
    if len(x) == len(set(x)) and x[0] != '0':
        if int(x, 8) % 5 == 0:
            for i in pri[:8:2]:
                x = x.replace(i, '*')
            for i in pri[1:8:2]:
                x = x.replace(i, '!')
            if '**' not in x and '!!' not in x:
                cnt += 1
print(cnt)
