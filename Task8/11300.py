from itertools import product as pro

alph = sorted('ГОНДУБШ')
res = []
for pos, val in enumerate(pro(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] != 'Б' and val.count('У') == 0 and val.count('Н') >= 2:
        res.append(pos)
print(res[-1])
