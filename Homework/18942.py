from itertools import product as pro

cnt = 0
for val in pro('ДИОНСЙ', repeat=6):
    res = []
    ch = []
    val = ''.join(val)
    if val.count('Д') + val.count('Н') == 1:
        res.append(True)
    else:
        res.append(False)
    for i in val:
        ch.append(i * 2)
    for i in ch:
        if i not in val:
            res.append(True)
        else:
            res.append(False)
    if res.count(False) == 0:
        cnt += 1
print(cnt)
