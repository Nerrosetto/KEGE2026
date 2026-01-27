from string import printable as pri
from itertools import product as pro

cnt = 0
for val in pro(pri[:9], repeat=7):
    val = ''.join(val)
    flag1 = False
    flag2 = False
    if val[0] != '0':
        for i in pri[1:9:2]:
            if val[0] == i:
                flag1 = True
        for i in pri[:9:2]:
            if val[-1] == i:
                flag2 = True
        if flag1 == False and flag2 == False and val.count('8') == 1:
            cnt += 1
print(cnt)
