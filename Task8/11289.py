from string import printable as pri
from itertools import product as pro

cnt = 0
for val in pro(pri[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('2') == 0 and len(set(val)) == len(val):
            for i in '1357':
                val = val.replace(i, '*')
            for i in '0468':
                val = val.replace(i, '+')
            if '++' not in val and '**' not in val:
                cnt += 1
print(cnt)
