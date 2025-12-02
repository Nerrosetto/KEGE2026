from itertools import product as pro

res = []
alph = sorted('ФОКУС')
for pos, val in enumerate(pro(alph, repeat=5), start=1):
    val = ''.join(val)
    if 'Ф' not in val and val.count('У') == 2:
        res.append(pos)
print(res[-1])
