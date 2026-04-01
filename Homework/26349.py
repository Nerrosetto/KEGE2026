from itertools import product as pro

for pos, val in enumerate(pro(sorted('СУЛАК'), repeat=6), start=1):
    val = ''.join(val)
    if (val[0] == 'Л' or val[0] == 'С') and sum(
            [val.count(i) for i in
             'УА']) <= 2 and 'УА' not in val and 'АУ' not in val and pos % 2 == 0 and pos == 12368:
        print(len(val))
        break
