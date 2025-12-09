from itertools import product as pro
from string import printable as pri

cnt = 0
for val in pro(pri[:8], repeat=5):
    val = ''.join(val)
    if val.count('7') <= 2 and val[0] != '0' and val[-1] not in '26' and val[0] not in [str(i) for i in pri[:8] if
                                                                                        int(i, 8) % 2 != 0]:
        cnt += 1
print(cnt)
