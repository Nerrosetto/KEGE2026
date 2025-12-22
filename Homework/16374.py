from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:7], repeat=7):
    ch = 0
    if val[0] != '0':
        for i in '0246':
            ch += val.count(i)
    if ch == 2:
        cnt += 1
print(cnt)
