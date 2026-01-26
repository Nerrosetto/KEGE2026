from itertools import product as pro

alph = sorted('ШКОЛА')
for pos, val in enumerate(pro(alph, repeat=5), start=1):
    val = ''.join(val)
    if val == 'ШАЛАШ':
        print(pos)
