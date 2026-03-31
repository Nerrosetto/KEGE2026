from string import printable as pri
from itertools import product as pro

cnt = 0
for i in pro(pri[:25], repeat=4):
    i = ''.join(i)
    a = []
    if i[0] != '0':
        a += [pri.index(t) for t in i]
        u1 = sum([a.count(q) for q in a if q % 2 == 0]) >= 1
        u2 = sum([i > 15 for i in a]) > 2
        if all((u1, u2)):
            cnt += 1
print(cnt)
