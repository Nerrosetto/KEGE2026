from itertools import product as pro

for val, i in enumerate(pro(sorted('НРТУ'), repeat=4), start=1):
    i = ''.join(i)
    if val == 215:
        print(i)