from itertools import product as pro

alph = sorted('АВТОР')
for pos, val in enumerate(pro(alph, repeat=4), start=1):
    val = ''.join(val)
    if val == 'ВАТА':
        print(pos)
        break
