from itertools import product as pro

for pos, i in enumerate(pro(sorted('ПОЛЕНИЦА'), repeat=5), start=1):
    i = ''.join(i)
    if 'А' not in [i[0], i[-1]] and i.count('Л') >= 3 and pos % 2 != 0:
        print(pos)
        break
