from string import printable as pri
from itertools import product as pro

cnt = 0
for val in pro(pri[:12], repeat=7):
    ans = ''
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if int(i, 12) % 3 == 0:
                ans += '*'
            else:
                ans += '-'
        if '++' not in ans and '--' not in ans:
            cnt += 1
print(cnt)
