from string import printable as pri
from itertools import product as pro


cnt = 0
for val in pro(pri[:6], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('2') == 1:
            for i in pri[:6:2]:
                if i != '2':
                    val = val.replace(i, '!')
            if '!2' not in val and '2!' not in val:
                cnt += 1
print(cnt)
