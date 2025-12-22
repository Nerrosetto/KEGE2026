from itertools import permutations as pro

cnt = 0
for val in set(pro('АМФИБРАХИЙ')):
    if 'ИИФАА' in val or 'ААФИИ' in val:
        cnt += 1
print(cnt)
