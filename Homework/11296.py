from itertools import product as pro

res = []
al = sorted('ДОСЖ')
for pos, num in enumerate(pro(al, repeat=6), start=1):
    num = ''.join(num)
    if num[:2] == 'ЖС':
        print(pos)
        break
