from itertools import product as pro
from string import printable as pri

res = [f'{i}7' for i in range(1, 10)]
cnt = 0
for val in pro(pri[:8], repeat=10):
    val = ''.join(val)
    if val.count('7') == 5:
        for i in res:
            if i not in val:
                cnt += 1
print(cnt)
