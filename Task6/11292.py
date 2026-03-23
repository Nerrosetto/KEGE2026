from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:16], repeat=5):
    i = ''.join(i)
    if i[0] != '0':
        if i.count('6') == 2:
            for t in pri[:16:2]:
                if t != '6':
                    i = i.replace(t, '*')
            if all(('*6' not in i, '6*' not in i, '66' not in i)):
                cnt += 1
print(cnt)
