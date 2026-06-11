from itertools import product as pro
from string import printable as pri

check = 0
ans = 0
for pos, i in enumerate(pro(pri[:10], repeat=5), start=1):
    i = ''.join(i)
    if i[0] == '0':
        check += 1
    else:
        if (pos - check) % 15 == 0:
            for t in pri[:10:2]:
                i = i.replace(t, '*')
            for t in pri[1:10:2]:
                i = i.replace(t, '!')
            if '**' not in i and '!!' not in i:
                ans = pos - check
print(ans)
