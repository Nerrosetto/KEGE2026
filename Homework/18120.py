from itertools import product as pro

cnt = 0
for pos, val in enumerate(pro(sorted('ПРЕСТОЛ'), repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and ('Е' == val[-1] or 'О' == val[-1]) and val.count('П') + val.count('Р') + val.count('С') + val.count('Т') + val.count('Л') <= 3:
        cnt += 1
print(cnt)
