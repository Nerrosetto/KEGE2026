from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:15], repeat=5):
    val = ''.join(val)
    if val.count('8') == 1 and val[0] != '0':
        cnt_2 = 0
        for i in val:
            if int(i, 15) > 9:
                cnt_2 += 1
        if cnt_2 >= 2:
            cnt += 1
print(cnt)
print('_' * 250)
from itertools import product
from string import printable

cnt = 0
for val in product(printable[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        if len([i for i in val if int(i, 15) > 9]) >= 2:
            if [1 for i in val if int(i, 15) > 9].count(1) >= 2:
                if sum([1 for i in val if int(i, 15) > 9]) >= 2:
                    if sum([val.count(i) for i in printable[10:15]]) >= 2:
                        cnt += 1
print(cnt)
