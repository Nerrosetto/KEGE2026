from string import printable as pri
from itertools import product as pro


def con(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


cnt = 0
for val in pro(pri[:7], repeat=5):
    val = ''.join(val)
    u1 = sum(val.count(str(i)) for i in range(3, 6)) == 2
    if u1:
        u2 = []
        for i in pro(set(val)):
            if i[0] * 2 not in val:
                u2.append(True)
            else:
                u2.append(False)
        if all(u2):
            cnt += 1
print(cnt)
