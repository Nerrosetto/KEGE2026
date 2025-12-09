from itertools import product as pro

res = []
cnt = 0
for pos, val in enumerate(pro(sorted('ЯНВАРЬ'), repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'Я' and val.count('Ь') == 1 and 'ЯЯ' not in val:
        res.append(pos)
print(res[-1])
