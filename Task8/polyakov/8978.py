from itertools import product as pro

ans = 0
for pos, i in enumerate(pro(sorted('ЦИТРУС'), repeat=5), start=1):
    i = ''.join(i)
    if i.count('И') == 2 and i.count('ЦЦ') == 0:
        ans = pos
print(ans)
