from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:7], repeat=5):
    i = ''.join(i)
    u1 = True
    for d in range(1, 5):
        if i[d] == i[d - 1]:
            u1 = False
    if i.count('6') == 1 and u1 and i[0] != '0':
        cnt += 1
print(cnt)
