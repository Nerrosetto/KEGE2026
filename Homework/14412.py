from itertools import product as pro

cnt = 0
for val in pro('АЛГОРИТМ', repeat=6):
    res = []
    val = ''.join(val)
    if val.count('Л') <= 1 and val[0] != 'Р':
        res.append(True)
    else:
        res.append(False)
    for i in 'ЛГРТМ':
        if val[-1] == i:
            res.append(False)
    if res.count(False) == 0:
        cnt += 1
print(cnt)
