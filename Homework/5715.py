from itertools import product as pro

cnt = 0
for val in pro(sorted('ПКБ'), repeat=15):
    val = ''.join(val)
    if val.count('К') > val.count('П') > val.count('Б'):
        cnt += 1
print(cnt)
