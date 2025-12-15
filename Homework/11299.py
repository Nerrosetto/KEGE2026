from itertools import product as pro

res = []
for pos, val in enumerate(pro(sorted('БМЮРН'), repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'М' and 'Ю' not in val and val.count('Р') >= 2:
        res.append(pos)
print(res[-1])
