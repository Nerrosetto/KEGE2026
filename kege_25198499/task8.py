from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:7], repeat=5):
    i = ''.join(i)
    for d in range(1, 5):
        if i[d] == i[d - 1]:
            continue
    if i.count('6') == 1:
        cnt += 1
print(cnt)
