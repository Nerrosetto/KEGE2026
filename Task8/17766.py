from itertools import product as pro

res = []
for pos, val in enumerate(pro(sorted('СЕНТЯБРЬ'), repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'Р' and val.count('Ь') == 0:
        res.append(pos)
print(res[-1])
