from itertools import product as pro

cnt = 0
flag = False
for val in pro(sorted('МАСЛО'), repeat=6):
    val = ''.join(val)
    for i in 'АО':
        val = val.replace(i, '*')
    if val.count('*') == 1:
        cnt += 1
print(cnt)
