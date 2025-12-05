from itertools import product as pro

alph = sorted('СОЛНЦЕ')
cnt = 0
for pos, val in enumerate(pro(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'ОЕ' and val.count('Ц') == 2 and pos % 2 == 0:
        cnt += 1
print(cnt)
