from itertools import product as pro

res = []
for pos, val in enumerate(pro(sorted('ГРАНИТ'), repeat=6), start=1):
    val = ''.join(val)
    ch_2 = []
    if pos % 2 != 0:
        for i in 'АИГ':
            if val[0] != i:
                ch_2.append(True)
            else:
                ch_2.append(False)
        if ch_2.count(False) == 0:
            if val.count('А') == 1:
                res.append(pos)
print(res[0])
