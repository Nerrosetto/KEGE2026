from itertools import product as pro

res = []
cnt = 0
for pos, val in enumerate(pro(sorted('СУБЛИМАЦЯ'), repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[-1] != 'Я' and val.count('У') + val.count('И') + val.count('А') + val.count('Я') == 2:
        res.append(pos)
print(res[-1])
