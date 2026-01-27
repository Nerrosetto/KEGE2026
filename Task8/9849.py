from string import printable as pri
from itertools import product as pro

cnt = 0
for val in set(pro(pri[10:16], repeat=6)):
    val = ''.join(val)
    flag = False
    for i in 'ae':
        if val[0] == i or val[-1] == i:
            flag = True
    if flag == False:
        cnt += 1
print(cnt)
